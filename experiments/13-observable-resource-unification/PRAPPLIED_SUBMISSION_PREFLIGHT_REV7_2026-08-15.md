# Physical Review Applied submission preflight — Experiment 13 Rev. 7

**Date:** 2026-08-15  
**Target:** Physical Review Applied — Regular Article  
**Status:** **SCIENTIFIC/PRODUCTION PREFLIGHT COMPLETE / HUMAN METADATA + DATA-ARCHIVE DECISION REQUIRED**

This file supersedes the Rev. 6 preflight for manuscript-specific production identity, source-package instructions, and final wording. Earlier preflight files remain historical APS-guidance provenance.

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
GitHub Actions run:   31912951827
head commit:          f464dc966e0223f6b8c3ff1e51f82f948c8e950c
artifact ID:          9254179157
artifact digest:      29072be047b7a8174404ba02f32de1615c45c06daebcd5627b9f5cda54339d56
PDF SHA-256:          e40627dfb12f122cafb013415a475efffabda02befbff757ebd80b2da993da50
TeX SHA-256:          806ebffeb398a892550c62b9bcb7bcfa0c85c75a9c349add6f0ad628103ac5d6
BibTeX SHA-256:       029d1029c487c99e277a24dc95ad536d10a41742992c89916a1991d423f39d3d
figure SHA-256:       e60d35acc894ca5317d4ca5b8dce1b7b8869cfa62ca0cb6475181cfb5728d0c6
pages:                8
undefined refs/cites: none
overfull/underfull:   none
all-page visual QA:   PASS
final adversarial loop: CLOSED
```

## 2. Current claim hierarchy

Foreground the manuscript asymmetrically:

```text
1. principal result: finite-temperature optical population lower bound;
2. principal diagnostic extension: full support/Fermi/capacity/selectivity tightness hierarchy;
3. realistic application: numerically converged second-order eight-band HgCdTe closure;
4. framework consequence: stage-specific non-transferability;
5. downstream example: final-sink versus finite-transit photon-recycling observability.
```

Do not present the definitional `S tau = 1` normalization as a novelty headline.

`eta_F` is the **Fermi-statistical factor**; Kubo-Greenwood is exact spectral bookkeeping.

Reserve `observability` for internal/terminal readout null spaces. The optical bound-tightness variable is `tau_bound^act`.

Support coverage `n_B^act/n_ref` is reference-domain dependent and should not be described as an intrinsic property of the selected optical map.

## 3. Approximately 100-word suitability justification

> This manuscript derives an equilibrium lower bound linking selected direct optical conductivity to the minimum thermal population of the one-body states carrying that response under a finite exact-shell coupling capacity. It resolves the bound’s tightness into support coverage, Fermi-statistical slack, shell-to-global capacity utilization, and within-shell selectivity, and validates the decomposition in a numerically converged eight-band HgCdTe model. The broader framework shows why detector inference is stage-specific: optical capacity, task/coherence selectivity, internal correlation, and terminal observability cannot be transferred between stages without the intervening physical map. A photon-recycling example demonstrates the resulting readout dependence through ideal final-sink and finite-transit Shockley–Ramo limits.

Do not add unsupported priority language.

## 4. Rev. 7 cover-letter draft

Human-owned fields remain bracketed deliberately.

```text
Dear Editors of Physical Review Applied,

Please consider our manuscript, “Stage-specific spectral geometry of photodetection: state-count bounds, selectivity, and observability,” for publication as a Regular Article in Physical Review Applied.

The manuscript derives an equilibrium lower bound on the thermal one-body endpoint population required to support selected direct optical conductivity when the exact-shell optical-velocity coupling has finite capacity. For a macroscopic density interpretation, the capacity must remain uniformly bounded along the thermodynamic sequence. If the relevant intensive quantities have ordinary thermodynamic limits, the same density inequality follows; otherwise the manuscript states the corresponding liminf bound explicitly.

The resulting inverse bound is resolved into physically distinct losses from selected-support coverage, Fermi statistics, shell-to-global capacity mismatch, and within-shell singular-value concentration. The support-coverage factor is explicitly identified as dependent on the declared reference population rather than as an intrinsic property of the selected optical map.

A numerically converged second-order eight-band HgCdTe calculation provides a realistic test. In the broad validation window, the selected active-support fraction is 0.66897, the Fermi-statistical factor is 0.30684, and the spectral-capacity tightness is 0.57262, giving an active-population bound tightness of 0.17570 and a full bound/reference ratio of approximately 0.1175. The manuscript states the numerical quadrature, capacity-search procedure, rank criterion, stability checks, and carrier-domain convergence check used for this decomposition.

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
Experiment 13 Rev. 7: sole primary active submission manuscript;
Experiment 12 manuscript: frozen fallback/development provenance;
concurrent or second overlapping submission of the present Experiment-12 manuscript: prohibited by project policy.
```

This resolves the publication-overlap concern only if the policy is maintained.

For the actual journal submission, the human author must still confirm the truthful submission-history statement. Do not automatically convert internal project policy into a factual declaration about what has or has not been submitted elsewhere.

If no related manuscript has ever been submitted or published, a statement such as

```text
This manuscript is not part of a joint submission and is not under consideration elsewhere.
```

may be appropriate only after human confirmation.

If any related manuscript has been submitted, posted, published, or is under consideration, disclose that accurately and reassess overlap before submission.

## 6. Data Availability / software archive

The manuscript is theoretical/numerical. The repository contains derivations, numerical scripts, convergence/rank audits, production builders, and manuscript QA.

Preferred final route:

```text
1. archive the controlling Rev. 7 source + numerical reproduction package in a persistent repository;
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
-> build_rev7.py
-> rev7_prapplied.tex
-> rev7_figures.tex
```

For journal upload, prefer the generated self-contained submission inputs rather than requiring APS to run the historical builder chain:

```text
rev7_prapplied.tex
rev7_figures.tex
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
thermodynamic uniform-capacity condition and liminf refinement;
full population-tightness hierarchy;
production HgCdTe numerical values;
carrier-cutoff convergence check;
rank-threshold/stability audit;
PT single-parent-doublet qualification;
immigration-death-exchange spectrum;
Poisson final-sink cancellation;
Shockley-Ramo zero-DC / finite-frequency-support result.
```

Current remaining editorial risk is breadth, especially the generic uniform-task subsection. Compress that first only if requested by an editor/referee; do not sacrifice the central theorem, HgCdTe reproducibility, coherent `N_eff` specialization, or readout boundary merely to preserve generic task exposition.

A BIA-inclusive HgCdTe stress test is optional follow-up, not a current submission requirement under the stated BIA-neglecting claim.

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
[ ] build the metadata-complete Rev. 7 source through CI
[ ] record final PDF/source hashes
[ ] visually inspect every final page
[ ] verify submitted source compiles to the submitted PDF
```

No Rev. 8 scientific revision is authorized by default.
