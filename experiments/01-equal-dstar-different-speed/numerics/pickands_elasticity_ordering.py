#!/usr/bin/env python3
"""Step-38 diagnostics for Pickands cross-elasticity ordering.

This helper checks the deterministic smoothing inequality

    0 <= zeta d_zeta F_zeta(t) <= F_zeta(t),

and evaluates the explicit matched-tangent hazard/strip bounds derived from it:

    h_tan/N_tan <= phi(u)/Q(u) - 1/u,

    [N_tan(u-d)-N_tan(u+d)]/N_tan(u)
      <= ((u-d)/u) Q(u-d)/Q(u)
         -((u+d)/u) Q(u+d)/Q(u).

It does not estimate the exact finite-u excursion-cluster correction.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.special import erf
from scipy.stats import norm


def F_zeta(t: np.ndarray | float, zeta: float) -> np.ndarray:
    t = np.asarray(t, dtype=float)
    a = np.abs(t)
    s = zeta * a
    return a * erf(s) + (np.exp(-s * s) - 1.0) / (math.sqrt(math.pi) * zeta)


def zeta_dF(t: np.ndarray | float, zeta: float) -> np.ndarray:
    t = np.asarray(t, dtype=float)
    s = zeta * np.abs(t)
    return (1.0 - np.exp(-s * s)) / (math.sqrt(math.pi) * zeta)


def hazard_upper(u: float) -> float:
    q = float(norm.sf(u))
    phi = float(norm.pdf(u))
    return phi / q - 1.0 / u


def symmetric_strip_factor(u: float, delta: float) -> float:
    q0 = float(norm.sf(u))
    minus = ((u - delta) / u) * float(norm.sf(u - delta)) / q0
    plus = ((u + delta) / u) * float(norm.sf(u + delta)) / q0
    return minus - plus


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--u", type=float, default=4.959)
    p.add_argument("--delta", type=float, default=1e-4)
    p.add_argument("--zeta", type=float, default=10.0)
    p.add_argument("--tmax", type=float, default=10.0)
    p.add_argument("--n", type=int, default=200001)
    args = p.parse_args()

    t = np.linspace(-args.tmax, args.tmax, args.n)
    F = F_zeta(t, args.zeta)
    D = zeta_dF(t, args.zeta)

    print("Step-38 Pickands cross-elasticity diagnostics")
    print(f"zeta={args.zeta:g}, t in [-{args.tmax:g},{args.tmax:g}]")
    print(f"min(zeta*dF)       = {D.min():.12e}")
    print(f"min(F-zeta*dF)     = {(F-D).min():.12e}")
    positive = F > 1e-15
    if np.any(positive):
        print(f"max((zeta*dF)/F)   = {(D[positive]/F[positive]).max():.12f}")

    h = hazard_upper(args.u)
    b = symmetric_strip_factor(args.u, args.delta)
    print()
    print(f"u                     = {args.u:.9f}")
    print(f"hazard upper h/N      = {h:.12f}")
    print(f"(h/N)/u               = {h/args.u:.12f}")
    print(f"delta                 = {args.delta:.3e}")
    print(f"symmetric strip factor= {b:.12e}")
    print(f"strip factor/(2delta) = {b/(2*args.delta):.12f}")
    print(f"if N=1e-6: strip <=   = {b*1e-6:.12e}")

    print()
    print(
        "Interpretation: the deterministic F inequality implies "
        "H(chi,lambda*zeta) <= H(lambda*chi,zeta), so along fixed-kappa "
        "threshold trajectories H is nondecreasing in u and the tangent "
        "hazard cannot exceed the displayed Gaussian multiplier."
    )


if __name__ == "__main__":
    main()
