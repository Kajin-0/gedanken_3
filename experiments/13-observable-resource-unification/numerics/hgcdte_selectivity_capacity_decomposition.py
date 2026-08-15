#!/usr/bin/env python3
"""Experiment-13 stable-rank decomposition of the Experiment-12 HgCdTe model.

Loads the authoritative second-order eight-band Kane implementation from
Experiment 12 and decomposes the active-population theorem tightness into

    Fermi/Kubo efficiency
    x shell capacity utilization
    x inverse coherent selectivity.

This is a numerical validation of the exact dispersive identity in
DISPERSIVE_SELECTIVITY_CAPACITY_DECOMPOSITION_2026-08-15.md.

The default quadrature is a moderately refined audit, not the production
continuous-supremum calculation. An optional production capacity can be
supplied to evaluate the final capacity factors against the separately
validated ordinary supremum.
"""

from __future__ import annotations

import argparse
import importlib.util
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
KANE_PATH = (
    ROOT
    / "experiments"
    / "12-oscillator-strength-state-count-bound"
    / "numerics"
    / "kane_8band_tightness.py"
)

spec = importlib.util.spec_from_file_location("kane8", KANE_PATH)
k8 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(k8)


def shell_audit(
    mu: float,
    elo: float,
    ehi: float,
    kmax: float,
    nr: int,
    nmu: int,
    nphi: int,
    cluster_tol: float = 1.0e-7,
):
    weighted = 0.0  # Experiment-12 transition sum; observable L = 2*weighted.
    r_exact = 0.0   # Exact thermally weighted velocity strength R_B.
    n_active = 0.0
    n_parent = 0.0
    sampled_cap2 = 0.0
    entries = []

    for kk, weight in k8.grid(kmax, nr, nmu, nphi):
        vals, vecs = np.linalg.eigh(k8.h8(*kk))
        vel = vecs.conj().T @ k8.vx(*kk) @ vecs
        f = k8.fermi(vals, mu)
        lower = np.where(vals < mu)[0]
        upper = np.where(vals > mu)[0]

        # Observable Fermi/Kubo lower functional.
        for i in lower:
            for j in upper:
                de = vals[j] - vals[i]
                if elo <= de <= ehi:
                    amp2 = abs(vel[j, i]) ** 2
                    weighted += (
                        weight
                        * (f[i] - f[j])
                        * amp2
                        / (math.exp(de / (2.0 * k8.KT)) - 1.0)
                    )

        groups = k8.energy_clusters(vals, tol=cluster_tol)
        for group in groups:
            eg = float(np.mean(vals[group]))
            partners = []

            if eg > mu:
                for gl in groups:
                    el = float(np.mean(vals[gl]))
                    if el < mu and elo <= eg - el <= ehi:
                        partners += gl
                if not partners:
                    continue
                block = vel[np.ix_(group, partners)]
                occupation = float(np.mean(f[group]))
            elif eg < mu:
                for gu in groups:
                    eu = float(np.mean(vals[gu]))
                    if eu > mu and elo <= eu - eg <= ehi:
                        partners += gu
                if not partners:
                    continue
                block = vel[np.ix_(partners, group)]
                occupation = float(np.mean(1.0 - f[group]))
            else:
                continue

            singular = np.linalg.svd(block, compute_uv=False)
            if singular.size == 0:
                continue

            lam = float(singular[0] ** 2)
            # Numerical rank threshold is deliberately many orders below the
            # physical ~1e6 m/s scale. Exact model degeneracies have already
            # been grouped by energy_clusters().
            rank = int(np.sum(singular > 1.0e-6))
            trace = float(np.sum(singular * singular))
            if rank == 0 or lam <= 0.0:
                continue

            r_exact += weight * occupation * trace
            n_active += weight * occupation * rank
            n_parent += weight * occupation * len(group)
            sampled_cap2 = max(sampled_cap2, lam)
            entries.append((weight, occupation, len(group), rank, trace, lam))

    l_obs = 2.0 * weighted
    eta_f = l_obs / r_exact

    return {
        "R_exact": r_exact,
        "L_observable": l_obs,
        "eta_F": eta_f,
        "N_active": n_active,
        "N_parent_selected": n_parent,
        "sampled_cap2": sampled_cap2,
        "entries": entries,
    }


def decompose(result, cap: float):
    cap2 = cap * cap
    n_active = result["N_active"]

    weighted_product = 0.0
    mean_c = 0.0
    mean_inverse_selectivity = 0.0
    mean_selectivity = 0.0
    s_min = float("inf")
    s_max = 0.0

    for weight, occupation, _dim, rank, trace, lam in result["entries"]:
        stable_rank = trace / lam
        selectivity = rank / stable_rank
        c = lam / cap2
        pop_weight = weight * occupation * rank / n_active

        weighted_product += pop_weight * c / selectivity
        mean_c += pop_weight * c
        mean_inverse_selectivity += pop_weight / selectivity
        mean_selectivity += pop_weight * selectivity
        s_min = min(s_min, selectivity)
        s_max = max(s_max, selectivity)

    tau_cap = result["R_exact"] / (cap2 * n_active)
    tau_obs = result["L_observable"] / (cap2 * n_active)

    return {
        "capacity": cap,
        "tau_capacity": tau_cap,
        "tau_observable": tau_obs,
        "decomposition_sum": weighted_product,
        "mean_capacity_utilization": mean_c,
        "mean_inverse_selectivity": mean_inverse_selectivity,
        "mean_selectivity": mean_selectivity,
        "selectivity_min": s_min,
        "selectivity_max": s_max,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--nr", type=int, default=100)
    parser.add_argument("--nmu", type=int, default=10)
    parser.add_argument("--nphi", type=int, default=16)
    parser.add_argument("--kmax", type=float, default=1.0)
    parser.add_argument("--elo", type=float, default=k8.EG)
    parser.add_argument("--ehi", type=float, default=0.50)
    parser.add_argument(
        "--production-capacity",
        type=float,
        default=1.01764e6,
        help="Separately validated ordinary-supremum v_B^cap in m/s.",
    )
    args = parser.parse_args()

    # The production chemical potential is obtained from the Experiment-12
    # carrier-state calculation. Use a moderately refined copy here so this
    # companion remains self-contained.
    mu, *_ = k8.carrier_state(kmax=2.0, nr=100, nmu=8, nphi=12)

    result = shell_audit(
        mu,
        args.elo,
        args.ehi,
        args.kmax,
        args.nr,
        args.nmu,
        args.nphi,
    )

    sampled_cap = math.sqrt(result["sampled_cap2"])
    sampled = decompose(result, sampled_cap)
    production = decompose(result, args.production_capacity)

    print("Experiment-13 HgCdTe stable-rank decomposition")
    print(f"mu = {mu:.9f} eV")
    print(f"window = [{args.elo:.9f}, {args.ehi:.6f}] eV")
    print(f"R_exact = {result['R_exact']:.9e} cm^-3 (m/s)^2")
    print(f"L_observable = {result['L_observable']:.9e} cm^-3 (m/s)^2")
    print(f"eta_F = {result['eta_F']:.9f}")
    print(f"N_active = {result['N_active']:.9e} cm^-3")
    print(f"N_parent_selected = {result['N_parent_selected']:.9e} cm^-3")
    print()

    for label, dec in (("sampled", sampled), ("production-cap", production)):
        print(label)
        for key, value in dec.items():
            print(f"  {key}: {value:.12g}")
        print(
            "  closure eta_F*tau_capacity: "
            f"{result['eta_F'] * dec['tau_capacity']:.12g}"
        )
        print()


if __name__ == "__main__":
    main()
