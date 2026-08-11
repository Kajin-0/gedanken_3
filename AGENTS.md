# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Fifteen logical steps completed. Step 15 validates a smooth finite-information-band correlated Gaussian timing scan numerically: practical timing-grid refinement is stable within Monte Carlo uncertainty and agrees with Rice/Euler-characteristic continuous-time predictions at the validation points. A Rice-based trend study shows the fast/slow crossover shifting to smaller normalized timing uncertainty as accessible high-frequency timing information increases. Those crossover values are approximate, not exact phase-boundary results. No universal replacement metric and no novelty claim.

Read this file first, then:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. `experiments/01-equal-dstar-different-speed/MATCHED_FILTER_SNR_STEP.md`
4. `experiments/01-equal-dstar-different-speed/FINITE_WINDOW_PHASE_STEP.md`
5. `experiments/01-equal-dstar-different-speed/LATENCY_COMPENSATED_DISPERSION_STEP.md`
6. `experiments/01-equal-dstar-different-speed/SNR_ACCUMULATION_STEP.md`
7. `experiments/01-equal-dstar-different-speed/DEADLINE_DETECTION_PROBABILITY_STEP.md`
8. `experiments/01-equal-dstar-different-speed/UNKNOWN_TIME_SEARCH_STEP.md`
9. `experiments/01-equal-dstar-different-speed/CONTINUOUS_TIME_SEARCH_CORRELATION_STEP.md`
10. `experiments/01-equal-dstar-different-speed/SEARCH_PENALTY_REVERSAL_STEP.md`
11. `experiments/01-equal-dstar-different-speed/DETECTION_TIME_SURFACE_STEP.md`
12. `experiments/01-equal-dstar-different-speed/DIMENSIONLESS_DETECTION_SURFACE_STEP.md`
13. `experiments/01-equal-dstar-different-speed/TASK_REGIME_BOUNDARY_STEP.md`
14. `experiments/01-equal-dstar-different-speed/NUMERICAL_SCAN_CONVERGENCE_STEP.md`
15. `experiments/01-equal-dstar-different-speed/FINITE_BANDWIDTH_REGULARIZATION_STEP.md`
16. `experiments/01-equal-dstar-different-speed/FINITE_BANDWIDTH_NUMERICAL_STEP.md`
17. `experiments/01-equal-dstar-different-speed/numerics/correlated_scan_mc.py`
18. `experiments/01-equal-dstar-different-speed/numerics/regularized_scan_mc.py`

The repository follows the physics rather than a predetermined criticism of `D*`. Preserve assumptions, counterexamples, cancellations, negative results, rejected shortcuts, failed numerical estimates, refinements, validation limits, invalidations, and unresolved branches.

---

## 1. Mandatory repository protocol

Before every material write:

1. fetch live `main` / current target;
2. inspect intervening changes when needed;
3. fetch the current blob SHA before replacing an existing file;
4. never overwrite stale state;
5. preserve failed/corrected branches and explain why they changed;
6. make narrow edits or explicit compact consolidations;
7. update `CURRENT_STATE.md` whenever the scientific frontier changes;
8. append or consolidate a timestamped entry in `PROGRESS_LOG.md` for consequential work.

**Live `main` overrides snapshots and recovery notes.**

---

## 2. Epistemic labels

Use explicitly where useful:

- **DEFINED** — convention/model definition.
- **ASSUMED** — idealization introduced for the thought experiment.
- **DERIVED** — follows mathematically from stated assumptions.
- **COUNTEREXAMPLE** — construction sufficient to disprove an implication.
- **CONDITIONAL** — true only under listed assumptions.
- **REFINEMENT** — sharpens a prior statement without erasing it.
- **NEGATIVE RESULT** — a natural candidate effect was tested and shown absent under the stated model.
- **REJECTED SHORTCUT** — a tempting inference/formula was shown not to answer the actual question.
- **FAILED NUMERICAL ESTIMATE** — a computed value did not survive convergence/validation and must not be reused as a result.
- **NUMERICAL VALIDATION** — a numerical method/result survived the explicitly stated convergence/cross-check tests, within reported uncertainty and scope.
- **OPEN** — not established.
- **INVALIDATED** — shown false under its stated generality.
- **NON-CLAIM** — deliberately not asserted.

Do not use `novel`, `universal`, `fundamental`, `first`, etc. without a separate prior-art audit.

---

## 3. Original question

Two hypothetical detectors satisfy

```math
D_A^*=D_B^*
```

but initially have

```math
\tau_A=1\ \mathrm{ns},
\qquad
\tau_B=1\ \mathrm{s}.
```

Does equal conventional specific detectivity imply equal ability to detect an arbitrary optical signal?

---

## 4. Surviving chain

### Step 01 — reference scalar D* insufficiency
Equal reference `D*` does not guarantee equal SNR for arbitrary temporal signals. Signal/noise filtering can cancel; no universal `fast is better` claim.

### Step 02 — full-observation known-waveform SNR

```math
\rho_\infty^2
=\int |P|^2|G|^2/S_n\,df
=\frac1A\int|P|^2D^{*2}\,df.
```

Complete magnitude `D*(f)` is sufficient for this restricted full-observation problem.

### Step 03 — unknown timing negative result; finite-window failure
**NEGATIVE RESULT:** identical complete `D*(f)` gives identical stationary-Gaussian full-observation timing-search statistics. Finite truncation can break equivalence because magnitude `D*(f)` discards phase/placement.

### Step 04 — pure-delay loophole removed
A stable causal all-pass factor preserves complete magnitude `D*(f)` and total infinite-time SNR while changing finite-window SNR after latency compensation.

### Step 05 — finite-time SNR

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
\qquad
\eta(t)=\rho_t^2/\rho_\infty^2.
```

### Step 06 — known-time Gaussian decision

```math
P_D(t;\alpha)=\Phi[\rho_t-\Phi^{-1}(1-\alpha)].
```

### Step 07 — independent-slot unknown-time penalty

```math
\gamma_{M,\alpha}=\Phi^{-1}[(1-\alpha)^{1/M}].
```

`M` is not digital sample count in a continuous timing scan.

### Step 08 — continuous-time full-template covariance
Timing-search covariance is the autocorrelation of the noise-whitened template. When the second moment exists, `f_rms` controls local covariance curvature and Rice upcrossing density. Sample rate alone does not set timing trials.

### Step 09 — finite-deadline scan and conditional reversal
The actual finite scan uses `q_t=C_t^-1s_t` and its own covariance.

**REJECTED SHORTCUT:** finite-window `eta(t)` and full-template `f_rms` cannot be combined as one exact finite-deadline statistic.

The controlled equal-eventual-SNR time-scaled family can exhibit cross-detector ranking reversal: faster SNR accumulation can be outweighed by a larger unknown-time search burden.

### Step 10 — task-level detection-time surface

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t>0:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

Task-level surface, not a detector scalar.

### Step 11 — dimensionless collapse and no finite interior filter optimum

```math
\mathcal T_D
=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

**NEGATIVE RESULT:** no finite interior `t_opt` in this family; use all available data. Ranking reversal is cross-detector, not poor filter duration.

### Step 12 — task-regime boundary
For `r=tau_s/tau_f>1` and `ell=L/tau_s`, the exact preference boundary is

```math
X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)=0.
```

**REJECTED SHORTCUT:** asymptotic-margin equality is not the detection-time boundary.

Task space has both-feasible, slow-only, and neither-feasible regions; fast-only feasibility is impossible under equal eventual SNR. At least one finite crossover exists under standard continuity/extreme-value conditions; uniqueness remains open.

### Step 13 — direct correlated-scan prototype and continuum obstruction
A direct FFT moving-average Monte Carlo simulates the grid-sampled correlated finite-duration Gaussian scan with no independent-trials approximation.

Broad Step-12 behavior appears, but the apparent crossover moves under timing-grid refinement.

**FAILED NUMERICAL ESTIMATE:** diagnostic crossover values around `ell~49` are not continuum-converged and must never be quoted as results.

The exact finite hard-window covariance has

```math
\boxed{
a_x=-R_x'(0^+)=\frac{2x^2e^{-2x}}{\eta(x)}}
```

and

```math
R_x(y)=1-a_x|y|+O(y^2).
```

Therefore the finite scan is locally Brownian-like / mean-square nondifferentiable in ideal white noise, explaining slow grid convergence.

### Step 14 — finite accessible bandwidth regularization

**REJECTED SHORTCUT:** appending a noiseless invertible common low-pass does not necessarily reduce optimal-detection information bandwidth because whitening cancels the common magnitude where the transfer is nonzero.

A genuine information-band limitation makes the timing spectrum have finite second moment and removes the Step-13 cusp.

For a similarity-preserving finite-bandwidth family with fixed dimensionless `kappa`, equal band-limited eventual SNR, and time scaling,

```math
\mathcal T_{D,\kappa}
=\tau X_{D,\kappa}(\rho_0,\alpha,\beta,L/\tau),
```

and the fast/slow boundary retains

```math
X_{D,\kappa}(r\ell)-rX_{D,\kappa}(\ell)=0.
```

**REFINEMENT:** the Step-13 cusp is not the source of the task-regime reversal.

### Step 15 — smooth-band numerical validation

Choose the explicit Gaussian information weighting

```math
J_{x,\kappa}(\nu)=|H_x(\nu)|^2e^{-(\nu/\kappa)^2}.
```

This is a controlled high-frequency information/processing penalty, not an invertible common low-pass and not a unique physical readout law.

A periodic FFT spectral-synthesis Monte Carlo directly simulates the correlated stationary Gaussian scan. It is implemented in

```text
numerics/regularized_scan_mc.py
```

and cross-checked against the differentiable-process Rice/Euler-characteristic threshold.

Validation parameters:

```text
rho_0=5
r=1.2
alpha=0.01
beta=0.90
kappa=8
```

At the Rice-based provisional crossover:

```text
slow: x~3.78390, ell~54.7489, Gamma_Rice~3.66373
fast: x~4.54068, ell~65.6986, Gamma_Rice~3.70181
```

Direct 99th-percentile thresholds at `delta=0.05` and `0.025` overlap within bootstrap tail uncertainty and are compatible with the Rice predictions. Period doubling changes the threshold by less than current Monte Carlo uncertainty.

**NUMERICAL VALIDATION:** the systematic grid-to-continuum drift that invalidated Step 13 is absent in the smooth finite-`kappa` validation case.

Rice/EC trend study for the same operating point:

```text
kappa      ell_cross^Rice
2             75.56
4             61.58
8             54.75
16            51.43
32            49.89
```

**CONDITIONAL TREND:** restoring more high-frequency timing information moves the fast-to-slow switch to smaller `L/tau_s` for this tested regularization/model/parameter set.

These crossover numbers are approximate Rice-based trends, not exact Monte Carlo phase boundaries. They do not rehabilitate the rejected Step-13 `ell~49` estimate.

---

## 5. Current frontier

Moderate-tail finite-`kappa` numerics are now locally validated. The next unresolved object is the rare-event threshold

```math
\Gamma_\kappa(x,\ell,\alpha)
```

for detector-relevant `alpha`, especially `alpha~10^-6`, where ordinary Monte Carlo is inefficient.

The next task is to develop or adapt a rare-event/high-threshold method, validate it against direct Monte Carlo where overlap is possible, and compare the resulting crossover against Rice theory.

---

## 6. Scope boundary

Do not claim:

- faster is universally better or worse;
- a universal speed-detectivity tradeoff or scalar replacement for `D*`;
- the diagnostic Step-13 `ell~49` crossover is real;
- any arbitrary invertible low-pass is a true information-bandwidth limit;
- the Step-15 Gaussian information weighting is the unique physical readout model;
- the Rice crossover table is an exact phase boundary;
- fixed physical bandwidth has the same ordering as fixed dimensionless bandwidth;
- crossover uniqueness;
- true-alignment crossing equals exact global rejection/localization;
- novelty.

Unknown amplitudes/phases, signal-dependent shot noise, sequential stopping, nonlinear response, saturation, dead time, nonstationarity, and globally optimal non-Gaussian decisions remain untouched.

---

## 7. Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can a rare-event / high-threshold numerical method be built for the smooth regularized scan so that `Gamma_kappa(x,ell,alpha)` and the fast/slow crossover can be solved directly at detector-relevant false-alarm probabilities such as `alpha=10^-6`, and how different is that result from the Rice prediction?
