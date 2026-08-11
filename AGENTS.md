# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Sixteen logical steps completed. Step 16 introduces an exact Palm/upcrossing rare-event identity and low-variance importance sampler for the smooth finite-`kappa` timing scan, validates `alpha=10^-6` without brute-force Monte Carlo, and finds a rare-event-corrected crossover `ell_s ~=0.5721 +/-0.001` for the stated `kappa=8`, `r=1.2`, `rho_0=6.2`, `beta=0.90` validation task. Rice predicts `0.57144`, only about `0.12%` lower. No universal replacement metric and no novelty claim.

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
17. `experiments/01-equal-dstar-different-speed/RARE_EVENT_UPCROSSING_STEP.md`
18. `experiments/01-equal-dstar-different-speed/numerics/correlated_scan_mc.py`
19. `experiments/01-equal-dstar-different-speed/numerics/regularized_scan_mc.py`
20. `experiments/01-equal-dstar-different-speed/numerics/upcrossing_importance_sampling.py`

The repository follows the physics rather than a predetermined criticism of `D*`. Preserve assumptions, counterexamples, cancellations, negative results, rejected shortcuts, failed numerical estimates, numerical validations, refinements, invalidations, and unresolved branches.

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
- **FAILED NUMERICAL ESTIMATE** — a computed value did not survive convergence/validation and must never be reused as a result.
- **NUMERICAL VALIDATION** — a numerical method/result survived the explicitly stated convergence/cross-check tests within its stated scope.
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

### Step 01 — scalar reference `D*` insufficiency
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

### Step 12 — exact task-regime boundary
For `r=tau_s/tau_f>1` and `ell=L/tau_s`, the exact preference boundary is

```math
X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)=0.
```

**REJECTED SHORTCUT:** asymptotic-margin equality is not the detection-time boundary.

Task space has both-feasible, slow-only, and neither-feasible regions; fast-only feasibility is impossible under equal eventual SNR. At least one finite crossover exists under standard continuity/extreme-value conditions; uniqueness remains open.

### Step 13 — direct correlated-scan prototype and continuum obstruction
A direct FFT moving-average Monte Carlo simulates the grid-sampled correlated finite-duration Gaussian scan without independent-trials replacement.

**FAILED NUMERICAL ESTIMATE:** diagnostic crossover values around `ell~49` are not continuum-converged and must never be quoted as results.

The finite hard-window covariance has

```math
\boxed{
a_x=-R_x'(0^+)=\frac{2x^2e^{-2x}}{\eta(x)}}
```

and `R_x(y)=1-a_x|y|+...`, so the ideal-white-noise finite scan is locally Brownian-like / nondifferentiable.

### Step 14 — finite information bandwidth
**REJECTED SHORTCUT:** an invertible noiseless common low-pass does not necessarily regularize optimal information bandwidth because whitening can cancel it.

A genuine finite accessible information band makes the timing spectrum have finite second moment and removes the Step-13 cusp.

For fixed dimensionless `kappa`, the time-scaled task surface and fast/slow boundary survive.

### Step 15 — smooth-band numerical validation
Use

```math
J_{x,\kappa}(\nu)=|H_x(\nu)|^2e^{-(\nu/\kappa)^2}.
```

Direct correlated FFT simulation is stable under practical grid refinement and agrees with Rice/Euler-characteristic predictions at the validation points.

The Rice trend study for `rho_0=5`, `r=1.2`, `alpha=0.01`, `beta=0.90` gives decreasing crossover `ell` as `kappa` increases. Those values are approximate trends, not exact phase boundaries.

### Step 16 — rare-event Palm/upcrossing method

#### Grid-event mixture
For an `n`-point correlated timing grid, conditioning a uniformly chosen point above `u` gives the exact grid-event importance weight

```math
w=nQ(u)/K_u.
```

This is efficient but still estimates a discrete grid maximum.

#### Exact continuous identity
For a differentiable stationary Gaussian scan,

```math
\lambda_u=E[N_u^+]
=L\frac{\sigma}{2\pi}e^{-u^2/2},
```

and under the upcrossing Palm law

```math
\boxed{
P_{FA}(u)
=Q(u)+\lambda_u
E_\uparrow\!\left[
\frac{1_{\{z(0)\le u\}}}{N_u^+}
\right].
}
```

Therefore

```math
\boxed{P_{FA}(u)\le Q(u)+\lambda_u.}
```

**DERIVED / REFINEMENT:** the first-order Rice/EC formula is an upper bound in the one-dimensional differentiable setting. Its error comes from multiple upcrossings and endpoint/upcrossing overlap.

The Palm slope is

```math
z'(T)\sim\mathrm{Rayleigh}(\sigma).
```

#### `alpha=10^-6` validation
The Step-15 `rho_0=5` task is infeasible even at known time because the required margin is about `6.035`, so use

```text
rho_0=6.2
r=1.2
alpha=1e-6
beta=0.90
kappa=8.
```

Rice predicts

```text
ell_s^Rice ~=0.571441752
x_s ~=4.473364397
x_f ~=5.368037276
u_s ~=4.895464822
u_f ~=4.913100340.
```

At those thresholds, `5000` Palm paths give

```text
slow P_FA ~=9.9949037e-7, SE ~=2.04e-10
fast P_FA ~=9.9922753e-7, SE ~=2.70e-10.
```

Multiple-upcrossing and endpoint-overlap fractions are only about `10^-3`. Rice overestimates the exact false-alarm probability by less than `0.1%`, with threshold corrections of order `10^-4`.

Propagating those corrections and re-evaluating near the switch gives

```math
\boxed{\ell_\times^{Palm}\approx0.5721}
```

with conservative numerical summary

```text
ell_cross^Palm ~=0.5721 +/-0.001.
```

Rice gives `0.57144`, only `~0.12%` lower.

**NUMERICAL VALIDATION / CONDITIONAL:** at `alpha=10^-6` in this smooth `kappa=8` validation task, high excursions are overwhelmingly isolated, making Rice nearly exact and the Palm estimator extremely efficient.

Implementation: `numerics/upcrossing_importance_sampling.py`.

---

## 5. Current frontier

The rare-event threshold is now numerically accessible without brute-force sampling. The next question is whether the small Palm correction and the fast/slow crossover admit a simple high-threshold asymptotic description as `kappa`, `r`, `rho_0`, and `beta` vary.

---

## 6. Scope boundary

Do not claim:

- faster is universally better or worse;
- a universal speed-detectivity tradeoff or scalar replacement for `D*`;
- the Step-13 `ell~49` diagnostic crossover is real;
- arbitrary invertible low-pass filtering is a true information-band limitation;
- the Step-15 Gaussian weighting is a unique physical readout law;
- Rice is always accurate to `0.1%`;
- the Step-16 crossover applies outside the stated `rho_0=6.2`, `r=1.2`, `beta=0.90`, `kappa=8`, `alpha=1e-6` validation task;
- crossover uniqueness;
- fixed physical bandwidth has the same ordering as fixed dimensionless bandwidth;
- true-alignment crossing equals exact global rejection/localization;
- novelty.

Unknown amplitudes/phases, signal-dependent shot noise, sequential stopping, nonlinear response, saturation, dead time, nonstationarity, and globally optimal non-Gaussian decisions remain untouched.

---

## 7. Single next question — DO NOT ANSWER UNTIL PROMPTED

> Does the near-exact Rice/Palm behavior persist as the dimensionless timing bandwidth `kappa` and speed ratio `r` are varied, and can the high-threshold limit yield a simple asymptotic law for the fast/slow crossover?
