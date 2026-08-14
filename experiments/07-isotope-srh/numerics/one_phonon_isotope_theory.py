#!/usr/bin/env python3
"""Reduced-order analytical checks for Experiment 07.

Pure theory only.  Evaluates a single-optical-phonon capture surrogate with
quantized displacement matrix-element scaling, Bose factor, 3-D thermal carrier
phase space, and optional Gaussian energy broadening.
"""
import math
import numpy as np
from scipy.integrate import quad

KB_MEV_K = 8.617333262e-2
CM1_TO_MEV = 0.1239841984

M_HG = 200.59
M_HG_204 = 204.0
M_TE = 127.60
HW_NAT = 143.0 * CM1_TO_MEV


def mu(a, b):
    return a*b/(a+b)


def hg_frequency_ratio():
    return math.sqrt(mu(M_HG, M_TE)/mu(M_HG_204, M_TE))


def bose(hw, T):
    x = hw/(KB_MEV_K*T)
    return 1.0/(math.exp(x)-1.0)


def phase_sharp(delta, T):
    if delta <= 0:
        return 0.0
    return math.sqrt(delta)*math.exp(-delta/(KB_MEV_K*T))


def phase_broadened(delta, sigma, T):
    if sigma <= 0:
        return phase_sharp(delta, T)
    upper = max(20.0*KB_MEV_K*T, max(delta, 0.0)+10.0*sigma, 20.0*sigma)
    norm = 1.0/(math.sqrt(2.0*math.pi)*sigma)
    def f(E):
        return math.sqrt(E)*math.exp(-E/(KB_MEV_K*T))*norm*math.exp(-(E-delta)**2/(2.0*sigma*sigma))
    return quad(f, 0.0, upper, epsabs=1e-13, epsrel=1e-10, limit=300)[0]


def capture(hw, delta, sigma, T):
    # For a diatomic relative coordinate with fixed force constant and electronic
    # derivative: |g|^2 ~ 1/(mu*omega) ~ omega.  Proportionality constants cancel.
    return hw*(bose(hw, T)+1.0)*phase_broadened(delta, sigma, T)


def sharp_log_mass_sensitivity(hw, delta, T, alpha):
    """d ln C / d ln M for fixed electronic separation E."""
    x = hw/(KB_MEV_K*T)
    N = bose(hw, T)
    return alpha*(-1.0 + x*(N+1.0) - hw/(2.0*delta))


def sign_crossing(hw, T):
    x = hw/(KB_MEV_K*T)
    N = bose(hw, T)
    denom = 2.0*(x*(N+1.0)-1.0)
    return hw/denom


def main():
    T = 77.0
    ratio = hg_frequency_ratio()
    hwA = HW_NAT
    hwB = hwA*ratio
    dhw = hwB-hwA
    alpha_hg = 0.5*M_TE/(M_HG+M_TE)

    print(f"T={T:g} K")
    print(f"Hg-only omega_B/omega_A={ratio:.9f}")
    print(f"hw: {hwA:.6f} -> {hwB:.6f} meV; shift={dhw:.6f} meV")
    print(f"alpha_Hg={alpha_hg:.9f}")
    print(f"sharp sign-crossing detuning={sign_crossing(hwA,T):.6f} meV")
    print()

    deltas = [0.0, 0.05, 0.10, 0.20, 0.50, 1.0, 2.0, 5.0]
    sigmas = [0.0, 0.10, 0.20, 0.47, 1.0]
    print("Heavy/natural capture ratio with fixed electronic separation")
    print("delta_A(meV) " + " ".join(f"sigma={s:g}" for s in sigmas))
    for d in deltas:
        vals = []
        for s in sigmas:
            A = capture(hwA, d, s, T)
            B = capture(hwB, d+dhw, s, T)
            vals.append(B/A if A > 0 else float('nan'))
        print(f"{d:11.3f} " + " ".join(f"{v:10.5f}" for v in vals))

    print("\nSharp-model logarithmic mass sensitivity")
    for d in [0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0]:
        print(f"delta={d:5.2f} meV  S_M={sharp_log_mass_sensitivity(hwA,d,T,alpha_hg): .6f}")


if __name__ == "__main__":
    main()
