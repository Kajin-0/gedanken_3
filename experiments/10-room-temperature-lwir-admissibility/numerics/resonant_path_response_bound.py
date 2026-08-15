#!/usr/bin/env python3
"""Reproduce one-port TCMT path-enhancement / response-time bounds for Exp10."""

from __future__ import annotations

import math


def g_abs(A: float) -> float:
    if not (0.0 < A <= 1.0):
        raise ValueError("A must be in (0,1]")
    return 1.0 - math.sqrt(1.0 - A)


def main() -> None:
    c = 299_792_458.0
    lam0 = 10e-6
    A0 = 0.90
    zeta = -math.log(1.0 - A0)
    g = g_abs(A0)

    # Existing single-pass coefficient Sigma_sp=C/v^2.
    C = 1.0666799497e29  # m^-2 (m/s)^2
    v_active = 1.0e6
    sigma_sp_cm2 = (C / v_active**2) / 1e4

    # Simple one-optical-wavelength circulation: L=lambda/n, vE=c/n => L/vE=lambda/c.
    t_circ = lam0 / c

    print(f"A0={A0:.3f}")
    print(f"g(A0)={g:.12f}")
    print(f"zeta={zeta:.12f}")
    print(f"lambda0/c={t_circ:.6e} s")
    print(f"single-pass Sigma(v=1e6)={sigma_sp_cm2:.6e} cm^-2")
    print()
    print("tau_max(s)     resonant/single-pass     Sigma_res_bound(cm^-2)")
    for tau in (1e-13, 1e-12, 1e-11, 1e-10):
        ratio = (g / zeta) * (t_circ / tau)
        sigma_res = sigma_sp_cm2 * ratio
        print(f"{tau:10.3e}     {ratio:18.9e}     {sigma_res:18.9e}")

    # Response time at which this simple resonator bound equals the original single-pass bound.
    tau_equal = (g / zeta) * t_circ
    print()
    print(f"tau_equal={tau_equal:.6e} s")


if __name__ == "__main__":
    main()
