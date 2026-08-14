#!/usr/bin/env python3
import math

KB_EV_K = 8.617333262e-5
T_K = 77.0
KT_MEV = KB_EV_K*T_K*1e3

# Standard atomic weights and generous stable-isotope endpoints.
AW = {"Hg":200.59, "Cd":112.414, "Te":127.60}
ISO = {"Hg":(196.0,204.0), "Cd":(106.0,116.0), "Te":(120.0,130.0)}

def mu(a,b):
    return a*b/(a+b)

def omega_ratio(a,b,a0,b0):
    # Harmonic diatomic scale omega ~ mu^{-1/2}
    return math.sqrt(mu(a0,b0)/mu(a,b))

def eligible_fraction(delta_mev):
    # Fraction of a 3-D Maxwell-Boltzmann kinetic-energy distribution with E < delta.
    if delta_mev <= 0:
        return 0.0
    u = delta_mev/KT_MEV
    return math.erf(math.sqrt(u)) - 2/math.sqrt(math.pi)*math.sqrt(u)*math.exp(-u)

def shell_weight(delta_mev):
    # Minimal single-dispersionless-phonon carrier phase-space scale.
    # Not a capture coefficient: proportional only to sqrt(E)*exp(-E/kT), E=delta.
    if delta_mev <= 0:
        return 0.0
    return math.sqrt(delta_mev)*math.exp(-delta_mev/KT_MEV)

print(f"T={T_K:g} K, kT={KT_MEV:.6f} meV")
for cation in ("Hg","Cd"):
    r_light = omega_ratio(ISO[cation][0],ISO['Te'][0],AW[cation],AW['Te'])
    r_heavy = omega_ratio(ISO[cation][1],ISO['Te'][1],AW[cation],AW['Te'])
    print(f"{cation}Te-like omega(light)/omega(natural)={r_light:.6f}")
    print(f"{cation}Te-like omega(heavy)/omega(natural)={r_heavy:.6f}")
    print(f"{cation}Te-like full light-to-heavy span={(r_light/r_heavy-1)*100:.3f}%")

# Acoustic cutoff stress: values quoted in HgCdTe vacancy-capture literature.
for label, emax, ratio_h in (
    ("HgTe-like LA",10.56,omega_ratio(ISO['Hg'][1],ISO['Te'][1],AW['Hg'],AW['Te'])),
    ("CdTe-like LA",13.40,omega_ratio(ISO['Cd'][1],ISO['Te'][1],AW['Cd'],AW['Te'])),
):
    eh = emax*ratio_h
    print(f"\n{label}: natural {emax:.4f} meV; heavy-isotope estimate {eh:.4f} meV")
    for eb in (9.8,10.0,10.1,10.2,10.3,10.4,10.5,12.0,12.5,12.8,13.0):
        fn = eligible_fraction(emax-eb)
        fh = eligible_fraction(eh-eb)
        if fn > 0:
            print(f"Eb={eb:4.1f} meV: F_nat={fn:.6g}, F_heavy={fh:.6g}, ratio={fh/fn:.4g}")

# Optical-phonon threshold stress using representative HgTe-like LO scale ~143 cm^-1.
CM_TO_MEV = 0.1239841984
EOP = 143.0*CM_TO_MEV
RH = omega_ratio(ISO['Hg'][1],ISO['Te'][1],AW['Hg'],AW['Te'])
EOP_H = EOP*RH
print(f"\nHgTe-like optical mode: natural {EOP:.4f} meV; heavy estimate {EOP_H:.4f} meV")
for eb in (17.0,17.3,17.5,17.55,17.6,17.7):
    wn=shell_weight(EOP-eb); wh=shell_weight(EOP_H-eb)
    ratio=wh/wn if wn>0 else float('nan')
    print(f"Eb={eb:.2f}: shell_nat={wn:.6g}, shell_heavy={wh:.6g}, ratio={ratio:.4g}")
