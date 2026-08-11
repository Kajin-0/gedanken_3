# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 13:01 EDT  
**Status:** nine logical steps completed. Step 09 shows conditionally that a faster detector's larger unknown-time search penalty can reverse its finite-time detection ranking even while it still has more accumulated SNR. It also corrects a tempting but invalid shortcut: finite-deadline `eta(T)` cannot be combined directly with Step-08 full-observation `f_rms` without deriving the finite-deadline scan covariance. No universal replacement metric or novelty claim.

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

## 2. Surviving chain through Step 08

### Step 01 — scalar reference D* is insufficient

A physically allowed first-order + additive-output-noise construction gives unequal temporal-signal SNR despite equal reference `D*`.

**Qualification:** if dominant noise is filtered by the same pole, signal/noise attenuation can cancel. Do not infer `fast is always better`.

### Step 02 — known-waveform full-observation SNR

```math
\boxed{
\rho_\infty^2
=\int |P(f)|^2\frac{|G(f)|^2}{S_n(f)}df
=\frac1A\int |P(f)|^2D^{*2}(f)df.
}
```

Complete magnitude `D*(f)` is sufficient for this restricted known-waveform/full-observation maximum-linear-SNR problem.

### Step 03 — unknown timing alone versus finite truncation

Under stationary Gaussian full observation, identical complete `D*(f)` gives identical matched-filter timing-search statistics.

Finite truncation can break the equivalence because magnitude `D*(f)` discards temporal phase/placement.

### Step 04 — pure-delay loophole removed

A causal all-pass phase factor can preserve complete magnitude `D*(f)` and total infinite-time SNR while changing finite-window SNR even after arbitrary latency compensation.

### Step 05 — exact finite-time SNR accumulation

For finite record `[0,T]`,

```math
\boxed{
\rho_T^2=\langle s_T,C_T^{-1}s_T\rangle,
}
```

```math
\boxed{
\eta(T)=\rho_T^2/\rho_\infty^2.
}
```

This separates eventual detectability from rate of access to it.

### Step 06 — fixed-deadline detection probability

For the simple known-time Gaussian decision,

```math
\boxed{
P_D(T;\alpha)=
\Phi\!\left[
\rho_\infty\sqrt{\eta(T)}-
\Phi^{-1}(1-\alpha)
\right].
}
```

Equal eventual SNR can coexist with radically unequal early-deadline detection probability.

### Step 07 — independent-slot unknown-time search penalty

For `M` independent timing hypotheses scanned by their maximum,

```math
\boxed{
\gamma_{M,\alpha}
=\Phi^{-1}\!\left[(1-\alpha)^{1/M}\right].
}
```

Unknown timing consumes additional SNR margin through a global look-elsewhere threshold.

### Step 08 — continuous-time search correlation

For full observation, define

```math
K(f)=\frac{G(f)P(f)}{\sqrt{S_n(f)}},
```

```math
W(f)=\frac{|K(f)|^2}{\int|K(f')|^2df'}.
```

The normalized timing-scan covariance is

```math
\boxed{
r(\Delta)=\int W(f)e^{i2\pi f\Delta}df.
}
```

If the second spectral moment exists,

```math
\boxed{
f_{\mathrm{rms}}^2=\int f^2W(f)df,
}
```

```math
\boxed{
\tau_{\mathrm{curv}}=1/(2\pi f_{\mathrm{rms}}).
}
```

For a differentiable stationary Gaussian scan, Rice gives exact mean upcrossing density

```math
\boxed{
\nu_u^+=f_{\mathrm{rms}}e^{-u^2/2}.
}
```

**REFINEMENT:** higher ADC sampling rate alone does not raise the trials penalty. For the same waveform, identical complete magnitude `D*(f)` gives identical full-observation scan covariance and search penalty.

---

## 3. Step 09 — finite-deadline search and ranking reversal

### 3.1 Correction: finite-deadline eta and full-template f_rms are not one statistic

For an unknown-arrival scan that must decide using only `T` seconds after each candidate arrival, the actual optimal filter is

```math
q_T=C_T^{-1}s_T.
```

Its translated normalized noise-only scan has exact covariance

```math
\boxed{
r_T(\Delta)
=
\frac{
\int |Q_T(f)|^2S_n(f)e^{i2\pi f\Delta}df
}{
\int |Q_T(f)|^2S_n(f)df
},
}
```

where `Q_T` is the transform of `q_T`.

Therefore one must **not** combine Step-05 finite-window `rho_T` or `eta(T)` with Step-08 full-observation `f_rms` as though they were an exact single finite-deadline protocol.

Hard truncation can also destroy differentiability at the window boundary, so the Step-08 Rice curvature formula may require physical bandwidth regularization or a non-differentiable extreme-value treatment.

### 3.2 Equal-eventual-SNR time-scaled detector family

Use the same optical event

```math
p(t)=e^{-bt}u(t),
```

and stable causal family

```math
G_\tau(s)
=A_\tau\frac{s+b}{(s+1/\tau)^2}.
```

The output is

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
```

With equal white output-noise PSD `N`, choose

```math
A_\tau=\frac{2\rho_0\sqrt N}{\tau^{3/2}},
```

so every detector has exactly

```math
\rho_{\tau,\infty}=\rho_0.
```

Its finite-time SNR-squared accumulation is

```math
\boxed{
\eta_\tau(T)
=1-e^{-2x}(1+2x+2x^2),
\qquad x=T/\tau.
}
```

Hence for `tau_f<tau_s`,

```math
\rho_{f,T}>\rho_{s,T}
```

for every finite `T`, while both converge to `rho_0`.

### 3.3 Exact full-template search-threshold ordering

For this family, the full-observation timing-scan covariance is

```math
\boxed{
r_\tau(\Delta)
=\left(1+\frac{|\Delta|}{\tau}\right)
 e^{-|\Delta|/\tau}.
}
```

Thus

```math
z_\tau(t)\overset d=z_1(t/\tau).
```

Searching a fixed physical monitoring duration `L` is equivalent to searching the base process over `[0,L/tau]`.

Therefore the faster detector (`tau_f<tau_s`) has an exact full-template global threshold satisfying

```math
\boxed{
\gamma_f^\infty(L,\alpha)
>\gamma_s^\infty(L,\alpha)
}
```

for ordinary nontrivial false-alarm quantiles.

### 3.4 Conditional finite-deadline reversal theorem

Let `gamma_{i,T}(L,alpha)` be the exact threshold of the actual finite-deadline scan. Assume the standard regular convergence

```math
\gamma_{i,T}\to\gamma_i^\infty
\qquad (T\to\infty).
```

The fast finite-time SNR advantage

```math
\Delta\rho_T
=\rho_{f,T}-\rho_{s,T}
```

is positive for every finite `T` but tends to zero.

The search-threshold difference

```math
\Delta\gamma_T
=\gamma_{f,T}-\gamma_{s,T}
```

converges to the strictly positive full-template threshold gap.

Therefore, for sufficiently large but finite `T`,

```math
\boxed{
0<\Delta\rho_T<\Delta\gamma_T.
}
```

The Gaussian true-time crossing margin is

```math
m_i=\rho_{i,T}-\gamma_{i,T}.
```

Hence

```math
\boxed{
m_f<m_s
}
```

and therefore

```math
\boxed{
P_{D,true,f}(T)<P_{D,true,s}(T)
}
```

**even though**

```math
\boxed{
\rho_{f,T}>\rho_{s,T}.
}
```

**DERIVED / CONDITIONAL:** faster SNR accumulation is not guaranteed to dominate the statistical cost of finer unknown-arrival-time resolution.

This does not contradict Step 03 because the present family has equal integrated asymptotic SNR but different SNR-weighted spectra; it does not have identical complete `D*(f)`.

See `SEARCH_PENALTY_REVERSAL_STEP.md`.

---

## 4. Current scientific frontier

The project now has one internally consistent task-level structure:

```text
rho_infinity
    eventual known-time matched-filter separation

rho_T / eta(T)
    finite-deadline accessible separation

r_T(Delta)
    finite-deadline unknown-time search covariance

gamma_T(L,alpha)
    global search threshold set by that covariance and monitoring interval

P_D,true
    controlled by rho_T - gamma_T in the simple Gaussian max-scan setting
```

The key lesson is no longer a monotonic `speed versus sensitivity` tradeoff. Deadline performance can be improved by faster SNR acquisition yet degraded by finer timing-search resolution, and either effect can dominate depending on the task.

---

## 5. What has been established

- Equal reference scalar `D*` does not determine arbitrary temporal-signal SNR.
- Full-observation known-waveform SNR is `integral |P|^2|G|^2/S_n df`.
- Complete magnitude `D*(f)` is sufficient for that restricted full-observation problem.
- Finite observation can make magnitude `D*(f)` insufficient because phase/temporal dispersion controls SNR accumulation.
- Exact finite-record SNR is `rho_T^2=<s_T,C_T^-1s_T>`.
- Unknown timing raises a global search threshold determined by the matched-filter scan covariance rather than sample count.
- The exact finite-deadline search covariance is built from the finite-window optimal filter `q_T`, not the full template.
- In a controlled equal-eventual-SNR time-scaled family, faster response gives more accumulated SNR at every finite deadline but also a larger full-template timing-search threshold.
- **CONDITIONAL REVERSAL:** under standard finite-to-full scan convergence, the larger search penalty must eventually reverse the finite-time detection ranking at some finite deadline.

---

## 6. What has not been established

- No universal statement that faster detectors are better or worse.
- No universal speed-detectivity tradeoff.
- No universal scalar replacement for `D*`.
- No exact closed-form finite-deadline supremum threshold for the Step-09 family.
- No universal reversal deadline `T_0`.
- No claim that ranking reversal is common in practical photodetectors; Step 09 is an existence/conditional result.
- No Bayes-optimal unknown-time detector, repeated/sequential stopping, unknown amplitude/phase, signal-dependent noise, nonlinear response, saturation, dead time, or nonstationary treatment.
- No novelty claim.

---

## 7. Single natural next question — DO NOT ANSWER YET

> Is there a compact task-level description — perhaps a detection-time surface in `(P_FA, P_D, L)` rather than a scalar figure of merit — that contains both SNR accumulation and timing-search uncertainty without discarding the detector response information exposed in Steps 01–09?
