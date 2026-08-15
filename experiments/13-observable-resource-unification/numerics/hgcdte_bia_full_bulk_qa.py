#!/usr/bin/env python3
"""Hard implementation QA for the homogeneous B+/B-/C_k HgCdTe BIA model.

The numerical hierarchy audit is forbidden unless this script passes.
It checks the phase/basis convention against the already validated parent Kane
Hamiltonian before testing the added inversion-asymmetry terms.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
FULL_PATH = HERE / "hgcdte_bia_full_bulk.py"
STRESS_PATH = HERE / "hgcdte_bia_c_linear_stress.py"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


fb = load("full_bia", FULL_PATH)
cs = load("c_stress", STRESS_PATH)
k8 = fb.k8


def tr_block(j, ms):
    u = np.zeros((len(ms), len(ms)), dtype=complex)
    for col, m in enumerate(ms):
        row = ms.index(-m)
        u[row, col] = (-1) ** int(round(j - m))
    return u


UT = np.zeros((8, 8), dtype=complex)
UT[0:2, 0:2] = tr_block(0.5, [0.5, -0.5])
UT[2:6, 2:6] = tr_block(1.5, [1.5, 0.5, -0.5, -1.5])
UT[6:8, 6:8] = tr_block(0.5, [0.5, -0.5])


def tr(a):
    return UT @ a.conj() @ UT.conj().T


def c_only_from_full(kx, ky, kz):
    """Extract the C-only terms exactly as implemented in the full model."""
    h = np.zeros((8, 8), dtype=complex)
    h[2:6, 2:6] = (fb.C / np.sqrt(3.0)) * (
        fb.QX*kx + fb.QY*ky + fb.QZ*kz
    )
    c87 = -1j * np.sqrt(3.0) * fb.C * (
        fb.TYZ.conj().T * kx + fb.TZX.conj().T * ky + fb.TXY.conj().T * kz
    )
    h[2:6, 6:8] = c87
    h[6:8, 2:6] = c87.conj().T
    return h


def d_c_only_dx_from_full():
    d = np.zeros((8, 8), dtype=complex)
    d[2:6, 2:6] = (fb.C / np.sqrt(3.0)) * fb.QX
    dc87 = -1j * np.sqrt(3.0) * fb.C * fb.TYZ.conj().T
    d[2:6, 6:8] = dc87
    d[6:8, 2:6] = dc87.conj().T
    return d


def main():
    points = [
        np.array([0.017, -0.031, 0.043]),
        np.array([-0.12, 0.08, 0.055]),
        np.array([0.21, 0.19, -0.14]),
        np.array([0.37, -0.22, 0.11]),
    ]

    theta2_err = float(np.max(np.abs(UT @ UT.conj() + np.eye(8))))
    p8_err = 0.0
    p7_err = 0.0
    herm_err = 0.0
    tr_bia_err = 0.0
    tr_full_err = 0.0
    tr_v_err = 0.0
    deriv_err = 0.0
    c8_reduction_err = 0.0
    c8_deriv_reduction_err = 0.0

    eps = 1.0e-7

    for kk in points:
        h0 = k8.h8(*kk)
        # Regression gate: the published T_i convention must reproduce the
        # existing parent Kane P blocks exactly in the present basis.
        p8_err = max(
            p8_err,
            float(np.max(np.abs(h0[0:2, 2:6] / k8.P - fb.p_block(*kk))))
        )
        p7_err = max(
            p7_err,
            float(np.max(np.abs(h0[0:2, 6:8] / k8.P - fb.p7_block(*kk))))
        )

        hb = fb.h_bia(*kk)
        hf = fb.h8_full_bia(*kk)
        vf = fb.vx_full_bia(*kk)
        herm_err = max(
            herm_err,
            float(np.max(np.abs(hb - hb.conj().T))),
            float(np.max(np.abs(hf - hf.conj().T))),
        )
        tr_bia_err = max(
            tr_bia_err,
            float(np.max(np.abs(tr(hb) - fb.h_bia(*(-kk)))))
        )
        tr_full_err = max(
            tr_full_err,
            float(np.max(np.abs(tr(hf) - fb.h8_full_bia(*(-kk)))))
        )
        tr_v_err = max(
            tr_v_err,
            float(np.max(np.abs(tr(vf) + fb.vx_full_bia(*(-kk)))))
        )

        kp = kk.copy(); kp[0] += eps
        km = kk.copy(); km[0] -= eps
        dfd = (fb.h8_full_bia(*kp) - fb.h8_full_bia(*km)) / (2.0 * eps)
        dan = k8.dh_dkx(*kk) + fb.dh_bia_dkx(*kk)
        deriv_err = max(deriv_err, float(np.max(np.abs(dfd - dan))))

        # The Gamma8 diagonal C block must reduce exactly to the already
        # symmetry-validated C-linear stress implementation.
        cf = c_only_from_full(*kk)
        c8_reduction_err = max(
            c8_reduction_err,
            float(np.max(np.abs(cf[2:6,2:6] - cs.h_c_linear(*kk)[2:6,2:6])))
        )
        c8_deriv_reduction_err = max(
            c8_deriv_reduction_err,
            float(np.max(np.abs(
                d_c_only_dx_from_full()[2:6,2:6] - cs.DHC_DKX[2:6,2:6]
            )))
        )

    gamma_err = float(np.max(np.abs(fb.h_bia(0.0, 0.0, 0.0))))

    print("Experiment 13 full homogeneous B+/B-/C_k BIA QA")
    print(f"theta_squared_plus_I_error={theta2_err:.12g}")
    print(f"parent_P_Gamma6_Gamma8_error={p8_err:.12g}")
    print(f"parent_P_Gamma6_Gamma7_error={p7_err:.12g}")
    print(f"hermiticity_error_eV={herm_err:.12g}")
    print(f"BIA_TR_error_eV={tr_bia_err:.12g}")
    print(f"full_H_TR_error_eV={tr_full_err:.12g}")
    print(f"full_velocity_TRodd_error_mps={tr_v_err:.12g}")
    print(f"analytic_vs_finite_difference_dHdx_error_eVnm={deriv_err:.12g}")
    print(f"Gamma_BIA_norm_eV={gamma_err:.12g}")
    print(f"Gamma8_C_reduction_error_eV={c8_reduction_err:.12g}")
    print(f"Gamma8_C_derivative_reduction_error_eVnm={c8_deriv_reduction_err:.12g}")
    print(fb.alloy_parameters_text(), end="")

    checks = {
        "theta2": (theta2_err, 1e-12),
        "P_Gamma8": (p8_err, 1e-12),
        "P_Gamma7": (p7_err, 1e-12),
        "hermiticity": (herm_err, 1e-12),
        "BIA_TR": (tr_bia_err, 1e-11),
        "full_TR": (tr_full_err, 1e-11),
        "velocity_TRodd": (tr_v_err, 1e-5),
        "finite_difference": (deriv_err, 2e-8),
        "Gamma": (gamma_err, 1e-15),
        "C8_reduction": (c8_reduction_err, 1e-12),
        "C8_derivative_reduction": (c8_deriv_reduction_err, 1e-12),
    }
    failed = [name for name, (value, tol) in checks.items() if value > tol]
    if failed:
        print("RESULT=FAIL")
        raise SystemExit("failed gates: " + ", ".join(failed))
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
