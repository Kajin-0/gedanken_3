#!/usr/bin/env python3
"""Step-30 universal Brownian-parabola / Gaussian-mollifier crossover.

Canonical process:

    Y_inf(s) = B(s) - s^2

where B is two-sided standard Brownian motion.  For finite crossover parameter
mu, smooth the white derivative of B with amplitude transfer

    exp[-q^2/(8 mu^2)]

and integrate from zero to obtain B_mu.  Then

    Y_mu(s) = B_mu(s) - s^2.

The small-chi generalized-Pickands crossover is

    F(mu) = (2/sqrt(pi)) E[sup Y_inf - sup Y_mu].

Because the rough endpoint maximum has O(sqrt(ds)) grid bias, this script
uses nested grids cut from one finest simulation and extrapolates linearly in
sqrt(ds) to ds -> 0.  This is a numerical continuum extrapolation, not an
exact analytic evaluation.
"""

from __future__ import annotations

import argparse
import math

import numpy as np


def simulate(
    mus: list[float],
    *,
    paths: int,
    dt: float,
    horizon: float,
    strides: tuple[int, ...],
    batch: int,
    seed: int,
) -> dict[float, dict[str, object]]:
    if not mus or min(mus) <= 0.0:
        raise ValueError("all mu values must be positive")

    rng = np.random.default_rng(seed)
    nT = int(round(horizon / dt))

    period_target = max(4.0 * horizon, 12.0 / min(mus))
    nfft = 1
    while nfft * dt < period_target:
        nfft *= 2

    omega = 2.0 * math.pi * np.fft.fftfreq(nfft, d=dt)
    filt = {
        mu: np.exp(-(omega * omega) / (8.0 * mu * mu))
        for mu in mus
    }

    t_full = np.arange(-nT, nT + 1, dtype=float) * dt
    parabola = t_full * t_full

    samples: dict[tuple[float, int], list[np.ndarray]] = {
        (mu, s): [] for mu in mus for s in strides
    }

    for start in range(0, paths, batch):
        b = min(batch, paths - start)

        white = rng.standard_normal((b, nfft))
        y_inf = white / math.sqrt(dt)
        Y = np.fft.fft(y_inf, axis=1)

        bp_inf = np.cumsum(y_inf[:, :nT] * dt, axis=1)
        bn_inf = -np.cumsum(y_inf[:, -1 : -nT - 1 : -1] * dt, axis=1)
        B_inf = np.concatenate(
            [bn_inf[:, ::-1], np.zeros((b, 1)), bp_inf], axis=1
        )

        M_inf = {
            s: np.max(B_inf[:, ::s] - parabola[None, ::s], axis=1)
            for s in strides
        }

        for mu in mus:
            y_mu = np.fft.ifft(Y * filt[mu][None, :], axis=1).real
            bp_mu = np.cumsum(y_mu[:, :nT] * dt, axis=1)
            bn_mu = -np.cumsum(y_mu[:, -1 : -nT - 1 : -1] * dt, axis=1)
            B_mu = np.concatenate(
                [bn_mu[:, ::-1], np.zeros((b, 1)), bp_mu], axis=1
            )

            for s in strides:
                M_mu = np.max(B_mu[:, ::s] - parabola[None, ::s], axis=1)
                samples[(mu, s)].append(M_inf[s] - M_mu)

    factor = 2.0 / math.sqrt(math.pi)
    out: dict[float, dict[str, object]] = {}

    for mu in mus:
        rows: list[dict[str, float]] = []
        for s in strides:
            x = np.concatenate(samples[(mu, s)])
            rows.append(
                {
                    "ds": dt * s,
                    "D": float(x.mean()),
                    "D_se": float(x.std(ddof=1) / math.sqrt(paths)),
                }
            )

        xfit = np.sqrt([r["ds"] for r in rows])
        yfit = np.array([r["D"] for r in rows])
        intercept = float(np.polyfit(xfit, yfit, 1)[1])

        # Also fit the three finest grids as a local stability diagnostic.
        n3 = min(3, len(rows))
        intercept3 = float(np.polyfit(xfit[:n3], yfit[:n3], 1)[1])

        F = factor * intercept
        F3 = factor * intercept3
        out[mu] = {
            "rows": rows,
            "D_continuum_all": intercept,
            "D_continuum_3finest": intercept3,
            "F_all": F,
            "F_3finest": F3,
            "sqrt_mu_F_3finest": math.sqrt(mu) * F3,
        }

    return out


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--mus",
        type=str,
        default="0.5,1,2,3,5,10,20",
        help="comma-separated positive mu values",
    )
    p.add_argument("--paths", type=int, default=2200)
    p.add_argument("--dt", type=float, default=0.0005)
    p.add_argument("--horizon", type=float, default=5.0)
    p.add_argument("--strides", type=str, default="1,2,4,8")
    p.add_argument("--batch", type=int, default=20)
    p.add_argument("--seed", type=int, default=20260815)
    p.add_argument(
        "--bessel-mean",
        type=float,
        default=0.87,
        help="Step-28 unweighted E[M_K] diagnostic used only to print tail A_K",
    )
    args = p.parse_args()

    mus = [float(x) for x in args.mus.split(",") if x.strip()]
    strides = tuple(int(x) for x in args.strides.split(",") if x.strip())

    result = simulate(
        mus,
        paths=args.paths,
        dt=args.dt,
        horizon=args.horizon,
        strides=strides,
        batch=args.batch,
        seed=args.seed,
    )

    print("mu       F_all      F_3finest   sqrt(mu)F_3")
    for mu in mus:
        r = result[mu]
        print(
            f"{mu:7.3f}  {r['F_all']:10.6f}  {r['F_3finest']:10.6f}  "
            f"{r['sqrt_mu_F_3finest']:12.6f}"
        )

    A_K = 2.0 / math.sqrt(math.pi) * args.bessel_mean
    print(f"\nBessel-tail A_K from supplied E[M_K]={args.bessel_mean}: {A_K}")
    print("Expected large-mu law: F(mu) ~ A_K/sqrt(mu)")
    print("NOTE: continuum values remain Monte Carlo + grid-extrapolation estimates.")


if __name__ == "__main__":
    main()
