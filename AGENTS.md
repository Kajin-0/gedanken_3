# Repository Recovery Guide — gedanken_3

**Date:** 2026-08-15  
**Active research branch:** `experiment-13-observable-resource-unification`  
**Current repository frontier:** **Experiment 13 unified flagship Rev. 4 — science frozen; title-complete Physical Review Applied production PDF QA-passed; human submission inputs required**

## Recovery order

Read these first, in order:

1. `agent.md`
2. `experiments/13-observable-resource-unification/00_ACTIVE_FRONTIER_REV4_FLAGSHIP_2026-08-15.md`
3. `experiments/13-observable-resource-unification/REV4_PRAPPLIED_TITLE_COMPLETE_PRODUCTION_QA_2026-08-15.md`
4. `experiments/13-observable-resource-unification/PAPER_REV4_RENDERED_HOSTILE_REVIEW_2026-08-15.md`
5. `experiments/13-observable-resource-unification/PRAPPLIED_SUBMISSION_PREFLIGHT_2026-08-15.md`
6. `experiments/13-observable-resource-unification/PAPER_DRAFT_REV4_CLAIM_REFERENCE_CLEAN_2026-08-15.md`
7. `experiments/13-observable-resource-unification/PAPER_REV4_REFERENCE_QA_2026-08-15.md`
8. `experiments/13-observable-resource-unification/PAPER_REV4_FINAL_HOSTILE_CLAIM_REFERENCE_REVIEW_2026-08-15.md`
9. `experiments/13-observable-resource-unification/HGCDTE_STABLE_RANK_PRODUCTION_QA_2026-08-15.md`
10. `experiments/13-observable-resource-unification/HGCDTE_PT_SYMMETRY_STABLE_RANK_EXPLANATION_2026-08-15.md`

Older Experiment-13 notes are derivation history. If they conflict with the recovery order above, the newer files control.

## Controlling title-complete production identity

```text
GitHub Actions run:   31901326001
head commit:          7b2f8fe1a9e92ba8ea778828c2682c5a374a1abb
artifact ID:          9251170031
artifact digest:      11d4bf5bd6262d6a19c6b1f0bdbdb7a7d16644981b9bd597c199e7a23ddbf32e
PDF SHA-256:          d2e65ab9b0953e1f987c8c2c2b47e4d8558ac72989b84325590b3a0a67086ee8
built TeX SHA-256:    c1459c18e4bf5d20f09a9a956c23b565c76bd0a913fe9636adc2ca7fe1e2b8f9
BibTeX SHA-256:       029d1029c487c99e277a24dc95ad536d10a41742992c89916a1991d423f39d3d
pages:                7
undefined refs/cites: none
overfull boxes:       none
reference titles:     complete for current bibliography
visual QA:            PASS
```

Pages 1–6 are render-identical to the hostile-reviewed pre-title-completion package. Only bibliography page 7 changed during title completion, and page 7 separately passed visual QA.

## Strategic state

```text
FLAGSHIP-FIRST STRATEGY:   ACTIVE
TARGET:                    Physical Review Applied Regular Article
SCIENTIFIC CONTENT:        FROZEN
PRODUCTION PDF:            QA-PASSED
REFERENCE TITLES:          COMPLETE
NEW THEORY BY DEFAULT:     STOP
```

The Experiment-01 Applied Optics, Experiment-09 PRA, and Experiment-12 PRB manuscripts remain mature frozen fallback packages. Preserve them. Do not simultaneously submit materially overlapping standalone and flagship manuscripts.

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

Use selected direct cross-chemical-potential conductivity and the basis-invariant exact-energy-shell capacity. Do not substitute arbitrary total conductivity or a pairwise velocity maximum.

The theorem bounds equilibrium one-body endpoint population. It is not a universal dark-current, generation-rate, finite-bandwidth-noise, or `D*` theorem.

## Unified connector and shell decomposition

For a physically declared admissible domain,

```math
\boxed{\mathcal S_{X|D}\tau_{X|D}=1.}
```

This is organizing algebra, not a generic novelty claim.

Important realizations:

```text
Experiment 09:   S=N_eff=1/sum_j w_j^2
Experiment 12:   S_th,B^act=1/tau_cap^act
uniform tasks:   S=d/r_st
readout stage:   channel-specific positive effects and null sectors
```

The dispersive thermal decomposition is

```math
\tau_{cap}^{act}=\sum_aw_a^{act}\frac{c_a}{\mathcal S_a^{act}},
\qquad
\tau_{obs}^{act}=\eta_F\sum_aw_a^{act}\frac{c_a}{\mathcal S_a^{act}}.
```

## Production HgCdTe result

```text
n_ref             = 1.005140525e17 cm^-3
v_B^cap           = 1.01764e6 m/s
eta_F             = 0.306836598
tau_cap^act       = 0.572622972
tau_obs^act       = 0.175701685
bound/reference   ~= 0.118
bound/active      ~= 0.176
```

```math
0.306836598\times0.572622972=0.175701685.
```

Selected active exact-shell blocks have `S_a^act=1` to floating-point precision only in the **BIA-neglecting second-order Kane validation model**. Do not generalize the exact equality to real zincblende HgCdTe without a BIA-inclusive calculation.

## Recycling observability result

Under independent conservative one-final-sink Poisson lineages, ideal endpoint counting can have zero interterminal cross-spectrum despite internal recycling and mean crosstalk. Finite-transit Shockley-Ramo coupling can lift the endpoint source-channel null at finite frequency even though an internally created/recombined pair has zero integrated induced charge. A nonzero ensemble cross-spectrum is allowed, not guaranteed.

## Novelty boundary

Do not claim generic matrix, stable-rank, task-information, bright/dark-state, Shockley-Ramo, GR-noise, Poisson-output, photon-recycling, or optical-sum-rule theory as new.

The candidate contribution remains the detector-specific cross-closure, shell decomposition/material diagnosis, and conservative-recycling readout boundary. No direct prior-art collision was found in completed targeted audits; historical priority remains unproven.

## Production / submission infrastructure

```text
experiments/13-observable-resource-unification/typeset/rev4_unified_prapplied.tex
experiments/13-observable-resource-unification/typeset/rev4_unified.bib
experiments/13-observable-resource-unification/typeset/rev4_figures.tex
experiments/13-observable-resource-unification/typeset/build_rev4.py
.github/workflows/rev4-flagship-pdf.yml
experiments/13-observable-resource-unification/PRAPPLIED_SUBMISSION_PREFLIGHT_2026-08-15.md
```

Do not replace the theorem-label/environment slicing in `build_rev4.py` with a broad multiline regex. An earlier broad regex swallowed preceding manuscript content in an intermediate built copy; the authoritative scientific source remained intact and the regression was caught during visual QA.

## Next work

Do **not** reopen theory by default.

Remaining human/submission inputs:

```text
author name
institutional affiliation
corresponding email
acknowledgments / funding statement
submission-history / joint-submission declaration
final Data Availability Statement / archival citation decision
optional ORCID and referee recommendations/exclusions
```

Once supplied, make metadata/submission-only edits, rebuild through CI, record new hashes, and inspect every rendered page again.

Reopen science only for a concrete mathematical defect, numerical inconsistency, direct prior-art collision, explicit referee/editor request, or specific journal requirement.
