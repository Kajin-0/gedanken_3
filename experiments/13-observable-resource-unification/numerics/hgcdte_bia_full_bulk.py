#!/usr/bin/env python3
"""Homogeneous-bulk BIA extension of the Experiment-13 HgCdTe 8-band model.

Model scope
-----------
Adds the zero-strain, zero-magnetic-field homogeneous-bulk inversion-asymmetry
terms from the standard 6c/8v/7v block formulation:

  * B8v^+ quadratic 6c-8v coupling;
  * B8v^- quadratic 6c-8v coupling;
  * C_k linear 8v-8v coupling;
  * C_k linear 8v-7v coupling.

For a homogeneous scalar B7v and commuting bulk momenta, the published
6c-7v B7v term is proportional to k_[i B7v k_j] and vanishes identically.

The HgTe/CdTe effective B^+, B^-, and C_k endpoint values are those used by
Li et al. (PRB 95, 035308 (2017)); linear alloy interpolation is used, as in
that work. This script deliberately describes the result as the homogeneous
B+/B-/C_k model, not as every possible atomistic/interface inversion term.
"""

from __future__ import annotations

import importlib.util
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
KANE_PATH = (
    ROOT / "experiments" / "12-oscillator-strength-state-count-bound"
    / "numerics" / "kane_8band_tightness.py"
)
spec = importlib.util.spec_from_file_location("kane8", KANE_PATH)
k8 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(k8)

# Li et al., PRB 95, 035308 (2017), effective HgTe/CdTe BIA parameters.
# B parameters: eV A^2 -> eV nm^2 by x 0.01.
# C parameter: eV A -> eV nm by x 0.1.
BPLUS_HGTE_EV_A2 = -20.0
BPLUS_CDTE_EV_A2 = -21.44
BMINUS_HGTE_EV_A2 = 1.0
BMINUS_CDTE_EV_A2 = -0.635
C_HGTE_EV_A = -0.0746
C_CDTE_EV_A = -0.0234

BPLUS_EV_A2 = (1.0 - k8.X) * BPLUS_HGTE_EV_A2 + k8.X * BPLUS_CDTE_EV_A2
BMINUS_EV_A2 = (1.0 - k8.X) * BMINUS_HGTE_EV_A2 + k8.X * BMINUS_CDTE_EV_A2
C_EV_A = (1.0 - k8.X) * C_HGTE_EV_A + k8.X * C_CDTE_EV_A

BPLUS = 0.01 * BPLUS_EV_A2
BMINUS = 0.01 * BMINUS_EV_A2
C = 0.1 * C_EV_A


def j32_matrices():
    j = 1.5
    ms = np.array([1.5, 0.5, -0.5, -1.5])
    jp = np.zeros((4, 4), dtype=complex)
    for col, m in enumerate(ms):
        mp = m + 1.0
        rows = np.where(np.isclose(ms, mp))[0]
        if rows.size:
            row = int(rows[0])
            jp[row, col] = math.sqrt(j * (j + 1.0) - m * (m + 1.0))
    jm = jp.conj().T
    return 0.5*(jp+jm), (jp-jm)/(2.0j), np.diag(ms)


JX, JY, JZ = j32_matrices()

# Vector-operator matrices in the exact Gamma6/Gamma8 phase convention of the
# parent Kane implementation. The ordinary sqrt(3) P T.k block is regression-
# checked against k8.h8 before any BIA calculation is accepted.
TX = 1.0/(3.0*math.sqrt(2.0)) * np.array([
    [-math.sqrt(3.0), 0.0, 1.0, 0.0],
    [0.0, -1.0, 0.0, math.sqrt(3.0)],
], dtype=complex)
TY = -1j/(3.0*math.sqrt(2.0)) * np.array([
    [math.sqrt(3.0), 0.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, math.sqrt(3.0)],
], dtype=complex)
TZ = math.sqrt(2.0)/3.0 * np.array([
    [0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 1.0, 0.0],
], dtype=complex)

TXX = 2.0 * TX @ JX
TYY = 2.0 * TY @ JY
TZZ = 2.0 * TZ @ JZ
TXY = TX @ JY + TY @ JX
TYZ = TY @ JZ + TZ @ JY
TZX = TZ @ JX + TX @ JZ


def anti(a, b):
    return a @ b + b @ a


QX = anti(JX, JY @ JY - JZ @ JZ)
QY = anti(JY, JZ @ JZ - JX @ JX)
QZ = anti(JZ, JX @ JX - JY @ JY)


def p_block(kx, ky, kz):
    """Published Gamma6-Gamma8 ordinary Kane block divided by P."""
    return math.sqrt(3.0) * (kx*TX + ky*TY + kz*TZ)


def p7_block(kx, ky, kz):
    """Published Gamma6-Gamma7 ordinary Kane block divided by P."""
    sx = np.array([[0,1],[1,0]], dtype=complex)
    sy = np.array([[0,-1j],[1j,0]], dtype=complex)
    sz = np.array([[1,0],[0,-1]], dtype=complex)
    return -(kx*sx + ky*sy + kz*sz) / math.sqrt(3.0)


def h_bia(kx: float, ky: float, kz: float) -> np.ndarray:
    h = np.zeros((8, 8), dtype=complex)

    # B8v^+ homogeneous limit of the symmetrized quadratic block.
    hp = 1j * math.sqrt(3.0) * BPLUS * (
        TX * (ky*kz) + TY * (kz*kx) + TZ * (kx*ky)
    )

    # Independent B8v^- quadratic tensor block.
    scalar_q = (2.0/3.0)*kz*kz - (1.0/3.0)*kx*kx - (1.0/3.0)*ky*ky
    hm = (math.sqrt(3.0)/2.0) * BMINUS * (
        (TXX - TYY) * scalar_q - TZZ * (kx*kx - ky*ky)
    )

    h[0:2, 2:6] += hp + hm
    h[2:6, 0:2] += (hp + hm).conj().T

    # Full constant-C_k valence contribution: Gamma8 diagonal plus Gamma8-Gamma7.
    h[2:6, 2:6] += (C / math.sqrt(3.0)) * (
        QX*kx + QY*ky + QZ*kz
    )
    c87 = -1j * math.sqrt(3.0) * C * (
        TYZ.conj().T * kx + TZX.conj().T * ky + TXY.conj().T * kz
    )
    h[2:6, 6:8] += c87
    h[6:8, 2:6] += c87.conj().T

    # The homogeneous B7v commutator block vanishes for scalar constant B7v.
    return h


def dh_bia_dkx(kx: float, ky: float, kz: float) -> np.ndarray:
    d = np.zeros((8, 8), dtype=complex)

    dp = 1j * math.sqrt(3.0) * BPLUS * (TY*kz + TZ*ky)
    dm = (math.sqrt(3.0)/2.0) * BMINUS * (
        (TXX - TYY) * (-(2.0/3.0)*kx) - TZZ * (2.0*kx)
    )
    d[0:2, 2:6] += dp + dm
    d[2:6, 0:2] += (dp + dm).conj().T

    d[2:6, 2:6] += (C / math.sqrt(3.0)) * QX
    dc87 = -1j * math.sqrt(3.0) * C * TYZ.conj().T
    d[2:6, 6:8] += dc87
    d[6:8, 2:6] += dc87.conj().T
    return d


def h8_full_bia(kx: float, ky: float, kz: float) -> np.ndarray:
    return k8.h8(kx, ky, kz) + h_bia(kx, ky, kz)


def vx_full_bia(kx: float, ky: float, kz: float) -> np.ndarray:
    return (k8.dh_dkx(kx, ky, kz) + dh_bia_dkx(kx, ky, kz)) * 1.0e-9 / k8.HBAR_EV_S


def alloy_parameters_text():
    return (
        f"x_Cd={k8.X:.12g}\n"
        f"Bplus_eVA2={BPLUS_EV_A2:.12g}\n"
        f"Bminus_eVA2={BMINUS_EV_A2:.12g}\n"
        f"Ck_eVA={C_EV_A:.12g}\n"
    )


if __name__ == "__main__":
    print("Experiment 13 homogeneous B+/B-/C_k HgCdTe BIA model")
    print(alloy_parameters_text(), end="")
