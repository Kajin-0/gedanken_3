# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-12 20:31 EDT  
**Status:** mathematical closure branch stopped after 49 logical steps; detector-facing prior-art audit completed. **NOVELTY NOT ESTABLISHED.** The focused audit finds direct prior art for pulsed/energy detectivity, sensitivity–bandwidth tradeoffs, and unknown-arrival matched-filter false-alarm penalties. No direct match was found for the complete photodetector construction in which two channels have equal eventual matched-filter SNR yet reverse finite-time detection ranking under one global-false-alarm unknown-arrival scan. That construction is therefore only a **possible synthesis contribution**, not a novelty claim.

Read next:
1. `PRIOR_ART_AUDIT_DETECTOR_TASK_REVERSAL.md`
2. `EXACT_COVARIANCE_GRID_TRANSFER_STOP_STEP.md`
3. `PROGRESS_LOG.md`

---

## Detector/detection-theory core — Steps 01–12

The surviving core is:

- A scalar reference `D*` does not determine arbitrary temporal-signal performance.
- Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation stationary-Gaussian maximum-SNR problem.
- Finite windows make phase/time placement operationally relevant even when magnitude response is identical; an all-pass construction removes the trivial pure-delay objection.
- Finite-time optimal SNR is `rho_T^2=<s_T,C_T^-1 s_T>`.
- Unknown arrival introduces a global-false-alarm timing-search penalty governed by the matched-filter scan covariance rather than ADC sample count.
- In the controlled equal-eventual-SNR family, faster temporal response accumulates evidence sooner but shortens timing correlation length. Under the **defined scanning protocol**, these effects can reverse the fast/slow detection ranking.
- The constructed task surface has the dimensionless form `T_D=tau X_D(rho0,alpha,beta,L/tau)`.

**Scope:** this is a protocol/task result, not a universal detector ordering and not a claim that faster detectors are generally worse.

---

## Mathematical companion — Steps 13–49

The later branch exists to test whether the ranking-reversal witness survives continuous-time false-alarm control. It is now hard-stopped.

Key surviving corrections/results:

- **FAILED NUMERICAL ESTIMATE:** Step-13 rough-grid crossover `ell~49` invalid; hard-window scan is locally Brownian-like.
- Genuine finite information bandwidth removes the cusp; an invertible noiseless low-pass does not because optimal whitening cancels it.
- Rice's apparent upper switch near `kappa_f~130` is **INVALIDATED**; Palm preserves only the lower switch near `21.7 +/- .3`.
- **INVALIDATED INTERMEDIATE:** rough/smoothed coupling coefficient `.8131`; corrected `.8906480701 sqrt(chi/zeta)`.
- **INVALIDATED NUMERICAL INTERPRETATION:** raw tiny-chi Step-27 values were grid biased.
- Crossing moments fail at high bandwidth because one physical excursion contains many micro-upcrossings; finite-amplitude excursion clusters replace them.
- Step 39 finds `R=N_a/N_tan~1.56`; the finite-u correction is not a small-amplitude remainder.
- Step 40 gives Cameron-Martin exact-event threshold translation.
- Step 41 replaces empirical q interpolation with analytic Gaussian-process control.
- **INVALIDATED NUMERICAL VALUE:** Step-35 tiny-q pair RMS `~5.4e-5`; corrected asymptotic value `~2.69e-5`.
- Raw inverse-duration Palm concentration is formally bounded but useless; duration truncation at `L0=.02` makes a finite-sample endpoint bound possible.
- Step 44 gives a true pointwise finite-grid 95% upper bound `P_FA/alpha<.999957771`, but with only `.00004223 alpha` margin.
- Witness retuning cannot robustly absorb continuum error: `X=7.50` gains fast `~.001575 alpha` while `X=7.70` pushes the slow branch near feasibility.
- Step 46 isolates the grid error as missed between-sample maxima; **WORDING CORRECTION:** the five-event nested-grid result supports sign/scale consistency only, not precise coefficient verification.
- Step 47 gives the exact pure-alpha1 discrete Pickands correction `H_1^delta=nu(sqrt(2delta))`.
- Step 48 shows the finite-u mixed Brownian-parabola transfer changes the finite-level discretization ratio only at `O(1e-5)` relative to an `O(9e-4)` loss.
- Step 49 evaluates the **exact finite-window covariance** directly. Physical `dt=.001` versus `dt/32`, pooled `6000` paired paths:

```text
H_exact^Delta          .5528146649
H_exact^(Delta/32)     .5532776622
relative loss          8.3682629e-4
paired SE              6.8953e-6
approx 95% interval    [8.2331e-4,8.5034e-4]
pure-alpha1 loss       8.3657896e-4
exact-minus-pure       +2.47e-7 +/-6.90e-6
```

**HARD-STOP TRIGGERED:** the remaining publication-grade mapping from exact-covariance spectral intensity to the exact finite-search false-alarm event is no longer proportionate to the detector question. Do not resume this proof chain unless external review identifies a decision-relevant gap.

---

## Prior-art audit disposition

Focused audit file: `PRIOR_ART_AUDIT_DETECTOR_TASK_REVERSAL.md`.

### Established prior art / do not claim novelty

1. **Scalar D* is insufficient for arbitrary pulse detection.** R. Clark Jones treated pulse/energy detectivity using frequency-dependent `D*(f)` in 1960.
2. **Sensitivity-speed and detectivity-bandwidth tradeoffs are established.** Garcia & Dereniak reported a `D*f*` product in 1990; a 2026 Nature Communications paper explicitly defines `USBL = D* x bandwidth`.
3. **Unknown-arrival/location matched filtering incurs a search false-alarm penalty.** Adjacent signal-detection literature shows global false-alarm thresholds depend on the peak process, template autocorrelation, and an effective sampling/trial rate.
4. **All-pass phase manipulation at fixed magnitude is standard systems theory.** The repo's finite-window photodetector counterexample may be pedagogically useful, but its stand-alone novelty confidence is low.

### Possible contribution — novelty still open

No direct hit was found for the complete construction:

```text
equal eventual matched-filter SNR
+ different detector temporal scales
+ fixed unknown-arrival interval
+ global false-alarm scan
+ finite-time evidence accumulation
+ template-dependent timing-search complexity
→ explicit fast/slow detection-time ranking reversal.
```

Disposition:

```text
POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.
```

The neighboring radar, sonar, astronomy, gravitational-wave, sequential-detection, and optical-receiver literatures are large. Absence of a direct hit in this focused audit is not proof of novelty.

---

## Active next phase

Do **not** create Step 50 of the mathematical closure chain.

The next logical action is detector-facing consolidation:

1. compress Steps 01–12 into a short theorem/counterexample narrative;
2. make the novelty burden rest only on the specific equal-eventual-SNR ranking-reversal construction;
3. cite Jones/modern detector characterization and matched-filter search literature as established ingredients;
4. move Steps 13–49 to a technical companion/appendix track.

### Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can the detector-facing result be compressed into a short paper architecture whose central theorem is the protocol-specific equal-eventual-SNR ranking reversal, while all established ingredients and Steps 13–49 are moved out of the main narrative?

---

## Scope boundary

Do not claim: faster universally better/worse; a universal scalar replacement for `D*`; `D* x bandwidth` as a new metric; unknown-arrival search penalties as new; the scanning protocol universally optimal; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 values as continuum truth; Step-34 fully formal theorem; Step-36 uniform hazard theorem; `R~1`; numerical covariance constants interval-certified; `L0=.02` optimal; Step-44 as a continuum certificate; Step-46 coefficient precisely verified; Step-47 canonical ratio as exact finite-u false-alarm ratio; Step-48/49 Monte Carlo intervals as distribution-free theorem-level; `X=7.16` mathematically optimal; no re-entrant pocket for all task parameters; novelty.