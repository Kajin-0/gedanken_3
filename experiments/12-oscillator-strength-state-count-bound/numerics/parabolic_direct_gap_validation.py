"""Finite-temperature validation of Experiment 12 for 3-D parabolic direct bands.

Units: k_B T = hbar = m_e = 1.  Overall DOS/spin constants cancel from
bound/exact ratios.
"""

from __future__ import annotations

import math
from scipy.integrate import quad
from scipy.optimize import brentq

EG_OVER_KBT = 4.795922925


def fermi_arg(x: float) -> float:
    if x > 50.0:
        return math.exp(-x)
    if x < -50.0:
        return 1.0 - math.exp(x)
    return 1.0 / (math.exp(x) + 1.0)


def inv_expm1(x: float) -> float:
    if x > 50.0:
        return math.exp(-x)
    return 1.0 / math.expm1(x)


def validate(mh_over_me: float) -> tuple[float, float, float]:
    me = 1.0
    mh = mh_over_me
    Eg = EG_OVER_KBT

    kmax = 20.0 * math.sqrt(max(me, mh, 1.0))

    def n_e(mu: float) -> float:
        return quad(
            lambda k: k * k * fermi_arg(Eg / 2.0 + k * k / (2.0 * me) - mu),
            0.0,
            kmax,
            epsabs=1e-11,
            limit=300,
        )[0]

    def n_h(mu: float) -> float:
        return quad(
            lambda k: k
            * k
            * (1.0 - fermi_arg(-Eg / 2.0 - k * k / (2.0 * mh) - mu)),
            0.0,
            kmax,
            epsabs=1e-11,
            limit=300,
        )[0]

    mu = brentq(lambda x: n_e(x) - n_h(x), -20.0, 20.0)
    exact = n_e(mu) + n_h(mu)

    def bound_integrand(k: float) -> float:
        Ec = Eg / 2.0 + k * k / (2.0 * me)
        Ev = -Eg / 2.0 - k * k / (2.0 * mh)
        D = fermi_arg(Ev - mu) - fermi_arg(Ec - mu)
        Ecv = Ec - Ev
        return 2.0 * k * k * D * inv_expm1(Ecv / 2.0)

    bound = quad(bound_integrand, 0.0, kmax, epsabs=1e-11, limit=300)[0]

    boltzmann_ratio = (4.0 * me * mh / (me + mh) ** 2) ** 0.75
    return mu, bound / exact, boltzmann_ratio


def main() -> None:
    print(f"Eg/kBT = {EG_OVER_KBT:.9f}")
    print("m_h/m_e      mu/kBT       bound/exact    Boltzmann")
    for ratio in (0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0):
        mu, exact_ratio, boltz = validate(ratio)
        print(f"{ratio:7.3f}    {mu:11.6f}    {exact_ratio:11.9f}    {boltz:11.9f}")


if __name__ == "__main__":
    main()
