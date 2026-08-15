# Active Frontier — Experiment 13 unified flagship Rev. 4

**Date:** 2026-08-15  
**Branch:** `experiment-13-observable-resource-unification`  
**Target:** Physical Review Applied — Regular Article  
**Status:** **SCIENTIFICALLY FROZEN / TITLE-COMPLETE PRODUCTION PDF QA-PASSED / FLAGSHIP-FIRST / HUMAN SUBMISSION METADATA REQUIRED**

This file supersedes earlier Experiment-13 recovery notes whenever they disagree with it.

## Read first

1. `REV4_PRAPPLIED_TITLE_COMPLETE_PRODUCTION_QA_2026-08-15.md`
2. `PAPER_REV4_RENDERED_HOSTILE_REVIEW_2026-08-15.md`
3. `PRAPPLIED_SUBMISSION_PREFLIGHT_2026-08-15.md`
4. `REV4_PRAPPLIED_PRODUCTION_QA_2026-08-15.md`
5. `PAPER_DRAFT_REV4_CLAIM_REFERENCE_CLEAN_2026-08-15.md`
6. `PAPER_REV4_REFERENCE_QA_2026-08-15.md`
7. `PAPER_REV4_FINAL_HOSTILE_CLAIM_REFERENCE_REVIEW_2026-08-15.md`
8. `HGCDTE_STABLE_RANK_PRODUCTION_QA_2026-08-15.md`
9. `HGCDTE_PT_SYMMETRY_STABLE_RANK_EXPLANATION_2026-08-15.md`
10. `CHANNEL_SPECIFIC_OBSERVABILITY_GEOMETRY_2026-08-15.md`

## Controlling title-complete production identity

The controlling rendered manuscript is now the bibliography-title-complete seven-page Physical Review Applied REVTeX build:

```text
GitHub Actions run ID: 31901326001
head commit:           7b2f8fe1a9e92ba8ea778828c2682c5a374a1abb
artifact ID:           9251170031
artifact SHA-256:      11d4bf5bd6262d6a19c6b1f0bdbdb7a7d16644981b9bd597c199e7a23ddbf32e
PDF SHA-256:           d2e65ab9b0953e1f987c8c2c2b47e4d8558ac72989b84325590b3a0a67086ee8
built TeX SHA-256:     c1459c18e4bf5d20f09a9a956c23b565c76bd0a913fe9636adc2ca7fe1e2b8f9
BibTeX SHA-256:        029d1029c487c99e277a24dc95ad536d10a41742992c89916a1991d423f39d3d
figure SHA-256:        c577b1b09eaad28367b0a1318783feb95397b6d85b9ecf885200ed1d817c4f54
```

Production characteristics:

```text
7 pages / US Letter / two-column REVTeX prapplied
5 native vector TikZ figures
reference titles complete for current bibliography
undefined references: none
undefined citations:  none
overfull boxes:        none
all scientific pages:  visual QA preserved exactly
changed bibliography page 7: visual QA PASS
rendered hostile review: PASS
```

The bibliography-title rebuild left the built TeX and figures unchanged. Rendered pages 1–6 are byte-for-byte identical to the already hostile-reviewed production PDF; only page 7 changed and it separately passed visual inspection.

## Central physical theorem

For selected direct cross-chemical-potential transitions in an equilibrium independent-quasiparticle system,

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

Authoritative conductivity convention:

```math
\sigma_1^{cross}(\omega)
=\frac{\pi e^2}{V}
\sum_{cv}^{cross}
\frac{D_{cv}|v_{cv}|^2}{E_{cv}}
\delta\!\left(\omega-\frac{E_{cv}}{\hbar}\right).
```

The theorem requires the selected/direct cross-`mu` conductivity contribution, not arbitrary raw total conductivity. It bounds equilibrium one-body endpoint population, not universal dark current, generation rate, finite-bandwidth noise, or `D*`.

## Unified admissible-domain reciprocity

For a physically declared admissible domain `D`,

```math
\mathcal S_{X|D}
=\frac{\lambda_DTrX}{Tr(G_DX)},
\qquad
\tau_{X|D}
=\frac{Tr(G_DX)}{\lambda_DTrX},
```

so

```math
\boxed{\mathcal S_{X|D}\tau_{X|D}=1.}
```

This is organizing algebra, not a claim of new matrix theory. Its detector significance is the cross-identification of forward selectivity and inverse resource certification for the same physically declared capacity.

Important specializations:

```text
uniform task ensemble:     S=d/r_st
coherent bright projector: S=N_eff=1/sum_j w_j^2
thermal endpoint space:    S_th,B^act=1/tau_cap^act
```

## Shell-resolved population-bound decomposition

For selected endpoint shells `a`,

```math
\boxed{
\tau_{cap}^{act}=\sum_aw_a^{act}\frac{c_a}{\mathcal S_a^{act}},
}
```

and

```math
\boxed{
\tau_{obs}^{act}=\eta_F\sum_aw_a^{act}\frac{c_a}{\mathcal S_a^{act}}.
}
```

This separates theorem slack into Fermi/Kubo asymmetry, shell-to-global capacity mismatch, and within-shell singular-spectrum concentration.

## Production HgCdTe closure

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

The selected active exact-shell blocks have `S_a^act=1` to about `4e-14` **within the BIA-neglecting second-order Kane validation model**. The fixed-k `PT` doublet/quaternionic explanation is model-specific. Real zincblende HgCdTe has BIA; do not generalize the exact isotropy without a BIA-inclusive calculation.

## Recycling / terminal-observability result

At fixed frequency, terminal `i` has positive observability effect

```math
G_i(\omega)=M^\dagger|i><i|M.
```

A positive internal sector null to one terminal has zero cross contribution with every other terminal.

Under independent conservative one-final-sink Poisson lineages, final-sink-only counting can therefore have exactly zero interterminal endpoint cross-spectrum despite internal recycling and mean crosstalk.

For a pair created internally and later recombining internally at a common point,

```math
Q_i^{rec}=0,
```

but

```math
H_i^{rec}(\omega)
=i\omega e\int\Delta\phi_i(t)e^{-i\omega t}dt
```

can have finite-frequency support. Finite-transit Shockley-Ramo readout can lift the endpoint source-channel null at finite frequency; a nonzero ensemble cross-spectrum is allowed, not guaranteed.

## Novelty boundary

Do not claim novelty for positive/Gram operators, stable rank, task/Fisher matrices, generic bright/dark states, quantum discrimination, Shockley-Ramo theory, GR-noise coupling, Poisson output, HgCdTe photon recycling/mean crosstalk, or optical sum rules.

Candidate-new detector content remains narrowly:

```text
1. forward-selectivity / inverse-certification cross-identification;
2. exact mapping of nonuniform N_eff and thermal endpoint capacity;
3. shell-resolved decomposition of the optical population theorem;
4. production HgCdTe factor diagnosis and PT/BIA model interpretation;
5. conservative recycling final-sink channel null versus finite-transit Ramo lifting;
6. their causal organization into one staged detector argument.
```

No direct prior-art collision was found in the completed targeted audits. Use narrow “we derive” language rather than unsupported priority claims.

## Production / submission infrastructure

```text
typeset/rev4_unified_prapplied.tex
typeset/rev4_unified.bib
typeset/rev4_figures.tex
typeset/build_rev4.py
.github/workflows/rev4-flagship-pdf.yml
PRAPPLIED_SUBMISSION_PREFLIGHT_2026-08-15.md
```

Physical Review Applied preflight is complete for all non-human requirements currently actionable. The manuscript is a Regular Article; a 100-word suitability justification and cover-letter draft are recorded in the preflight note. A final Data Availability Statement/archive citation still requires a human archive decision.

Do not replace the safe theorem-label/environment slicing in `build_rev4.py` with a broad multiline regex.

## Publication strategy

```text
Experiment 13 unified flagship:  PRIMARY submission path
Experiment 01 manuscript:        FROZEN fallback
Experiment 09 manuscript:        FROZEN fallback
Experiment 12 manuscript:        FROZEN fallback PRB package
```

Do not simultaneously submit materially overlapping flagship and standalone versions.

## Remaining blockers / next action

No scientific work is required by default.

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

Once those are supplied:

```text
1. insert metadata only;
2. resolve final DAS/archive citation;
3. rebuild through CI;
4. record new TeX/PDF hashes;
5. inspect all pages again;
6. submit if no metadata-induced production defect appears.
```

Do not reopen theory absent a concrete mathematical defect, numerical inconsistency, direct prior-art collision, referee/editor request, or specific journal requirement.
