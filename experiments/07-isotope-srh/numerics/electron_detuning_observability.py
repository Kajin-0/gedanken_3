#!/usr/bin/env python3
"""Reduced-order observability window for Experiment 07 electron capture.

This is a metrology scale calculation, not a microscopic V_Hg capture prediction.
Cn is deliberately swept over a broad bracket.
"""
import math

KB_MEV_K = 8.617333262e-2
KB_J_K = 1.380649e-23
H = 6.62607015e-34
M0 = 9.1093837015e-31

EG_EV = 0.040
MSTAR_REL = 0.071 * EG_EV  # standard HgCdTe scale used in detector modeling
MSTAR = MSTAR_REL * M0
ESEP_MEV = 17.5            # representative near-one-phonon electron separation


def Nc(T):
    """Parabolic-edge DOS scale, cm^-3."""
    return 2.0 * (2.0 * math.pi * MSTAR * KB_J_K * T / H**2)**1.5 / 1e6


def emission(Cn, T, Esep=ESEP_MEV):
    return Cn * Nc(T) * math.exp(-Esep / (KB_MEV_K * T))


def capture_time(Cn, nfill):
    return 1.0 / (Cn * nfill)


def sigma_delta_E(T, s_e, s_c, s_Nc):
    """A-B-A bracket uncertainty for independent per-state log errors."""
    s_log = math.sqrt(1.5 * (s_e**2 + s_c**2 + s_Nc**2))
    return KB_MEV_K * T * s_log


def main():
    CBRACKET = (1e-12, 1e-10, 1e-9, 1e-8)
    print(f"Eg={EG_EV*1e3:.1f} meV; m*/m0={MSTAR_REL:.6f}; Esep={ESEP_MEV:.2f} meV")
    print("\nEmission rate e_n [s^-1]")
    print("T(K)  " + "  ".join(f"Cn={c:.0e}" for c in CBRACKET))
    for T in (15, 20, 25, 30, 35, 40):
        vals = "  ".join(f"{emission(c,T):.4g}" for c in CBRACKET)
        print(f"{T:4d}  {vals}")

    print("\nDirect filling time tau_c [s]")
    for n in (1e13, 1e14, 1e15):
        vals = "  ".join(f"{capture_time(c,n):.4g}" for c in CBRACKET)
        print(f"nfill={n:.0e}: {vals}")

    print("\nA-B-A single-temperature electronic-separation uncertainty [meV]")
    print("assumes per-state log errors (e,C,Nc)=(0.5%,0.5%,0.2%) or (1%,1%,0.2%)")
    for T in (15,20,25,30,35,40):
        a=sigma_delta_E(T,.005,.005,.002)
        b=sigma_delta_E(T,.01,.01,.002)
        print(f"T={T:2d} K: {a:.5f}, {b:.5f}")

    # Differential closure: Y=Delta ln e - Delta ln C - Delta ln Nc = -Delta E/(kT)
    Ts=(20.,25.,30.,35.,40.)
    x=[1/(KB_MEV_K*T) for T in Ts]
    for se,sc,sn in ((.005,.005,.002),(.01,.01,.002)):
        sy=math.sqrt(1.5*(se*se+sc*sc+sn*sn))
        # no-intercept fit is the physical null if degeneracy/entropy do not change
        sigE0=sy/math.sqrt(sum(xx*xx for xx in x))
        xb=sum(x)/len(x)
        sigEfree=sy/math.sqrt(sum((xx-xb)**2 for xx in x))
        print(f"\n20-40 K differential fit, state errors {se:.3%},{sc:.3%},{sn:.3%}:")
        print(f"  sigma DeltaE, zero-intercept = {sigE0:.5f} meV")
        print(f"  sigma DeltaE, free intercept = {sigEfree:.5f} meV")


if __name__ == '__main__':
    main()
