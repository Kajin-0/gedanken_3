#!/usr/bin/env python3
"""Step-44 dedicated L0-truncated occupation-Palm endpoint certificate.

This reproduces the fast rough-endpoint long-cluster estimator used in Step 44.
Each path contributes

    Y = m_a * S / L * 1{L >= L0}

under the lower-level occupation-Palm law.  The support is exactly

    0 <= Y <= m_a/L0

for the implemented finite grid.  Independent batches may be pooled and a
Maurer-Pontil empirical-Bernstein upper confidence bound applied once to the
pooled i.i.d. sample.

The default seeds reproduce the four 50k batches used in Step 44.  This helper
reports finite-grid statistics only; continuum timing-grid bias is separate.
"""

from __future__ import annotations

import argparse
import math
import numpy as np
from scipy.stats import norm

RHO_FULL = 6.2407571
BETA = 0.90
ALPHA = 1.0e-6


def eta(x: float) -> float:
    return 1.0 - math.exp(-2.0*x)*(1.0 + 2.0*x + 2.0*x*x)


def H_x(omega: np.ndarray, x: float) -> np.ndarray:
    z = 1.0 + 1j*omega
    return (1.0 - np.exp(-z*x)*(1.0 + z*x))/(z*z)


def build_model(x: float, delta: float, period_target: float):
    nfft = 1
    while nfft*delta < period_target:
        nfft *= 2
    omega = 2.0*math.pi*np.fft.fftfreq(nfft, d=delta)
    eig = np.abs(H_x(omega, x))**2
    eig /= eig.mean()
    return np.sqrt(eig), np.fft.ifft(eig).real


def component_duration(segment, start, end, *, level, delta):
    n = len(segment)-1
    if start == 0:
        t_left = 0.0
    else:
        z0 = float(segment[start-1]); z1 = float(segment[start])
        den = z1-z0
        frac = (level-z0)/den if den != 0 else 1.0
        frac = min(max(frac, 0.0), 1.0)
        t_left = (start-1+frac)*delta
    if end == n:
        t_right = n*delta
    else:
        z0 = float(segment[end]); z1 = float(segment[end+1])
        den = z0-z1
        frac = (z0-level)/den if den != 0 else 1.0
        frac = min(max(frac, 0.0), 1.0)
        t_right = (end+frac)*delta
    return max(t_right-t_left, 0.5*delta)


def one_batch(*, n_paths, seed, X, ell, gap, L0, target_delta,
              period_target, batch_size):
    z_beta = float(norm.ppf(BETA))
    u = RHO_FULL*math.sqrt(eta(X)) - z_beta
    a = u-gap
    q_a = float(norm.sf(a))
    m_a = ell*q_a

    n_intervals = max(20, int(round(ell/target_delta)))
    delta = ell/n_intervals
    sqrt_eig, covariance_full = build_model(X, delta, period_target)
    nfft = len(sqrt_eig)
    offsets = np.arange(-n_intervals, n_intervals+1)
    idx = offsets % nfft
    covariance = covariance_full[idx]

    rng = np.random.default_rng(seed)
    sum_y = 0.0
    sum_y2 = 0.0
    selected_success = 0
    selected_short = 0

    for start_path in range(0, n_paths, batch_size):
        b = min(batch_size, n_paths-start_path)
        white = rng.standard_normal((b, nfft))
        process = np.fft.ifft(
            np.fft.fft(white, axis=1)*sqrt_eig[None,:], axis=1
        ).real
        y_cond = norm.isf(rng.random(b)*q_a)
        local = (
            process[:,idx]
            + covariance[None,:]*(y_cond-process[:,0])[:,None]
        )
        selected = rng.integers(0, n_intervals+1, size=b)

        for j, m_value in enumerate(selected):
            m = int(m_value)
            left = n_intervals-m
            segment = local[j, left:left+n_intervals+1]
            above = segment > a
            if not above[m]:
                continue
            s = m
            while s > 0 and above[s-1]:
                s -= 1
            e = m
            while e < n_intervals and above[e+1]:
                e += 1
            if np.max(segment[s:e+1]) <= u:
                continue
            selected_success += 1
            L = component_duration(segment, s, e, level=a, delta=delta)
            if L < L0:
                selected_short += 1
                y = 0.0
            else:
                y = m_a/L
            sum_y += y
            sum_y2 += y*y

    mean = sum_y/n_paths
    variance = max(
        (sum_y2 - n_paths*mean*mean)/(n_paths-1), 0.0
    )
    return {
        "n": n_paths,
        "seed": seed,
        "sum_y": sum_y,
        "sum_y2": sum_y2,
        "mean": mean,
        "sd": math.sqrt(variance),
        "success": selected_success,
        "short": selected_short,
        "u": u,
        "a": a,
        "m_a": m_a,
        "delta": delta,
        "nfft": nfft,
    }


def pooled_stats(rows):
    n = sum(r["n"] for r in rows)
    sum_y = sum(r["sum_y"] for r in rows)
    sum_y2 = sum(r["sum_y2"] for r in rows)
    mean = sum_y/n
    variance = max((sum_y2-n*mean*mean)/(n-1), 0.0)
    return n, mean, math.sqrt(variance)


def empirical_bernstein(sample_sd, support, n, failure_prob):
    logterm = math.log(2.0/failure_prob)
    variance_term = math.sqrt(2.0*sample_sd*sample_sd*logterm/n)
    range_term = 7.0*support*logterm/(3.0*(n-1))
    return variance_term+range_term, variance_term, range_term


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--X", type=float, default=7.16)
    p.add_argument("--Lambda", type=float, default=.895)
    p.add_argument("--gap", type=float, default=.15)
    p.add_argument("--L0", type=float, default=.02)
    p.add_argument("--delta", type=float, default=.001)
    p.add_argument("--period", type=float, default=16.0)
    p.add_argument("--paths-per-seed", type=int, default=50000)
    p.add_argument("--batch", type=int, default=100)
    p.add_argument("--seeds", default="20260812,20260813,20260814,20260815")
    p.add_argument("--failure", type=float, default=.05)
    p.add_argument("--short-bound", type=float, default=3.9e-11)
    args = p.parse_args()

    seeds = [int(s) for s in args.seeds.split(",") if s.strip()]
    rows = []
    for seed in seeds:
        row = one_batch(
            n_paths=args.paths_per_seed,
            seed=seed,
            X=args.X,
            ell=args.Lambda,
            gap=args.gap,
            L0=args.L0,
            target_delta=args.delta,
            period_target=args.period,
            batch_size=args.batch,
        )
        rows.append(row)
        print(
            f"seed={seed} n={row['n']} mean/alpha={row['mean']/ALPHA:.9f} "
            f"sd={row['sd']:.9e} success={row['success']} short={row['short']}"
        )

    n, mean, sd = pooled_stats(rows)
    m_a = rows[0]["m_a"]
    support = m_a/args.L0
    radius, variance_term, range_term = empirical_bernstein(
        sd, support, n, args.failure
    )
    total = mean + radius + args.short_bound

    print("\nPooled certificate")
    print(f"n={n}")
    print(f"mean/alpha={mean/ALPHA:.12f}")
    print(f"sample SD={sd:.12e}")
    print(f"support={support:.12e}")
    print(f"variance term/alpha={variance_term/ALPHA:.12f}")
    print(f"range term/alpha={range_term/ALPHA:.12f}")
    print(f"radius/alpha={radius/ALPHA:.12f}")
    print(f"short bound/alpha={args.short_bound/ALPHA:.12f}")
    print(f"finite-grid upper/alpha={total/ALPHA:.12f}")
    print(f"finite-grid margin/alpha={1.0-total/ALPHA:.12e}")
    print(
        "NOTE: this is a pointwise finite-grid statistical certificate only. "
        "Continuum timing-grid bias and simultaneous multi-node confidence are separate."
    )


if __name__ == "__main__":
    main()
