#!/usr/bin/env python3
"""Continuum-stable full-template feasibility witness for Paper A.

This calculation is deliberately NOT a numerical localization of the finite-
window guarantee-time crossover. It uses the smooth full-template timing process

    R_infinity(y) = (1 + |y|) exp(-|y|)

to certify a quantitative slow-only guarantee-feasibility point. This avoids the
hard-window covariance cusp that invalidated the Step-13 grid crossover.

Paper-A witness parameters:

    rho0  = 3.5
    alpha = 0.05
    beta  = 0.90
    r     = tau_s / tau_f = 1.2

At known arrival time, the guarantee equation is analytic up to the scalar root
of eta(x), and the fast channel wins because both channels require the same x0
but physical time scales as tau.

At the common physical uncertainty

    L = 3.30 tau_f = 2.75 tau_s,

the full-template feasibility threshold is

    c = rho0 - Phi^{-1}(beta).

The script estimates

    P[sup_{0<=q<=ell} Z_infinity(q) > c]

for ell_s=2.75 and ell_f=3.30. If the slow probability is below alpha while
the fast probability is above alpha, the slow channel is asymptotically
guarantee-feasible and the fast channel is not.

The full template h(v)=v exp(-v) is truncated only for simulation. The default
x_tail=16 leaves a squared-template-energy fraction below 7e-12 outside the
simulation filter. Maxima are evaluated on nested grids from one common finest
grid so grid-refinement changes are directly paired.

Default production run:

    240000 paired paths
    delta_fine = 0.0025
    nested grids = 0.01, 0.005, 0.0025
    seed = 20260818

This file is a Paper-A numerical witness, not Step 50 and not a reopening of the
Step-13--49 rare-event closure branch.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.optimize import brentq
from scipy.signal import fftconvolve
from scipy.stats import beta as beta_dist
from scipy.stats import norm


RHO0_DEFAULT = 3.5
ALPHA_DEFAULT = 0.05
BETA_DEFAULT = 0.90
R_DEFAULT = 1.2
ELL_SLOW_DEFAULT = 2.75
ELL_FAST_DEFAULT = 3.30
DELTA_FINE_DEFAULT = 0.0025
X_TAIL_DEFAULT = 16.0
N_PATHS_DEFAULT = 240_000
SEED_DEFAULT = 20260818


def eta(x: float) -> float:
    return 1.0 - math.exp(-2.0 * x) * (1.0 + 2.0 * x + 2.0 * x * x)


def known_time_x0(rho0: float, alpha: float, beta: float) -> float:
    target = (float(norm.ppf(1.0 - alpha)) + float(norm.ppf(beta))) / rho0
    if not 0.0 < target < 1.0:
        raise ValueError("known-time operating point is not finitely feasible")
    return float(brentq(lambda x: math.sqrt(eta(x)) - target, 1.0e-12, 100.0))


def clopper_pearson(count: int, n: int, confidence: float = 0.95) -> tuple[float, float]:
    """Exact two-sided binomial confidence interval."""
    tail = 0.5 * (1.0 - confidence)
    lo = 0.0 if count == 0 else float(beta_dist.ppf(tail, count, n - count + 1))
    hi = 1.0 if count == n else float(beta_dist.ppf(1.0 - tail, count + 1, n - count))
    return lo, hi


def normalized_midpoint_template(x_tail: float, delta: float) -> np.ndarray:
    n = int(round(x_tail / delta))
    v = (np.arange(n, dtype=float) + 0.5) * delta
    h = v * np.exp(-v)
    return h / np.linalg.norm(h)


def nested_grid_pfa(
    *,
    ell_slow: float,
    ell_fast: float,
    threshold: float,
    delta_fine: float,
    strides: tuple[int, ...],
    x_tail: float,
    n_paths: int,
    batch: int,
    seed: int,
) -> list[dict[str, float]]:
    if ell_slow >= ell_fast:
        raise ValueError("ell_slow must be smaller than ell_fast")

    h = normalized_midpoint_template(x_tail, delta_fine)
    n_scan_fast = int(round(ell_fast / delta_fine)) + 1
    slow_index_fine = int(round(ell_slow / delta_fine))

    for stride in strides:
        if slow_index_fine % stride != 0 or (n_scan_fast - 1) % stride != 0:
            raise ValueError("requested nested grids do not land exactly on both endpoints")

    counts_slow = {stride: 0 for stride in strides}
    counts_fast = {stride: 0 for stride in strides}

    rng = np.random.default_rng(seed)
    done = 0
    while done < n_paths:
        b = min(batch, n_paths - done)
        white = rng.standard_normal((b, n_scan_fast + len(h) - 1))
        z_fine = fftconvolve(white, h[None, :], mode="valid", axes=1)

        for stride in strides:
            z = z_fine[:, ::stride]
            slow_index = slow_index_fine // stride
            maximum_slow = z[:, : slow_index + 1].max(axis=1)
            maximum_fast = z.max(axis=1)
            counts_slow[stride] += int(np.count_nonzero(maximum_slow > threshold))
            counts_fast[stride] += int(np.count_nonzero(maximum_fast > threshold))

        done += b

    rows: list[dict[str, float]] = []
    for stride in strides:
        count_s = counts_slow[stride]
        count_f = counts_fast[stride]
        p_s = count_s / n_paths
        p_f = count_f / n_paths
        slow_lo, slow_hi = clopper_pearson(count_s, n_paths)
        fast_lo, fast_hi = clopper_pearson(count_f, n_paths)
        rows.append(
            {
                "delta": delta_fine * stride,
                "slow_count": float(count_s),
                "slow_pfa": p_s,
                "slow_ci_lo": slow_lo,
                "slow_ci_hi": slow_hi,
                "fast_count": float(count_f),
                "fast_pfa": p_f,
                "fast_ci_lo": fast_lo,
                "fast_ci_hi": fast_hi,
                "paired_extra_fast_exceedances": float(count_f - count_s),
            }
        )
    return rows


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--rho0", type=float, default=RHO0_DEFAULT)
    p.add_argument("--alpha", type=float, default=ALPHA_DEFAULT)
    p.add_argument("--beta", type=float, default=BETA_DEFAULT)
    p.add_argument("--r", type=float, default=R_DEFAULT)
    p.add_argument("--ell-slow", type=float, default=ELL_SLOW_DEFAULT)
    p.add_argument("--ell-fast", type=float, default=ELL_FAST_DEFAULT)
    p.add_argument("--delta-fine", type=float, default=DELTA_FINE_DEFAULT)
    p.add_argument("--x-tail", type=float, default=X_TAIL_DEFAULT)
    p.add_argument("--paths", type=int, default=N_PATHS_DEFAULT)
    p.add_argument("--batch", type=int, default=250)
    p.add_argument("--seed", type=int, default=SEED_DEFAULT)
    args = p.parse_args()

    expected_fast_ell = args.r * args.ell_slow
    if abs(expected_fast_ell - args.ell_fast) > 1.0e-12:
        raise ValueError("ell_fast must equal r * ell_slow for one common physical L")

    x0 = known_time_x0(args.rho0, args.alpha, args.beta)
    z_beta = float(norm.ppf(args.beta))
    threshold = args.rho0 - z_beta
    missing_energy = 1.0 - eta(args.x_tail)

    print("Paper A full-template feasibility witness")
    print(f"rho0={args.rho0:.12g} alpha={args.alpha:.12g} beta={args.beta:.12g} r={args.r:.12g}")
    print(f"z_beta={z_beta:.12g}")
    print(f"full-template feasibility threshold c={threshold:.12g}")
    print(f"known-time x0={x0:.12g}")
    print(f"T_G,f(L=0)/tau_f={x0:.12g}")
    print(f"T_G,s(L=0)/tau_f={args.r * x0:.12g}")
    print(f"common physical L/tau_f={args.ell_fast:.12g}")
    print(f"common physical L/tau_s={args.ell_slow:.12g}")
    print(f"x_tail={args.x_tail:.12g} missing squared-template energy={missing_energy:.12g}")
    print()

    rows = nested_grid_pfa(
        ell_slow=args.ell_slow,
        ell_fast=args.ell_fast,
        threshold=threshold,
        delta_fine=args.delta_fine,
        strides=(4, 2, 1),
        x_tail=args.x_tail,
        n_paths=args.paths,
        batch=args.batch,
        seed=args.seed,
    )

    for row in rows:
        print(f"delta={row['delta']:.7g}")
        print(
            "  slow: "
            f"PFA={row['slow_pfa']:.9f} "
            f"95% CP=[{row['slow_ci_lo']:.9f}, {row['slow_ci_hi']:.9f}]"
        )
        print(
            "  fast: "
            f"PFA={row['fast_pfa']:.9f} "
            f"95% CP=[{row['fast_ci_lo']:.9f}, {row['fast_ci_hi']:.9f}]"
        )
        print(f"  paired extra fast exceedances={int(row['paired_extra_fast_exceedances'])}")

    finest = rows[-1]
    print()
    if finest["slow_ci_hi"] < args.alpha and finest["fast_ci_lo"] > args.alpha:
        print("CLASSIFICATION: slow guarantee-feasible / fast guarantee-infeasible at this physical L")
    else:
        print("CLASSIFICATION: witness does not separate alpha at 95% confidence")


if __name__ == "__main__":
    main()
