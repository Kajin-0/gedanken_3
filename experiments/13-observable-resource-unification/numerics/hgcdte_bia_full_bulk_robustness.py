#!/usr/bin/env python3
"""Convergence/robustness audit for the full homogeneous HgCdTe BIA result."""

from __future__ import annotations

import importlib.util
import math
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


rf = load("refined", "hgcdte_bia_c_linear_refined.py")
fb = load("full_bia", "hgcdte_bia_full_bulk.py")
bs = rf.bs
k8 = fb.k8


def hierarchy(hfun, vfun, nr, nmu, nphi, cap, cluster_tol=1e-7):
    mu, nref = bs.carrier_state(hfun, kmax=2.0, nr=nr, nmu=nmu, nphi=nphi)
    res = bs.shell_audit(
        hfun, vfun, mu, k8.EG, 0.50, 1.0,
        nr, nmu, nphi, cluster_tol=cluster_tol,
    )
    cap2 = cap*cap
    support = res["N_active"] / nref
    tau_cap = res["R_exact"] / (cap2 * res["N_active"])
    tau_bound = res["L_bound"] / (cap2 * res["N_active"])
    return {
        "mu": mu,
        "nref": nref,
        "nactive": res["N_active"],
        "support": support,
        "eta_F": res["eta_F"],
        "tau_cap": tau_cap,
        "tau_bound": tau_bound,
        "full_ratio": support * tau_bound,
        "selectivity_min": res["selectivity_min"],
        "selectivity_max": res["selectivity_max"],
        "nonunit_fraction": res["nonunit_selectivity_population_fraction"],
        "block_count_by_dim": res["block_count_by_dim"],
    }


def print_result(label, r):
    print(f"[{label}]")
    for key, value in r.items():
        print(f"{key}={value}")
    print()


def main():
    # Multi-seed continuous ordinary supremum at the same 120x10x16 chemical
    # potential used by the controlling five-case refined hierarchy audit.
    mu_ref, _ = bs.carrier_state(
        fb.h8_full_bia, kmax=2.0, nr=120, nmu=10, nphi=16
    )
    caps = []
    print("[FULL_BIA_CAPACITY_MULTI_SEED]")
    print(f"controlling_mu_eV={mu_ref:.12g}")
    for seed in (20260819, 20260829, 20260839, 20260849):
        cap, kk = rf.numerical_supremum(
            fb.h8_full_bia, fb.vx_full_bia,
            mu_ref, k8.EG, 0.50, 1.0, seed,
        )
        caps.append(cap)
        print(f"seed={seed} capacity_mps={cap:.12g} k={kk.tolist()}")
    print(f"capacity_min_mps={min(caps):.12g}")
    print(f"capacity_max_mps={max(caps):.12g}")
    print(f"capacity_spread_fraction={(max(caps)-min(caps))/np.mean(caps):.12g}")
    cap_full = float(np.mean(caps))
    print()

    # The BIA-off continuous capacity is already independently production-validated.
    cap_off = 1.01763960719e6

    grids = [
        ("GRID_60x6x8", 60, 6, 8),
        ("GRID_80x8x12", 80, 8, 12),
        ("GRID_100x10x12", 100, 10, 12),
    ]
    for label, nr, nmu, nphi in grids:
        off = hierarchy(k8.h8, k8.vx, nr, nmu, nphi, cap_off)
        full = hierarchy(fb.h8_full_bia, fb.vx_full_bia, nr, nmu, nphi, cap_full)
        print_result(label + "_OFF", off)
        print_result(label + "_FULL", full)
        print(f"[{label}_RELATIVE]")
        for key in ("nref", "nactive", "support", "eta_F", "tau_cap", "tau_bound", "full_ratio"):
            print(f"{key}={full[key]/off[key]-1.0:.12g}")
        print()

    # Exact-shell clustering tolerance: a true BIA splitting should remain
    # one-dimensional over tolerances well above numerical diagonalization noise.
    print("[FULL_BIA_CLUSTER_TOLERANCE]")
    for tol in (1e-9, 1e-8, 1e-7, 1e-6, 1e-5):
        r = hierarchy(
            fb.h8_full_bia, fb.vx_full_bia,
            50, 6, 8, cap_full, cluster_tol=tol,
        )
        print(
            f"tol_eV={tol:.1e} selectivity_min={r['selectivity_min']:.12g} "
            f"selectivity_max={r['selectivity_max']:.12g} "
            f"nonunit_fraction={r['nonunit_fraction']:.12g} "
            f"block_count={r['block_count_by_dim']} full_ratio={r['full_ratio']:.12g}"
        )


if __name__ == "__main__":
    main()
