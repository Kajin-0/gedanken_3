# Physical Review Applied submission preflight — Experiment 13 Rev. 4

**Date:** 2026-08-15  
**Target:** Physical Review Applied — Regular Article  
**Status:** **SUBMISSION MATERIALS PREPARED / HUMAN METADATA + DATA-ARCHIVE DECISION REQUIRED / FINAL BIBLIOGRAPHY-TITLE REBUILD PENDING AT CREATION**

## 1. Current journal requirements checked

Official APS / Physical Review Applied author guidance was checked on 2026-08-15.

Relevant official pages:

- `https://journals.aps.org/prapplied/authors`
- `https://journals.aps.org/authors/data-availability-statements`
- `https://journals.aps.org/authors/style-basics`
- `https://journals.aps.org/authors/editorial-policies-practices-physical-review-applied`

Current points relevant to this manuscript:

```text
Regular Article: no formal length limit.
A PDF alone is sufficient to enter peer review, but LaTeX source is preferred.
Physical Review Applied requires article titles in the published reference list.
A complete Data Availability Statement is required during submission.
Research Articles should provide an approximately 100-word justification of suitability.
The cover letter should explain context, key findings, submission history/joint-submission status,
and optionally recommended/excluded referees.
Appendices are generally preferred over standalone Supplemental Material for derivations/details.
Authors are advised to avoid unsupported priority language such as "first", "new", or "novel".
```

The manuscript already follows the final point: it uses narrow `we derive` positioning and explicitly identifies established mathematical ingredients.

## 2. Article type

Use:

```text
Physical Review Applied
Regular Article
```

Do not convert to a Letter by default. The unified argument benefits from retaining the theorem derivation, HgCdTe validation, and observability section in one self-contained article.

## 3. Required suitability justification

The following is 100 words and can be entered in the Physical Review Applied submission form:

> This manuscript derives a detector-facing equilibrium bound linking selected direct optical conductivity to the minimum thermal population of the one-body states that carry that response under a finite microscopic coupling capacity. It then exposes how the same spectral capacity controls forward selectivity and inverse resource certification, and resolves the bound tightness shell by shell. A production eight-band HgCdTe calculation explains the realistic 17.6% active-population tightness quantitatively. The work also identifies a readout-dependent boundary for conservative photon-recycling observability. These results connect semiconductor material physics, detector task selectivity, and terminal noise observability in a form directly relevant to applied photodetector design analysis.

Do not expand this into novelty/priority claims.

## 4. Cover-letter draft

Human metadata is left in brackets intentionally.

```text
Dear Editors of Physical Review Applied,

Please consider our manuscript, “Spectral geometry of photodetection: optical state-count bounds, selectivity, and internal observability,” for publication as a Regular Article in Physical Review Applied.

The manuscript addresses a detector-physics question at the interface of semiconductor response, measurement selectivity, and terminal readout. Its central result is an equilibrium lower bound on the one-body thermal endpoint population required to support a selected direct optical conductivity when the microscopic exact-shell velocity coupling has finite capacity. We then show how the same capacity structure controls forward selectivity and inverse resource certification, and derive a shell-resolved decomposition of the resulting bound tightness.

A production-resolution second-order eight-band HgCdTe calculation gives a quantitative test of the framework: the broad-window active-population tightness of 0.1757 factors into a 0.5726 capacity-utilization factor and a 0.3068 Fermi/Kubo factor. The manuscript also derives a conditional terminal-observability boundary showing how conservative photon-recycling lineages can be null under ideal final-sink counting yet acquire finite-frequency support through finite-transit Shockley–Ramo coupling.

We have deliberately limited the claims to these detector-specific results. Positive-operator methods, stable rank, bright/dark states, Shockley–Ramo theory, Poisson-output theory, photon recycling, and optical sum rules are treated as established ingredients rather than priority claims.

[SUBMISSION-HISTORY / JOINT-SUBMISSION STATEMENT]

[OPTIONAL RECOMMENDED OR EXCLUDED REFEREES]

Thank you for considering the manuscript.

Sincerely,
[AUTHOR NAME]
[AFFILIATION]
[EMAIL]
```

### Submission-history line

If no related paper has been submitted anywhere, use a plain factual sentence such as:

```text
This manuscript is not part of a joint submission.
```

Do not make a stronger statement about prior or concurrent submission until the human author confirms it.

## 5. Data Availability Statement

APS requires a complete Data Availability Statement during submission.

This is a theoretical/numerical paper. The public GitHub repository contains the derivations, numerical scripts, QA notes, and production infrastructure, but a publication-grade persistent archival identifier has not yet been recorded in the manuscript package.

### Preferred route

Before final submission or at latest before publication:

1. archive the controlling source/scripts with a persistent DOI, e.g. through a DOI-minting research archive;
2. add a formal data/software reference to the bibliography;
3. use a statement of the form:

```text
The data and software that support the findings of this article are openly available in Ref. [DATA-REF].
```

### Acceptable submission-stage fallback

If no DOI has been minted by submission time, enter a truthful statement that the supporting analytical derivations and numerical software are available in the public research repository, with the exact repository URL/commit or other stable locator requested by APS. Update it to the archival DOI during revision/proofing if one is created.

Do not invent a DOI or claim a permanent archive that does not exist.

## 6. Reference-title requirement

Physical Review Applied requires titles in published references and strongly encourages complete titled references at submission.

The production BibTeX database initially omitted titles for several legacy references. A dedicated bibliography-completeness patch now adds titles for:

```text
Piotrowski and Gawron (1997)
Callen and Welton (1951)
Watanabe and Oshikawa (2020)
Gusynin and Sharapov (2006)
Gusynin, Sharapov, and Carbotte (2007)
Novik et al. (2005)
Laurenti et al. (1990)
Mirasol (1963)
Harrison and Lemoine (1981)
```

It also adds the Mao–Mendez-Valderrama–Chowdhury DOI and the Harrison–Lemoine page range.

This patch requires a fresh compile/hash/all-page QA because added reference titles can change bibliography pagination. The pre-title-completion PDF must not be treated as the final submission identity after this patch.

## 7. Source package expected for APS

Submission source set:

```text
rev4_unified_prapplied.tex
rev4_unified.bib
rev4_figures.tex
build_rev4.py              [repository reproducibility; not necessarily uploaded to APS]
```

The built source produced by `build_rev4.py` is:

```text
rev4_unified_prapplied_built.tex
```

For APS upload, prefer the self-contained built TeX plus:

```text
rev4_unified.bib
rev4_figures.tex
```

or upload the complete production source set if the submission server handles the builder workflow cleanly. The submitted PDF must match the compiled source package.

No external raster figure files are required; the five figures are native TikZ.

## 8. Supplemental Material

No Supplemental Material is required by default.

The paper is only seven pages and is self-contained. Physical Review Applied generally prefers appendices over separate Supplemental Material for derivations/details in Regular Articles. Do not create an SM file merely to make the submission look more substantial.

If a referee later requests additional numerical convergence detail, an appendix or repository-backed supplement can be added then.

## 9. Human inputs still required

Before actual submission:

```text
[ ] legal/publication author name
[ ] institutional affiliation to appear on paper
[ ] corresponding email
[ ] acknowledgments
[ ] funding statement / explicit no-funding statement as appropriate
[ ] submission-history/joint-submission statement
[ ] optional referee recommendations/exclusions
[ ] data/software archive decision and final DAS
[ ] ORCID if the author wishes to supply it
```

These must not be guessed by an agent.

## 10. Final gate after those inputs

Once the human metadata and DAS are resolved:

```text
1. edit metadata only;
2. compile through the reproducible CI path;
3. require zero undefined citations/references and zero overfull boxes;
4. record new TeX/PDF/bibliography/figure hashes;
5. render every page;
6. inspect every page visually;
7. compare scientific equations/numbers against the frozen Rev. 4 state;
8. only then call the package submission-ready.
```
