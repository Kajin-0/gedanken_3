"""Numerical checks for Experiment 10 near-threshold direct Auger scaling.

This script does not calculate a microscopic Auger coefficient. It verifies:
1. the exact scalar-asymmetry threshold q_th(beta);
2. the collinear threshold partition;
3. positivity of the six-dimensional constrained-final-energy Hessian;
4. nonzero linear opening slope a = -dM_min/dq0 at threshold;
5. activation factors for the 10-um / 300-K witness.
"""

import math
import numpy as np
from scipy.optimize import brentq, minimize_scalar

EG_EV = 0.1239841984
KB_T_EV = 0.0258519998
DELTA_OVER_KBT = EG_EV / (2.0 * KB_T_EV)


def s(q):
    return np.sqrt(1.0 + q * q)


def beta_required(q0, x):
    return (
        2.0 * s(x) + s(q0 - 2.0 * x) - s(q0)
    ) / (2.0 * (q0 - x) ** 2)


def beta_c(q0):
    result = minimize_scalar(
        lambda x: beta_required(q0, x),
        bounds=(0.0, q0 / 2.0),
        method="bounded",
        options={"xatol": 1e-13},
    )
    candidates = [
        (result.fun, result.x),
        (beta_required(q0, 0.0), 0.0),
        (beta_required(q0, q0 / 2.0), q0 / 2.0),
    ]
    return min(candidates, key=lambda item: item[0])


def q_threshold(beta):
    hi = 1.0
    while beta_c(hi)[0] > beta:
        hi *= 1.5
    return brentq(lambda q0: beta_c(q0)[0] - beta, 1e-8, hi)


def electron_energy_vec(k, beta):
    q = np.linalg.norm(k)
    return s(q) + beta * q * q


def hole_energy_vec(k, beta):
    q = np.linalg.norm(k)
    return s(q) - beta * q * q


def final_energy(y, q0, beta):
    k1 = np.array(y[:3], dtype=float)
    k2 = np.array(y[3:], dtype=float)
    k0 = np.array([0.0, 0.0, q0])
    k3 = k0 - k1 - k2
    return (
        electron_energy_vec(k1, beta)
        + electron_energy_vec(k2, beta)
        + hole_energy_vec(k3, beta)
    )


def initial_energy(q0, beta):
    return s(q0) + beta * q0 * q0


def hessian_fd(func, x, h=1e-4):
    n = len(x)
    H = np.zeros((n, n), dtype=float)
    fx = func(x)
    for i in range(n):
        ei = np.zeros(n)
        ei[i] = h
        H[i, i] = (func(x + ei) - 2.0 * fx + func(x - ei)) / h**2
        for j in range(i + 1, n):
            ej = np.zeros(n)
            ej[j] = h
            H[i, j] = H[j, i] = (
                func(x + ei + ej)
                - func(x + ei - ej)
                - func(x - ei + ej)
                + func(x - ei - ej)
            ) / (4.0 * h * h)
    return H


def minimum_mismatch(q0, beta):
    result = minimize_scalar(
        lambda x: (
            2.0 * s(x)
            + s(q0 - 2.0 * x)
            - s(q0)
            - 2.0 * beta * (q0 - x) ** 2
        ),
        bounds=(0.0, q0 / 2.0),
        method="bounded",
        options={"xatol": 1e-13},
    )
    return result.fun


def threshold_diagnostics(beta):
    q0 = q_threshold(beta)
    _, x = beta_c(q0)
    z = q0 - 2.0 * x
    y0 = np.array([0.0, 0.0, x, 0.0, 0.0, x])
    H = hessian_fd(lambda y: final_energy(y, q0, beta), y0)
    eig = np.linalg.eigvalsh(H)

    dq = 1e-5
    dM_dq = (
        minimum_mismatch(q0 + dq, beta)
        - minimum_mismatch(q0 - dq, beta)
    ) / (2.0 * dq)
    a = -dM_dq
    u0 = q0 / s(q0) + 2.0 * beta * q0
    phase_geometry = (a / u0) ** 2 / math.sqrt(np.prod(eig))

    kth_over_delta = s(q0) + beta * q0 * q0 - 1.0
    kth_over_kbt = kth_over_delta * DELTA_OVER_KBT

    return {
        "beta": beta,
        "A_m": 2.0 * beta,
        "q_th": q0,
        "x": x,
        "z": z,
        "K_th_over_kBT": kth_over_kbt,
        "hessian_eigenvalues": eig,
        "a": a,
        "u0": u0,
        "phase_geometry": phase_geometry,
        "lifetime_activation": math.exp(-kth_over_kbt),
        "event_activation": math.exp(-(DELTA_OVER_KBT + kth_over_kbt)),
    }


if __name__ == "__main__":
    # beta ~= 0.04238 corresponds to A_m ~= 0.08476 and K_th ~= 10 kBT.
    diag = threshold_diagnostics(0.04238)
    for key, value in diag.items():
        print(f"{key}: {value}")

    print("\nActivation table")
    rows = [
        (0.40, 5.873),
        (0.20, 7.536),
        (0.10, 9.470),
        (0.08476, 10.000),
        (0.04, 12.848),
        (0.02, 16.273),
        (0.01, 20.675),
    ]
    for A_m, kth in rows:
        print(
            A_m,
            kth,
            math.exp(-kth),
            math.exp(-(DELTA_OVER_KBT + kth)),
        )
