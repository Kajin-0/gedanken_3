# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 13:18 EDT:** This log is intentionally compact. Every scientific milestone, correction, negative result, and stopping point is retained; full derivations live in the dedicated step files.

---

## 2026-08-11 11:21 EDT — Scalar D* insufficiency

Equal low-frequency/reference `D*` was assigned to two detectors with `tau_A=1 ns`, `tau_B=1 s`, equal area, equal low-frequency responsivity, and equal additive output-noise density.

For the same 1 Hz tone and estimator bandwidth,

```text
SNR_A/SNR_B ~ 6.36.
```

**DERIVED / COUNTEREXAMPLE:** equal scalar reference `D*` does not guarantee equal SNR for arbitrary temporal signals.

**Qualification:** signal/noise filtering can cancel. This is not `fast is always better`.

---

## 2026-08-11 11:32 EDT — Known-waveform full-observation SNR

For waveform `P(f)`, LTI transfer `G(f)`, and stationary additive output-noise PSD `S_n(f)`,

```math
\boxed{
\rho_\infty^2
=\int |P(f)|^2\frac{|G(f)|^2}{S_n(f)}df
=\frac1A\int|P(f)|^2D^{*2}(f)df.
}
```

**DERIVED / CONDITIONAL:** full-observation known-waveform detectability is a spectral overlap between waveform and detector signal-to-noise sensitivity.

Full derivation: `MATCHED_FILTER_SNR_STEP.md`.

---

## 2026-08-11 12:02 EDT — Unknown timing versus finite observation

Under stationary Gaussian full observation, equal complete `D*(f)` gives equal ideal unknown-arrival matched-filter search statistics.

A finite fixed record can nevertheless distinguish a pure-delay pair with identical complete magnitude `D*(f)`.

**DERIVED / COUNTEREXAMPLE:** finite truncation can make phase/temporal placement operationally relevant.

**Qualification:** known latency can remove this specific example.

Full derivation: `FINITE_WINDOW_PHASE_STEP.md`.

---

## 2026-08-11 12:09 EDT — Latency-compensated dispersion

A stable causal all-pass factor preserves magnitude response, complete magnitude `D*(f)`, and total infinite-time SNR while spreading a compact response into a tail.

Even after arbitrary constant alignment,

```math
\boxed{
\max_\delta\rho_{B,T}^2<\rho_{A,T}^2.
}
```

**DERIVED / COUNTEREXAMPLE:** the finite-window failure is not merely a pure-delay artifact.

Full derivation: `LATENCY_COMPENSATED_DISPERSION_STEP.md`.

---

## 2026-08-11 12:18 EDT — Exact SNR accumulation

For finite record `[0,t]`,

```math
\boxed{
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
}
```

and

```math
\boxed{
\eta(t)=\rho_t^2/\rho_\infty^2.
}
```

In white noise, `eta` is cumulative signal-energy fraction. For the ideal exponential response,

```math
\eta_\tau(t)=1-e^{-2t/\tau}.
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

With equal eventual SNR, early-deadline detection probabilities can differ radically even while eventual detection probabilities coincide.

Full derivation: `DEADLINE_DETECTION_PROBABILITY_STEP.md`.

---

## 2026-08-11 12:38 EDT — Independent-slot unknown-time search

For `M` independent Gaussian timing hypotheses scanned by their maximum,

```math
\boxed{
\gamma_{M,\alpha}
=\Phi^{-1}\!\left[(1-\alpha)^{1/M}\right].
}
```

**DERIVED / CONDITIONAL:** timing uncertainty consumes additional SNR margin through a global search threshold.

**Critical warning:** `M` is not the number of digital samples in a real continuous scan.

Full derivation: `UNKNOWN_TIME_SEARCH_STEP.md`.

---

## 2026-08-11 12:47 EDT — Continuous-time timing-search correlation

Define the full-observation noise-whitened template

```math
K(f)=\frac{G(f)P(f)}{\sqrt{S_n(f)}}
```

and normalized SNR spectral weight `W(f)=|K|^2/integral|K|^2`.

The normalized timing-scan covariance is

```math
\boxed{
r(\Delta)=\int W(f)e^{i2\pi f\Delta}df.
}
```

If the second moment exists,

```math
f_{rms}^2=\int f^2W(f)df
```

and Rice's exact mean upcrossing density for a differentiable unit-variance Gaussian scan is

```math
\boxed{
\nu_u^+=f_{rms}e^{-u^2/2}.
}
```

**REFINEMENT:** digital sample rate alone does not determine timing trials. For the same waveform, identical complete `D*(f)` gives identical full-observation search covariance and penalty.

**Regularity warning:** the ideal abrupt exponential has divergent second spectral moment in ideal white noise, so the Rice curvature formula requires physical high-frequency regularization or a smoother waveform.

Full derivation: `CONTINUOUS_TIME_SEARCH_CORRELATION_STEP.md`.

---

## 2026-08-11 13:01 EDT — Finite-deadline correction and search-penalty reversal

The finite-deadline SNR `rho_t` and Step-08 full-observation `f_rms` do **not** automatically belong to the same scan statistic.

For an actual finite-deadline unknown-time scan,

```math
q_t=C_t^{-1}s_t,
```

with exact translated noise-only covariance

```math
\boxed{
r_t(\Delta)
=\frac{
\int |Q_t(f)|^2S_n(f)e^{i2\pi f\Delta}df
}{
\int |Q_t(f)|^2S_n(f)df
}.
}
```

**REFINEMENT / CORRECTION:** do not combine finite-window `eta(t)` with full-template `f_rms` as one exact finite-deadline formula.

A stable causal equal-eventual-SNR family was then constructed:

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
```

with output

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
```

Its accumulation is

```math
\boxed{
\eta_\tau(t)
=1-e^{-2x}(1+2x+2x^2),
\qquad x=t/\tau.
}
```

The faster member has more finite-time SNR at every finite `t` while the SNR gap tends to zero.

Its full-template timing covariance scales exactly as

```math
\boxed{
r_\tau(\Delta)
=\left(1+\frac{|\Delta|}{\tau}\right)e^{-|\Delta|/\tau}.
}
```

Thus a faster member explores a longer normalized timing interval over the same physical monitoring duration and has a larger full-template global threshold.

Under standard convergence of finite-deadline scan thresholds to full-template thresholds, for sufficiently large finite `t`,

```math
P_{D,true,f}<P_{D,true,s}
```

while still

```math
\rho_{f,t}>\rho_{s,t}.
```

**DERIVED / CONDITIONAL:** faster SNR acquisition is not guaranteed to dominate unknown-time search complexity.

Full derivation: `SEARCH_PENALTY_REVERSAL_STEP.md`.

---

## 2026-08-11 13:18 EDT — Task-level detection-time surface

### Prompted continuation

Seek a compact task-level description that retains finite-time SNR accumulation and timing-search uncertainty without collapsing them into a universal scalar detector metric.

### Same finite-duration measurement for signal and search

For each candidate filter duration `t`, use

```math
q_t=C_t^{-1}s_t
```

with

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle.
```

Translate that same filter over the unknown-arrival interval `[0,L]` and define

```math
Z_{t,L}=\sup_{0\le\tau\le L}z_t(\tau).
```

At allowed global false-alarm probability `alpha`, define

```math
\boxed{
\gamma_t(L,\alpha)
=F^{-1}_{Z_{t,L}|H_0}(1-\alpha).
}
```

At the true event alignment,

```math
z_t(\tau_0)|H_1\sim N(\rho_t,1),
```

so

```math
\boxed{
P_{D,true}(t;L,\alpha)
=\Phi[\rho_t-\gamma_t(L,\alpha)].
}
```

Define the task margin

```math
\boxed{
m(t;L,\alpha)=\rho_t-\gamma_t(L,\alpha).
}
```

### Important refinement: deadline is not forced filter duration

The raw margin `m(t)` need not be monotone because changing `t` changes both accumulated SNR and timing-search threshold.

If the task allows maximum post-event delay `T`, the detector can always ignore later data and choose any `t<=T`:

```math
\boxed{
m^*(T;L,\alpha)
=\sup_{0<t\le T}m(t;L,\alpha).
}
```

Hence optimized by-deadline performance is nondecreasing even if a forced use-all-data statistic is not.

### Detection-time surface

For required event-attributable detection probability `beta`, define

```math
\boxed{
\mathcal T_D(\alpha,\beta,L)
=\inf\left\{
t>0:
\rho_t-\gamma_t(L,\alpha)
\ge\Phi^{-1}(\beta)
\right\}.
}
```

Set `mathcal T_D=infinity` if no duration can meet the operating point.

This surface maps

```text
allowed global false alarm alpha
required detection probability beta
arrival-time uncertainty interval L
```

to the minimum post-event decision delay.

It is explicitly task-specific. It requires the finite-record detector signal/noise response and the finite-duration timing-search covariance; it is not a detector-only replacement for `D*`.

### Feasibility and possible optimal filter duration

Define

```math
m_max(L,alpha)=sup_t [rho_t-gamma_t(L,alpha)].
```

The requested `(alpha,beta,L)` point is feasible under this true-time criterion iff

```math
m_max(L,alpha)>=Phi^{-1}(beta).
```

If the supremum is attained, a task-optimal filter duration can be defined by

```math
t_opt in argmax_t [rho_t-gamma_t(L,alpha)].
```

A finite interior optimum is possible in principle but has not yet been established for a concrete regime.

### Exact ordering properties

Under nested search protocols, the required detection time cannot decrease when:

```text
required beta increases,
allowed alpha decreases,
or timing-uncertainty interval L increases.
```

Known-time, independent-slot, and continuous correlated-search results from Steps 06–09 are recovered as special cases.

Full derivation: `DETECTION_TIME_SURFACE_STEP.md`.

### Next question, held open

For the Step-09 time-scaled equal-eventual-SNR family, does the detection-time surface collapse onto dimensionless variables such as `t/tau`, `L/tau`, `rho_infinity`, `P_FA`, and `P_D`, and does that reveal a finite optimal integration/filter duration in any regime?
