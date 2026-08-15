# Agent Handoff — Gedanken 3

**Date:** 2026-08-15  
**Active branch:** `experiment-13-observable-resource-unification`  
**Repository frontier:** **Experiment 13 flagship Rev. 4 — science frozen; title-complete Physical Review Applied PDF QA-passed; human submission inputs required**

## Read first

1. `experiments/13-observable-resource-unification/00_ACTIVE_FRONTIER_REV4_FLAGSHIP_2026-08-15.md`
2. `experiments/13-observable-resource-unification/REV4_PRAPPLIED_TITLE_COMPLETE_PRODUCTION_QA_2026-08-15.md`
3. `experiments/13-observable-resource-unification/PAPER_REV4_RENDERED_HOSTILE_REVIEW_2026-08-15.md`
4. `experiments/13-observable-resource-unification/PRAPPLIED_SUBMISSION_PREFLIGHT_2026-08-15.md`
5. `experiments/13-observable-resource-unification/PAPER_DRAFT_REV4_CLAIM_REFERENCE_CLEAN_2026-08-15.md`
6. `experiments/13-observable-resource-unification/HGCDTE_STABLE_RANK_PRODUCTION_QA_2026-08-15.md`
7. `experiments/13-observable-resource-unification/HGCDTE_PT_SYMMETRY_STABLE_RANK_EXPLANATION_2026-08-15.md`

## Controlling production identity

```text
Actions run:          31901326001
head commit:          7b2f8fe1a9e92ba8ea778828c2682c5a374a1abb
artifact ID:          9251170031
artifact digest:      11d4bf5bd6262d6a19c6b1f0bdbdb7a7d16644981b9bd597c199e7a23ddbf32e
PDF SHA-256:          d2e65ab9b0953e1f987c8c2c2b47e4d8558ac72989b84325590b3a0a67086ee8
built TeX SHA-256:    c1459c18e4bf5d20f09a9a956c23b565c76bd0a913fe9636adc2ca7fe1e2b8f9
BibTeX SHA-256:       029d1029c487c99e277a24dc95ad536d10a41742992c89916a1991d423f39d3d
pages:                7
undefined refs/cites: none
overfull boxes:       none
reference titles:     complete
visual QA:            PASS
```

Pages 1–6 are render-identical to the hostile-reviewed package; only bibliography page 7 changed during title completion and it separately passed visual QA.

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

Unified organizing identity:

```math
\boxed{\mathcal S_{X|D}\tau_{X|D}=1.}
```

Do not sell this generic algebra as the novelty headline.

Shell decomposition:

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
S_th,B^act        ~= 1.746
bound/reference   ~= 0.118
bound/active      ~= 0.176
```

`S_a^act=1` to about `4e-14` only in the BIA-neglecting second-order Kane validation. Do not generalize exact isotropy to real zincblende HgCdTe without a BIA-inclusive calculation.

## Recycling / observability result

Under independent conservative one-final-sink Poisson lineages, ideal endpoint counting can have zero interterminal cross-spectrum despite internal recycling and mean crosstalk. Finite-transit Shockley-Ramo coupling can lift that endpoint source-channel null at finite frequency while an internally created/recombined pair still has zero integrated induced charge. Nonzero ensemble cross-spectrum is allowed, not guaranteed.

## Strategy

```text
Experiment 13 flagship:       PRIMARY
Experiment 01 manuscript:     FROZEN fallback
Experiment 09 manuscript:     FROZEN fallback
Experiment 12 manuscript:     FROZEN fallback
new theory by default:        STOP
```

No direct prior-art collision was found in completed targeted audits. Historical priority remains unproven.

## Submission materials already prepared

`PRAPPLIED_SUBMISSION_PREFLIGHT_2026-08-15.md` contains:

```text
100-word suitability justification;
cover-letter draft;
Data Availability/archive guidance;
source-package checklist;
reference-title compliance note.
```

## Remaining human/submission inputs

```text
author name
institutional affiliation
corresponding email
acknowledgments / funding statement
submission-history / joint-submission declaration
final Data Availability Statement / archival citation decision
optional ORCID and referee recommendations/exclusions
```

When supplied, make metadata/submission-only changes, rebuild through CI, record new hashes, and inspect every page again.

No new Gedanken branch or theory rewrite is authorized by default. Reopen science only for a concrete mathematical defect, numerical inconsistency, direct prior-art collision, or explicit editor/referee requirement.
