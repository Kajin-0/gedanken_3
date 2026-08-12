#!/usr/bin/env python3
"""Step-39 finite-u remainder-factor diagnostics.

This helper is deterministic. It combines:
- the hard-window covariance coefficients at the Step-34 fast witness X=7.16,
- the Step-30 small-chi canonical crossover approximation for H(chi,zeta),
- Step-33/34 exact-cluster first-moment central estimates,
- Step-36 strip-intensity central estimates,
- the Step-38 tangent-strip/hazard formulas.

It diagnoses the factorization

    N_a(u,q) = N_tan(u,q) R(u,q)

and the inferred logarithmic threshold slope

    -d_u log R = h_a/N_a - h_tan/N_tan.

The displayed L_R=0.8 is a conservative numerical working envelope, not a
theorem or formal confidence bound.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.stats import norm

ALPHA = 1.0e-6
X = 7.16
ELL = 0.895
F0 = 0.892

# Step-30 canonical table. Linear interpolation is only a compact diagnostic;
# the dedicated Step-30 helper is the authoritative continuum calculation.
MU = np.array([0.0, 0.5, 1.0, 2.0, 3.0, 5.0, 10.0, 20.0])
FC = np.array([0.892, 0.806, 0.729, 0.597, 0.512, 0.410, 0.297, 0.213])


def eta(x: float) -> float:
    return 1.0 - math.exp(-2.0 * x) * (1.0 + 2.0 * x + 2.0 * x * x)


def a_x(x: float) -> float:
    e = eta(x)
    return 2.0 * x * x * math.exp(-2.0 * x) / e


def b_x(x: float) -> float:
    e = eta(x)
    return (
        1.0
        + math.exp(-2.0 * x) * (2.0 * x * x - 2.0 * x - 1.0)
    ) / e


def canonical_F(mu: float) -> float:
    if math.isinf(mu):
        return 0.0
    if mu <= MU[-1]:
        return float(np.interp(mu, MU, FC))
    return 0.98 / math.sqrt(mu)


def tangent_H(kappa: float, u: float) -> float:
    a = a_x(X)
    b = b_x(X)
    chi = a * u / math.sqrt(b)
    h0 = 1.0 / math.sqrt(math.pi)
    if math.isinf(kappa):
        return h0 + chi ** (2.0 / 3.0) * F0
    zeta = kappa / (math.sqrt(2.0) * u * math.sqrt(b))
    mu = math.sqrt(2.0) * zeta * chi ** (1.0 / 3.0)
    return h0 + chi ** (2.0 / 3.0) * (F0 - canonical_F(mu))


def tangent_first_moment(kappa: float, u: float) -> float:
    b = b_x(X)
    return (
        ELL
        * u
        * math.sqrt(b)
        / math.sqrt(2.0)
        * tangent_H(kappa, u)
        * norm.sf(u)
    )


def tangent_hazard(kappa: float, u: float, du: float = 1.0e-4) -> float:
    lp = math.log(tangent_first_moment(kappa, u + du))
    lm = math.log(tangent_first_moment(kappa, u - du))
    return -(lp - lm) / (2.0 * du)


def strip_factor(u: float, delta: float, L_R: float = 0.0) -> float:
    q = norm.sf
    a_minus = (u - delta) / u * q(u - delta) / q(u)
    a_plus = (u + delta) / u * q(u + delta) / q(u)
    return a_minus * math.exp(L_R * delta) - a_plus * math.exp(-L_R * delta)


def main() -> None:
    # u values from Step 38; N_a central values from Steps 33/34;
    # strip coefficients use the Step-36 w=0.01 diagnostic.
    rows = [
        (170.0, 4.958875, 0.9878, 4.95),
        (300.0, 4.958948, 0.98624, 5.06),
        (1000.0, 4.958980, 0.98423, 5.31),
        (math.inf, 4.958983, 0.98968, 5.32),
    ]

    print("Step-39 finite-u remainder factor")
    print(f"eta={eta(X):.10f}  a_x={a_x(X):.10e}  b_x={b_x(X):.10f}")
    print(
        "kappa_f   N_a/a   N_tan/a      R      h_a/N_a   h_tan/N_tan   -dlogR/du"
    )
    for kappa, u, n_exact_alpha, strip_density_alpha in rows:
        n_tan_alpha = tangent_first_moment(kappa, u) / ALPHA
        R = n_exact_alpha / n_tan_alpha
        h_exact_ratio = strip_density_alpha / n_exact_alpha
        h_tan_ratio = tangent_hazard(kappa, u)
        dlog = h_exact_ratio - h_tan_ratio
        label = "inf" if math.isinf(kappa) else f"{kappa:.0f}"
        print(
            f"{label:>7s}  {n_exact_alpha:7.5f}  {n_tan_alpha:8.5f}  {R:7.4f}  "
            f"{h_exact_ratio:10.4f}  {h_tan_ratio:12.4f}  {dlog:10.4f}"
        )

    u = 4.959
    delta = 1.0e-4
    base = strip_factor(u, delta, L_R=0.0)
    conservative = strip_factor(u, delta, L_R=0.8)
    print("\nSymmetric strip factors at u=4.959, delta=1e-4")
    print(f"tangent only:       {base:.10e}")
    print(f"with L_R=0.8:       {conservative:.10e}")
    print(f"increment from R:   {conservative-base:.10e}")
    print(f"absolute at N_a~a:  {conservative*ALPHA:.10e}")
    print("\nNOTE: L_R=0.8 is a numerical working envelope, not a theorem.")


if __name__ == "__main__":
    main()
