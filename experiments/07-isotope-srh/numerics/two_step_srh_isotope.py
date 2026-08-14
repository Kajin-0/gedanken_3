#!/usr/bin/env python3
"""Reduced-order isotope sensitivity test for HgCdTe SRH capture.

This is a stress model, not a microscopic capture calculation.  It asks how much
natural->heavy isotope substitution can change a sequential two-capture SRH cycle
once a finite capture-energy spread and an isotope-insensitive bypass are allowed.
"""

import math
import numpy as np
from numpy.polynomial.hermite import hermgauss

T_K = 77.0
KB_MEV_K = 8.617333262e-2
KT = KB_MEV_K * T_K
CM1_TO_MEV = 0.1239841984

AW_HG = 200.59
AW_TE = 127.60
M_HG_HEAVY = 204.0
M_TE_HEAVY = 130.0


def mu(a, b):
    return a * b / (a + b)


def omega_ratio(a, b, a0, b0):
    return math.sqrt(mu(a0, b0) / mu(a, b))


R_HEAVY = omega_ratio(M_HG_HEAVY, M_TE_HEAVY, AW_HG, AW_TE)
EOP_NAT = 143.0 * CM1_TO_MEV
EOP_HEAVY = EOP_NAT * R_HEAVY
ELA_NAT = 10.56
ELA_HEAVY = ELA_NAT * R_HEAVY

# Gauss-Hermite quadrature for a Gaussian distribution of relative
# defect/phonon capture energy with standard deviation sigma_E.
XH, WH = hermgauss(64)
WH = WH / math.sqrt(math.pi)


def erf_array(x):
    return np.vectorize(math.erf)(x)


def acoustic_phase(delta):
    """Fraction of 3-D MB carriers with E < delta."""
    delta = np.asarray(delta, dtype=float)
    out = np.zeros_like(delta)
    mask = delta > 0
    u = delta[mask] / KT
    out[mask] = (
        erf_array(np.sqrt(u))
        - 2.0 / math.sqrt(math.pi) * np.sqrt(u) * np.exp(-u)
    )
    return out


def optical_phase(delta):
    """Minimal single-optical-phonon 3-D phase-space proxy."""
    delta = np.asarray(delta, dtype=float)
    return np.where(
        delta > 0,
        np.sqrt(np.maximum(delta, 0.0)) * np.exp(-np.maximum(delta, 0.0) / KT),
        0.0,
    )


def averaged_phase(E0, sigma_E, Ephonon, kind):
    E0 = np.atleast_1d(E0).astype(float)
    if sigma_E <= 0:
        delta = Ephonon - E0
        return acoustic_phase(delta) if kind == "acoustic" else optical_phase(delta)

    Eb = E0[:, None] + math.sqrt(2.0) * sigma_E * XH[None, :]
    delta = Ephonon - Eb
    val = acoustic_phase(delta) if kind == "acoustic" else optical_phase(delta)
    return val @ WH


def capture_ratio(E0, sigma_E, E_nat, E_heavy, kind, f_ref, delta_ref=1.0):
    """Heavy/natural capture-rate ratio with a fixed bypass.

    f_ref is the fraction of the NATURAL capture rate supplied by the isotope-
    sensitive one-phonon path at E0=E_nat-delta_ref.  The absolute bypass is then
    held fixed while E0 and isotope mass are varied.
    """
    phi_ref = averaged_phase(np.array([E_nat - delta_ref]), sigma_E, E_nat, kind)[0]
    bypass = phi_ref * (1.0 - f_ref) / f_ref if f_ref < 1.0 else 0.0
    pn = averaged_phase(E0, sigma_E, E_nat, kind)
    ph = averaged_phase(E0, sigma_E, E_heavy, kind)
    return (bypass + ph) / (bypass + pn)


def cycle_ratio(Rn, Rp, b=1.0):
    """Heavy/natural sequential SRH-cycle rate ratio.

    b = r_n,natural / r_p,natural.
    """
    return Rn * Rp * (b + 1.0) / (Rn * b + Rp)


def minimum_ratio(sigma_E, f_ref, kind="optical", both=True, b=1.0):
    E_nat = EOP_NAT if kind == "optical" else ELA_NAT
    E_heavy = EOP_HEAVY if kind == "optical" else ELA_HEAVY
    E0 = np.linspace(E_nat - 3.0, E_nat + 2.0, 30001)
    R = capture_ratio(E0, sigma_E, E_nat, E_heavy, kind, f_ref)
    G = R if both else cycle_ratio(R, np.ones_like(R), b=b)
    i = np.nanargmin(G)
    return float(G[i]), float(E0[i])


def critical_sensitive_fraction(sigma_E, kind="optical", target=0.5):
    """Minimum f_ref for which the best tuned BOTH-sensitive cycle reaches target."""
    lo, hi = 0.5, 0.999999999
    if minimum_ratio(sigma_E, hi, kind=kind, both=True)[0] > target:
        return None
    for _ in range(50):
        mid = 0.5 * (lo + hi)
        if minimum_ratio(sigma_E, mid, kind=kind, both=True)[0] <= target:
            hi = mid
        else:
            lo = mid
    return hi


def main():
    sigma_raman = (8.9 * CM1_TO_MEV) / 2.354820045

    print(f"T={T_K:g} K, kT={KT:.6f} meV")
    print(f"HgTe-like heavy/natural frequency ratio={R_HEAVY:.9f}")
    print(f"LA: {ELA_NAT:.6f} -> {ELA_HEAVY:.6f} meV")
    print(f"LO(143 cm^-1): {EOP_NAT:.6f} -> {EOP_HEAVY:.6f} meV")
    print(f"8.9 cm^-1 FWHM -> sigma_E={sigma_raman:.6f} meV\n")

    print("Minimum heavy/natural SRH-cycle rate, both captures equally sensitive")
    print("sigma_E(meV)  f_ref   acoustic   optical")
    for sigma in (0.0, 0.05, 0.10, 0.20, 0.30, sigma_raman, 0.50):
        for f in (0.75, 0.90, 0.99, 1.00):
            ga = minimum_ratio(sigma, f, kind="acoustic", both=True)[0]
            go = minimum_ratio(sigma, f, kind="optical", both=True)[0]
            print(f"{sigma:11.4f}  {f:5.2f}   {ga:8.4f}   {go:8.4f}")
        print()

    print("Critical natural one-phonon fraction f_ref for >=2x rate suppression")
    print("sigma_E(meV)  acoustic   optical")
    for sigma in (0.0, 0.05, 0.10, 0.20, 0.30, sigma_raman, 0.50):
        fa = critical_sensitive_fraction(sigma, kind="acoustic")
        fo = critical_sensitive_fraction(sigma, kind="optical")
        print(f"{sigma:11.4f}  {fa!s:>8}   {fo!s:>8}")

    print("\nOne-sensitive-step example at sigma_E=0.10 meV (optical phonon)")
    for b in (0.1, 1.0, 10.0):
        for f in (0.90, 0.99, 1.0):
            g, e0 = minimum_ratio(0.10, f, kind="optical", both=False, b=b)
            print(f"b={b:4.1f}, f_ref={f:4.2f}: min g_heavy/g_nat={g:.4f} at Eb={e0:.4f} meV")


if __name__ == "__main__":
    main()
