# Experiment 12 — Rev9 exposition-revision scope

**Date:** 2026-08-15  
**Branch:** `experiment-12-oscillator-strength-state-count-bound`  
**Source manuscript:** exact QA-passed `experiment12_prb_rev9.pdf`, recovered from the user Library  
**Scientific disposition:** **EXPOSITION ONLY / REV9 SCIENCE FROZEN**

## Purpose

Revise the Rev9 manuscript so that a physicist outside this exact subfield can follow the logical thread without reconstructing the argument from notation alone. This is not a simplification pass and not a scientific revision.

## Non-negotiable invariants

The revision must preserve:

```text
all numbered equations and mathematical inequalities;
all theorem hypotheses and quantifier structure;
all thermodynamic-limit and moving-window uniformity requirements;
all exact-mu endpoint caveats;
the distinction between cross-mu and conventional band populations;
the intrinsic-gap restriction on n_e=n_h=n_th;
the projected-block SVD definition of v_B^cap;
the exact support-rank interpretation and its discontinuity caveat;
all parabolic, Dirac, first-order Kane, and second-order HgCdTe validation results;
all numerical convergence, branch-selection, and bounded-k-domain qualifications;
all scope exclusions and all statements of what is not claimed;
all 18 references;
no novelty or priority claim.
```

## Requested exposition changes

1. Before every important new formal object, give one or two plain-language sentences explaining what it represents physically and why the proof needs it.
2. Before each major derivation step, state what logical obstacle that step resolves.
3. After each major numbered result, restate its physical content in one plain sentence.
4. Split compound sentences that carry multiple conditions or caveats.
5. Retain precise technical terms but gloss them at first use.
6. Introduce the equal-mass mirror-symmetric parabolic equality case near the beginning as a running intuition anchor, while retaining the complete validation subsection later.
7. Preserve and, where helpful, clarify negative-scope statements at section boundaries.
8. Do not remove equations, math, validation, references, hedges, caveats, or precision.

## Running intuition anchor

The early intuition should be the ideal equal-mass, mirror-symmetric parabolic two-band optical model with constant one-to-one optical matrix element. In that model every selected direct transition lies symmetrically about the chemical potential and each selected shell spends the same velocity resource per optically active degree of freedom. It therefore saturates both ingredients of the active-subspace inequality. The manuscript should refer back to this case while deriving the general result, but the full derivation and Eq. (36)–(38) validation remain in Section V.

## Source-of-truth hierarchy for QA

1. Exact Rev9 PDF text and equation numbering.
2. `MANUSCRIPT_REV9_CHANGESET_2026-08-15.md`.
3. `REV8_EXTERNAL_REREVIEW_RESPONSE_2026-08-15.md`.
4. `MANUSCRIPT_REV8_CHANGESET_2026-08-15.md`.
5. `MANUSCRIPT_REV7_CHANGESET_2026-08-15.md`.
6. Numerical reproducibility files and HgCdTe validation notes.

## Deliverables

- a new tracked Rev9-equivalent exposition-revised manuscript, leaving the prior Rev9 record untouched;
- a post-edit invariance/QA note explicitly checking equations, validation numbers, qualifiers, exclusions, and references against Rev9;
- synchronized recovery documentation.
