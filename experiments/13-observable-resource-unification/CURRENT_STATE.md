# Current State — Experiment 13: Stage-Specific Spectral Geometry of Photodetection

**Date:** 2026-08-15  
**Scope:** analytical/theoretical only  
**Target:** Physical Review Applied — Regular Article  
**Status:** **REV. 5 CONTROLS / PRODUCTION QA PASS / RENDERED HOSTILE REVIEW PASS / HUMAN SUBMISSION INPUTS REMAIN**

## Read first

1. `00_ACTIVE_FRONTIER_REV5_FLAGSHIP_2026-08-15.md`
2. `PAPER_REV5_RENDERED_HOSTILE_REVIEW_2026-08-15.md`
3. `REV5_PRAPPLIED_PRODUCTION_QA_2026-08-15.md`
4. `PAPER_REV5_ADVERSARIAL_RESPONSE_2026-08-15.md`
5. `PRAPPLIED_SUBMISSION_PREFLIGHT_2026-08-15.md`
6. `PAPER_DRAFT_REV4_CLAIM_REFERENCE_CLEAN_2026-08-15.md` — historical scientific baseline
7. `HGCDTE_STABLE_RANK_PRODUCTION_QA_2026-08-15.md`
8. `HGCDTE_PT_SYMMETRY_STABLE_RANK_EXPLANATION_2026-08-15.md`
9. `CHANNEL_SPECIFIC_OBSERVABILITY_GEOMETRY_2026-08-15.md`

Rev. 4 remains preserved as the reproducible pre-adversarial-review checkpoint. Rev. 5 supersedes it for submission.

## Controlling Rev. 5 production identity

```text
GitHub Actions run:   31903046137
head commit:          8ac77c06accd02e56c43910b903ff53bb07a72dd
artifact ID:          9251615353
artifact digest:      64046cfd6972a9fbc810ab4a67ef61b27b9cd16249b7c666ecd75fabd5c5f843
PDF SHA-256:          ce0fd199bb43652edf598ce7fa516e093e41fdc7a664d336092b8161ea7fa1c9
TeX SHA-256:          9f45c235d3e2852fe04bf77a2adf519213e7af76ef8c9a7e26194a2cb10c72e7
figure SHA-256:       19c7b0f83ddadc9ff7000144ea09e257bb9d130fd898a519f88707bf54cbcf6d
pages:                8
undefined refs/cites: none
overfull boxes:       none
all-page visual QA:   PASS
rendered hostile review: PASS
```

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

This theorem is unchanged by Rev. 5. It requires selected direct cross-chemical-potential conductivity and an independently justified exact-shell velocity capacity.

## Rev. 5 conceptual thesis

The paper no longer treats a reciprocal definition as the unifying theorem.

The controlling principle is stage-specific inference:

```text
H_task -> H_exc -> H_int -> H_term
```

Capacity, selectivity, internal correlation, and terminal observability are properties of the relevant physical stage map. They cannot be transferred between stages without including the intervening dynamics.

The fixed-map identity

```math
\mathcal S_{X|D}\tau_{X|D}=1
```

is explicitly described as definitional bookkeeping.

## Full population-tightness hierarchy

Rev. 5 promotes

```math
\boxed{
\frac{n_{bound}}{n_{ref}}
=
\frac{n_{\mathcal B}^{act}}{n_{ref}}
\eta_F
\sum_a w_a^{act}\frac{c_a}{\mathcal S_a^{act}}.
}
```

The hierarchy identifies:

```text
selected-support coverage;
Fermi/Kubo asymmetry;
shell-to-global capacity mismatch;
within-shell response selectivity.
```

## Production HgCdTe closure

```text
n_ref                    = 1.0051405e17 cm^-3
n_B^act                  = 6.7241114e16 cm^-3
n_B^act / n_ref          = 0.66897
eta_F                    = 0.30684
tau_cap^act              = 0.57262
tau_obs^act              = 0.17570
v_B^cap                  = 1.01764e6 m/s
bound/reference          ~= 0.1175
```

```math
0.66897\times0.30684\times0.57262=0.1175398\ldots
```

The exact within-shell isotropy in this validation is restricted to thermally relevant selected parent shells that are single fixed-k `PT` Kramers doublets in the BIA-neglecting second-order Kane model. Generic multidoublet `PT` blocks need only have paired singular values. Real zincblende HgCdTe contains BIA.

## Internal occupancy / recycling

The two-pixel cross-spectrum is now explicitly tied to an immigration-death-exchange Markov process with two-sided angular-frequency PSD convention.

Under independent Poisson primaries, independent noninteracting lineages, one final sink per lineage, final-sink-only readout, no branching/gain, and no shared electronics, exclusive marking gives independent final-sink streams and zero ideal endpoint cross-spectrum.

Finite-transit Shockley-Ramo motion can restore finite-frequency source-channel support even when the internally created/recombined segment has zero integrated induced charge. A nonzero ensemble cross-spectrum is allowed, not guaranteed.

## Hostile-review disposition

```text
central optical theorem:             PASS
stable-rank terminology:             FIXED
full tightness hierarchy:            PASS
HgCdTe numerical closure:            PASS
PT single-parent qualification:      FIXED
Markov noise model:                  FIXED
channel-null proof:                  PASS
final-sink Poisson proof:            PASS
Shockley-Ramo result:                PASS
stage-specific unification:          PASS WITH MODERATE EDITORIAL RISK
rendered PDF:                        PASS
new scientific revision required:    NO
```

## Strategy

```text
Experiment 13 Rev. 5:     primary flagship submission path
Experiment 13 Rev. 4:     preserved historical checkpoint
Experiment 01 manuscript: frozen fallback
Experiment 09 manuscript: frozen fallback
Experiment 12 manuscript: frozen fallback
new theory by default:    stop
```

## Remaining inputs

No scientific revision is currently required.

Before submission, supply/resolve:

```text
author name;
affiliation;
corresponding email;
acknowledgments/funding;
submission-history declaration;
final Data Availability / archival citation decision;
optional ORCID and referee recommendations/exclusions.
```

After metadata insertion, rebuild through CI, record new hashes, and inspect all pages again. Reopen science only for a concrete defect, direct prior-art collision, or explicit editor/referee request.
