#!/usr/bin/env python3
"""Step-19 fixed-physics bandwidth optimum calculator.

The underlying unregularized full-template detector SNR `rho_full` is held
fixed while the accessible Gaussian information-band scale kappa is varied.
Unlike Step 18, accessible eventual SNR is NOT renormalized.

Model:
    H_inf(nu) = 1/(1+i nu)^2
    information weight = exp[-(nu/kappa)^2]

For the large-speed-ratio / full-fast-template / Rice objective,

    ell_crit(kappa)
      = 2*pi*[alpha-Q(u)]*exp(u^2/2)/sigma(kappa)

with
    u = rho_full*sqrt(F(kappa)) - Phi^-1(beta)
    F = I0/(pi/2)
    sigma^2 = I2/I0.

This is a controlled asymptotic/task calculator, not a hardware optimizer and
not a literal circuit -3 dB bandwidth model.
"""

from __future__ import annotations

import argparse
import math

from scipy.integrate import quad
from scipy.optimize import brentq, minimize_scalar
from scipy.stats import norm


def moments(kappa: float) -> tuple[float, float]:
    """Return I0 and I2 using nu=kappa*y for narrow-band stability."""
    if kappa <= 0:
        raise ValueError("kappa must be positive")

    def d0(y: float) -> float:
        return math.exp(-y * y) / (1.0 + (kappa * y) ** 2) ** 2

    def d2(y: float) -> float:
        nu2 = (kappa * y) ** 2
        return nu2 * math.exp(-y * y) / (1.0 + nu2) ** 2

    i0 = 2.0 * kappa * quad(d0, 0.0, 10.0, epsabs=1e-13, epsrel=1e-11)[0]
    i2 = 2.0 * kappa * quad(d2, 0.0, 10.0, epsabs=1e-13, epsrel=1e-11)[0]
    return i0, i2


def accessible_fraction(kappa: float) -> float:
    i0, _ = moments(kappa)
    return i0 / (math.pi / 2.0)


def accessible_snr(kappa: float, rho_full: float) -> float:
    return rho_full * math.sqrt(accessible_fraction(kappa))


def sigma_inf(kappa: float) -> float:
    i0, i2 = moments(kappa)
    return math.sqrt(i2 / i0)


def known_time_required_snr(alpha: float, beta: float) -> float:
    return float(norm.ppf(1.0 - alpha) + norm.ppf(beta))


def ell_crit_rice(
    kappa: float,
    rho_full: float,
    alpha: float,
    beta: float,
) -> float:
    z_beta = float(norm.ppf(beta))
    gamma = float(norm.ppf(1.0 - alpha))
    rho = accessible_snr(kappa, rho_full)
    u = rho - z_beta
    if u <= gamma:
        return 0.0
    return (
        2.0
        * math.pi
        * (alpha - float(norm.sf(u)))
        * math.exp(0.5 * u * u)
        / sigma_inf(kappa)
    )


def find_kappa_min(rho_full: float, alpha: float, beta: float) -> float:
    req = known_time_required_snr(alpha, beta)
    if rho_full <= req:
        raise ValueError("Full-band detector is not even known-time feasible.")

    lo = 1e-8
    hi = 1.0
    while accessible_snr(hi, rho_full) < req:
        hi *= 2.0
    return brentq(
        lambda k: accessible_snr(k, rho_full) - req,
        lo,
        hi,
        xtol=1e-12,
        rtol=1e-11,
    )


def optimize_kappa(
    rho_full: float,
    alpha: float,
    beta: float,
) -> tuple[float, float]:
    kmin = find_kappa_min(rho_full, alpha, beta)

    result = minimize_scalar(
        lambda logk: -ell_crit_rice(math.exp(logk), rho_full, alpha, beta),
        bounds=(math.log(kmin * (1.0 + 1e-8)), math.log(1e5)),
        method="bounded",
        options={"xatol": 1e-10},
    )
    kopt = math.exp(result.x)
    return kopt, -float(result.fun)


def calibrate_rho_full(
    kappa_reference: float,
    rho_accessible_reference: float,
) -> float:
    return rho_accessible_reference / math.sqrt(accessible_fraction(kappa_reference))


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--alpha", type=float, default=1e-6)
    p.add_argument("--beta", type=float, default=0.90)
    p.add_argument("--tau-fast", type=float, default=1e-9)
    p.add_argument("--kappa-ref", type=float, default=8.0)
    p.add_argument("--rho-ref", type=float, default=6.2)
    p.add_argument(
        "--rho-full",
        type=float,
        default=None,
        help="If omitted, calibrate rho_full so rho_accessible(kappa_ref)=rho_ref.",
    )
    args = p.parse_args()

    rho_full = (
        args.rho_full
        if args.rho_full is not None
        else calibrate_rho_full(args.kappa_ref, args.rho_ref)
    )

    kmin = find_kappa_min(rho_full, args.alpha, args.beta)
    kopt, ellopt = optimize_kappa(rho_full, args.alpha, args.beta)

    z_beta = float(norm.ppf(args.beta))
    u_inf = rho_full - z_beta
    ell_inf = (
        2.0
        * math.pi
        * (args.alpha - float(norm.sf(u_inf)))
        * math.exp(0.5 * u_inf * u_inf)
    )

    omega_opt = kopt / args.tau_fast
    f_opt = omega_opt / (2.0 * math.pi)
    f_min = (kmin / args.tau_fast) / (2.0 * math.pi)

    print(f"rho_full: {rho_full}")
    print(f"known_time_required_snr: {known_time_required_snr(args.alpha, args.beta)}")
    print(f"kappa_min: {kmin}")
    print(f"kappa_opt: {kopt}")
    print(f"ell_crit_opt: {ellopt}")
    print(f"ell_crit_infinite_band: {ell_inf}")
    print(f"relative_gain_vs_infinite: {ellopt / ell_inf - 1.0}")
    print(f"rho_at_opt: {accessible_snr(kopt, rho_full)}")
    print(f"sigma_at_opt: {sigma_inf(kopt)}")
    print(f"f_min_hz_for_tau_fast: {f_min}")
    print(f"f_opt_hz_for_tau_fast: {f_opt}")
    print(f"L_cross_opt_seconds: {args.tau_fast * ellopt}")
    print(f"L_cross_infinite_seconds: {args.tau_fast * ell_inf}")


if __name__ == "__main__":
    main()
