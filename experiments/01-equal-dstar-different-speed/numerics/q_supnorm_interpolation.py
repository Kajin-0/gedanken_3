#!/usr/bin/env python3
"""Step-41 analytic inter-node sup-norm probability envelopes.

This helper does not simulate Gaussian paths. It evaluates the conservative
probability budgets used in Step 41:

1. the corrected tiny-q endpoint chord asymptotic;
2. the rough endpoint deterministic-net + modulus bound;
3. the differentiable finite-q Rice sup-tail bound;
4. the Step-40 Cameron-Martin threshold translation.

The Step-34 node Monte Carlo/profile numbers and the spectral envelopes below
remain numerical inputs, not formal interval arithmetic.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.stats import norm


ALPHA = 1.0e-6
ELL = 0.895
X = 7.16
M_RKHS = 0.92
MAX_DU_DQ = 5.6e-3

ENDPOINT_UPPER_OVER_ALPHA = 0.98968
ENDPOINT_SE_OVER_ALPHA = 0.00429
PAIRED_MAX_SE_OVER_ALPHA = 0.00106
Z_MC = 1.645
GRID_ALLOWANCE_OVER_ALPHA = 0.002
MAX_POSITIVE_PAIRED_OVER_ALPHA = 1.9e-8


def eta_x(x: float) -> float:
    return 1.0 - math.exp(-2.0 * x) * (1.0 + 2.0 * x + 2.0 * x * x)


def endpoint_chord_constants(x: float = X) -> tuple[float, float, float, float]:
    c = x * math.exp(-x)
    i0 = 0.5 * math.pi * eta_x(x)
    l0 = math.sqrt(2.0 * math.sqrt(math.pi) * c * c / i0)
    chord_coeff = math.sqrt(math.sqrt(2.0) - 1.0) * l0
    return c, i0, l0, chord_coeff


def cm_upper(p: float, threshold_drop: float, m_floor: float = M_RKHS) -> float:
    return float(norm.cdf(norm.ppf(p) + threshold_drop / m_floor))


def endpoint_node_upper_ratio() -> float:
    return (
        ENDPOINT_UPPER_OVER_ALPHA
        + Z_MC * ENDPOINT_SE_OVER_ALPHA
        + GRID_ALLOWANCE_OVER_ALPHA
    )


def common_finite_node_upper_ratio() -> float:
    combined = math.sqrt(
        ENDPOINT_SE_OVER_ALPHA**2 + PAIRED_MAX_SE_OVER_ALPHA**2
    )
    return (
        ENDPOINT_UPPER_OVER_ALPHA
        + Z_MC * combined
        + GRID_ALLOWANCE_OVER_ALPHA
    )


def rough_endpoint_cover() -> dict[str, float]:
    # Covers q in [0, .0035] from the endpoint q=0.
    q_width = 0.0035
    sigma = 2.1e-5
    k_star = 2.0e-4
    h = 1.0e-9
    eta_grid = 9.0e-12
    eta_mod = 3.0e-13

    n = math.ceil(ELL / h) + 1
    e0 = sigma * math.sqrt(2.0 * math.log(2.0 * n / eta_grid))
    mean_mod = math.sqrt(2.0 * k_star * h / math.pi)
    tail_mod = math.sqrt(2.0 * k_star * h * math.log(2.0 * n / eta_mod))
    epsilon = e0 + mean_mod + tail_mod
    du = MAX_DU_DQ * q_width

    p0 = endpoint_node_upper_ratio() * ALPHA
    p_shift = cm_upper(p0, epsilon + du)
    total = p_shift + eta_grid + eta_mod

    return {
        "q_width": q_width,
        "sigma": sigma,
        "N": float(n),
        "e_grid": e0,
        "mean_mod": mean_mod,
        "tail_mod": tail_mod,
        "epsilon": epsilon,
        "du": du,
        "eta": eta_grid + eta_mod,
        "p_over_alpha": total / ALPHA,
    }


def rice_eta(v: float, lambda_d: float) -> float:
    """Two-sided smooth stationary-Gaussian sup tail by Rice union bound."""
    return float(
        2.0 * norm.sf(v)
        + ELL * lambda_d / math.pi * math.exp(-0.5 * v * v)
    )


def optimize_finite_cell(
    *,
    sigma: float,
    lambda_d: float,
    node_correction_over_alpha: float,
    q_halfwidth: float = 0.0025,
) -> dict[str, float]:
    node_ratio = common_finite_node_upper_ratio() + node_correction_over_alpha
    p_node = node_ratio * ALPHA
    du = MAX_DU_DQ * q_halfwidth

    best: dict[str, float] | None = None
    for v in np.linspace(5.0, 11.0, 2401):
        epsilon = sigma * float(v)
        eta = rice_eta(float(v), lambda_d)
        p_shift = cm_upper(p_node, epsilon + du)
        total = p_shift + eta
        if best is None or total < best["total"]:
            best = {
                "v": float(v),
                "epsilon": epsilon,
                "eta": eta,
                "p_shift": p_shift,
                "total": total,
                "p_over_alpha": total / ALPHA,
                "node_over_alpha": node_ratio,
            }
    assert best is not None
    return best


def main() -> None:
    c, i0, l0, chord = endpoint_chord_constants()
    print("Corrected tiny-q endpoint chord")
    print(f"c_X={c:.10f}")
    print(f"I0={i0:.10f}")
    print(f"L0={l0:.10f}")
    print(f"chord coefficient={chord:.10f}")
    print(f"RMS q=0 -> .005  ~ {chord*.005:.10e}")
    print(f"RMS q=0 -> .0025 ~ {chord*.0025:.10e}")

    ep = rough_endpoint_cover()
    print("\nRough endpoint cover")
    for k, v in ep.items():
        print(f"{k:>14s}: {v:.12g}")

    # Rounded conservative half-cell spectral envelopes from the Step-41
    # deterministic calculations. Corrections are Step-34 paired-profile inputs.
    rows = [
        # q, sigma, lambda_d, node correction/alpha, halfwidth
        (0.0050, 2.10e-5, 8.00e4, MAX_POSITIVE_PAIRED_OVER_ALPHA, 0.0025),
        (0.0100, 2.10e-5, 2.00e4, MAX_POSITIVE_PAIRED_OVER_ALPHA, 0.0025),
        (0.0150, 2.10e-5, 8.00e3, MAX_POSITIVE_PAIRED_OVER_ALPHA, 0.0025),
        (0.0200, 2.10e-5, 4.00e3, MAX_POSITIVE_PAIRED_OVER_ALPHA, 0.0025),
        (0.0250, 2.12e-5, 2.50e3, -0.00048, 0.0025),
        (0.0300, 2.15e-5, 1.55e3, MAX_POSITIVE_PAIRED_OVER_ALPHA, 0.0025),
        (0.0350, 2.21e-5, 1.10e3, MAX_POSITIVE_PAIRED_OVER_ALPHA, 0.0025),
        (0.0400, 2.28e-5, 8.20e2, -0.00045, 0.0025),
        (0.0450, 2.38e-5, 6.30e2, -0.000152, 0.0025),
        (0.0500, 2.52e-5, 5.00e2, -0.00070, 0.0025),
        (0.0550, 2.68e-5, 4.00e2, -0.000152, 0.0025),
        (0.0600, 2.89e-5, 3.20e2, -0.00060, 0.0025),
        (0.0650, 3.13e-5, 2.60e2, -0.00115, 0.0025),
        (0.0700, 3.41e-5, 2.15e2, -0.00159, 0.0025),
        (0.0750, 3.72e-5, 1.80e2, -0.00152, 0.0025),
        (0.0767, 1.40e-5, 2.00e2, -0.00188, 0.00085),
    ]

    print("\nFinite-q Rice covers")
    print(
        "q       sigma*      lambda*   node_corr/alpha   v_opt   final_p/alpha"
    )
    worst = (0.0, 0.0)
    for q, sigma, lam, correction, halfwidth in rows:
        out = optimize_finite_cell(
            sigma=sigma,
            lambda_d=lam,
            node_correction_over_alpha=correction,
            q_halfwidth=halfwidth,
        )
        print(
            f"{q:0.4f}  {sigma:10.3e}  {lam:9.3g}  "
            f"{correction:15.8f}  {out['v']:6.3f}  "
            f"{out['p_over_alpha']:13.9f}"
        )
        if out["p_over_alpha"] > worst[1]:
            worst = (q, out["p_over_alpha"])

    print(f"\nworst finite-q row: q={worst[0]:.4f}, p/alpha={worst[1]:.9f}")
    print(
        "NOTE: probability inequalities are analytic. Spectral envelopes, node "
        "profile corrections, Monte Carlo node uncertainties, and grid allowances "
        "are conservative numerical inputs rather than formal interval bounds."
    )


if __name__ == "__main__":
    main()
