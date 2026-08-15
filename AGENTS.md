# AGENTS.md — Research Objective, Recovery, and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active branch:** `experiment-10-room-temperature-lwir-admissibility`

Before material writes, fetch live targets and exact blob SHAs. Preserve failed, corrected, conditional, and negative paths. Do not use novelty or priority language without a dedicated prior-art audit.

## Primary objective

Generate analytical/theoretical photodetector research from simple Gedanken experiments. The target is a defensible theorem, bound, invariant, counterexample, scaling law, or escape condition—not a materials list or a new scalar FOM.

## Hard global scope — ANALYTICAL / THEORETICAL ONLY

Allowed work: first-principles derivations, exact toy models, analytical bounds/no-go theorems, asymptotics, numerical thought experiments, analytical comparisons, and prior-art audits.

Do not make fabrication, measurement, instrumentation, sample procurement, or laboratory optimization the next step.

## Recovery order

1. `AGENTS.md`
2. `agent.md`
3. `experiments/10-room-temperature-lwir-admissibility/CURRENT_STATE.md`
4. `experiments/10-room-temperature-lwir-admissibility/THEOREM_CORE_2026-08-14.md`
5. `experiments/10-room-temperature-lwir-admissibility/JOINT_ADMISSIBILITY_NOVELTY_AUDIT_2026-08-14.md`
6. `experiments/10-room-temperature-lwir-admissibility/GENERAL_SPECTATOR_BAND_ADMISSIBILITY_THEOREM_STEP_2026-08-14.md`
7. `experiments/10-room-temperature-lwir-admissibility/HEAVY_HOLE_AUGER_RATE_AND_JOINT_BOUND_STEP_2026-08-14.md`
8. `experiments/10-room-temperature-lwir-admissibility/THIRD_BAND_HEAVY_HOLE_AUGER_ESCAPE_STEP_2026-08-14.md`
9. `experiments/10-room-temperature-lwir-admissibility/RADIATIVE_BOUNDARY_ADMISSIBILITY_STEP_2026-08-14.md`
10. earlier Experiment-10 derivations only as needed.

Do not infer chronology from `main`; later experiments live on divergent branches.

## Fixed target

```math
T=300\ \mathrm K,
\qquad
\lambda_c=10\ \mu\mathrm m,
\qquad
E_g=0.123984\ \mathrm{eV},
\qquad
E_g/(k_BT)\approx4.796.
```

Research question:

> What electronic structure must a passive LWIR interband absorber possess to approach HgCdTe-class room-temperature intrinsic detector quality without sacrificing useful temporal response?

---

# Closed / controlling results

## A. Active massive-Dirac matched absorptance

For the controlled single-pass active pair,

```math
n_c\propto v^{-3},
\qquad
\alpha_D\propto v^{-1},
\qquad
d\propto v,
```

so in the two-band neutral model

```math
\Sigma_c=C/v^2.
```

When spectator hole bands are added, neutrality shifts `mu>0`, increasing active electron density and reducing active-pair absorption. Therefore the rigorous statement becomes

```math
\boxed{\Sigma_c\ge C/v^2}
```

for the same required active-pair single-pass optical depth.

## B. Microscopic lattice velocity resource

```math
\boxed{v\le V_{hop}.}
```

## C. Symmetric two-band direct Auger

Exact particle-hole-symmetric finite-gap massive-Dirac `eeh/hhe` direct Auger is kinematically closed.

Scalar particle-hole asymmetry reopens the channel with weak-asymmetry threshold

```math
\boxed{K_{th}\sim E_g\mathcal A_m^{-1/3}.}
```

Near an interior threshold, pure kinematic phase space scales as `(K-K_th)^2`; microscopic overlap zeros can add powers.

## D. External optical floor

For radiative/background comparison, match the complete external mode-resolved optical boundary, not useful front-side absorptance alone.

At equilibrium,

```math
\Phi_{abs}^{ext}=\Phi_{em}^{ext}=\Phi_0.
```

Internal radiative recombination is not invariant because photon recycling changes internal event count.

At the ideal 10-um/300-K hemispherical step benchmark:

```text
Phi_0 = 4.89777e17 cm^-2 s^-1
q Phi_0 = 0.0784710 A/cm^2
```

Direct-Auger/radiative activation parity occurs at `K_th=Eg/2`.

## E. General spectator-band Auger ceiling

For positive isotropic convex spectator excitation `E_s(p)`, define

```math
\boxed{
 v_s^{crit}=\inf_{p>0}\frac{E_s(p)}{p}.
}
```

Exact finite-energy normal-momentum spectator-assisted CCCH closure in the continuum model is equivalent to

```math
\boxed{v\le v_s^{crit}.}
```

For multiple spectators,

```math
v_{spec}=\min_s v_s^{crit}.
```

This is mathematically Landau-like; equal-group-velocity impact-ionization threshold theory is classical. Do not claim this kinematic construction as a new principle.

Parabolic heavy-hole corollary:

```math
\boxed{M_{hh}v^2\le2(\Delta+\delta_{hh}).}
```

## F. Strongest current conditional theorem

Define

```math
v_{adm}=\min(V_{hop},v_{spec}).
```

Under the controlled single-pass, active-pair-optically-dominant hypotheses and exact normal-momentum spectator-assisted Auger closure,

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

For one parabolic heavy-hole spectator,

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

This is the current theorem candidate; novelty is not established.

---

# Novelty discipline

Established and unavailable as novelty:

```text
alpha/G_th detector-material optimization;
band-structure Auger suppression in small-gap detectors;
HgCdTe heavy-hole CCCH/Auger-1;
equal-group-velocity impact-ionization thresholds;
Landau min[E(p)/p] critical-velocity construction;
Dirac/quasi-relativistic Auger suppression;
multiband IR superlattice design balancing absorption and Auger;
radiative detailed balance and photon recycling.
```

Focused search did not locate the exact composed carrier-column inequality, but a hostile reviewer could reasonably regard it as an elementary synthesis.

Current disposition:

```text
PROVISIONAL CONDITIONAL THEOREM PACKAGE.
NO DIRECT COLLISION FOUND IN FOCUSED AUDIT.
NOVELTY NOT ESTABLISHED.
NO MANUSCRIPT YET.
```

---

# Hard theorem boundaries

## Optically active spectator bands

If spectator useful absorption is unconstrained, `alpha_D ~ 1/v` no longer fixes physical thickness. The carrier-column theorem requires active-pair optical dominance or an explicit spectator optical-strength bound.

Actual HgCdTe heavy-hole states are optically active; do not present the current theorem as a quantitative bulk-HgCdTe bound.

## Arbitrary photonic path enhancement

The relation `d=zeta/alpha` is single-pass. Resonators, gratings and slow-light structures can reduce physical thickness at fixed external absorptance.

Without a photonic path/dwell-time resource, a universal physical carrier-column floor is not established.

## Exact closure is sufficient, not necessary

Radiative/background-limited performance requires sufficiently small nonradiative traffic, not exact closure of every channel.

---

# DO NOT DO

Do not rank compounds. Do not add another electronic recombination mechanism now. Do not insert phenomenological Auger lifetimes. Do not draft a manuscript before the optical loophole and theorem review are resolved.

# NEXT ACTION

Attack the photonic loophole from the simplest passive temporal coupled-mode model:

> At fixed external absorptance and a specified detector temporal response/bandwidth, what maximum optical path enhancement / photon dwell time is possible? Can a resonator or slow-light structure make the physical active carrier column arbitrarily small, or does finite response restore a generalized lower bound?

Separate elementary resonator algebra from any broad delay-bandwidth/passivity theorem and audit prior art aggressively.