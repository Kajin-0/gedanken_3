#!/usr/bin/env python3
"""Step-40 Cameron-Martin RKHS barrier diagnostics.

This helper evaluates the high-band timing covariance floor and the exact
probit threshold bounds obtained from a covariance-kernel Cameron-Martin
barrier.

For a unit-variance Gaussian process with covariance R_q and search interval
[0, ell], choose t0=ell/2 and

    m_q = inf_t R_q(t-t0).

The RKHS kernel section has norm 1, so

    h_delta(t) = delta R_q(t-t0) / m_q

has h_delta >= delta and Cameron-Martin norm delta/m_q.

If p(u)=P(sup z > u), the exact event-level bounds are

    p(u-delta) <= Phi(Phi^{-1}(p(u)) + delta/m_q),
    p(u+delta) >= Phi(Phi^{-1}(p(u)) - delta/m_q).

The script uses deterministic spectral quadrature for finite kappa and the
closed hard-window covariance at kappa=infinity. It is a numerical diagnostic,
not formal interval arithmetic.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.stats import norm


def eta(x: float) -> float:
    return 1.0 - math.exp(-2.0 * x) * (1.0 + 2.0 * x + 2.0 * x * x)


def rough_covariance(x: float, y: float) -> float:
    """Exact normalized covariance for h(v)=v exp(-v) 1_[0,x]."""
    y = abs(float(y))
    if y >= x:
        return 0.0

    L = x - y
    den = eta(x) / 4.0
    i1 = 0.25 - math.exp(-2.0 * L) * (L / 2.0 + 0.25)
    i2 = 0.25 - math.exp(-2.0 * L) * (
        L * L / 2.0 + L / 2.0 + 0.25
    )
    return math.exp(-y) * (i2 + y * i1) / den


def h_sq(x: float, omega: np.ndarray) -> np.ndarray:
    z = 1.0 + 1j * omega
    numerator = 1.0 - np.exp(-z * x) * (1.0 + z * x)
    h = numerator / (z * z)
    return np.abs(h) ** 2


def finite_covariance(
    *,
    x: float,
    kappa: float,
    lags: np.ndarray,
    omega_step: float,
    cutoff_sigma: float,
) -> np.ndarray:
    """Deterministic cosine quadrature of normalized finite-band covariance."""
    omega_max = cutoff_sigma * kappa
    omega = np.arange(0.0, omega_max + omega_step, omega_step)
    spectral_mass = h_sq(x, omega) * np.exp(-(omega / kappa) ** 2)
    normalization = 2.0 * np.trapezoid(spectral_mass, omega)

    out = np.empty_like(lags, dtype=float)
    for i, lag in enumerate(lags):
        numerator = 2.0 * np.trapezoid(
            spectral_mass * np.cos(omega * float(lag)), omega
        )
        out[i] = numerator / normalization
    return out


def covariance_floor(
    *,
    x: float,
    ell: float,
    kappa: float,
    n_t: int,
    omega_step: float,
    cutoff_sigma: float,
) -> tuple[float, float]:
    t0 = ell / 2.0
    lags = np.linspace(-t0, t0, n_t)

    if math.isinf(kappa):
        values = np.array([rough_covariance(x, lag) for lag in lags])
    else:
        values = finite_covariance(
            x=x,
            kappa=kappa,
            lags=lags,
            omega_step=omega_step,
            cutoff_sigma=cutoff_sigma,
        )

    i = int(np.argmin(values))
    return float(values[i]), float(lags[i])


def probit_bounds(*, p: float, delta: float, m: float) -> dict[str, float]:
    z = float(norm.ppf(p))
    r = delta / m
    lower = float(norm.cdf(z - r))
    upper = float(norm.cdf(z + r))
    return {
        "z": z,
        "rkhs_radius": r,
        "p_u_plus_delta_lower": lower,
        "p_u_minus_delta_upper": upper,
        "symmetric_strip_upper": upper - lower,
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--x", type=float, default=7.16)
    p.add_argument("--ell", type=float, default=0.895)
    p.add_argument(
        "--kappa",
        default="170,200,300,500,1000,inf",
        help="comma-separated finite kappa values plus optional inf",
    )
    p.add_argument("--n-t", type=int, default=501)
    p.add_argument("--omega-step", type=float, default=0.03)
    p.add_argument("--cutoff-sigma", type=float, default=6.0)
    p.add_argument("--alpha", type=float, default=1e-6)
    p.add_argument("--p-upper-alpha", type=float, default=0.98968)
    p.add_argument("--delta", type=float, default=1e-4)
    p.add_argument("--working-floor", type=float, default=0.92)
    args = p.parse_args()

    kappas: list[float] = []
    for token in args.kappa.split(","):
        token = token.strip().lower()
        if not token:
            continue
        kappas.append(math.inf if token in {"inf", "infinity"} else float(token))

    print("Covariance-kernel barrier floors")
    print("kappa_f       m_q             argmin_lag      1/m_q")
    for kappa in kappas:
        m, lag = covariance_floor(
            x=args.x,
            ell=args.ell,
            kappa=kappa,
            n_t=args.n_t,
            omega_step=args.omega_step,
            cutoff_sigma=args.cutoff_sigma,
        )
        label = "inf" if math.isinf(kappa) else f"{kappa:g}"
        print(f"{label:>8s}   {m:14.10f}   {lag:14.8f}   {1.0/m:10.7f}")

    p_upper = args.p_upper_alpha * args.alpha
    bounds = probit_bounds(
        p=p_upper,
        delta=args.delta,
        m=args.working_floor,
    )

    print("\nConservative probit threshold bound")
    print(f"p(u) upper / alpha:        {p_upper/args.alpha:.9f}")
    print(f"working covariance floor:  {args.working_floor:.9f}")
    print(f"delta:                     {args.delta:.9g}")
    print(f"RKHS radius delta/m:       {bounds['rkhs_radius']:.12g}")
    print(
        "p(u-delta) upper / alpha: "
        f"{bounds['p_u_minus_delta_upper']/args.alpha:.9f}"
    )
    print(
        "p(u+delta) lower / alpha: "
        f"{bounds['p_u_plus_delta_lower']/args.alpha:.9f}"
    )
    print(
        "symmetric strip upper:    "
        f"{bounds['symmetric_strip_upper']:.12g}"
    )

    print(
        "\nNOTE: covariance quadrature and the chosen working floor are numerical, "
        "not formal interval arithmetic. The Cameron-Martin event inequalities "
        "are analytic once a valid positive covariance floor is supplied."
    )


if __name__ == "__main__":
    main()
