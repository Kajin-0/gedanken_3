# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 13:39 EDT  
**Status:** twelve logical steps completed. Step 12 converts the prior existence result into an analytic task-regime structure for two time-scaled equal-eventual-SNR detectors: an exact implicit fast/slow detection-time boundary, a slow-only feasibility region, no fast-only feasibility region, and—under standard continuity/extreme-value conditions—at least one finite fast-to-slow crossover as timing uncertainty grows. No universal replacement metric and no novelty claim.

---

## 1. Original starting point

Two hypothetical detectors satisfy

```math
D_A^*=D_B^*,
```

but have very different temporal responses, initially

```math
\tau_A=1\ \mathrm{ns},
\qquad
\tau_B=1\ \mathrm{s}.
```

Question: does equal conventional specific detectivity imply equal ability to detect an arbitrary optical signal?

---

## 2. Surviving logical chain

### Step 01 — scalar reference D* is insufficient

A physically allowed first-order response plus additive output noise gives unequal temporal-signal SNR despite equal reference `D*`; the explicit 1 Hz example gives `SNR_A/SNR_B ~ 6.36`.

**COUNTEREXAMPLE / QUALIFICATION:** equal reference `D*` does not determine arbitrary-signal SNR. If dominant noise is filtered by the same pole, signal/noise attenuation can cancel. Do not infer `fast is always better`.

### Step 02 — known-waveform full-observation SNR

For waveform `P(f)`, transfer `G(f)`, and stationary additive output-noise PSD `S_n(f)`,

```math
\boxed{
\rho_\infty^2
=\int |P(f)|^2\frac{|G(f)|^2}{S_n(f)}df
=\frac1A\int |P(f)|^2D^{*2}(f)df.
}
```

Complete magnitude `D*(f)` is sufficient for this restricted known-waveform/full-observation maximum-linear-SNR problem.

### Step 03 — unknown timing negative result; finite truncation counterexample

Under stationary Gaussian full observation, identical complete `D*(f)` gives identical ideal unknown-arrival matched-filter search statistics.

**NEGATIVE RESULT:** unknown arrival time alone does not break the ideal equivalence.

A finite fixed record can nevertheless distinguish detectors with identical magnitude `D*(f)` because phase/temporal placement is discarded.

### Step 04 — pure-delay loophole removed

A stable causal all-pass factor preserves complete magnitude `D*(f)` and total infinite-time SNR while changing finite-window SNR even after arbitrary constant latency compensation.

**COUNTEREXAMPLE:** nonlinear phase/dispersion can redistribute when recoverable SNR appears.

### Step 05 — exact finite-time SNR accumulation

For finite record `[0,t]`,

```math
\boxed{
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
}
```

```math
\boxed{
\eta(t)=\rho_t^2/\rho_\infty^2.
}
```

This separates eventual detectability from the rate at which it becomes available.

### Step 06 — known-time Gaussian detection probability

```math
\boxed{
P_D(t;\alpha)
=\Phi\!\left[
\rho_t-\Phi^{-1}(1-\alpha)
\right].
}
```

Equal eventual SNR can coexist with radically unequal early-deadline detection probability.

### Step 07 — independent-slot unknown-time search penalty

For `M` independent candidate arrival times,

```math
\boxed{
\gamma_{M,\alpha}
=\Phi^{-1}\!\left[(1-\alpha)^{1/M}\right].
}
```

Unknown timing consumes additional SNR margin through a global search threshold.

**WARNING:** `M` is not digital sample count in a continuous timing scan.

### Step 08 — continuous-time full-template search correlation

With

```math
K(f)=\frac{G(f)P(f)}{\sqrt{S_n(f)}},
\qquad
W(f)=\frac{|K(f)|^2}{\int|K|^2df},
```

```math
\boxed{
r(\Delta)=\int W(f)e^{i2\pi f\Delta}df.
}
```

When the second spectral moment exists, `f_rms^2=integral f^2W df`; differentiable Gaussian scans obey Rice upcrossing statistics.

**REFINEMENT:** sample rate alone does not raise timing-search complexity. For the same waveform, identical complete `D*(f)` gives identical full-observation timing covariance.

**REGULARITY WARNING:** the ideal abrupt exponential used earlier has divergent second spectral moment in ideal white noise, so Rice curvature requires physical high-frequency regularization or a smoother waveform.

### Step 09 — exact finite-deadline scan and conditional ranking reversal

The actual finite-deadline scan uses

```math
q_t=C_t^{-1}s_t
```

with exact timing covariance

```math
\boxed{
r_t(\Delta)
=\frac{\int |Q_t(f)|^2S_n(f)e^{i2\pi f\Delta}df}
{\int |Q_t(f)|^2S_n(f)df}.
}
```

**CORRECTION / INVALID SHORTCUT:** finite-window `eta(t)` cannot be combined directly with Step-08 full-template `f_rms` as one exact finite-deadline statistic.

A controlled equal-eventual-SNR family was introduced:

```math
p(t)=e^{-bt}u(t),
```

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
```

with

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t)
```

and amplitude scaling chosen so every member has the same `rho_infinity=rho_0`.

Its accumulation is

```math
\eta_\tau(t)=1-e^{-2x}(1+2x+2x^2),
\qquad x=t/\tau.
```

Faster members have more finite-time SNR at every finite duration, but their full-template timing search over fixed physical `L` has a larger threshold. Under standard finite-to-full threshold convergence, a finite-deadline cross-detector ranking reversal occurs.

### Step 10 — task-level detection-time surface

For each chosen filter duration `t`, compute finite SNR and timing-search threshold from the same filter.

```math
Z_{t,L}=\sup_{0\le\tau\le L}z_t(\tau),
```

```math
\gamma_t(L,\alpha)
=F^{-1}_{Z_{t,L}|H_0}(1-\alpha),
```

```math
P_{D,true}(t;L,\alpha)
=\Phi[\rho_t-\gamma_t(L,\alpha)].
```

Define

```math
\boxed{
\mathcal T_D(\alpha,\beta,L)
=\inf\{t>0:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
}
```

This is a task-level surface, not a detector-only replacement for `D*`.

A generic finite interior optimal filter duration was left open.

### Step 11 — exact dimensionless collapse and negative filter-optimum result

For the Step-09 family,

```math
x=t/\tau,
\qquad
\ell=L/\tau,
```

```math
\rho_{\tau,t}=\rho_0\sqrt{\eta(x)},
```

and

```math
r_{\tau,t}(\Delta)=R_x(|\Delta|/\tau),
```

where

```math
R_x(y)
=\frac{\int_0^{x-y}v(v+y)e^{-2v-y}dv}
{\int_0^x v^2e^{-2v}dv}
```

for `0<=y<x`, zero otherwise.

Thus

```math
\gamma_{\tau,t}(L,\alpha)=\Gamma(x,\ell,\alpha),
```

and

```math
\boxed{
\mathcal T_D
=\tau X_D\!\left(\rho_0,\alpha,\beta,\frac{L}{\tau}\right).
}
```

For fixed lag, `R_x` is nondecreasing with filter duration. Slepian comparison makes the global threshold nonincreasing with `x`, while `eta'(x)>0`.

**NEGATIVE RESULT:** this family has no finite interior `t_opt`; the optimal filter uses all data allowed by the deadline. Step-09 reversal is therefore a cross-detector scaling effect, not poor filter-duration choice.

### Step 12 — exact fast/slow task-regime boundary

Let

```math
r=\tau_s/\tau_f>1,
\qquad
\ell=L/\tau_s.
```

Then

```math
T_{D,f}=\tau_f X_D(\rho_0,\alpha,\beta,r\ell),
```

```math
T_{D,s}=r\tau_f X_D(\rho_0,\alpha,\beta,\ell).
```

The exact detection-time crossover boundary is

```math
\boxed{
B_r
= X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)=0.
}
```

**REJECTED SHORTCUT:** equality of asymptotic margins is not the preference boundary. The slow detector has the better asymptotic search margin for every `L>0`, yet the fast detector wins at `L=0` and sufficiently small `L` because its physical time unit is smaller.

Define

```math
c=\rho_0-\Phi^{-1}(\beta)
```

and the full-template threshold `Gamma_infinity(ell,alpha)`. Feasibility partitions exactly into:

```text
both feasible:
    c > Gamma_infinity(r ell,alpha)

slow-only feasible:
    Gamma_infinity(ell,alpha) < c <= Gamma_infinity(r ell,alpha)

neither feasible:
    c <= Gamma_infinity(ell,alpha)
```

Because the fast member always has the larger normalized search domain, **fast-only feasibility is impossible** under equal `rho_0`.

Define the dimensionless feasibility limit

```math
\ell_{crit}
=\sup\{\ell:\Gamma_\infty(\ell,\alpha)<\rho_0-\Phi^{-1}(\beta)\}.
```

Then

```math
\boxed{L_{crit}(\tau)=\tau\ell_{crit}.}
```

Hence

```math
\boxed{L_{crit,s}/L_{crit,f}=\tau_s/\tau_f=r.}
```

Under standard continuity and Gaussian extreme-value growth, fast wins at `L=0`, fast becomes infeasible first as `L` grows, and slow remains feasible there. Therefore at least one finite crossover

```math
L_\times\in(0,L_{crit,f})
```

must occur. **No uniqueness has been proved.**

A high-threshold Rice approximation can estimate `ell_crit`, but not the exact crossover surface; exact `Gamma(x,ell,alpha)` remains unresolved.

See `TASK_REGIME_BOUNDARY_STEP.md`.

---

## 3. Current scientific frontier

For the controlled family, the task hierarchy is now

```text
rho_0
    equal eventual known-time SNR

x=t/tau
    dimensionless filter duration

ell=L/tau
    dimensionless timing uncertainty

eta(x)
    finite-time SNR accumulation

R_x
    exact finite-duration timing covariance

Gamma(x,ell,alpha)
    exact global correlated-search threshold

X_D
    dimensionless minimum decision delay

B_r=0
    fast/slow detection-time crossover boundary

Gamma_infinity vs rho_0-Phi^{-1}(beta)
    feasibility partition
```

The project now predicts four qualitative task regimes as timing uncertainty grows:

```text
small L -> fast wins
intermediate L -> crossover within both-feasible region
larger L -> slow-only feasible
still larger L -> neither feasible
```

No fast-only feasibility regime exists in this equal-eventual-SNR scaled family.

---

## 4. What has been established

- Equal reference scalar `D*` does not determine arbitrary temporal-signal SNR.
- Complete magnitude `D*(f)` is sufficient only for the restricted full-observation known-waveform problem.
- Finite observation can make magnitude `D*(f)` insufficient because temporal phase/dispersion controls SNR accumulation.
- Exact finite-record SNR is `rho_t^2=<s_t,C_t^-1s_t>`.
- Unknown timing raises a global search threshold governed by matched-filter timing covariance, not sample count.
- Finite-deadline SNR and timing search must be derived from the same finite filter.
- The controlled equal-eventual-SNR family admits a conditional cross-detector ranking reversal.
- Its task-level detection-time surface collapses exactly onto dimensionless variables.
- **NEGATIVE RESULT:** no finite interior filter optimum exists for this family.
- **DERIVED:** the fast/slow preference boundary is an implicit task-space surface `B_r=0`.
- **DERIVED:** slow-only feasibility can occur, fast-only feasibility cannot, and physical timing-uncertainty tolerance scales linearly with `tau`.
- **DERIVED / CONDITIONAL:** at least one finite fast-to-slow crossover exists as timing uncertainty grows.

---

## 5. What has not been established

- No universal statement that faster detectors are better or worse.
- No universal speed-detectivity tradeoff or scalar replacement for `D*`.
- No exact closed form for the correlated Gaussian supremum threshold `Gamma(x,ell,alpha)`.
- No exact numerical crossover `L_x` yet and no proof of crossover uniqueness.
- No claim that the extreme `1 ns` versus `1 s` scaling is representative of practical photodetectors.
- No exact global-rejection/localization boundary; the criterion remains true-alignment threshold crossing.
- No Bayes-optimal unknown-time detector, sequential stopping, unknown amplitude/phase, signal-dependent noise, nonlinear response, saturation, dead time, or nonstationarity.
- No novelty claim.

---

## 6. Single natural next question — DO NOT ANSWER YET

> Can the finite-duration Gaussian scan with covariance `R_x` be computed numerically accurately enough to map `Gamma(x,ell,alpha)`, solve `B_r=0`, and produce an actual fast/slow phase diagram for chosen `(rho_0,r,alpha,beta)` without reverting to an uncontrolled independent-trials approximation?
