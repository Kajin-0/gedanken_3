#!/usr/bin/env python3
"""High-threshold crossover asymptotics for Experiment 01, Step 17.

This script evaluates the endpoint-retaining Rice/EC crossover law for the
smooth Gaussian information-band regularization used in Steps 15-17 and
compares finite speed ratios against the large-r fast-feasibility asymptote.

It is a deterministic asymptotic calculator, not a Palm Monte Carlo solver.
Palm corrections are handled separately by upcrossing_importance_sampling.py.
"""

from __future__ import annotations

import argparse
import math
from functools import lru_cache

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.stats import norm


def H_x(nu: float, x: float) -> complex:
    z = 1.0 + 1j * nu
    return (1.0 - np.exp(-z * x) * (1.0 + z * x)) / (z * z)


def H_inf(nu: float) -> complex:
    z = 1.0 + 1j * nu
    return 1.0 / (z * z)


def _quad_even(fun, kappa: float) -> float:
    upper = max(10.0 * kappa, 50.0)
    value, _ = quad(fun, 0.0, upper, epsabs=1e-10, epsrel=1e-8, limit=300)
    return 2.0 * value


@lru_cache(None)
def eventual_energy(kappa: float) -> float:
    return _quad_even(
        lambda nu: abs(H_inf(nu)) ** 2 * math.exp(-(nu / kappa) ** 2),
        kappa,
    )


@lru_cache(None)
def moments(x_rounded: float, kappa: float) -> tuple[float, float]:
    x = float(x_rounded)
    i0 = _quad_even(
        lambda nu: abs(H_x(nu, x)) ** 2 * math.exp(-(nu / kappa) ** 2),
        kappa,
    )
    i2 = _quad_even(
        lambda nu: nu * nu * abs(H_x(nu, x)) ** 2 * math.exp(-(nu / kappa) ** 2),
        kappa,
    )
    return i0, i2


def rho_fraction(x: float, kappa: float) -> float:
    i0, _ = moments(round(float(x), 10), float(kappa))
    return math.sqrt(i0 / eventual_energy(float(kappa)))


def sigma_nu(x: float, kappa: float) -> float:
    i0, i2 = moments(round(float(x), 10), float(kappa))
    return math.sqrt(i2 / i0)


def sigma_inf(kappa: float) -> float:
    i0 = eventual_energy(kappa)
    i2 = _quad_even(
        lambda nu: nu * nu * abs(H_inf(nu)) ** 2 * math.exp(-(nu / kappa) ** 2),
        kappa,
    )
    return math.sqrt(i2 / i0)


def rice_ell_from_margin(u: float, sigma: float, alpha: float) -> float:
    available = alpha - norm.sf(u)
    if available <= 0.0:
        return math.inf
    return 2.0 * math.pi * available * math.exp(0.5 * u * u) / sigma


def crossover_rice(
    r: float,
    rho0: float,
    alpha: float,
    beta: float,
    kappa: float,
) -> tuple[float, float]:
    z_beta = norm.ppf(beta)

    def residual(x: float) -> float:
        u_s = rho0 * rho_fraction(x, kappa) - z_beta
        u_f = rho0 * rho_fraction(r * x, kappa) - z_beta
        ell_s = rice_ell_from_margin(u_s, sigma_nu(x, kappa), alpha)
        ell_f = rice_ell_from_margin(u_f, sigma_nu(r * x, kappa), alpha)
        return ell_f - r * ell_s

    grid = np.linspace(0.2, 15.0, 200)
    vals = [residual(float(x)) for x in grid]
    for xa, xb, fa, fb in zip(grid[:-1], grid[1:], vals[:-1], vals[1:]):
        if math.isfinite(fa) and math.isfinite(fb) and fa * fb < 0.0:
            x = brentq(residual, float(xa), float(xb))
            u_s = rho0 * rho_fraction(x, kappa) - z_beta
            ell = rice_ell_from_margin(u_s, sigma_nu(x, kappa), alpha)
            return x, ell
    raise RuntimeError("No physical crossover root found in scan interval")


def ellcrit_rice(rho0: float, alpha: float, beta: float, kappa: float) -> float:
    u_inf = rho0 - norm.ppf(beta)
    return rice_ell_from_margin(u_inf, sigma_inf(kappa), alpha)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--rho0", type=float, default=6.2)
    p.add_argument("--alpha", type=float, default=1e-6)
    p.add_argument("--beta", type=float, default=0.90)
    p.add_argument("--kappa", type=float, default=8.0)
    p.add_argument("--r", type=float, default=1.2)
    args = p.parse_args()

    x, ell = crossover_rice(args.r, args.rho0, args.alpha, args.beta, args.kappa)
    crit = ellcrit_rice(args.rho0, args.alpha, args.beta, args.kappa)

    print(f"x_s={x:.12g}")
    print(f"ell_s_cross={ell:.12g}")
    print(f"ell_f_cross=r*ell={args.r * ell:.12g}")
    print(f"ellcrit_fast_full_template={crit:.12g}")
    print(f"relative_large_r_error={(args.r * ell / crit - 1.0):.6e}")


if __name__ == "__main__":
    main()
