# PRA Rev. 5 render QA — Experiment 09

**Date:** 2026-08-14  
**Target:** Physical Review A — Regular Article  
**Manuscript:** `Scalable internal false-count limits in a coherence-selective photodetector`  
**Status:** RENDER PASS / SCIENTIFIC MAJOR-REVISION REPAIRS INCLUDED / NOVELTY NOT ESTABLISHED

## Rendered artifacts

Local production artifacts:

```text
Experiment09_PRA_Rev5_2026-08-14.tex
Experiment09_PRA_Rev5_2026-08-14.pdf
```

Final PDF SHA-256:

```text
bb41ad84b0904a9d126c9150a784effed0a9a77875f8358f4f03b7867df0bb7a
```

## Production checks

```text
REVTeX / PRA two-column compile: PASS
pages: 9
PDF open / preflight: PASS
citations: RESOLVED
cross-references: RESOLVED
missing-glyph / clipping check: PASS
figure legibility: PASS
figure embedding: VECTOR PDF
horizontal overfull boxes: NONE FOUND
remaining TeX warnings: two benign 5.74806 pt overfull-vbox output/grid warnings
```

The remaining `Overfull \vbox (5.74806pt too high) ... while \output is active` messages arise from REVTeX float/grid placement. Page-level visual inspection found no clipping, overlap, or unreadable content, so no scientific/layout change was made solely to silence them.

Author and affiliation metadata remain placeholders.

---

# Scientific changes represented in this render

Rev. 5 is not a cosmetic rerender of Rev. 4. It incorporates the external hostile-review repairs.

## 1. Primary asymptotic observable changed

The main internally generated false-event observable is now the dilute susceptibility

```math
\chi_N(\eta)
=N\int_0^{T_N(\eta)}C_{loc,N}(u)\,du
=\lim_{d\to0}\mu_{loc,N}(\eta;d)/d.
```

The old fixed-per-site-rate `d`, `N->infinity` formulation is no longer described as a uniformly valid low-density asymptotic.

Finite-rate independent-particle counting is retained only as a conditional kinetic realization:

```math
\mu_{loc,N}=d\chi_N.
```

## 2. Explicit Lindblad generator included

The manuscript now states

```math
\dot\varrho
=\kappa_N\mathcal D[|c\rangle\langle B|]\varrho
+\gamma_N\sum_j\mathcal D[|j\rangle\langle j|]\varrho,
```

and derives the exact closed `(P,b)` dynamics from it.

## 3. Scaling derivations expanded

The manuscript gives explicit leading signal/local-event kernels for:

```text
alpha > beta;
alpha < beta;
balanced fast eta < q0;
balanced slow eta > q0;
balanced boundary eta = q0.
```

The logarithmic boundary is derived through the Lambert-W balance rather than only stated.

## 4. Saturation robustness included

An intentionally severe one-event-per-site-per-gate model is used as a robustness test. On every strict slow-recycling branch in the bounded-coupling class,

```math
\mu_{1,N}(T_N)=\Theta(N).
```

Thus the detailed `N^(2-alpha)` powers belong to the unsaturable independent-particle reference model, while the slow-branch divergence itself survives maximal per-site saturation.

## 5. Headline language tightened

`eta_sc` is called the **bounded-response efficiency supremum**:

```math
\eta_{sc}=\sup\{\eta:\chi_N(\eta)=O(1)\}.
```

The manuscript explicitly states that `O(1)` means nondivergent with system size and does not imply an acceptably small false-event probability.

At balanced fixed rates (`s=0`), `q0` is a supremum but is not attained because the boundary susceptibility grows as `(ln N)^2`.

## 6. No-go scope made explicit

The main no-go is stated only **within the linear single-excitation resource class**:

```math
\text{strict slow recycling}\Rightarrow\chi_N=\Omega(N).
```

## 7. Figure 1 corrected again

The mechanism schematic now distinguishes microscopic processes from emergent clocks:

```text
local event -> bright component 1/N and dark-subspace component 1-1/N;
primitive local dephasing: gamma_N;
emergent return clock: effective slow eigenmode r_{-,N};
separate decision strip for T_N(eta) and chi_N.
```

The dashed `r_-` arrow is explicitly labeled as an effective eigenmode, not a microscopic jump.

Figure 2 plots `chi_N` and is described as a finite-N consistency illustration, not an independent numerical validation.

Figure 3 is a scaling-classification diagram.

## 8. Thermodynamic result demoted

The effective local-detailed-balance reverse-extraction analysis is supporting material and is no longer coequal with the susceptibility theorem.

---

# Current QA disposition

```text
Rev. 4 external major objection: REPAIRED IN REV. 5
one-body mathematics: RETAINED
large-N asymptotic self-consistency: REFORMULATED THROUGH chi_N
Lindblad specification: ADDED
asymptotic proof detail: EXPANDED
saturation stress: PASSES AT THE NO-GO LEVEL
figures: PASS CURRENT VISUAL QA
render: PASS
novelty: NOT ESTABLISHED
submission readiness: REQUIRES ONE FRESH HOSTILE REVIEW OF REV. 5
```

The next review should focus on whether the remaining exact-symmetry assumption is too restrictive for PRA significance—especially bounded heterogeneity in optical coupling, local dephasing, or a finite-rank bright subspace—not on the superseded fixed-`d` low-density objection.
