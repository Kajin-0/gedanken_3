# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Seventeen logical steps completed. Step 17 derives a compact endpoint-retaining Palm/Rice crossover law, proves that Rice accuracy is not uniform as finite-window `kappa -> infinity`, and obtains the extreme-speed-ratio asymptote `r ell_cross -> ell_crit,kappa`, or physically `L_cross -> tau_fast ell_crit,kappa`. No universal replacement metric and no novelty claim.

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
18. `experiments/01-equal-dstar-different-speed/HIGH_THRESHOLD_CROSSOVER_ASYMPTOTICS_STEP.md`
19. `experiments/01-equal-dstar-different-speed/numerics/correlated_scan_mc.py`
20. `experiments/01-equal-dstar-different-speed/numerics/regularized_scan_mc.py`
21. `experiments/01-equal-dstar-different-speed/numerics/upcrossing_importance_sampling.py`
22. `experiments/01-equal-dstar-different-speed/numerics/asymptotic_crossover.py`

The repository follows the physics rather than a predetermined criticism of `D*`. Preserve assumptions, counterexamples, cancellations, negative results, rejected shortcuts, failed numerical estimates, numerical validations, asymptotic limits, refinements, invalidations, and unresolved branches.

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
- **NUMERICAL VALIDATION** — a numerical method/result survived the explicitly stated convergence/cross-check tests within scope.
- **ASYMPTOTIC** — derived in a controlled limiting regime; do not silently apply outside that limit.
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
Equal reference scalar `D*` does not determine arbitrary temporal-signal SNR. Signal/noise filtering can cancel; no universal `fast is better` claim.

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
Continuous timing-search covariance is the autocorrelation of the noise-whitened template. When the second spectral moment exists, `f_rms` controls local curvature and Rice upcrossing density. Sample rate alone does not set timing trials.

### Step 09
The actual finite scan uses `q_t=C_t^-1s_t` and its own covariance.

**REJECTED SHORTCUT:** finite-window `eta(t)` and full-template `f_rms` cannot be combined as one exact finite-deadline statistic.

The controlled equal-eventual-SNR time-scaled family can exhibit cross-detector ranking reversal.

### Step 10

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t>0:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

Task-level surface, not a detector scalar.

### Step 11

```math
\mathcal T_D
=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

**NEGATIVE RESULT:** no finite interior `t_opt` in the controlled family; use all available data. Ranking reversal is cross-detector, not poor filter duration.

### Step 12
For `r=tau_s/tau_f>1` and `ell=L/tau_s`, the exact preference boundary is

```math
X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)=0.
```

**REJECTED SHORTCUT:** asymptotic-margin equality is not the detection-time boundary.

Task space has both-feasible, slow-only, and neither-feasible regions; fast-only feasibility is impossible under equal eventual SNR. At least one finite crossover exists under standard conditions; uniqueness remains open.

### Step 13
A direct correlated finite-scan Monte Carlo reproduces broad behavior but the apparent crossover moves under grid refinement.

**FAILED NUMERICAL ESTIMATE:** diagnostic `ell~49` values are not continuum-converged and must never be quoted.

The exact finite hard-window covariance has

```math
\boxed{a_x=-R_x'(0^+)=2x^2e^{-2x}/\eta(x)}
```

and `R_x(y)=1-a_x|y|+...`, so the ideal-white-noise finite scan is locally Brownian-like / nondifferentiable.

### Step 14
**REJECTED SHORTCUT:** an invertible noiseless common low-pass does not necessarily reduce optimal information bandwidth because whitening can cancel it.

A genuine finite information band removes the cusp. For fixed dimensionless `kappa`, the scaled task boundary survives.

### Step 15
Use the smooth Gaussian information weighting

```math
J_{x,\kappa}(\nu)=|H_x(\nu)|^2e^{-(\nu/\kappa)^2}.
```

Direct correlated simulation has controlled grid behavior and agrees with Rice/EC at moderate validation points. The Rice crossover shifts to smaller normalized timing uncertainty as `kappa` increases over the tested range; these are approximate trends only.

### Step 16
For the differentiable scan,

```math
\boxed{
P_{FA}(u)
=Q(u)+\lambda_u
E_\uparrow\!\left[
\frac{1_{\{z(0)\le u\}}}{N_u^+}
\right],
}
```

with

```math
\lambda_u=L\frac{\sigma}{2\pi}e^{-u^2/2}.
```

Thus Rice/EC is an upper bound; its error is multiple excursions plus endpoint overlap.

For `rho_0=6.2`, `r=1.2`, `alpha=1e-6`, `beta=0.90`, `kappa=8`, Palm gives `ell_cross ~=0.5721 +/-0.001`; Rice gives `0.57144`.

### Step 17
At a crossover, define

```math
u_s=\rho_0\mathcal R_\kappa(x)-\Phi^{-1}(\beta),
```

```math
u_f=\rho_0\mathcal R_\kappa(rx)-\Phi^{-1}(\beta).
```

The exact Palm-corrected smooth-process boundary is

```math
\boxed{
\frac{[\alpha-Q(u_f)]e^{u_f^2/2}}{\sigma_f C_f}
=r
\frac{[\alpha-Q(u_s)]e^{u_s^2/2}}{\sigma_s C_s}.
}
```

For isolated excursions `C_s,C_f~1`, the endpoint-retaining Rice law is

```math
\boxed{
u_f^2-u_s^2
\approx2\ln\!\left[
r\frac{\sigma_f}{\sigma_s}
\frac{\alpha-Q(u_s)}{\alpha-Q(u_f)}
\right].}
```

**REJECTED SHORTCUT:** small `alpha` does not justify dropping `Q(u)`. In the Step-16 task the endpoint term is roughly half the false-alarm budget.

For finite hard-window `x`,

```math
\boxed{
\sigma_\kappa^2(x)
\sim\frac{a_x}{\sqrt\pi}\kappa
\qquad(\kappa\to\infty),
}
```

so Rice upcrossing counts diverge as `sqrt(kappa)` and the Palm factor must shrink as at least `O(kappa^-1/2)`. **Rice accuracy is not uniform into the rough limit.**

For the extreme speed-ratio branch define

```math
\Gamma_{\infty,\kappa}(\ell_{crit,\kappa},\alpha)
=\rho_0-\Phi^{-1}(\beta).
```

Then

```math
\boxed{r\ell_\times\to\ell_{crit,\kappa},}
```

and physically

```math
\boxed{L_\times\to\tau_f\ell_{crit,\kappa}.}
```

The slow time constant drops out at leading order. Rice finite-`r` solutions are already within about `0.1%` by `r=2` and about `5e-4%` by `r=3` for representative `kappa` values.

At the Step-16 validation parameters with `kappa=8`, `ell_crit^Rice ~=0.723222`; for the original `tau_f=1 ns`, `tau_s=1 s` ratio this gives the **illustrative-only** scale `L_cross~0.723 ns`, with Palm indicating only a sub-percent correction.

**REFINEMENT:** the limits do not commute. Fixed finite `r` followed by `kappa->infinity` recreates rough finite-window behavior; `r->infinity` first forces the fast detector onto its smooth full template, making the subsequent bandwidth-removal limit regular.

---

## 5. Current frontier

The co-scaled finite-bandwidth branch is now analytically compressed: it has an exact Palm correction structure, a practical high-threshold crossover equation, a proof of nonuniform Rice behavior in the rough limit, and a simple extreme-speed-ratio law.

The leading unresolved physical branch is the **same physical electronics bandwidth** applied to both unequal-`tau` detectors. Then

```math
\kappa_f=\Omega_B\tau_f,
\qquad
\kappa_s=\Omega_B\tau_s
```

are different, so the similarity ordering used in Steps 14–17 no longer applies automatically.

---

## 6. Scope boundary

Do not claim:

- faster is universally better or worse;
- a universal speed-detectivity tradeoff or scalar replacement for `D*`;
- the Step-13 `ell~49` diagnostic crossover is real;
- arbitrary invertible low-pass filtering is a true information-band limitation;
- the Gaussian information weighting is a unique physical readout law;
- Rice is always accurate to `0.1%`;
- the large-`r` law implies the illustrative `0.723 ns` is a real-detector prediction;
- crossover uniqueness;
- fixed physical bandwidth has the same ordering as fixed dimensionless bandwidth;
- true-alignment crossing equals exact global rejection/localization;
- novelty.

Unknown amplitudes/phases, signal-dependent shot noise, sequential stopping, nonlinear response, saturation, dead time, nonstationarity, and globally optimal non-Gaussian decisions remain untouched.

---

## 7. Single next question — DO NOT ANSWER UNTIL PROMPTED

> If both detectors are connected to the **same physical readout bandwidth** rather than the same dimensionless `kappa`, does the large-`r` crossover law survive, and can the electronics bandwidth itself change or optimize which detector wins?
