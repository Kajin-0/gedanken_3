# Paper A — Submission Architecture Readiness Check

**Date:** 2026-08-13  
**Branch:** `agent/paper-a-submission-package`  
**Target manuscript:** `PAPER_A_APPLIED_OPTICS_DRAFT.md`, Rev. 3

## Disposition

```text
THEOREM-LEVEL SCIENCE: PASS FROM FINAL INTERNAL ADVERSARIAL QA
JOURNAL-FACING CLAIM SCOPE: PASS
ABSTRACT SCOPE/LENGTH: PASS
FIGURE LOGIC: PASS
PRACTICAL TIMING-WINDOW INTERPRETATION: PASS
EXISTENCE-CONSTRUCTION DISCLOSURE: PASS
ONE-SIDED FEASIBILITY-BOUND PRESENTATION: PASS
PRIOR-ART HONESTY: PASS
NOVELTY: NOT ESTABLISHED
APPLIED OPTICS FIT: PLAUSIBLE, WITH MODERATE EDITORIAL-SIGNIFICANCE RISK
```

No new mathematical defect was found in the external-paper phase.

---

## Regression checks

### Obsolete theorem notation

Search for `T_D` in the Rev. 3 journal-facing draft:

```text
0 matches
```

### Priority language

Search for `novel`:

```text
0 matches
```

The word `first` appears only in ordinary phrases such as “first crossing” and “boundary occurs first”; there is no priority claim.

### Full-scan claim boundary

The draft explicitly retains

```math
P_D^{scan}\ge P_{D,true}
```

and states that it does **not** prove exact full signal-present scan detection-time reversal.

### Quantitative witness

The controlling result remains the continuum bracket

```math
P_{FA,s}\le0.0336428
<0.05
<0.0624701\le P_{FA,f}.
```

The manuscript and Figure 3 label the slow result as an **upper bound** and the fast result as a **lower bound**. Neither is represented as an exact PFA.

### Witness parameter interpretation

The Rev. 3 text explicitly states that

```text
alpha = .05
r = 6
```

were chosen to give a transparent finite-scale analytic witness. They are not recommended operating specifications and are not claimed to be representative of a particular detector pair.

### Physical interpretation

`G_tau` is described as a small-signal optical-to-electrical **existence construction**. The paper does not present it as a microscopic HgCdTe, InSb, photodiode, or APD model.

`L` is tied to experimentally meaningful timing uncertainty, including trigger/synchronization uncertainty, an asynchronous transient window, or a time-of-flight/range gate.

---

## Figure package

Reproduction script:

`numerics/paper_a_submission_figures.py`

Figures:

1. accumulated SNR fraction versus physical integration time;
2. physical full-template timing covariance for the `r=6` pair over common `L`;
3. one-sided continuum feasibility bounds around `alpha=.05`.

No numerical `T_G(L)` crossover curve is included or authorized.

---

## Submission-package status

The scientific text is now sufficiently stable to move into a real Optica manuscript template.

Before actual submission, still required:

1. author name/affiliation/contact metadata;
2. final Funding statement;
3. final Disclosures statement;
4. final Data Availability wording;
5. journal-template reference formatting and DOI verification;
6. insertion/export of the three final figure files;
7. rendered-manuscript QA and independent referee-style review.

Those are submission-production tasks, not reasons to reopen the theory.

---

## Scientific hard stop remains

**Do not create Step 50 by default.**

Do not revive invalidated hard-window grid crossover claims merely to obtain a more visually satisfying phase diagram.
