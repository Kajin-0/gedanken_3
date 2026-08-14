#!/usr/bin/env python3
"""Exact finite-N checks of the Experiment-09 rate-scaling phase diagram.

Uses the exact one-body extraction/dephasing kernels and the independent-particle
count lift. The examples are dimensionless theory checks, not material values.
"""

from __future__ import annotations

import math
from scipy.integrate import quad
from scipy.optimize import brentq


def rates(N: int, kappa: float, gamma: float):
    a = kappa + gamma
    delta = math.sqrt(a * a - 4.0 * kappa * gamma / N)
    return 0.5 * (a - delta), 0.5 * (a + delta), delta


def collection(t: float, N: int, kappa: float, gamma: float, b0: float) -> float:
    rm, rp, delta = rates(N, kappa, gamma)
    A = (rp - kappa * b0) / delta
    B = (kappa * b0 - rm) / delta
    return 1.0 - A * math.exp(-rm * t) - B * math.exp(-rp * t)


def minimal_gate(N: int, kappa: float, gamma: float, eta: float) -> float:
    f = lambda t: collection(t, N, kappa, gamma, 1.0) - eta
    hi = 1.0 / (kappa + gamma)
    while f(hi) < 0.0:
        hi *= 2.0
    return float(brentq(f, 0.0, hi, xtol=1e-13, rtol=1e-12))


def exact_point(
    N: int,
    kappa0: float,
    gamma0: float,
    alpha: float,
    beta: float,
    d: float,
    eta: float,
):
    kappa = kappa0 * N**alpha
    gamma = gamma0 * N**beta
    T = minimal_gate(N, kappa, gamma, eta)
    integrand = lambda u: collection(u, N, kappa, gamma, 1.0 / N)
    integral = quad(integrand, 0.0, T, epsabs=1e-12, epsrel=1e-10, limit=300)[0]
    return T, N * d * integral


def x_eta(eta: float) -> float:
    return -math.log(1.0 - eta)


def extraction_dominated_coeff(kappa0: float, d: float, eta: float):
    x = x_eta(eta)
    return x / kappa0, d * (x - eta) / kappa0


def dephasing_dominated_coeff(kappa0: float, d: float, eta: float):
    return extraction_dominated_coeff(kappa0, d, eta)


def balanced_subcritical_coeff(kappa0, gamma0, d, eta):
    A = kappa0 + gamma0
    q = kappa0 / A
    x = -math.log(1.0 - eta / q)
    T = x / A
    mu = d / A * (0.5 * q * (1.0 - q) * x * x + q * q * x - q * eta)
    return T, mu


def balanced_supercritical_coeff(kappa0, gamma0, d, eta):
    A = kappa0 + gamma0
    q = kappa0 / A
    lam = kappa0 * gamma0 / A
    L = math.log((1.0 - q) / (1.0 - eta))
    H = L - (eta - q) / (1.0 - q)
    return L / lam, d * H / lam


def show_case(name, alpha, beta, eta, kappa0=10.0, gamma0=1.0, d=1.0):
    print(name)
    print(f"  alpha={alpha:g} beta={beta:g} eta={eta:g}")

    if alpha > beta:
        Tcoef, mucoef = extraction_dominated_coeff(kappa0, d, eta)
        print(f"  predicted: T*N^alpha -> {Tcoef:.10f}")
        print(f"             mu*N^alpha -> {mucoef:.10f}")
        for N in (100, 1000, 10000):
            T, mu = exact_point(N, kappa0, gamma0, alpha, beta, d, eta)
            print(f"  N={N:5d}: {T*N**alpha:.10f}  {mu*N**alpha:.10f}")

    elif alpha < beta:
        Tcoef, mucoef = dephasing_dominated_coeff(kappa0, d, eta)
        print(f"  predicted: T/N^(1-alpha) -> {Tcoef:.10f}")
        print(f"             mu/N^(2-alpha) -> {mucoef:.10f}")
        for N in (100, 1000, 10000):
            T, mu = exact_point(N, kappa0, gamma0, alpha, beta, d, eta)
            print(
                f"  N={N:5d}: {T/N**(1-alpha):.10f}  "
                f"{mu/N**(2-alpha):.10f}"
            )

    else:
        q = kappa0 / (kappa0 + gamma0)
        if eta < q:
            Tcoef, mucoef = balanced_subcritical_coeff(kappa0, gamma0, d, eta)
            print(f"  q={q:.10f}; predicted T*N^alpha -> {Tcoef:.10f}")
            print(f"                 mu*N^alpha -> {mucoef:.10f}")
            for N in (100, 1000, 10000):
                T, mu = exact_point(N, kappa0, gamma0, alpha, beta, d, eta)
                print(f"  N={N:5d}: {T*N**alpha:.10f}  {mu*N**alpha:.10f}")
        elif eta > q:
            Tcoef, mucoef = balanced_supercritical_coeff(kappa0, gamma0, d, eta)
            print(f"  q={q:.10f}; predicted T/N^(1-alpha) -> {Tcoef:.10f}")
            print(f"                 mu/N^(2-alpha) -> {mucoef:.10f}")
            for N in (100, 1000, 10000):
                T, mu = exact_point(N, kappa0, gamma0, alpha, beta, d, eta)
                print(
                    f"  N={N:5d}: {T/N**(1-alpha):.10f}  "
                    f"{mu/N**(2-alpha):.10f}"
                )
        else:
            print("  critical eta=q: use logarithmic theorem / dedicated Rev.1 check")
    print()


def main():
    show_case("EXTRACTION DOMINATED", alpha=0.5, beta=0.0, eta=0.90)
    show_case("BALANCED SUBCRITICAL", alpha=0.5, beta=0.5, eta=0.50)
    show_case("BALANCED SUPERCRITICAL", alpha=0.5, beta=0.5, eta=0.95)
    show_case("DEPHASING DOMINATED", alpha=0.0, beta=0.5, eta=0.90)
    show_case("EXTRACTION DOMINATED BUT BOTH RATES SLOW", alpha=-0.5, beta=-1.0, eta=0.90)


if __name__ == "__main__":
    main()
