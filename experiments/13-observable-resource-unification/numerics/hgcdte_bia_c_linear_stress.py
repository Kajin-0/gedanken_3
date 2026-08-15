#!/usr/bin/env python3
"""C-linear bulk-inversion-asymmetry stress test for Experiment 13.

This is deliberately NOT labeled a full BIA calculation. It augments the
controlling second-order 8-band HgCdTe Hamiltonian with the standard
zincblende Gamma8 k-linear BIA invariant weighted by C_k, using linearly
interpolated HgTe/CdTe endpoint parameters.

Purpose:
  1. break the artificial fixed-k PT degeneracy of the BIA-neglecting model;
  2. test the exact-shell prediction that generic one-dimensional active
     parent shells still satisfy S_a^act = 1 identically;
  3. quantify where the BIA perturbation moves the population-bound hierarchy:
     eta_F, active support, shell/global capacity utilization, and global
     capacity.

The quadratic B^+/B^- BIA couplings are intentionally omitted here. Therefore
all numerical conclusions are C-linear stress-test results, not claims for a
complete zincblende BIA Hamiltonian.
"""

from __future__ import annotations

import argparse
import importlib.util
import math
from pathlib import Path

import numpy as np
from scipy.optimize import brentq

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

# Li et al., PRB 95, 035308 (2017), Appendix B / Table II.
# Hg_{1-x}Cd_xTe parameters are linearly interpolated there.
C_HGTE_EV_A = -0.0746
C_CDTE_EV_A = -0.0234
C_ALLOY_EV_A = (1.0 - k8.X) * C_HGTE_EV_A + k8.X * C_CDTE_EV_A
C_ALLOY_EV_NM = 0.1 * C_ALLOY_EV_A


def j32_matrices():
    """Dimensionless J=3/2 matrices in |3/2,m> order m=3/2,...,-3/2."""
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
    jx = 0.5 * (jp + jm)
    jy = (jp - jm) / (2.0j)
    jz = np.diag(ms)
    return jx, jy, jz


JX, JY, JZ = j32_matrices()


def sym(a, b):
    return 0.5 * (a @ b + b @ a)


QX = sym(JX, JY @ JY - JZ @ JZ)
QY = sym(JY, JZ @ JZ - JX @ JX)
QZ = sym(JZ, JX @ JX - JY @ JY)
C_PREF = 2.0 / math.sqrt(3.0) * C_ALLOY_EV_NM


def h_c_linear(kx: float, ky: float, kz: float) -> np.ndarray:
    """Gamma8 C_k BIA invariant, embedded in the current 8-band basis."""
    h = np.zeros((8, 8), dtype=complex)
    h[2:6, 2:6] = C_PREF * (kx * QX + ky * QY + kz * QZ)
    return h


def dhc_dkx() -> np.ndarray:
    d = np.zeros((8, 8), dtype=complex)
    d[2:6, 2:6] = C_PREF * QX
    return d


DHC_DKX = dhc_dkx()


def h8_c(kx: float, ky: float, kz: float) -> np.ndarray:
    return k8.h8(kx, ky, kz) + h_c_linear(kx, ky, kz)


def vx_c(kx: float, ky: float, kz: float) -> np.ndarray:
    # dH/dk is in eV nm; convert to m/s exactly as the parent implementation.
    return (k8.dh_dkx(kx, ky, kz) + DHC_DKX) * 1.0e-9 / k8.HBAR_EV_S


def carrier_state(hfun, kmax=2.0, nr=80, nmu=8, nphi=12):
    energies = []
    weights = []
    for kk, w in k8.grid(kmax, nr, nmu, nphi):
        energies.append(np.linalg.eigvalsh(hfun(*kk)))
        weights.append(w)
    e = np.asarray(energies)
    w = np.asarray(weights)

    def neutrality(mu):
        f = k8.fermi(e, mu)
        ne = np.sum(w[:, None] * f[:, 6:8])
        nh = np.sum(w[:, None] * (1.0 - f[:, :6]))
        return ne - nh

    mu = brentq(neutrality, 0.08, 0.19)
    f = k8.fermi(e, mu)
    below = e < mu
    ne_cross = np.sum(w[:, None] * np.where(~below, f, 0.0))
    nh_cross = np.sum(w[:, None] * np.where(below, 1.0 - f, 0.0))
    return mu, ne_cross + nh_cross


def shell_audit(hfun, vfun, mu, elo, ehi, kmax, nr, nmu, nphi,
                cluster_tol=1.0e-7):
    weighted = 0.0
    r_exact = 0.0
    n_active = 0.0
    sampled_cap2 = 0.0

    weighted_dim = {}
    active_dim = {}
    max_selectivity_by_dim = {}
    selectivity_min = float("inf")
    selectivity_max = 0.0
    nonunit_selectivity_weight = 0.0
    total_active_weight = 0.0
    max_split_near_old_doublet = 0.0

    entries = []

    for kk, weight in k8.grid(kmax, nr, nmu, nphi):
        vals, vecs = np.linalg.eigh(hfun(*kk))
        vel = vecs.conj().T @ vfun(*kk) @ vecs
        f = k8.fermi(vals, mu)
        lower = np.where(vals < mu)[0]
        upper = np.where(vals > mu)[0]

        # Diagnostic: adjacent-pair splitting in the ordering inherited from the
        # 8-band model. This is not used in the theorem, only to expose the scale
        # of same-k degeneracy lifting.
        for p, q in ((0, 1), (2, 3), (4, 5), (6, 7)):
            max_split_near_old_doublet = max(
                max_split_near_old_doublet, abs(float(vals[q] - vals[p]))
            )

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
            rank = int(np.sum(singular > 1.0e-6))
            if rank == 0:
                continue
            lam = float(singular[0] ** 2)
            trace = float(np.sum(singular * singular))
            if lam <= 0.0:
                continue

            stable_rank = trace / lam
            selectivity = rank / stable_rank
            dim = len(group)
            pop = weight * occupation * rank

            r_exact += weight * occupation * trace
            n_active += pop
            sampled_cap2 = max(sampled_cap2, lam)
            weighted_dim[dim] = weighted_dim.get(dim, 0.0) + pop
            active_dim[dim] = active_dim.get(dim, 0) + 1
            max_selectivity_by_dim[dim] = max(
                max_selectivity_by_dim.get(dim, 0.0), selectivity
            )
            selectivity_min = min(selectivity_min, selectivity)
            selectivity_max = max(selectivity_max, selectivity)
            total_active_weight += pop
            if abs(selectivity - 1.0) > 1.0e-8:
                nonunit_selectivity_weight += pop

            entries.append((weight, occupation, rank, trace, lam, selectivity, dim))

    l_bound = 2.0 * weighted
    eta_f = l_bound / r_exact
    cap2 = sampled_cap2

    decomposition = 0.0
    mean_c = 0.0
    mean_inv_s = 0.0
    for weight, occupation, rank, trace, lam, selectivity, _dim in entries:
        pop_weight = weight * occupation * rank / n_active
        c = lam / cap2
        decomposition += pop_weight * c / selectivity
        mean_c += pop_weight * c
        mean_inv_s += pop_weight / selectivity

    return {
        "R_exact": r_exact,
        "L_bound": l_bound,
        "eta_F": eta_f,
        "N_active": n_active,
        "sampled_capacity": math.sqrt(cap2),
        "tau_cap": r_exact / (cap2 * n_active),
        "tau_bound": l_bound / (cap2 * n_active),
        "decomposition": decomposition,
        "mean_capacity_utilization": mean_c,
        "mean_inverse_selectivity": mean_inv_s,
        "selectivity_min": selectivity_min,
        "selectivity_max": selectivity_max,
        "nonunit_selectivity_population_fraction": (
            nonunit_selectivity_weight / total_active_weight
            if total_active_weight > 0 else 0.0
        ),
        "weighted_dim": weighted_dim,
        "block_count_by_dim": active_dim,
        "max_selectivity_by_dim": max_selectivity_by_dim,
        "max_adjacent_pair_split_eV": max_split_near_old_doublet,
    }


def run_case(label, hfun, vfun, carrier_nr, carrier_nmu, carrier_nphi,
             optical_nr, optical_nmu, optical_nphi, optical_kmax, elo, ehi):
    mu, nref = carrier_state(
        hfun, kmax=2.0, nr=carrier_nr, nmu=carrier_nmu, nphi=carrier_nphi
    )
    res = shell_audit(
        hfun, vfun, mu, elo, ehi, optical_kmax,
        optical_nr, optical_nmu, optical_nphi,
    )
    support_fraction = res["N_active"] / nref
    full_ratio_sampled = support_fraction * res["tau_bound"]

    print(f"[{label}]")
    print(f"mu_eV={mu:.12g}")
    print(f"nref_cm3={nref:.12g}")
    print(f"nactive_cm3={res['N_active']:.12g}")
    print(f"support_fraction={support_fraction:.12g}")
    print(f"eta_F={res['eta_F']:.12g}")
    print(f"sampled_capacity_mps={res['sampled_capacity']:.12g}")
    print(f"tau_cap={res['tau_cap']:.12g}")
    print(f"tau_bound={res['tau_bound']:.12g}")
    print(f"full_ratio_sampled={full_ratio_sampled:.12g}")
    print(f"decomposition={res['decomposition']:.12g}")
    print(f"mean_capacity_utilization={res['mean_capacity_utilization']:.12g}")
    print(f"mean_inverse_selectivity={res['mean_inverse_selectivity']:.12g}")
    print(f"selectivity_min={res['selectivity_min']:.12g}")
    print(f"selectivity_max={res['selectivity_max']:.12g}")
    print(
        "nonunit_selectivity_population_fraction="
        f"{res['nonunit_selectivity_population_fraction']:.12g}"
    )
    print(f"max_adjacent_pair_split_eV={res['max_adjacent_pair_split_eV']:.12g}")
    print(f"block_count_by_dim={res['block_count_by_dim']}")
    print(f"max_selectivity_by_dim={res['max_selectivity_by_dim']}")
    print(f"weighted_dim={res['weighted_dim']}")
    print()
    return {
        "mu": mu,
        "nref": nref,
        "support_fraction": support_fraction,
        "full_ratio_sampled": full_ratio_sampled,
        **res,
    }


def rel(new, old):
    return (new / old - 1.0) if old != 0 else float("nan")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--carrier-nr", type=int, default=80)
    p.add_argument("--carrier-nmu", type=int, default=8)
    p.add_argument("--carrier-nphi", type=int, default=12)
    p.add_argument("--optical-nr", type=int, default=80)
    p.add_argument("--optical-nmu", type=int, default=8)
    p.add_argument("--optical-nphi", type=int, default=12)
    p.add_argument("--optical-kmax", type=float, default=0.8)
    p.add_argument("--elo", type=float, default=k8.EG)
    p.add_argument("--ehi", type=float, default=0.50)
    args = p.parse_args()

    # Structural sanity checks for the added invariant.
    if np.max(np.abs(QX - QX.conj().T)) > 1.0e-12:
        raise RuntimeError("QX is not Hermitian")
    if np.max(np.abs(QY - QY.conj().T)) > 1.0e-12:
        raise RuntimeError("QY is not Hermitian")
    if np.max(np.abs(QZ - QZ.conj().T)) > 1.0e-12:
        raise RuntimeError("QZ is not Hermitian")

    print("Experiment 13 HgCdTe C-linear BIA stress test")
    print(f"x_Cd={k8.X:.12g}")
    print(f"C_HgTe_eVA={C_HGTE_EV_A:.12g}")
    print(f"C_CdTe_eVA={C_CDTE_EV_A:.12g}")
    print(f"C_alloy_eVA={C_ALLOY_EV_A:.12g}")
    print("WARNING: quadratic B+/B- BIA terms are omitted; this is C-linear only.")
    print()

    base = run_case(
        "BIA_OFF", k8.h8, k8.vx,
        args.carrier_nr, args.carrier_nmu, args.carrier_nphi,
        args.optical_nr, args.optical_nmu, args.optical_nphi,
        args.optical_kmax, args.elo, args.ehi,
    )
    bia = run_case(
        "C_LINEAR_BIA_ON", h8_c, vx_c,
        args.carrier_nr, args.carrier_nmu, args.carrier_nphi,
        args.optical_nr, args.optical_nmu, args.optical_nphi,
        args.optical_kmax, args.elo, args.ehi,
    )

    print("[RELATIVE_CHANGE_C_ON_VS_OFF]")
    for key in (
        "nref", "support_fraction", "eta_F", "sampled_capacity", "tau_cap",
        "tau_bound", "full_ratio_sampled", "mean_capacity_utilization",
        "mean_inverse_selectivity",
    ):
        print(f"{key}={rel(bia[key], base[key]):.12g}")


if __name__ == "__main__":
    main()
