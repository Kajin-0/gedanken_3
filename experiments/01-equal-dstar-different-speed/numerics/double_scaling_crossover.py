#!/usr/bin/env python3
"""Step-29 Brownian-parabola double-scaling diagnostics.

This helper converts the Step-27 paired generalized-Pickands gaps into the
small-chi Brownian-parabola scaling variables

    h_chi = sqrt(2) * chi^(1/3)
    mu    = zeta * h_chi
    F_emp = [H_mix(chi)-H(chi,zeta)] / chi^(2/3)

and evaluates the physical r=2 endpoint trajectory

    mu_i = kappa_i * chi_i^(1/3) / [u_i sqrt(b_i)].

It intentionally uses the already reported paired Step-27 data.  It does not
fit a new asymptotic coefficient or claim a certified onset bandwidth.
"""

from __future__ import annotations

import math


SQRT_PI = math.sqrt(math.pi)


def eta(x: float) -> float:
    return 1.0 - math.exp(-2.0 * x) * (1.0 + 2.0 * x + 2.0 * x * x)


def a_coeff(x: float) -> float:
    return 2.0 * x * x * math.exp(-2.0 * x) / eta(x)


def b_coeff(x: float) -> float:
    e2 = math.exp(-2.0 * x)
    return (1.0 + e2 * (2.0 * x * x - 2.0 * x - 1.0)) / eta(x)


def collapse_row(chi: float, zeta: float, sqrt_zeta_gap: float) -> dict[str, float]:
    delta_h = sqrt_zeta_gap / math.sqrt(zeta)
    mu = math.sqrt(2.0) * zeta * chi ** (1.0 / 3.0)
    f_emp = delta_h / chi ** (2.0 / 3.0)
    return {
        "chi": chi,
        "zeta": zeta,
        "mu": mu,
        "delta_H": delta_h,
        "F_emp": f_emp,
        "sqrt_mu_F": math.sqrt(mu) * f_emp,
    }


def endpoint_parameters() -> dict[str, float]:
    r = 2.0
    rho_full = 6.2407571
    beta = 0.90
    # Same surrogate endpoint used in Step 26.
    x_inf = 7.73248
    # scipy-free hard-coded Phi^-1(0.90)
    z_beta = 1.2815515655446004

    x_f = x_inf
    x_s = x_inf / r
    b_f = b_coeff(x_f)
    b_s = b_coeff(x_s)
    u_f = rho_full * math.sqrt(eta(x_f)) - z_beta
    u_s = rho_full * math.sqrt(eta(x_s)) - z_beta
    chi_f = a_coeff(x_f) * u_f / math.sqrt(b_f)
    chi_s = a_coeff(x_s) * u_s / math.sqrt(b_s)

    mu_per_kappa_f = chi_f ** (1.0 / 3.0) / (u_f * math.sqrt(b_f))
    mu_per_kappa_s = r * chi_s ** (1.0 / 3.0) / (u_s * math.sqrt(b_s))

    return {
        "r": r,
        "x_f": x_f,
        "x_s": x_s,
        "u_f": u_f,
        "u_s": u_s,
        "b_f": b_f,
        "b_s": b_s,
        "chi_f": chi_f,
        "chi_s": chi_s,
        "mu_per_kappa_f": mu_per_kappa_f,
        "mu_per_kappa_s": mu_per_kappa_s,
    }


def main() -> None:
    # Step-27 paired values: sqrt(zeta) * [H_mix-H(chi,zeta)].
    data = {
        1.1395336491335272e-4: {20.0: 0.00579, 40.0: 0.00651, 80.0: 0.00681},
        0.06454723600738278: {20.0: 0.2037, 40.0: 0.2072, 80.0: 0.2116},
        0.1: {20.0: 0.2757, 40.0: 0.2760, 80.0: 0.2783},
    }

    print("Step-27 data in Step-29 double-scaling variables")
    print("chi              zeta      mu        F_emp      sqrt(mu)F")
    for chi, zmap in data.items():
        for zeta, gap in zmap.items():
            row = collapse_row(chi, zeta, gap)
            print(
                f"{chi: .8e}  {zeta:6.1f}  {row['mu']:8.3f}  "
                f"{row['F_emp']:9.4f}  {row['sqrt_mu_F']:10.4f}"
            )
        print()

    ep = endpoint_parameters()
    print("Physical r=2 endpoint double-scaling rates")
    for key, value in ep.items():
        print(f"{key}: {value}")

    print("\nmu along physical kappa_f sweep")
    print("kappa_f      mu_fast      mu_slow")
    for kappa in [100.0, 200.0, 300.0, 1000.0, 10000.0]:
        print(
            f"{kappa:8.1f}  "
            f"{ep['mu_per_kappa_f'] * kappa:10.3f}  "
            f"{ep['mu_per_kappa_s'] * kappa:10.3f}"
        )

    print("\nNominal fast-channel crossover scales")
    for target_mu in [1.0, 10.0, 100.0]:
        print(
            f"mu_fast={target_mu:g}: "
            f"kappa_f={target_mu / ep['mu_per_kappa_f']:.3f}"
        )

    h0 = 1.0 / SQRT_PI
    endpoint_h = [
        (ep["chi_f"], 0.5660),
        (ep["chi_s"], 0.7133),
        (0.1, 0.76698),
    ]
    print("\nIndependent H_mix-H0 versus chi^(2/3) check")
    print("chi              Hmix-H0      chi^(2/3)    ratio")
    for chi, hmix in endpoint_h:
        diff = hmix - h0
        scale = chi ** (2.0 / 3.0)
        print(f"{chi: .8e}  {diff:10.6f}  {scale:10.6f}  {diff/scale:8.3f}")


if __name__ == "__main__":
    main()
