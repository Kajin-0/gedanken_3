#!/usr/bin/env python3
"""Step-22 Palm-corrected boundary mapping utility.

This script extends the Step-21 finite-r Palm validator in two ways:

1. finite-r boundary mapping:
   solve representative fast/slow equality points in (Lambda, kappa_f) using
   locally iterated Palm correction factors;

2. large-r full-template bandwidth scan:
   estimate the Palm-corrected feasibility length ell_crit(kappa) and compare
   finite bandwidth against the infinite-band endpoint.

The model is the same controlled Gaussian information-band surrogate used in
Steps 15-22. It is not a literal circuit -3 dB model or hardware optimizer.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np
from scipy.optimize import brentq
from scipy.special import erfc
from scipy.stats import norm


RHO_FULL = 6.2407571
ALPHA = 1e-6
BETA = 0.90


def H_x(nu: np.ndarray, x: float) -> np.ndarray:
    z = 1.0 + 1j * nu
    return (1.0 - np.exp(-z * x) * (1.0 + z * x)) / (z * z)


def finite_moments(x: float, kappa: float, dnu: float = 0.05) -> tuple[float, float]:
    upper = max(30.0, 6.0 * kappa)
    nu = np.arange(0.0, upper + dnu, dnu)
    density = np.abs(H_x(nu, x)) ** 2 * np.exp(-(nu / kappa) ** 2)
    i0 = 2.0 * float(np.trapezoid(density, nu))
    i2 = 2.0 * float(np.trapezoid(nu * nu * density, nu))
    return i0, i2


def rho_sigma_finite(x: float, kappa: float, rho_full: float = RHO_FULL) -> tuple[float, float]:
    i0, i2 = finite_moments(x, kappa)
    rho = rho_full * math.sqrt(i0 / (math.pi / 2.0))
    sigma = math.sqrt(i2 / i0)
    return rho, sigma


def rice_allowed_ell(x: float, kappa: float, rho_full: float, alpha: float, beta: float) -> float:
    rho, sigma = rho_sigma_finite(x, kappa, rho_full)
    u = rho - float(norm.ppf(beta))
    q = float(norm.sf(u))
    if q >= alpha:
        return 0.0
    return 2.0 * math.pi * (alpha - q) * math.exp(0.5 * u * u) / sigma


@dataclass
class PalmEstimate:
    C: float
    C_se: float
    multiple_fraction: float
    endpoint_fraction: float
    delta: float


def palm_factor_finite(
    *,
    x: float,
    ell: float,
    kappa: float,
    rho_full: float,
    beta: float,
    paths: int,
    seed: int,
    target_delta: float | None = None,
    period_target: float = 10.0,
) -> PalmEstimate:
    rho, _ = rho_sigma_finite(x, kappa, rho_full)
    u = rho - float(norm.ppf(beta))

    if target_delta is None:
        target_delta = min(0.003, 0.20 / kappa)

    n_intervals = max(10, int(round(ell / target_delta)))
    delta = ell / n_intervals

    nfft = 1
    while nfft < int(math.ceil(period_target / delta)):
        nfft *= 2

    omega = 2.0 * math.pi * np.fft.fftfreq(nfft, d=delta)
    eig = np.abs(H_x(omega, x)) ** 2 * np.exp(-(omega / kappa) ** 2)
    eig /= eig.mean()

    sqrt_eig = np.sqrt(eig)
    covariance = np.fft.ifft(eig).real
    covariance_derivative = np.fft.ifft(1j * omega * eig).real
    sigma = math.sqrt(float(np.mean((omega**2) * eig)))
    sigma2 = sigma * sigma

    offsets = np.arange(-n_intervals, n_intervals + 1)
    idx = offsets % nfft
    c_value = covariance[idx]
    c_deriv = -covariance_derivative[idx]

    rng = np.random.default_rng(seed)
    sum_c = 0.0
    sum_c2 = 0.0
    multiple = 0
    overlap = 0

    batch_size = 20
    for start in range(0, paths, batch_size):
        batch = min(batch_size, paths - start)
        white = rng.standard_normal((batch, nfft))
        white_fft = np.fft.fft(white, axis=1)

        process = np.fft.ifft(white_fft * sqrt_eig[None, :], axis=1).real
        derivative = np.fft.ifft(
            white_fft * (1j * omega * sqrt_eig)[None, :], axis=1
        ).real

        slope = sigma * np.sqrt(-2.0 * np.log(rng.random(batch)))
        local = (
            process[:, idx]
            + c_value[None, :] * (u - process[:, 0])[:, None]
            + (c_deriv / sigma2)[None, :]
            * (slope - derivative[:, 0])[:, None]
        )

        crossing_position = rng.integers(1, n_intervals, size=batch)
        for j in range(batch):
            m = int(crossing_position[j])
            left = n_intervals - m
            segment = local[j, left : left + n_intervals + 1]

            starts_above = bool(segment[0] > u)
            transitions = np.where(
                (segment[:-1] < u) & (segment[1:] > u)
            )[0]
            other = int(np.sum((transitions < m - 1) | (transitions > m)))
            n_up = 1 + other

            multiple += int(n_up > 1)
            overlap += int(starts_above)
            c = 0.0 if starts_above else 1.0 / n_up
            sum_c += c
            sum_c2 += c * c

    c_mean = sum_c / paths
    c_var = (sum_c2 - paths * c_mean * c_mean) / (paths - 1)
    c_se = math.sqrt(max(c_var, 0.0) / paths)

    return PalmEstimate(
        C=c_mean,
        C_se=c_se,
        multiple_fraction=multiple / paths,
        endpoint_fraction=overlap / paths,
        delta=delta,
    )


def solve_boundary_with_fixed_C(
    *,
    kappa_fast: float,
    r: float,
    C_fast: float,
    C_slow: float,
    rho_full: float,
    alpha: float,
    beta: float,
) -> tuple[float, float]:
    def equation(X: float) -> float:
        ell_f = rice_allowed_ell(X, kappa_fast, rho_full, alpha, beta) / C_fast
        ell_s = rice_allowed_ell(X / r, r * kappa_fast, rho_full, alpha, beta) / C_slow
        return ell_f - r * ell_s

    grid = np.linspace(0.5, 18.0, 100)
    values = [equation(float(x)) for x in grid]
    roots: list[tuple[float, float]] = []

    for a, b, fa, fb in zip(grid[:-1], grid[1:], values[:-1], values[1:]):
        if fa * fb < 0.0:
            X = brentq(equation, float(a), float(b), xtol=2e-5)
            Lambda = rice_allowed_ell(X, kappa_fast, rho_full, alpha, beta) / C_fast
            if Lambda > 0.0:
                roots.append((X, Lambda))

    if not roots:
        raise RuntimeError("No positive boundary root found in search interval")

    return max(roots, key=lambda z: z[1])


def iterative_finite_r_boundary(
    *,
    kappa_fast: float,
    r: float,
    rho_full: float,
    alpha: float,
    beta: float,
    paths: int,
    iterations: int,
    seed: int,
) -> tuple[float, float, PalmEstimate, PalmEstimate]:
    X, Lambda = solve_boundary_with_fixed_C(
        kappa_fast=kappa_fast,
        r=r,
        C_fast=1.0,
        C_slow=1.0,
        rho_full=rho_full,
        alpha=alpha,
        beta=beta,
    )

    fast_est = slow_est = None
    for it in range(iterations):
        fast_est = palm_factor_finite(
            x=X,
            ell=Lambda,
            kappa=kappa_fast,
            rho_full=rho_full,
            beta=beta,
            paths=paths,
            seed=seed + 20 * it,
        )
        slow_est = palm_factor_finite(
            x=X / r,
            ell=Lambda / r,
            kappa=r * kappa_fast,
            rho_full=rho_full,
            beta=beta,
            paths=paths,
            seed=seed + 20 * it + 1,
        )
        X, Lambda = solve_boundary_with_fixed_C(
            kappa_fast=kappa_fast,
            r=r,
            C_fast=fast_est.C,
            C_slow=slow_est.C,
            rho_full=rho_full,
            alpha=alpha,
            beta=beta,
        )

    assert fast_est is not None and slow_est is not None
    return X, Lambda, fast_est, slow_est


def full_template_moments(kappa: float) -> tuple[float, float]:
    if math.isinf(kappa):
        return math.pi / 2.0, math.pi / 2.0

    q = 1.0 / kappa
    E = math.exp(q * q) * erfc(q)
    i0 = math.pi * E * (0.5 - q * q) + math.sqrt(math.pi) * q
    i2 = math.pi * E * (0.5 + q * q) - math.sqrt(math.pi) * q
    return i0, i2


def full_template_rice_ell(kappa: float, rho_full: float, alpha: float, beta: float) -> tuple[float, float]:
    i0, i2 = full_template_moments(kappa)
    rho = rho_full * math.sqrt(i0 / (math.pi / 2.0))
    u = rho - float(norm.ppf(beta))
    q = float(norm.sf(u))
    if q >= alpha:
        return 0.0, u
    sigma = math.sqrt(i2 / i0)
    ell = 2.0 * math.pi * (alpha - q) * math.exp(0.5 * u * u) / sigma
    return ell, u


def palm_factor_full_template(
    *,
    kappa: float,
    ell: float,
    rho_full: float,
    alpha: float,
    beta: float,
    paths: int,
    seed: int,
    delta: float = 0.0025,
    period_target: float = 10.0,
) -> PalmEstimate:
    _, u = full_template_rice_ell(kappa, rho_full, alpha, beta)

    n_intervals = max(10, int(round(ell / delta)))
    delta = ell / n_intervals
    nfft = 1
    while nfft < int(math.ceil(period_target / delta)):
        nfft *= 2

    omega = 2.0 * math.pi * np.fft.fftfreq(nfft, d=delta)
    eig = 1.0 / (1.0 + omega * omega) ** 2
    if not math.isinf(kappa):
        eig *= np.exp(-(omega / kappa) ** 2)
    eig /= eig.mean()

    sqrt_eig = np.sqrt(eig)
    covariance = np.fft.ifft(eig).real
    covariance_derivative = np.fft.ifft(1j * omega * eig).real
    sigma = math.sqrt(float(np.mean((omega**2) * eig)))
    sigma2 = sigma * sigma

    offsets = np.arange(-n_intervals, n_intervals + 1)
    idx = offsets % nfft
    c_value = covariance[idx]
    c_deriv = -covariance_derivative[idx]

    rng = np.random.default_rng(seed)
    sum_c = 0.0
    sum_c2 = 0.0
    multiple = 0
    overlap = 0
    batch_size = 20

    for start in range(0, paths, batch_size):
        batch = min(batch_size, paths - start)
        white = rng.standard_normal((batch, nfft))
        white_fft = np.fft.fft(white, axis=1)
        process = np.fft.ifft(white_fft * sqrt_eig[None, :], axis=1).real
        derivative = np.fft.ifft(
            white_fft * (1j * omega * sqrt_eig)[None, :], axis=1
        ).real

        slope = sigma * np.sqrt(-2.0 * np.log(rng.random(batch)))
        local = (
            process[:, idx]
            + c_value[None, :] * (u - process[:, 0])[:, None]
            + (c_deriv / sigma2)[None, :]
            * (slope - derivative[:, 0])[:, None]
        )

        crossing_position = rng.integers(1, n_intervals, size=batch)
        for j in range(batch):
            m = int(crossing_position[j])
            left = n_intervals - m
            segment = local[j, left : left + n_intervals + 1]
            starts_above = bool(segment[0] > u)
            transitions = np.where(
                (segment[:-1] < u) & (segment[1:] > u)
            )[0]
            other = int(np.sum((transitions < m - 1) | (transitions > m)))
            n_up = 1 + other
            multiple += int(n_up > 1)
            overlap += int(starts_above)
            c = 0.0 if starts_above else 1.0 / n_up
            sum_c += c
            sum_c2 += c * c

    c_mean = sum_c / paths
    c_var = (sum_c2 - paths * c_mean * c_mean) / (paths - 1)
    c_se = math.sqrt(max(c_var, 0.0) / paths)

    return PalmEstimate(
        C=c_mean,
        C_se=c_se,
        multiple_fraction=multiple / paths,
        endpoint_fraction=overlap / paths,
        delta=delta,
    )


def iterative_full_template_boundary(
    *,
    kappa: float,
    rho_full: float,
    alpha: float,
    beta: float,
    paths: int,
    iterations: int,
    seed: int,
) -> tuple[float, PalmEstimate]:
    ell_rice, _ = full_template_rice_ell(kappa, rho_full, alpha, beta)
    ell = ell_rice
    estimate = None
    for it in range(iterations):
        estimate = palm_factor_full_template(
            kappa=kappa,
            ell=ell,
            rho_full=rho_full,
            alpha=alpha,
            beta=beta,
            paths=paths,
            seed=seed + it,
        )
        ell = ell_rice / estimate.C

    assert estimate is not None
    return ell, estimate


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=["finite-r", "full-template"], default="finite-r")
    p.add_argument("--kappa", type=float, default=60.0)
    p.add_argument("--r", type=float, default=2.0)
    p.add_argument("--rho-full", type=float, default=RHO_FULL)
    p.add_argument("--alpha", type=float, default=ALPHA)
    p.add_argument("--beta", type=float, default=BETA)
    p.add_argument("--paths", type=int, default=5000)
    p.add_argument("--iterations", type=int, default=2)
    p.add_argument("--seed", type=int, default=0)
    args = p.parse_args()

    kappa = math.inf if math.isinf(args.kappa) else args.kappa

    if args.mode == "finite-r":
        X, Lambda, fast, slow = iterative_finite_r_boundary(
            kappa_fast=kappa,
            r=args.r,
            rho_full=args.rho_full,
            alpha=args.alpha,
            beta=args.beta,
            paths=args.paths,
            iterations=args.iterations,
            seed=args.seed,
        )
        print(f"X_boundary: {X}")
        print(f"Lambda_boundary: {Lambda}")
        print(f"C_fast: {fast.C}")
        print(f"C_fast_se: {fast.C_se}")
        print(f"C_slow: {slow.C}")
        print(f"C_slow_se: {slow.C_se}")
        print(f"fast_multiple_fraction: {fast.multiple_fraction}")
        print(f"slow_multiple_fraction: {slow.multiple_fraction}")
    else:
        ell, estimate = iterative_full_template_boundary(
            kappa=kappa,
            rho_full=args.rho_full,
            alpha=args.alpha,
            beta=args.beta,
            paths=args.paths,
            iterations=args.iterations,
            seed=args.seed,
        )
        print(f"ell_crit_palm: {ell}")
        print(f"C_up: {estimate.C}")
        print(f"C_up_se: {estimate.C_se}")
        print(f"multiple_fraction: {estimate.multiple_fraction}")
        print(f"endpoint_fraction: {estimate.endpoint_fraction}")


if __name__ == "__main__":
    main()
