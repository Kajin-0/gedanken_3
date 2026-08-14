# PRA Rev. 8a — final precision patch

**Date:** 2026-08-14  
**Branch:** `experiment-09-coherence-selective-photodetection`  
**Status:** submission-production baseline pending author metadata and final citation-network check.

## Trigger

A fresh re-review of Rev. 8 found the manuscript technically ready except for one mathematical shorthand in the abstract:

```math
P_{FA}=d\chi_N+O(d^2)
```

The body already contained the more precise expansion

```math
P_{FA}=1-e^{-d\chi_N}
=d\chi_N+O(d^2\chi_N^2).
```

Because `chi_N` is itself the quantity whose size dependence is under study, dropping the factor `chi_N^2` from the remainder could be misread as making the remainder uniform in `N`.

## Rev. 8a correction

The abstract now reads

```math
P_{FA}=d\chi_N+O(d^2\chi_N^2).
```

The Fig. 1 caption contained the same abbreviated remainder and was corrected at the same time.

No theorem, equation in the body, figure geometry, parameter choice, asymptotic result, citation, or discussion claim changed.

## QA

```text
REVTeX compile: PASS
pages: 9
PDF preflight: PASS
page 1 visual QA: PASS
page 3 / Fig. 1 visual QA: PASS
overfull boxes: NONE
underfull boxes: NONE
```

Final local artifacts:

```text
Experiment09_PRA_Rev8a_2026-08-14.pdf
SHA-256 794c8b1c30ea82150b333f4163515871990c9573dd791b94484e5dc4a44ab043

Experiment09_PRA_Rev8a_2026-08-14.tex
SHA-256 d0f694cf71a9e2663ae7a0955901f41457afca92588f17882fb2b33877de02e0
```

## Current scientific disposition

The most recent hostile re-review found all substantive Rev. 6 objections repaired in Rev. 8, independently recomputed the exact Fig. 2 slopes with the disclosed parameters, and found no regression in the previously audited derivations. Its recommendation was effectively **ready**, subject only to this one-line remainder correction and real author/affiliation metadata at actual submission.

Do not open new theory merely to continue revision numbering. Remaining work is submission production unless a new external review identifies a specific scientific blocker.
