# Agent Handoff — Gedanken 3

**Date:** 2026-08-15  
**Active branch:** `experiment-13-observable-resource-unification`  
**Repository-wide frontier:** **Experiment 13 unified flagship Rev. 4 — science frozen; seven-page Physical Review Applied production PDF QA-passed; human metadata required**

## Read first

1. `experiments/13-observable-resource-unification/00_ACTIVE_FRONTIER_REV4_FLAGSHIP_2026-08-15.md`
2. `experiments/13-observable-resource-unification/REV4_PRAPPLIED_PRODUCTION_QA_2026-08-15.md`
3. `experiments/13-observable-resource-unification/PAPER_REV4_RENDERED_HOSTILE_REVIEW_2026-08-15.md`
4. `experiments/13-observable-resource-unification/PAPER_DRAFT_REV4_CLAIM_REFERENCE_CLEAN_2026-08-15.md`
5. `experiments/13-observable-resource-unification/PAPER_REV4_REFERENCE_QA_2026-08-15.md`
6. `experiments/13-observable-resource-unification/PAPER_REV4_FINAL_HOSTILE_CLAIM_REFERENCE_REVIEW_2026-08-15.md`
7. `experiments/13-observable-resource-unification/HGCDTE_STABLE_RANK_PRODUCTION_QA_2026-08-15.md`
8. `experiments/13-observable-resource-unification/HGCDTE_PT_SYMMETRY_STABLE_RANK_EXPLANATION_2026-08-15.md`

If these conflict with older notes, this order controls.

## Strategic state

```text
SCIENTIFIC CONTENT FREEZE:       PASS / ACTIVE
FLAGSHIP-FIRST STRATEGY:         ACTIVE
TARGET:                          Physical Review Applied Regular Article
PRODUCTION PDF:                  PASS
ALL-PAGE VISUAL QA:              PASS
RENDERED HOSTILE REVIEW:         PASS
NEW THEORY BY DEFAULT:           STOP
REMAINING BLOCKER:               HUMAN METADATA ONLY
```

Frozen fallback manuscripts remain:

```text
Experiment 01 — Applied Optics
Experiment 09 — PRA
Experiment 12 — PRB
```

Preserve them. Do not simultaneously submit materially overlapping standalone and flagship versions.

## Controlling production identity

```text
GitHub Actions run:   31900965632
head commit:          f41bdc6a4e580bfadd8155903f4127b2b63655ca
artifact ID:          9251078733
artifact digest:      1b4375f9953707ddf1e6b35bf55f91377370274d230298429398096f1b42e01a
PDF SHA-256:          84c86c30019a0517246493ad4b9aacd60ac54051164b27ca7dfedac2fdba800f
built TeX SHA-256:    c1459c18e4bf5d20f09a9a956c23b565c76bd0a913fe9636adc2ca7fe1e2b8f9
pages:                7
undefined refs/cites: none
overfull boxes:       none
```

All seven rendered pages were inspected directly. Every theorem section and all five figures are present, legible, and unclipped.

## Central theorem

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

Use selected direct cross-`mu` conductivity, not arbitrary total measured conductivity. This is an equilibrium one-body endpoint-population theorem, not a universal dark-current, generation-rate, noise, or `D*` theorem.

## Unified connector

For a physically declared admissible domain,

```math
\boxed{\mathcal S_{X|D}\tau_{X|D}=1.}
```

This is organizing algebra, not the novelty headline.

Important specializations:

```text
uniform task ensemble:      S=d/r_st
rank-one coherent detector: S=N_eff=1/sum_j w_j^2
thermal endpoint ensemble:  S_th,B^act=1/tau_cap^act
```

Shell-resolved thermal decomposition:

```math
\tau_{cap}^{act}=\sum_aw_a^{act}\frac{c_a}{\mathcal S_a^{act}},
```

```math
\tau_{obs}^{act}=\eta_F\sum_aw_a^{act}\frac{c_a}{\mathcal S_a^{act}}.
```

## Production HgCdTe result

```text
mu                            = 0.1354615106 eV
n_ref                         = 1.005140525e17 cm^-3
R_B                           = 3.987420232e28 cm^-3 (m/s)^2
L_B                           = 1.223486457e28 cm^-3 (m/s)^2
n_B^act                       = 6.724111444e16 cm^-3
v_B^cap                       = 1.01764e6 m/s
eta_F                         = 0.306836598
tau_cap^act                   = 0.572622972
tau_obs^act                   = 0.175701685
S_th,B^act                    ~= 1.746
bound/reference               ~= 0.118
bound/active                  ~= 0.176
```

```math
0.306836598\times0.572622972=0.175701685.
```

Selected active exact-shell blocks have `S_a^act=1` to about `4e-14` **only in the BIA-neglecting second-order Kane validation model**. Do not universalize that equality to real zincblende HgCdTe without a BIA-inclusive calculation.

## Recycling / observability result

A terminal has positive effect

```math
G_i(\omega)=M^\dagger|i><i|M.
```

Under independent conservative one-final-sink Poisson lineages, ideal final-sink counting can give zero interterminal cross-spectrum despite internal recycling and mean crosstalk.

For an internally created and internally recombined pair,

```math
Q_i^{rec}=0,
```

while finite-transit Shockley-Ramo motion can give finite-frequency support. The endpoint channel null can therefore be lifted at finite frequency; a nonzero ensemble cross-spectrum is allowed, not guaranteed.

## Novelty discipline

Do not claim generic positive-operator, stable-rank, task-information, bright/dark-state, Shockley-Ramo, GR-noise, Poisson-output, photon-recycling, or optical-sum-rule theory as new.

Candidate-new content is the detector-specific cross-closure, shell decomposition/material diagnosis, and conservative-recycling observability boundary. No direct prior-art collision was found in the completed targeted audits; historical priority remains unproven.

## Production files

```text
experiments/13-observable-resource-unification/typeset/rev4_unified_prapplied.tex
experiments/13-observable-resource-unification/typeset/rev4_unified.bib
experiments/13-observable-resource-unification/typeset/rev4_figures.tex
experiments/13-observable-resource-unification/typeset/build_rev4.py
.github/workflows/rev4-flagship-pdf.yml
```

Do not replace the safe theorem-label/environment slicing in `build_rev4.py` with a broad multiline regex. An earlier broad regex swallowed preceding manuscript content in an intermediate build; the authoritative source was not damaged and the regression was repaired.

## Remaining blockers / next action

Human metadata is still intentionally placeholder text:

```text
author
institutional affiliation
corresponding email
acknowledgments / funding
```

When supplied, make a **metadata-only** edit, rebuild through CI, record new hashes, and inspect all pages again.

No new Gedanken branch or scientific rewrite is authorized by default. Reopen science only for a concrete mathematical defect, numerical inconsistency, direct prior-art collision, explicit referee/editor request, or specific journal requirement.
