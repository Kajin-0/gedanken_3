#!/usr/bin/env python3
"""Step-36 tail-sensitive cluster-maximum strip diagnostic.

Fix a lower declustering level a=u-Delta and the connected components of
{z>a}. For a selected lower-level component under the occupation-Palm law,
record its maximum M_I and duration L. Then

    E[D_a(y1,y2)]
      = ell Q(a) E_a[ 1{y1 < M_I <= y2} / L ]

where D_a counts fixed lower-level components whose maxima lie in the success
threshold strip. Since

    {y1 < sup z <= y2} subset {D_a(y1,y2)>=1},

this first moment is an exact upper bound on the buffered-threshold probability.

The script estimates the local strip intensity for the fast Step-34 trajectory.
It is Monte Carlo/grid numerical work, not formal interval arithmetic.
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
    finite_rho,
)


def strip_first_moments(
    *,
    x: float,
    ell: float,
    kappa: float,
    amplitude_gap: float,
    half_widths: list[float],
    target_delta: float,
    period_target: float,
    n_paths: int,
    batch_size: int,
    seed: int,
) -> dict[str, object]:
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

    nfft = len(model.sqrt_eig)
    offsets = np.arange(-n_intervals, n_intervals + 1)
    idx = offsets % nfft
    covariance = model.covariance[idx]

    rng = np.random.default_rng(seed)
    sum_success = 0.0
    sum_success2 = 0.0
    sums = {w: 0.0 for w in half_widths}
    sums2 = {w: 0.0 for w in half_widths}

    for start_path in range(0, n_paths, batch_size):
        b = min(batch_size, n_paths - start_path)
        white = rng.standard_normal((b, nfft))
        process = np.fft.ifft(
            np.fft.fft(white, axis=1) * model.sqrt_eig[None, :], axis=1
        ).real

        y_cond = norm.isf(rng.random(b) * q_a)
        local = (
            process[:, idx]
            + covariance[None, :] * (y_cond - process[:, 0])[:, None]
        )
        selected = rng.integers(0, n_intervals + 1, size=b)

        for j in range(b):
            m = int(selected[j])
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

            maximum = float(np.max(segment[start : end + 1]))
            length = component_duration(
                segment,
                start,
                end,
                level=a,
                delta=delta,
            )
            weight = m_a / length

            if maximum > u:
                sum_success += weight
                sum_success2 += weight * weight

            for width in half_widths:
                if u - width < maximum <= u + width:
                    sums[width] += weight
                    sums2[width] += weight * weight

    n = float(n_paths)
    success = sum_success / n
    success_var = max(sum_success2 / n - success * success, 0.0)

    rows = []
    for width in half_widths:
        strip = sums[width] / n
        strip_var = max(sums2[width] / n - strip * strip, 0.0)
        rows.append(
            {
                "half_width": width,
                "strip_first_moment": strip,
                "strip_se": math.sqrt(strip_var / n),
                "strip_over_alpha": strip / ALPHA,
                "density_over_alpha": strip / (2.0 * width * ALPHA),
            }
        )

    return {
        "u": u,
        "a": a,
        "Q_a": q_a,
        "delta": delta,
        "success_first_moment": success,
        "success_se": math.sqrt(success_var / n),
        "rows": rows,
    }


def parse_kappa(text: str) -> float:
    return math.inf if text.lower() in {"inf", "infinity"} else float(text)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--kappas", default="170,300,1000,inf")
    p.add_argument("--x", type=float, default=7.16)
    p.add_argument("--ell", type=float, default=0.895)
    p.add_argument("--gap", type=float, default=0.15)
    p.add_argument("--widths", default="0.005,0.01,0.02")
    p.add_argument("--delta", type=float, default=0.0015)
    p.add_argument("--period", type=float, default=16.0)
    p.add_argument("--paths", type=int, default=12000)
    p.add_argument("--batch", type=int, default=25)
    p.add_argument("--seed", type=int, default=20260811)
    args = p.parse_args()

    kappas = [parse_kappa(v.strip()) for v in args.kappas.split(",") if v.strip()]
    widths = [float(v) for v in args.widths.split(",") if v.strip()]

    print("Tail-sensitive fixed-cluster maximum strip diagnostic")
    print(
        f"x={args.x}, ell={args.ell}, gap={args.gap}, paths={args.paths}, alpha={ALPHA}"
    )
    print("kappa_f      u       width   strip/alpha   SE/alpha   density/alpha")

    for i, kappa in enumerate(kappas):
        result = strip_first_moments(
            x=args.x,
            ell=args.ell,
            kappa=kappa,
            amplitude_gap=args.gap,
            half_widths=widths,
            target_delta=args.delta,
            period_target=args.period,
            n_paths=args.paths,
            batch_size=args.batch,
            seed=args.seed + 100 * i,
        )
        label = "inf" if math.isinf(kappa) else f"{kappa:g}"
        for row in result["rows"]:
            print(
                f"{label:>7s}   {result['u']:7.4f}   "
                f"{row['half_width']:7.4f}   "
                f"{row['strip_over_alpha']:11.6f}   "
                f"{row['strip_se']/ALPHA:9.6f}   "
                f"{row['density_over_alpha']:13.6f}"
            )

    print(
        "\nInterpretation: density/alpha near O(5) means the buffered-threshold "
        "probability scales like rare-event intensity times strip width, rather "
        "than the order-one coefficient in a global Gaussian anti-concentration bound."
    )
    print(
        "NOTE: the cluster-strip inequality is exact; the displayed strip moments "
        "are finite-grid Monte Carlo estimates."
    )


if __name__ == "__main__":
    main()
