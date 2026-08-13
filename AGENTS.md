# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** detector-facing consolidation after a forty-nine-step mathematical closure branch. **MATHEMATICAL CLOSURE HARD-STOPPED. PRIOR-ART AUDIT COMPLETED. NOVELTY NOT ESTABLISHED.** Step 49 is the final default proof step. A focused detector/detection-theory literature audit now finds direct prior art for pulse/energy detectivity from frequency-dependent `D*(f)`, sensitivity–bandwidth joint metrics, and unknown-arrival matched-filter false-alarm penalties controlled by template correlation. No direct hit was found for the complete equal-eventual-SNR photodetector construction in which different temporal scales reverse finite-time detection ranking under one global-false-alarm unknown-arrival scan. That construction is only a **POSSIBLE SYNTHESIS CONTRIBUTION**, not a novelty claim. Do not restart the Gaussian-extremes closure chain or invent a new scalar metric by default.

Read first:
1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PRIOR_ART_AUDIT_DETECTOR_TASK_REVERSAL.md`
3. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
4. final closure step: `experiments/01-equal-dstar-different-speed/EXACT_COVARIANCE_GRID_TRANSFER_STOP_STEP.md`
5. final closure helper: `experiments/01-equal-dstar-different-speed/numerics/exact_covariance_grid_transfer.py`

Live `main` overrides chat summaries or stale notes.

---

## Mandatory repository protocol
Before material writes: fetch live target and exact blob SHA; never overwrite stale state; preserve failed/corrected paths. `CURRENT_STATE.md`, `PROGRESS_LOG.md`, and this file must move whenever the research frontier changes.

Useful epistemic labels include: **DEFINED, ASSUMED, DERIVED, CONDITIONAL, COUNTEREXAMPLE, REFINEMENT, NEGATIVE RESULT, REJECTED SHORTCUT, FAILED NUMERICAL ESTIMATE, NUMERICAL VALIDATION, PARTIAL CERTIFICATE, RIGOROUS FINITE-GRID STATISTICAL CERTIFICATE, PAIRED NESTED-GRID DIAGNOSTIC, EXACT CANONICAL FINITE-GRID CORRECTION, EXACT CELLWISE BRIDGE DECOMPOSITION, PAIRED FINITE-LEVEL TRANSFER INTERVAL, PAIRED EXACT-COVARIANCE TRANSFER INTERVAL, HARD-GATE PASSED, HARD-STOP TRIGGERED, PRIOR-ART AUDIT, POSSIBLE SYNTHESIS CONTRIBUTION, NOVELTY NOT ESTABLISHED, INVALIDATED, ASYMPTOTIC, OPEN, NON-CLAIM.**

Do not use `novel`, `universal`, `fundamental`, `first`, or equivalent novelty language without a deeper audit that actually supports it. `Universal` remains allowed only for the explicitly model-reduced canonical crossover function.

---

## Detector-facing core — Steps 01–12

The surviving detector result is:

- Scalar reference `D*` does not determine arbitrary temporal-signal performance.
- Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation stationary-Gaussian problem.
- Finite windows make phase/time placement operationally relevant even with identical magnitude response; an all-pass construction removes the trivial pure-delay objection.
- Finite-time optimal SNR is `rho_T^2=<s_T,C_T^-1 s_T>`.
- Unknown arrival introduces a global-false-alarm timing search governed by matched-filter scan covariance rather than raw ADC sample count.
- In the controlled equal-eventual-SNR family, faster response accumulates evidence sooner but shortens timing correlation length. Under the **defined scanning protocol**, those effects can reverse the fast/slow detection ranking.
- The constructed task surface obeys `T_D=tau X_D(rho0,alpha,beta,L/tau)`.

**Scope:** this is a task/protocol result. Do not state that faster detectors are generally worse or that the scan is universally optimal.

---

## Mathematical companion — Steps 13–49

Keep these as technical companion/appendix material unless an external reviewer identifies a decision-relevant gap.

Key surviving corrections and closure results:

- **FAILED NUMERICAL ESTIMATE:** Step-13 rough-grid crossover `ell~49` invalid; hard-window scan is locally Brownian-like.
- Genuine finite information bandwidth removes the cusp; an invertible noiseless low-pass does not because optimal whitening cancels it.
- Rice's apparent upper switch near `kappa_f~130` is **INVALIDATED**; Palm preserves only the lower switch near `21.7 +/- .3`.
- **INVALIDATED INTERMEDIATE:** coupling coefficient `.8131`; corrected `.8906480701 sqrt(chi/zeta)`.
- **INVALIDATED NUMERICAL INTERPRETATION:** raw tiny-chi Step-27 values were grid biased.
- Crossing moments fail from micro-upcrossings; finite-amplitude excursion clusters replace them.
- Step 39 finds `R=N_a/N_tan~1.56`; finite-u correction is not a small-amplitude remainder.
- Step 40 gives Cameron-Martin exact-event threshold translation.
- Step 41 replaces empirical q interpolation with analytic Gaussian-process control.
- **INVALIDATED NUMERICAL VALUE:** Step-35 tiny-q pair RMS `~5.4e-5`; corrected asymptotic `~2.69e-5`.
- Duration truncation at `L0=.02` makes bounded-weight finite-sample concentration possible; Step 44 gives pointwise finite-grid 95% `P_FA/alpha<.999957771`, but only `.00004223 alpha` margin.
- Step 45 shows witness retuning trades one near-boundary problem for another.
- Step 46 isolates missed between-sample maxima as the dominant grid error. **WORDING CORRECTION:** the five-event paired result has ~47% relative SE and supports sign/scale consistency only, not precise coefficient validation.
- Step 47 gives exact pure-alpha1 discrete Pickands correction `H_1^delta=nu(sqrt(2delta))`.
- Step 48 gives mixed finite-u transfer only `O(1e-5)` relative to an `O(9e-4)` grid loss.
- Step 49 evaluates the exact finite-window covariance directly. Physical `dt=.001` versus `dt/32`, pooled `6000` paired paths:

```text
H_exact^Delta          .5528146649
H_exact^(Delta/32)     .5532776622
relative loss          8.3682629e-4
paired SE              6.8953e-6
approx 95% interval    [8.2331e-4,8.5034e-4]
pure-alpha1 loss       8.3657896e-4
exact-minus-pure       +2.47e-7 +/-6.90e-6
```

**HARD-STOP TRIGGERED:** the remaining publication-grade mapping from exact-covariance spectral intensity to exact finite-search false-alarm probability is no longer proportionate to the detector question. Do not create Step 50 of this proof chain by default.

---

## Prior-art audit disposition

Full focused audit: `experiments/01-equal-dstar-different-speed/PRIOR_ART_AUDIT_DETECTOR_TASK_REVERSAL.md`.

### Established ingredients — not novelty targets

1. **Pulse/energy detection from frequency-dependent detectivity:** R. Clark Jones treated this directly in 1960. Scalar `D*` insufficiency for arbitrary pulses is therefore not new.
2. **Sensitivity–speed / detectivity–bandwidth comparison:** established in detector literature; `D* x bandwidth`-type metrics already exist. Do not propose a simple product as a new universal metric.
3. **Unknown-arrival matched-filter search penalty:** established adjacent detection theory; false-alarm rate/threshold depends on the correlated peak process, template autocorrelation, and effective trial rate rather than raw sample count.
4. **All-pass magnitude preservation with altered dispersion:** standard systems theory. The photodetector finite-window counterexample may be useful pedagogically, but stand-alone novelty confidence is low.

### Only plausible novelty-bearing object

Focused search found no direct match for the complete construction:

```text
equal eventual matched-filter SNR
+ different detector temporal scales
+ fixed unknown-arrival interval
+ global false-alarm scan
+ finite-time evidence accumulation
+ template-dependent timing-search correlation
→ explicit fast/slow detection-time ranking reversal.
```

Disposition:

```text
POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.
```

Absence of a direct hit is not proof of novelty. Adjacent radar, sonar, astronomy, gravitational-wave, sequential-detection, optical-receiver, and statistical decision literatures remain large. A deeper citation-network and patent audit would be needed before any novelty claim.

---

## Active next phase

Do **not** restart the Gaussian-extremes proof chain.

The next logical task is detector-facing consolidation:
1. compress Steps 01–12 into a short theorem/counterexample paper architecture;
2. place the novelty burden only on the complete equal-eventual-SNR ranking-reversal synthesis;
3. cite Jones, established detectivity–bandwidth work, and matched-filter search literature as prior art rather than rediscoveries;
4. move Steps 13–49 into technical companion/appendix material;
5. perform a deeper novelty audit only if the compressed result still looks publication-worthy.

### Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can the detector-facing result be compressed into a short paper architecture whose central theorem is the protocol-specific equal-eventual-SNR ranking reversal, with established ingredients cited as prior art and Steps 13–49 moved out of the main narrative?

---

## Scope boundary
Do not claim: faster universally better/worse; a universal scalar replacement for `D*`; `D* x bandwidth` as new; unknown-arrival matched-filter search penalty as new; scanning protocol universally optimal; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 values as continuum truth; Step-34 fully formal theorem; Step-36 uniform hazard theorem; `R~1`; numerical covariance constants interval-certified; `L0=.02` optimal; Step-44 as continuum certificate; Step-46 coefficient precisely verified; Step-47 canonical ratio as exact finite-u false-alarm ratio; Step-48/49 Monte Carlo intervals as distribution-free theorem-level results; `X=7.16` mathematically optimal; no re-entrant pocket for all task parameters; novelty.