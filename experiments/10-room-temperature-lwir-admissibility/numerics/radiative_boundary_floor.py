#!/usr/bin/env python3
"""Reproduce the ideal external radiative boundary benchmark for Experiment 10.

Analytical/theoretical support only. No experimental workflow.
"""

import math
from scipy.integrate import quad

H = 6.62607015e-34
C = 299792458.0
KB = 1.380649e-23
Q = 1.602176634e-19

T = 300.0
LAMBDA_C = 10e-6
EG = H * C / LAMBDA_C
XG = EG / (KB * T)


def planck_tail_integrand(x: float) -> float:
    if x > 50.0:
        return x * x * math.exp(-x)
    return x * x / math.expm1(x)


I2 = quad(planck_tail_integrand, XG, math.inf, epsabs=1e-14)[0]
PHI0_M2 = 2.0 * math.pi * (KB * T) ** 3 / (H**3 * C**2) * I2
PHI0_CM2 = PHI0_M2 / 1e4
J0_CM2 = Q * PHI0_CM2
N_EDGE = 1.0 / math.expm1(XG)
I2_BOLTZ = (XG * XG + 2.0 * XG + 2.0) * math.exp(-XG)

print(f"Eg/kBT = {XG:.12f}")
print(f"I2 exact = {I2:.12f}")
print(f"I2 Boltzmann-tail = {I2_BOLTZ:.12f}")
print(f"Boltzmann-tail relative error = {(I2_BOLTZ / I2 - 1.0):.6%}")
print(f"Phi0 = {PHI0_CM2:.8e} cm^-2 s^-1")
print(f"2 Phi0 = {2.0 * PHI0_CM2:.8e} cm^-2 s^-1")
print(f"q Phi0 = {J0_CM2:.8f} A/cm^2")
print(f"n_B(Eg) = {N_EDGE:.10f}")

# Previously derived exact K_th/kBT witnesses from the scalar-asymmetry model.
thresholds = {
    0.40: 5.873,
    0.20: 7.536,
    0.10: 9.470,
    0.08476: 10.000,
    0.04: 12.848,
    0.02: 16.273,
    0.01: 20.675,
}

print("\nA_m      K_th/kBT      exp[-(K_th-Eg/2)/kBT]")
for asym, kth_over_kbt in thresholds.items():
    ratio = math.exp(-(kth_over_kbt - XG / 2.0))
    print(f"{asym:<8g} {kth_over_kbt:>10.3f}      {ratio:.8e}")

min_kth_over_eg = math.sqrt(3.0) / 2.0
min_extra_exp = math.exp(-(min_kth_over_eg - 0.5) * XG)
print("\nPositive-curvature scalar model:")
print(f"min K_th/Eg = {min_kth_over_eg:.12f}")
print(f"max direct-Auger/radiative exponential ratio = {min_extra_exp:.8e}")
