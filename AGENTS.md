# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Thirteen logical steps completed. Step 13 directly simulates the correlated finite-duration Gaussian timing scan without an independent-trials approximation, rejects nonconverged coarse crossover values, and derives the exact covariance cusp that makes the finite hard-window scan locally Brownian-like / nondifferentiable in ideal white noise. The current frontier is how to compute or regularize the continuous-time supremum in a controlled way. No universal replacement metric and no novelty claim.

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
15. `experiments/01-equal-dstar-different-speed/numerics/correlated_scan_mc.py`

The repository follows the physics rather than a predetermined criticism of `D*`. Preserve assumptions, counterexamples, cancellations, negative results, rejected shortcuts, failed numerical estimates, refinements, invalidations, and unresolved branches.

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
- **COUNTEREXAMPLE** — physically consistent construction sufficient to disprove an implication.
- **CONDITIONAL** — true only under listed assumptions.
- **REFINEMENT** — sharpens a prior conditional statement.
- **NEGATIVE RESULT** — a natural candidate effect was tested and shown absent under the stated model.
- **REJECTED SHORTCUT** — a tempting inference/formula was shown not to answer the actual question.
- **FAILED NUMERICAL ESTIMATE** — a computed value did not survive convergence/validation and must not be reused as a result.
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

### Step 01
Equal reference scalar `D*` does not determine arbitrary temporal-signal SNR. Signal/noise filtering can cancel, so no universal `fast is better` claim.

### Step 02

```math
\rho_\infty^2
=\int |P|^2|G|^2/S_n\,df
=\frac1A\int|P|^2D^{*2}\,df.
```

Complete magnitude `D*(f)` is sufficient for this restricted full-observation known-waveform problem.

### Step 03
**NEGATIVE RESULT:** unknown timing alone does not break the ideal stationary-Gaussian full-observation equivalence for equal complete `D*(f)`. Finite truncation can.

### Step 04
A causal all-pass construction removes the pure-delay loophole: equal magnitude `D*(f)` and equal infinite-time SNR can still yield different latency-compensated finite-window SNR.

### Step 05

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
\qquad
\eta(t)=\rho_t^2/\rho_\infty^2.
```

### Step 06

```math
P_D(t;\alpha)=\Phi[\rho_t-\Phi^{-1}(1-\alpha)].
```

### Step 07

```math
\gamma_{M,\alpha}=\Phi^{-1}[(1-\alpha)^{1/M}].
```

`M` is not digital sample count in a continuous timing scan.

### Step 08
Full-template timing covariance is the autocorrelation of the noise-whitened template. Sample rate alone does not set timing trials. Smooth-process Rice theory applies only when the second spectral moment exists.

### Step 09
The actual finite scan uses `q_t=C_t^-1 s_t` and its own timing covariance.

**REJECTED SHORTCUT:** do not mix finite-window `eta(t)` with full-template `f_rms` as one exact statistic.

A controlled equal-eventual-SNR time-scaled family permits a conditional cross-detector reversal: faster SNR accumulation can be outweighed by larger unknown-time search burden.

### Step 10

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t>0:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

Task-level detection-time surface; not a detector scalar.

### Step 11
For the scaled family,

```math
\mathcal T_D
=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

**NEGATIVE RESULT:** no finite interior `t_opt`; use all available data. Ranking reversal is cross-detector, not poor filter duration.

### Step 12
For `r=tau_s/tau_f>1` and `ell=L/tau_s`, the exact preference boundary is

```math
X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)=0.
```

**REJECTED SHORTCUT:** asymptotic-margin equality is not the detection-time boundary.

Task space has both-feasible, slow-only, and neither-feasible regions; fast-only feasibility is impossible under equal eventual SNR. At least one finite fast-to-slow crossover exists under standard continuity/extreme-value conditions; uniqueness remains open.

### Step 13 — numerical correlated-scan prototype and continuum obstruction

The dimensionless finite white-noise scan is

```math
z_x(u)=\frac1{\sqrt{E_x}}\int_0^x v e^{-v}\,dW(u+v),
```

with exact covariance `R_x`.

A direct FFT moving-average Monte Carlo simulates the **correlated grid-sampled process**; it does not use effective independent trials.

Method-validation parameters:

```text
rho_0=5
r=1.2
alpha=0.01
beta=0.90
```

Broad Step-12 behavior is reproduced, but the apparent crossover moves under grid refinement.

Diagnostic only:

```text
delta=0.05   -> ell_s ~48.5–49.0
delta=0.025  -> ell_s ~49.25–49.5
delta=0.0125 -> fast still favored at ell_s=49.5 in that run
```

**FAILED NUMERICAL ESTIMATE:** `ell_x~49` is not a valid continuous-time result.

The reason is exact. For every finite hard cutoff,

```math
\boxed{
a_x=-R_x'(0^+)=\frac{2x^2e^{-2x}}{\eta(x)}}
```

and

```math
R_x(y)=1-a_x|y|+O(y^2).
```

Thus

```math
E[(z(u+h)-z(u))^2]\sim2a_x|h|,
```

so the finite scan is locally Brownian-like / mean-square nondifferentiable in ideal white noise. Grid maxima therefore converge slowly to the continuous supremum. Near the feasibility edge, small threshold errors cause large detection-time/crossover errors.

The full-template limit is smooth, so the finite-hard-window and `x->infinity` limits do not commute.

---

## 5. Current frontier

The analytic task-regime structure survives. The unresolved numerical object is the **continuous supremum quantile**

```math
\Gamma(x,\ell,\alpha)
```

for the locally rough finite-window Gaussian scan.

A fixed timing grid is not yet a controlled continuum solver near the crossover.

The next task should compare two controlled routes:

1. a mathematically justified adaptive/between-grid treatment for the cusp process;
2. physical finite readout/noise bandwidth, which regularizes the scan and introduces an additional dimensionless bandwidth parameter.

Then test whether the fast/slow boundary survives and whether the result converges as the regularization is removed.

---

## 6. Scope boundary

Do not claim:

- faster is universally better or worse;
- a universal speed-detectivity tradeoff or scalar replacement for `D*`;
- the diagnostic `ell~49` crossover is real;
- crossover uniqueness;
- fixed-grid Monte Carlo has solved the continuous supremum;
- full-template Rice theory exactly solves the finite hard-window scan;
- all detector families have monotone filter-duration margins;
- true-alignment crossing equals exact global rejection/localization;
- novelty.

Unknown amplitudes/phases, signal-dependent shot noise, sequential stopping, nonlinear response, saturation, dead time, nonstationarity, and globally optimal non-Gaussian decisions remain untouched.

---

## 7. Single next question — DO NOT ANSWER UNTIL PROMPTED

> What is the cleanest controlled way to recover the continuous-time finite-window supremum — by a justified adaptive/between-grid treatment of the cusp process or by introducing physical finite readout bandwidth — and does the fast/slow task boundary survive that regularization?
