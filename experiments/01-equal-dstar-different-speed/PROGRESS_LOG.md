# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 13:28 EDT:** This log is intentionally compact. Every scientific milestone, correction, negative result, and stopping point is retained; full derivations live in the dedicated step files.

---

## 2026-08-11 11:21 EDT — Scalar D* insufficiency

Equal low-frequency/reference `D*` was assigned to detectors with `tau_A=1 ns`, `tau_B=1 s` under a physically allowed first-order + additive-output-noise model.

For the same 1 Hz tone and estimator bandwidth,

```text
SNR_A/SNR_B ~ 6.36.
```

**DERIVED / COUNTEREXAMPLE:** equal scalar reference `D*` does not guarantee equal SNR for arbitrary temporal signals.

**Qualification:** signal/noise filtering can cancel. This is not `fast is always better`.

---

## 2026-08-11 11:32 EDT — Known-waveform full-observation SNR

```math
\boxed{
\rho_\infty^2
=\int |P(f)|^2\frac{|G(f)|^2}{S_n(f)}df
=\frac1A\int |P(f)|^2D^{*2}(f)df.
}
```

**DERIVED / CONDITIONAL:** full-observation known-waveform detectability is a spectral overlap between waveform and detector signal-to-noise sensitivity.

Full derivation: `MATCHED_FILTER_SNR_STEP.md`.

---

## 2026-08-11 12:02 EDT — Unknown timing versus finite observation

Under stationary Gaussian full observation, equal complete `D*(f)` gives equal ideal unknown-arrival matched-filter search statistics.

Finite truncation can nevertheless distinguish a pure-delay pair with identical complete magnitude `D*(f)`.

**DERIVED / COUNTEREXAMPLE:** finite truncation can make phase/temporal placement operationally relevant.

**Qualification:** known latency can remove this specific example.

Full derivation: `FINITE_WINDOW_PHASE_STEP.md`.

---

## 2026-08-11 12:09 EDT — Latency-compensated dispersion

A stable causal all-pass factor preserves complete magnitude `D*(f)` and total infinite-time SNR while spreading a compact response into a tail.

Even after arbitrary constant alignment,

```math
\max_\delta\rho_{B,T}^2<\rho_{A,T}^2.
```

**DERIVED / COUNTEREXAMPLE:** the finite-window failure is not merely a pure-delay artifact.

Full derivation: `LATENCY_COMPENSATED_DISPERSION_STEP.md`.

---

## 2026-08-11 12:18 EDT — Exact SNR accumulation

For finite record `[0,t]`,

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
```

```math
\eta(t)=\rho_t^2/\rho_\infty^2.
```

**CONSEQUENCE:** eventual detectability and rate of access to it are distinct.

Full derivation: `SNR_ACCUMULATION_STEP.md`.

---

## 2026-08-11 12:30 EDT — Detection probability by deadline

For the simple known-time Gaussian test,

```math
\boxed{
P_D(t;\alpha)=
\Phi\!\left[
\rho_t-\Phi^{-1}(1-\alpha)
\right].
}
```

**DERIVED / CONDITIONAL:** equal eventual SNR can coexist with radically unequal early-deadline detection probability.

Full derivation: `DEADLINE_DETECTION_PROBABILITY_STEP.md`.

---

## 2026-08-11 12:38 EDT — Independent-slot unknown-time search

For `M` independent timing hypotheses,

```math
\boxed{
\gamma_{M,\alpha}
=\Phi^{-1}\!\left[(1-\alpha)^{1/M}\right].
}
```

**DERIVED / CONDITIONAL:** timing uncertainty consumes SNR margin through a global search threshold.

**Warning:** `M` is not digital sample count in a real continuous scan.

Full derivation: `UNKNOWN_TIME_SEARCH_STEP.md`.

---

## 2026-08-11 12:47 EDT — Continuous-time timing-search correlation

Define

```math
K(f)=\frac{G(f)P(f)}{\sqrt{S_n(f)}},
\qquad
W(f)=\frac{|K(f)|^2}{\int|K|^2df}.
```

Then

```math
\boxed{
r(\Delta)=\int W(f)e^{i2\pi f\Delta}df.
}
```

When the second moment exists,

```math
f_{rms}^2=\int f^2W(f)df
```

and Rice gives mean upcrossing density

```math
\nu_u^+=f_{rms}e^{-u^2/2}.
```

**REFINEMENT:** digital sample rate alone does not determine timing trials. For the same waveform, identical complete `D*(f)` gives identical full-observation search covariance.

**Regularity warning:** the ideal abrupt exponential has divergent second spectral moment in ideal white noise; Rice curvature needs regularization or a smoother waveform.

Full derivation: `CONTINUOUS_TIME_SEARCH_CORRELATION_STEP.md`.

---

## 2026-08-11 13:01 EDT — Finite-deadline correction and search-penalty reversal

The actual finite-deadline scan must use

```math
q_t=C_t^{-1}s_t
```

with covariance

```math
\boxed{
r_t(\Delta)
=\frac{\int |Q_t(f)|^2S_n(f)e^{i2\pi f\Delta}df}
{\int |Q_t(f)|^2S_n(f)df}.
}
```

**CORRECTION:** do not combine finite-window `eta(t)` with the Step-08 full-template `f_rms` as one exact finite-deadline statistic.

A stable causal equal-eventual-SNR family was constructed:

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
```

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
```

Its finite-time accumulation is

```math
\eta_\tau(t)
=1-e^{-2x}(1+2x+2x^2),
\qquad x=t/\tau.
```

The faster member has more finite-time SNR at every finite `t`, while its full-template search over fixed physical `L` has a larger threshold.

Under standard finite-to-full threshold convergence, the unknown-time detection ranking reverses at sufficiently large finite duration even while the faster member retains more accumulated SNR.

**DERIVED / CONDITIONAL:** faster SNR acquisition is not guaranteed to dominate unknown-time search complexity.

Full derivation: `SEARCH_PENALTY_REVERSAL_STEP.md`.

---

## 2026-08-11 13:18 EDT — Task-level detection-time surface

For each chosen filter duration `t`, compute both finite SNR and unknown-time search threshold from the same finite filter.

Define

```math
Z_{t,L}=\sup_{0\le\tau\le L}z_t(\tau),
```

```math
\gamma_t(L,\alpha)
=F^{-1}_{Z_{t,L}|H_0}(1-\alpha),
```

and

```math
P_{D,true}(t;L,\alpha)
=\Phi[\rho_t-\gamma_t(L,\alpha)].
```

The task margin is

```math
m(t;L,\alpha)=\rho_t-\gamma_t(L,\alpha).
```

If maximum allowed delay is `T`, the detector can choose any `t<=T`, so optimized by-deadline performance uses

```math
m^*(T)=\sup_{0<t\le T}m(t).
```

Define

```math
\boxed{
\mathcal T_D(\alpha,\beta,L)
=\inf\{t>0:m(t;L,\alpha)\ge\Phi^{-1}(\beta)\}.
}
```

This is a task-level surface, not a detector-only replacement for `D*`.

A finite interior optimal filter duration was left open generically.

Full derivation: `DETECTION_TIME_SURFACE_STEP.md`.

---

## 2026-08-11 13:28 EDT — Dimensionless surface and filter-duration ordering

### Exact dimensionless collapse

For the Step-09 family define

```math
x=t/\tau,
\qquad
\ell=L/\tau.
```

Then

```math
\boxed{
\rho_{\tau,t}=\rho_0\sqrt{\eta(x)},
}
```

with

```math
\eta(x)=1-e^{-2x}(1+2x+2x^2).
```

The exact finite-duration white-noise timing covariance is

```math
\boxed{
r_{\tau,t}(\Delta)=R_x(|\Delta|/\tau),
}
```

where

```math
R_x(y)
=\frac{\int_0^{x-y}v(v+y)e^{-2v-y}dv}
{\int_0^x v^2e^{-2v}dv}
```

for `0<=y<x`, and zero otherwise.

Therefore

```math
\boxed{
\gamma_{\tau,t}(L,\alpha)=\Gamma(x,\ell,\alpha)
}
```

and

```math
\boxed{
\mathcal T_D
=\tau\,X_D\!\left(\rho_0,\alpha,\beta,\frac{L}{\tau}\right).
}
```

### Exact null result for filter optimization

For fixed lag `y`, `R_x(y)` is a positive-weight average of a nondecreasing function, so

```math
x_2>x_1
\Rightarrow
R_{x_2}(y)\ge R_{x_1}(y)
\quad\forall y.
```

Slepian Gaussian comparison then gives

```math
\Gamma(x_2,\ell,\alpha)
\le
\Gamma(x_1,\ell,\alpha).
```

Meanwhile

```math
\eta'(x)=4x^2e^{-2x}>0.
```

Hence

```math
\boxed{
M(x)=\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha)
\text{ is strictly increasing.}
}
```

**DERIVED / NEGATIVE RESULT:** this family has no finite interior optimal filter duration. If the allowed maximum delay is `T`, the optimal filter uses `t=T`.

This does not undo Step 09. The cross-detector reversal is caused by the different dimensionless search domains `L/tau`, not by either detector using a self-suboptimal integration duration.

Full derivation: `DIMENSIONLESS_DETECTION_SURFACE_STEP.md`.

### Next question, held open

For two members with different `tau` but equal `rho_0`, determine the boundary in task space `(L, alpha, beta)` where their detection-time surfaces cross and the detector that reaches the required decision first switches from the faster member to the slower member.
