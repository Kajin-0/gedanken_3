# Progress Log — Experiment 01

**Consolidation note — 2026-08-12 22:09 EDT:** mathematical closure stopped after Step 49; prior-art audit and short-paper architecture completed; Paper A merged and consistency-compressed; **severe adversarial review now completed. Disposition: MAJOR REVISION / no fatal internal mathematical contradiction found / blocking operational-interpretation issues / novelty not established.**

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

**HARD-STOP TRIGGERED at Step 49:** do not create Step 50 by default.

---

## Detector-facing prior-art audit — 20:31 EDT

`PRIOR_ART_AUDIT_DETECTOR_TASK_REVERSAL.md` found direct prior art for pulse/energy detectivity from frequency-dependent response, detectivity-bandwidth benchmarking, unknown-arrival matched-filter search penalties, and standard all-pass magnitude/phase separation.

Disposition:

```text
POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.
```

---

## Paper A drafting and consolidation

### 20:42 EDT — architecture

`PAPER_ARCHITECTURE_TASK_REVERSAL.md` fixed a five-section detector-facing paper and moved Steps 13–49 out of the main narrative.

### 20:52 EDT — opening manuscript

`PAPER_A_DRAFT_OPENING.md` drafted title, abstract, Introduction, and Section II through exact finite-record timing covariance.

### 21:03 EDT — Sections III–IV

`PAPER_A_DRAFT.md` added the exact correlated-scan threshold, true-alignment margin, dimensionless task surface, feasibility partition, and Proposition 1 crossover proof.

### 21:35 EDT — Section V

`PAPER_A_SECTION_V.md` drafted detector-task interpretation, limitations, and experiment-design implications.

### 21:47 EDT — merge and consistency pass

`PAPER_A_DRAFT.md` became the single authoritative five-section manuscript. Section IV ends with the theorem/proof; Section V alone carries interpretation. Body terminology standardized on eventual matched-filter SNR. True-alignment criterion explicitly distinguished from full signal-present scan probability. No new theorem claims or Steps 13–49 machinery added.

---

## 22:09 EDT — severe adversarial reviewer audit

New file: `PAPER_A_ADVERSARIAL_REVIEW_AUDIT.md`.

### Core mathematics that survived

Direct checking found no fatal internal contradiction in:

```text
A_tau normalization;
eta(x);
R_x(y);
covariance ordering and Slepian direction;
strict margin monotonicity;
T_D=tau X_D(...,L/tau);
feasibility partition;
conditional intermediate-value crossover proof.
```

### Blocking issue A — acquisition clock

The stationary full-template scan over an arrival window `L` implicitly requires a batch record of about `L+t`. Current `T_D=t` is therefore not automatically an online wall-clock detection latency. Define the batch protocol and either call `T_D` the required post-window integration duration or define `T_wall=L+T_D`.

### Blocking issue B — true-alignment criterion

```math
P_{D,true}=\Phi[\rho_0\sqrt{\eta(x)}-\Gamma]
```

is not the exact full signal-present scan probability. It is a conservative guarantee because

```math
P_D^{scan}\ge P_{D,true}.
```

A reversal of guarantee times does not by itself prove a reversal of exact scan detection times. Default repair: explicitly reframe Paper A around a **true-alignment guaranteed detection criterion** rather than reopening the full Gaussian-extremes theorem.

### Major issue C — physical detector realization

Restore the fixed optical event and stable causal detector family:

```math
p(t)=e^{-bt}u(t),
```

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
```

which produces the manuscript template. State that equal eventual matched-filter SNR is event-specific and deliberately stronger than equal scalar `D*`.

### Major issue D — Proposition 1 assumptions

Strengthen rather than merely assume large-search growth and boundary divergence. The latter can largely be derived from `eta(x)<1`, `Gamma(x,ell)>=Gamma_infty(ell)`, boundary equality, and continuity. Add explicit Slepian and stationary-Gaussian extreme-value citations.

### Major issue E — no robust quantitative example

The existence theorem may cross only near the feasibility singularity. After conceptual repairs, add one continuum-validated non-knife-edge example/phase diagram with comfortable margins. Do not reuse invalidated Step-13 or treat Step-44 as continuum truth.

### Presentation/citation repairs

- distinguish `D*` noise-bandwidth normalization from detector temporal bandwidth;
- define the white-noise PSD/covariance convention exactly;
- reconsider title wording "equal asymptotic sensitivity" because `rho_0` is event-specific;
- add Yang DOI `10.1038/s41467-026-72259-1`;
- add Slepian/extreme-value citations;
- define `Phi` and standardize crossover notation.

### Additional novelty risk

Milstein et al., *Applied Optics* 47, 296–311 (2008), DOI `10.1364/AO.47.000296`, studies constant-false-alarm acquisition time in a specified range window for direct-detection ladar with Geiger-mode APDs. It is not a direct fast/slow reversal match, but it confirms substantial adjacent prior art at the photodetection/unknown-delay/acquisition-time intersection.

### Reviewer-style disposition

```text
MAJOR REVISION BEFORE SUBMISSION.
Do not format or submit yet.
```

---

## Current stopping point

Stay inside **Paper A**. Do not reopen the Gaussian-extremes branch.

### Single next question

> Can the manuscript be revised first to make the acquisition clock and the true-alignment guarantee criterion operationally exact, without changing the existing Gaussian-extremes hard stop or claiming a full signal-present scan theorem?
