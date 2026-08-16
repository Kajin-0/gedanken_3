# Full homogeneous BIA — splitting-diagnostic clarification

**Date:** 2026-08-15  
**Status:** **CLAIM-PRECISION ADDENDUM / NO NUMERICAL OR THEOREM CHANGE**

The full homogeneous `B8v+ / B8v- / C_k` HgCdTe audit reports a maximum selected-support separation of approximately `26.56 meV` and a k-space-weighted value of approximately `10.88 meV`.

These quantities are deliberately **diagnostics**, not inputs to the optical population theorem or the tightness hierarchy.

## What the diagnostic is

At each sampled k point that contains at least one selected cross-mu transition, the eigenvalues are ordered and the calculation records the largest separation among the adjacent pairs inherited from the BIA-off doublet ordering:

```text
(0,1), (2,3), (4,5), (6,7).
```

The maximum of that adjacent-pair separation over selected-support k points is about `26.56 meV`.

It demonstrates that the inversion-breaking perturbation is not numerically infinitesimal on the selected support.

## What the diagnostic is not

It is **not** a globally branch-tracked spin splitting through every possible band crossing or avoided crossing. Therefore manuscript language should call it an

> adjacent-pair separation diagnostic over selected-support points

rather than an unqualified spin splitting.

## Quantities that do not depend on this diagnostic

The following controlling results are computed directly from the BIA-inclusive eigenproblem and do not use the adjacent-pair diagnostic:

```text
chemical potential;
reference population;
active population;
Fermi-statistical factor;
exact-shell block dimensions;
exact-shell singular values and S_a;
continuous ordinary-supremum capacity;
tau_cap;
tau_bound;
full bound/reference ratio.
```

In particular, the central BIA result

```text
40452 sampled active exact blocks are one-dimensional;
S_a^act = 1 for every active block;
continuous capacity ~= 1.0220274e6 m/s;
full bound/reference ratio ~= 0.11651;
relative change from BIA-off ~= -0.82%.
```

is independent of how the adjacent-pair diagnostic is labeled or interpreted.

## Disposition

The final Rev. 8 production builder tightens the manuscript wording accordingly. No numerical recalculation or scientific revision is triggered by this clarification.
