# Progress Log — Experiment 01

**Consolidation note — 2026-08-12 21:47 EDT:** mathematical closure stopped after Step 49; prior-art audit and short-paper architecture completed; **Paper A is now a single complete manuscript in `PAPER_A_DRAFT.md` after merging Section V and performing a consistency/compression pass. Novelty is not established.** Full derivations and failed/corrected branches remain in dedicated step files.

---

## Steps 01–12 — detector/detection-theory core

Equal scalar reference `D*` does not determine arbitrary temporal-signal performance. Full magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation stationary-Gaussian problem. Finite windows make phase/time placement relevant. Unknown arrival introduces global false-alarm timing-search complexity. In the defined scanning protocol, a controlled equal-eventual-SNR family can reverse fast/slow ranking because temporal compression changes both evidence accumulation and timing-search correlation length. This is protocol/task specific, not a universal detector theorem.

Exact detector-facing scaling:

```math
T_D(\alpha,\beta,L;\tau,\rho_0)
=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

For `r=tau_s/tau_f>1` and `ell=L/tau_s`:

```math
B_r(\ell)=X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)=0.
```

Under the Step-12 continuity/extreme-value assumptions: fast wins at known time; approaching the fast feasibility boundary, fast detection time diverges while slow remains feasible; at least one finite fast-to-slow crossover therefore exists. Slow-only feasibility is possible, fast-only feasibility is excluded in this deliberately equal-eventual-SNR scaled family, and uniqueness is not established.

---

## Steps 13–49 — mathematical stress-test branch

The later branch tested whether continuous timing-search statistics invalidated the detector-facing construction.

Consequential corrections and surviving results:

- **FAILED NUMERICAL ESTIMATE:** Step-13 rough-grid crossover `ell~49` invalid; hard-window timing scans are locally Brownian-like.
- Genuine finite information bandwidth removes the cusp; an invertible noiseless low-pass does not because optimal whitening cancels it.
- Rice's apparent upper switch near `kappa_f~130` was **INVALIDATED**; Palm preserved only the lower switch near `21.7 +/- .3`.
- **INVALIDATED INTERMEDIATE:** coupling coefficient `.8131`; corrected `.8906480701 sqrt(chi/zeta)`.
- **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-chi values were grid biased.
- Crossing counts fail from micro-upcrossings; finite-amplitude excursion clusters replace them.
- Step 39 found `R=N_a/N_tan~1.56`, rejecting a small-amplitude finite-u remainder.
- Step 40 introduced Cameron-Martin exact-event threshold translation.
- Step 41 replaced empirical q interpolation with analytic Gaussian-process control and corrected Step-35 tiny-q pair RMS from `~5.4e-5` to `~2.69e-5` asymptotically.
- Step 44 gave a genuine pointwise finite-grid 95% bound `P_FA/alpha<.999957771`, but only `.00004223 alpha` margin; continuum grid bias dominated.
- Step 45 showed witness retuning trades one near-boundary problem for another.
- Step 46 isolated missed between-sample maxima as the dominant grid error. **WORDING CORRECTION:** the five-event result supports sign/scale consistency only, not precise coefficient verification.
- Step 47 obtained the exact pure-alpha1 discrete Pickands correction.
- Step 48 found mixed finite-u transfer only `O(1e-5)` relative to an `O(9e-4)` discretization loss.
- Step 49 simulated the exact finite-window covariance directly and found the same grid-loss scale; higher-order covariance did not cancel it at order `1e-4`.

**HARD-STOP TRIGGERED at Step 49:** the remaining publication-grade mapping from exact-covariance spectral intensity to exact finite-search false-alarm probability is no longer proportionate to the detector question. Do not create Step 50 by default.

---

## Detector-facing prior-art audit — 20:31 EDT

`PRIOR_ART_AUDIT_DETECTOR_TASK_REVERSAL.md` found direct prior art for:

- pulse/energy detectivity from frequency-dependent detector response;
- sensitivity-speed / detectivity-bandwidth joint benchmarking;
- unknown-arrival matched-filter search penalties controlled by correlated peak statistics/template autocorrelation;
- standard all-pass magnitude preservation with altered phase/dispersion.

No direct hit was found in the focused audit for the complete equal-eventual-SNR photodetector task-reversal construction.

Disposition:

```text
POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.
```

---

## Paper architecture — 20:42 EDT

`PAPER_ARCHITECTURE_TASK_REVERSAL.md` fixed a five-section detector-facing paper:

1. established detector-metric context and finite-task question;
2. controlled equal-eventual-SNR family;
3. dimensionless detection-time surface;
4. task-reversal theorem and feasibility partition;
5. interpretation, limits, and detector-specification implications.

The main paper excludes Pickands/Palm/Rice/high-band endpoint closure machinery.

---

## Paper A drafting sequence

### 20:52 EDT — opening manuscript

`PAPER_A_DRAFT_OPENING.md` drafted title, abstract, Introduction, and Section II through the exact finite-record timing covariance. Established `D*`, pulse, bandwidth, and unknown-arrival search results were conceded explicitly as prior art.

### 21:03 EDT — Sections III–IV

`PAPER_A_DRAFT.md` added the correlated-scan threshold

```math
\Pr\left[\sup_{0\le q\le\ell}Z_x(q)>\Gamma(x,\ell,\alpha)\right]=\alpha,
```

the margin

```math
M(x;\ell,\rho_0,\alpha)
=\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha),
```

and the exact task scaling

```math
\boxed{T_D=\tau X_D(\rho_0,\alpha,\beta,L/\tau).}
```

Covariance ordering plus Gaussian comparison makes `Gamma` nonincreasing with observation duration, so `M` is strictly increasing. The reversal is not a self-suboptimal integration-duration effect.

Section IV formalized the task boundary, both/slow-only/neither feasibility partition, and Proposition 1 crossover proof. No uniqueness or universal faster/slower ordering is claimed.

### 21:35 EDT — Section V module

`PAPER_A_SECTION_V.md` established the discussion framework: detector–task ordering, device characterization versus task qualification, no new scalar sensitivity-speed metric, explicit protocol/model limitations, and the practical statement that timing uncertainty makes response time part of both evidence accumulation and nuisance-search geometry.

### 21:47 EDT — manuscript merge and consistency/compression pass

**Authoritative manuscript:** `PAPER_A_DRAFT.md`.

Changes completed:

- merged Section V into the main manuscript;
- moved references after the conclusion;
- removed the duplicate Section-IV interpretation block and let Section V carry interpretation;
- tightened the abstract and Introduction while preserving all scope restrictions;
- standardized body terminology on **eventual matched-filter SNR**;
- kept “asymptotic sensitivity” primarily as title/context language;
- checked Proposition 1 assumptions against the abstract and conclusion;
- kept the true-alignment criterion explicitly distinct from the total signal-present scan-maximum probability;
- preserved the conclusion that the relevant object is `X_D(rho_0,alpha,beta,L/tau)`, not a new detector-only scalar;
- did not add new theorem claims, numerical phase-diagram claims, or Step-13–49 closure machinery.

Detector-facing closing statement:

> **Detector specifications rank devices only relative to the task for which the ranking is being made. When arrival time is uncertain, response time affects both signal accumulation and the statistical size of the timing search.**

---

## Current stopping point

Stay inside **Paper A**. The scientific narrative is complete and compressed.

### Single next question

> Can the complete `PAPER_A_DRAFT.md` now receive a severe reviewer-style audit for mathematical correctness, hidden assumptions, citation adequacy, overclaiming, notation defects, and likely reviewer objections before formatting/submission work?
