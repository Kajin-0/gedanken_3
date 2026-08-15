#!/usr/bin/env python3
"""Lightweight one-at-a-time HgCdTe parameter sensitivity for Experiment 12.

Uses the same Hamiltonian and projected-block ordinary-supremum routines as the
production/audit scripts, but a deliberately reduced 24x4x6 quadrature because
this is a robustness diagnostic rather than the production value.
"""
import math
import kane_8band_tightness as k
import supremum_active_support_audit as a

NR, NMU, NPHI = 24, 4, 6
BASE = {name: getattr(k, name) for name in ("EP", "DELTA", "F", "G1", "G2", "G3")}


def set_parameters(values):
    for name, value in values.items():
        setattr(k, name, value)
    k.MUW = 0.5 * (k.G3 - k.G2)
    k.GBAR = 0.5 * (k.G3 + k.G2)
    k.P = math.sqrt(k.EP * k.A0)


def evaluate(values, seed):
    set_parameters(values)
    mu, _, _, ne_cross, nh_cross = k.carrier_state(kmax=2.0, nr=NR, nmu=NMU, nphi=NPHI)
    nref = ne_cross + nh_cross
    sampled = k.optical_bound(mu, nref, k.EG, 0.50, 1.0, nr=NR, nmu=NMU, nphi=NPHI)
    cap, _, _ = a.numerical_supremum(mu, k.EG, 0.50, 1.0, quantity="capacity", seed=seed)
    twice_weighted = sampled["bound"] * sampled["capacity"] ** 2
    bound = twice_weighted / cap**2
    return bound / nref, cap, mu, nref


def main():
    baseline = dict(BASE)
    r0 = evaluate(baseline, 20260870)
    print("diagnostic grid: 24 x 4 x 6")
    print(f"baseline ratio = {r0[0]:.9f}")
    ratios = []
    for i, name in enumerate(("EP", "DELTA", "F", "G1", "G2", "G3")):
        for fac in (0.95, 1.05):
            p = dict(BASE)
            p[name] *= fac
            ratio, cap, mu, nref = evaluate(p, 20260871 + 2*i + (fac > 1))
            ratios.append(ratio)
            print(f"{name:5s} x {fac:.2f}: ratio={ratio:.9f} cap={cap:.3f} mu={mu:.9f} nref={nref:.6e}")
    print(f"ratio range = {min(ratios):.9f} .. {max(ratios):.9f}")
    print(f"relative to baseline = {min(ratios)/r0[0]-1:+.3%} .. {max(ratios)/r0[0]-1:+.3%}")
    set_parameters(BASE)

if __name__ == "__main__":
    main()
