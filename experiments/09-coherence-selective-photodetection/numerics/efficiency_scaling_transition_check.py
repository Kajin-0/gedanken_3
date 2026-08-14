#!/usr/bin/env python3
"""Exact finite-N checks for the Experiment-09 efficiency scaling theorem.

The script compares the exact one-body extraction/dephasing kernels with the
large-N subcritical, critical, and supercritical asymptotic formulas.

Default illustrative parameters are dimensionless:
    kappa = 10
    gamma = 1
    d = 1

They are chosen for transparent numerical separation and are not material
parameters or detector design recommendations.
"""

from __future__ import annotations

import math

from scipy.optimize import brentq
from scipy.special import lambertw


def exact_rates(N: int, kappa: float, gamma: float) -> tuple[float, float, float]:
    a = kappa + gamma
    delta = math.sqrt(a * a - 4.0 * kappa * gamma / N)
    r_minus = 0.5 * (a - delta)
    r_plus = 0.5 * (a + delta)
    return r_minus, r_plus, delta


def surviving_probability(
    t: float, N: int, kappa: float, gamma: float, b0: float
) -> float:
    r_minus, r_plus, delta = exact_rates(N, kappa, gamma)
    A = (r_plus - kappa * b0) / delta
    B = (kappa * b0 - r_minus) / delta
    return A * math.exp(-r_minus * t) + B * math.exp(-r_plus * t)


def collection_probability(
    t: float, N: int, kappa: float, gamma: float, b0: float
) -> float:
    return 1.0 - surviving_probability(t, N, kappa, gamma, b0)


def minimal_gate(N: int, kappa: float, gamma: float, eta: float) -> float:
    def residual(t: float) -> float:
        return collection_probability(t, N, kappa, gamma, 1.0) - eta

    hi = 1.0 / max(kappa + gamma, 1.0e-15)
    while residual(hi) < 0.0:
        hi *= 2.0
    return float(brentq(residual, 0.0, hi, xtol=1.0e-13, rtol=1.0e-13))


def exact_dark_mean(
    N: int, kappa: float, gamma: float, d: float, eta: float
) -> tuple[float, float]:
    T = minimal_gate(N, kappa, gamma, eta)
    r_minus, r_plus, delta = exact_rates(N, kappa, gamma)
    b0 = 1.0 / N
    A = (r_plus - kappa * b0) / delta
    B = (kappa * b0 - r_minus) / delta
    integral = (
        T
        - A / r_minus * (1.0 - math.exp(-r_minus * T))
        - B / r_plus * (1.0 - math.exp(-r_plus * T))
    )
    return T, N * d * integral


def subcritical_limit(
    kappa: float, gamma: float, d: float, eta: float
) -> tuple[float, float]:
    a = kappa + gamma
    q = kappa / a
    x = -math.log(1.0 - eta / q)
    T = x / a
    mu = d / a * (
        0.5 * q * (1.0 - q) * x * x + q * q * x - q * eta
    )
    return T, mu


def supercritical_limit(
    kappa: float, gamma: float, d: float, eta: float
) -> tuple[float, float]:
    a = kappa + gamma
    q = kappa / a
    lam = kappa * gamma / a
    log_ratio = math.log((1.0 - q) / (1.0 - eta))
    T_over_N = log_ratio / lam
    mu_over_N2 = d / lam * (log_ratio - (eta - q) / (1.0 - q))
    return T_over_N, mu_over_N2


def critical_leading(
    N: int, kappa: float, gamma: float, d: float
) -> tuple[float, float]:
    a = kappa + gamma
    q = kappa / a
    x = float(lambertw(N / (1.0 - q) ** 2).real)
    T = x / a
    mu = d / a * (
        0.5 * q * (1.0 - q) * x * x
        + q * q * x
        - q * q * (1.0 - math.exp(-x))
    )
    return T, mu


def main() -> None:
    kappa = 10.0
    gamma = 1.0
    d = 1.0
    q = kappa / (kappa + gamma)

    print("Experiment 09 efficiency scaling transition check")
    print(f"kappa={kappa:g} gamma={gamma:g} d={d:g} eta_c=q={q:.12f}")
    print()

    for eta in (0.50, 0.90):
        T_inf, mu_inf = subcritical_limit(kappa, gamma, d, eta)
        print(f"SUBCRITICAL eta={eta:.6f}")
        print(f"  asymptotic T={T_inf:.12f} mu={mu_inf:.12f}")
        for N in (100, 1000, 10000):
            T, mu = exact_dark_mean(N, kappa, gamma, d, eta)
            print(f"  N={N:5d}: T={T:.12f} mu={mu:.12f}")
        print()

    for eta in (0.95, 0.99):
        T_over_N, mu_over_N2 = supercritical_limit(kappa, gamma, d, eta)
        print(f"SUPERCRITICAL eta={eta:.6f}")
        print(
            f"  asymptotic T/N={T_over_N:.12f} "
            f"mu/N^2={mu_over_N2:.12f}"
        )
        for N in (100, 1000, 10000):
            T, mu = exact_dark_mean(N, kappa, gamma, d, eta)
            print(
                f"  N={N:5d}: T/N={T/N:.12f} "
                f"mu/N^2={mu/(N*N):.12f}"
            )
        print()

    print(f"CRITICAL eta=q={q:.12f}")
    for N in (100, 1000, 10000, 1000000):
        T, mu = exact_dark_mean(N, kappa, gamma, d, q)
        T_lead, mu_lead = critical_leading(N, kappa, gamma, d)
        print(
            f"  N={N:7d}: exact T={T:.9f} mu={mu:.9f}; "
            f"leading T={T_lead:.9f} mu={mu_lead:.9f}"
        )


if __name__ == "__main__":
    main()
