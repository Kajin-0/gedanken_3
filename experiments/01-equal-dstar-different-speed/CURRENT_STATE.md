# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 13:18 EDT  
**Status:** ten logical steps completed. Step 10 packages the exact finite-time/search results into a task-level detection-time surface rather than a universal detector scalar. It also distinguishes maximum allowed decision delay from the filter duration actually used: a rational detector may ignore later data, so optimized by-deadline performance is monotone even when a forced use-all-data search statistic is not. No novelty claim.

---

## 1. Original starting point

Two detectors satisfy

```math
D_A^*=D_B^*,
```

with

```math
\tau_A=1\ \mathrm{ns},
\qquad
\tau_B=1\ \mathrm{s}.
```

Original question: does equal conventional specific detectivity imply equal ability to detect an arbitrary optical signal?

---

## 2. Surviving chain through Step 04

### Step 01 — scalar reference `D*` is insufficient

A physically allowed first-order + additive-output-noise construction gives unequal temporal-signal SNR despite equal reference `D*`.

**Qualification:** if dominant noise is filtered by the same pole, signal/noise attenuation can cancel. Do not infer `fast is always better`.

### Step 02 — known-waveform full-observation SNR

```math
\boxed{
\rho_\infty^2
=\int |P(f)|^2\frac{|G(f)|^2}{S_n(f)}df
=\frac1A\int|P(f)|^2D^{*2}(f)df.
}
```

Complete magnitude `D*(f)` is sufficient for this restricted known-waveform/full-observation maximum-linear-SNR problem.

### Step 03 — unknown timing alone versus finite truncation

Under stationary Gaussian full observation, identical complete `D*(f)` gives identical matched-filter timing-search statistics.

Finite truncation can break the equivalence because magnitude `D*(f)` discards temporal phase/placement.

### Step 04 — pure-delay loophole removed

A causal all-pass phase factor can preserve complete magnitude `D*(f)` and total infinite-time SNR while changing finite-window SNR even after arbitrary latency compensation.

See the dedicated Step-01–04 files for full derivations.

---

## 3. Step 05 — exact finite-time SNR accumulation

For finite record `[0,t]`, with restricted covariance operator `C_t`,

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

For white-noise exponential output,

```math
\eta_\tau(t)=1-e^{-2t/\tau}.
```

This separates eventual detectability from the rate at which it becomes available.

---

## 4. Step 06 — fixed-deadline known-time detection

For the simple Gaussian known-time binary decision,

```math
\boxed{
P_D(t;\alpha)=
\Phi\!\left[
\rho_t-\Phi^{-1}(1-\alpha)
\right].
}
```

Equivalently, using `eta`,

```math
P_D=\Phi\!\left[
\rho_\infty\sqrt{\eta(t)}-
\Phi^{-1}(1-\alpha)
\right].
```

Equal eventual SNR can coexist with radically unequal early-deadline detection probability.

---

## 5. Step 07 — independent-slot unknown-time search

For `M` independent timing hypotheses scanned by their maximum,

```math
\boxed{
\gamma_{M,\alpha}
=\Phi^{-1}\!\left[(1-\alpha)^{1/M}\right].
}
```

Unknown timing consumes additional SNR margin through a global look-elsewhere threshold.

**Warning:** `M` is not digital sample count in a continuous timing scan.

---

## 6. Step 08 — continuous-time full-observation search

Define the full-observation noise-whitened template

```math
K(f)=\frac{G(f)P(f)}{\sqrt{S_n(f)}},
```

and normalized SNR spectral weight

```math
W(f)=\frac{|K(f)|^2}{\int|K(f')|^2df'}.
```

The normalized timing-scan covariance is

```math
\boxed{
r(\Delta)=\int W(f)e^{i2\pi f\Delta}df.
}
```

If the second moment exists,

```math
\boxed{
f_{\mathrm{rms}}^2=\int f^2W(f)df,
}
```

and for a differentiable stationary Gaussian scan, Rice gives

```math
\boxed{
\nu_u^+=f_{\mathrm{rms}}e^{-u^2/2}.
}
```

**REFINEMENT:** higher ADC sampling rate alone does not raise the trials factor. For the same waveform, identical complete magnitude `D*(f)` gives identical full-observation scan covariance and search penalty.

---

## 7. Step 09 — exact finite-deadline scan and conditional ranking reversal

### Correct finite-deadline search object

For a scan using only `t` seconds after each candidate event time, the filter is

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

**CORRECTION:** do not combine finite-window `eta(t)` with Step-08 full-template `f_rms` as if they were one exact finite-deadline statistic.

### Equal-eventual-SNR family

For

```math
p(t)=e^{-bt}u(t),
```

and

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
```

choose amplitude scaling so every member has identical `rho_infinity=rho_0`. The output is

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t),
```

with

```math
\boxed{
\eta_\tau(t)
=1-e^{-2x}(1+2x+2x^2),
\qquad x=t/\tau.
}
```

For `tau_f<tau_s`, the faster member has strictly larger finite-time SNR at every finite `t`, while the gap tends to zero.

The full-template search covariance is

```math
\boxed{
r_\tau(\Delta)
=\left(1+\frac{|\Delta|}{\tau}\right)e^{-|\Delta|/\tau}.
}
```

Thus a faster member searches a longer normalized timing interval over the same physical monitoring duration `L` and has a larger full-template global threshold.

Under standard convergence of the finite-deadline scan thresholds to their full-template values, a finite-deadline ranking reversal must occur for sufficiently large finite `t`:

```math
P_{D,true,f}<P_{D,true,s}
```

while still

```math
\rho_{f,t}>\rho_{s,t}.
```

**DERIVED / CONDITIONAL:** rapid SNR acquisition is not guaranteed to dominate unknown-time search complexity.

See `SEARCH_PENALTY_REVERSAL_STEP.md`.

---

## 8. Step 10 — task-level detection-time surface

Let the event arrival time be unknown over

```math
\tau_0\in[0,L].
```

For each chosen post-candidate filter duration `t`, define the normalized translated scan `z_t(tau)` using the same finite-duration optimal filter `q_t`.

Let

```math
Z_{t,L}=\sup_{0\le\tau\le L}z_t(\tau).
```

For a global false-alarm probability

```math
P_{FA}=\alpha,
```

define the exact finite-duration search threshold

```math
\boxed{
\gamma_t(L,\alpha)
=F^{-1}_{Z_{t,L}|H_0}(1-\alpha).
}
```

At the true event alignment,

```math
z_t(\tau_0)|H_1\sim\mathcal N(\rho_t,1),
```

so the event-attributable crossing probability is

```math
\boxed{
P_{D,true}(t;L,\alpha)
=\Phi\!\left[
\rho_t-\gamma_t(L,\alpha)
\right].
}
```

Define the raw task margin

```math
\boxed{
m(t;L,\alpha)
=\rho_t-\gamma_t(L,\alpha).
}
```

Unlike the known-time case, `m(t)` need not be monotone because both accumulated SNR and search threshold can change with filter duration.

### Rational by-deadline envelope

If the maximum allowed decision delay is `T`, the measurement may use any shorter filter duration `0<t<=T`. Therefore define

```math
\boxed{
m^*(T;L,\alpha)
=\sup_{0<t\le T}m(t;L,\alpha).
}
```

Then

```math
\boxed{
P_{D,true}^*(T;L,\alpha)
=\Phi[m^*(T;L,\alpha)].
}
```

and `m*(T)` is nondecreasing because extra available data may always be ignored.

### Detection-time surface

For required event-attributable probability

```math
P_D=\beta,
```

define

```math
\boxed{
\mathcal T_D(\alpha,\beta,L)
=
\inf\left\{
t>0:
\rho_t-\gamma_t(L,\alpha)
\ge
\Phi^{-1}(\beta)
\right\}.
}
```

If no filter duration satisfies the target, set

```math
\mathcal T_D=\infty.
```

This is a **task-level surface**, not a detector-only scalar. It maps

```text
allowed global false alarm alpha
required detection probability beta
arrival-time uncertainty interval L
```

to the minimum post-event decision delay.

It retains the full detector/waveform/noise dependence through

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle
```

and the finite-duration scan covariance/threshold generated by the same filter.

### Task-optimal filter duration

Define

```math
\boxed{
m_{\max}(L,\alpha)
=\sup_{t>0}[\rho_t-\gamma_t(L,\alpha)].
}
```

The requested `(alpha,beta,L)` point is feasible under this criterion iff

```math
m_{\max}(L,\alpha)\ge\Phi^{-1}(\beta).
```

If the supremum is attained, an optimal integration/filter duration can be defined by

```math
\boxed{
t_{\mathrm{opt}}
\in\operatorname*{arg\,max}_{t>0}
[\rho_t-\gamma_t(L,\alpha)].
}
```

A finite interior optimum is possible in principle, but has not yet been established for a concrete detector regime.

### Exact orderings

Under nested monitoring/search intervals:

- higher required `beta` cannot reduce `mathcal T_D`;
- smaller allowed `alpha` cannot reduce `mathcal T_D`;
- larger timing-uncertainty interval `L` cannot reduce `mathcal T_D`.

Known-time, independent-slot, and continuous correlated-search results from Steps 06–09 are recovered as special cases.

See `DETECTION_TIME_SURFACE_STEP.md`.

---

## 9. Current scientific frontier

The project now has a coherent task-level hierarchy:

```text
rho_infinity
    eventual known-time matched-filter separation

rho_t / eta(t)
    separation available to a chosen finite-duration filter

r_t(Delta)
    timing-search covariance for that same finite filter

gamma_t(L,alpha)
    global false-alarm threshold over unknown arrival time

m(t;L,alpha)=rho_t-gamma_t
    raw event-attributable detection margin

m*(T;L,alpha)
    best margin achievable by maximum allowed delay T

mathcal T_D(alpha,beta,L)
    minimum decision delay required for the specified task
```

This preserves the physics exposed by the thought experiment instead of compressing it prematurely into one speed/sensitivity number.

---

## 10. What has been established

- Scalar reference `D*` does not determine arbitrary temporal-signal SNR.
- Full-observation known-waveform SNR is `integral |P|^2|G|^2/S_n df`.
- Complete magnitude `D*(f)` is sufficient for that restricted full-observation problem.
- Finite observation can make magnitude `D*(f)` insufficient because phase/temporal dispersion controls SNR accumulation.
- Exact finite-record SNR is `rho_t^2=<s_t,C_t^-1s_t>`.
- Unknown timing raises a global threshold governed by the matched-filter timing covariance rather than digital sample count.
- The exact finite-deadline scan covariance is built from the finite-duration optimal filter.
- A controlled equal-eventual-SNR family admits conditional ranking reversal between faster SNR accumulation and finer timing-search resolution.
- A compact task-level detection-time surface can package accumulated SNR and timing-search uncertainty without pretending they are detector-only scalars.
- Optimizing over filter durations no longer than the allowed deadline guarantees that best by-deadline performance cannot degrade merely because more data become available.

---

## 11. What has not been established

- No universal statement that faster detectors are better or worse.
- No universal speed-detectivity tradeoff.
- No universal scalar replacement for `D*`.
- No exact closed-form finite-duration supremum threshold for arbitrary correlated scans.
- No proof yet that a finite interior `t_opt` occurs in the Step-09 family or in practical photodetectors.
- The defined surface uses true-alignment threshold crossing; exact global rejection/localization probabilities require the full signal-induced scan mean away from the true alignment.
- No Bayes-optimal unknown-time detector, repeated/sequential stopping, unknown amplitude/phase, signal-dependent noise, nonlinear response, saturation, dead time, or nonstationarity.
- No novelty claim.

---

## 12. Single natural next question — DO NOT ANSWER YET

> For the time-scaled equal-eventual-SNR family introduced in Step 09, does the detection-time surface collapse onto dimensionless variables such as `t/tau`, `L/tau`, `rho_infinity`, `P_FA`, and `P_D`, and does that reveal a finite optimal integration/filter duration in any regime?
