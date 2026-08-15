"""Reproduce the Experiment-12 10-um / 300-K single-pass column bound."""

import math

EPS0 = 8.8541878128e-12
C = 299792458.0
HBAR = 1.054571817e-34
E_CHARGE = 1.602176634e-19
KB = 1.380649e-23

T = 300.0
LAMBDA = 10e-6
N_B = 3.5
A0 = 0.90
FRACTIONAL_BANDWIDTH = 0.10

omega0 = 2.0 * math.pi * C / LAMBDA
Egamma = HBAR * omega0
x = Egamma / (KB * T)
zeta0 = -math.log(1.0 - A0)
domega = FRACTIONAL_BANDWIDTH * omega0
thermal_factor = 1.0 / (math.exp(x / 2.0) - 1.0)


def sigma_column_min(vmax: float) -> float:
    """Minimum electron column in m^-2 for the narrowband single-pass corollary."""
    return (
        N_B
        * EPS0
        * C
        * Egamma
        * zeta0
        * domega
        / (math.pi * E_CHARGE**2 * vmax**2)
        * thermal_factor
    )


print(f"Egamma/kBT = {x:.9f}")
print(f"thermal factor = {thermal_factor:.9f}")
print(f"zeta0 = {zeta0:.9f}")
print()
print("vmax (m/s)      Sigma_min (cm^-2)")
for vmax in (5e5, 1e6, 1.07e6, 2e6, 3e6):
    sigma_cm2 = sigma_column_min(vmax) / 1e4
    print(f"{vmax:10.3e}      {sigma_cm2:12.6e}")
