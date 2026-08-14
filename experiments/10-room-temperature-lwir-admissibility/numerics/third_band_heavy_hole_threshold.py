#!/usr/bin/env python3
"""Reproduce Experiment-10 minimal third-band heavy-hole Auger thresholds.

Model (energies in units of Delta = Eg/2):
    e(q) = sqrt(1+q^2)
    h_hh(q) = 1 + eta + q^2/(2 rho)

with
    rho = M_hh v^2 / Delta = M_hh/m_D
    eta = delta_hh/Delta.

For fixed total momentum q0, the minimum final e+e+h_hh energy is
parameterized by the common group velocity u:
    x = u/sqrt(1-u^2)
    z = rho*u
    q0 = 2*x + z
    F = 2/sqrt(1-u^2) + 1 + eta + rho*u^2/2.

The channel is closed for rho <= 2(1+eta); otherwise there is one finite
threshold satisfying F = sqrt(1+q0^2).
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Optional

from scipy.optimize import brentq


@dataclass(frozen=True)
class Threshold:
    rho: float
    eta: float
    u: float
    q: float
    k_over_delta: float

    @property
    def k_over_eg(self) -> float:
        return self.k_over_delta / 2.0


def mismatch_u(u: float, rho: float, eta: float) -> tuple[float, float, float]:
    gamma = 1.0 / math.sqrt(1.0 - u * u)
    q = u * (2.0 * gamma + rho)
    final = 2.0 * gamma + 1.0 + eta + 0.5 * rho * u * u
    initial = math.sqrt(1.0 + q * q)
    return final - initial, q, final


def threshold(rho: float, eta: float = 0.0) -> Optional[Threshold]:
    rho_c = 2.0 * (1.0 + eta)
    if rho <= rho_c:
        return None

    root = brentq(
        lambda u: mismatch_u(u, rho, eta)[0],
        0.0,
        1.0 - 1e-13,
        xtol=1e-14,
        rtol=1e-13,
    )
    _, q, initial = mismatch_u(root, rho, eta)
    return Threshold(rho, eta, root, q, initial - 1.0)


def main() -> None:
    eg_over_kbt = 4.795922925
    delta_over_kbt = eg_over_kbt / 2.0

    print("touching heavy-hole branch: eta=0")
    print("rho      q_th       K/Eg       K/kBT      exp[-(K-Eg/2)/kBT]")
    for rho in (2.1, 2.5, 3, 4, 5, 10, 20, 50, 100):
        th = threshold(rho, 0.0)
        assert th is not None
        k_kbt = th.k_over_eg * eg_over_kbt
        rel_exp = math.exp(-(k_kbt - delta_over_kbt))
        print(
            f"{rho:5.1f}  {th.q:9.3f}  {th.k_over_eg:9.3f}  "
            f"{k_kbt:9.3f}  {rel_exp:16.3e}"
        )

    flat_rel = math.exp(-delta_over_kbt)
    print("\nflat-band rho->infinity limit")
    print(f"K/Eg -> 1 for eta=0")
    print(f"relative radiative activation -> {flat_rel:.6f}")

    print("\nclosure mass ceiling for the 10-um target, eta=0")
    eV = 1.602176634e-19
    m0 = 9.1093837015e-31
    eg_eV = 0.1239841984
    for v in (5e5, 1e6, 1.07e6, 2e6, 3e6):
        mmax = eg_eV * eV / (v * v)
        print(f"v={v:8.3e} m/s   M_hh^max/m0={mmax/m0:.6f}")


if __name__ == "__main__":
    main()
