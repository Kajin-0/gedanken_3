# Experiment 12 — PRB submission metadata checklist

**Date:** 2026-08-14  
**Target:** Physical Review B — Regular Article  
**Scientific text:** `MANUSCRIPT_REV6_2026-08-14.md`  
**Rendered QA:** `PRB_RENDER_QA_2026-08-14.md`

## 1. Manuscript metadata

```text
Working title:
Thermal quasiparticle population bound from direct interband optical spectral weight

Article type:
Regular Article

Target journal:
Physical Review B

Fallback journal:
Journal of Applied Physics
```

## 2. Author-owned fields still required

Do not infer or fabricate these during production.

```text
[ ] Full author name(s), exact publication spelling
[ ] Author order
[ ] Affiliation(s)
[ ] Corresponding-author email
[ ] ORCID(s), if used
[ ] Funding statement
[ ] Conflict-of-interest / disclosure statement
[ ] Confirmation of authorship approval
[ ] Confirmation of simultaneous-submission status
[ ] Prior Physical Review submission history
[ ] Joint-submission status
[ ] Recommended referees, optional
[ ] Excluded referees, optional
```

## 3. Data Availability Statement

Physical Review requires a Data Availability Statement during submission.

This manuscript is analytical/theoretical, but it reports numerical validation values obtained from equations and reproducibility scripts. Two defensible paths are available.

### Preferred publication path — archive the validation scripts

Archive the exact reproducibility scripts in a persistent repository such as Zenodo and cite the resulting DOI.

Recommended statement after a DOI exists:

> The numerical results supporting this article can be reproduced from the equations presented in the manuscript. The scripts used for the numerical validation calculations are openly available at Ref. [DATA REFERENCE].

The corresponding data/software citation should be added to the reference list in APS format.

### Conservative path if no public archive is created before submission

> No experimental data were created or analyzed in this study. The numerical values reported in the article can be reproduced directly from the equations presented in the manuscript. The calculation scripts are available from the corresponding author upon reasonable request.

This should be reviewed against the final APS submission-form choices before submission.

### Do not use without checking

Avoid the unqualified statement

```text
“No data were created or analyzed in this study.”
```

because the manuscript contains numerical validation values and reproducibility scripts even though it contains no experimental dataset.

## 4. Reproducibility materials already present in the branch

The Experiment-12 branch contains analytical/numerical validation scripts, including the Dirac validation and single-pass witness used in manuscript development.

Before archival deposit:

```text
[ ] identify every script needed to reproduce a number quoted in Rev6;
[ ] remove obsolete scripts that correspond only to rejected intermediate formulations;
[ ] add a short README with software version and command lines;
[ ] run the scripts from a clean environment;
[ ] record expected outputs;
[ ] archive the frozen package and obtain a persistent DOI;
[ ] add the data/software citation to the manuscript and DAS.
```

This is a reproducibility/production task, not a new scientific calculation.

## 5. Submission letter

Current draft:

`PRB_COVER_LETTER_DRAFT_2026-08-14.md`

The cover letter already contains:

```text
context of the result;
summary of key findings;
why the result fits PRB;
explicit scope limitations;
placeholders for submission history;
placeholders for recommended/excluded referees.
```

Author-owned declarations must be filled before submission.

## 6. Manuscript-source production status

Local PRB REVTeX render has passed compile and visual QA.

QA-passed local artifacts:

```text
experiment12_prb_rev6.tex
SHA-256 ecd9e09621c6fc3e87e9e6293f51ae4499b68a9e9ca878662a076e5d21700ced

experiment12_prb_rev6.pdf
SHA-256 b705d0868c3f2349a1821b5856f09792e8b2e0599d98efe38745c4e353229896
```

The source uses REVTeX 4.2 and an embedded `thebibliography` for local reproducibility because the current build environment lacks the `bibtex` executable.

## 7. Final pre-submission gate

Before actual submission:

```text
[ ] author metadata complete
[ ] funding/disclosure fields complete
[ ] submission-history statements complete
[ ] Data Availability Statement finalized
[ ] reproducibility archive decision made
[ ] exact final source recompiled
[ ] final PDF visually reviewed after author metadata is inserted
[ ] no “first,” “novel,” or priority language introduced
[ ] no universal dark-current / D* / noise claim introduced
```

## 8. Current stopping rule

```text
NO MORE THEORY BY DEFAULT.
```

The only open work is submission production and author-owned metadata unless a genuine external referee identifies a scientific defect.