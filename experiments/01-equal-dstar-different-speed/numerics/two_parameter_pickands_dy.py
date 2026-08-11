#!/usr/bin/env python3
"""Estimate the Step-25 two-parameter generalized Pickands constant.

For

    g_{chi,zeta}(t)
      = t^2 + sqrt(2)*chi*F_zeta(t)

with

    F_zeta(t)
      = |t| erf(zeta |t|)
        + [exp(-zeta^2 t^2)-1]/(sqrt(pi) zeta),

let eta be a centered Gaussian stationary-increment process with
Var eta(t)=g(t), and

    W(t)=sqrt(2)*eta(t)-g(t).

The continuous generalized Dieker-Yakir representation is

    H(chi,zeta) = E[ sup_t exp(W(t)) / integral exp(W(t)) dt ].

Efficient finite-zeta simulation uses

    eta(t)=Z*t + 2^(1/4)*sqrt(chi)*B_zeta(t),

where B_zeta(t)=integral_0^t Y_zeta(s) ds and Y_zeta is stationary Gaussian
with covariance

    E[Y_zeta(0)Y_zeta(t)] = zeta/sqrt(pi) * exp(-zeta^2 t^2).

Its spectral density is exp[-omega^2/(4 zeta^2)], so Y_zeta is synthesized
by FFT on a periodic domain and integrated once.

The result is a numerical approximation: the exact expectation is evaluated
with finite path count, finite time truncation, and finite time spacing.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.special import erf


def F_zeta(t: np.ndarray, zeta: float) -> np.ndarray:
    a = np.abs(t)
    return (
        a * erf(zeta * a)
        + (np.exp(-(zeta * a) ** 2) - 1.0) / (math.sqrt(math.pi) * zeta)
    )


def g_variogram(t: np.ndarray, chi: float, zeta: float) -> np.ndarray:
    return t * t + math.sqrt(2.0) * chi * F_zeta(t, zeta)


def simulate_Bzeta_batch(
    zeta: float,
    T: float,
    dt: float,
    batch: int,
    rng: np.random.Generator,
) -> tuple[np.ndarray, np.ndarray]:
    """Return B_zeta(+t_j), B_zeta(-t_j), j=1..T/dt.

    A periodic stationary derivative Y_zeta is synthesized from its exact
    Fourier-series spectrum. The period is chosen much larger than both the
    Dieker-Yakir truncation window and the derivative correlation length.
    """
    if zeta <= 0.0:
        raise ValueError("zeta must be positive")

    nT = int(round(T / dt))
    period_target = max(4.0 * T, 12.0 / zeta)

    nfft = 1
    while nfft * dt < period_target:
        nfft *= 2

    omega = 2.0 * math.pi * np.fft.fftfreq(nfft, d=dt)

    # Under C(h)=(1/2pi) int S(omega)e^(i omega h)domega,
    # S_Y(omega)=exp[-omega^2/(4 zeta^2)].  For a periodic discrete grid the
    # circulant covariance eigenvalues are S_Y/dt.
    eig = np.exp(-(omega * omega) / (4.0 * zeta * zeta)) / dt

    white = rng.standard_normal((batch, nfft))
    y = np.fft.ifft(
        np.fft.fft(white, axis=1) * np.sqrt(eig)[None, :], axis=1
    ).real

    # Positive branch: B(t)=int_0^t Y(s)ds.
    yp = y[:, : nT + 1]
    bp = np.cumsum(0.5 * (yp[:, :-1] + yp[:, 1:]) * dt, axis=1)

    # Negative branch: B(-s)=-int_{-s}^0 Y(v)dv.
    yn = np.concatenate([y[:, 0:1], y[:, -1 : -nT - 1 : -1]], axis=1)
    bn = -np.cumsum(0.5 * (yn[:, :-1] + yn[:, 1:]) * dt, axis=1)

    return bp, bn


def estimate_H(
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

    rng = np.random.default_rng(seed)
    ratios: list[np.ndarray] = []
    rough_coeff = 2.0 ** 0.25 * math.sqrt(chi)

    nT = int(round(T / dt))
    t = np.arange(1, nT + 1, dtype=float) * dt
    g = g_variogram(t, chi, zeta)

    for start in range(0, paths, batch):
        b = min(batch, paths - start)
        slope = rng.standard_normal(b)

        if chi > 0.0:
            bp, bn = simulate_Bzeta_batch(zeta, T, dt, b, rng)
        else:
            bp = np.zeros((b, nT))
            bn = np.zeros((b, nT))

        wp = (
            math.sqrt(2.0)
            * (slope[:, None] * t[None, :] + rough_coeff * bp)
            - g[None, :]
        )
        wn = (
            math.sqrt(2.0)
            * (-slope[:, None] * t[None, :] + rough_coeff * bn)
            - g[None, :]
        )

        peak = np.maximum.reduce([wp.max(axis=1), wn.max(axis=1), np.zeros(b)])

        ep = np.exp(wp - peak[:, None])
        en = np.exp(wn - peak[:, None])
        e0 = np.exp(-peak)

        # Trapezoidal approximation to integral_{-T}^{T} exp(W(t))dt.
        integral = dt * (
            e0
            + ep.sum(axis=1)
            + en.sum(axis=1)
            - 0.5 * ep[:, -1]
            - 0.5 * en[:, -1]
        )

        # After subtracting peak, the numerator M is exactly exp(peak), so
        # M/S = 1 / integral of exp(W-peak).
        ratios.append(1.0 / integral)

    sample = np.concatenate(ratios)
    mean = float(sample.mean())
    se = float(sample.std(ddof=1) / math.sqrt(len(sample)))

    return {
        "chi": chi,
        "zeta": zeta,
        "H_hat": mean,
        "MC_standard_error": se,
        "paths": float(paths),
        "T": T,
        "dt": dt,
        "smooth_exact_1_over_sqrt_pi": 1.0 / math.sqrt(math.pi),
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--chi", type=float, default=0.1)
    p.add_argument("--zeta", type=float, default=9.0)
    p.add_argument("--paths", type=int, default=8000)
    p.add_argument("--T", type=float, default=8.0)
    p.add_argument(
        "--dt",
        type=float,
        default=None,
        help="Default resolves both the O(1) excursion scale and ~1/zeta smoothing scale.",
    )
    p.add_argument("--batch", type=int, default=100)
    p.add_argument("--seed", type=int, default=20260811)
    args = p.parse_args()

    dt = args.dt if args.dt is not None else min(0.008, 0.08 / args.zeta)

    result = estimate_H(
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
