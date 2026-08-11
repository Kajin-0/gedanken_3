# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 14:18 EDT:** This log remains intentionally compact while preserving every scientific milestone, correction, negative result, rejected shortcut, failed numerical estimate, numerical validation, and stopping point. Full derivations live in dedicated step files.

---

## 2026-08-11 11:21 EDT — Scalar D* insufficiency

Equal reference `D*` with `tau_A=1 ns`, `tau_B=1 s` was tested in a physically allowed first-order + additive-output-noise model. The same 1 Hz tone gave `SNR_A/SNR_B ~6.36`.

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

Full derivation: `FINITE_WINDOW_PHASE_STEP.md`.

---

## 2026-08-11 12:09 EDT — Latency-compensated dispersion

A stable causal all-pass factor preserved complete magnitude `D*(f)` and total infinite-time SNR while changing finite-window SNR after constant alignment.

**COUNTEREXAMPLE:** finite-window insufficiency is not merely a pure-delay artifact.

Full derivation: `LATENCY_COMPENSATED_DISPERSION_STEP.md`.

---

## 2026-08-11 12:18 EDT — Exact finite-time SNR

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
\qquad
\eta(t)=\rho_t^2/\rho_\infty^2.
```

Eventual detectability and rate of access to it are distinct.

Full derivation: `SNR_ACCUMULATION_STEP.md`.

---

## 2026-08-11 12:30 EDT — Detection probability by deadline

```math
P_D(t;\alpha)=\Phi[\rho_t-\Phi^{-1}(1-\alpha)].
```

Equal eventual SNR can coexist with radically unequal early-deadline detection probability.

Full derivation: `DEADLINE_DETECTION_PROBABILITY_STEP.md`.

---

## 2026-08-11 12:38 EDT — Independent-slot unknown-time search

```math
\gamma_{M,\alpha}=\Phi^{-1}[(1-\alpha)^{1/M}].
```

Timing uncertainty consumes SNR margin through a global threshold.

**WARNING:** `M` is not digital sample count in a real continuous scan.

Full derivation: `UNKNOWN_TIME_SEARCH_STEP.md`.

---

## 2026-08-11 12:47 EDT — Continuous-time timing-search covariance

Derived

```math
r(\Delta)=\int W(f)e^{i2\pi f\Delta}df
```

from the noise-whitened template. When the second moment exists, `f_rms` controls local covariance curvature and Rice upcrossing density.

**REFINEMENT:** sample rate alone does not set timing trials. Identical complete `D*(f)` gives identical full-observation search covariance for the same waveform.

Full derivation: `CONTINUOUS_TIME_SEARCH_CORRELATION_STEP.md`.

---

## 2026-08-11 13:01 EDT — Finite-deadline correction and ranking reversal

The actual finite scan must use `q_t=C_t^-1s_t` and its own timing covariance.

**REJECTED SHORTCUT:** do not combine finite-window `eta(t)` with full-template `f_rms` as one exact statistic.

Constructed the equal-eventual-SNR family

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
\qquad
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
```

Faster members accumulate more finite-time SNR but face a larger fixed-physical-`L` timing-search burden. Under standard finite-to-full convergence, cross-detector ranking reverses.

Full derivation: `SEARCH_PENALTY_REVERSAL_STEP.md`.

---

## 2026-08-11 13:18 EDT — Task-level detection-time surface

Defined

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t>0:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

This is task-level, not a detector scalar.

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

Pointwise covariance ordering plus Slepian comparison makes the global search threshold nonincreasing with filter duration while SNR rises strictly.

**NEGATIVE RESULT:** no finite interior `t_opt`; use all data allowed by the deadline.

Full derivation: `DIMENSIONLESS_DETECTION_SURFACE_STEP.md`.

---

## 2026-08-11 13:39 EDT — Fast/slow task-regime boundary

For `r=tau_s/tau_f>1` and `ell=L/tau_s`, the exact preference boundary is

```math
X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)=0.
```

**REJECTED SHORTCUT:** asymptotic-margin equality is not the minimum-decision-time boundary.

Task space partitions into both-feasible, slow-only, and neither-feasible regions; fast-only feasibility is impossible under equal eventual SNR. Physical timing-uncertainty feasibility scales as `L_crit=tau ell_crit`. At least one finite fast-to-slow crossover exists under standard continuity/extreme-value conditions; uniqueness remains open.

Full derivation: `TASK_REGIME_BOUNDARY_STEP.md`.

---

## 2026-08-11 13:50 EDT — Direct correlated-scan numerical prototype

Implemented direct FFT moving-average Monte Carlo for the exact **grid-sampled correlated** finite-duration Gaussian scan. No independent-trials approximation was used.

Validation task:

```text
rho_0=5
r=1.2
alpha=0.01
beta=0.90
```

Broad fast-to-slow behavior appeared, but the apparent crossover moved under grid refinement.

**FAILED NUMERICAL ESTIMATE:** diagnostic crossover values near `ell~49` are not continuum-converged and must not be quoted.

Exact cause:

```math
\boxed{
a_x=-R_x'(0^+)=\frac{2x^2e^{-2x}}{\eta(x)}}
```

and

```math
R_x(y)=1-a_x|y|+O(y^2),
```

so

```math
E[(z(u+h)-z(u))^2]\sim2a_x|h|.
```

The finite hard-window scan is locally Brownian-like / nondifferentiable in ideal white noise, causing slow grid-to-continuum convergence.

Full derivation: `NUMERICAL_SCAN_CONVERGENCE_STEP.md`.  
Prototype: `numerics/correlated_scan_mc.py`.

---

## 2026-08-11 14:10 EDT — True finite-bandwidth regularization

**REJECTED SHORTCUT:** merely appending a noiseless invertible common low-pass does not necessarily regularize optimal detection because whitening can undo it.

For a true finite information band, the timing-spectrum second moment is finite and

```math
-r_{t,B}''(0)=\int\omega^2W_{t,B}(\omega)d\omega.
```

The Step-13 cusp disappears and the scan becomes mean-square differentiable.

For the similarity-preserving family with `kappa=Omega_B tau`, equal band-limited eventual SNR, and fixed `kappa`, the detection-time scaling and fast/slow boundary survive:

```math
\mathcal T_{D,\kappa}
=\tau X_{D,\kappa}(\rho_0,\alpha,\beta,L/\tau),
```

```math
X_{D,\kappa}(r\ell)-rX_{D,\kappa}(\ell)=0.
```

**REFINEMENT:** the Step-13 roughness is not the source of the regime reversal.

Full derivation: `FINITE_BANDWIDTH_REGULARIZATION_STEP.md`.

---

## 2026-08-11 14:18 EDT — Smooth-band numerical validation

### Explicit numerical regularizer

Choose the controlled Gaussian information weighting

```math
J_{x,\kappa}(\nu)
=|H_x(\nu)|^2e^{-(\nu/\kappa)^2},
```

with

```math
H_x(\nu)
=\frac{1-e^{-(1+i\nu)x}[1+(1+i\nu)x]}{(1+i\nu)^2}.
```

This is an explicit high-frequency information/processing penalty, not an invertible common low-pass and not claimed as a unique physical readout model.

### Controlled correlated simulation

Implemented periodic FFT spectral synthesis of the stationary correlated Gaussian scan in

```text
numerics/regularized_scan_mc.py
```

with timing-grid, period, bootstrap-tail, and Rice/EC checks.

Validation task:

```text
rho_0=5
r=1.2
alpha=0.01
beta=0.90
kappa=8
```

Rice-based provisional crossover point:

```text
ell_s ~=54.7489
slow x ~=3.78390, Gamma_Rice ~=3.66373
fast x ~=4.54068, ell_f ~=65.6986, Gamma_Rice ~=3.70181
```

Direct 99th-percentile thresholds:

```text
slow delta=0.05, 15000 paths:
    3.6401 [bootstrap95 3.5967,3.6821]
slow delta=0.025, 12000 paths:
    3.6470 [bootstrap95 3.5924,3.7012]

fast delta=0.05, 15000 paths:
    3.7041 [bootstrap95 3.6480,3.7530]
fast delta=0.025, 12000 paths:
    3.6649 [bootstrap95 3.6325,3.7017]
```

**NUMERICAL VALIDATION:** the two grid resolutions overlap within Monte Carlo tail uncertainty and are compatible with the continuous Rice predictions. The systematic upward threshold drift from Step 13 is absent. Doubling the synthesis period changes the threshold by less than the current tail uncertainty.

### Bandwidth trend — approximate only

Using Rice/Euler-characteristic theory as a trend estimator for the same operating point:

```text
kappa      ell_cross^Rice
2             75.56
4             61.58
8             54.75
16            51.43
32            49.89
```

**CONDITIONAL TREND:** in this regularized model, increasing accessible high-frequency timing information moves the fast-to-slow switch to smaller `L/tau_s`.

These values are not exact Monte Carlo phase boundaries and do not rehabilitate the rejected Step-13 `ell~49` number.

Full derivation: `FINITE_BANDWIDTH_NUMERICAL_STEP.md`.  
Code: `numerics/regularized_scan_mc.py`.

### Next question, held open

Can a rare-event / high-threshold numerical method be built for the smooth regularized scan so that `Gamma_kappa` and the crossover can be solved directly at `alpha~10^-6`, and how different is that result from Rice theory?
