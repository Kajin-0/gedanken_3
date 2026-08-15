# Experiment 13 Rev. 5 — response to extreme adversarial review

**Date:** 2026-08-15  
**Target:** Physical Review Applied — Regular Article  
**Disposition:** **CORE THEOREM RETAINED / MANDATORY TECHNICAL CORRECTIONS APPLIED / UNIFICATION REFRAMED AROUND STAGE-SPECIFIC INFERENCE / LOCAL 8-PAGE RENDER PASSES VISUAL QA**

## Review diagnosis

The hostile review did not identify a fatal error in the optical population theorem. Its strongest publication threat was editorial: the Rev. 4 manuscript could be read as elevating the definitional identity `S tau = 1` into the unifying theorem and then attaching a semiconductor theorem and a stochastic readout result to it.

Rev. 5 changes the center of gravity without reopening the underlying research branch.

## Mandatory technical corrections

### 1. Stable-rank terminology

Rev. 4 used

```math
Tr(G)/lambda_max(G)
```

under generic "stable rank" language. Rev. 5 defines instead

```math
r_eff(G)=Tr(G)/lambda_max(G)=srank(sqrt(G)).
```

When `G=M^dagger M`, this equals the conventional stable rank of `M`. The shell-resolved quantity

```math
Tr(M_a M_a^dagger)/||M_a||_op^2
```

remains the conventional stable rank of `M_a`.

### 2. Task bound domain

The worst-orthogonal-task bound now states explicitly `d>1`.

### 3. Conditional meaning of certification

The manuscript now states that "certified" is conditional on:

```text
X lying in the declared admissible domain;
lambda_D actually bounding the relevant physical coupling there;
the measured response being attributable to X.
```

### 4. PT-isotropy qualification

Rev. 5 no longer says that PT symmetry generically makes an arbitrary exact-shell block fully singular-value isotropic.

It states the actual validation condition:

```text
each thermally relevant selected parent shell is one fixed-k PT Kramers doublet.
```

For one two-dimensional parent doublet, PT-even coupling to any number of partner doublets gives

```math
MM^dagger proportional to I_2,
```

so the two nonzero singular values are equal.

For a general multidoublet parent block, PT symmetry guarantees Kramers-paired singular values, not equality of every nonzero singular value.

### 5. Stochastic process behind the occupancy cross-spectrum

The two-pixel spectrum is now explicitly attached to an immigration-death-exchange Markov process:

```text
immigration into A and B: gamma m per pixel;
local deaths: gamma x_A and gamma x_B;
exchange A->B and B->A: k x_A and k x_B;
stationary means: E[x_A]=E[x_B]=m;
PSD convention: two-sided angular-frequency PSD.
```

The text explicitly notes that drift rates and stationary mean alone do not determine the innovation covariance or spectrum.

### 6. Channel-null proof

For a positive internal sector `X`, Rev. 5 now defines

```math
Y_X=M X M^dagger >= 0.
```

If channel `i` is null, `(Y_X)_ii=0`; PSD Cauchy-Schwarz gives

```math
|(Y_X)_ij|^2 <= (Y_X)_ii (Y_X)_jj = 0.
```

### 7. Final-sink Poisson cancellation proof

The manuscript now gives the explicit marking argument: a parent Poisson process of rate `Lambda` independently marked into exactly one sink produces independent Poisson sink streams of rates `Lambda p_A` and `Lambda p_B`; independent random displacement preserves independence. The zero cross-spectrum is therefore no longer left as a citation-level assertion.

## Conceptual revision

### `S tau = 1` demoted

The reciprocal identity remains because it is exact and useful bookkeeping, but Rev. 5 states plainly that it follows from the definitions and is not a new matrix theorem.

It is removed from the abstract and no longer receives a displayed equation in the conclusion.

### Stage-specific non-transferability promoted

The new central conceptual statement is:

```text
Optical excitation, internal dynamics, and terminal readout are different physical maps.
A spectral edge, singular-value distribution, or null space of one stage cannot be transferred to another stage without composing the intervening physical map.
```

This appears in the title, abstract, introduction, Fig. 1, discussion, and conclusion.

The paper therefore no longer claims that all three physical problems are consequences of one universal operator.

## Full population-tightness hierarchy promoted

Rev. 5 defines

```math
n_bound=L_B/(v_B^cap)^2
```

and writes the exact full factorization

```math
n_bound/n_ref
=
(n_B^act/n_ref)
eta_F
sum_a w_a^act c_a/S_a^act.
```

This identifies four physically distinct sources of lost tightness:

```text
support coverage;
Fermi/Kubo asymmetry;
shell-to-global capacity mismatch;
within-shell response selectivity.
```

For the broad HgCdTe validation:

```text
support coverage      = 0.66897
Fermi/Kubo            = 0.30684
capacity utilization  = 0.57262
within-shell factor   = 1.00000
active tightness      = 0.17570
full bound/reference  ~= 0.1175
```

This factorization is now the central "spectral geometry" result after the optical population theorem.

## Editorial changes

New candidate title:

> **Stage-specific spectral geometry of photodetection: state-count bounds, selectivity, and observability**

The abstract is re-ranked around:

1. optical population theorem;
2. full tightness hierarchy;
3. HgCdTe validation;
4. downstream readout-dependent observability.

The generic reciprocal identity is no longer given equal abstract weight.

## Figure changes

Five native vector figures remain, but the hierarchy is changed:

```text
Fig. 1 — stage-specific detector maps / non-transferability
Fig. 2 — principal optical population theorem flow
Fig. 3 — full four-factor population-tightness hierarchy
Fig. 4 — HgCdTe numerical closure of that hierarchy
Fig. 5 — final-sink versus finite-transit Ramo observability
```

## Local production QA

Candidate source:

```text
rev5_prapplied.tex
rev5_figures.tex
rev5_refs.bbl
```

Local build:

```text
REVTeX 4.2 / prapplied / two-column
8 pages
US Letter
opens successfully
no encryption
no undefined citations/references observed
no overfull boxes observed
all 8 pages rendered and visually inspected
no clipping, figure overflow, broken glyphs, or equation overflow
```

REVTeX still emits the same class-level deferred-float/stuck-float warning around the HgCdTe table, but the table and all figures are visibly present and correctly placed. This is a layout warning, not missing content.

## Scientific regression disposition

The following are intentionally unchanged:

```text
cross-mu Fermi inequality;
selected-conductivity convention;
exact-shell velocity capacity;
central population theorem;
HgCdTe production inputs and principal numerical values;
N_eff bright-projector result;
shell-resolved active-population factorization;
endpoint Poisson cancellation assumptions;
Shockley-Ramo zero-DC / possible nonzero-AC result.
```

## Recommendation

Do not submit Rev. 4 unchanged after receiving this review.

Rev. 5 is the stronger manuscript architecture. The hostile review's technical points are correct enough to merit repair, and its main editorial criticism is best answered by changing the paper's thesis rather than defending the definitional identity more aggressively.

Before calling Rev. 5 submission-ready, perform one more extreme adversarial review of the actual Rev. 5 PDF, with particular attention to whether the stage-specific thesis now genuinely connects Sections II-VII rather than merely changing the language.
