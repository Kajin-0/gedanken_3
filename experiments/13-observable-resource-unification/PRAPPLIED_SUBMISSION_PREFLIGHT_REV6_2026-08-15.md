# Physical Review Applied submission preflight — Experiment 13 Rev. 6

**Date:** 2026-08-15  
**Target:** Physical Review Applied — Regular Article  
**Status:** **SCIENTIFIC/PRODUCTION PREFLIGHT COMPLETE / HUMAN METADATA + DATA-ARCHIVE DECISION REQUIRED**

This file supersedes `PRAPPLIED_SUBMISSION_PREFLIGHT_2026-08-15.md` for manuscript-specific title, terminology, production identity, cover-letter language, and source-package instructions. The older file remains useful only as historical APS-guidance provenance.

## 1. Controlling manuscript

Title:

> **Stage-specific spectral geometry of photodetection: state-count bounds, selectivity, and observability**

Article type:

```text
Physical Review Applied
Regular Article
```

Controlling production identity:

```text
GitHub Actions run:   31905440563
head commit:          1fcd627f194223dbf277cbf9d51b87501b1fcdb6
artifact ID:          9252213152
artifact digest:      38709b3e6f5e6b236812a70b78880c195a4e86d718a62e9b5d1e2bb63e6f7a7b
PDF SHA-256:          fa3c40b73ae8c75b8317e5522ebf50fb5fbf77c099aeeef52cf378a4febcf2e6
TeX SHA-256:          2a4bed7a70098e1e641a59d64d16adfe549fc35d775868e2a6b4ec7b03fa3d74
BibTeX SHA-256:       029d1029c487c99e277a24dc95ad536d10a41742992c89916a1991d423f39d3d
figure SHA-256:       07ee725da6522c7060c27644852a78977468ba02dd85ba0497e66f820f67b816
pages:                8
undefined refs/cites: none
overfull/underfull:   none
all-page visual QA:   PASS
final hostile review: PASS
```

## 2. Current claim hierarchy

The submission should foreground the manuscript asymmetrically:

```text
1. principal result: finite-temperature optical population lower bound;
2. principal diagnostic extension: full support/Fermi/capacity/selectivity tightness hierarchy;
3. realistic application: production second-order eight-band HgCdTe closure;
4. framework consequence: stage-specific non-transferability;
5. downstream example: final-sink versus finite-transit photon-recycling observability.
```

Do not present the definitional `S tau = 1` normalization as a novelty headline.

Do not call `eta_F` a Fermi/Kubo loss. It is the **Fermi-statistical factor**; Kubo-Greenwood is the exact spectral representation.

Reserve `observability` for internal/terminal readout null spaces. The optical bound-tightness variable is `tau_bound^act`.

## 3. Approximately 100-word suitability justification

The following is 100 words under ordinary whitespace counting after treating slash/dash-separated compounds separately:

> This manuscript derives an equilibrium lower bound linking selected direct optical conductivity to the minimum thermal population of the one-body states carrying that response under a finite exact-shell coupling capacity. It resolves the bound’s tightness into support coverage, Fermi-statistical slack, shell-to-global capacity utilization, and within-shell selectivity, and validates the decomposition in a production eight-band HgCdTe model. The broader framework shows why detector inference is stage-specific: optical capacity, task/coherence selectivity, internal correlation, and terminal observability cannot be transferred between stages without the intervening physical map. A photon-recycling example demonstrates the resulting readout dependence through ideal final-sink and finite-transit Shockley–Ramo limits.

Do not add unsupported priority language.

## 4. Rev. 6 cover-letter draft

Human-owned fields remain bracketed deliberately.

```text
Dear Editors of Physical Review Applied,

Please consider our manuscript, “Stage-specific spectral geometry of photodetection: state-count bounds, selectivity, and observability,” for publication as a Regular Article in Physical Review Applied.

The manuscript derives an equilibrium lower bound on the thermal one-body endpoint population required to support selected direct optical conductivity when the exact-shell optical-velocity coupling has finite capacity. For a macroscopic density interpretation, the capacity is required to remain uniformly bounded along the thermodynamic sequence. The resulting inverse bound is then resolved into physically distinct losses from selected-support coverage, Fermi statistics, shell-to-global capacity mismatch, and within-shell singular-value concentration.

A production-resolution second-order eight-band HgCdTe calculation provides a realistic test. In the broad validation window, the selected active-support fraction is 0.66897, the Fermi-statistical factor is 0.30684, and the spectral-capacity tightness is 0.57262, giving an active-population bound tightness of 0.17570 and a full bound/reference ratio of approximately 0.1175. The manuscript states the numerical quadrature, capacity-search procedure, rank criterion, and stability checks used for this decomposition.

The broader detector framework is stage-specific rather than a claim that one operator describes the complete device. Optical capacity, task/coherence selectivity, internal correlation, and terminal observability belong to different physical maps and cannot be transferred between stages without the intervening dynamics. A conservative photon-recycling example illustrates this distinction: ideal exclusive final-sink counting can erase interterminal cross-noise, whereas finite-transit Shockley–Ramo motion can restore finite-frequency source-channel support despite zero integrated induced charge for an internally created and recombined pair segment.

The manuscript treats positive-operator methods, stable-rank concepts, bright/dark-state physics, Shockley–Ramo theory, Poisson splitting, photon recycling, and optical sum rules as established ingredients rather than priority claims.

[SUBMISSION-HISTORY / RELATED-MANUSCRIPT STATEMENT — HUMAN CONFIRMATION REQUIRED]

[OPTIONAL RECOMMENDED OR EXCLUDED REFEREES]

Thank you for considering the manuscript.

Sincerely,
[AUTHOR NAME]
[AFFILIATION]
[EMAIL]
```

## 5. Publication relationship to Experiment 12

Project policy is explicit:

```text
Experiment 13 Rev. 6: sole primary active submission manuscript;
Experiment 12 manuscript: frozen fallback/development provenance;
concurrent or second overlapping submission of the present Experiment-12 manuscript: prohibited by project policy.
```

This resolves the internal publication-overlap concern only if the policy is maintained.

For the actual journal submission, the human author must still confirm the truthful submission-history statement. Do not automatically convert the internal project policy into a factual declaration about what has or has not been submitted elsewhere.

If no related manuscript has ever been submitted or published, a plain statement such as

```text
This manuscript is not part of a joint submission and is not under consideration elsewhere.
```

may be appropriate only after human confirmation.

If any related manuscript has been submitted, posted, published, or is under consideration, disclose that accurately and reassess overlap before submission.

## 6. Data Availability / software archive

The manuscript is theoretical/numerical. The repository contains derivations, numerical scripts, convergence/rank audits, production builders, and manuscript QA.

Preferred final route:

```text
1. archive the controlling Rev. 6 source + numerical reproduction package in a persistent repository;
2. obtain a DOI or other permanent archival identifier;
3. add that record to the bibliography/data statement;
4. use a concise Data Availability Statement pointing to the archived record.
```

Do not invent a DOI.

If submission occurs before a persistent archive is minted, use a truthful public-repository/commit statement consistent with current APS requirements, then update to the archive during revision if appropriate.

## 7. Source package for APS

The reproducible repository chain is

```text
build_rev4.py
-> recorded Rev4-to-Rev5 patches
-> build_rev6.py
-> rev6_prapplied.tex
-> rev6_figures.tex
```

For journal upload, prefer the generated self-contained submission inputs rather than requiring APS to run the historical builder chain:

```text
rev6_prapplied.tex
rev6_figures.tex
rev4_unified.bib
```

The submitted PDF must match the compiled source package corresponding to the final metadata-complete build.

No external raster figures are required; the figures are native TikZ.

## 8. Scientific items that are closed

Do not reopen by default:

```text
cross-mu Fermi inequality;
Kubo-Greenwood normalization;
exact-shell capacity theorem;
thermodynamic uniform-capacity condition;
full population-tightness hierarchy;
production HgCdTe numerical values;
rank-threshold/stability audit;
PT single-parent-doublet qualification;
immigration-death-exchange spectrum;
Poisson final-sink cancellation;
Shockley-Ramo zero-DC / finite-frequency-support result.
```

Current remaining editorial risk is breadth, especially the generic uniform-task subsection. Compress that first only if requested by an editor/referee; do not sacrifice the central theorem, HgCdTe reproducibility, coherent `N_eff` specialization, or readout boundary merely to preserve generic task exposition.

## 9. Human completion checklist

Before a real submission:

```text
[ ] author name(s)
[ ] affiliation(s)
[ ] corresponding-author email
[ ] ORCID if desired/required
[ ] acknowledgments/funding statement
[ ] conflicts/disclosures as required
[ ] truthful submission-history / related-manuscript declaration
[ ] final Data Availability / persistent archive decision
[ ] optional recommended/excluded referees
[ ] replace all manuscript metadata placeholders
[ ] build the metadata-complete Rev. 6 source through CI
[ ] record final PDF/source hashes
[ ] visually inspect every final page
[ ] verify submitted source compiles to the submitted PDF
```

No Rev. 7 scientific revision is authorized by default.
