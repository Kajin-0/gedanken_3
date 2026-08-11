# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 13:50 EDT:** This log is intentionally compact but preserves every scientific milestone, correction, negative result, rejected shortcut, failed numerical route, and stopping point. Full derivations live in dedicated step files.

---

## 2026-08-11 11:21 EDT — Scalar `D*` insufficiency

Equal reference `D*` with `tau_A=1 ns`, `tau_B=1 s` was tested in a first-order + additive-output-noise model. The same 1 Hz tone gave `SNR_A/SNR_B ~6.36`.

**COUNTEREXAMPLE:** equal scalar reference `D*` does not guarantee equal SNR for arbitrary temporal signals.

**QUALIFICATION:** signal/noise filtering can cancel; do not infer `fast is always better`.

---

## 2026-08-11 11:32 EDT — Known-waveform full-observation SNR

Derived

```math
\rho_\infty^2
=\int |P|^2|G|^2/S_n\,df
=\frac1A\int|P|^2D^{*2}\,df.
```

Complete magnitude `D*(f)` is sufficient for this restricted full-observation problem.

Full derivation: `MATCHED_FILTER_SNR_STEP.md`.

---

## 2026-08-11 12:02 EDT — Unknown timing negative result; finite truncation

**NEGATIVE RESULT:** under stationary Gaussian full observation, equal complete `D*(f)` gives equal ideal unknown-arrival matched-filter search statistics.

Finite truncation can still distinguish detectors because magnitude `D*(f)` discards temporal phase/placement.

**QUALIFICATION:** compensating known pure delay removes that specific example.

Full derivation: `FINITE_WINDOW_PHASE_STEP.md`.

---

## 2026-08-11 12:09 EDT — Latency-compensated dispersion

A stable causal all-pass factor preserved complete magnitude `D*(f)` and total infinite-time SNR while changing finite-window SNR after arbitrary constant alignment.

**COUNTEREXAMPLE:** finite-window insufficiency is not merely a pure-delay artifact.

Full derivation: `LATENCY_COMPENSATED_DISPERSION_STEP.md`.

---

## 2026-08-11 12:18 EDT — Exact finite-time SNR

Derived

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
\qquad
\eta(t)=\rho_t^2/\rho_\infty^2.
```

Eventual detectability and rate of access to it are distinct.

Full derivation: `SNR_ACCUMULATION_STEP.md`.

---

## 2026-08-11 12:30 EDT — Detection probability by deadline

For the simple known-time Gaussian test,

```math
P_D(t;\alpha)=\Phi[\rho_t-\Phi^{-1}(1-\alpha)].
```

Equal eventual SNR can coexist with radically unequal early-deadline detection probability.

Full derivation: `DEADLINE_DETECTION_PROBABILITY_STEP.md`.

---

## 2026-08-11 12:38 EDT — Independent-slot unknown-time search

For `M` independent timing hypotheses,

```math
\gamma_{M,\alpha}=\Phi^{-1}[(1-\alpha)^{1/M}].
```

Timing uncertainty consumes SNR margin through a global threshold.

**WARNING:** `M` is not digital sample count in a real continuous scan.

Full derivation: `UNKNOWN_TIME_SEARCH_STEP.md`.

---

## 2026-08-11 12:47 EDT — Continuous-time full-template search correlation

Derived scan covariance from the noise-whitened template,

```math
r(\Delta)=\int W(f)e^{i2\pi f\Delta}df.
```

When the second moment exists, `f_rms` controls local covariance curvature and Rice upcrossing density.

**REFINEMENT:** digital sample rate alone does not set timing trials. Identical complete `D*(f)` gives identical full-observation search covariance for the same waveform.

**REGULARITY WARNING:** the ideal abrupt exponential has divergent second moment in ideal white noise.

Full derivation: `CONTINUOUS_TIME_SEARCH_CORRELATION_STEP.md`.

---

## 2026-08-11 13:01 EDT — Finite-deadline correction and ranking reversal

The actual finite scan must use

```math
q_t=C_t^{-1}s_t
```

and its own covariance.

**REJECTED / INVALID SHORTCUT:** finite-window `eta(t)` and full-template `f_rms` cannot be mixed into one exact finite-deadline formula.

Constructed the stable causal equal-eventual-SNR family

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
\qquad
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
```

Faster members accumulate more finite-time SNR but face a larger fixed-physical-`L` timing-search burden. Under standard finite-to-full threshold convergence, cross-detector ranking reverses.

Full derivation: `SEARCH_PENALTY_REVERSAL_STEP.md`.

---

## 2026-08-11 13:18 EDT — Task-level detection-time surface

Defined

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t>0:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

This is task-level, not a detector scalar. Generic finite interior filter optimum left open.

Full derivation: `DETECTION_TIME_SURFACE_STEP.md`.

---

## 2026-08-11 13:28 EDT — Dimensionless collapse and filter-duration negative result

For the controlled family,

```math
x=t/\tau,
\qquad
\ell=L/\tau,
```

```math
\mathcal T_D=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

Pointwise covariance ordering plus Slepian comparison makes the global search threshold nonincreasing with filter duration while SNR increases strictly.

**NEGATIVE RESULT:** no finite interior `t_opt` in this family; use all data allowed by the deadline.

Full derivation: `DIMENSIONLESS_DETECTION_SURFACE_STEP.md`.

---

## 2026-08-11 13:39 EDT — Fast/slow task-regime boundary

For

```math
r=\tau_s/\tau_f>1,
\qquad
\ell=L/\tau_s,
```

the exact preference boundary is

```math
X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)=0.
```

**REJECTED SHORTCUT:** asymptotic-margin equality is not the minimum-decision-time boundary.

Task space partitions into both-feasible, slow-only, and neither-feasible regions; fast-only feasibility is impossible under equal eventual SNR. Physical timing-uncertainty feasibility obeys `L_crit=tau ell_crit`.

Under standard continuity/extreme-value conditions, at least one finite fast-to-slow crossover must occur. Uniqueness and exact location remain open.

Full derivation: `TASK_REGIME_BOUNDARY_STEP.md`.

---

## 2026-08-11 13:50 EDT — Direct correlated-scan numerical prototype

### Numerical route attempted

Implemented a direct FFT moving-average Monte Carlo for the exact **grid-sampled correlated** finite-duration Gaussian scan generated by

```math
h_x(v)=v e^{-v}1_{[0,x]}(v).
```

No independent-trials approximation was used.

A deliberately moderate method-validation task used

```text
rho_0=5
r=1.2
alpha=0.01
beta=0.90
```

before attempting the original `1 ns` versus `1 s` / `alpha=1e-6` extreme.

### What worked

The direct correlated simulation reproduced the broad Step-12 behavior:

```text
small timing uncertainty -> fast wins
larger timing uncertainty -> fast advantage shrinks
near fast feasibility edge -> fast required delay rises sharply
```

### What failed

The apparent crossover was not stable under timing-grid refinement.

Diagnostic values only:

```text
delta=0.05   -> apparent ell_s crossover around 48.5–49.0
delta=0.025  -> apparent ell_s crossover around 49.25–49.5
delta=0.0125 -> fast still favored at ell_s=49.5 in that sampled run
```

Path counts also differed, so this is not a controlled extrapolation sequence.

**REJECTED PRELIMINARY RESULT:** do not quote `ell_x~49` as the continuous-time crossover.

### Why it failed — exact covariance cusp

For finite hard-window covariance `R_x`, differentiation at zero gives

```math
R_x'(0^+)=-\frac{h_x(x)^2}{2E_x},
\qquad
E_x=\eta(x)/4.
```

Hence

```math
\boxed{
a_x=-R_x'(0^+)=\frac{2x^2e^{-2x}}{\eta(x)}}
```

and

```math
\boxed{R_x(y)=1-a_x|y|+O(y^2).}
```

Therefore

```math
\boxed{E[(z(u+h)-z(u))^2]\sim2a_x|h|.}
```

The finite hard-window scan is locally Brownian-like / mean-square nondifferentiable for every finite `x` in ideal white noise. A fixed time grid therefore misses between-grid maxima with slow continuum convergence.

The full-template limit is smooth, so finite-hard-window and `x->infinity` limits do not commute. This explains why Step-08 smooth Rice theory cannot simply repair the finite-window numerical scan.

**NUMERICAL CONCLUSION:** broad regime structure is robust, but no trustworthy continuous-time crossover or phase diagram is available yet from fixed-grid Monte Carlo.

Full derivation: `NUMERICAL_SCAN_CONVERGENCE_STEP.md`.  
Reproducible prototype: `numerics/correlated_scan_mc.py`.

### Next question, held open

What is the cleanest controlled way to recover the continuous finite-window supremum: a justified between-grid/adaptive treatment of the cusp process, or a physical finite readout bandwidth that regularizes it; and does the fast/slow task boundary survive?
