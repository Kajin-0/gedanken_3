#!/usr/bin/env python3
"""Symmetry and convention QA for the Experiment-13 C-linear BIA stress test."""

from __future__ import annotations

import importlib.util
import math
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
STRESS_PATH = HERE / "hgcdte_bia_c_linear_stress.py"
spec = importlib.util.spec_from_file_location("bia_stress", STRESS_PATH)
bs = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(bs)
k8 = bs.k8


def time_reversal_block(j, ms):
    u = np.zeros((len(ms), len(ms)), dtype=complex)
    for col, m in enumerate(ms):
        row = ms.index(-m)
        u[row, col] = (-1) ** int(round(j - m))
    return u


U6 = time_reversal_block(0.5, [0.5, -0.5])
U8 = time_reversal_block(1.5, [1.5, 0.5, -0.5, -1.5])
U7 = time_reversal_block(0.5, [0.5, -0.5])
UT = np.zeros((8, 8), dtype=complex)
UT[0:2, 0:2] = U6
UT[2:6, 2:6] = U8
UT[6:8, 6:8] = U7


def tr_transform(a):
    return UT @ a.conj() @ UT.conj().T


def explicit_c_gamma8(kx, ky, kz):
    """Equivalent Appendix-B C1/C2 form in the same Gamma8 basis."""
    c = bs.C_ALLOY_EV_NM
    kp = kx + 1j * ky
    c1 = -0.5 * c * kp
    c2 = 0.5 * c * kz
    return np.array([
        [0, np.conj(np.conj(c1)), 2*c2, math.sqrt(3)*np.conj(c1)],
        [np.conj(c1), 0, -math.sqrt(3)*c1, -2*c2],
        [2*c2, -math.sqrt(3)*np.conj(c1), 0, c1],
        [math.sqrt(3)*c1, -2*c2, np.conj(c1), 0],
    ], dtype=complex)


def main():
    # Correct a deliberately verbose first-row expression above to make the
    # intended C1 entry explicit and then compare point by point.
    points = [
        np.array([0.017, -0.031, 0.043]),
        np.array([-0.12, 0.08, 0.055]),
        np.array([0.21, 0.19, -0.14]),
    ]

    antiunitary_square = UT @ UT.conj()
    theta2_err = np.max(np.abs(antiunitary_square + np.eye(8)))

    herm_err = 0.0
    tr_base_err = 0.0
    tr_bia_err = 0.0
    tr_v_base_err = 0.0
    tr_v_bia_err = 0.0
    explicit_err = 0.0

    for kk in points:
        hb0 = k8.h8(*kk)
        hb1 = bs.h8_c(*kk)
        hc = bs.h_c_linear(*kk)
        herm_err = max(
            herm_err,
            float(np.max(np.abs(hc - hc.conj().T))),
            float(np.max(np.abs(hb1 - hb1.conj().T))),
        )
        tr_base_err = max(
            tr_base_err,
            float(np.max(np.abs(tr_transform(hb0) - k8.h8(*(-kk))))),
        )
        tr_bia_err = max(
            tr_bia_err,
            float(np.max(np.abs(tr_transform(hb1) - bs.h8_c(*(-kk))))),
        )
        tr_v_base_err = max(
            tr_v_base_err,
            float(np.max(np.abs(tr_transform(k8.vx(*kk)) + k8.vx(*(-kk))))),
        )
        tr_v_bia_err = max(
            tr_v_bia_err,
            float(np.max(np.abs(tr_transform(bs.vx_c(*kk)) + bs.vx_c(*(-kk))))),
        )

        c1 = -0.5 * bs.C_ALLOY_EV_NM * (kk[0] + 1j * kk[1])
        c2 = 0.5 * bs.C_ALLOY_EV_NM * kk[2]
        alt = np.array([
            [0, c1, 2*c2, math.sqrt(3)*np.conj(c1)],
            [np.conj(c1), 0, -math.sqrt(3)*c1, -2*c2],
            [2*c2, -math.sqrt(3)*np.conj(c1), 0, c1],
            [math.sqrt(3)*c1, -2*c2, np.conj(c1), 0],
        ], dtype=complex)
        explicit_err = max(
            explicit_err,
            float(np.max(np.abs(hc[2:6, 2:6] - alt))),
        )

    gamma_bia = float(np.max(np.abs(bs.h_c_linear(0.0, 0.0, 0.0))))

    print("Experiment 13 C-linear BIA symmetry QA")
    print(f"theta_squared_plus_I_error={theta2_err:.12g}")
    print(f"hermiticity_error_eV={herm_err:.12g}")
    print(f"base_TR_error_eV={tr_base_err:.12g}")
    print(f"C_BIA_TR_error_eV={tr_bia_err:.12g}")
    print(f"base_velocity_TRodd_error_mps={tr_v_base_err:.12g}")
    print(f"C_BIA_velocity_TRodd_error_mps={tr_v_bia_err:.12g}")
    print(f"Gamma_C_BIA_norm_eV={gamma_bia:.12g}")
    print(f"invariant_vs_C1C2_matrix_error_eV={explicit_err:.12g}")

    tolerances = {
        "theta2": (theta2_err, 1e-12),
        "hermiticity": (herm_err, 1e-12),
        "base_TR": (tr_base_err, 1e-11),
        "C_BIA_TR": (tr_bia_err, 1e-11),
        "base_v_TRodd": (tr_v_base_err, 1e-5),
        "C_BIA_v_TRodd": (tr_v_bia_err, 1e-5),
        "Gamma": (gamma_bia, 1e-15),
        "matrix_convention": (explicit_err, 1e-12),
    }
    failed = [name for name, (value, tol) in tolerances.items() if value > tol]
    if failed:
        raise SystemExit("FAILED: " + ", ".join(failed))
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
