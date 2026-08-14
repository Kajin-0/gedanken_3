#!/usr/bin/env python3
"""Reproduce Experiment-10 scalar-asymmetry Auger reopening thresholds.

Model:
    E_±(k) = D k^2 ± sqrt(Delta^2 + (hbar v k)^2)

Dimensionless parameters:
    q = hbar v k / Delta
    beta = D Delta / (hbar^2 v^2)
    A_m = 2 |beta|

The exact collinear threshold at fixed q0 is

    beta_c(q0) = min_x [2 s(x) + s(q0-2x) - s(q0)] / [2 (q0-x)^2],

with s(q)=sqrt(1+q^2), 0 <= x <= q0/2.
"""

from __future__ import annotations

import math
from scipy.optimize import brentq, minimize_scalar

EG_OVER_KBT = 4.79592292
DELTA_OVER_KBT = EG_OVER_KBT / 2.0


def s(q: float) -> float:
    return math.sqrt(1.0 + q * q)


def beta_at_partition(q0: float, x: float) -> float:
    z = q0 - 2.0 * x
    numerator = 2.0 * s(x) + s(z) - s(q0)
    denominator = 2.0 * (q0 - x) ** 2
    return numerator / denominator


def threshold_partition(q0: float) -> tuple[float, float, float]:
    result = minimize_scalar(
        lambda x: beta_at_partition(q0, x),
        bounds=(0.0, q0 / 2.0),
        method="bounded",
        options={"xatol": 1e-13},
    )

    candidates = [
        (result.fun, result.x),
        (beta_at_partition(q0, 0.0), 0.0),
        (beta_at_partition(q0, q0 / 2.0), q0 / 2.0),
    ]
    beta_c, x = min(candidates)
    z = q0 - 2.0 * x
    return beta_c, x, z


def q_threshold(beta: float) -> float:
    if not (0.0 < beta < 0.5):
        raise ValueError("This script assumes 0 < beta < 1/2.")

    def residual(q: float) -> float:
        return threshold_partition(q)[0] - beta

    lo = 1e-8
    hi = 2.0
    while residual(hi) > 0.0:
        hi *= 2.0
    return brentq(residual, lo, hi, xtol=1e-12)


def threshold_data_from_am(am: float) -> dict[str, float]:
    beta = am / 2.0
    q = q_threshold(beta)
    beta_c, x, z = threshold_partition(q)
    e_total_over_delta = s(q) + beta * q * q
    k_over_kbt = (e_total_over_delta - 1.0) * DELTA_OVER_KBT
    return {
        "A_m": am,
        "beta": beta,
        "q_th": q,
        "x": x,
        "z": z,
        "K_th_over_kBT": k_over_kbt,
        "E_e_th_over_Eg": e_total_over_delta / 2.0,
        "beta_check": beta_c,
    }


def am_for_target_kbt(target: float) -> float:
    def residual(am: float) -> float:
        return threshold_data_from_am(am)["K_th_over_kBT"] - target

    return brentq(residual, 1e-5, 0.414, xtol=1e-12)


def main() -> None:
    q_star = math.sqrt(2.0 + 2.0 * math.sqrt(2.0))
    beta_star = (math.sqrt(2.0) - 1.0) / 2.0

    print("Branch-change constants")
    print(f"q_*    = {q_star:.9f}")
    print(f"beta_* = {beta_star:.9f}")
    print()

    print("Exact thresholds at Eg/kBT = 4.79592292")
    print("A_m      beta       q_th       K_th/kBT    E_e,th/Eg")
    for am in (0.40, 0.20, 0.10, 0.04, 0.02, 0.01):
        row = threshold_data_from_am(am)
        print(
            f"{row['A_m']:0.4f}   {row['beta']:0.5f}   "
            f"{row['q_th']:8.4f}   {row['K_th_over_kBT']:10.4f}   "
            f"{row['E_e_th_over_Eg']:10.4f}"
        )
    print()

    print("Inverted symmetry tolerances")
    print("target K_th/kBT   max A_m     m_h/m_e")
    for target in (8.0, 10.0, 12.0, 15.0):
        am = am_for_target_kbt(target)
        mass_ratio = (1.0 + am) / (1.0 - am)
        print(f"{target:8.1f}         {am:0.6f}     {mass_ratio:0.6f}")
    print()

    print("Weak-asymmetry asymptotic")
    print("beta_c(q) ~ 4/q^3")
    print("q_th ~ (4/beta)^(1/3)")
    print("K_th ~ Eg * A_m^(-1/3)")


if __name__ == "__main__":
    main()
