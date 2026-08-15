# Active Frontier — Experiment 13 unified flagship Rev. 5

**Date:** 2026-08-15  
**Branch:** `experiment-13-observable-resource-unification`  
**Target:** Physical Review Applied — Regular Article  
**Status:** **REV. 5 SUPERSEDES REV. 4 / SCIENTIFIC AND RENDERED HOSTILE REVIEW PASSED / HUMAN SUBMISSION METADATA REMAINS**

This file supersedes earlier Experiment-13 active-frontier files whenever they disagree with it. Rev. 4 remains a preserved reproducible historical checkpoint.

## Read first

1. `PAPER_REV5_RENDERED_HOSTILE_REVIEW_2026-08-15.md`
2. `REV5_PRAPPLIED_PRODUCTION_QA_2026-08-15.md`
3. `PAPER_REV5_ADVERSARIAL_RESPONSE_2026-08-15.md`
4. `PAPER_DRAFT_REV4_CLAIM_REFERENCE_CLEAN_2026-08-15.md` — historical scientific baseline
5. `PAPER_REV4_REFERENCE_QA_2026-08-15.md`
6. `HGCDTE_STABLE_RANK_PRODUCTION_QA_2026-08-15.md`
7. `HGCDTE_PT_SYMMETRY_STABLE_RANK_EXPLANATION_2026-08-15.md`
8. `CHANNEL_SPECIFIC_OBSERVABILITY_GEOMETRY_2026-08-15.md`

## Controlling production identity

```text
GitHub Actions run:   31903046137
head commit:          8ac77c06accd02e56c43910b903ff53bb07a72dd
artifact ID:          9251615353
artifact digest:      64046cfd6972a9fbc810ab4a67ef61b27b9cd16249b7c666ecd75fabd5c5f843
PDF SHA-256:          ce0fd199bb43652edf598ce7fa516e093e41fdc7a664d336092b8161ea7fa1c9
built TeX SHA-256:    9f45c235d3e2852fe04bf77a2adf519213e7af76ef8c9a7e26194a2cb10c72e7
figure SHA-256:       19c7b0f83ddadc9ff7000144ea09e257bb9d130fd898a519f88707bf54cbcf6d
pages:                8
undefined refs/cites: none
overfull boxes:       none
all-page visual QA:   PASS
rendered hostile review: PASS
```

One underfull paragraph and REVTeX class-level float warnings remain visually harmless.

## Why Rev. 5 supersedes Rev. 4

An external extreme adversarial review found the Rev. 4 central optical theorem sound, but correctly identified vulnerabilities that should not be defended away:

```text
1. Tr(G)/lambda_max(G) is srank(sqrt(G)), not generally stable rank of G;
2. S tau = 1 is definitional and was too prominent;
3. PT symmetry alone does not make arbitrary multidoublet blocks fully isotropic;
4. the two-pixel occupancy spectrum required an explicitly defined stochastic process;
5. the paper's true unity should be stage-specific inference, not one universal operator;
6. the full bound/reference tightness hierarchy should include support coverage.
```

Rev. 5 repairs all six points.

## Controlling conceptual thesis

The paper no longer claims that one operator describes every detector stage.

```text
H_task -> H_exc -> H_int -> H_term
```

Each stage has its own physical map.

The central conceptual rule is:

```text
capacity, response selectivity, internal correlation, and terminal observability
belong to the physical map on which they are defined;
none may be transferred between stages without the intervening dynamics.
```

The reciprocal `S tau = 1` relation remains fixed-map bookkeeping and is explicitly identified as definitional.

## Central semiconductor theorem

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

This theorem is unchanged from the previously audited Experiment-12/Rev.-4 result.

It requires selected direct cross-chemical-potential conductivity and an independently justified finite exact-shell capacity. It is an equilibrium independent-quasiparticle one-body population theorem, not a universal dark-current or `D*` theorem.

## Full population-tightness hierarchy

Rev. 5 promotes the exact relation

```math
\boxed{
\frac{n_{bound}}{n_{ref}}
=
\frac{n_{\mathcal B}^{act}}{n_{ref}}
\eta_F
\sum_a w_a^{act}\frac{c_a}{\mathcal S_a^{act}}.
}
```

This separates four mechanisms:

```text
selected-support coverage;
Fermi/Kubo asymmetry;
shell-to-global capacity mismatch;
within-shell response selectivity.
```

The final two occur inside the weighted sum in the general dispersive formula and are not falsely treated as two independent global factors.

## Production HgCdTe closure

```text
n_ref                    = 1.0051405e17 cm^-3
n_B^act                  = 6.7241114e16 cm^-3
support fraction         = 0.66897
eta_F                    = 0.30684
tau_cap^act              = 0.57262
tau_obs^act              = 0.17570
v_B^cap                  = 1.01764e6 m/s
full bound/reference     ~= 0.1175
```

```math
0.66897\times0.30684\times0.57262=0.1175398\ldots
```

and

```math
0.30684\times0.57262=0.17570.
```

## PT qualification

In the BIA-neglecting validation, each thermally relevant selected **parent** exact shell is one fixed-k `PT` Kramers doublet.

For one parent doublet coupled to any number of partner doublets,

```math
MM^\dagger\propto I_2,
```

so the two nonzero singular values are equal.

For a general multidoublet parent block, `PT` symmetry guarantees Kramers-paired singular values but does **not** require all nonzero singular values to be equal.

Real zincblende HgCdTe contains BIA; no universal shell-isotropy claim is made.

## Occupancy / recycling model

The internal two-pixel spectrum is now explicitly tied to an immigration-death-exchange Markov model:

```text
immigration into A,B: gamma m per pixel;
local death: gamma x_A, gamma x_B;
exchange: A->B at k x_A, B->A at k x_B;
stationary means: m;
PSD: two-sided angular-frequency convention.
```

The resulting cross-spectrum is

```math
S_{x,12}(\omega)=m\left[
\frac{\gamma}{\gamma^2+\omega^2}
-\frac{\gamma+2k}{(\gamma+2k)^2+\omega^2}
\right].
```

## Endpoint versus Ramo observability

Under independent Poisson primaries, independent noninteracting lineages, one final sink per lineage, final-sink-only measurement, no branching/gain, and no shared electronics, exclusive Poisson marking produces independent final-sink streams and

```math
S_{AB}^{end}(\omega)=0.
```

For a finite-transit internally created/recombined pair,

```math
Q_i^{rec}=0
```

while

```math
H_i^{rec}(\omega)
=i\omega e\int\Delta\phi_i(t)e^{-i\omega t}dt
```

can be nonzero for finite frequency. A nonzero ensemble cross-spectrum becomes allowed, not guaranteed.

## Final hostile-review disposition

```text
CENTRAL OPTICAL THEOREM:             PASS
STABLE-RANK TERMINOLOGY:             FIXED
FULL TIGHTNESS HIERARCHY:            PASS
HgCdTe NUMERICAL CLOSURE:            PASS
PT SINGLE-PARENT QUALIFICATION:      FIXED
MARKOV NOISE MODEL:                  FIXED
CHANNEL-NULL PROOF:                  PASS
FINAL-SINK POISSON PROOF:            PASS
SHOCKLEY-RAMO RESULT:                PASS
STAGE-SPECIFIC UNIFICATION:          PASS WITH MODERATE EDITORIAL RISK
RENDERED PDF:                        PASS
NEW SCIENTIFIC REVISION REQUIRED:    NO
```

The remaining risk is editorial breadth/significance, not an identified mathematical or physical defect.

## Publication strategy

```text
Experiment 13 Rev. 5 flagship: PRIMARY submission path
Experiment 13 Rev. 4:          preserved historical checkpoint
Experiment 01 manuscript:      frozen fallback
Experiment 09 manuscript:      frozen fallback
Experiment 12 manuscript:      frozen fallback PRB package
```

Do not submit materially overlapping flagship and standalone versions simultaneously.

## Remaining submission inputs

No new theory should be added by default.

Human/submission inputs still required:

```text
author name;
affiliation;
corresponding email;
acknowledgments/funding statement;
submission-history declaration;
final Data Availability / software archive decision;
optional referee recommendations/exclusions.
```

After metadata insertion, rebuild through CI, record new hashes, inspect all pages again, and submit if no metadata-induced regression appears.
