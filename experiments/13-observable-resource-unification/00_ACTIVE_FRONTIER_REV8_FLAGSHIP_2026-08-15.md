# Active Frontier — Experiment 13 unified flagship Rev. 8

**Date:** 2026-08-15  
**Branch:** `experiment-13-observable-resource-unification`  
**Target:** Physical Review Applied — Regular Article  
**Status:** **REV. 8 CONTROLS / FULL HOMOGENEOUS BIA ROBUSTNESS ADDED / 8-PAGE PRODUCTION QA PASS / HOSTILE REVIEW PASS / HUMAN SUBMISSION INPUTS REMAIN**

This file supersedes earlier Experiment-13 frontier files whenever they disagree with it.

## Read first

1. `PAPER_REV8_BIA_ROBUST_HOSTILE_REVIEW_2026-08-15.md`
2. `REV8_PRAPPLIED_PRODUCTION_QA_2026-08-15.md`
3. `HGCDTE_FULL_HOMOGENEOUS_BIA_ROBUSTNESS_2026-08-15.md`
4. `HGCDTE_FULL_BIA_SPLITTING_DIAGNOSTIC_CLARIFICATION_2026-08-15.md`
5. `CURRENT_STATE.md`
6. `PRAPPLIED_SUBMISSION_PREFLIGHT_REV8_2026-08-15.md` once created

## Controlling manuscript identity

```text
Actions run:          31916728949
source commit:        813fd8a2fc3011ef6e3ba63a0567cb3eee30297b
artifact ID:          9255118533
artifact digest:      a5d7aac0a5f3a68783a3510c9c2e8632af3e5b4e34f326e3012dd1aa6316bfcd
PDF SHA-256:          309655aec80a7778428beedad4c95b53b27b8ebae24143310b1f4fdc1c6faf87
TeX SHA-256:          08efd63da8e5558a07bbc5a4bc9be8667811bf2314705c69f257e30b9b565973
pages:                8
undefined refs/cites: none
overfull/underfull:   none
all-page visual QA:   PASS
hostile scientific review: PASS
```

## Central theorem

Unchanged:

```math
\boxed{
 n_e+n_h
 \ge n_{e,\mathcal B}^{act}+n_{h,\mathcal B}^{act}
 \ge
 \frac{2}{\pi e^2(v_{\mathcal B}^{cap})^2}
 \int_{\mathcal B}
 \frac{\hbar\omega\sigma_1^{cross}(\omega)}
 {e^{\hbar\omega/(2k_BT)}-1}d\omega.
}
```

Finite-system exact; macroscopic density requires the existing uniform-capacity/liminf conditions.

## Full tightness hierarchy

Unchanged:

```math
\frac{n_{bound}}{n_{ref}}
=
\frac{n_{\mathcal B}^{act}}{n_{ref}}
\eta_F
\sum_a w_a^{act}\frac{c_a}{\mathcal S_a^{act}}.
```

The BIA robustness calculation directly stress-tests the within-shell factor and the redistribution among the other factors.

## Baseline HgCdTe production result

Still controls Table I / Fig. 4:

```text
support fraction       = 0.66897
eta_F                  = 0.30684
tau_cap^act            = 0.57262
tau_bound^act          = 0.17570
full bound/reference   ~= 0.1175
v_B^cap                = 1.01764e6 m/s
```

## New Rev. 8 homogeneous BIA stress result

The symmetry-checked homogeneous effective eight-band model includes `B8v+`, `B8v-`, and complete `C_k` bulk couplings with interpolated effective parameters

```text
B8v+ = -0.2026 eV nm^2
B8v- = +0.00706 eV nm^2
C_k  = -0.00654 eV nm
```

at the present composition.

Refined comparison:

```text
BIA off:
capacity              = 1.01764e6 m/s
full ratio            = 0.11747
active blocks         = 20072 dimension-2
S_a                   = 1 for every sampled active block

homogeneous BIA:
capacity              = 1.02203e6 m/s
full ratio            = 0.11651
active blocks         = 40452 dimension-1
S_a                   = 1 for every sampled active block
```

Relative full-BIA change:

```text
capacity              ~= +0.43%
full ratio            ~= -0.82%
within-shell factor   = unchanged at 1
```

Mechanism:

```text
BIA breaks the generic fixed-k PT doublet
-> exact active parent becomes one-dimensional
-> one nonzero singular value
-> rank = stable rank = 1
-> S_a^act = 1.
```

The BIA correction therefore migrates into support, Fermi weighting, and absolute capacity rather than creating a new within-exact-shell singular-concentration penalty in this model.

Limitations are explicit: homogeneous effective eight-band model only; no atomistic/interface inversion asymmetry; no universal claim for exceptional multidimensional exact degeneracies; no BIA-parameter uncertainty propagation.

## Robustness / QA

Full-BIA implementation passes parent-Kane phase-convention reproduction, Hermiticity, spinful time reversal, T-odd velocity, Gamma-zero BIA, analytic velocity derivative, and C-term reduction checks.

The continuous BIA capacity is stable over four optimizer seeds to approximately `1.4e-8` fractional spread. Independent grids keep the full-ratio change near or below one percent. Exact-shell clustering tolerance `1e-9` through `1e-5 eV` leaves every sampled active BIA shell one-dimensional with `S_a=1`.

The reported 26.6-meV quantity is only an adjacent-pair separation diagnostic over selected-support points and is not used by the theorem or hierarchy.

## Publication architecture

```text
Experiment 13 Rev. 8:     SOLE PRIMARY ACTIVE SUBMISSION MANUSCRIPT
Experiment 12 manuscript: FROZEN FALLBACK / DEVELOPMENT PROVENANCE
Experiment 01 manuscript: FROZEN FALLBACK
Experiment 09 manuscript: FROZEN FALLBACK
concurrent overlapping submission: DO NOT DO
```

## Stop rule

**Do not create Rev. 9 by default.**

The current technical loop is closed. Reopen science only for a concrete external referee/editor criticism, mathematical counterexample, numerical inconsistency, or direct prior-art collision.

Remaining work is human/submission metadata and final Data Availability/archive decisions.
