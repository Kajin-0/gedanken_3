"""Validate the Experiment-12 global thermal-optical sum inequality on Dirac models.

The script reports:
1. the exact 2-D neutral massless-Dirac/graphene ratio (1/2) analytically;
2. the exact 3-D massless-Dirac ratio (2/3) analytically;
3. numerical bound/exact ratios for the 3-D massive-Dirac family.

Dimensionless units k_B T = hbar = v = e = N_D = 1 are used for the
3-D numerical ratio, so all dimensional prefactors cancel.
"""

import math
from scipy.integrate import quad


def fermi(E: float) -> float:
    if E > 50.0:
        return math.exp(-E)
    return 1.0 / (math.exp(E) + 1.0)


def bose_half(E: float) -> float:
    """1/[exp(E/2)-1] with stable large-E behavior."""
    if E / 2.0 > 50.0:
        return math.exp(-E / 2.0)
    return 1.0 / math.expm1(E / 2.0)


def massive_dirac_sigma(E: float, delta: float) -> float:
    """3-D massive-Dirac Re sigma in units e^2/(hbar v), with kBT=hbar=1."""
    if E <= 2.0 * delta:
        return 0.0
    root = math.sqrt(1.0 - 4.0 * delta * delta / (E * E))
    return (
        E
        / (12.0 * math.pi)
        * (1.0 + 2.0 * delta * delta / (E * E))
        * root
        * math.tanh(E / 4.0)
    )


def massive_dirac_ratio(delta: float) -> float:
    # Global theorem for total n_e+n_h:
    # n_bound = 2/(pi e^2 v^2) int d omega E sigma/(exp(E/2)-1).
    lower = 2.0 * delta
    upper = max(100.0, lower + 100.0)
    integral = quad(
        lambda E: E * massive_dirac_sigma(E, delta) * bose_half(E),
        lower,
        upper,
        epsabs=1e-12,
        limit=500,
    )[0]
    n_bound_total = 2.0 * integral / math.pi

    # Exact total thermal density = 2/pi^2 * F_2(delta).
    F2 = quad(
        lambda q: q * q * fermi(math.sqrt(q * q + delta * delta)),
        0.0,
        max(50.0, delta + 50.0),
        epsabs=1e-12,
        limit=500,
    )[0]
    n_exact_total = 2.0 * F2 / (math.pi * math.pi)
    return n_bound_total / n_exact_total


print("2-D neutral massless Dirac / graphene: bound/exact = 1/2")
print("3-D neutral massless Dirac:            bound/exact = 2/3")
print()
print("3-D massive Dirac")
print("Delta/kBT    bound/exact")
for delta in (0.0, 0.5, 1.0, 2.39796146, 4.0, 8.0, 16.0):
    print(f"{delta:9.6f}    {massive_dirac_ratio(delta):.9f}")
