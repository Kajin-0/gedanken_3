#!/usr/bin/env python3
"""Referee audit for Experiment 12 Rev9/Rev10 HgCdTe validation.

Purpose
-------
1. Check the proposed isolated-Gamma capacity correction against the actual
   cross-chemical-potential selection used by the theorem.
2. Replace the sampled quadrature maximum by a reproducible numerical search
   for the ordinary supremum of the projected-block capacity on each bounded
   optical k-domain.
3. Recompute the theorem ratios with that ordinary-supremum denominator.
4. Decompose tightness into

       n_bound / n_ref
       = (n_bound / n_B^act) * (n_B^act / n_ref)

   using the exact selected-block support ranks on the production quadrature.

The underlying Hamiltonian and production integrals are imported from
``kane_8band_tightness.py`` so this audit cannot silently drift to a different
model.

The global optimization is a numerical supremum search, not an interval-
arithmetic proof. A fixed seed makes the audit reproducible. The manuscript
continues to describe the HgCdTe calculation as a numerical validation.
"""

import math
import numpy as np
from scipy.optimize import differential_evolution

from kane_8band_tightness import (
    EG,
    T_K,
    carrier_state,
    energy_clusters,
    fermi,
    grid,
    h8,
    optical_bound,
    optical_point,
    vx,
)

PROD_NR = 160
PROD_NMU = 10
PROD_NPHI = 16
DENSE_NR = 200
DENSE_NMU = 12
DENSE_NPHI = 20
CLUSTER_TOL = 1.0e-7
RANK_THRESHOLD_MPS = 1.0e-6

WINDOWS = [
    ("Eg..1.5Eg", EG, 1.5 * EG, 0.30),
    ("Eg..2Eg", EG, 2.0 * EG, 0.45),
    ("Eg..3Eg", EG, 3.0 * EG, 0.70),
    ("Eg..0.5eV", EG, 0.50, 1.00),
]


def spherical_k(x):
    """Convert (k, theta, phi) to Cartesian k in nm^-1."""
    k, theta, phi = x
    st = math.sin(theta)
    return np.array(
        [
            k * st * math.cos(phi),
            k * st * math.sin(phi),
            k * math.cos(theta),
        ]
    )


def local_capacity_and_pairmax(x, mu, elo, ehi):
    kk = spherical_k(x)
    _, cap2, pair2, _ = optical_point(
        kk, mu, elo, ehi, cluster_tol=CLUSTER_TOL
    )
    return math.sqrt(cap2), math.sqrt(pair2)


def numerical_supremum(mu, elo, ehi, kmax, quantity="capacity", seed=20260815):
    """Reproducible global search of the ordinary local-block supremum."""

    def objective(x):
        cap, pair = local_capacity_and_pairmax(x, mu, elo, ehi)
        value = cap if quantity == "capacity" else pair
        return -value

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
    value = -float(result.fun)
    kk = spherical_k(result.x)
    return value, kk, result.x


def selected_rank(singular_values, threshold=RANK_THRESHOLD_MPS):
    return int(np.sum(np.asarray(singular_values) > threshold))


def active_point(kk, mu, elo, ehi, rank_threshold=RANK_THRESHOLD_MPS):
    """Thermal selected-support population per one k point, before k weight."""
    vals, U = np.linalg.eigh(h8(*kk))
    M = U.conj().T @ vx(*kk) @ U
    groups = energy_clusters(vals, tol=CLUSTER_TOL)

    ne_act = 0.0
    nh_act = 0.0

    for g in groups:
        eg = float(np.mean(vals[g]))
        if eg > mu:
            partners = []
            for gl in groups:
                el = float(np.mean(vals[gl]))
                if el < mu and elo <= eg - el <= ehi:
                    partners += gl
            if partners:
                sv = np.linalg.svd(M[np.ix_(g, partners)], compute_uv=False)
                ne_act += float(fermi(eg, mu)) * selected_rank(
                    sv, threshold=rank_threshold
                )

        elif eg < mu:
            partners = []
            for gu in groups:
                eu = float(np.mean(vals[gu]))
                if eu > mu and elo <= eu - eg <= ehi:
                    partners += gu
            if partners:
                sv = np.linalg.svd(M[np.ix_(partners, g)], compute_uv=False)
                nh_act += float(1.0 - fermi(eg, mu)) * selected_rank(
                    sv, threshold=rank_threshold
                )

    return ne_act, nh_act


def active_population(mu, elo, ehi, kmax, nr, nmu, nphi, rank_threshold=RANK_THRESHOLD_MPS):
    ne_act = 0.0
    nh_act = 0.0
    for kk, weight in grid(kmax, nr, nmu, nphi):
        ne_k, nh_k = active_point(
            kk, mu, elo, ehi, rank_threshold=rank_threshold
        )
        ne_act += weight * ne_k
        nh_act += weight * nh_k
    return ne_act, nh_act


def main():
    print("Experiment 12 HgCdTe supremum / active-support referee audit")
    print(f"T = {T_K:.1f} K")
    print(
        "production quadrature = "
        f"Nk={PROD_NR}, Ncos={PROD_NMU}, Nphi={PROD_NPHI}"
    )
    print(
        "denser audit grid      = "
        f"Nk={DENSE_NR}, Ncos={DENSE_NMU}, Nphi={DENSE_NPHI}"
    )

    mu, ne, nh, ne_cross, nh_cross = carrier_state(
        kmax=2.0, nr=PROD_NR, nmu=PROD_NMU, nphi=PROD_NPHI
    )
    nref = ne_cross + nh_cross

    print("\nEquilibrium cross-mu state:")
    print(f"mu = {mu:.9f} eV")
    print(f"mu - Eg = {(mu - EG) * 1e3:.3f} meV")
    print(f"n_ref = {nref:.6e} cm^-3")

    gamma_vals = np.linalg.eigvalsh(h8(0.0, 0.0, 0.0))
    gamma_upper = gamma_vals[gamma_vals > mu]
    print("\nGamma-point cross-mu audit:")
    print("Gamma eigenvalues (eV):", np.array2string(gamma_vals, precision=9))
    print(f"number of Gamma states above mu = {len(gamma_upper)}")
    if len(gamma_upper) == 0:
        print(
            "RESULT: the selected cross-mu projected block is empty at Gamma; "
            "the proposed isolated Gamma8->Gamma6 capacity correction does not apply."
        )

    print("\nOrdinary-supremum and active-support audit:")
    header = (
        "window        sampled_cap  sup_cap      |k|_sup   "
        "ratio_sup  nact/nref  bound/nact"
    )
    print(header)

    broad_pair_sup = None
    for index, (name, elo, ehi, optical_kmax) in enumerate(WINDOWS):
        prod = optical_bound(
            mu,
            nref,
            elo,
            ehi,
            optical_kmax,
            nr=PROD_NR,
            nmu=PROD_NMU,
            nphi=PROD_NPHI,
            cluster_tol=CLUSTER_TOL,
        )

        cap_sup, kk_sup, _ = numerical_supremum(
            mu, elo, ehi, optical_kmax, quantity="capacity", seed=20260815 + index
        )

        # optical_bound returns bound = 2*weighted/cap_sampled^2.
        twice_weighted = prod["bound"] * prod["capacity"] ** 2
        bound_sup = twice_weighted / cap_sup**2
        ratio_sup = bound_sup / nref

        ne_act, nh_act = active_population(
            mu,
            elo,
            ehi,
            optical_kmax,
            PROD_NR,
            PROD_NMU,
            PROD_NPHI,
        )
        nact = ne_act + nh_act
        active_fraction = nact / nref
        bound_active = bound_sup / nact

        print(
            f"{name:12s} "
            f"{prod['capacity']/1e6:10.6f}  "
            f"{cap_sup/1e6:10.6f}  "
            f"{np.linalg.norm(kk_sup):8.5f}  "
            f"{ratio_sup:9.6f}  "
            f"{active_fraction:9.6f}  "
            f"{bound_active:10.6f}"
        )

        if name == "Eg..0.5eV":
            pair_sup, kk_pair, _ = numerical_supremum(
                mu,
                elo,
                ehi,
                optical_kmax,
                quantity="pair",
                seed=20260855,
            )
            broad_pair_sup = (pair_sup, kk_pair, cap_sup)

    if broad_pair_sup is not None:
        pair_sup, kk_pair, cap_sup = broad_pair_sup
        print("\nBroad-window pairwise diagnostic:")
        print(f"ordinary projected-block sup = {cap_sup:.6f} m/s")
        print(f"ordinary pairwise sup        = {pair_sup:.6f} m/s")
        print(f"|k| at pairwise sup          = {np.linalg.norm(kk_pair):.6f} nm^-1")
        print(
            "bound overstatement from pairwise substitution = "
            f"{((cap_sup / pair_sup) ** 2 - 1.0):.3%}"
        )

    print("\nBroad-window active-rank threshold check (reduced grid):")
    for threshold in (1e-6, 1e-3, 1.0, 1e2, 1e4):
        ne_a, nh_a = active_population(
            mu, EG, 0.50, 1.00, 40, 6, 8, rank_threshold=threshold
        )
        print(
            f"rank threshold={threshold:8.1e} m/s  "
            f"nact/nref={(ne_a + nh_a) / nref:.9f}"
        )

    ne_dense, nh_dense = active_population(
        mu, EG, 0.50, 1.00, DENSE_NR, DENSE_NMU, DENSE_NPHI
    )
    print("\nDense broad-window support check:")
    print(f"nact/nref = {(ne_dense + nh_dense) / nref:.9f}")


if __name__ == "__main__":
    main()
