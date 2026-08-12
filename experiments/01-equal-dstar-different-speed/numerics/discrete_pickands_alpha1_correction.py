#!/usr/bin/env python3
"""Step-47 exact alpha=1 discrete Pickands correction diagnostic.

For the canonical alpha=1 Pickands tangent

    W(t) = sqrt(2) B(t) - |t|,

physical grid spacing dt maps to canonical spacing

    delta = a * u^2 * dt

when the original stationary Gaussian covariance is

    R(h) = 1 - a |h| + o(|h|).

The discrete Pickands constant is

    H_1^delta = nu(sqrt(2 delta)),

where nu is the classical Gaussian overshoot function.  In the present detector
calibration x=sqrt(2 delta)<0.002, so the convergent small-x expansion of log nu
through x^5 is far beyond the required precision.

This helper evaluates only the canonical tangent correction.  It does not certify
the finite-u transfer to the actual timing process.
"""

from __future__ import annotations

import argparse
import math

RHO_FULL = 6.2407571
BETA_Q = 0.90

# Riemann-zeta values needed for the convergent small-x expansion.
ZETA_HALF = -1.4603545088095868
ZETA_MINUS_HALF = -0.20788622497735457
ZETA_MINUS_THREE_HALF = -0.02548520188983304


def eta(x: float) -> float:
    return 1.0 - math.exp(-2.0*x)*(1.0 + 2.0*x + 2.0*x*x)


def cusp_a(x: float) -> float:
    return 2.0*x*x*math.exp(-2.0*x)/eta(x)


def normal_ppf_90() -> float:
    # Phi^{-1}(0.9), kept explicit to avoid a scipy dependency in this helper.
    return 1.2815515655446004


def threshold_u(x: float) -> float:
    return RHO_FULL*math.sqrt(eta(x)) - normal_ppf_90()


def beta_constant() -> float:
    return -ZETA_HALF/math.sqrt(2.0*math.pi)


def log_nu_small_x(x: float) -> float:
    """Convergent small-x expansion of log nu through O(x^5).

    The present use has x<0.002, so the omitted term is numerically negligible.
    """
    return (
        ZETA_HALF/math.sqrt(2.0*math.pi)*x
        - ZETA_MINUS_HALF/(24.0*math.sqrt(2.0*math.pi))*x**3
        + ZETA_MINUS_THREE_HALF/(640.0*math.sqrt(2.0*math.pi))*x**5
    )


def canonical_row(X: float, dt: float) -> dict[str, float]:
    a = cusp_a(X)
    u = threshold_u(X)
    delta = a*u*u*dt
    x = math.sqrt(2.0*delta)
    h = math.exp(log_nu_small_x(x))
    return {
        "X": X,
        "dt": dt,
        "a": a,
        "u": u,
        "delta": delta,
        "x": x,
        "H": h,
        "loss": 1.0-h,
        "leading": beta_constant()*x,
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--X", type=float, default=7.16)
    p.add_argument("--dts", default="0.001,0.0005,0.00025")
    args = p.parse_args()

    dts = [float(v) for v in args.dts.split(",") if v.strip()]
    rows = [canonical_row(args.X, dt) for dt in dts]

    print("Step-47 alpha=1 canonical discrete Pickands correction")
    print(f"X={args.X:g}  a={rows[0]['a']:.12e}  u={rows[0]['u']:.12f}")
    print(f"beta={beta_constant():.12f}")
    print()
    print("dt          delta             x                 H_1^delta          loss              beta*x")
    for r in rows:
        print(
            f"{r['dt']:<11.8f} {r['delta']:.12e}  {r['x']:.12e}  "
            f"{r['H']:.12f}  {r['loss']:.12e}  {r['leading']:.12e}"
        )

    if len(rows) >= 2:
        coarse = rows[0]
        fine = rows[-1]
        print()
        print(
            "canonical coarse-to-fine loss difference = "
            f"{coarse['loss']-fine['loss']:.12e}"
        )

    # Also show the moderate witness-time option discussed in Step 45.
    if abs(args.X-7.16) < 1e-12:
        r75 = canonical_row(7.50, 0.001)
        print()
        print("X=7.50, dt=.001 design diagnostic")
        print(f"a={r75['a']:.12e}  u={r75['u']:.12f}")
        print(f"canonical loss={r75['loss']:.12e}")

    print(
        "\nNOTE: H_1^delta is exact for the canonical alpha=1 tangent. "
        "The finite-u transfer to the actual mixed timing process remains open."
    )


if __name__ == "__main__":
    main()
