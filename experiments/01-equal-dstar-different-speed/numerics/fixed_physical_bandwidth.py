#!/usr/bin/env python3
"""Large-speed-ratio crossover under one shared physical information bandwidth.

This implements the Step-18 Rice-limit full-template formula for the smooth
Gaussian information-band surrogate used in Steps 15-18.

The two detectors share one physical angular information scale Omega_B, so
    kappa_f = Omega_B * tau_f
    kappa_s = Omega_B * tau_s.

Under the controlled equal-accessible-eventual-SNR normalization and the
large-r condition that the slow detector approaches known-time operation, the
physical crossover is

    L_cross ~= tau_f * C / sigma_inf(kappa_f),

where

    C = 2*pi*[alpha-Q(u_inf)]*exp(u_inf^2/2)
    u_inf = rho0 - Phi^{-1}(beta)

and sigma_inf is the derivative standard deviation of the regularized full
fast template.

This is an illustrative asymptotic calculator, not a hardware optimizer and
not a literal -3 dB electronics model.
"""

from __future__ import annotations

import argparse
import math

from scipy.integrate import quad
from scipy.stats import norm


def sigma_inf(kappa: float) -> float:
    """Derivative standard deviation of the regularized full template.

    Uses nu = kappa*y so the narrow-band kappa << 1 limit remains numerically
    well conditioned.
    """
    if kappa <= 0:
        raise ValueError("kappa must be positive")

    def d0(y: float) -> float:
        return math.exp(-y * y) / (1.0 + (kappa * y) ** 2) ** 2

    def d2(y: float) -> float:
        return (
            (kappa * y) ** 2
            * math.exp(-y * y)
            / (1.0 + (kappa * y) ** 2) ** 2
        )

    i0 = 2.0 * kappa * quad(d0, 0.0, 10.0, epsabs=1e-13, epsrel=1e-11)[0]
    i2 = 2.0 * kappa * quad(d2, 0.0, 10.0, epsabs=1e-13, epsrel=1e-11)[0]
    return math.sqrt(i2 / i0)


def task_constant(rho0: float, alpha: float, beta: float) -> tuple[float, float]:
    u_inf = rho0 - float(norm.ppf(beta))
    q = float(norm.sf(u_inf))
    if alpha <= q:
        raise ValueError(
            "Task is not asymptotically feasible: alpha must exceed Q(u_inf)."
        )
    c = 2.0 * math.pi * (alpha - q) * math.exp(0.5 * u_inf * u_inf)
    return u_inf, c


def rice_large_r_crossover(
    tau_fast: float,
    omega_b: float,
    rho0: float,
    alpha: float,
    beta: float,
) -> dict[str, float]:
    if tau_fast <= 0 or omega_b <= 0:
        raise ValueError("tau_fast and omega_b must be positive")

    u_inf, c = task_constant(rho0, alpha, beta)
    kappa_fast = omega_b * tau_fast
    sigma = sigma_inf(kappa_fast)
    ell_crit = c / sigma
    l_cross = tau_fast * ell_crit

    return {
        "u_inf": u_inf,
        "task_constant_C": c,
        "kappa_fast": kappa_fast,
        "sigma_inf": sigma,
        "ell_crit": ell_crit,
        "L_cross_seconds": l_cross,
        "electronics_limit_seconds": math.sqrt(2.0) * c / omega_b,
        "wide_band_limit_seconds": c * tau_fast,
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--tau-fast", type=float, default=1e-9)
    p.add_argument(
        "--f-band",
        type=float,
        default=1e8,
        help="Gaussian information-band scale in Hz; Omega_B=2*pi*f_band",
    )
    p.add_argument("--rho0", type=float, default=6.2)
    p.add_argument("--alpha", type=float, default=1e-6)
    p.add_argument("--beta", type=float, default=0.90)
    args = p.parse_args()

    result = rice_large_r_crossover(
        tau_fast=args.tau_fast,
        omega_b=2.0 * math.pi * args.f_band,
        rho0=args.rho0,
        alpha=args.alpha,
        beta=args.beta,
    )

    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
