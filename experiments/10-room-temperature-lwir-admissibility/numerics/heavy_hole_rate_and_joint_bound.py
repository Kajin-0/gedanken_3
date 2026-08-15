#!/usr/bin/env python3
"""Reproduce heavy-hole CCCH threshold phase-space factors and exact-closure column bounds.

Analytical/theoretical helper for Experiment 10.
No empirical Auger coefficient is used.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
from scipy.optimize import brentq


@dataclass(frozen=True)
class ThresholdResult:
    rho: float
    eta: float
    u: float
    q: float
    K_over_Delta: float
    x: float
    z: float
    det_H: float
    gamma: float
    reduced_phase_prefactor: float


def q_of_u(u: float, rho: float) -> float:
    return 2.0 * u / math.sqrt(1.0 - u * u) + rho * u


def final_energy_over_delta(u: float, rho: float, eta: float) -> float:
    return (
        2.0 / math.sqrt(1.0 - u * u)
        + 1.0
        + eta
        + 0.5 * rho * u * u
    )


def mismatch(u: float, rho: float, eta: float) -> float:
    q = q_of_u(u, rho)
    return final_energy_over_delta(u, rho, eta) - math.sqrt(1.0 + q * q)


def threshold(rho: float, eta: float = 0.0) -> ThresholdResult | None:
    rho_c = 2.0 * (1.0 + eta)
    if rho <= rho_c:
        return None

    # mismatch is positive at u=0 and negative near u=1 on the open side.
    u = brentq(lambda t: mismatch(t, rho, eta), 0.0, 1.0 - 1e-12)
    q = q_of_u(u, rho)
    e0 = math.sqrt(1.0 + q * q)
    K_over_Delta = e0 - 1.0

    x = u / math.sqrt(1.0 - u * u)
    z = rho * u

    a_perp = math.sqrt(1.0 - u * u)
    a_parallel = (1.0 - u * u) ** 1.5
    c = 1.0 / rho

    det_H = (
        a_parallel * (a_parallel + 2.0 * c)
        * (a_perp * (a_perp + 2.0 * c)) ** 2
    )

    v0_q = q / math.sqrt(1.0 + q * q)
    gamma = 1.0 - u / v0_q
    reduced_phase_prefactor = gamma * gamma / math.sqrt(det_H)

    return ThresholdResult(
        rho=rho,
        eta=eta,
        u=u,
        q=q,
        K_over_Delta=K_over_Delta,
        x=x,
        z=z,
        det_H=det_H,
        gamma=gamma,
        reduced_phase_prefactor=reduced_phase_prefactor,
    )


def near_closure_phase_asymptote(rho: float, eta: float = 0.0) -> float:
    rho_c = 2.0 * (1.0 + eta)
    drho = rho - rho_c
    if drho <= 0:
        return 0.0
    return math.sqrt(3.0) * rho_c ** 1.5 / 64.0 * drho ** 1.5


def closure_column_bound(
    C: float,
    Eg_eV: float,
    M_hh_over_m0: float,
    delta_hh_eV: float = 0.0,
) -> tuple[float, float]:
    """Return (v_c [m/s], Sigma_min [cm^-2]) for exact CCCH closure."""
    e = 1.602176634e-19
    m0 = 9.1093837015e-31
    Eg_J = Eg_eV * e
    delta_J = delta_hh_eV * e
    Delta_J = 0.5 * Eg_J
    M = M_hh_over_m0 * m0

    vc2 = 2.0 * (Delta_J + delta_J) / M
    vc = math.sqrt(vc2)
    sigma_m2 = C / vc2
    return vc, sigma_m2 / 1e4


def main() -> None:
    print("Open-side threshold geometry, eta=0")
    print(
        "rho      Kth/Eg      gamma       det(H)        P_red        P_asympt"
    )
    for rho in (2.05, 2.10, 2.50, 3.0, 4.0, 5.0, 10.0, 20.0, 50.0, 100.0, 1000.0):
        r = threshold(rho, 0.0)
        assert r is not None
        print(
            f"{rho:6.2f}  {r.K_over_Delta/2.0:10.6f}  "
            f"{r.gamma:10.4e}  {r.det_H:12.4e}  "
            f"{r.reduced_phase_prefactor:10.4e}  "
            f"{near_closure_phase_asymptote(rho):10.4e}"
        )

    print("\nNear-closure checks")
    for drho in (0.20, 0.10, 0.05, 0.02):
        rho = 2.0 + drho
        r = threshold(rho, 0.0)
        assert r is not None
        print(
            f"drho={drho:.3f}: qth={r.q:.6f}, 3/drho={3/drho:.6f}, "
            f"P/P_asym={r.reduced_phase_prefactor/near_closure_phase_asymptote(rho):.6f}"
        )

    print("\nExact-closure matched-column bound at 10 um / 300 K witness")
    C = 1.0666799497e29  # m^-2 (m/s)^2
    Eg_eV = 0.1239841984
    print("Mhh/m0      vc (m/s)      Sigma_min (cm^-2)")
    for mr in (0.50, 0.20, 0.10, 0.05, 0.02):
        vc, sigma = closure_column_bound(C, Eg_eV, mr, 0.0)
        print(f"{mr:6.3f}   {vc:11.4e}   {sigma:14.6e}")


if __name__ == "__main__":
    main()
