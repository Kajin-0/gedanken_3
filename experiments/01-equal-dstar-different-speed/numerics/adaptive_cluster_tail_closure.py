#!/usr/bin/env python3
"""Step-34 paired excursion-cluster closure on q=kappa_f^(-1/2).

This helper reduces high-band Monte Carlo cost by anchoring the fast cluster
upper moment at kappa=infinity and estimating only finite-band differences with
common random numbers.  It also scans the slow lower cluster bound absolutely
because the slow margin is much larger.

The script is a numerical certification aid, not formal interval arithmetic.
It uses the Step-33 excursion-cluster definitions and occupation-Palm proposal.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.stats import norm

from excursion_cluster_moment_enclosure import (
    ALPHA,
    BETA,
    RHO_FULL,
    build_model,
    component_duration,
    detector_cluster_bounds,
    finite_rho,
)


def selected_component_upper_contribution(
    *,
    white_fft: np.ndarray,
    trunc_uniform: np.ndarray,
    selected: np.ndarray,
    x: float,
    ell: float,
    kappa: float,
    amplitude_gap: float,
    target_delta: float,
    period_target: float,
) -> np.ndarray:
    """Per-path occupation-Palm contribution to E[C_Delta]."""
    z_beta = float(norm.ppf(BETA))
    u = finite_rho(x, kappa) - z_beta
    a = u - amplitude_gap
    q_a = float(norm.sf(a))
    m_a = ell * q_a

    n_intervals = max(20, int(round(ell / target_delta)))
    delta = ell / n_intervals
    model = build_model(
        x=x,
        kappa=kappa,
        delta=delta,
        period_target=period_target,
    )
    if white_fft.shape[1] != len(model.sqrt_eig):
        raise RuntimeError("common-random-number models must use the same FFT size")

    offsets = np.arange(-n_intervals, n_intervals + 1)
    idx = offsets % len(model.sqrt_eig)
    covariance = model.covariance[idx]

    process = np.fft.ifft(
        white_fft * model.sqrt_eig[None, :], axis=1
    ).real
    y_cond = norm.isf(trunc_uniform * q_a)
    local = (
        process[:, idx]
        + covariance[None, :] * (y_cond - process[:, 0])[:, None]
    )

    out = np.zeros(len(trunc_uniform), dtype=float)
    for j, m_value in enumerate(selected):
        m = int(m_value)
        left = n_intervals - m
        segment = local[j, left : left + n_intervals + 1]
        above = segment > a
        if not above[m]:
            continue

        start = m
        while start > 0 and above[start - 1]:
            start -= 1
        end = m
        while end < n_intervals and above[end + 1]:
            end += 1

        if np.max(segment[start : end + 1]) <= u:
            continue

        length = component_duration(
            segment,
            start,
            end,
            level=a,
            delta=delta,
        )
        out[j] = m_a / length

    return out


def paired_fast_profile(
    q_values: list[float],
    *,
    X: float,
    Lambda: float,
    amplitude_gap: float,
    target_delta: float,
    period_target: float,
    n_paths: int,
    batch_size: int,
    seed: int,
) -> dict[float, dict[str, float]]:
    if 0.0 not in q_values:
        raise ValueError("q_values must include q=0 endpoint anchor")

    n_intervals = max(20, int(round(Lambda / target_delta)))
    delta = Lambda / n_intervals
    endpoint_model = build_model(
        x=X,
        kappa=math.inf,
        delta=delta,
        period_target=period_target,
    )
    nfft = len(endpoint_model.sqrt_eig)

    rng = np.random.default_rng(seed)
    sum_value = {q: 0.0 for q in q_values}
    sum_value2 = {q: 0.0 for q in q_values}
    sum_diff = {q: 0.0 for q in q_values if q != 0.0}
    sum_diff2 = {q: 0.0 for q in q_values if q != 0.0}

    for start_path in range(0, n_paths, batch_size):
        b = min(batch_size, n_paths - start_path)
        white = rng.standard_normal((b, nfft))
        white_fft = np.fft.fft(white, axis=1)
        trunc_uniform = rng.random(b)
        selected = rng.integers(0, n_intervals + 1, size=b)

        contributions: dict[float, np.ndarray] = {}
        for q in q_values:
            kappa = math.inf if q == 0.0 else 1.0 / (q * q)
            values = selected_component_upper_contribution(
                white_fft=white_fft,
                trunc_uniform=trunc_uniform,
                selected=selected,
                x=X,
                ell=Lambda,
                kappa=kappa,
                amplitude_gap=amplitude_gap,
                target_delta=target_delta,
                period_target=period_target,
            )
            contributions[q] = values
            sum_value[q] += float(values.sum())
            sum_value2[q] += float(np.dot(values, values))

        endpoint = contributions[0.0]
        for q in q_values:
            if q == 0.0:
                continue
            d = contributions[q] - endpoint
            sum_diff[q] += float(d.sum())
            sum_diff2[q] += float(np.dot(d, d))

    out: dict[float, dict[str, float]] = {}
    n = float(n_paths)
    for q in q_values:
        mean = sum_value[q] / n
        variance = max((sum_value2[q] - n * mean * mean) / (n - 1.0), 0.0)
        row = {
            "upper": mean,
            "upper_se": math.sqrt(variance / n),
        }
        if q != 0.0:
            dmean = sum_diff[q] / n
            dvar = max((sum_diff2[q] - n * dmean * dmean) / (n - 1.0), 0.0)
            row["difference_from_endpoint"] = dmean
            row["difference_se"] = math.sqrt(dvar / n)
        out[q] = row

    return out


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--X", type=float, default=7.16)
    p.add_argument("--Lambda", type=float, default=0.895)
    p.add_argument("--gap", type=float, default=0.15)
    p.add_argument("--delta", type=float, default=0.0012)
    p.add_argument("--period", type=float, default=16.0)
    p.add_argument("--paired-paths", type=int, default=3000)
    p.add_argument("--slow-paths", type=int, default=3000)
    p.add_argument("--batch", type=int, default=20)
    p.add_argument("--seed", type=int, default=20260811)
    p.add_argument(
        "--q",
        default="0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.055,0.06,0.065,0.07,0.075,0.0767",
    )
    p.add_argument("--endpoint-upper", type=float, default=0.98968)
    p.add_argument("--endpoint-upper-se", type=float, default=0.00429)
    p.add_argument("--z", type=float, default=1.645)
    p.add_argument("--fast-grid-allowance", type=float, default=0.002)
    p.add_argument("--fast-mesh-allowance", type=float, default=0.0006)
    args = p.parse_args()

    q_values = [float(v) for v in args.q.split(",") if v.strip()]
    if 0.0 not in q_values:
        q_values = [0.0] + q_values

    fast = paired_fast_profile(
        q_values,
        X=args.X,
        Lambda=args.Lambda,
        amplitude_gap=args.gap,
        target_delta=args.delta,
        period_target=args.period,
        n_paths=args.paired_paths,
        batch_size=args.batch,
        seed=args.seed,
    )

    print("Paired fast upper-moment corrections")
    print("q        kappa_f       dU/alpha       SE[dU]/alpha")
    max_se_diff = 0.0
    max_positive = 0.0
    for q in q_values:
        if q == 0.0:
            print(f"{q:7.4f}   {'inf':>10s}       endpoint          --")
            continue
        kappa = 1.0 / (q * q)
        d = fast[q]["difference_from_endpoint"] / ALPHA
        se = fast[q]["difference_se"] / ALPHA
        max_se_diff = max(max_se_diff, se)
        max_positive = max(max_positive, d)
        print(f"{q:7.4f}   {kappa:10.2f}   {d:12.8f}   {se:12.8f}")

    combined_se = math.sqrt(args.endpoint_upper_se**2 + max_se_diff**2)
    fast_envelope = (
        args.endpoint_upper
        + max_positive
        + args.z * combined_se
        + args.fast_grid_allowance
        + args.fast_mesh_allowance
    )
    print(f"\nmax paired SE/alpha: {max_se_diff:.8f}")
    print(f"max positive paired correction/alpha: {max_positive:.8f}")
    print(f"fast conservative envelope/alpha: {fast_envelope:.8f}")

    print("\nSlow absolute cluster lower scan")
    print("q        kappa_f       lower/alpha      SE_lower/alpha")
    for i, q in enumerate(q_values):
        kappa = math.inf if q == 0.0 else 1.0 / (q * q)
        _, slow = detector_cluster_bounds(
            kappa_fast=kappa,
            X=args.X,
            Lambda=args.Lambda,
            amplitude_gap=args.gap,
            target_delta=args.delta,
            period_target=args.period,
            n_paths=args.slow_paths,
            batch_size=args.batch,
            seed=args.seed + 10000 + i,
        )
        label = "inf" if q == 0.0 else f"{kappa:.2f}"
        print(
            f"{q:7.4f}   {label:>10s}   "
            f"{slow['PFA_lower']/ALPHA:12.8f}   "
            f"{slow['SE_PFA_lower_delta']/ALPHA:12.8f}"
        )

    print(
        "\nNOTE: this script reports a paired numerical closure aid. The endpoint "
        "anchor, Gaussian-SE factor, grid allowance, and inter-node allowance are "
        "not formal interval arithmetic or a theorem-level continuity bound."
    )


if __name__ == "__main__":
    main()
