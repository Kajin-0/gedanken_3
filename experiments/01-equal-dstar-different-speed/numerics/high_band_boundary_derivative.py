#!/usr/bin/env python3
"""Step-26 high-band fast/slow boundary derivative diagnostic.

This calculator evaluates the coupled 1/sqrt(kappa_f) boundary coefficient
from the matched finite-u tangent surrogate described in
HIGH_BAND_BOUNDARY_DERIVATIVE_STEP.md.

It does NOT prove the observed

    H_mix(chi) - H(chi,zeta) ~ C_H(chi)/sqrt(zeta)

law.  Instead, it accepts locally measured C_H values and propagates them
through the exact implicit-boundary algebra.  The purpose is to make the
sign calculation reproducible and to separate the asymptotic algebra from
the still-open smoothing-rate theorem.
"""

from __future__ import annotations

import argparse
import math

from scipy.stats import norm


def eta(x: float) -> float:
    return 1.0 - math.exp(-2.0 * x) * (1.0 + 2.0 * x + 2.0 * x * x)


def a_coeff(x: float) -> float:
    return 2.0 * x * x * math.exp(-2.0 * x) / eta(x)


def b_coeff(x: float) -> float:
    e2 = math.exp(-2.0 * x)
    return (1.0 + e2 * (2.0 * x * x - 2.0 * x - 1.0)) / eta(x)


def d_coefficient(
    *,
    A_inf: float,
    C_H: float,
    H_inf: float,
    u: float,
    b: float,
    kappa_scale: float,
) -> float:
    """Coefficient d_i in A_i=A_i_inf+d_i/sqrt(kappa_f)+... ."""
    return (
        A_inf
        * (C_H / H_inf)
        * math.sqrt(math.sqrt(2.0) * u * math.sqrt(b) / kappa_scale)
    )


def coupled_coefficients(
    *,
    A_fx: float,
    A_sx: float,
    d_f: float,
    d_s: float,
) -> tuple[float, float]:
    denominator = A_fx - A_sx
    x1 = -(d_f - d_s) / denominator
    C_lambda = (A_fx * d_s - A_sx * d_f) / denominator
    return x1, C_lambda


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--r", type=float, default=2.0)
    p.add_argument("--rho-full", type=float, default=6.2407571)
    p.add_argument("--beta", type=float, default=0.90)
    p.add_argument("--X-inf", type=float, default=7.73248)
    p.add_argument("--Lambda-inf-surrogate", type=float, default=0.88564)

    # Local generalized-Pickands endpoint/smoothing values measured around
    # the Step-23 equality trajectory.
    p.add_argument("--H-fast", type=float, default=0.5660)
    p.add_argument("--H-slow", type=float, default=0.7133)
    p.add_argument("--C-fast", type=float, default=0.0061)
    p.add_argument("--C-slow", type=float, default=0.20)

    # Numerical X-derivatives of the Mills-corrected tangent admissible
    # physical search lengths at the surrogate infinite-band equality.
    p.add_argument("--Afx", type=float, default=4.94e-3)
    p.add_argument("--Asx", type=float, default=4.50e-1)
    args = p.parse_args()

    z_beta = float(norm.ppf(args.beta))
    x_f = args.X_inf
    x_s = args.X_inf / args.r

    b_f = b_coeff(x_f)
    b_s = b_coeff(x_s)
    u_f = args.rho_full * math.sqrt(eta(x_f)) - z_beta
    u_s = args.rho_full * math.sqrt(eta(x_s)) - z_beta

    chi_f = a_coeff(x_f) * u_f / math.sqrt(b_f)
    chi_s = a_coeff(x_s) * u_s / math.sqrt(b_s)

    d_f = d_coefficient(
        A_inf=args.Lambda_inf_surrogate,
        C_H=args.C_fast,
        H_inf=args.H_fast,
        u=u_f,
        b=b_f,
        kappa_scale=1.0,
    )
    d_s = d_coefficient(
        A_inf=args.Lambda_inf_surrogate,
        C_H=args.C_slow,
        H_inf=args.H_slow,
        u=u_s,
        b=b_s,
        kappa_scale=args.r,
    )

    x1, C_lambda = coupled_coefficients(
        A_fx=args.Afx,
        A_sx=args.Asx,
        d_f=d_f,
        d_s=d_s,
    )

    print(f"X_inf_surrogate: {args.X_inf}")
    print(f"x_fast: {x_f}")
    print(f"x_slow: {x_s}")
    print(f"u_fast: {u_f}")
    print(f"u_slow: {u_s}")
    print(f"chi_fast: {chi_f}")
    print(f"chi_slow: {chi_s}")
    print(f"d_fast: {d_f}")
    print(f"d_slow: {d_s}")
    print(f"x1: {x1}")
    print(f"C_Lambda: {C_lambda}")

    if C_lambda > 0.0:
        print("asymptotic_boundary_side: above rough endpoint")
        print("asymptotic_derivative_sign: negative")
    elif C_lambda < 0.0:
        print("asymptotic_boundary_side: below rough endpoint")
        print("asymptotic_derivative_sign: positive")
    else:
        print("asymptotic_boundary_side: leading coefficient vanishes")
        print("asymptotic_derivative_sign: unresolved at this order")


if __name__ == "__main__":
    main()
