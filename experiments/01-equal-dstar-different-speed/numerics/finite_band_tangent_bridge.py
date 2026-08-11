#!/usr/bin/env python3
"""Step-24 finite-band tangent bridge calculator.

For the finite hard-window template h_x(v)=v exp(-v) 1_[0,x], Step 23 gave
local coefficients a_x and b_x. Step 24 adds the finite Gaussian information
band and derives the two high-excursion coordinates

    chi  = a_x u / sqrt(b_x)
    zeta = kappa / (sqrt(2) u sqrt(b_x)).

The matched tangent variogram is

    g(t) = t^2 + sqrt(2) chi [
        |t| erf(zeta |t|)
        + (exp(-zeta^2 t^2)-1)/(sqrt(pi) zeta)
    ].

This helper evaluates the coefficients and limiting checks. It is not a
hardware model and does not evaluate the generalized Pickands constant itself.
"""

from __future__ import annotations

import argparse
import math


def eta(x: float) -> float:
    return 1.0 - math.exp(-2.0 * x) * (1.0 + 2.0 * x + 2.0 * x * x)


def a_x(x: float) -> float:
    return 2.0 * x * x * math.exp(-2.0 * x) / eta(x)


def b_x(x: float) -> float:
    return (
        1.0 + math.exp(-2.0 * x) * (2.0 * x * x - 2.0 * x - 1.0)
    ) / eta(x)


def chi(x: float, u: float) -> float:
    b = b_x(x)
    return a_x(x) * u / math.sqrt(b)


def zeta(x: float, u: float, kappa: float) -> float:
    b = b_x(x)
    return kappa / (math.sqrt(2.0) * u * math.sqrt(b))


def J(y: float, kappa: float) -> float:
    ay = abs(y)
    return (
        0.5 * math.pi * ay * math.erf(0.5 * kappa * ay)
        + math.sqrt(math.pi)
        / kappa
        * (math.exp(-0.25 * (kappa * y) ** 2) - 1.0)
    )


def tangent_variogram(t: float, chi_value: float, zeta_value: float) -> float:
    at = abs(t)
    if zeta_value <= 0.0:
        raise ValueError("zeta must be positive")
    bracket = (
        at * math.erf(zeta_value * at)
        + (math.exp(-(zeta_value * t) ** 2) - 1.0)
        / (math.sqrt(math.pi) * zeta_value)
    )
    return t * t + math.sqrt(2.0) * chi_value * bracket


def curvature_asymptotic(x: float, kappa: float) -> float:
    return b_x(x) + a_x(x) * kappa / math.sqrt(math.pi)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--x", type=float, default=3.75)
    p.add_argument("--u", type=float, default=5.0)
    p.add_argument("--kappa", type=float, default=100.0)
    p.add_argument("--t", type=float, default=1.0)
    args = p.parse_args()

    av = a_x(args.x)
    bv = b_x(args.x)
    cv = chi(args.x, args.u)
    zv = zeta(args.x, args.u, args.kappa)

    print(f"eta: {eta(args.x)}")
    print(f"a_x: {av}")
    print(f"b_x: {bv}")
    print(f"chi: {cv}")
    print(f"zeta: {zv}")
    print(f"tangent_variogram(t): {tangent_variogram(args.t, cv, zv)}")
    print(f"finite_band_curvature_asymptotic: {curvature_asymptotic(args.x, args.kappa)}")
    print(f"infinite_band_tangent(t): {args.t**2 + math.sqrt(2.0)*cv*abs(args.t)}")


if __name__ == "__main__":
    main()
