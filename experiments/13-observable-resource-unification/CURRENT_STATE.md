# Current State — Experiment 13: Stage-Specific Spectral Geometry of Photodetection

**Date:** 2026-08-15  
**Scope:** analytical/theoretical only  
**Target:** Physical Review Applied — Regular Article  
**Status:** **REV. 8 CONTROLS / FULL HOMOGENEOUS BIA ROBUSTNESS ADDED / 8-PAGE PRODUCTION QA PASS / HOSTILE REVIEW PASS / HUMAN SUBMISSION INPUTS REMAIN**

## Read first

1. `00_ACTIVE_FRONTIER_REV8_FLAGSHIP_2026-08-15.md`
2. `PAPER_REV8_BIA_ROBUST_HOSTILE_REVIEW_2026-08-15.md`
3. `REV8_PRAPPLIED_PRODUCTION_QA_2026-08-15.md`
4. `HGCDTE_FULL_HOMOGENEOUS_BIA_ROBUSTNESS_2026-08-15.md`
5. `PRAPPLIED_SUBMISSION_PREFLIGHT_REV8_2026-08-15.md`

Earlier revisions are reproducible development history. Rev. 8 controls for submission.

## Controlling identity

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
hostile review:       PASS
```

## Central theorem — unchanged

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

Finite-system exact; macroscopic interpretation retains the Rev. 7 uniform-capacity and liminf qualifications.

## Full tightness hierarchy — unchanged

```math
\frac{n_{bound}}{n_{ref}}
=
\frac{n_{\mathcal B}^{act}}{n_{ref}}
\eta_F
\sum_a w_a^{act}\frac{c_a}{\mathcal S_a^{act}}.
```

Support coverage remains reference-domain dependent; `eta_F` is Fermi-statistical; optical bound tightness is `tau_bound^act`.

## Baseline HgCdTe production closure

```text
support fraction       = 0.66897
eta_F                  = 0.30684
tau_cap^act            = 0.57262
tau_bound^act          = 0.17570
full bound/reference   ~= 0.1175
v_B^cap                = 1.01764e6 m/s
```

## New Rev. 8 homogeneous BIA result

The separate homogeneous effective eight-band stress model includes `B8v+`, `B8v-`, and complete `C_k` bulk couplings. At the present composition the interpolated effective values used are

```text
B8v+ = -0.2026 eV nm^2
B8v- = +0.00706 eV nm^2
C_k  = -0.00654 eV nm
```

Refined results:

```text
BIA off:
capacity              = 1.01764e6 m/s
full ratio            = 0.11747
active exact blocks   = 20072 dimension-2
S_a                   = 1 throughout sampled active support

homogeneous BIA:
capacity              = 1.02203e6 m/s
full ratio            = 0.11651
active exact blocks   = 40452 dimension-1
S_a                   = 1 throughout sampled active support
```

Relative changes:

```text
capacity              ~= +0.43%
full bound/reference  ~= -0.82%
within-shell factor   = unchanged at 1
```

The structural mechanism is exact for the sampled one-dimensional active parents: one nonzero singular value implies rank = stable rank = 1.

Hard implementation QA, multi-seed capacity search, independent grids, and clustering-tolerance sweeps all pass. The 26.6-meV value is only an adjacent-pair separation diagnostic over selected-support points; it is not used by the theorem or hierarchy.

Scope limitation: homogeneous effective eight-band BIA only; no atomistic/interface model or universal claim for exceptional multidimensional exact degeneracies.

## Publication architecture

```text
Experiment 13 Rev. 8:     SOLE PRIMARY ACTIVE SUBMISSION MANUSCRIPT
Experiment 12 manuscript: FROZEN FALLBACK / DEVELOPMENT PROVENANCE
Experiment 01 manuscript: FROZEN FALLBACK
Experiment 09 manuscript: FROZEN FALLBACK
concurrent overlapping submission: DO NOT DO
```

## Final review disposition

```text
central theorem:                      PASS / UNCHANGED
full tightness hierarchy:             PASS / UNCHANGED
baseline HgCdTe validation:           PASS / UNCHANGED
homogeneous BIA implementation:       PASS
BIA exact-shell result:               PASS
BIA capacity/grid/seed/cluster QA:    PASS
BIA claim scope:                      PASS
recycling/Ramo result:                PASS / UNCHANGED
production PDF:                       PASS
Rev. 9 required:                      NO
```

## Stop rule

Do not create Rev. 9 by default. Reopen science only for a concrete external criticism, mathematical counterexample, numerical inconsistency, or direct prior-art collision.

Remaining work is human metadata, submission-history declaration, and Data Availability/persistent-archive decisions. After those are supplied, make metadata-only edits, rebuild through Rev. 8 CI, record final hashes, and inspect every final page.
