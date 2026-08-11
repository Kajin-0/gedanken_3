#!/usr/bin/env python3
"""Step-20 finite-r fixed-physics bandwidth reversal calculator.

This extends the Step-19 fixed-physics Gaussian information-band model to a
finite detector speed ratio r=tau_s/tau_f.

Both detectors have the same unregularized full-band eventual known-time SNR
rho_full, and both are passed through the same *physical* information-band
scale Omega_B. Therefore

    kappa_f = Omega_B * tau_f
    kappa_s = r * kappa_f.

For finite dimensionless decision duration x,

    H_x(nu) = [1-exp(-(1+i nu)x)(1+(1+i nu)x)]/(1+i nu)^2

and the accessible finite-duration SNR is

    rho(x,kappa)=rho_full*sqrt(I0_x(kappa)/(pi/2)).

The smooth timing-scan curvature is

    sigma^2=I2_x/I0_x.

The high-threshold Rice/EC threshold Gamma solves

    alpha = Q(Gamma) + ell*sigma/(2*pi)*exp(-Gamma^2/2).

The earliest dimensionless detection duration solves

    rho(x,kappa)-Gamma(x,ell,kappa)-Phi^-1(beta)=0.

This is a controlled Rice-model calculator, not an exact Palm-corrected
continuous-time solver and not a literal circuit -3 dB model.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.optimize import brentq
from scipy.stats import norm


def H_x(nu: np.ndarray, x: float) -> np.ndarray:
    z = 1.0 + 1j * nu
    return (1.0 - np.exp(-z * x) * (1.0 + z * x)) / (z * z)


def moments_finite(
    x: float,
    kappa: float,
    dnu: float = 0.02,
) -> tuple[float, float]:
    """Return I0 and I2 for the finite template by direct spectral quadrature."""
    if x <= 0.0 or kappa <= 0.0 or dnu <= 0.0:
        raise ValueError("x, kappa, and dnu must be positive")

    upper = max(30.0, 6.0 * kappa)
    nu = np.arange(0.0, upper + dnu, dnu)
    h2 = np.abs(H_x(nu, x)) ** 2
    weight = np.exp(-(nu / kappa) ** 2)
    density = h2 * weight

    i0 = 2.0 * float(np.trapezoid(density, nu))
    i2 = 2.0 * float(np.trapezoid(nu * nu * density, nu))
    return i0, i2


def rho_sigma(
    x: float,
    kappa: float,
    rho_full: float,
    dnu: float,
) -> tuple[float, float]:
    i0, i2 = moments_finite(x, kappa, dnu)
    rho = rho_full * math.sqrt(i0 / (math.pi / 2.0))
    sigma = math.sqrt(i2 / i0)
    return rho, sigma


def rice_threshold(
    x: float,
    ell: float,
    kappa: float,
    alpha: float,
    rho_full: float,
    dnu: float,
) -> tuple[float, float]:
    """Return Rice threshold and finite-duration SNR."""
    rho, sigma = rho_sigma(x, kappa, rho_full, dnu)
    gamma_known = float(norm.isf(alpha))

    if ell <= 0.0:
        return gamma_known, rho

    def equation(u: float) -> float:
        return (
            0.5 * math.erfc(u / math.sqrt(2.0))
            + ell * sigma / (2.0 * math.pi) * math.exp(-0.5 * u * u)
            - alpha
        )

    gamma = brentq(equation, gamma_known, 12.0, xtol=1e-12)
    return gamma, rho


def decision_margin(
    x: float,
    ell: float,
    kappa: float,
    rho_full: float,
    alpha: float,
    beta: float,
    dnu: float,
) -> float:
    gamma, rho = rice_threshold(x, ell, kappa, alpha, rho_full, dnu)
    return rho - gamma - float(norm.ppf(beta))


def detection_x(
    ell: float,
    kappa: float,
    rho_full: float,
    alpha: float,
    beta: float,
    dnu: float,
    xmax: float = 40.0,
) -> float:
    """Earliest positive root of the Rice decision margin; inf if not found."""
    grid = np.concatenate(
        [
            np.geomspace(0.05, 2.0, 18),
            np.linspace(2.0, xmax, 60),
        ]
    )

    x0 = float(grid[0])
    m0 = decision_margin(x0, ell, kappa, rho_full, alpha, beta, dnu)
    if m0 >= 0.0:
        return x0

    for x1_raw in grid[1:]:
        x1 = float(x1_raw)
        m1 = decision_margin(x1, ell, kappa, rho_full, alpha, beta, dnu)
        if m0 < 0.0 <= m1:
            return brentq(
                lambda x: decision_margin(
                    x, ell, kappa, rho_full, alpha, beta, dnu
                ),
                x0,
                x1,
                xtol=1e-8,
            )
        x0, m0 = x1, m1

    return math.inf


def physical_time_difference(
    kappa_fast: float,
    r: float,
    Lambda: float,
    rho_full: float,
    alpha: float,
    beta: float,
    dnu: float,
) -> tuple[float, float, float]:
    """Return x_f, r*x_s, and their difference in units of tau_f."""
    x_f = detection_x(
        Lambda, kappa_fast, rho_full, alpha, beta, dnu, xmax=40.0
    )
    x_s = detection_x(
        Lambda / r,
        r * kappa_fast,
        rho_full,
        alpha,
        beta,
        dnu,
        xmax=30.0,
    )

    t_s_fast_units = r * x_s
    if not math.isfinite(x_f) or not math.isfinite(x_s):
        return x_f, t_s_fast_units, math.nan
    return x_f, t_s_fast_units, x_f - t_s_fast_units


def find_switch(
    lo: float,
    hi: float,
    r: float,
    Lambda: float,
    rho_full: float,
    alpha: float,
    beta: float,
    dnu: float,
) -> float:
    def difference(kappa_fast: float) -> float:
        _, _, delta = physical_time_difference(
            kappa_fast,
            r,
            Lambda,
            rho_full,
            alpha,
            beta,
            dnu,
        )
        if not math.isfinite(delta):
            raise ValueError(
                "Switch bracket must keep both detectors feasible throughout root solve."
            )
        return delta

    return brentq(difference, lo, hi, xtol=1e-6)


def preference_label(x_f: float, t_s: float) -> str:
    fast_ok = math.isfinite(x_f)
    slow_ok = math.isfinite(t_s)
    if not fast_ok and not slow_ok:
        return "neither"
    if not fast_ok:
        return "slow_only"
    if not slow_ok:
        return "fast_only"
    if x_f < t_s:
        return "fast"
    if t_s < x_f:
        return "slow"
    return "equal"


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--r", type=float, default=2.0)
    p.add_argument("--Lambda", type=float, default=0.895)
    p.add_argument("--rho-full", type=float, default=6.2407571)
    p.add_argument("--alpha", type=float, default=1e-6)
    p.add_argument("--beta", type=float, default=0.90)
    p.add_argument("--dnu", type=float, default=0.02)
    p.add_argument("--tau-fast", type=float, default=1e-9)
    args = p.parse_args()

    sample_kappa = [20.0, 25.0, 30.0, 80.0, 120.0, 140.0, 160.0]

    print("kappa_f   T_f/tau_f   T_s/tau_f   preference")
    for kappa in sample_kappa:
        x_f, t_s, _ = physical_time_difference(
            kappa,
            args.r,
            args.Lambda,
            args.rho_full,
            args.alpha,
            args.beta,
            args.dnu,
        )
        print(
            f"{kappa:8.3f}  {x_f:11.6g}  {t_s:11.6g}  "
            f"{preference_label(x_f, t_s)}"
        )

    if abs(args.r - 2.0) < 1e-12 and abs(args.Lambda - 0.895) < 1e-12:
        k1 = find_switch(
            25.0,
            30.0,
            args.r,
            args.Lambda,
            args.rho_full,
            args.alpha,
            args.beta,
            args.dnu,
        )
        k2 = find_switch(
            120.0,
            140.0,
            args.r,
            args.Lambda,
            args.rho_full,
            args.alpha,
            args.beta,
            args.dnu,
        )

        for label, kappa in [("switch_1", k1), ("switch_2", k2)]:
            x_f, t_s, delta = physical_time_difference(
                kappa,
                args.r,
                args.Lambda,
                args.rho_full,
                args.alpha,
                args.beta,
                args.dnu,
            )
            f_band = kappa / (2.0 * math.pi * args.tau_fast)
            print(f"{label}_kappa_fast: {kappa}")
            print(f"{label}_T_fast_over_tau_fast: {x_f}")
            print(f"{label}_T_slow_over_tau_fast: {t_s}")
            print(f"{label}_difference: {delta}")
            print(f"{label}_information_band_hz: {f_band}")


if __name__ == "__main__":
    main()
