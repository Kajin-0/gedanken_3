#!/usr/bin/env python3
"""Continuum-level Paper A slow-only feasibility bracket.

This is a compact, reproducible calculation for the full-template process

    R(y) = (1 + |y|) exp(-|y|).

It avoids finite-time hard-window grid maxima entirely.

Parameters:

    rho0 = 3.5
    alpha = 0.05
    beta = 0.90
    r = tau_s / tau_f = 6
    L = 9 tau_f = 1.5 tau_s

Slow-channel continuum upper bound:

    P_FA <= Q(c) + ell_s/(2*pi) exp(-c^2/2)

because a continuous differentiable stationary Gaussian path that exceeds c
must either begin above c or have at least one upcrossing, and the expected
number of upcrossings is exact by Rice's formula for R''(0)=-1.

Fast-channel continuum lower bound:

Sample seven points over [0,9] separated by d=1.5. Every off-diagonal
covariance is at most epsilon=R(1.5). Compare by Slepian to the equicorrelated
vector

    Y_i = sqrt(epsilon) V + sqrt(1-epsilon) E_i.

The sampled fast maximum is stochastically at least as large as this comparison
maximum, so the continuous fast supremum is also at least as likely to exceed c.
The equicorrelated maximum probability is a one-dimensional normal integral.

This is a Paper-A manuscript witness, not Step 50 and not a reopening of the
Step-13--49 finite-window rare-event closure branch.
"""

from __future__ import annotations

import math

from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.stats import norm


RHO0 = 3.5
ALPHA = 0.05
BETA = 0.90
RATIO = 6.0
ELL_SLOW = 1.5
ELL_FAST = RATIO * ELL_SLOW
N_FAST_SAMPLES = 7
SAMPLE_SPACING = ELL_FAST / (N_FAST_SAMPLES - 1)


def eta(x: float) -> float:
    return 1.0 - math.exp(-2.0 * x) * (1.0 + 2.0 * x + 2.0 * x * x)


def covariance(y: float) -> float:
    y = abs(y)
    return (1.0 + y) * math.exp(-y)


def known_time_x0() -> float:
    target = (norm.ppf(1.0 - ALPHA) + norm.ppf(BETA)) / RHO0
    return float(brentq(lambda x: math.sqrt(eta(x)) - target, 1.0e-12, 100.0))


def slow_rice_upper(c: float) -> float:
    return float(norm.sf(c) + ELL_SLOW / (2.0 * math.pi) * math.exp(-0.5 * c * c))


def equicorrelated_max_pfa(c: float) -> tuple[float, float]:
    epsilon = covariance(SAMPLE_SPACING)
    root_e = math.sqrt(epsilon)
    root_i = math.sqrt(1.0 - epsilon)

    def integrand(v: float) -> float:
        conditional_cdf = norm.cdf((c - root_e * v) / root_i)
        return norm.pdf(v) * conditional_cdf**N_FAST_SAMPLES

    cdf, error = quad(integrand, -10.0, 10.0, epsabs=1.0e-13, epsrel=1.0e-13, limit=300)
    return 1.0 - cdf, error


def main() -> None:
    z_beta = float(norm.ppf(BETA))
    c = RHO0 - z_beta
    x0 = known_time_x0()

    slow_upper = slow_rice_upper(c)
    fast_lower, quad_error = equicorrelated_max_pfa(c)
    epsilon = covariance(SAMPLE_SPACING)

    print("Paper A analytic full-template feasibility bracket")
    print(f"rho0={RHO0:.12g} alpha={ALPHA:.12g} beta={BETA:.12g} r={RATIO:.12g}")
    print(f"c=rho0-Phi^-1(beta)={c:.15g}")
    print(f"known-time x0={x0:.15g}")
    print(f"T_G,f(0)/tau_f={x0:.15g}")
    print(f"T_G,s(0)/tau_f={RATIO*x0:.15g}")
    print(f"L/tau_f={ELL_FAST:.15g} L/tau_s={ELL_SLOW:.15g}")
    print()
    print(f"slow continuum Rice/union upper bound={slow_upper:.15g}")
    print(f"fast sampled-point spacing={SAMPLE_SPACING:.15g}")
    print(f"equicorrelation epsilon=R(d)={epsilon:.15g}")
    print(f"fast continuum Slepian lower bound={fast_lower:.15g}")
    print(f"1D quadrature absolute error estimate={quad_error:.3g}")
    print()
    if slow_upper < ALPHA < fast_lower:
        print("CERTIFIED REGIME BRACKET: slow guarantee-feasible / fast guarantee-infeasible")
    else:
        print("BRACKET FAILED: alpha is not separated by the two bounds")


if __name__ == "__main__":
    main()
