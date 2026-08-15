#!/usr/bin/env python3
"""Refined hierarchy audit for homogeneous HgCdTe BIA terms.

Compares five models on the same exact-shell/capacity pipeline:
  1. BIA off;
  2. the previously validated Gamma8-diagonal C_k-only stress model;
  3. complete eight-band C_k valence coupling (Gamma8 diagonal + Gamma8-Gamma7);
  4. quadratic B8v^+ + B8v^- only;
  5. full homogeneous B8v^+ + B8v^- + C_k.

Every case uses the same refined quadrature and an independent continuous
ordinary-supremum search for the selected projected-block capacity.
"""

from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent


def load(name, filename):
    path = HERE / filename
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


rf = load("refined_c", "hgcdte_bia_c_linear_refined.py")
cs = rf.bs
fb = load("full_bia", "hgcdte_bia_full_bulk.py")
k8 = fb.k8


def h_c_complete(kx, ky, kz):
    h = np.zeros((8, 8), dtype=complex)
    h[2:6, 2:6] = (fb.C / np.sqrt(3.0)) * (
        fb.QX*kx + fb.QY*ky + fb.QZ*kz
    )
    c87 = -1j * np.sqrt(3.0) * fb.C * (
        fb.TYZ.conj().T*kx + fb.TZX.conj().T*ky + fb.TXY.conj().T*kz
    )
    h[2:6, 6:8] = c87
    h[6:8, 2:6] = c87.conj().T
    return k8.h8(kx, ky, kz) + h


def vx_c_complete(kx, ky, kz):
    d = np.zeros((8, 8), dtype=complex)
    d[2:6, 2:6] = (fb.C / np.sqrt(3.0)) * fb.QX
    dc87 = -1j * np.sqrt(3.0) * fb.C * fb.TYZ.conj().T
    d[2:6, 6:8] = dc87
    d[6:8, 2:6] = dc87.conj().T
    return (k8.dh_dkx(kx, ky, kz) + d) * 1.0e-9 / k8.HBAR_EV_S


def h_b_only(kx, ky, kz):
    # Subtract the C-only valence portion from the full BIA perturbation.
    return k8.h8(kx, ky, kz) + fb.h_bia(kx, ky, kz) - (
        h_c_complete(kx, ky, kz) - k8.h8(kx, ky, kz)
    )


def vx_b_only(kx, ky, kz):
    dc = np.zeros((8, 8), dtype=complex)
    dc[2:6, 2:6] = (fb.C / np.sqrt(3.0)) * fb.QX
    dc87 = -1j * np.sqrt(3.0) * fb.C * fb.TYZ.conj().T
    dc[2:6, 6:8] = dc87
    dc[6:8, 2:6] = dc87.conj().T
    db = fb.dh_bia_dkx(kx, ky, kz) - dc
    return (k8.dh_dkx(kx, ky, kz) + db) * 1.0e-9 / k8.HBAR_EV_S


def rel(new, old):
    return new / old - 1.0


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--carrier-nr", type=int, default=120)
    p.add_argument("--carrier-nmu", type=int, default=10)
    p.add_argument("--carrier-nphi", type=int, default=16)
    p.add_argument("--optical-nr", type=int, default=120)
    p.add_argument("--optical-nmu", type=int, default=10)
    p.add_argument("--optical-nphi", type=int, default=16)
    p.add_argument("--optical-kmax", type=float, default=1.0)
    args = p.parse_args()

    print("Experiment 13 refined homogeneous BIA hierarchy decomposition")
    print(fb.alloy_parameters_text(), end="")
    print()

    common = (
        args.carrier_nr, args.carrier_nmu, args.carrier_nphi,
        args.optical_nr, args.optical_nmu, args.optical_nphi,
        args.optical_kmax, k8.EG, 0.50,
    )

    cases = [
        ("BIA_OFF", k8.h8, k8.vx, 20260815),
        ("GAMMA8_C_ONLY", cs.h8_c, cs.vx_c, 20260816),
        ("COMPLETE_C_K", h_c_complete, vx_c_complete, 20260817),
        ("BPLUS_BMINUS_ONLY", h_b_only, vx_b_only, 20260818),
        ("FULL_BPLUS_BMINUS_CK", fb.h8_full_bia, fb.vx_full_bia, 20260819),
    ]

    results = {}
    for label, hfun, vfun, seed in cases:
        results[label] = rf.evaluate(label, hfun, vfun, *common, seed)

    base = results["BIA_OFF"]
    print("[RELATIVE_TO_BIA_OFF]")
    keys = (
        "nref", "nactive", "support_fraction", "eta_F",
        "continuous_capacity", "tau_cap_continuous", "tau_bound_continuous",
        "full_ratio_continuous", "mean_inverse_selectivity",
    )
    for label, *_ in cases[1:]:
        print(label)
        for key in keys:
            print(f"  {key}={rel(results[label][key], base[key]):.12g}")

    print("[INCREMENTAL_TERM_EFFECTS]")
    # How much the missing Gamma8-Gamma7 C_k channel changes the older C-only audit.
    for key in keys:
        print(
            f"C87_increment_{key}="
            f"{rel(results['COMPLETE_C_K'][key], results['GAMMA8_C_ONLY'][key]):.12g}"
        )
    # How much adding C_k changes the quadratic-B-only model.
    for key in keys:
        print(
            f"C_on_top_of_B_{key}="
            f"{rel(results['FULL_BPLUS_BMINUS_CK'][key], results['BPLUS_BMINUS_ONLY'][key]):.12g}"
        )


if __name__ == "__main__":
    main()
