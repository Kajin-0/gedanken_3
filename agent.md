# Agent recovery entrypoint

Read `AGENTS.md` first, then this file. Do not infer chronology from `main` alone.

## Hard scope

Experiment 10 is analytical/theoretical only. Preserve negative/corrected/conditional paths. Do not use novelty or priority language without a dedicated audit.

# ACTIVE FRONTIER — Experiment 10

Branch:

```text
experiment-10-room-temperature-lwir-admissibility
```

No manuscript is justified yet.

## Read in this order

1. `experiments/10-room-temperature-lwir-admissibility/CURRENT_STATE.md`
2. `experiments/10-room-temperature-lwir-admissibility/THEOREM_CORE_2026-08-14.md`
3. `experiments/10-room-temperature-lwir-admissibility/JOINT_ADMISSIBILITY_NOVELTY_AUDIT_2026-08-14.md`
4. `experiments/10-room-temperature-lwir-admissibility/GENERAL_SPECTATOR_BAND_ADMISSIBILITY_THEOREM_STEP_2026-08-14.md`
5. `experiments/10-room-temperature-lwir-admissibility/HEAVY_HOLE_AUGER_RATE_AND_JOINT_BOUND_STEP_2026-08-14.md`
6. `experiments/10-room-temperature-lwir-admissibility/THIRD_BAND_HEAVY_HOLE_AUGER_ESCAPE_STEP_2026-08-14.md`
7. `experiments/10-room-temperature-lwir-admissibility/RADIATIVE_BOUNDARY_ADMISSIBILITY_STEP_2026-08-14.md`
8. earlier Experiment-10 derivations only as needed.

Fixed target:

```math
T=300\ \mathrm K,
\qquad
\lambda_c=10\ \mu\mathrm m,
\qquad
E_g=0.1239841984\ \mathrm{eV},
\qquad
E_g/(k_BT)\approx4.796.
```

---

# Current theorem package

## Active-pair single-pass lower bound

For the finite-gap massive-Dirac active pair, at fixed required active-pair optical depth,

```math
\boxed{\Sigma_c\ge C/v^2.}
```

The equality holds in the two-band `mu=0` model; spectator hole states shift `mu>0`, increase active electron density and reduce active interband Pauli factor, so the relation becomes a lower bound.

Standard witness:

```math
C=1.06668\times10^{29}\ \mathrm{m^{-2}(m/s)^2}.
```

## Lattice ceiling

```math
\boxed{v\le V_{hop}.}
```

## General spectator-band closure ceiling

For positive isotropic convex spectator hole excitation `E_s(p)`,

```math
\boxed{
 v_s^{crit}=\inf_{p>0}E_s(p)/p.
}
```

Exact finite-energy normal-momentum spectator-assisted CCCH closure is equivalent to

```math
\boxed{v\le v_s^{crit}.}
```

For multiple spectators,

```math
v_{spec}=\min_s v_s^{crit}.
```

This is mathematically Landau-like and uses classical equal-group-velocity impact-ionization threshold physics. Do not claim the kinematic construction as novel.

Parabolic heavy-hole corollary:

```math
\boxed{M_{hh}v^2\le2(\Delta+\delta_{hh}).}
```

## Strongest current conditional detector bound

Define

```math
v_{adm}=\min(V_{hop},v_{spec}).
```

Then under the controlled **single-pass, active-pair-optically-dominant** hypotheses,

```math
\boxed{
\Sigma_c
\ge
\frac{C}{v_{adm}^2}
=
\max\!\left[
C/V_{hop}^2,
\max_s C/(v_s^{crit})^2
\right].
}
```

Parabolic heavy-hole version:

```math
\boxed{
\Sigma_c
\ge
\max\!\left[
C/V_{hop}^2,
C M_{hh}/(2(\Delta+\delta_{hh}))
\right].
}
```

---

# Critical limitations

## Spectator optical absorption

If spectator bands have unconstrained useful optical strength,

```math
\alpha_{tot}=\alpha_D+\alpha_s,
```

the active-pair `C/v^2` physical-thickness bound is not universal.

If `alpha_s <= chi_opt alpha_D`, only

```math
\Sigma_c\ge C/[(1+\chi_{opt})v_{adm}^2]
```

follows.

Actual HgCdTe heavy-hole states are optically active, so the current theorem is not a quantitative bulk-HgCdTe bound.

## Arbitrary photonic path enhancement

The relation `d=zeta/alpha` is single-pass. Resonant cavities, gratings, slow-light structures, etc. can reduce physical absorber thickness at fixed external absorptance.

This is currently the largest escape from the physical carrier-column theorem.

## Exact closure is sufficient, not necessary

A detector can remain radiative/background limited with a finite but small Auger rate. Do not confuse exact-closure admissibility with the globally optimal material.

---

# Novelty boundary

Established prior art includes:

```text
alpha/G_th detector-material optimization;
small-gap band-structure Auger suppression;
HgCdTe heavy-hole CCCH;
equal-group-velocity impact-ionization thresholds;
Landau min E/p critical-velocity construction;
Dirac/quasi-relativistic Auger suppression;
IR superlattice design balancing absorption and Auger;
radiative detailed balance and photon recycling.
```

Focused search did not locate the exact composed carrier-column inequality, but it may be judged an elementary synthesis.

Current disposition:

```text
PROVISIONAL CONDITIONAL THEOREM PACKAGE.
NOVELTY NOT ESTABLISHED.
NO MANUSCRIPT YET.
```

# NEXT ACTION

Do not add another electronic recombination mechanism.

Attack the optical loophole:

> For a passive absorber with specified external absorptance and finite detector temporal response/bandwidth, derive the maximum permissible optical path enhancement / photon dwell time. Determine whether resonant or slow-light enhancement can make physical active carrier column arbitrarily small, or whether finite response restores a generalized lower bound.

Start with the simplest one-port resonator / temporal coupled-mode model. Separate an elementary cavity result from any broader passive delay-bandwidth theorem. Aggressively audit prior art before treating any tradeoff as novel.