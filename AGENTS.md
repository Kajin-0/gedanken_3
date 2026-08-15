# Repository Recovery Guide — gedanken_3

**Date:** 2026-08-15  
**Active research branch:** `experiment-13-observable-resource-unification`  
**Current repository frontier:** **Experiment 13 Rev. 5 — Physical Review Applied flagship, production QA + rendered hostile review passed**

## Recovery order

Read these first:

1. `agent.md`
2. `experiments/13-observable-resource-unification/00_ACTIVE_FRONTIER_REV5_FLAGSHIP_2026-08-15.md`
3. `experiments/13-observable-resource-unification/PAPER_REV5_RENDERED_HOSTILE_REVIEW_2026-08-15.md`
4. `experiments/13-observable-resource-unification/REV5_PRAPPLIED_PRODUCTION_QA_2026-08-15.md`
5. `experiments/13-observable-resource-unification/PAPER_REV5_ADVERSARIAL_RESPONSE_2026-08-15.md`
6. `experiments/13-observable-resource-unification/CURRENT_STATE.md`
7. `experiments/13-observable-resource-unification/PRAPPLIED_SUBMISSION_PREFLIGHT_2026-08-15.md`

Rev. 4 and earlier Experiment-13 files are derivation/production history. Preserve them, but Rev. 5 controls whenever states conflict.

## Controlling production identity

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
visual QA:            PASS
hostile review:       PASS
```

## Why Rev. 5 exists

An external extreme adversarial review found no collapse of the central optical population theorem but correctly identified weaknesses in Rev. 4:

```text
stable-rank terminology was imprecise;
S tau = 1 was definitional and too prominent;
PT symmetry was stated too broadly for multidoublet blocks;
the occupancy-noise stochastic process was underdefined;
the full support/Fermi/capacity/selectivity hierarchy was not foregrounded;
the manuscript's unity needed to be stage-specific inference rather than one universal operator.
```

Rev. 5 fixes these issues and passed a second rendered hostile review. No Rev. 6 scientific revision is currently required.

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

Use selected direct cross-chemical-potential conductivity and the exact-shell capacity. Do not substitute arbitrary total conductivity or a pairwise velocity maximum.

## Stage-specific conceptual thesis

```text
H_task -> H_exc -> H_int -> H_term
```

Capacity, selectivity, internal correlation, and terminal observability belong to different stage maps. None can be transferred between stages without the intervening physical dynamics.

The fixed-map identity

```math
\mathcal S_{X|D}\tau_{X|D}=1
```

is explicitly treated as definitional bookkeeping, not a novelty claim.

For a maximally mixed task ensemble the generic positive-effect quantity is

```math
r_{eff}(G)=Tr(G)/lambda_max(G)=srank(sqrt(G)),
```

not generally the stable rank of `G` itself.

## Full population-bound hierarchy

```math
\boxed{
\frac{n_{bound}}{n_{ref}}
=
\frac{n_{\mathcal B}^{act}}{n_{ref}}
\eta_F
\sum_a w_a^{act}\frac{c_a}{\mathcal S_a^{act}}.
}
```

This resolves lost tightness into:

```text
support coverage;
Fermi/Kubo asymmetry;
shell/global capacity mismatch;
within-shell response selectivity.
```

## HgCdTe production closure

```text
n_B^act / n_ref      = 0.66897
eta_F                = 0.30684
tau_cap^act          = 0.57262
tau_obs^act          = 0.17570
full bound/reference ~= 0.1175
v_B^cap              = 1.01764e6 m/s
```

```math
0.66897\times0.30684\times0.57262=0.1175398\ldots
```

Complete singular-value isotropy is claimed only for the thermally relevant selected **single-parent-doublet** sectors in the BIA-neglecting validation. Generic multidoublet `PT` blocks need only have Kramers-paired singular values. Real zincblende HgCdTe contains BIA.

## Recycling / terminal-observability boundary

The two-pixel internal cross-spectrum now refers to an explicit immigration-death-exchange Markov model with two-sided angular-frequency PSD.

Ideal final-sink zero cross-spectrum requires Poisson primaries, independent noninteracting lineages, exactly one final sink, final-sink-only readout, no branching/gain, and no shared electronics.

Finite-transit Shockley-Ramo motion can restore finite-frequency source-channel support even when an internally created/recombined pair segment has zero integrated induced charge. Nonzero ensemble cross-spectrum is allowed, not guaranteed.

## Reproducible Rev. 5 production

Rev. 5 is mechanically constructed from the frozen Rev. 4 built source:

```text
experiments/13-observable-resource-unification/typeset/rev5_from_rev4.patch.part1
experiments/13-observable-resource-unification/typeset/rev5_from_rev4.patch.part2
experiments/13-observable-resource-unification/typeset/rev5_from_rev4.patch.part3
experiments/13-observable-resource-unification/typeset/rev5_figures.tex
.github/workflows/rev5-flagship-pdf.yml
```

CI reconstructs Rev. 4, applies the recorded Rev. 5 patch, compiles, runs automated QA, renders every page, and uploads the artifact.

## Strategy

```text
Experiment 13 Rev. 5:     PRIMARY flagship submission path
Experiment 13 Rev. 4:     preserved historical checkpoint
Experiment 01 manuscript: frozen fallback
Experiment 09 manuscript: frozen fallback
Experiment 12 manuscript: frozen fallback
new theory by default:    STOP
```

Do not simultaneously submit materially overlapping flagship and standalone versions.

## Remaining work

No new scientific revision is currently required.

Human/submission inputs still needed:

```text
author name;
affiliation;
corresponding email;
acknowledgments/funding statement;
submission-history declaration;
final Data Availability / archival citation decision;
optional ORCID and referee recommendations/exclusions.
```

After metadata insertion, rebuild through CI, record new hashes, inspect all pages again, and submit if clean. Reopen science only for a concrete mathematical defect, numerical inconsistency, direct prior-art collision, or explicit editor/referee requirement.
