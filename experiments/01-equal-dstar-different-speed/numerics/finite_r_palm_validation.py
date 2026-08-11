#!/usr/bin/env python3
"""Step-21 Palm validation for the finite-r common-bandwidth problem.

This script evaluates the exact continuous upcrossing-Palm identity from
Step 16 at the *available decision threshold*

    u_avail(x) = rho(x,kappa) - Phi^{-1}(beta)

for the Step-20 fixed-physics finite-r detector family.

The selected upcrossing is imposed continuously by conditioning on
z(0)=u and z'(0)>0. Secondary crossings and endpoint overlap are counted on
a fine local grid, so those small correction terms retain a controlled
resolution error.

This is not a literal circuit model. The Gaussian information weighting is
    exp[-(nu/kappa)^2].
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np
from scipy.stats import norm


RHO_FULL_DEFAULT = 6.2407571
ALPHA_DEFAULT = 1e-6
BETA_DEFAULT = 0.90


def H_x(nu: np.ndarray, x: float) -> np.ndarray:
    z = 1.0 + 1j * nu
    return (1.0 - np.exp(-z * x) * (1.0 + z * x)) / (z * z)


def finite_moments(x: float, kappa: float, dnu: float = 0.02) -> tuple[float, float]:
    upper = max(30.0, 6.0 * kappa)
    nu = np.arange(0.0, upper + dnu, dnu)
    density = np.abs(H_x(nu, x)) ** 2 * np.exp(-(nu / kappa) ** 2)
    i0 = 2.0 * float(np.trapezoid(density, nu))
    i2 = 2.0 * float(np.trapezoid(nu * nu * density, nu))
    return i0, i2


def rho_sigma(x: float, kappa: float, rho_full: float) -> tuple[float, float]:
    i0, i2 = finite_moments(x, kappa)
    rho = rho_full * math.sqrt(i0 / (math.pi / 2.0))
    sigma = math.sqrt(i2 / i0)
    return rho, sigma


@dataclass
class PeriodicModel:
    delta: float
    period: float
    freqs: np.ndarray
    sqrt_eig: np.ndarray
    covariance: np.ndarray
    covariance_derivative: np.ndarray
    sigma_derivative: float


def build_periodic_model(
    x: float,
    kappa: float,
    delta: float,
    period_target: float = 12.0,
) -> PeriodicModel:
    n_target = int(math.ceil(period_target / delta))
    nfft = 1
    while nfft < n_target:
        nfft *= 2
    period = nfft * delta

    freqs = 2.0 * math.pi * np.fft.fftfreq(nfft, d=delta)
    eig = np.abs(H_x(freqs, x)) ** 2 * np.exp(-(freqs / kappa) ** 2)
    eig = eig / eig.mean()
    sqrt_eig = np.sqrt(eig)

    covariance = np.fft.ifft(eig).real
    covariance_derivative = np.fft.ifft(1j * freqs * eig).real
    sigma = math.sqrt(float(np.mean((freqs**2) * eig)))

    return PeriodicModel(
        delta=delta,
        period=period,
        freqs=freqs,
        sqrt_eig=sqrt_eig,
        covariance=covariance,
        covariance_derivative=covariance_derivative,
        sigma_derivative=sigma,
    )


def palm_false_alarm_at_available_margin(
    *,
    x: float,
    ell: float,
    kappa: float,
    rho_full: float = RHO_FULL_DEFAULT,
    beta: float = BETA_DEFAULT,
    target_delta: float | None = None,
    period_target: float = 12.0,
    n_paths: int = 5000,
    batch_size: int = 20,
    seed: int = 0,
) -> dict[str, float]:
    rho, _ = rho_sigma(x, kappa, rho_full)
    u = rho - float(norm.ppf(beta))

    if target_delta is None:
        target_delta = min(0.0025, 0.15 / kappa)

    n_intervals = max(10, int(round(ell / target_delta)))
    delta = ell / n_intervals

    model = build_periodic_model(x, kappa, delta, period_target)
    sigma = model.sigma_derivative
    sigma2 = sigma * sigma

    offsets = np.arange(-n_intervals, n_intervals + 1)
    idx = offsets % len(model.freqs)
    c_value = model.covariance[idx]
    c_deriv = -model.covariance_derivative[idx]

    rng = np.random.default_rng(seed)

    sum_c = 0.0
    sum_c2 = 0.0
    multiple = 0
    overlap = 0

    for start in range(0, n_paths, batch_size):
        b = min(batch_size, n_paths - start)

        white = rng.standard_normal((b, len(model.freqs)))
        white_fft = np.fft.fft(white, axis=1)
        process = np.fft.ifft(
            white_fft * model.sqrt_eig[None, :], axis=1
        ).real
        derivative = np.fft.ifft(
            white_fft
            * (1j * model.freqs * model.sqrt_eig)[None, :],
            axis=1,
        ).real

        slope = sigma * np.sqrt(-2.0 * np.log(rng.random(b)))

        local = (
            process[:, idx]
            + c_value[None, :] * (u - process[:, 0])[:, None]
            + (c_deriv / sigma2)[None, :]
            * (slope - derivative[:, 0])[:, None]
        )

        crossing_position = rng.integers(1, n_intervals, size=b)

        for j in range(b):
            m = int(crossing_position[j])
            left = n_intervals - m
            segment = local[j, left : left + n_intervals + 1]

            starts_above = bool(segment[0] > u)
            transitions = np.where(
                (segment[:-1] < u) & (segment[1:] > u)
            )[0]

            other = int(np.sum((transitions < m - 1) | (transitions > m)))
            n_up = 1 + other

            if n_up > 1:
                multiple += 1
            if starts_above:
                overlap += 1

            c = 0.0 if starts_above else 1.0 / n_up
            sum_c += c
            sum_c2 += c * c

    c_mean = sum_c / n_paths
    c_var = (sum_c2 - n_paths * c_mean * c_mean) / (n_paths - 1)
    c_se = math.sqrt(max(c_var, 0.0) / n_paths)

    lam = ell * sigma / (2.0 * math.pi) * math.exp(-0.5 * u * u)
    pfa = float(norm.sf(u)) + lam * c_mean
    pfa_se = lam * c_se

    return {
        "rho": rho,
        "u_available": u,
        "sigma_derivative": sigma,
        "C_up": c_mean,
        "C_up_se": c_se,
        "false_alarm": pfa,
        "false_alarm_se": pfa_se,
        "fraction_multiple_upcrossings": multiple / n_paths,
        "fraction_endpoint_overlap": overlap / n_paths,
        "delta": delta,
        "period": model.period,
        "n_paths": float(n_paths),
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--x", type=float, required=True)
    p.add_argument("--ell", type=float, required=True)
    p.add_argument("--kappa", type=float, required=True)
    p.add_argument("--rho-full", type=float, default=RHO_FULL_DEFAULT)
    p.add_argument("--beta", type=float, default=BETA_DEFAULT)
    p.add_argument("--alpha", type=float, default=ALPHA_DEFAULT)
    p.add_argument("--delta", type=float, default=None)
    p.add_argument("--period", type=float, default=12.0)
    p.add_argument("--paths", type=int, default=5000)
    p.add_argument("--batch", type=int, default=20)
    p.add_argument("--seed", type=int, default=0)
    args = p.parse_args()

    result = palm_false_alarm_at_available_margin(
        x=args.x,
        ell=args.ell,
        kappa=args.kappa,
        rho_full=args.rho_full,
        beta=args.beta,
        target_delta=args.delta,
        period_target=args.period,
        n_paths=args.paths,
        batch_size=args.batch,
        seed=args.seed,
    )

    for key, value in result.items():
        print(f"{key}: {value}")

    print(f"false_alarm_over_alpha: {result['false_alarm'] / args.alpha}")


if __name__ == "__main__":
    main()
