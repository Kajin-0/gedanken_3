# Current State — Experiment 13: Spectral Geometry / Observable-Resource Unification

**Date:** 2026-08-15  
**Scope:** analytical/theoretical only  
**Target:** Physical Review Applied — Regular Article  
**Status:** **FLAGSHIP REV. 4 SCIENTIFICALLY FROZEN / TITLE-COMPLETE PRODUCTION PDF QA-PASSED / HUMAN SUBMISSION INPUTS REQUIRED**

## Read first

1. `00_ACTIVE_FRONTIER_REV4_FLAGSHIP_2026-08-15.md`
2. `REV4_PRAPPLIED_TITLE_COMPLETE_PRODUCTION_QA_2026-08-15.md`
3. `PAPER_REV4_RENDERED_HOSTILE_REVIEW_2026-08-15.md`
4. `PRAPPLIED_SUBMISSION_PREFLIGHT_2026-08-15.md`
5. `PAPER_DRAFT_REV4_CLAIM_REFERENCE_CLEAN_2026-08-15.md`
6. `PAPER_REV4_REFERENCE_QA_2026-08-15.md`
7. `PAPER_REV4_FINAL_HOSTILE_CLAIM_REFERENCE_REVIEW_2026-08-15.md`
8. `HGCDTE_STABLE_RANK_PRODUCTION_QA_2026-08-15.md`
9. `HGCDTE_PT_SYMMETRY_STABLE_RANK_EXPLANATION_2026-08-15.md`
10. `CHANNEL_SPECIFIC_OBSERVABILITY_GEOMETRY_2026-08-15.md`

## Controlling title-complete PDF

```text
Actions run:            31901326001
head commit:            7b2f8fe1a9e92ba8ea778828c2682c5a374a1abb
artifact ID:            9251170031
artifact digest:        11d4bf5bd6262d6a19c6b1f0bdbdb7a7d16644981b9bd597c199e7a23ddbf32e
PDF SHA-256:            d2e65ab9b0953e1f987c8c2c2b47e4d8558ac72989b84325590b3a0a67086ee8
built TeX SHA-256:      c1459c18e4bf5d20f09a9a956c23b565c76bd0a913fe9636adc2ca7fe1e2b8f9
BibTeX SHA-256:         029d1029c487c99e277a24dc95ad536d10a41742992c89916a1991d423f39d3d
pages:                  7
undefined refs/cites:   none
overfull boxes:         none
reference titles:       complete for current bibliography
visual QA:              PASS
```

Pages 1–6 are rendered byte-for-byte identically to the hostile-reviewed pre-title-completion package. Only bibliography page 7 changed; it separately passed visual QA.

## Scientific center

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

The theorem uses selected direct cross-`mu` conductivity and the basis-invariant exact-shell capacity. It bounds equilibrium one-body endpoint population, not universal dark current, generation rate, finite-bandwidth noise, or `D*`.

Unified connector:

```math
\boxed{\mathcal S_{X|D}\tau_{X|D}=1.}
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

`S_a^act=1` to about `4e-14` only within the BIA-neglecting second-order Kane validation model. Do not universalize the exact shell isotropy to real zincblende HgCdTe without a BIA-inclusive calculation.

## Recycling / observability result

Under independent conservative one-final-sink Poisson lineages, ideal final-sink counting can have exactly zero interterminal cross-spectrum despite internal recycling and mean crosstalk. Finite-transit Shockley-Ramo current can lift the endpoint source-channel null at finite frequency even though an internally created/recombined pair has zero integrated induced charge. A nonzero ensemble cross-spectrum is allowed, not guaranteed.

## Strategy

```text
Experiment 13 flagship:       primary submission path
Experiment 01 manuscript:     frozen fallback
Experiment 09 manuscript:     frozen fallback
Experiment 12 manuscript:     frozen fallback
new theory by default:        stop
```

No direct prior-art collision was found in completed targeted audits. Historical priority remains unproven; avoid priority language.

## APS submission preflight

Current Physical Review Applied requirements were checked. The repository now contains:

```text
100-word suitability justification
cover-letter draft
data-availability/archive decision guidance
source-package checklist
reference-title completion
```

No standalone Supplemental Material is required by default.

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

When these are supplied, make metadata/submission-only changes, rebuild, rehash, and visually inspect every page. Reopen science only for a concrete scientific defect, direct prior-art collision, or explicit editor/referee requirement.
