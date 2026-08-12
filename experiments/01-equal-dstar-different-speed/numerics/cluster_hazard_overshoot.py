#!/usr/bin/env python3
"""Step-37 high-threshold cluster overshoot / hazard helper.

This script compares the fixed-class Pickands endpoint models at the Step-36
operating threshold. It is a deterministic asymptotic diagnostic, not an exact
finite-u cluster calculation.

For local covariance R(t)=1-c|t|^gamma+o(|t|^gamma), Pickands gives

    N(u) ~ K u^(2/gamma) Q(u).

For a threshold shift s/u,

    N(u+s/u)/N(u) -> exp(-s),

independent of gamma at leading order.  The helper prints finite-u hazard and
symmetric-strip coefficients for gamma=1 and the smooth Gaussian-peak model.
"""

from __future__ import annotations

import argparse
import math

from scipy.stats import norm


def inverse_mills(u: float) -> float:
    return float(norm.pdf(u) / norm.sf(u))


def rough_pickands_hazard(u: float, gamma: float) -> float:
    """Hazard of the explicit leading model u^(2/gamma) Q(u)."""
    return inverse_mills(u) - (2.0 / gamma) / u


def model_tail(u: float, gamma: float) -> float:
    return (u ** (2.0 / gamma)) * float(norm.sf(u))


def symmetric_strip_coefficient(u: float, w: float, gamma: float) -> float:
    n0 = model_tail(u, gamma)
    return (model_tail(u - w, gamma) - model_tail(u + w, gamma)) / (2.0 * w * n0)


def smooth_peak_strip_coefficient(u: float, w: float) -> float:
    """Exact coefficient for the smooth Rice leading form proportional to phi(u)."""
    p0 = float(norm.pdf(u))
    return (float(norm.pdf(u - w)) - float(norm.pdf(u + w))) / (2.0 * w * p0)


def overshoot_ratio(u: float, s: float, gamma: float) -> float:
    return model_tail(u + s / u, gamma) / model_tail(u, gamma)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--u", type=float, default=4.959)
    p.add_argument("--widths", default="0.005,0.01,0.02")
    p.add_argument("--s", default="0.1,0.25,0.5,1.0")
    args = p.parse_args()

    u = args.u
    widths = [float(x) for x in args.widths.split(",") if x.strip()]
    s_values = [float(x) for x in args.s.split(",") if x.strip()]

    print(f"u={u:.6f}")
    print(f"inverse Mills phi/Q = {inverse_mills(u):.9f}")
    print(f"smooth Rice peak hazard = u = {u:.9f}")
    print(f"Pickands gamma=2 leading hazard = {rough_pickands_hazard(u, 2.0):.9f}")
    print(f"Pickands gamma=1 leading hazard = {rough_pickands_hazard(u, 1.0):.9f}")

    print("\nSymmetric strip coefficient [N(u-w)-N(u+w)]/(2w N(u))")
    print("w          smooth-phi      gamma=2        gamma=1")
    for w in widths:
        print(
            f"{w:8.5f}   {smooth_peak_strip_coefficient(u,w):12.8f}"
            f"   {symmetric_strip_coefficient(u,w,2.0):12.8f}"
            f"   {symmetric_strip_coefficient(u,w,1.0):12.8f}"
        )

    print("\nOvershoot ratio N(u+s/u)/N(u) versus exp(-s)")
    print("s          exp(-s)         gamma=2        gamma=1")
    for s in s_values:
        print(
            f"{s:8.4f}   {math.exp(-s):12.8f}"
            f"   {overshoot_ratio(u,s,2.0):12.8f}"
            f"   {overshoot_ratio(u,s,1.0):12.8f}"
        )

    print(
        "\nInterpretation: fixed-class Pickands theory explains the 1/u overshoot "
        "scale and h~uN asymptotically.  It does not provide a uniform finite-u "
        "constant across q->0, where the model crosses from infinitesimally smooth "
        "finite-band paths to the rough hard-window endpoint."
    )


if __name__ == "__main__":
    main()
