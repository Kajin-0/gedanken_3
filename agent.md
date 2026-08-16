# Agent Handoff — Gedanken 3

**Date:** 2026-08-15  
**Active branch:** `experiment-13-observable-resource-unification`  
**Repository frontier:** **Experiment 13 Rev. 8 — Physical Review Applied flagship; homogeneous full-BIA robustness added; 8-page production and hostile-review pass; human submission inputs remain**

## Read first

1. `experiments/13-observable-resource-unification/00_ACTIVE_FRONTIER_REV8_FLAGSHIP_2026-08-15.md`
2. `experiments/13-observable-resource-unification/PAPER_REV8_BIA_ROBUST_HOSTILE_REVIEW_2026-08-15.md`
3. `experiments/13-observable-resource-unification/REV8_PRAPPLIED_PRODUCTION_QA_2026-08-15.md`
4. `experiments/13-observable-resource-unification/HGCDTE_FULL_HOMOGENEOUS_BIA_ROBUSTNESS_2026-08-15.md`
5. `experiments/13-observable-resource-unification/PRAPPLIED_SUBMISSION_PREFLIGHT_REV8_2026-08-15.md`
6. `experiments/13-observable-resource-unification/CURRENT_STATE.md`

Rev. 7 and earlier are historical checkpoints. Rev. 8 controls.

## Controlling production identity

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
visual QA:            PASS
hostile review:       PASS
```

## Core theorem and hierarchy

Unchanged from Rev. 7. The cross-mu population theorem remains the central result, with the existing thermodynamic uniform-capacity/liminf qualifications.

```math
\frac{n_{bound}}{n_{ref}}
=
\frac{n_{\mathcal B}^{act}}{n_{ref}}
\eta_F
\sum_a w_a^{act}\frac{c_a}{\mathcal S_a^{act}}.
```

## Baseline HgCdTe production values

```text
support fraction       = 0.66897
eta_F                  = 0.30684
tau_cap^act            = 0.57262
tau_bound^act          = 0.17570
full bound/reference   ~= 0.1175
v_B^cap                = 1.01764e6 m/s
```

These remain the Table-I/Fig.-4 baseline.

## Rev. 8 BIA robustness result

A separate symmetry-checked homogeneous effective eight-band model adds `B8v+`, `B8v-`, and complete `C_k` bulk couplings.

At the present composition:

```text
B8v+ = -0.2026 eV nm^2
B8v- = +0.00706 eV nm^2
C_k  = -0.00654 eV nm
```

Refined results:

```text
BIA off:  capacity 1.01764e6 m/s; full ratio 0.11747; 20072 dim-2 active blocks; S_a=1
BIA on:   capacity 1.02203e6 m/s; full ratio 0.11651; 40452 dim-1 active blocks; S_a=1
```

Relative:

```text
capacity +0.43%
full ratio -0.82%
within-shell factor unchanged at 1
```

Key mechanism: generic BIA splitting makes the sampled active exact parents one-dimensional, so a nonzero block has one singular value and `rank = stable rank = 1`.

Implementation QA and multi-seed/grid/cluster robustness all pass. The 26.6-meV number is only an adjacent-pair separation diagnostic, not a theorem input.

Scope: homogeneous effective eight-band BIA only; not atomistic/interface complete and not universal for exceptional multidimensional exact degeneracies.

## Publication architecture — mandatory

```text
Experiment 13 Rev. 8:     SOLE PRIMARY ACTIVE SUBMISSION MANUSCRIPT
Experiment 12 manuscript: FROZEN FALLBACK / DEVELOPMENT PROVENANCE
Experiment 01 manuscript: FROZEN FALLBACK
Experiment 09 manuscript: FROZEN FALLBACK
concurrent overlapping submission: DO NOT DO
```

## Stop rule

Do not create Rev. 9 or reopen science by default. The current technical loop is closed.

Human/submission inputs only:

```text
author name;
affiliation;
corresponding email;
acknowledgments/funding;
conflicts/disclosures as applicable;
truthful submission-history declaration;
final Data Availability / persistent-archive decision;
optional ORCID/referee recommendations/exclusions.
```

After insertion, rebuild through Rev. 8 CI, record hashes, inspect every page, and verify submitted source reproduces submitted PDF.
