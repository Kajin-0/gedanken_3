#!/usr/bin/env python3
"""Step-35 analytic q-coupling continuity diagnostics.

For q=kappa^{-1/2}, define the normalized spectral amplitude

    A_q(w) = |H_x(w)| exp[-w^2 q^4 / 2] / sqrt(I_x(q)).

Then

    dA_q/dq = -2 q^3 (w^2-M2(q)) A_q

and

    ||dA_q/dq||_2^2 = 4 q^6 Var_q(w^2).

This script evaluates the derivative norm, the exact pairwise pointwise coupling
variance, and the threshold derivative for the Step-34 fast/slow witness times.
It uses deterministic floating-point quadrature and is not formal interval
arithmetic.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.integrate import quad


RHO_FULL = 6.2407571


def eta(x: float) -> float:
    return 1.0 - math.exp(-2.0 * x) * (1.0 + 2.0 * x + 2.0 * x * x)


def H_abs2(w: float, x: float) -> float:
    z = 1.0 + 1j * w
    h = (1.0 - np.exp(-z * x) * (1.0 + z * x)) / (z * z)
    return float(abs(h) ** 2)


def integral_moment(q: float, x: float, power: int) -> float:
    if q == 0.0:
        if power == 0:
            return 0.5 * math.pi * eta(x)
        raise ValueError("positive spectral moments diverge at q=0")

    def integrand(w: float) -> float:
        return (w**power) * H_abs2(w, x) * math.exp(-(w * w) * q**4)

    value, _ = quad(
        integrand,
        0.0,
        math.inf,
        epsabs=1.0e-9,
        epsrel=2.0e-8,
        limit=800,
    )
    return 2.0 * value


def I0(q: float, x: float) -> float:
    return integral_moment(q, x, 0)


def derivative_norm(q: float, x: float) -> float:
    if q == 0.0:
        c = x * math.exp(-x)
        i0 = 0.5 * math.pi * eta(x)
        return c * math.sqrt(2.0 * math.sqrt(math.pi) / i0)

    i0 = I0(q, x)
    m2 = integral_moment(q, x, 2) / i0
    m4 = integral_moment(q, x, 4) / i0
    return 2.0 * q**3 * math.sqrt(max(m4 - m2 * m2, 0.0))


def rho(q: float, x: float) -> float:
    return RHO_FULL * math.sqrt(I0(q, x) / (0.5 * math.pi))


def threshold_derivative(q: float, x: float) -> float:
    if q == 0.0:
        return 0.0
    i0 = I0(q, x)
    m2 = integral_moment(q, x, 2) / i0
    return -2.0 * q**3 * m2 * rho(q, x)


def pair_pointwise_variance(q: float, r: float, x: float) -> float:
    if q == 0.0 and r == 0.0:
        return 0.0
    qm = ((q**4 + r**4) / 2.0) ** 0.25
    overlap = I0(qm, x) / math.sqrt(I0(q, x) * I0(r, x))
    return max(2.0 * (1.0 - overlap), 0.0)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--X", type=float, default=7.16)
    p.add_argument("--qmax", type=float, default=0.0767)
    p.add_argument("--dq", type=float, default=0.005)
    args = p.parse_args()

    x_fast = args.X
    x_slow = args.X / 2.0

    q_values = [0.0, 0.02, 0.04, 0.06, args.qmax]

    print("Fast spectral q-derivative norm")
    for q in q_values:
        print(f"q={q:8.5f}  ||dA/dq||={derivative_norm(q, x_fast):.10f}")

    norms = [derivative_norm(float(q), x_fast) for q in np.linspace(0.0, args.qmax, 25)]
    lfast = max(norms)
    print(f"\ncoarse-grid max fast derivative norm: {lfast:.10f}")
    print(f"L2-Lipschitz pointwise RMS bound for dq={args.dq:g}: {lfast*args.dq:.10e}")

    max_du = max(
        abs(threshold_derivative(float(q), x_fast))
        for q in np.linspace(0.0, args.qmax, 25)
    )
    print(f"max |du/dq| fast on coarse q grid: {max_du:.10f}")
    print(f"threshold-motion bound for dq={args.dq:g}: {max_du*args.dq:.10e}")

    print("\nExact pairwise pointwise RMS values")
    pairs = [(0.0, args.dq), (0.070, 0.075), (0.075, args.qmax)]
    for q, r in pairs:
        sd = math.sqrt(pair_pointwise_variance(q, r, x_fast))
        print(f"q={q:.5f} -> {r:.5f}: RMS={sd:.10e}")

    print("\nSlow intrinsic derivative norm (slow q coordinate)")
    for qf in q_values:
        qs = qf / math.sqrt(2.0)
        intrinsic = derivative_norm(qs, x_slow)
        wrt_qf = intrinsic / math.sqrt(2.0)
        print(
            f"q_f={qf:8.5f} q_s={qs:8.5f} "
            f"||dA/dq_s||={intrinsic:.10f}  ||dA/dq_f||={wrt_qf:.10f}"
        )

    print(
        "\nNOTE: deterministic quadrature only. The cluster-count functional itself "
        "is discontinuous under sup-norm perturbations, so these process-level "
        "Lipschitz constants do not by themselves prove cluster-moment Lipschitz "
        "continuity."
    )


if __name__ == "__main__":
    main()
