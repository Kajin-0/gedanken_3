#!/usr/bin/env python3
"""Step-27 common-noise Gaussian-mollifier coupling diagnostics.

This script serves two purposes:

1. evaluate the exact deterministic/variance bounds for the coupling between
   the Brownian endpoint field B_infinity and the Gaussian-smoothed field
   B_zeta;
2. estimate H_mix(chi)-H(chi,zeta) with common random numbers, which sharply
   reduces the Monte-Carlo variance compared with subtracting independent
   Dieker-Yakir estimates.

The finite-zeta derivative field has spectral density

    exp[-omega^2/(4 zeta^2)]

and is generated from the same white-noise realization as the Brownian
endpoint by the amplitude filter

    exp[-omega^2/(8 zeta^2)].

This remains a numerical Dieker-Yakir approximation: finite path count,
finite truncation window, finite dt, and periodic FFT synthesis remain.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.optimize import brentq
from scipy.special import erf


SQRT_PI = math.sqrt(math.pi)


def f_scaled(s: np.ndarray | float) -> np.ndarray | float:
    return s * erf(s) + (np.exp(-(np.asarray(s) ** 2)) - 1.0) / SQRT_PI


def F_zeta(t: np.ndarray, zeta: float) -> np.ndarray:
    a = np.abs(t)
    return a * erf(zeta * a) + (np.exp(-(zeta * a) ** 2) - 1.0) / (
        SQRT_PI * zeta
    )


def drift_gap_scaled(s: np.ndarray | float) -> np.ndarray | float:
    s_arr = np.asarray(s)
    return s_arr * (1.0 - erf(s_arr)) + (1.0 - np.exp(-(s_arr**2))) / SQRT_PI


def variance_profile_scaled(s: np.ndarray | float) -> np.ndarray | float:
    s_arr = np.asarray(s)
    return s_arr + f_scaled(s_arr) - math.sqrt(2.0) * f_scaled(math.sqrt(2.0) * s_arr)


def variance_profile_derivative(s: float) -> float:
    return 1.0 + float(erf(s)) - 2.0 * float(erf(math.sqrt(2.0) * s))


def exact_coupling_constants() -> dict[str, float]:
    s_star = brentq(variance_profile_derivative, 1.0e-12, 2.0)
    v_max = float(variance_profile_scaled(s_star))
    v_long = (math.sqrt(2.0) - 1.0) / SQRT_PI
    spectral_variance_coeff = 2.0 ** 1.5 * v_max
    spectral_rms_coeff = math.sqrt(spectral_variance_coeff)
    return {
        "s_star": s_star,
        "v_max": v_max,
        "v_long_lag": v_long,
        "spectral_random_variance_coefficient": spectral_variance_coeff,
        "spectral_random_rms_coefficient": spectral_rms_coeff,
        "drift_gap_coefficient": math.sqrt(2.0) / SQRT_PI,
    }


def g_finite(t: np.ndarray, chi: float, zeta: float) -> np.ndarray:
    return t * t + math.sqrt(2.0) * chi * F_zeta(t, zeta)


def g_infinite(t: np.ndarray, chi: float) -> np.ndarray:
    return t * t + math.sqrt(2.0) * chi * np.abs(t)


def paired_gap_estimate(
    chi: float,
    zeta: float,
    *,
    paths: int,
    T: float,
    dt: float,
    batch: int,
    seed: int,
) -> dict[str, float]:
    if chi < 0.0:
        raise ValueError("chi must be nonnegative")
    if zeta <= 0.0:
        raise ValueError("zeta must be positive")

    nT = int(round(T / dt))
    t = np.arange(1, nT + 1, dtype=float) * dt
    g_fin = g_finite(t, chi, zeta)
    g_inf = g_infinite(t, chi)

    period_target = max(4.0 * T, 12.0 / zeta)
    nfft = 1
    while nfft * dt < period_target:
        nfft *= 2

    omega = 2.0 * math.pi * np.fft.fftfreq(nfft, d=dt)
    amplitude_filter = np.exp(-(omega * omega) / (8.0 * zeta * zeta))

    rng = np.random.default_rng(seed)
    rough_coeff = 2.0 ** 0.25 * math.sqrt(chi)

    paired_differences: list[np.ndarray] = []
    endpoint_values: list[np.ndarray] = []
    finite_values: list[np.ndarray] = []

    def dy_ratio(
        slope: np.ndarray,
        bp: np.ndarray,
        bn: np.ndarray,
        g: np.ndarray,
    ) -> np.ndarray:
        wp = math.sqrt(2.0) * (
            slope[:, None] * t[None, :] + rough_coeff * bp
        ) - g[None, :]
        wn = math.sqrt(2.0) * (
            -slope[:, None] * t[None, :] + rough_coeff * bn
        ) - g[None, :]

        peak = np.maximum.reduce([wp.max(axis=1), wn.max(axis=1), np.zeros(len(slope))])
        ep = np.exp(wp - peak[:, None])
        en = np.exp(wn - peak[:, None])
        e0 = np.exp(-peak)

        integral = dt * (
            e0
            + ep.sum(axis=1)
            + en.sum(axis=1)
            - 0.5 * ep[:, -1]
            - 0.5 * en[:, -1]
        )
        return 1.0 / integral

    completed = 0
    while completed < paths:
        b = min(batch, paths - completed)

        # White derivative samples: variance 1/dt, so a rectangular integral
        # produces exact N(0,dt) Brownian increments on the discrete grid.
        white = rng.standard_normal((b, nfft))
        y_inf = white / math.sqrt(dt)
        y_fin = np.fft.ifft(
            np.fft.fft(y_inf, axis=1) * amplitude_filter[None, :], axis=1
        ).real

        bp_inf = np.cumsum(y_inf[:, :nT] * dt, axis=1)
        bp_fin = np.cumsum(y_fin[:, :nT] * dt, axis=1)

        bn_inf = -np.cumsum(y_inf[:, -1 : -nT - 1 : -1] * dt, axis=1)
        bn_fin = -np.cumsum(y_fin[:, -1 : -nT - 1 : -1] * dt, axis=1)

        slope = rng.standard_normal(b)

        h_inf = dy_ratio(slope, bp_inf, bn_inf, g_inf)
        h_fin = dy_ratio(slope, bp_fin, bn_fin, g_fin)

        endpoint_values.append(h_inf)
        finite_values.append(h_fin)
        paired_differences.append(h_inf - h_fin)
        completed += b

    endpoint = np.concatenate(endpoint_values)
    finite = np.concatenate(finite_values)
    diff = np.concatenate(paired_differences)

    gap = float(diff.mean())
    gap_se = float(diff.std(ddof=1) / math.sqrt(paths))

    return {
        "chi": chi,
        "zeta": zeta,
        "H_mix_hat": float(endpoint.mean()),
        "H_finite_hat": float(finite.mean()),
        "paired_gap": gap,
        "paired_gap_se": gap_se,
        "sqrt_zeta_gap": math.sqrt(zeta) * gap,
        "sqrt_zeta_gap_se": math.sqrt(zeta) * gap_se,
        "paths": float(paths),
        "T": T,
        "dt": dt,
        "period": nfft * dt,
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--chi", type=float, default=0.0645)
    p.add_argument("--zeta", type=float, default=40.0)
    p.add_argument("--paths", type=int, default=4000)
    p.add_argument("--T", type=float, default=8.0)
    p.add_argument("--dt", type=float, default=None)
    p.add_argument("--batch", type=int, default=40)
    p.add_argument("--seed", type=int, default=20260811)
    p.add_argument(
        "--constants-only",
        action="store_true",
        help="Print exact coupling constants and skip Monte Carlo.",
    )
    args = p.parse_args()

    constants = exact_coupling_constants()
    print("Exact coupling constants")
    for key, value in constants.items():
        print(f"{key}: {value}")

    if args.constants_only:
        return

    dt = args.dt if args.dt is not None else min(0.0025, 0.06 / args.zeta)
    print("\nPaired Dieker-Yakir estimate")
    result = paired_gap_estimate(
        args.chi,
        args.zeta,
        paths=args.paths,
        T=args.T,
        dt=dt,
        batch=args.batch,
        seed=args.seed,
    )
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
