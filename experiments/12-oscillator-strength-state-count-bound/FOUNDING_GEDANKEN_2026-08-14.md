# Experiment 12 — Oscillator-Strength / Thermal-State-Count Bound

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Initial status:** **PROVISIONAL BRANCH — FIRST RESULT SURVIVED FOCUSED COLLISION SCREEN / NOVELTY NOT ESTABLISHED**

## Founding question

Experiment 10 found, for a specific finite-gap massive-Dirac family, that matching useful single-pass absorptance produces a thermal carrier-column scaling

```math
\Sigma_e\propto v^{-2}.
```

But that result was tied to one dispersion family.

Experiment 12 asks a more abstract question:

> At fixed interband optical spectral weight, can an intrinsic semiconductor make its equilibrium free-carrier population arbitrarily small if the microscopic interband velocity operator has a finite norm?

Equivalently:

> Can one obtain arbitrarily large optical oscillator strength from arbitrarily few thermally occupiable conduction/valence states without increasing the microscopic velocity/oscillator-strength resource itself?

The intended result is not another material figure of merit. The target is a state-count inequality that follows from

```text
Fermi occupation + intrinsic charge neutrality +
interband optical matrix elements + operator norm/rank.
```

## Minimal Gedanken system

Start with a finite active volume `V` containing two exactly resonant single-particle manifolds:

```text
valence manifold: dimension N_v, energy E_v;
conduction manifold: dimension N_c, energy E_c;
transition energy: E_gamma = E_c - E_v > 0.
```

All spin, valley, orbital, and finite-volume degeneracies are counted explicitly inside `N_v` and `N_c`.

Assume:

```text
noninteracting quasiparticles;
thermal equilibrium at temperature T;
a common chemical potential mu fixed by intrinsic neutrality;
linear optical response;
no excitons or collective many-body oscillator-strength transfer yet;
one chosen optical polarization i;
a physical velocity operator v_i with finite norm ||v_i|| <= v_max.
```

Let

```math
V_{cv}=P_c\hat v_iP_v
```

be the conduction-valence block of the velocity operator.

The experiment begins by comparing two resources:

```text
thermal state count:
    how many of these states are occupied by equilibrium electrons/holes;

optical state strength:
    how much absorptive spectral weight the same manifolds can carry.
```

## Immediate novelty hazards

Do not claim novelty for:

```text
Kubo-Greenwood optical conductivity;
TRK/f-sum rules;
ordinary alpha/G_th infrared detector figures of merit;
quantum-metric control of interband oscillator strength;
Pauli blocking;
rank/singular-value inequalities by themselves.
```

The only possible contribution would be their specific composition into a thermal-carrier lower bound for an intrinsic interband absorber.

## First target

Derive the tight minimum equilibrium carrier number for a required absorptive velocity-matrix Frobenius weight

```math
S_{abs}=\sum_{cv}(f_v-f_c)|v_{cv}|^2
```

when

```math
\|\hat v_i\|\le v_{max}.
```

Then convert that result to an observable integrated optical conductivity using Kubo-Greenwood.

Do not generalize to arbitrary dispersive/many-body bands until the two-manifold theorem is exact.
