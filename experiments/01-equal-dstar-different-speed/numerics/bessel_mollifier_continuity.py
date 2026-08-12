#!/usr/bin/env python3
"""Step-28 two-sided BES(3) Gaussian-mollifier diagnostic.

This helper simulates the local Brownian-extremum profile used in the Step-28
continuity-correction argument.

For two independent BES(3) processes joined at zero, define the two-sided
profile R(t).  With

    K(s) = sqrt(2/pi) exp(-2 s^2),

compute

    M_K(R) = inf_u integral K(v) R(u-v) dv.

The Step-28 theorem sketch only needs M_K>0 almost surely.  The Monte Carlo
mean is a numerical diagnostic and must NOT be substituted for the actual
Dieker-Yakir-weighted coefficient

    E[Psi_infinity * M_K(R_*)].

The unweighted mean is expected to be around 0.87 for the conventions used
here.  Grid/truncation refinement is required for precision work.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.signal import fftconvolve


def kernel(t: np.ndarray) -> np.ndarray:
    return math.sqrt(2.0 / math.pi) * np.exp(-2.0 * t * t)


def simulate_mk(
    *,
    paths: int,
    dt: float,
    horizon: float,
    minimize_window: float,
    batch: int,
    seed: int,
) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    n = int(round(horizon / dt))
    t = np.arange(-n, n + 1, dtype=float) * dt

    k = kernel(t)
    k /= k.sum() * dt

    mask = np.abs(t) <= minimize_window
    samples: list[np.ndarray] = []

    for start in range(0, paths, batch):
        b = min(batch, paths - start)

        # Independent 3-D Brownian motions on the two sides.
        inc_p = rng.normal(scale=math.sqrt(dt), size=(b, 3, n))
        inc_m = rng.normal(scale=math.sqrt(dt), size=(b, 3, n))

        bm_p = np.concatenate(
            [np.zeros((b, 3, 1)), np.cumsum(inc_p, axis=2)], axis=2
        )
        bm_m = np.concatenate(
            [np.zeros((b, 3, 1)), np.cumsum(inc_m, axis=2)], axis=2
        )

        r_p = np.sqrt(np.sum(bm_p * bm_p, axis=1))
        r_m = np.sqrt(np.sum(bm_m * bm_m, axis=1))

        # Join two independent BES(3) branches at the common zero.
        r = np.concatenate([r_m[:, 1:][:, ::-1], r_p], axis=1)

        conv = fftconvolve(r, k[None, :], mode="same", axes=1) * dt
        samples.append(np.min(conv[:, mask], axis=1))

    x = np.concatenate(samples)
    return float(x.mean()), float(x.std(ddof=1) / math.sqrt(len(x)))


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--paths", type=int, default=10000)
    p.add_argument("--dt", type=float, default=0.005)
    p.add_argument("--horizon", type=float, default=6.0)
    p.add_argument("--minimize-window", type=float, default=1.5)
    p.add_argument("--batch", type=int, default=100)
    p.add_argument("--seed", type=int, default=20260811)
    args = p.parse_args()

    mean, se = simulate_mk(
        paths=args.paths,
        dt=args.dt,
        horizon=args.horizon,
        minimize_window=args.minimize_window,
        batch=args.batch,
        seed=args.seed,
    )

    print(f"paths: {args.paths}")
    print(f"dt: {args.dt}")
    print(f"horizon: {args.horizon}")
    print(f"E[M_K] estimate: {mean}")
    print(f"Monte Carlo standard error: {se}")
    print("NOTE: this is the unweighted BES diagnostic, not C_H(chi).")


if __name__ == "__main__":
    main()
