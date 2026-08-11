# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Fourteen logical steps completed. Step 14 introduces a true finite accessible measurement bandwidth, rejects the naive idea that any invertible low-pass automatically regularizes optimal detection, proves that genuine finite information bandwidth removes the Step-13 covariance cusp, and shows that the fast/slow task-regime boundary survives in a similarity-preserving finite-bandwidth family. No universal replacement metric and no novelty claim.

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
16. `experiments/01-equal-dstar-different-speed/numerics/correlated_scan_mc.py`

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
- **COUNTEREXAMPLE** — construction sufficient to disprove an implication.
- **CONDITIONAL** — true only under listed assumptions.
- **REFINEMENT** — sharpens a prior statement without erasing it.
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

`M` is not digital sample count in a continuous scan.

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

Therefore the finite scan is locally Brownian-like / mean-square nondifferentiable in ideal white noise, explaining slow grid convergence. The full-template limit is smooth, so the limits do not commute.

### Step 14 — finite accessible bandwidth regularization

**REJECTED SHORTCUT:** appending a noiseless invertible common low-pass does not necessarily reduce optimal-detection information bandwidth because whitening cancels the common magnitude where the transfer is nonzero.

Use instead a true accessible angular-frequency band

```math
|\omega|\le\Omega_B.
```

Then the finite-duration timing covariance satisfies

```math
\boxed{
-r_{t,B}''(0)
=\int\omega^2W_{t,B}(\omega)d\omega
\le\Omega_B^2.
}
```

The Step-13 cusp disappears and the finite scan is mean-square differentiable. Rice-type continuous-time crossing methods become admissible again.

For the similarity-preserving regularized family define

```math
\kappa=\Omega_B\tau
```

and hold `kappa` fixed while normalizing all members to equal **band-limited eventual SNR** `rho_0`.

Then

```math
\boxed{
\mathcal T_{D,\kappa}
=\tau X_{D,\kappa}(\rho_0,\alpha,\beta,L/\tau).
}
```

The regularized fast/slow boundary retains the exact form

```math
\boxed{
X_{D,\kappa}(r\ell)-rX_{D,\kappa}(\ell)=0.
}
```

The normalized full-template threshold remains nondecreasing with search length, so both-feasible / slow-only / neither-feasible ordering and exclusion of fast-only feasibility survive. Under the same continuity/mixing conditions, at least one fast-to-slow crossover survives.

**REFINEMENT:** Step-13 roughness is a property of the infinite-white-bandwidth hard-window idealization, not the source of the task-regime reversal.

**OPEN:** if the same physical bandwidth is imposed on both unequal-`tau` detectors, then `kappa_f != kappa_s`; the simple similarity ordering no longer follows automatically.

---

## 5. Current frontier

The preferred next numerical object is the smooth finite-bandwidth threshold

```math
\Gamma_\kappa(x,\ell,\alpha).
```

Unlike Step 13's rough process, finite `kappa` permits controlled grid convergence and an independent Rice/extreme-value cross-check.

The next task is to compute `Gamma_kappa`, solve the regularized crossover, and study how it moves as `kappa` increases toward the rough white-noise limit.

---

## 6. Scope boundary

Do not claim:

- faster is universally better or worse;
- a universal speed-detectivity tradeoff or scalar replacement for `D*`;
- the diagnostic `ell~49` crossover is real;
- any arbitrary invertible low-pass is a true information-bandwidth limit;
- fixed physical bandwidth has the same ordering as fixed dimensionless `kappa`;
- crossover uniqueness;
- true-alignment crossing equals exact global rejection/localization;
- novelty.

Unknown amplitudes/phases, signal-dependent shot noise, sequential stopping, nonlinear response, saturation, dead time, nonstationarity, and globally optimal non-Gaussian decisions remain untouched.

---

## 7. Single next question — DO NOT ANSWER UNTIL PROMPTED

> For finite dimensionless bandwidth `kappa`, can the now-smooth Gaussian timing scan be simulated with controlled grid convergence and Rice/extreme-value cross-checks to obtain a trustworthy `Gamma_kappa(x,ell,alpha)` and fast/slow crossover, and how does that crossover move as `kappa` is increased toward the rough white-noise limit?
