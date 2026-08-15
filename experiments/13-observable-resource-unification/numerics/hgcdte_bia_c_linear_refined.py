#!/usr/bin/env python3
"""Refined C-linear BIA audit for the Experiment-13 HgCdTe hierarchy.

Builds on hgcdte_bia_c_linear_stress.py and adds:
  * refined hierarchy quadrature;
  * selected-support-only same-k splitting diagnostic;
  * continuous ordinary-supremum search for the projected optical capacity;
  * full bound/reference ratios using the continuous capacity rather than the
    sampled quadrature maximum.

Still C-linear only: quadratic B^+/B^- BIA terms remain excluded.
"""

from __future__ import annotations

import argparse
import importlib.util
import math
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution

HERE = Path(__file__).resolve().parent
STRESS_PATH = HERE / "hgcdte_bia_c_linear_stress.py"
spec = importlib.util.spec_from_file_location("bia_stress", STRESS_PATH)
bs = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(bs)
k8 = bs.k8


def spherical_k(x):
    k, theta, phi = x
    st = math.sin(theta)
    return np.array([
        k * st * math.cos(phi),
        k * st * math.sin(phi),
        k * math.cos(theta),
    ])


def local_capacity(hfun, vfun, kk, mu, elo, ehi, cluster_tol=1.0e-7):
    vals, vecs = np.linalg.eigh(hfun(*kk))
    vel = vecs.conj().T @ vfun(*kk) @ vecs
    groups = k8.energy_clusters(vals, tol=cluster_tol)
    cap2 = 0.0

    for group in groups:
        eg = float(np.mean(vals[group]))
        partners = []
        if eg > mu:
            for gl in groups:
                el = float(np.mean(vals[gl]))
                if el < mu and elo <= eg - el <= ehi:
                    partners += gl
            if partners:
                sv = np.linalg.svd(vel[np.ix_(group, partners)], compute_uv=False)
                if sv.size:
                    cap2 = max(cap2, float(sv[0] ** 2))
        elif eg < mu:
            for gu in groups:
                eu = float(np.mean(vals[gu]))
                if eu > mu and elo <= eu - eg <= ehi:
                    partners += gu
            if partners:
                sv = np.linalg.svd(vel[np.ix_(partners, group)], compute_uv=False)
                if sv.size:
                    cap2 = max(cap2, float(sv[0] ** 2))
    return math.sqrt(cap2)


def numerical_supremum(hfun, vfun, mu, elo, ehi, kmax, seed):
    def objective(x):
        kk = spherical_k(x)
        return -local_capacity(hfun, vfun, kk, mu, elo, ehi)

    result = differential_evolution(
        objective,
        bounds=[(0.0, kmax), (0.0, math.pi), (0.0, 2.0 * math.pi)],
        seed=seed,
        popsize=14,
        maxiter=65,
        polish=True,
        tol=1.0e-8,
        updating="immediate",
        workers=1,
    )
    kk = spherical_k(result.x)
    return -float(result.fun), kk


def selected_splitting(hfun, mu, elo, ehi, kmax, nr, nmu, nphi):
    max_split = 0.0
    weighted_split = 0.0
    total_weight = 0.0
    k_selected_min = float("inf")
    k_selected_max = 0.0
    selected_points = 0

    for kk, weight in k8.grid(kmax, nr, nmu, nphi):
        vals = np.linalg.eigvalsh(hfun(*kk))
        lower = np.where(vals < mu)[0]
        upper = np.where(vals > mu)[0]
        selected_here = False
        for i in lower:
            for j in upper:
                de = vals[j] - vals[i]
                if elo <= de <= ehi:
                    selected_here = True
                    break
            if selected_here:
                break
        if not selected_here:
            continue

        selected_points += 1
        kmag = float(np.linalg.norm(kk))
        k_selected_min = min(k_selected_min, kmag)
        k_selected_max = max(k_selected_max, kmag)
        split = max(abs(float(vals[q] - vals[p])) for p, q in ((0,1),(2,3),(4,5),(6,7)))
        max_split = max(max_split, split)
        weighted_split += weight * split
        total_weight += weight

    return {
        "selected_points": selected_points,
        "k_selected_min": k_selected_min,
        "k_selected_max": k_selected_max,
        "max_selected_adjacent_pair_split_eV": max_split,
        "weighted_selected_adjacent_pair_split_eV": (
            weighted_split / total_weight if total_weight > 0 else 0.0
        ),
    }


def evaluate(label, hfun, vfun, carrier_nr, carrier_nmu, carrier_nphi,
             optical_nr, optical_nmu, optical_nphi, optical_kmax,
             elo, ehi, seed):
    mu, nref = bs.carrier_state(
        hfun, kmax=2.0, nr=carrier_nr, nmu=carrier_nmu, nphi=carrier_nphi
    )
    res = bs.shell_audit(
        hfun, vfun, mu, elo, ehi, optical_kmax,
        optical_nr, optical_nmu, optical_nphi,
    )
    cap_sup, kk_sup = numerical_supremum(
        hfun, vfun, mu, elo, ehi, optical_kmax, seed
    )
    split = selected_splitting(
        hfun, mu, elo, ehi, optical_kmax,
        optical_nr, optical_nmu, optical_nphi,
    )

    cap2 = cap_sup ** 2
    tau_cap_sup = res["R_exact"] / (cap2 * res["N_active"])
    tau_bound_sup = res["L_bound"] / (cap2 * res["N_active"])
    support_fraction = res["N_active"] / nref
    full_ratio_sup = support_fraction * tau_bound_sup

    print(f"[{label}]")
    print(f"mu_eV={mu:.12g}")
    print(f"nref_cm3={nref:.12g}")
    print(f"nactive_cm3={res['N_active']:.12g}")
    print(f"support_fraction={support_fraction:.12g}")
    print(f"eta_F={res['eta_F']:.12g}")
    print(f"sampled_capacity_mps={res['sampled_capacity']:.12g}")
    print(f"continuous_capacity_mps={cap_sup:.12g}")
    print(f"capacity_sup_kx={kk_sup[0]:.12g}")
    print(f"capacity_sup_ky={kk_sup[1]:.12g}")
    print(f"capacity_sup_kz={kk_sup[2]:.12g}")
    print(f"capacity_sup_kmag={np.linalg.norm(kk_sup):.12g}")
    print(f"tau_cap_continuous={tau_cap_sup:.12g}")
    print(f"tau_bound_continuous={tau_bound_sup:.12g}")
    print(f"full_ratio_continuous={full_ratio_sup:.12g}")
    print(f"mean_inverse_selectivity_sampled={res['mean_inverse_selectivity']:.12g}")
    print(f"selectivity_min={res['selectivity_min']:.12g}")
    print(f"selectivity_max={res['selectivity_max']:.12g}")
    print(f"nonunit_selectivity_population_fraction={res['nonunit_selectivity_population_fraction']:.12g}")
    print(f"block_count_by_dim={res['block_count_by_dim']}")
    for key, value in split.items():
        print(f"{key}={value}")
    print()

    return {
        "mu": mu,
        "nref": nref,
        "nactive": res["N_active"],
        "support_fraction": support_fraction,
        "eta_F": res["eta_F"],
        "sampled_capacity": res["sampled_capacity"],
        "continuous_capacity": cap_sup,
        "tau_cap_continuous": tau_cap_sup,
        "tau_bound_continuous": tau_bound_sup,
        "full_ratio_continuous": full_ratio_sup,
        "mean_inverse_selectivity": res["mean_inverse_selectivity"],
        **split,
    }


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
    p.add_argument("--elo", type=float, default=k8.EG)
    p.add_argument("--ehi", type=float, default=0.50)
    args = p.parse_args()

    print("Experiment 13 refined HgCdTe C-linear BIA audit")
    print(f"x_Cd={k8.X:.12g}")
    print(f"C_alloy_eVA={bs.C_ALLOY_EV_A:.12g}")
    print("WARNING: C-linear BIA only; quadratic B+/B- terms are omitted.")
    print()

    base = evaluate(
        "BIA_OFF", k8.h8, k8.vx,
        args.carrier_nr, args.carrier_nmu, args.carrier_nphi,
        args.optical_nr, args.optical_nmu, args.optical_nphi,
        args.optical_kmax, args.elo, args.ehi, 20260815,
    )
    bia = evaluate(
        "C_LINEAR_BIA_ON", bs.h8_c, bs.vx_c,
        args.carrier_nr, args.carrier_nmu, args.carrier_nphi,
        args.optical_nr, args.optical_nmu, args.optical_nphi,
        args.optical_kmax, args.elo, args.ehi, 20260816,
    )

    print("[RELATIVE_CHANGE_C_ON_VS_OFF]")
    for key in (
        "nref", "nactive", "support_fraction", "eta_F",
        "continuous_capacity", "tau_cap_continuous", "tau_bound_continuous",
        "full_ratio_continuous", "mean_inverse_selectivity",
    ):
        print(f"{key}={rel(bia[key], base[key]):.12g}")


if __name__ == "__main__":
    main()
