# Active Frontier — Experiment 13 flagship Rev. 6

**Date:** 2026-08-15  
**Branch:** `experiment-13-observable-resource-unification`  
**Target:** Physical Review Applied — Regular Article  
**Status:** **REV. 6 SUPERSEDES REV. 5 / SECOND RE-REVIEW TECHNICAL ISSUES CLOSED / PRODUCTION + ALL-PAGE QA PASS / HUMAN SUBMISSION INPUTS REMAIN**

This file controls Experiment 13 whenever older frontier or recovery notes disagree with it. Rev. 4 and Rev. 5 remain reproducible historical checkpoints.

## Read first

1. `PAPER_REV6_FINAL_HOSTILE_REVIEW_2026-08-15.md`
2. `REV6_PRAPPLIED_PRODUCTION_QA_2026-08-15.md`
3. `PAPER_REV6_RESPONSE_TO_REREVIEW_2026-08-15.md`
4. `00_ACTIVE_FRONTIER_REV5_FLAGSHIP_2026-08-15.md` — historical
5. `PAPER_REV5_RENDERED_HOSTILE_REVIEW_2026-08-15.md` — historical review that led to Rev. 6
6. `PRAPPLIED_SUBMISSION_PREFLIGHT_2026-08-15.md` — submission guidance; Rev. 4 identifiers inside it are historical and should be overridden by this frontier

## Controlling production identity

```text
GitHub Actions run:   31905440563
head commit:          1fcd627f194223dbf277cbf9d51b87501b1fcdb6
artifact ID:          9252213152
artifact digest:      38709b3e6f5e6b236812a70b78880c195a4e86d718a62e9b5d1e2bb63e6f7a7b
PDF SHA-256:          fa3c40b73ae8c75b8317e5522ebf50fb5fbf77c099aeeef52cf378a4febcf2e6
TeX SHA-256:          2a4bed7a70098e1e641a59d64d16adfe549fc35d775868e2a6b4ec7b03fa3d74
figure SHA-256:       07ee725da6522c7060c27644852a78977468ba02dd85ba0497e66f820f67b816
builder SHA-256:      fafa390867f6cfe665f2b79647d58837c525c155f6c6f65d277b27d2d9243859
pages:                8
undefined refs/cites: none
overfull boxes:       none
underfull boxes:      none
all-page visual QA:   PASS
final hostile review: PASS
```

## Central theorem — unchanged

For selected direct cross-chemical-potential transitions,

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

At finite normalization volume this is an exact finite-system inequality.

For a macroscopic density floor, Rev. 6 explicitly restores

```math
\boxed{
\bar v_{\mathcal B}^{cap}
=\limsup_{j\to\infty}v_{\mathcal B,V_j}^{cap}<\infty.
}
```

Finite capacity at every finite volume is not enough if it diverges with system size.

## Stage-specific thesis

```text
H_task -> H_exc -> H_int -> H_term
```

Capacity, response selectivity, internal correlation, and terminal observability belong to the physical map on which they are defined. They cannot be transferred between detector stages without the intervening dynamics.

The fixed-stage reciprocal identity remains definitional bookkeeping and is not a novelty claim.

## Full population-tightness hierarchy

```math
\boxed{
\frac{n_{bound}}{n_{ref}}
=
\frac{n_{\mathcal B}^{act}}{n_{ref}}
\eta_F
\sum_a w_a^{act}\frac{c_a}{\mathcal S_a^{act}}.
}
```

The four physical loss mechanisms are:

```text
selected-support coverage;
Fermi-statistical slack;
shell-to-global capacity mismatch;
within-shell singular-spectrum concentration.
```

`eta_F` is now explicitly a **Fermi-statistical factor**. Kubo-Greenwood is an exact spectral representation and introduces no independent inequality/slack.

The optical bound-tightness variable is now

```math
\tau_{bound}^{act},
```

not `tau_obs`; `observability` is reserved for the terminal/readout null-space discussion.

## Production HgCdTe closure

```text
Eg                       = 0.123984 eV
x                        = 0.17973
Delta                    = 1.04945 eV
F                        = -0.01618
gamma1                   = 3.6273
gamma2                   = 0.3598
gamma3                   = 1.0717
EP                       = 18.8 eV
carrier cutoff           = 2.0 nm^-1
production quadrature    = 160 x 10 x 16
support check            = 200 x 12 x 20
degeneracy clustering    = 1e-7 eV
rank diagnostic          = singular value > 1e-6 m/s
rank-threshold audit     = 1e-9 through 1e4 m/s on 40 x 6 x 8, fraction stable to printed precision
selected k extent        = 0.583 nm^-1
v_B^cap                  = 1.01764e6 m/s
support fraction         = 0.66897
eta_F                    = 0.30684
tau_cap^act              = 0.57262
tau_bound^act            = 0.17570
full bound/reference     ~= 0.1175
```

```math
0.66897\times0.30684\times0.57262=0.1175398\ldots.
```

On the compact bounded momentum domain, the finite-dimensional second-order velocity matrix has a volume-independent microscopic operator bound. Therefore the projected-block capacity used in this HgCdTe validation satisfies the restored uniform thermodynamic-capacity hypothesis within the stated model.

## PT qualification

Complete nonzero singular-value isotropy is claimed only for the thermally relevant selected parent shells that are single fixed-k `PT` Kramers doublets in the BIA-neglecting validation.

Generic multidoublet `PT` blocks need only have Kramers-paired singular values. Real zincblende HgCdTe contains BIA.

## Recycling/readout boundary

The two-pixel internal cross-spectrum belongs to an explicit immigration-death-exchange Markov process with two-sided angular-frequency PSD.

Ideal endpoint zero cross-spectrum requires Poisson primaries, independent noninteracting lineages, exactly one final sink, final-sink-only readout, no branching/gain, and no shared electronics.

Finite-transit Shockley-Ramo motion can lift the single-lineage source-channel null at finite frequency even when the internally created/recombined segment carries zero integrated induced charge. A nonzero ensemble cross-spectrum becomes allowed, not guaranteed.

## Publication architecture — mandatory

The Rev. 5 re-review correctly identified that Experiment 13 substantially inherits Experiment 12's principal theorem and realistic HgCdTe validation.

The project-level resolution is:

```text
Experiment 13 Rev. 6:     SOLE PRIMARY ACTIVE SUBMISSION MANUSCRIPT
Experiment 12 PRB paper:  FROZEN FALLBACK / DEVELOPMENT PROVENANCE
simultaneous submission:  DO NOT DO
separate later submission of current Experiment 12 after Experiment 13 publication: DO NOT DO without a fresh overlap/distinct-contribution audit
```

The controlling Experiment-12 notice is:

`experiments/12-oscillator-strength-state-count-bound/00_SUBMISSION_HOLD_EXPERIMENT13_SUPERSESSION_2026-08-15.md`.

Experiments 01 and 09 also remain frozen fallback packages while their substantive results are included in the flagship. Do not submit materially overlapping versions concurrently.

## Reproducible production chain

```text
build_rev4.py
-> reconstruct Rev. 4
-> apply Rev. 4 -> Rev. 5 recorded patch sequence
-> build_rev6.py
-> rev6_prapplied.tex + rev6_figures.tex
-> REVTeX/BibTeX
-> automated QA
-> 180-dpi all-page renders
```

Workflow:

`.github/workflows/rev6-flagship-pdf.yml`

## Final hostile-review disposition

```text
CENTRAL THEOREM:                       PASS
THERMODYNAMIC CONDITION:              RESTORED / PASS
HgCdTe UNIFORM-CAPACITY LINK:         PASS
NUMERICAL METHOD DISCLOSURE:          PASS
SUPPORT-RANK THRESHOLD/STABILITY:     PASS
OBSERVABILITY TERMINOLOGY:            FIXED
FERMI/KUBO ATTRIBUTION:               FIXED
PUBLICATION OVERLAP:                  RESOLVED IF SUPERSESSION POLICY MAINTAINED
TASK/COHERENCE BREADTH:               MODERATE EDITORIAL RISK ONLY
PRODUCTION PDF:                       PASS
NEW SCIENTIFIC REVISION REQUIRED:     NO
```

## Remaining work

Do **not** create Rev. 7 or reopen theory by default.

Human/submission inputs remain:

```text
author name;
affiliation;
corresponding email;
acknowledgments/funding;
submission-history declaration;
final Data Availability / archival citation decision;
optional ORCID and referee recommendations/exclusions.
```

Before actual submission, update the submission-preflight/cover-letter layer to the Rev. 6 title/terminology and insert human-owned declarations. Then rebuild, hash, and inspect every page again.
