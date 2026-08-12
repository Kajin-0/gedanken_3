#!/usr/bin/env python3
"""Step-46 rough-endpoint grid-bias decomposition and Brownian scaling.

This helper summarizes the paired nested-grid diagnostic and evaluates the
leading Brownian continuity correction

    beta * sqrt(2 a_X dt),

with beta=-zeta(1/2)/sqrt(2*pi).

The stored paired numbers are the pooled 24k common-path results used in Step 46.
They are numerical diagnostics, not a finite-dt theorem.
"""

from __future__ import annotations

import argparse
import math


ALPHA = 1e-6
A_X_DEFAULT = 6.19142e-5
BETA = 0.5825971579390108
HAZARD_ALPHA_DEFAULT = 5.0  # h_a(u)/alpha per unit threshold

# Pooled 24k nested-grid common-path diagnostics from Step 46.
PAIRED = {
    "fine_minus_coarse": {
        "mean_alpha": 0.000530099965072112,
        "se_alpha": 0.0002506903267478721,
        "missed_success_contrib_alpha": 0.0005214924786081679,
        "duration_only_contrib_alpha": 8.607486463944103e-06,
        "missed_count": 5,
        "n_paths": 24000,
        "dt_fine": 0.00025,
        "dt_coarse": 0.001,
    },
    "fine_minus_medium": {
        "mean_alpha": 0.00015785241307226025,
        "se_alpha": 0.00015068651243343783,
        "missed_success_contrib_alpha": 0.00015067186398881683,
        "duration_only_contrib_alpha": 7.180549083443421e-06,
        "missed_count": 1,
        "n_paths": 24000,
        "dt_fine": 0.00025,
        "dt_coarse": 0.0005,
    },
}


def amplitude_correction(dt: float, a_x: float) -> float:
    return BETA * math.sqrt(2.0 * a_x * dt)


def probability_correction_alpha(dt: float, a_x: float, hazard_alpha: float) -> float:
    return hazard_alpha * amplitude_correction(dt, a_x)


def required_dt(target_alpha_fraction: float, a_x: float, hazard_alpha: float) -> float:
    c = hazard_alpha * BETA * math.sqrt(2.0 * a_x)
    return (target_alpha_fraction / c) ** 2


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--a-x", type=float, default=A_X_DEFAULT)
    p.add_argument("--hazard-alpha", type=float, default=HAZARD_ALPHA_DEFAULT)
    p.add_argument("--margin-alpha", type=float, default=4.2228796e-5)
    args = p.parse_args()

    print("Step-46 rough-grid continuity correction")
    print(f"a_X={args.a_x:.10e}")
    print(f"beta={BETA:.12f}")
    print(f"hazard coefficient h/alpha={args.hazard_alpha:.6f} per threshold unit")
    print()

    for dt in (0.001, 0.0005, 0.00025):
        amp = amplitude_correction(dt, args.a_x)
        prob = probability_correction_alpha(dt, args.a_x, args.hazard_alpha)
        print(
            f"dt={dt:.7f}  amplitude_corr={amp:.12e}  "
            f"prob_corr/alpha={prob:.12e}"
        )

    pred_cf = probability_correction_alpha(0.001, args.a_x, args.hazard_alpha) - probability_correction_alpha(0.00025, args.a_x, args.hazard_alpha)
    pred_mf = probability_correction_alpha(0.0005, args.a_x, args.hazard_alpha) - probability_correction_alpha(0.00025, args.a_x, args.hazard_alpha)

    print("\nPredicted nested-grid differences")
    print(f".001 - .00025 predicted / alpha = {pred_cf:.12e}")
    print(f".0005 - .00025 predicted / alpha = {pred_mf:.12e}")

    print("\nObserved paired nested-grid differences")
    for name, row in PAIRED.items():
        print(
            f"{name}: mean/alpha={row['mean_alpha']:.12e} "
            f"SE/alpha={row['se_alpha']:.12e} "
            f"missed_count={row['missed_count']} "
            f"missed_contrib/alpha={row['missed_success_contrib_alpha']:.12e} "
            f"duration_contrib/alpha={row['duration_only_contrib_alpha']:.12e}"
        )

    dt_req = required_dt(args.margin_alpha, args.a_x, args.hazard_alpha)
    print("\nStep-44 margin diagnostic")
    print(f"target margin/alpha={args.margin_alpha:.12e}")
    print(f"leading asymptotic dt required ~= {dt_req:.12e}")
    print(
        "NOTE: the sqrt(dt) formula is an asymptotic Brownian extreme-value "
        "continuity correction, not a finite-dt one-sided bound for the detector process."
    )


if __name__ == "__main__":
    main()
