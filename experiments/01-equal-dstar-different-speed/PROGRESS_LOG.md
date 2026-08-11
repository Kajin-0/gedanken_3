# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 15:00 EDT:** This log is intentionally compact but preserves every scientific milestone, correction, negative result, rejected shortcut, failed numerical estimate, numerical validation, and stopping point. Full derivations live in dedicated step files.

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
**NEGATIVE RESULT:** equal complete `D*(f)` gives equal ideal stationary-Gaussian full-observation timing-search statistics. Finite truncation can still distinguish detectors because magnitude `D*(f)` discards temporal phase/placement.

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

**WARNING:** `M` is not digital sample count in a continuous timing scan.

Full derivation: `UNKNOWN_TIME_SEARCH_STEP.md`.

---

## 2026-08-11 12:47 EDT — Continuous-time timing covariance
Derived the matched-filter timing covariance from the noise-whitened template. When the second moment exists, `f_rms` controls local curvature and Rice upcrossing density.

**REFINEMENT:** sample rate alone does not set timing trials.

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

## 2026-08-11 13:28 EDT — Dimensionless collapse and filter-duration negative result
For the controlled family,

```math
\mathcal T_D=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

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

Task space partitions into both-feasible, slow-only, and neither-feasible regions; fast-only feasibility is impossible under equal eventual SNR. At least one finite crossover exists under standard continuity/extreme-value conditions; uniqueness remains open.

Full derivation: `TASK_REGIME_BOUNDARY_STEP.md`.

---

## 2026-08-11 13:50 EDT — Direct correlated-scan prototype and continuum obstruction
Implemented direct FFT moving-average Monte Carlo for the grid-sampled correlated finite-duration scan. No independent-trials approximation was used.

**FAILED NUMERICAL ESTIMATE:** apparent crossover values around `ell~49` do not survive timing-grid refinement and must never be quoted.

Exact cause:

```math
\boxed{a_x=-R_x'(0^+)=2x^2e^{-2x}/\eta(x)}
```

and `R_x(y)=1-a_x|y|+...`, so the finite hard-window scan is locally Brownian-like / nondifferentiable in ideal white noise.

Full derivation: `NUMERICAL_SCAN_CONVERGENCE_STEP.md`.

---

## 2026-08-11 14:10 EDT — True finite-bandwidth regularization
**REJECTED SHORTCUT:** an invertible noiseless common low-pass does not necessarily regularize optimal information bandwidth because whitening can undo it.

A true finite information band makes the timing-spectrum second moment finite and removes the cusp. For fixed `kappa=Omega_B tau`, the scaled task surface and fast/slow boundary survive.

Full derivation: `FINITE_BANDWIDTH_REGULARIZATION_STEP.md`.

---

## 2026-08-11 14:18 EDT — Smooth-band numerical validation
Use

```math
J_{x,\kappa}(\nu)=|H_x(\nu)|^2e^{-(\nu/\kappa)^2}.
```

Direct correlated FFT simulation is stable under practical grid refinement and compatible with Rice/EC at the validation points.

For `rho_0=5`, `r=1.2`, `alpha=0.01`, `beta=0.90`, Rice gives the approximate trend

```text
kappa      ell_cross^Rice
2             75.56
4             61.58
8             54.75
16            51.43
32            49.89
```

These are trend estimates, not exact phase boundaries.

Full derivation: `FINITE_BANDWIDTH_NUMERICAL_STEP.md`.

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

Hence Rice/EC is an upper bound; its error is exactly multiple excursions plus endpoint/upcrossing overlap.

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

### Exact Palm-corrected crossover identity
At a crossover set

```math
x_s=x,
\quad x_f=rx,
\quad \ell_s=\ell,
\quad \ell_f=r\ell,
```

with thresholds

```math
u_s=\rho_0\mathcal R_\kappa(x)-\Phi^{-1}(\beta),
```

```math
u_f=\rho_0\mathcal R_\kappa(rx)-\Phi^{-1}(\beta).
```

If

```math
C_\uparrow=E_\uparrow[1_{z(0)\le u}/N_u^+],
```

then

```math
\boxed{
\frac{[\alpha-Q(u_f)]e^{u_f^2/2}}{\sigma_f C_f}
=r
\frac{[\alpha-Q(u_s)]e^{u_s^2/2}}{\sigma_s C_s}.
}
```

With isolated excursions `C_s,C_f~1`, this gives the endpoint-retaining Rice crossover law

```math
\boxed{
u_f^2-u_s^2
\approx2\ln\!\left[
r\frac{\sigma_f}{\sigma_s}
\frac{\alpha-Q(u_s)}{\alpha-Q(u_f)}
\right].}
```

### Rejected endpoint shortcut
**REJECTED SHORTCUT:** `alpha <<1` does not imply `Q(u)<<alpha`. In the Step-16 task the endpoint terms consume roughly `45–50%` of the global false-alarm budget; dropping them moves the predicted crossover from `~0.571` to about `1.0`.

### Rice accuracy is not uniform in bandwidth
For finite hard-window `x`,

```math
H_x(\nu)\sim ixe^{-x}e^{-i\nu x}/\nu,
```

which yields

```math
\boxed{
\sigma_\kappa^2(x)
\sim\frac{a_x}{\sqrt\pi}\kappa
\qquad(\kappa\to\infty).
}
```

Thus Rice upcrossing counts grow as `sqrt(kappa)` while exact excursion probability remains bounded, forcing

```math
C_\uparrow=O(\kappa^{-1/2}).
```

**DERIVED:** the near-exact `kappa=8` Rice/Palm agreement cannot persist uniformly into the rough Step-13 limit.

A `3000`-path Palm sweep at `r=1.2`, `alpha=1e-6` shows the correction growing from below resolution at `kappa=2`, to about `0.1%` at `kappa=8`, a few tenths of a percent at `kappa=16`, and about `0.4–0.7%` at `kappa=32`.

### Large speed-ratio law
Define

```math
u_\infty=\rho_0-\Phi^{-1}(\beta)
```

and the fast detector's full-template feasibility edge

```math
\Gamma_{\infty,\kappa}(\ell_{crit,\kappa},\alpha)=u_\infty.
```

On the tracked fast-to-slow crossover branch,

```math
\boxed{
r\ell_\times\to\ell_{crit,\kappa},}
```

so

```math
\boxed{
\ell_\times\sim\ell_{crit,\kappa}/r,}
```

and

```math
\boxed{
L_\times\to\tau_f\ell_{crit,\kappa}.}
```

The slow time constant drops out at leading order.

Rice gives

```math
\ell_{crit,\kappa}^{Rice}
=\frac{2\pi[\alpha-Q(u_\infty)]}{\sigma_{\infty,\kappa}}
e^{u_\infty^2/2}.
```

For the Step-16 task:

```text
kappa      ell_crit^Rice
2             0.988282
4             0.811380
8             0.723222
16            0.678958
32            0.656729
```

Finite-r convergence is very rapid: `r=2` is within about `0.1%` of the large-r limit and `r=3` within about `5e-4%` across representative `kappa` values.

For the original `tau_f=1 ns`, `tau_s=1 s` ratio and only the Step-16 validation parameters with `kappa=8`, the illustrative large-r Rice scale is `L_cross ~0.723 ns`; Palm indicates only a sub-percent correction.

### Noncommuting limits
At fixed finite `r`, `kappa->infinity` recreates finite-window roughness and destroys uniform Rice accuracy. If `r->infinity` is taken first, the fast detector uses its smooth full template and `sigma_infinity,kappa->1`, so bandwidth removal remains regular.

Full derivation: `HIGH_THRESHOLD_CROSSOVER_ASYMPTOTICS_STEP.md`.  
Calculator: `numerics/asymptotic_crossover.py`.

### Next question, held open
If both detectors are connected to the **same physical readout bandwidth** rather than the same dimensionless `kappa`, does the large-r crossover law survive, and can the electronics bandwidth itself change or optimize which detector wins?
