# Experiment 07 — Novelty / Dominance Stop

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Disposition:** CLOSE AS DEFAULT RESEARCH-NOVELTY PATH / RETAIN DERIVED IDENTITIES AS TECHNICAL NOTES / DO NOT DRAFT PAPER

## 1. Original question

Could isotopic mass engineering of HgCdTe reveal or strongly alter mercury-vacancy Shockley–Read–Hall capture by shifting the phonon spectrum while leaving the electronic chemistry nearly unchanged?

The branch evolved through several forms:

1. macroscopic phononic-crystal suppression of SRH — rejected because relevant HgCdTe lattice modes are THz/atomic-scale;
2. heavy-isotope dark-current engineering — rejected as non-robust once realistic isotope shifts, bypass channels and spectral broadening were included;
3. isotope spectroscopy of the one-optical-phonon `V_Hg` channel — retained temporarily;
4. full analytical isotope-response theory — developed in the files listed below.

## 2. HgCdTe-specific primary-theory anchor

Kozlov et al. (JETP 2024) calculate electron and hole capture on mercury-vacancy states in narrow-gap HgCdTe with band gaps around 35–40 meV by single optical phonon emission.

For electron capture to the `A2^-1` level approximately `E2=20 meV` above the valence-band edge, the energy-selection coordinate is

```math
\boxed{K=\hbar\omega_{LO}-(E_g-E_2).}
```

The paper explicitly states that electron capture is about three orders of magnitude slower than hole capture in the studied case, so the SRH relaxation time is controlled by electron capture.

It includes both HgTe-like and CdTe-like optical phonon branches.

The 2026 follow-on quantum-well paper likewise states that electron capture substantially exceeds hole capture time and governs SRH, as in bulk material.

## 3. Correct analytical results obtained in Experiment 07

### A. Serial/parallel isotope-control theorem

For a sequential cycle with step rates `r_i` and waiting times `tau_i=1/r_i`,

```math
R_{cyc}=\frac1{\sum_i\tau_i},
```

and

```math
\boxed{
S_R=\sum_i\frac{\tau_i}{\sum_j\tau_j}S_{r_i}.
}
```

If each step contains parallel channels, the complete isotope sensitivity is a convex combination of microscopic channel sensitivities.

This is mathematically correct but belongs to established rate-control / reaction-network structure.

### B. Standard-SRH isotope decomposition

For ordinary SRH recombination, capture-kinetic isotope sensitivity enters as a weighted combination of `S_Cn` and `S_Cp`, while defect concentration and electronic thermodynamics (`E_g`, trap level, densities of states) contribute independent isotope sectors.

Therefore a total dark-current isotope coefficient cannot uniquely identify isotope-sensitive capture.

### C. Finite-broadening threshold regularization

For an onset

```math
F_0(\Delta)\sim\Delta^\beta\Theta(\Delta)
```

convolved with Gaussian width `sigma`,

```math
\left.
\frac{\partial\ln F_\sigma}{\partial\Delta}
\right|_0
=\frac{\sqrt2\Gamma[(\beta+2)/2]}
{\Gamma[(\beta+1)/2]}\frac1\sigma.
```

Thus finite spectral width replaces formal threshold divergence by the dimensionless ratio `deltaDelta/sigma`.

### D. Corrected one-phonon mass sensitivity

The earlier toy model omitted quantized matrix-element and Bose-factor isotope dependence.

For

```math
C\propto\omega^p(N_\omega+1)\Delta^\beta e^{-\Delta/kT}
```

and pure phonon mass scaling,

```math
\boxed{
S_C=\alpha\left[-p+x(N_\omega+1)-\beta\frac{\hbar\omega}{\Delta}\right].
}
```

The sign crossing is

```math
\Delta_\times=\frac{\beta\hbar\omega}{x(N_\omega+1)-p}.
```

The former `beta=1/2` sign-reversal conclusion is therefore model-dependent.

### E. General Laplace/cumulant closure

For a positive capture kernel

```math
C(\beta)=A(N+1)\int_0^\infty\Phi(E)e^{-\beta E}dE,
```

```math
\frac{d}{d\beta}\ln\frac{C}{N+1}=-\langle E\rangle_\beta,
```

```math
\frac{d^2}{d\beta^2}\ln\frac{C}{N+1}=\operatorname{Var}_\beta(E)\ge0.
```

This is an exact Laplace-transform/cumulant identity, not new capture physics.

### F. Isotope-mode rank closure

If isotope dependence enters only through `m` mode coordinates,

```math
\mathbf S=A\mathbf K.
```

The elemental isotope-response vector lies in the mode-participation column space.

For ideal HgTe-like and CdTe-like coordinates,

```math
\boxed{
S_{Te}=\frac{M_{Hg}}{M_{Te}}S_{Hg}
+\frac{M_{Cd}}{M_{Te}}S_{Cd}.
}
```

This remains true for arbitrary threshold functions and arbitrary serial/parallel SRH topology, provided the two-mode mass-only assumption holds.

The generic result is a chain-rule / partial-isotope-coefficient identity, not a standalone novelty claim.

### G. Bandgap–isotope differential equivalence and multibranch no-go

For one phonon branch,

```math
\Delta=\hbar\omega-E_g+E_2.
```

An isotope phonon shift is detuning-equivalent to

```math
\delta E_{g,eq}=-\delta(\hbar\omega)
```

when electronic energies are held fixed.

However with two independent HgTe-like and CdTe-like branches, `E_g` shifts both detunings while elemental cation isotope masses shift different branches. Therefore the total `C_n(E_g)` slope cannot uniquely determine an elemental isotope coefficient unless one branch dominates or branch-resolved capture contributions are known.

This removes the hoped-for parameter-free prediction from the published total composition/bandgap curve alone.

### H. Phonon-edge exponent correction

For coupling-weighted phonon edge density `J_ph(u)~u^eta` and 3-D conduction-electron DOS,

```math
F(\Delta)\sim\Delta^{\eta+3/2}.
```

Therefore the dispersionless `sqrt(Delta)` threshold law is not universal.

For a continuous branch edge with `beta>=1`, the reduced model has no 77-K isotope sign reversal inside the `0-5 meV` electron kinetic window emphasized by the 2024 HgCdTe calculation.

### I. Defect-population isotope sector

For harmonic defect formation,

```math
S_{N_V,a}
=\frac{\beta}{2}\Delta\left[\sum_\nu p_{\nu a}U_\nu\right].
```

The leading classical mass dependence cancels for a consistently balanced formation reaction; equilibrium defect isotope effects arise from quantum vibrational terms.

Thus the total SRH isotope coefficient differs between quenched and annealed defect ensembles:

```math
S_{SRH}^{quenched}\simeq S_{C_n},
```

```math
S_{SRH}^{annealed}\simeq S_{C_n}+S_{N_V}.
```

Again this is established finite-temperature defect thermodynamics applied to the HgCdTe problem.

## 4. Strong prior-art / comparator audit

The following established bodies of theory dominate the generic novelty claims:

1. first-principles nonradiative carrier capture via electron-phonon coupling and multiphonon emission;
2. modern all-mode capture theory and phonon-frequency renormalization across defect charge states;
3. direct semiconductor isotope control of nonradiative defect lifetime, including the 2026 silicon T-center work showing a >5x isotope lifetime effect through a shifted local vibrational mode;
4. partial isotope coefficients and isotope sum rules in multicomponent electron-phonon systems;
5. flux/control summation theorems for multistep reaction networks;
6. harmonic and anharmonic vibrational contributions to finite-temperature point-defect formation free energies;
7. the existing Kozlov et al. HgCdTe mercury-vacancy single-optical-phonon capture calculation itself.

No exact HgCdTe isotope-capture calculation was located in the targeted search. That absence is not enough to rescue a strong theory claim because the proposed extension is straightforward once the established HgCdTe capture kernel and established isotope-mass machinery are combined.

## 5. Adversarial reviewer disposition

A skeptical reviewer could fairly summarize the project as:

> The manuscript differentiates an existing HgCdTe mercury-vacancy capture model with respect to isotope mass and derives several generic sensitivity identities. The isotope perturbation may be physically interesting, but the principal mathematical tools are standard and the underlying nonradiative/isotope mechanism is established. Without a genuinely new microscopic prediction from a full branch-resolved HgCdTe calculation or a new theorem not reducible to chain-rule/control/Laplace identities, the advance is incremental.

That criticism is currently correct.

## 6. Stop decision

```text
HgCdTe isotope effect as broad dark-current engineering mechanism: CLOSED
HgCdTe isotope-SRH analytical branch as major novelty path: CLOSED BY DEFAULT
mathematical identities derived here: RETAIN
HgCdTe-specific energy bookkeeping corrections: RETAIN
full isotope perturbation of the existing Kozlov numerical capture model: POSSIBLE CALCULATION, BUT NOT STRONG ENOUGH BY ITSELF TO JUSTIFY CONTINUED FRONTIER STATUS
paper drafting: DO NOT BEGIN
```

Reopen Experiment 07 only if a new theoretical ingredient appears that is not already contained in established isotope-sensitive nonradiative-capture theory—for example a genuinely new invariant with measurable consequences that survives multimode electronic renormalization and is not a chain-rule identity.

## 7. Files to retain as controlling theory notes

Read:

1. `00_THEORETICAL_ONLY_SCOPE_2026-08-14.md`
2. `00_NOVELTY_STOP_2026-08-14.md`
3. `THEORETICAL_ISOTOPE_CONTROL_SUM_RULE_2026-08-14.md`
4. `ONE_PHONON_MASS_SENSITIVITY_AND_LAPLACE_CLOSURE_2026-08-14.md`
5. `ISOTOPE_MODE_RANK_CLOSURE_2026-08-14.md`
6. `BANDGAP_ISOTOPE_DIFFERENTIAL_EQUIVALENCE_2026-08-14.md`
7. `PHONON_EDGE_EXPONENT_AND_ISOTOPE_SIGN_2026-08-14.md`
8. `DEFECT_POPULATION_ISOTOPE_SECTOR_2026-08-14.md`

Older experimental-feasibility and metrology files remain archived history only and must not be resumed under the user's theory-only constraint.

## 8. Next research rule

Do not rescue Experiment 07 by simply adding more isotope parameters or recreating the published HgCdTe numerical capture calculation.

Return to premise generation. Screen the next theoretical photodetector Gedanken experiment against its strongest existing theorem or architecture before developing it.
