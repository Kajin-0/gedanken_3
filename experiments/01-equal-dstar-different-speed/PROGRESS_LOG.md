# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 14:33 EDT:** This log is intentionally compact but preserves every scientific milestone, correction, negative result, rejected shortcut, failed numerical estimate, numerical validation, and stopping point. Full derivations live in the dedicated step files.

---

## 2026-08-11 11:21 EDT — Scalar `D*` insufficiency
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

**WARNING:** `M` is not digital sample count in a continuous scan.

Full derivation: `UNKNOWN_TIME_SEARCH_STEP.md`.

---

## 2026-08-11 12:47 EDT — Continuous-time timing-search covariance
Derived timing covariance from the noise-whitened template. When the second spectral moment exists, `f_rms` controls local covariance curvature and Rice upcrossing density.

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

Faster members accumulate more finite-time SNR but face a larger fixed-physical-`L` timing-search burden. Under standard finite-to-full convergence, cross-detector ranking can reverse.

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

Pointwise covariance ordering plus Slepian comparison makes the global search threshold nonincreasing with filter duration while SNR increases strictly.

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

Broad fast-to-slow behavior appeared, but the apparent crossover moved under timing-grid refinement.

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

so the finite hard-window scan is locally Brownian-like / mean-square nondifferentiable in ideal white noise.

Full derivation: `NUMERICAL_SCAN_CONVERGENCE_STEP.md`.  
Prototype: `numerics/correlated_scan_mc.py`.

---

## 2026-08-11 14:10 EDT — True finite-bandwidth regularization
**REJECTED SHORTCUT:** merely appending a noiseless invertible common low-pass does not necessarily regularize optimal detection because whitening can undo it.

A true finite information band makes the timing-spectrum second moment finite and removes the Step-13 cusp.

For fixed dimensionless `kappa=Omega_B tau` and equal band-limited eventual SNR,

```math
\mathcal T_{D,\kappa}
=\tau X_{D,\kappa}(\rho_0,\alpha,\beta,L/\tau),
```

and the fast/slow boundary survives.

**REFINEMENT:** the Step-13 roughness is not the source of the regime reversal.

Full derivation: `FINITE_BANDWIDTH_REGULARIZATION_STEP.md`.

---

## 2026-08-11 14:18 EDT — Smooth-band numerical validation
Use the controlled Gaussian information weighting

```math
J_{x,\kappa}(\nu)=|H_x(\nu)|^2e^{-(\nu/\kappa)^2}.
```

A periodic FFT spectral-synthesis Monte Carlo directly simulates the correlated stationary Gaussian scan in

```text
numerics/regularized_scan_mc.py
```

and is stable under practical timing-grid refinement for the validation points.

At `rho_0=5`, `r=1.2`, `alpha=0.01`, `beta=0.90`, Rice/EC gives the approximate trend

```text
kappa      ell_cross^Rice
2             75.56
4             61.58
8             54.75
16            51.43
32            49.89
```

**CONDITIONAL TREND:** more accessible high-frequency timing information moves the fast-to-slow switch to smaller `L/tau_s` in this tested model.

These are approximate Rice trends, not exact phase boundaries.

Full derivation: `FINITE_BANDWIDTH_NUMERICAL_STEP.md`.  
Code: `numerics/regularized_scan_mc.py`.

---

## 2026-08-11 14:33 EDT — Rare-event Palm/upcrossing calculation at `alpha=10^-6`

### Why the validation parameters changed
At `alpha=10^-6`, `beta=0.90`, the known-time required SNR is

```text
Phi^-1(1-alpha)+Phi^-1(beta) ~= 6.03498.
```

Therefore the Step-15 `rho_0=5` task is impossible even with known timing. Use instead

```text
rho_0=6.2
r=1.2
alpha=1e-6
beta=0.90
kappa=8.
```

### First rare-event route — exact grid-event mixture
For an `n`-point timing grid, choose one point uniformly and condition it above `u`. If `K_u` points exceed the level, the exact importance weight is

```math
\boxed{w=nQ(u)/K_u.}
```

This efficiently estimates the **grid maximum**, but still carries finite-grid continuum bias.

### Continuous Palm route
For a differentiable stationary Gaussian scan with derivative standard deviation `sigma`, let `N_u^+` be the number of level-`u` upcrossings and

```math
\lambda_u
=E[N_u^+]
=L\frac{\sigma}{2\pi}e^{-u^2/2}.
```

Under the Palm law of a randomly selected upcrossing,

```math
\boxed{
P_{FA}(u)
=Q(u)+\lambda_u
E_\uparrow\!\left[
\frac{1_{\{z(0)\le u\}}}{N_u^+}
\right].
}
```

Hence

```math
\boxed{P_{FA}(u)\le Q(u)+\lambda_u.}
```

**DERIVED / REFINEMENT:** the first-order Rice/EC expression is an upper bound; its error is exactly due to endpoint/upcrossing overlap and multiple high excursions.

The Palm crossing slope is Rayleigh distributed:

```math
z'(T)\sim\mathrm{Rayleigh}(\sigma).
```

Implementation: `numerics/upcrossing_importance_sampling.py`.

### `10^-6` numerical result
Rice predicts the crossover

```text
ell_s^Rice ~=0.571441752
ell_f^Rice ~=0.685730102
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

Multiple-upcrossing and endpoint-overlap fractions are each only about `10^-3` in the Palm ensemble. Rice therefore overestimates the exact false-alarm probability by less than `0.1%`; the implied threshold corrections are only `~10^-4`.

Propagating the correction through the detection-time equations and re-evaluating near the corrected switch gives

```math
\boxed{\ell_\times^{Palm}\approx0.5721}
```

with conservative numerical summary

```text
ell_cross^Palm ~=0.5721 +/-0.001.
```

Rice gives `0.57144`, differing by only about `0.12%`.

**NUMERICAL VALIDATION / CONDITIONAL:** in this smooth `kappa=8` rare-event task, Rice is quantitatively extremely accurate. High-threshold paths are overwhelmingly isolated single excursions, making the Palm estimator nearly zero-variance.

### Important interpretation of the earlier point-mixture deficit
The point-mixture sampler estimates a discrete grid maximum. Its percent-level deficit relative to continuous Rice at practical grid spacing is a **missed-between-grid-maximum effect**, not a percent-level failure of Rice theory. The Palm method forces a continuous upcrossing and only discretizes the much rarer correction events.

Full derivation: `RARE_EVENT_UPCROSSING_STEP.md`.  
Code: `numerics/upcrossing_importance_sampling.py`.

### Next question, held open
Does the near-exact Rice/Palm behavior persist as `kappa` and `r` are varied, and can the high-threshold limit reveal a simple asymptotic law for the fast/slow crossover?
