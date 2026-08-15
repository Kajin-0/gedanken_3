"""Reproduce the corrected Experiment-12 10-um / 300-K single-pass window bound.

The useful frequency interval is [omega_g, 1.1 omega_g], i.e. a 10% band
above the 10-um absorption edge.  The thermal kernel is integrated exactly
rather than frozen at the band-edge value.
"""

import math
from scipy.integrate import quad

EPS0 = 8.8541878128e-12
C = 299792458.0
HBAR = 1.054571817e-34
E_CHARGE = 1.602176634e-19
KB = 1.380649e-23

T = 300.0
LAMBDA_G = 10e-6
N_B = 3.5
A0 = 0.90
FRACTIONAL_BANDWIDTH = 0.10

omega_g = 2.0 * math.pi * C / LAMBDA_G
omega_1 = omega_g
omega_2 = (1.0 + FRACTIONAL_BANDWIDTH) * omega_g
zeta0 = -math.log(1.0 - A0)


def thermal_kernel(omega: float) -> float:
    """K_T = hbar*omega/[exp(hbar*omega/(2 kBT))-1], in joules."""
    x = HBAR * omega / (2.0 * KB * T)
    return HBAR * omega / math.expm1(x)


kernel_integral = quad(thermal_kernel, omega_1, omega_2, epsabs=0.0, epsrel=1e-12)[0]

# Old narrow-band approximation, retained only to quantify the correction.
old_kernel_integral = thermal_kernel(omega_g) * (omega_2 - omega_1)
correction_ratio = kernel_integral / old_kernel_integral


def sigma_column_min(vstar: float) -> float:
    """Minimum intrinsic electron column in m^-2 for the single-pass corollary."""
    return (
        N_B
        * EPS0
        * C
        * zeta0
        * kernel_integral
        / (math.pi * E_CHARGE**2 * vstar**2)
    )


print(f"Eg/kBT = {HBAR * omega_g / (KB * T):.9f}")
print(f"zeta0 = {zeta0:.9f}")
print(f"window = [omega_g, {1.0 + FRACTIONAL_BANDWIDTH:.3f} omega_g]")
print(f"exact/constant-kernel ratio = {correction_ratio:.9f}")
print()
print("v_* (m/s)       Sigma_e,min (cm^-2)")
for vstar in (5e5, 1e6, 1.07e6, 2e6, 3e6):
    sigma_cm2 = sigma_column_min(vstar) / 1e4
    print(f"{vstar:10.3e}      {sigma_cm2:12.6e}")
