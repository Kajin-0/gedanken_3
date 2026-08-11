# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 15:22 EDT:** This log is intentionally compact but preserves every scientific milestone, correction, negative result, rejected shortcut, failed numerical estimate, numerical validation, asymptotic result, and stopping point. Full derivations live in the dedicated step files.

---

## 2026-08-11 11:21 EDT — Scalar `D*` insufficiency
Equal reference `D*` with `tau_A=1 ns`, `tau_B=1 s` was tested in a physically allowed first-order + additive-output-noise model. The same 1 Hz tone gave `SNR_A/SNR_B ~ 6.36`.

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
**NEGATIVE RESULT:** equal complete `D*(f)` gives equal ideal stationary-Gaussian full-observation timing-search statistics.

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

Full derivation: `DEADLINE_DETECTION_PROBABILITY_STEP.md`.

---

## 2026-08-11 12:38 EDT — Independent-slot unknown-time search

```math
\gamma_{M,\alpha}=\Phi^{-1}[(1-\alpha)^{1/M}].
```

**WARNING:** `M` is not digital sample count in a continuous scan.

Full derivation: `UNKNOWN_TIME_SEARCH_STEP.md`.

---

## 2026-08-11 12:47 EDT — Continuous timing covariance
Derived the timing-search covariance from the noise-whitened template. When the second spectral moment exists, its RMS timing frequency controls local curvature and Rice upcrossing density.

**REFINEMENT:** sample rate alone does not set timing-search complexity.

Full derivation: `CONTINUOUS_TIME_SEARCH_CORRELATION_STEP.md`.

---

## 2026-08-11 13:01 EDT — Finite-deadline correction and ranking reversal
The actual finite scan must use `q_t=C_t^-1s_t` and its own covariance.

**REJECTED SHORTCUT:** do not combine finite-window `eta(t)` with full-template `f_rms` as one exact statistic.

Constructed the equal-eventual-SNR family

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
\qquad
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
```

Faster members accumulate more finite-time SNR but can face a larger unknown-time search burden. Under standard finite-to-full convergence, cross-detector ranking can reverse.

Full derivation: `SEARCH_PENALTY_REVERSAL_STEP.md`.

---

## 2026-08-11 13:18 EDT — Task-level detection-time surface
Defined

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t>0:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

Task-level, not a detector scalar.

Full derivation: `DETECTION_TIME_SURFACE_STEP.md`.

---

## 2026-08-11 13:28 EDT — Dimensionless collapse; integration-time negative result
For the controlled scaled family,

```math
\mathcal T_D=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

Pointwise covariance ordering plus Slepian comparison makes the search threshold nonincreasing with integration duration while SNR rises strictly.

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

Task space partitions into both-feasible, slow-only, and neither-feasible regions; fast-only feasibility is impossible under equal eventual SNR. Under standard continuity/extreme-value conditions at least one finite fast-to-slow crossover exists; uniqueness remains open.

Full derivation: `TASK_REGIME_BOUNDARY_STEP.md`.

---

## 2026-08-11 13:50 EDT — Direct correlated-scan prototype and continuum obstruction
Implemented direct FFT moving-average Monte Carlo for the exact grid-sampled correlated finite-duration Gaussian scan. No independent-trials approximation was used.

Broad fast-to-slow behavior appeared, but the apparent crossover moved under timing-grid refinement.

**FAILED NUMERICAL ESTIMATE:** diagnostic crossover values around `ell ~ 49` are not continuum-converged and must never be quoted.

Exact cause:

```math
\boxed{a_x=-R_x'(0^+)=2x^2e^{-2x}/\eta(x)}
```

and

```math
R_x(y)=1-a_x|y|+O(y^2),
```

so the finite hard-window scan is locally Brownian-like / mean-square nondifferentiable in ideal white noise.

Full derivation: `NUMERICAL_SCAN_CONVERGENCE_STEP.md`.  
Prototype: `numerics/correlated_scan_mc.py`.

---

## 2026-08-11 14:10 EDT — Genuine finite-information-band regularization
**REJECTED SHORTCUT:** appending a noiseless invertible common low-pass does not necessarily regularize optimal detection because whitening can undo it.

A true information-band limitation makes the timing-spectrum second moment finite and removes the Step-13 cusp.

For a similarity-preserving family with fixed `kappa=Omega_B tau`, equal accessible eventual SNR, and time scaling,

```math
\mathcal T_{D,\kappa}
=\tau X_{D,\kappa}(\rho_0,\alpha,\beta,L/\tau),
```

and the fast/slow boundary survives.

Full derivation: `FINITE_BANDWIDTH_REGULARIZATION_STEP.md`.

---

## 2026-08-11 14:18 EDT — Smooth-band numerical validation
Choose the explicit Gaussian information weighting

```math
J_{x,\kappa}(\nu)=|H_x(\nu)|^2e^{-(\nu/\kappa)^2}.
```

Direct correlated FFT simulation is stable under practical timing-grid refinement and compatible with Rice/EC at validation points.

For `rho_0=5`, `r=1.2`, `alpha=0.01`, `beta=0.90`, Rice gives the approximate trend

```text
kappa      ell_cross^Rice
2             75.56
4             61.58
8             54.75
16            51.43
32            49.89
```

**CONDITIONAL TREND:** more accessible high-frequency timing information moves the fast-to-slow switch to smaller `L/tau_s` in this tested model.

These are trend estimates, not exact phase boundaries.

Full derivation: `FINITE_BANDWIDTH_NUMERICAL_STEP.md`.  
Code: `numerics/regularized_scan_mc.py`.

---

## 2026-08-11 14:33 EDT — Rare-event Palm/upcrossing method
For a differentiable stationary Gaussian scan,

```math
\lambda_u=E[N_u^+]
=L\frac{\sigma}{2\pi}e^{-u^2/2},
```

and

```math
\boxed{
P_{FA}(u)
=Q(u)+\lambda_u
E_\uparrow\!\left[
\frac{1_{\{z(0)\le u\}}}{N_u^+}
\right].
}
```

Hence Rice/EC is an upper bound; its error is exactly multiple high excursions plus endpoint/upcrossing overlap.

A first point-exceedance importance sampler efficiently solved the **grid maximum** but retained finite-grid continuum bias. This was kept as a valid discretized method, not mistaken for the continuous event.

For

```text
rho_0=6.2
r=1.2
alpha=1e-6
beta=0.90
kappa=8,
```

Rice predicts `ell_cross ~=0.571441752`; Palm gives `ell_cross ~=0.5721 +/-0.001`, only about `0.12%` higher.

Implementation: `numerics/upcrossing_importance_sampling.py`.

Full derivation: `RARE_EVENT_UPCROSSING_STEP.md`.

---

## 2026-08-11 15:00 EDT — High-threshold crossover law and extreme-speed-ratio asymptote
Derived the exact smooth Palm-corrected crossover identity

```math
\frac{[\alpha-Q(u_f)]e^{u_f^2/2}}{\sigma_f C_f}
=r
\frac{[\alpha-Q(u_s)]e^{u_s^2/2}}{\sigma_s C_s}.
```

For isolated excursions this reduces to a compact endpoint-retaining Rice law.

**REJECTED SHORTCUT:** `alpha << 1` does not imply `Q(u) << alpha`; in the rare-event validation task the endpoint term consumes roughly half the false-alarm budget.

For finite hard-window duration,

```math
\boxed{
\sigma_\kappa^2(x)
\sim\frac{a_x}{\sqrt\pi}\kappa
\qquad(\kappa\to\infty),
}
```

so Rice upcrossing counts grow as `sqrt(kappa)` while exact excursion probability remains bounded. The Palm correction must therefore shrink; Rice accuracy is not uniform into the rough Step-13 limit.

For the co-scaled extreme-speed-ratio branch define

```math
\Gamma_{\infty,\kappa}(\ell_{crit,\kappa},\alpha)
=\rho_0-\Phi^{-1}(\beta).
```

Then

```math
\boxed{r\ell_\times\to\ell_{crit,\kappa}},
```

and physically

```math
\boxed{L_\times\to\tau_f\ell_{crit,\kappa}}.
```

The slow time constant drops out at leading order. Finite-`r` Rice solutions converge rapidly to this limit.

**REFINEMENT:** fixed finite `r` followed by `kappa->infinity` recreates rough finite-window behavior; taking `r->infinity` first forces the fast detector onto its smooth full template and makes bandwidth removal regular.

Full derivation: `HIGH_THRESHOLD_CROSSOVER_ASYMPTOTICS_STEP.md`.  
Calculator: `numerics/asymptotic_crossover.py`.

---

## 2026-08-11 15:22 EDT — Same physical electronics bandwidth

### Model change
Replace the equal-`kappa` comparison with one common physical information-band scale:

```math
\kappa_f=\Omega_B\tau_f,
\qquad
\kappa_s=\Omega_B\tau_s=r\kappa_f.
```

To isolate timing/search effects, retain equal **accessible eventual SNR** `rho_0` across the two detector/readout combinations.

### Finite-`r` structure
The Step-17 Palm/Rice crossover identity remains valid, but slow and fast terms are evaluated at different `kappa_s` and `kappa_f`. The former one-parameter similarity reduction is lost.

### Large-`r` qualification
**REFINEMENT:** `r->infinity` alone is not enough if `kappa_f` is simultaneously allowed to vanish. The clean fast-feasibility-edge asymptote requires

```math
\ell_{crit}(\kappa_f)/r\to0.
```

In the electronics-limited regime this is equivalent to the slow detector having large `kappa_s=r kappa_f`.

Under that condition,

```math
\boxed{
L_\times
\to
\tau_f\ell_{crit}(\Omega_B\tau_f).
}
```

### Full-template timing curvature
For the Gaussian information-band full template,

```math
\sigma_\infty^2(\kappa)
=
\frac{\int \nu^2(1+\nu^2)^{-2}e^{-(\nu/\kappa)^2}d\nu}
{\int (1+\nu^2)^{-2}e^{-(\nu/\kappa)^2}d\nu}.
```

Writing `s=kappa^-2` gives

```math
\frac{d}{ds}\sigma_\infty^2
=-\operatorname{Var}_s(\nu^2)<0,
```

so `sigma_infinity` increases strictly with physical timing bandwidth.

### High-threshold physical crossover
Define

```math
\mathcal C
=2\pi[\alpha-Q(u_\infty)]e^{u_\infty^2/2},
\qquad
u_\infty=\rho_0-\Phi^{-1}(\beta).
```

Then

```math
\boxed{
L_\times^{Rice}
\sim
\tau_f\frac{\mathcal C}
{\sigma_\infty(\Omega_B\tau_f)}.
}
```

Two regimes follow:

```math
\boxed{
L_\times^{Rice}
\sim\frac{\sqrt2\mathcal C}{\Omega_B}
\qquad(\Omega_B\tau_f\ll1),
}
```

```math
\boxed{
L_\times^{Rice}
\to\mathcal C\tau_f
\qquad(\Omega_B\tau_f\gg1).
}
```

**FIRST NONTRIVIAL CONSEQUENCE:** once the intrinsic detector is faster than the accessible electronics, making the detector still faster no longer moves the task boundary at leading order; the electronics time `1/Omega_B` becomes the relevant scale.

For the Step-16 task only (`rho_0=6.2`, `alpha=1e-6`, `beta=0.90`), `C ~=0.63441`. For `tau_f=1 ns`, the Gaussian information-band model gives illustrative large-`r` Rice crossover scales from about `143 ns` at `f_B=1 MHz` to `0.646 ns` at `10 GHz`, approaching `0.634 ns` at infinite information bandwidth. These are model/task illustrations, not hardware recommendations.

### Bandwidth optimum question
Because `sigma_infinity(kappa)` increases monotonically, reducing bandwidth monotonically pushes the fast-to-slow crossover to larger `L` **when accessible eventual SNR is artificially held fixed**.

**NEGATIVE RESULT / QUALIFICATION:** no interior bandwidth optimum exists in this normalized large-`r` problem. This is not a physical optimization result because real bandwidth changes generally alter eventual SNR as well.

Full derivation: `FIXED_PHYSICAL_BANDWIDTH_STEP.md`.  
Calculator: `numerics/fixed_physical_bandwidth.py`.

### Next question, held open
If physical detector signal and noise amplitudes are held fixed while `Omega_B` is varied—so bandwidth changes both eventual SNR and timing-search burden—does a genuine finite optimal readout bandwidth emerge?
