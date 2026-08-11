# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 13:28 EDT  
**Status:** eleven logical steps completed. Step 11 derives an exact dimensionless form of the Step-10 task-level detection-time surface for the controlled equal-eventual-SNR time-scaled family. It also yields a negative result: within this family the true-alignment task margin increases strictly with filter duration, so no finite interior optimal integration duration exists. No universal replacement metric and no novelty claim.

---

## 1. Original starting point

Two hypothetical detectors satisfy

```math
D_A^*=D_B^*,
```

but have

```math
\tau_A=1\ \mathrm{ns},
\qquad
\tau_B=1\ \mathrm{s}.
```

Original question: does equal conventional specific detectivity imply equal ability to detect an arbitrary optical signal?

---

## 2. Surviving chain through Step 04

### Step 01 — scalar reference `D*` is insufficient

A physically allowed first-order response with additive output noise gives unequal temporal-signal SNR despite equal reference `D*`.

**Qualification:** signal and noise filtering can cancel. Do not infer `fast is always better`.

### Step 02 — full-observation known-waveform SNR

```math
\boxed{
\rho_\infty^2
=\int |P(f)|^2\frac{|G(f)|^2}{S_n(f)}df
=\frac1A\int |P(f)|^2D^{*2}(f)df.
}
```

Complete magnitude `D*(f)` is sufficient for this restricted known-waveform/full-observation maximum-linear-SNR problem.

### Step 03 — unknown timing alone versus finite truncation

Under stationary Gaussian full observation, identical complete `D*(f)` gives identical ideal timing-search statistics. Finite truncation can break the equivalence because magnitude `D*(f)` discards temporal phase/placement.

### Step 04 — pure-delay loophole removed

A stable causal all-pass factor can preserve complete magnitude `D*(f)` and total infinite-time SNR while changing finite-window SNR even after arbitrary constant latency compensation.

---

## 3. Step 05 — exact finite-time SNR

For a finite record `[0,t]`,

```math
\boxed{
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle.
}
```

Define

```math
\boxed{
\eta(t)=\rho_t^2/\rho_\infty^2.
}
```

This separates eventual detectability from the rate at which it becomes available.

---

## 4. Step 06 — known-time Gaussian decision

For the simple known-time test,

```math
\boxed{
P_D(t;\alpha)
=\Phi\!\left[
\rho_t-\Phi^{-1}(1-\alpha)
\right].
}
```

Equal eventual SNR can coexist with radically unequal early-deadline detection probability.

---

## 5. Step 07 — independent-slot unknown-time search

For `M` independent candidate arrival times scanned by their maximum,

```math
\boxed{
\gamma_{M,\alpha}
=\Phi^{-1}\!\left[(1-\alpha)^{1/M}\right].
}
```

Unknown timing consumes additional SNR margin through a global false-alarm threshold.

**Warning:** `M` is not digital sample count in a continuous timing scan.

---

## 6. Step 08 — continuous-time full-template search

With

```math
K(f)=\frac{G(f)P(f)}{\sqrt{S_n(f)}},
```

and normalized SNR spectral weight

```math
W(f)=\frac{|K(f)|^2}{\int|K(f')|^2df'},
```

the normalized timing-scan covariance is

```math
\boxed{
r(\Delta)=\int W(f)e^{i2\pi f\Delta}df.
}
```

When the second moment exists,

```math
f_{rms}^2=\int f^2W(f)df,
```

and a differentiable stationary Gaussian scan has Rice upcrossing density

```math
\nu_u^+=f_{rms}e^{-u^2/2}.
```

**REFINEMENT:** sample rate alone does not raise timing-search complexity. For the same waveform, identical complete magnitude `D*(f)` gives identical full-observation timing-search covariance.

---

## 7. Step 09 — exact finite-deadline scan and conditional ranking reversal

For a scan that uses only `t` seconds after each candidate event time, the correct finite filter is

```math
q_t=C_t^{-1}s_t.
```

Its exact stationary normalized noise-only scan covariance is

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

**CORRECTION:** do not combine finite-window `eta(t)` with the Step-08 full-template `f_rms` as if they belonged to one exact finite-deadline statistic.

A controlled equal-eventual-SNR family was constructed using

```math
p(t)=e^{-bt}u(t),
```

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
```

with output

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t)
```

and amplitude scaling chosen so every member has the same `rho_infinity=rho_0`.

For this family,

```math
\boxed{
\eta_\tau(t)
=1-e^{-2x}(1+2x+2x^2),
\qquad x=t/\tau.
}
```

The faster member has more finite-time SNR at every finite `t`, while the full-template timing covariance

```math
\boxed{
r_\tau(\Delta)
=\left(1+\frac{|\Delta|}{\tau}\right)e^{-|\Delta|/\tau}
}
```

implies a larger unknown-time search threshold over the same physical monitoring duration `L`.

Under standard convergence of finite-deadline thresholds to full-template thresholds, the detection ranking reverses for sufficiently large finite `t` even while the faster member still has more accumulated SNR.

**DERIVED / CONDITIONAL:** rapid SNR acquisition is not guaranteed to dominate timing-search complexity.

---

## 8. Step 10 — task-level detection-time surface

For each chosen filter duration `t`, use the same finite-duration optimal filter to compute both `rho_t` and the timing scan.

Let

```math
Z_{t,L}=\sup_{0\le\tau\le L}z_t(\tau).
```

Define the exact global false-alarm threshold

```math
\boxed{
\gamma_t(L,\alpha)
=F^{-1}_{Z_{t,L}|H_0}(1-\alpha).
}
```

At the true event alignment,

```math
\boxed{
P_{D,true}(t;L,\alpha)
=\Phi[\rho_t-\gamma_t(L,\alpha)].
}
```

Define

```math
m(t;L,\alpha)=\rho_t-\gamma_t(L,\alpha).
```

For maximum allowed delay `T`, a rational measurement can choose any `t<=T`, so

```math
m^*(T;L,\alpha)
=\sup_{0<t\le T}m(t;L,\alpha).
```

The task-level detection-time surface is

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

This is task-specific, not a detector-only replacement for `D*`.

---

## 9. Step 11 — exact dimensionless collapse

For the Step-09 family define

```math
x=\frac{t}{\tau},
\qquad
\ell=\frac{L}{\tau}.
```

The finite-time SNR is

```math
\boxed{
\rho_{\tau,t}=\rho_0\sqrt{\eta(x)},
}
```

with

```math
\eta(x)=1-e^{-2x}(1+2x+2x^2).
```

The exact finite-duration white-noise timing covariance scales as

```math
\boxed{
r_{\tau,t}(\Delta)
=R_x(|\Delta|/\tau),
}
```

where

```math
\boxed{
R_x(y)
=\frac{
\int_0^{x-y}v(v+y)e^{-2v-y}dv
}{
\int_0^x v^2e^{-2v}dv
},
\quad 0\le y<x,
}
```

and `R_x(y)=0` for `y>=x`.

Therefore the exact global threshold has the dimensionless form

```math
\boxed{
\gamma_{\tau,t}(L,\alpha)
=\Gamma(x,\ell,\alpha).
}
```

Define

```math
M(x;\ell,\rho_0,\alpha)
=\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha).
```

Then

```math
\boxed{
\mathcal T_D(\alpha,\beta,L;\tau,\rho_0)
=\tau\,
X_D\!\left(
\rho_0,\alpha,\beta,\frac{L}{\tau}
\right),
}
```

where

```math
X_D
=\inf\{x>0:M(x)\ge\Phi^{-1}(\beta)\}.
```

This is the exact dimensionless detection-surface collapse.

### Filter-duration ordering

For every fixed dimensionless lag `y`, `R_x(y)` is nondecreasing with `x`. The proof writes `R_x(y)` as a positive-weight average of the nondecreasing function

```math
H_y(v)=0\ (v<y),
\qquad
H_y(v)=e^y(1-y/v)\ (v\ge y).
```

Thus for `x_2>x_1`,

```math
R_{x_2}(y)\ge R_{x_1}(y)
\qquad\forall y.
```

By Slepian Gaussian comparison, the more correlated longer-filter scan has a global supremum threshold satisfying

```math
\boxed{
\Gamma(x_2,\ell,\alpha)
\le
\Gamma(x_1,\ell,\alpha).
}
```

Meanwhile

```math
\eta'(x)=4x^2e^{-2x}>0.
```

Therefore

```math
\boxed{
M(x;\ell,\rho_0,\alpha)
\text{ is strictly increasing in }x.
}
```

### Negative result: no finite interior `t_opt`

For this family,

```math
\boxed{
\operatorname*{arg\,max}_{0<t\le T}
[\rho_t-\gamma_t(L,\alpha)]
=\{T\}.
}
```

So the optimal filter always uses all data allowed by the deadline. The generic finite-interior-`t_opt` possibility from Step 10 is **not realized** here.

This does not undo Step 09. Each detector individually improves with longer filtering; the cross-detector reversal arises because, at fixed physical `L`, a faster detector has the larger dimensionless search domain

```math
L/\tau.
```

See `DIMENSIONLESS_DETECTION_SURFACE_STEP.md`.

---

## 10. Current scientific frontier

The controlled family now has the exact task structure

```text
rho_0
    equal eventual known-time SNR

x=t/tau
    dimensionless chosen filter duration

ell=L/tau
    dimensionless arrival-time uncertainty

eta(x)
    finite-time SNR accumulation

R_x(y)
    exact finite-duration timing-search covariance

Gamma(x,ell,alpha)
    exact global false-alarm threshold

M(x)=rho_0 sqrt(eta)-Gamma
    true-alignment task margin

T_D/tau = X_D(rho_0,alpha,beta,L/tau)
    dimensionless detection-time surface
```

A smaller `tau` has two competing consequences at fixed physical `L`:

```text
smaller physical time unit -> helps
larger L/tau search domain -> hurts
```

For one fixed detector, however, longer filter duration always helps in this family.

---

## 11. What has been established

- Scalar reference `D*` does not determine arbitrary temporal-signal SNR.
- Full-observation known-waveform SNR is `integral |P|^2|G|^2/S_n df`.
- Complete magnitude `D*(f)` is sufficient for that restricted full-observation problem.
- Finite observation can make magnitude `D*(f)` insufficient because temporal phase/dispersion controls finite-time SNR.
- Exact finite-record SNR is `rho_t^2=<s_t,C_t^-1s_t>`.
- Unknown timing raises a global threshold governed by matched-filter timing covariance rather than sample count.
- The finite-deadline search covariance must be derived from the same finite filter used to obtain `rho_t`.
- A controlled equal-eventual-SNR family permits conditional cross-detector ranking reversal.
- A task-level detection-time surface packages finite-time SNR and unknown-time search without collapsing them into a universal scalar.
- For the Step-09 family, that surface collapses exactly onto `rho_0`, `alpha`, `beta`, `t/tau`, and `L/tau`.
- **NEGATIVE RESULT:** no finite interior integration optimum exists for this family; the task margin increases strictly with filter duration.

---

## 12. What has not been established

- No universal statement that faster detectors are better or worse.
- No universal speed-detectivity tradeoff.
- No universal scalar replacement for `D*`.
- No closed-form exact correlated-scan threshold `Gamma(x,ell,alpha)`.
- No universal monotonic ordering of detection time with detector `tau` at fixed physical `L`.
- No claim that all detector families have monotone filter-duration margins.
- No exact global-rejection/localization surface; current `P_D` is true-alignment threshold crossing.
- No Bayes-optimal unknown-time detector, sequential stopping, unknown amplitude/phase, signal-dependent noise, nonlinear response, saturation, dead time, or nonstationarity.
- No novelty claim.

---

## 13. Single natural next question — DO NOT ANSWER YET

> For two members of this family with different `tau` but equal `rho_0`, what is the boundary in task space `(L, alpha, beta)` where their detection-time surfaces cross — i.e. where the detector that reaches the required decision first switches from the faster member to the slower member?
