# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 16:12 EDT:** This log is intentionally compact while preserving every scientific milestone, correction, negative result, rejected shortcut, failed numerical estimate, numerical validation, asymptotic result, and stopping point. Full derivations live in dedicated step files.

---

## 2026-08-11 11:21 EDT — Step 01: scalar `D*` insufficiency

Equal reference `D*` with `tau_A=1 ns`, `tau_B=1 s` was tested in a physically allowed first-order response with additive output noise. The same 1 Hz optical tone gave `SNR_A/SNR_B ~ 6.36`.

**COUNTEREXAMPLE:** equal scalar reference `D*` does not guarantee equal SNR for arbitrary temporal signals.

**QUALIFICATION:** signal/noise filtering can cancel; do not infer `fast is always better`.

---

## 2026-08-11 11:32 EDT — Step 02: known-waveform full-observation SNR

Derived

```math
\rho_\infty^2
=\int |P|^2|G|^2/S_n\,df
=\frac1A\int |P|^2D^{*2}\,df.
```

Complete magnitude `D*(f)` is sufficient for this restricted full-observation known-waveform maximum-linear-SNR problem.

Full derivation: `MATCHED_FILTER_SNR_STEP.md`.

---

## 2026-08-11 12:02 EDT — Step 03: unknown timing negative result; finite truncation

**NEGATIVE RESULT:** equal complete `D*(f)` gives equal ideal stationary-Gaussian full-observation timing-search statistics for the same optical waveform.

Finite truncation can still distinguish detectors because magnitude `D*(f)` discards temporal phase/placement.

Full derivation: `FINITE_WINDOW_PHASE_STEP.md`.

---

## 2026-08-11 12:09 EDT — Step 04: latency-compensated dispersion

A stable causal all-pass factor preserved complete magnitude `D*(f)` and total infinite-time SNR while changing finite-window SNR after constant latency alignment.

**COUNTEREXAMPLE:** finite-window insufficiency is not merely a pure-delay artifact.

Full derivation: `LATENCY_COMPENSATED_DISPERSION_STEP.md`.

---

## 2026-08-11 12:18 EDT — Step 05: exact finite-record SNR

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
\qquad
\eta(t)=\rho_t^2/\rho_\infty^2.
```

Eventual detectability and rate of access to it are distinct.

Full derivation: `SNR_ACCUMULATION_STEP.md`.

---

## 2026-08-11 12:30 EDT — Step 06: detection probability by deadline

```math
P_D(t;\alpha)=\Phi[\rho_t-\Phi^{-1}(1-\alpha)].
```

Equal eventual SNR can coexist with radically unequal early-deadline detection probability.

Full derivation: `DEADLINE_DETECTION_PROBABILITY_STEP.md`.

---

## 2026-08-11 12:38 EDT — Step 07: independent-slot timing search

```math
\gamma_{M,\alpha}=\Phi^{-1}[(1-\alpha)^{1/M}].
```

**WARNING:** `M` is not digital sample count in a real continuous timing scan.

Full derivation: `UNKNOWN_TIME_SEARCH_STEP.md`.

---

## 2026-08-11 12:47 EDT — Step 08: continuous timing-search covariance

Derived timing covariance from the noise-whitened template. When the second timing-spectral moment exists, its RMS frequency controls local covariance curvature and Rice upcrossing density.

**REFINEMENT:** sample rate alone does not set timing-search complexity.

Full derivation: `CONTINUOUS_TIME_SEARCH_CORRELATION_STEP.md`.

---

## 2026-08-11 13:01 EDT — Step 09: finite-deadline correction and ranking reversal

The actual finite search must use `q_t=C_t^-1s_t` and its own covariance.

**REJECTED SHORTCUT:** do not combine finite-window `eta(t)` with full-template `f_rms` as one exact statistic.

Constructed the equal-eventual-SNR family

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
```

Faster members acquire finite-time SNR sooner but can face a larger unknown-time search burden. Cross-detector ranking can reverse.

Full derivation: `SEARCH_PENALTY_REVERSAL_STEP.md`.

---

## 2026-08-11 13:18 EDT — Step 10: task-level detection-time surface

Defined

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

This is task-level, not a detector scalar.

Full derivation: `DETECTION_TIME_SURFACE_STEP.md`.

---

## 2026-08-11 13:28 EDT — Step 11: dimensionless collapse; integration-time negative result

For the controlled family,

```math
\mathcal T_D=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

Pointwise covariance ordering plus Slepian comparison makes the global search threshold nonincreasing with integration duration while SNR rises strictly.

**NEGATIVE RESULT:** no finite interior `t_opt`; use all available data.

Full derivation: `DIMENSIONLESS_DETECTION_SURFACE_STEP.md`.

---

## 2026-08-11 13:39 EDT — Step 12: fast/slow task-regime boundary

For `r=tau_s/tau_f>1` and `ell=L/tau_s`, the exact preference boundary is

```math
X_D(r\ell)-rX_D(\ell)=0.
```

**REJECTED SHORTCUT:** asymptotic-margin equality is not the minimum-decision-time boundary.

Task space has both-feasible, slow-only, and neither-feasible regions; fast-only feasibility is impossible under equal eventual SNR. At least one finite crossover exists under standard continuity/extreme-value assumptions; uniqueness remains open.

Full derivation: `TASK_REGIME_BOUNDARY_STEP.md`.

---

## 2026-08-11 13:50 EDT — Step 13: direct correlated prototype and continuum obstruction

Implemented direct FFT moving-average Monte Carlo for the actual grid-sampled finite-duration Gaussian timing scan; no independent-trials approximation was used.

Broad fast/slow behavior appeared, but the apparent crossover moved under timing-grid refinement.

**FAILED NUMERICAL ESTIMATE:** diagnostic crossover values around `ell ~ 49` are not continuum-converged and must never be quoted.

Exact cause:

```math
R_x(y)=1-a_x|y|+O(y^2),
\qquad
 a_x=2x^2e^{-2x}/\eta(x),
```

so the finite hard-window scan is locally Brownian-like / mean-square nondifferentiable in ideal white noise.

Full derivation: `NUMERICAL_SCAN_CONVERGENCE_STEP.md`.  
Prototype: `numerics/correlated_scan_mc.py`.

---

## 2026-08-11 14:10 EDT — Step 14: genuine finite information bandwidth

**REJECTED SHORTCUT:** an invertible noiseless common low-pass does not necessarily regularize optimal detection because whitening can undo it.

A genuine finite timing-information band makes the second spectral moment finite and removes the Step-13 cusp. For fixed dimensionless `kappa=Omega_B tau`, the task-surface structure and fast/slow boundary survive.

Full derivation: `FINITE_BANDWIDTH_REGULARIZATION_STEP.md`.

---

## 2026-08-11 14:18 EDT — Step 15: smooth-band numerical validation

Choose

```math
J_{x,\kappa}(\nu)=|H_x(\nu)|^2e^{-(\nu/\kappa)^2}.
```

Direct correlated FFT simulation has stable practical timing-grid behavior and agrees with Rice/Euler-characteristic predictions at the validation points.

**CONDITIONAL TREND:** increasing accessible timing bandwidth moved the fast-to-slow crossover to smaller normalized timing uncertainty in the tested model.

Full derivation: `FINITE_BANDWIDTH_NUMERICAL_STEP.md`.  
Code: `numerics/regularized_scan_mc.py`.

---

## 2026-08-11 14:33 EDT — Step 16: rare-event Palm/upcrossing method

For a differentiable stationary Gaussian scan,

```math
\boxed{
P_{FA}(u)
=Q(u)+\lambda_u
E_\uparrow\!\left[
\frac{1_{\{z(0)\le u\}}}{N_u^+}
\right]
}
```

with

```math
\lambda_u=L\frac{\sigma}{2\pi}e^{-u^2/2}.
```

Hence Rice/EC is an upper bound; its error is exactly multiple high excursions plus endpoint/upcrossing overlap.

A first point-exceedance importance sampler solved the **grid maximum** efficiently but retained finite-grid continuum bias; this was kept as a valid discretized method rather than mistaken for the continuous event.

For `rho_0=6.2`, `r=1.2`, `alpha=1e-6`, `beta=0.90`, `kappa=8`, Rice predicted `ell_cross ~=0.57144`; Palm gave `~0.5721 +/-0.001`.

Implementation: `numerics/upcrossing_importance_sampling.py`.  
Full derivation: `RARE_EVENT_UPCROSSING_STEP.md`.

---

## 2026-08-11 15:00 EDT — Step 17: high-threshold law and extreme speed ratio

Derived the exact smooth Palm-corrected crossover structure

```math
\frac{[\alpha-Q(u_f)]e^{u_f^2/2}}{\sigma_f C_f}
=r
\frac{[\alpha-Q(u_s)]e^{u_s^2/2}}{\sigma_s C_s}.
```

For isolated excursions this becomes a compact endpoint-retaining Rice law.

**REJECTED SHORTCUT:** `alpha << 1` does not imply `Q(u) << alpha`; the endpoint term used about half the false-alarm budget in the rare-event validation task.

For finite hard windows,

```math
\sigma_\kappa^2(x)\sim a_x\kappa/\sqrt\pi,
```

so Rice upcrossing counts grow toward the rough limit and Rice accuracy is not uniform in `kappa`.

For the co-scaled extreme-speed-ratio branch,

```math
\boxed{L_\times\to\tau_f\ell_{crit,\kappa}}.
```

**REFINEMENT:** fixed finite `r` followed by `kappa->infinity` recreates rough finite-window behavior; taking `r->infinity` first forces the fast detector onto its smooth full template.

Full derivation: `HIGH_THRESHOLD_CROSSOVER_ASYMPTOTICS_STEP.md`.  
Calculator: `numerics/asymptotic_crossover.py`.

---

## 2026-08-11 15:22 EDT — Step 18: one shared physical electronics bandwidth

Replace equal `kappa` with

```math
\kappa_f=\Omega_B\tau_f,
\qquad
\kappa_s=\Omega_B\tau_s.
```

To isolate timing/search effects, Step 18 still forced equal accessible eventual SNR.

**REFINEMENT:** the clean large-`r` one-edge asymptote requires `ell_crit(kappa_f)/r -> 0`; `r->infinity` alone is insufficient if `kappa_f` simultaneously collapses.

Under that condition,

```math
L_\times\to\tau_f\ell_{crit}(\Omega_B\tau_f).
```

The crossover changes from electronics-limited `~1/Omega_B` to detector-limited `~tau_f` as bandwidth grows.

**NEGATIVE RESULT / QUALIFICATION:** no interior bandwidth optimum exists while accessible eventual SNR is artificially held fixed.

Full derivation: `FIXED_PHYSICAL_BANDWIDTH_STEP.md`.  
Calculator: `numerics/fixed_physical_bandwidth.py`.

---

## 2026-08-11 15:33 EDT — Step 19: fixed physical signal/noise; genuine finite bandwidth optimum

Remove the Step-18 accessible-SNR renormalization. Let

```math
\rho_\infty(\kappa)=\rho_{full}\sqrt{F(\kappa)},
\qquad
\sigma^2(\kappa)=I_2/I_0.
```

Known-time feasibility gives a finite lower bandwidth threshold.

At wide bandwidth,

```math
\rho_\infty(\kappa)
=\rho_{full}[1-1/(2\kappa^2)+O(\kappa^{-3})],
```

while

```math
\sigma(\kappa)
=1-2/(\sqrt\pi\kappa)+O(\kappa^{-2}).
```

Thus SNR loss is `O(1/kappa^2)` but timing-search simplification is `O(1/kappa)`.

**DERIVED / CONDITIONAL:** for the large-`r` full-template Rice objective, infinite bandwidth is suboptimal whenever the full-band detector is strictly known-time feasible, and at least one finite bandwidth optimum exists.

Step-16-calibrated example:

```text
rho_full ~=6.240757
alpha=1e-6
beta=0.90
kappa_min ~=3.14545
kappa_opt^Rice ~=42.23
ell_crit^Rice(opt) ~=0.90083
ell_crit^Rice(infinity) ~=0.88906
```

A `10000`-path Palm spot check preserved the finite-candidate-over-infinite ordering but did not solve the exact Palm optimum.

Full derivation: `PHYSICAL_BANDWIDTH_OPTIMUM_STEP.md`.  
Calculator: `numerics/physical_bandwidth_optimum.py`.

---

## 2026-08-11 16:12 EDT — Step 20: finite speed ratio and double bandwidth reversal

### New fixed-physics finite-`r` asymmetry

Use one common physical bandwidth without SNR renormalization:

```math
\kappa_f=\Omega_B\tau_f,
\qquad
\kappa_s=r\kappa_f.
```

Because `F(kappa)` is strictly increasing,

```math
\rho_{\infty,s}
=\rho_{full}\sqrt{F(r\kappa_f)}
>
\rho_{\infty,f}
=\rho_{full}\sqrt{F(\kappa_f)}
```

for finite bandwidth, and

```math
\boxed{\rho_{\infty,s}/\rho_{\infty,f}\to\sqrt r}
```

in the narrow-band limit. The slower detector therefore becomes feasible first as a common narrow readout is widened.

### Explicit finite-r counterexample

Use

```text
r        = 2
rho_full = 6.2407571
alpha    = 1e-6
beta     = 0.90
Lambda   = L/tau_f = 0.895
```

with the full finite-duration spectral integrals and each detector's own Rice search threshold.

Representative decision times:

```text
kappa_f    T_f/tau_f    T_s/tau_f    preference
20         infeasible    7.56822       slow only
25          8.02316      7.61341       slow
30          6.81840      7.65936       fast
80          7.09937      8.03871       fast
120         7.93053      8.26231       fast
140         9.11095      8.35794       slow
160        infeasible    8.44554       slow only
```

The two finite switch points are

```text
kappa_cross_1 ~=25.4898402
kappa_cross_2 ~=130.1945883
```

and both occur while both detectors are feasible.

**NUMERICAL COUNTEREXAMPLE / CONDITIONAL:** sweeping one common physical readout bandwidth produces

```math
\boxed{\text{slow}\to\text{fast}\to\text{slow}}
```

with only a factor-of-two intrinsic detector speed difference.

Halving the spectral integration spacing from `dnu=0.02` to `0.01` moved the switches by only about `1.4e-8` and `5.4e-7`; the double reversal is not a frequency-quadrature artifact at the reported Rice precision.

Interpretation:

```text
narrow bandwidth      -> accessible-SNR asymmetry favors slow
intermediate bandwidth-> intrinsic speed advantage favors fast
wide bandwidth        -> unknown-time search burden favors slow
```

This proves that the finite-r task boundary can be nonmonotone in bandwidth and that the Step-19 finite-band structure is not merely an `r->infinity` artifact.

**OPEN:** exact Palm-corrected switch values are not yet known. The high-band switch especially requires rare-event validation because Step 17 showed nonuniform finite-window Rice accuracy as `kappa` grows.

Full derivation: `FINITE_R_BANDWIDTH_REVERSAL_STEP.md`.  
Calculator: `numerics/finite_r_bandwidth_reversal.py`.

### Next question, held open

Does the exact continuous Palm correction preserve both finite-`r` bandwidth reversals, especially the high-bandwidth switch, and how far do the two switch points move?
