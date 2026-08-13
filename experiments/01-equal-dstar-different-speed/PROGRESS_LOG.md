# Progress Log — Experiment 01

**Consolidation note — 2026-08-12 22:54 EDT:** mathematical closure remains hard-stopped after Step 49; prior-art audit and severe adversarial review completed; **Paper A blocking acquisition-clock and true-alignment claim-scope issues have now been repaired on the active revision branch.** The central theorem is now explicitly a task-dependent **guarantee-time** result. Robust exact-model quantitative example and final novelty audit remain open.

---

## Steps 01–12 — detector/detection-theory core

Equal scalar reference `D*` does not determine arbitrary temporal-signal performance. Full magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation stationary-Gaussian problem. Finite windows make phase/time placement relevant. Unknown arrival introduces global false-alarm timing-search complexity. In the defined scanning protocol, a controlled equal-eventual-SNR family can reverse fast/slow ranking because temporal compression changes both evidence accumulation and timing-search correlation length. This is protocol/task specific, not a universal detector theorem.

Historical detector-facing scaling before the major-revision semantic repair:

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

This historical notation is retained here for provenance. The active Paper A manuscript now replaces unqualified `T_D` by operational guarantee time `T_G`; see the 22:54 revision entry below.

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

Strengthen rather than merely assume large-search growth and boundary divergence. The latter can largely be derived from `eta(x)<1`, `Gamma(x,ell)>=Gamma_infty(ell)`, boundary equality, and continuity. Add explicit Slepian and stationary-Gaussian extreme-value support.

### Major issue E — no robust quantitative example

The existence theorem may cross only near the feasibility singularity. After conceptual repairs, add one continuum-validated non-knife-edge example/phase diagram with comfortable margins. Do not reuse invalidated Step-13 or treat Step-44 as continuum truth.

### Presentation/citation repairs

- distinguish `D*` noise-bandwidth normalization from detector temporal bandwidth;
- define the white-noise PSD/covariance convention exactly;
- reconsider title wording "equal asymptotic sensitivity" because `rho_0` is event-specific;
- add Yang DOI `10.1038/s41467-026-72259-1`;
- add Slepian/extreme-value support;
- define `Phi` and standardize crossover notation.

### Additional novelty risk

Milstein et al., *Applied Optics* 47, 296–311 (2008), DOI `10.1364/AO.47.000296`, studies constant-false-alarm acquisition time in a specified range window for direct-detection ladar with Geiger-mode APDs. It is not a direct fast/slow reversal match, but it confirms substantial adjacent prior art at the photodetection/unknown-delay/acquisition-time intersection.

### Reviewer-style disposition

```text
MAJOR REVISION BEFORE SUBMISSION.
Do not format or submit yet.
```

---

## 22:54 EDT — Paper A operational guarantee-time major revision

New audit trail: `PAPER_A_MAJOR_REVISION_2026-08-12.md`.

Revised authoritative manuscript: `PAPER_A_DRAFT.md` on the active revision branch.

### Blocking issue A resolved — exact batch clock

For every candidate arrival in `[0,L]` to receive the same duration-`t` post-arrival template, the record must extend to `L+t`.

The paper now defines

```math
\boxed{
T_G=\text{minimum required post-window integration duration}.
}
```

The actual batch wall time is

```math
\boxed{
T_{wall}=L+T_G.
}
```

Since `L` is common to both channels, `T_wall` and `T_G` have identical pairwise ordering.

### Blocking issue B resolved by exact claim narrowing

The manuscript now explicitly defines complete signal-present scan power and proves only the one-sided implication

```math
\boxed{
P_D^{scan}\ge P_{D,true}.
}
```

Thus `P_D,true>=beta` is a sufficient guarantee, and the theorem concerns the time required to satisfy that guarantee.

**No claim remains that the exact first solutions of `P_D^scan=beta` reverse ordering.**

### Common optical event restored

All channels now receive

```math
p(t)=e^{-bt}u(t)
```

through

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
```

producing

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
```

Equal eventual matched-filter SNR is explicitly event-specific.

### Noise and detector terminology tightened

The revision fixes

```math
E[n(t)n(t')]=N\delta(t-t'),
\qquad
\rho^2=(1/N)\int s^2dt,
```

and distinguishes `D*` noise-equivalent measurement-bandwidth normalization from detector temporal / `-3 dB` bandwidth.

### Proposition 1 strengthened

Two previous assumptions are now derived.

1. `Gamma_infty(ell,alpha)->infinity` follows directly from `R_infty(y)=(1+y)e^{-y}->0`: widely separated samples are compared by Slepian with an equicorrelated Gaussian vector whose maximum diverges.
2. `X_G->infinity` at `ell_crit` follows from `eta(x)<1`, `R_x<=R_infty`, `Gamma(x)>=Gamma_infty`, boundary equality, and continuity.

The proposition now assumes only known-time guarantee feasibility and ordinary threshold/first-crossing continuity.

### Hard stop explicitly preserved

No Step 50 was created. No Pickands/Palm/Rice closure branch was reopened.

The revision does **not** revive:

```text
Step-13 ell~49;
Step-20 upper Rice switch;
raw Step-27 tiny-chi values;
Step-44 as continuum truth;
Steps 47-49 as exact finite-u scan probabilities.
```

### Remaining major scientific presentation gap

A robust exact-hard-window quantitative example is still required.

The correct next numerical task is **margin-first design**, not rescue of the old `r=2, Lambda=.895` calibration. The example should show:

```text
low L: fast guarantee-time preference;
intermediate L: crossover with both channels comfortably guarantee-feasible;
larger L: slow-only guarantee feasibility;
```

with explicit continuum control.

The smooth finite-information Steps 14–16 remain a valid companion stress test but are not substituted for the exact Paper A model.

---

## Current stopping point

Paper A's two submission-blocking semantic issues are repaired, and the theorem is stronger and narrower.

The repository remains **not submission-ready** because:

```text
robust exact-model quantitative example is open;
final closest-prior-art / novelty audit is open;
final citation and manuscript QA remain to be done after the example.
```

### Single next question

> Can a new continuum-controlled exact-hard-window example be chosen for numerical margin rather than proximity to the old feasibility-edge witness, without reopening the Step-49 closure program?
