#!/usr/bin/env python3
"""Rare-event estimator for the smooth regularized timing scan.

This implements the Step-16 Palm/upcrossing importance sampler for the
one-dimensional differentiable stationary Gaussian scan defined by

    J_{x,kappa}(nu) = |H_x(nu)|^2 exp[-(nu/kappa)^2]

with

    H_x(nu) = [1 - exp(-(1+i nu)x)(1+(1+i nu)x)] / (1+i nu)^2.

The estimator targets

    P(sup_{0<=t<=L} z(t) > u)

through the exact decomposition

    Q(u) + lambda_u E_up[ 1{z(0)<=u} / N_u^+ ],

where E_up is the Palm law of a randomly selected level-u upcrossing.

Important scope note:
- the selected upcrossing itself is imposed continuously through Gaussian
  conditioning on z(0)=u and z'(0)>0;
- secondary upcrossings and the left-endpoint overlap correction are counted
  on a fine local grid, so those small correction terms still have a numerical
  resolution error;
- this script is for the smooth finite-kappa surrogate from Steps 14-16, not
  the rough infinite-white-bandwidth Step-13 process.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np
from scipy.stats import norm


def H_x(nu: np.ndarray, x: float) -> np.ndarray:
    z = 1.0 + 1j * nu
    return (1.0 - np.exp(-z * x) * (1.0 + z * x)) / (z * z)


def spectral_weight(nu: np.ndarray, x: float, kappa: float) -> np.ndarray:
    return np.abs(H_x(nu, x)) ** 2 * np.exp(-(nu / kappa) ** 2)


@dataclass
class PeriodicModel:
    delta: float
    period: float
    freqs: np.ndarray
    eigenvalues: np.ndarray
    sqrt_eigenvalues: np.ndarray
    covariance: np.ndarray
    covariance_derivative: np.ndarray
    sigma_derivative: float


def build_periodic_model(
    x: float,
    kappa: float,
    delta: float,
    period_target: float = 16.0,
) -> PeriodicModel:
    n = int(round(period_target / delta))
    if n % 2:
        n += 1
    period = n * delta

    freqs = 2.0 * np.pi * np.fft.fftfreq(n, d=delta)
    eig = spectral_weight(freqs, x, kappa)

    # Normalize so covariance(0)=1.
    eig = eig / np.mean(eig)
    sqrt_eig = np.sqrt(eig)

    covariance = np.fft.ifft(eig).real
    covariance_derivative = np.fft.ifft(1j * freqs * eig).real

    sigma2 = float(np.mean((freqs**2) * eig))
    sigma = math.sqrt(sigma2)

    return PeriodicModel(
        delta=delta,
        period=period,
        freqs=freqs,
        eigenvalues=eig,
        sqrt_eigenvalues=sqrt_eig,
        covariance=covariance,
        covariance_derivative=covariance_derivative,
        sigma_derivative=sigma,
    )


def rice_upcrossing_mean(u: float, ell: float, sigma: float) -> float:
    return ell * sigma / (2.0 * np.pi) * math.exp(-0.5 * u * u)


def rice_ec_false_alarm(u: float, ell: float, sigma: float) -> float:
    return norm.sf(u) + rice_upcrossing_mean(u, ell, sigma)


def sample_palm_false_alarm(
    *,
    x: float,
    ell: float,
    kappa: float,
    u: float,
    target_delta: float = 0.005,
    period_target: float = 16.0,
    n_paths: int = 5000,
    batch_size: int = 50,
    seed: int = 0,
) -> dict[str, float]:
    """Estimate continuous false alarm via an upcrossing Palm law.

    The interval length is represented exactly by choosing an integer number of
    local steps and then setting delta=ell/n_steps. The selected Palm crossing
    is placed at the origin; a random interior location of that crossing within
    the search interval approximates the uniform crossing-time Palm measure.
    """

    rng = np.random.default_rng(seed)

    n_intervals = max(2, int(round(ell / target_delta)))
    delta = ell / n_intervals

    model = build_periodic_model(
        x=x,
        kappa=kappa,
        delta=delta,
        period_target=period_target,
    )

    n_period = len(model.freqs)
    sigma = model.sigma_derivative
    sigma2 = sigma * sigma

    lam_up = rice_upcrossing_mean(u, ell, sigma)
    q0 = float(norm.sf(u))

    offsets = np.arange(-n_intervals, n_intervals + 1)
    idx = offsets % n_period

    # Cov[z(t), z(0)] = r(t)
    c_value = model.covariance[idx]

    # Cov[z(t), z'(0)] = -r'(t)
    c_deriv = -model.covariance_derivative[idx]

    sum_w = 0.0
    sum_w2 = 0.0
    total = 0
    multiple_count = 0
    overlap_count = 0

    for start in range(0, n_paths, batch_size):
        b = min(batch_size, n_paths - start)

        white = rng.standard_normal((b, n_period))
        white_fft = np.fft.fft(white, axis=1)

        process = np.fft.ifft(
            white_fft * model.sqrt_eigenvalues[None, :], axis=1
        ).real

        derivative = np.fft.ifft(
            white_fft
            * (1j * model.freqs * model.sqrt_eigenvalues)[None, :],
            axis=1,
        ).real

        z0_uncond = process[:, 0]
        dz0_uncond = derivative[:, 0]

        # Palm slope distribution at an upcrossing: Rayleigh(scale=sigma).
        v = sigma * np.sqrt(-2.0 * np.log(rng.random(b)))

        local = (
            process[:, idx]
            + c_value[None, :] * (u - z0_uncond)[:, None]
            + (c_deriv / sigma2)[None, :] * (v - dz0_uncond)[:, None]
        )

        # Crossing time is uniform in the open interval in the continuum.
        # Grid endpoints have zero continuum measure, so sample interior grid
        # positions only.
        crossing_position = rng.integers(1, n_intervals, size=b)

        for k in range(b):
            m = int(crossing_position[k])
            left = n_intervals - m
            segment = local[k, left : left + n_intervals + 1]

            starts_above = bool(segment[0] > u)

            transitions = np.where(
                (segment[:-1] < u) & (segment[1:] > u)
            )[0]

            # The forced Palm upcrossing lies at segment index m. Remove any
            # sampled transition that represents that selected crossing and
            # add the selected crossing exactly once.
            other = np.sum((transitions < m - 1) | (transitions > m))
            n_up = 1 + int(other)

            if n_up > 1:
                multiple_count += 1
            if starts_above:
                overlap_count += 1

            weight = 0.0 if starts_above else lam_up / n_up

            sum_w += weight
            sum_w2 += weight * weight
            total += 1

    mean_up = sum_w / total
    var_up = (sum_w2 - total * mean_up * mean_up) / (total - 1)
    se_up = math.sqrt(max(var_up, 0.0) / total)

    return {
        "false_alarm": q0 + mean_up,
        "mc_standard_error": se_up,
        "endpoint_Q": q0,
        "expected_upcrossings": lam_up,
        "rice_ec_upper_bound": q0 + lam_up,
        "sigma_derivative": sigma,
        "delta": delta,
        "period": model.period,
        "fraction_multiple_upcrossings": multiple_count / total,
        "fraction_endpoint_overlap": overlap_count / total,
        "n_paths": float(total),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=float, required=True)
    parser.add_argument("--ell", type=float, required=True)
    parser.add_argument("--kappa", type=float, default=8.0)
    parser.add_argument("--u", type=float, required=True)
    parser.add_argument("--delta", type=float, default=0.005)
    parser.add_argument("--period", type=float, default=16.0)
    parser.add_argument("--paths", type=int, default=5000)
    parser.add_argument("--batch", type=int, default=50)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    result = sample_palm_false_alarm(
        x=args.x,
        ell=args.ell,
        kappa=args.kappa,
        u=args.u,
        target_delta=args.delta,
        period_target=args.period,
        n_paths=args.paths,
        batch_size=args.batch,
        seed=args.seed,
    )

    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
