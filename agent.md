# Agent Handoff — Gedanken 3

**Date:** 2026-08-15  
**Active branch:** `experiment-13-observable-resource-unification`  
**Repository frontier:** **Experiment 13 Rev. 5 — Physical Review Applied production/rendered-hostile-review pass; human submission inputs remain**

## Read first

1. `experiments/13-observable-resource-unification/00_ACTIVE_FRONTIER_REV5_FLAGSHIP_2026-08-15.md`
2. `experiments/13-observable-resource-unification/PAPER_REV5_RENDERED_HOSTILE_REVIEW_2026-08-15.md`
3. `experiments/13-observable-resource-unification/REV5_PRAPPLIED_PRODUCTION_QA_2026-08-15.md`
4. `experiments/13-observable-resource-unification/PAPER_REV5_ADVERSARIAL_RESPONSE_2026-08-15.md`
5. `experiments/13-observable-resource-unification/PRAPPLIED_SUBMISSION_PREFLIGHT_2026-08-15.md`
6. `experiments/13-observable-resource-unification/CURRENT_STATE.md`

Rev. 4 is historical. Do not revert to it unless specifically comparing pre/post hostile-review states.

## Controlling production identity

```text
Actions run:          31903046137
head commit:          8ac77c06accd02e56c43910b903ff53bb07a72dd
artifact ID:          9251615353
artifact digest:      64046cfd6972a9fbc810ab4a67ef61b27b9cd16249b7c666ecd75fabd5c5f843
PDF SHA-256:          ce0fd199bb43652edf598ce7fa516e093e41fdc7a664d336092b8161ea7fa1c9
TeX SHA-256:          9f45c235d3e2852fe04bf77a2adf519213e7af76ef8c9a7e26194a2cb10c72e7
pages:                8
undefined refs/cites: none
overfull boxes:       none
visual QA:            PASS
hostile review:       PASS
```

## What changed from Rev. 4

An external extreme adversarial review found the central optical theorem sound but identified real weaknesses. Rev. 5 fixes them:

```text
Tr(G)/lambda_max(G) -> r_eff(G)=srank(sqrt(G));
S tau = 1 explicitly demoted to definitional bookkeeping;
stage-specific non-transferability promoted as the conceptual thesis;
full bound/reference tightness factorization added;
PT isotropy restricted to single-parent-doublet validation sectors;
immigration-death-exchange Markov model and PSD convention specified;
channel-null and final-sink Poisson proofs made explicit;
d>1 and conditional-certification qualifications added.
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

Unchanged from the previous audited theorem.

## New controlling hierarchy

```math
\boxed{
\frac{n_{bound}}{n_{ref}}
=
\frac{n_{\mathcal B}^{act}}{n_{ref}}
\eta_F
\sum_a w_a^{act}\frac{c_a}{\mathcal S_a^{act}}.
}
```

This is the physically informative organization:

```text
support coverage;
Fermi/Kubo asymmetry;
shell/global capacity mismatch;
within-shell selectivity.
```

HgCdTe broad-window closure:

```text
support fraction  = 0.66897
eta_F             = 0.30684
tau_cap^act       = 0.57262
active tightness  = 0.17570
full ratio        ~= 0.1175
```

## Stage-specific thesis

```text
H_task -> H_exc -> H_int -> H_term
```

Capacity, selectivity, internal correlation, and terminal observability belong to different physical maps. None may be transferred between stages without the intervening dynamics.

## PT boundary

Complete nonzero singular-value isotropy is claimed only for the thermally relevant selected parent shells that are single fixed-k `PT` Kramers doublets in the BIA-neglecting validation. Generic multidoublet `PT` blocks have paired singular values, not necessarily equal singular values. Real zincblende HgCdTe contains BIA.

## Recycling boundary

The occupancy spectrum now refers to an explicit immigration-death-exchange Markov model with two-sided angular-frequency PSD.

Ideal final-sink zero cross-spectrum requires Poisson primaries, independent lineages, one exclusive final sink, no branching/gain, and no shared electronics. Finite-transit Shockley-Ramo motion can lift the single-lineage source-channel null at finite frequency despite zero integrated induced charge. Ensemble cross-spectrum is allowed, not guaranteed.

## Strategy

```text
Experiment 13 Rev. 5:     PRIMARY submission path
Experiment 13 Rev. 4:     historical checkpoint
Experiment 01 manuscript: frozen fallback
Experiment 09 manuscript: frozen fallback
Experiment 12 manuscript: frozen fallback
new theory by default:    STOP
```

## Remaining work

No new scientific revision is currently authorized.

Required human/submission inputs:

```text
author name;
affiliation;
corresponding email;
acknowledgments/funding;
submission-history declaration;
final Data Availability / archive decision;
optional ORCID/referee recommendations/exclusions.
```

When supplied, make metadata-only changes, rebuild through CI, record new hashes, inspect all pages, and submit if clean.
