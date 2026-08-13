# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-12 20:42 EDT  
**Status:** mathematical closure branch stopped after 49 logical steps; detector-facing prior-art audit and paper architecture completed. **NOVELTY NOT ESTABLISHED.** The project is now divided into a short detector/detection-theory paper track and a separate technical Gaussian-extremes companion. Do not create Step 50 of the old proof chain by default.

Read next:
1. `PAPER_ARCHITECTURE_TASK_REVERSAL.md`
2. `PRIOR_ART_AUDIT_DETECTOR_TASK_REVERSAL.md`
3. `TASK_REGIME_BOUNDARY_STEP.md`
4. `PROGRESS_LOG.md`

---

## Detector/detection-theory core — Steps 01–12

The surviving core is:

- A scalar reference `D*` does not determine arbitrary temporal-signal performance, but this is established prior art for pulse detection and is **not** the novelty target.
- Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation stationary-Gaussian maximum-SNR problem.
- Finite windows make phase/time placement operationally relevant even when magnitude response is identical; an all-pass construction removes the trivial pure-delay objection.
- Finite-time optimal SNR is `rho_T^2=<s_T,C_T^-1 s_T>`.
- Unknown arrival introduces a global-false-alarm timing-search penalty governed by the matched-filter scan covariance rather than ADC sample count; this mechanism is established adjacent detection theory.
- In the controlled equal-eventual-SNR family, faster temporal response accumulates evidence sooner but shortens timing correlation length. Under the **defined scanning protocol**, these effects can reverse the fast/slow detection ranking.
- The constructed task surface has the exact dimensionless form

```math
T_D(\alpha,\beta,L;\tau,\rho_0)
=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

For two members with `tau_f<tau_s`, `r=tau_s/tau_f`, and `ell=L/tau_s`, the task boundary is

```math
B_r(\ell;\rho_0,\alpha,\beta)
=X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)=0.
```

Under the Step-12 continuity/extreme-value assumptions:

- at `L=0`, the fast detector reaches the required decision first;
- approaching the fast detector's feasibility boundary, its detection time diverges while the slow detector remains feasible;
- therefore at least one finite fast-to-slow crossover exists;
- slow-only feasibility is possible;
- fast-only feasibility is excluded in this equal-eventual-SNR scaled family;
- no crossover uniqueness is claimed.

**Scope:** this is a protocol/task result, not a universal detector ordering and not a claim that faster detectors are generally worse.

---

## Paper architecture now fixed

Full architecture: `PAPER_ARCHITECTURE_TASK_REVERSAL.md`.

Working title:

> **Task-Dependent Ordering of Photodetectors with Equal Asymptotic Sensitivity**

The main paper should contain only:

1. prior-art framing and the actual task question;
2. the controlled equal-eventual-SNR family;
3. the exact dimensionless detection-time surface;
4. the task-boundary/crossover theorem and feasibility partition;
5. physical interpretation and limitations.

The central paper equation is

```math
T_D=\tau X_D(\rho_0,\alpha,\beta,L/\tau),
```

and the novelty-bearing object, if a deeper audit supports it, is only the complete synthesis

```text
equal eventual matched-filter SNR
+ different detector time scales
+ fixed physical unknown-arrival interval
+ global false-alarm requirement
+ finite-time evidence accumulation
+ template-dependent timing-search correlation
-> explicit fast/slow detection-time boundary and reversal.
```

The main paper should use at most three figures: competing evidence/search scales, the dimensionless task surface, and the fast/slow task-regime diagram.

Do **not** put Pickands/Palm/Rice/high-band endpoint closure machinery in the main narrative.

---

## Prior-art audit disposition

Focused audit: `PRIOR_ART_AUDIT_DETECTOR_TASK_REVERSAL.md`.

### Established prior art / not novelty targets

- Jones 1960: pulse/energy detectivity from frequency-dependent detector sensitivity; scalar-`D*` insufficiency for arbitrary pulses is not new.
- Sensitivity-speed and detectivity-bandwidth comparisons are established; `D* x bandwidth`-type metrics already exist.
- Unknown-arrival/location matched-filter searches incur correlated global-false-alarm penalties; template correlation/effective trial rate is not a new detection-theory mechanism.
- All-pass magnitude preservation with altered phase/dispersion is standard systems theory.

### Possible synthesis contribution — novelty still open

No direct match was found in the focused audit for the complete equal-eventual-SNR photodetector task-reversal construction. Disposition remains:

```text
POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.
```

The adjacent radar, sonar, astronomy, gravitational-wave, sequential-detection, and optical-receiver literatures are large. A deeper citation-network/patent audit is required before novelty language.

---

## Technical mathematical companion — Steps 13–49

Steps 13–49 remain valuable as a robustness/stress-test record but are moved out of the main detector narrative.

Important surviving corrections/results include:

- **FAILED NUMERICAL ESTIMATE:** Step-13 rough-grid crossover `ell~49` invalid; hard-window scan is locally Brownian-like.
- Rice's apparent upper switch near `kappa_f~130` is **INVALIDATED**; Palm preserves only the lower switch near `21.7 +/- .3`.
- **INVALIDATED INTERMEDIATE:** rough/smoothed coupling coefficient `.8131`; corrected `.8906480701 sqrt(chi/zeta)`.
- **INVALIDATED NUMERICAL INTERPRETATION:** raw tiny-chi Step-27 values were grid biased.
- Crossing moments fail from micro-upcrossings; finite-amplitude excursion clusters replace them.
- Step 39 finds `R=N_a/N_tan~1.56`; finite-u correction is not a small-amplitude remainder.
- Step 40 gives Cameron-Martin exact-event threshold translation.
- Step 41 replaces empirical q interpolation with analytic Gaussian-process control.
- **INVALIDATED NUMERICAL VALUE:** Step-35 tiny-q pair RMS `~5.4e-5`; corrected asymptotic `~2.69e-5`.
- Step 44 gives a genuine pointwise finite-grid 95% bound `P_FA/alpha<.999957771`, but with only `.00004223 alpha` margin.
- Step 46 identifies missed between-sample maxima as the dominant continuum-grid error; the five-event numerical coefficient is only sign/scale consistent, not precisely validated.
- Step 47 gives exact pure-alpha1 discrete Pickands correction.
- Step 48 finds mixed finite-u grid-transfer residual only `O(1e-5)` relative to an `O(9e-4)` loss.
- Step 49 evaluates exact finite-window covariance directly and finds the same grid-loss scale; higher-order covariance does not cancel it at order `1e-4`.

**HARD-STOP remains active:** do not reopen this branch unless external review identifies a decision-relevant gap.

---

## Active next phase

Stay inside **Paper A**.

The next logical action is to draft, from `PAPER_ARCHITECTURE_TASK_REVERSAL.md`:

1. the central theorem/proposition in publication-style language;
2. the abstract;
3. the opening two pages/Introduction and controlled-family setup;
4. with established ingredients cited as prior art and all novelty/scope restrictions explicit.

### Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can the central theorem, abstract, and opening two pages now be drafted in publication-style language from the fixed architecture, without reintroducing the mathematical companion into the main narrative?

---

## Scope boundary

Do not claim: faster universally better/worse; a universal scalar replacement for `D*`; `D* x bandwidth` as a new metric; unknown-arrival search penalties as new; the scanning protocol universally optimal; crossover uniqueness; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 values as continuum truth; Step-34 fully formal theorem; Step-36 uniform hazard theorem; `R~1`; numerical covariance constants interval-certified; `L0=.02` optimal; Step-44 as a continuum certificate; Step-46 coefficient precisely verified; Step-47 canonical ratio as exact finite-u false-alarm ratio; Step-48/49 Monte Carlo intervals as distribution-free theorem-level; `X=7.16` mathematically optimal; no re-entrant pocket for all task parameters; novelty.