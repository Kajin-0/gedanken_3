#!/usr/bin/env python3
"""Step-45 common-random-number witness-time scan.

This helper compares the duration-truncated fast rough-endpoint Palm estimator
across candidate witness times X using the same Gaussian white noise, Palm
uniforms, and selected occupation times.  It also provides an ordinary slow
rough-endpoint cluster-moment pilot at a requested X.

The purpose is witness design, not a formal confidence certificate.  The
Step-44 finite-grid certificate remains the statistical anchor.
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


def paired_fast_scan(*, X_values, X0, ell, gap, L0, target_delta,
                     period_target, n_paths, seed, batch_size):
    n_intervals = max(20, int(round(ell/target_delta)))
    delta = ell/n_intervals
    z_beta = float(norm.ppf(BETA))

    models = {}
    for X in X_values:
        u = RHO_FULL*math.sqrt(eta(X)) - z_beta
        a = u-gap
        q_a = float(norm.sf(a))
        m_a = ell*q_a
        sqrt_eig, covariance_full = build_model(X, delta, period_target)
        nfft = len(sqrt_eig)
        offsets = np.arange(-n_intervals, n_intervals+1)
        idx = offsets % nfft
        models[X] = (u, a, q_a, m_a, sqrt_eig, covariance_full[idx], idx)

    nfft = len(models[X0][4])
    rng = np.random.default_rng(seed)
    sum_y = {X: 0.0 for X in X_values}
    sum_y2 = {X: 0.0 for X in X_values}
    sum_d = {X: 0.0 for X in X_values if X != X0}
    sum_d2 = {X: 0.0 for X in X_values if X != X0}
    short = {X: 0 for X in X_values}

    for start_path in range(0, n_paths, batch_size):
        b = min(batch_size, n_paths-start_path)
        white = rng.standard_normal((b, nfft))
        white_fft = np.fft.fft(white, axis=1)
        palm_uniform = rng.random(b)
        selected = rng.integers(0, n_intervals+1, size=b)
        values = {}

        for X in X_values:
            u, a, q_a, m_a, sqrt_eig, covariance, idx = models[X]
            process = np.fft.ifft(
                white_fft*sqrt_eig[None,:], axis=1
            ).real
            y_cond = norm.isf(palm_uniform*q_a)
            local = process[:,idx] + covariance[None,:]*(y_cond-process[:,0])[:,None]
            out = np.zeros(b)

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
                L = component_duration(segment, s, e, level=a, delta=delta)
                if L < L0:
                    short[X] += 1
                else:
                    out[j] = m_a/L

            values[X] = out
            sum_y[X] += float(out.sum())
            sum_y2[X] += float(np.dot(out, out))

        base = values[X0]
        for X in X_values:
            if X == X0:
                continue
            d = values[X]-base
            sum_d[X] += float(d.sum())
            sum_d2[X] += float(np.dot(d, d))

    result = {}
    n = float(n_paths)
    for X in X_values:
        mean = sum_y[X]/n
        variance = max((sum_y2[X]-n*mean*mean)/(n-1.0), 0.0)
        row = {"mean": mean, "se": math.sqrt(variance/n), "short": short[X]}
        if X != X0:
            dmean = sum_d[X]/n
            dvar = max((sum_d2[X]-n*dmean*dmean)/(n-1.0), 0.0)
            row["difference"] = dmean
            row["difference_se"] = math.sqrt(dvar/n)
        result[X] = row
    return result


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--X", default="7.16,7.5,7.7")
    p.add_argument("--X0", type=float, default=7.16)
    p.add_argument("--Lambda", type=float, default=.895)
    p.add_argument("--gap", type=float, default=.15)
    p.add_argument("--L0", type=float, default=.02)
    p.add_argument("--delta", type=float, default=.0015)
    p.add_argument("--period", type=float, default=16.0)
    p.add_argument("--paths", type=int, default=50000)
    p.add_argument("--batch", type=int, default=50)
    p.add_argument("--seed", type=int, default=778)
    args = p.parse_args()

    X_values = [float(v) for v in args.X.split(",") if v.strip()]
    if args.X0 not in X_values:
        X_values.append(args.X0)
        X_values.sort()

    rows = paired_fast_scan(
        X_values=X_values,
        X0=args.X0,
        ell=args.Lambda,
        gap=args.gap,
        L0=args.L0,
        target_delta=args.delta,
        period_target=args.period,
        n_paths=args.paths,
        seed=args.seed,
        batch_size=args.batch,
    )

    print("Paired fast rough-endpoint witness scan")
    print("X       mean/alpha       change/alpha       paired_SE/alpha   short")
    for X in X_values:
        row = rows[X]
        if X == args.X0:
            print(f"{X:5.2f}   {row['mean']/ALPHA:12.9f}       baseline               --       {row['short']}")
        else:
            print(
                f"{X:5.2f}   {row['mean']/ALPHA:12.9f}   "
                f"{row['difference']/ALPHA:12.9f}   "
                f"{row['difference_se']/ALPHA:12.9f}   {row['short']}"
            )

    print(
        "\nNOTE: this is a paired witness-design diagnostic. It is not a formal "
        "confidence certificate for the change in X and does not include the slow "
        "lower-bound calculation or continuum timing-grid bias."
    )


if __name__ == "__main__":
    main()
