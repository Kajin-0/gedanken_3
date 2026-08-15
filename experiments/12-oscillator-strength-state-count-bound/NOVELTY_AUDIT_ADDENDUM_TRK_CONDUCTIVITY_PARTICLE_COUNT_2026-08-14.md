# Experiment 12 — Novelty audit addendum: conductivity-to-particle-count precedents

**Date:** 2026-08-14  
**Disposition:** **ADJACENT PRECEDENT FOUND / NO DIRECT COLLISION / PRIORITY NOT ESTABLISHED**

## Why this addendum was needed

Experiment 12 derives an inverse optical-statistical inequality: surviving low-energy cross-chemical-potential optical spectral weight, together with a finite selected optical-velocity resource, imposes a minimum equilibrium thermal electron-hole excitation population.

A hostile novelty question is broader:

> Has optical or electrical conductivity already been integrated to infer an electronic particle count?

The answer is yes. That broader concept is established and must not be presented as new.

## Warm-dense-matter comparator

Mandy Bethkenhagen et al.,

**“Carbon ionization at gigabar pressures: An ab initio perspective on astrophysical high-density plasmas,”**
*Physical Review Research* **2**, 023260 (2020), DOI `10.1103/PhysRevResearch.2.023260`.

The paper calculates ionization degree directly from the dynamic electrical conductivity using the Thomas–Reiche–Kuhn (TRK) sum rule.

Thus the broad mapping

```text
conductivity spectral weight -> electronic particle count
```

is not itself a novelty basis for Experiment 12.

## Why it is not a direct collision

The Bethkenhagen et al. construction and Experiment 12 constrain different quantities with different response moments.

### TRK / conventional sum-rule direction

The TRK conductivity sum constrains an electron count through a conventional integrated oscillator-strength rule. Its particle count is associated with ionization/free-electron content in a warm dense plasma.

### Experiment-12 direction

Experiment 12 restricts the response to direct one-body transitions crossing the chemical potential and uses the finite-temperature kernel

```math
K_T(E)=\frac{E}{e^{E/(2k_BT)}-1}.
```

The resulting hierarchy is

```math
\frac{2}{\pi e^2(v_B^{cap})^2}
\int_B
K_T(\hbar\omega)\sigma_1^{cross}(\omega)d\omega
\le
n_{e,B}^{act}+n_{h,B}^{act}
\le n_e+n_h,
```

where `v_B^{cap}` is a per-energy-shell selected optical-velocity capacity and `n^{act}` counts thermally occupied optical support dimensions.

The right-hand population is the finite-temperature electron-hole excitation population relative to the chemical-potential split, not a TRK all-electron or plasma-ionization count.

## Focused final search

Primary-source searches were also run for combinations of:

```text
finite-temperature optical conductivity;
thermal carrier population;
minimum carrier density;
phase-space filling;
optical spectral weight;
cross-Fermi / cross-chemical-potential transitions;
thermal-kernel inequalities;
carrier-density / gain thresholds.
```

No source was identified that states the same inverse windowed inequality with the kernel

```math
E/[e^{E/(2k_BT)}-1]
```

and a per-shell optical matrix-strength/state-count resource.

This is an absence-of-collision result, not proof of priority.

## Updated novelty position

The manuscript must not claim novelty for any of the individual ingredients:

```text
conductivity-based particle counting;
Kubo-Greenwood response;
Pauli blocking / phase-space filling;
TRK / f-sum rules;
operator-norm or rank inequalities;
low-carrier band-structure engineering.
```

The only plausible contribution is the **specific composed inverse theorem**:

```text
finite surviving cross-mu optical spectral weight
+ finite per-shell optical-velocity capacity
-> minimum equilibrium thermal optical-support population
-> minimum total thermal electron-hole population.
```

Final audit status:

```text
DIRECT PRIOR-ART COLLISION: NOT FOUND
PRIORITY: NOT ESTABLISHED
NOVELTY RISK: HIGH BECAUSE THE PROOF IS ELEMENTARY
MANUSCRIPT MAY PROCEED ONLY WITH CONSERVATIVE CLAIM LANGUAGE
```