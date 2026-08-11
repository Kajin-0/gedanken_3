# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 13:50 EDT  
**Status:** thirteen logical steps completed. Step 13 directly simulates the correlated finite-duration Gaussian timing scan without an independent-trials approximation. The broad Step-12 regime structure is reproduced, but the apparent numerical crossover is not converged under timing-grid refinement. An exact covariance-cusp derivation explains the failure: every finite hard-window scan is locally Brownian-like / mean-square nondifferentiable in ideal white noise. Coarse crossover values are explicitly rejected. No universal replacement metric and no novelty claim.

---

## 1. Original question

Two detectors satisfy

```math
D_A^*=D_B^*
```

but initially have

```math
\tau_A=1\ \mathrm{ns},
\qquad
\tau_B=1\ \mathrm{s}.
```

Does equal conventional specific detectivity imply equal ability to detect an arbitrary optical signal?

---

## 2. Surviving logical chain

### Step 01 — scalar reference `D*` is insufficient

A physically allowed first-order + additive-output-noise example gives unequal temporal-signal SNR despite equal reference `D*` (`SNR_A/SNR_B ~ 6.36` for the explicit 1 Hz example).

**COUNTEREXAMPLE / QUALIFICATION:** equal scalar reference `D*` does not determine arbitrary-signal SNR. Signal/noise filtering can cancel, so do not infer `fast is always better`.

### Step 02 — full-observation known-waveform SNR

```math
\rho_\infty^2
=\int |P(f)|^2\frac{|G(f)|^2}{S_n(f)}df
=\frac1A\int |P(f)|^2D^{*2}(f)df.
```

Complete magnitude `D*(f)` is sufficient for this restricted known-waveform/full-observation maximum-linear-SNR problem.

### Step 03 — unknown timing negative result; finite-window failure

Under stationary Gaussian full observation, identical complete `D*(f)` gives identical ideal timing-search statistics.

**NEGATIVE RESULT:** unknown timing alone does not break the full-observation equivalence.

Finite truncation can break it because magnitude `D*(f)` discards temporal phase/placement.

### Step 04 — pure-delay loophole removed

A stable causal all-pass factor preserves complete magnitude `D*(f)` and total infinite-time SNR while changing finite-window SNR even after constant-latency compensation.

### Step 05 — exact finite-time SNR

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
\qquad
\eta(t)=\rho_t^2/\rho_\infty^2.
```

This separates eventual detectability from the rate at which it becomes available.

### Step 06 — known-time Gaussian decision

```math
P_D(t;\alpha)=\Phi[\rho_t-\Phi^{-1}(1-\alpha)].
```

Equal eventual SNR can coexist with radically unequal early-deadline detection probability.

### Step 07 — independent-slot unknown-time penalty

```math
\gamma_{M,\alpha}=\Phi^{-1}[(1-\alpha)^{1/M}].
```

**WARNING:** `M` is not digital sample count in a continuous scan.

### Step 08 — continuous-time full-template timing covariance

With

```math
K=GP/\sqrt{S_n},
\qquad
W=|K|^2/\int|K|^2df,
```

```math
r(\Delta)=\int W(f)e^{i2\pi f\Delta}df.
```

When the second spectral moment exists, `f_rms` controls local covariance curvature and Rice upcrossing density.

**REFINEMENT:** sample rate alone does not raise timing-search complexity. Identical complete `D*(f)` gives identical full-observation timing covariance for the same waveform.

### Step 09 — finite-deadline scan and conditional cross-detector reversal

The actual finite search must use

```math
q_t=C_t^{-1}s_t
```

and its own covariance `r_t(Delta)`.

**REJECTED / INVALID SHORTCUT:** finite-window `eta(t)` and full-template `f_rms` cannot be inserted into one exact finite-deadline formula without deriving the finite filter's search covariance.

A controlled equal-eventual-SNR family was introduced:

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
\qquad
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
```

Faster members accumulate more SNR at every finite duration but face a larger fixed-physical-`L` timing-search burden. Under standard finite-to-full threshold convergence, a cross-detector ranking reversal occurs.

### Step 10 — task-level detection-time surface

For each finite duration use the same filter for signal SNR and timing search:

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t>0:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

This is a task-level surface, not a detector scalar.

### Step 11 — exact dimensionless collapse; no finite interior filter optimum

For the scaled family,

```math
x=t/\tau,
\qquad
\ell=L/\tau,
```

```math
\mathcal T_D
=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

The exact finite-duration covariance is `R_x(|Delta|/tau)`. Pointwise covariance ordering plus Slepian comparison makes the search threshold nonincreasing with filter duration while SNR rises strictly.

**NEGATIVE RESULT:** this family has no finite interior `t_opt`; use all data allowed by the deadline. Step-09 reversal is cross-detector, not self-suboptimal filtering.

### Step 12 — exact fast/slow task-regime boundary

Let

```math
r=\tau_s/\tau_f>1,
\qquad
\ell=L/\tau_s.
```

The exact preference boundary is

```math
X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)=0.
```

**REJECTED SHORTCUT:** equality of asymptotic margins is not the minimum-decision-time boundary.

With

```math
c=\rho_0-\Phi^{-1}(\beta),
```

and full-template threshold `Gamma_infinity(ell,alpha)`, task space partitions into:

```text
both feasible:
    c > Gamma_infinity(r ell,alpha)

slow-only feasible:
    Gamma_infinity(ell,alpha) < c <= Gamma_infinity(r ell,alpha)

neither feasible:
    c <= Gamma_infinity(ell,alpha)
```

**DERIVED:** slow-only feasibility can occur; fast-only feasibility cannot under equal eventual SNR.

The physical timing-uncertainty feasibility scale obeys

```math
L_{crit}(\tau)=\tau\ell_{crit}.
```

Under standard continuity/extreme-value growth, at least one finite fast-to-slow crossover must occur; uniqueness remains open.

### Step 13 — direct correlated-scan numerics and rejected coarse crossover

The exact finite white-noise timing scan for the dimensionless hard-window template

```math
h_x(v)=v e^{-v}1_{[0,x]}(v)
```

is represented as

```math
z_x(u)
=\frac1{\sqrt{E_x}}\int_0^x h_x(v)dW(u+v),
```

with

```math
E_x=\int_0^xv^2e^{-2v}dv=\eta(x)/4.
```

A direct FFT moving-average Monte Carlo was implemented for the **correlated** grid-sampled process. No effective independent-trial count is used.

A method-validation case used

```text
rho_0=5
r=1.2
alpha=0.01
beta=0.90
```

rather than the original extreme ratio/tail before validating the numerical method.

The broad fast-to-slow regime structure appears, but the apparent crossover moves under timing-grid refinement:

```text
delta=0.05   -> diagnostic crossover around ell_s ~48.5–49.0
delta=0.025  -> diagnostic crossover around ell_s ~49.25–49.5
delta=0.0125 -> fast still favored at ell_s=49.5 in the sampled run
```

Path counts also differed, so this is not a clean extrapolation sequence.

**REJECTED PRELIMINARY RESULT:** do not quote `ell_x ~49` as the continuous-time crossover.

The exact reason is a covariance cusp. For `y>=0`, differentiating the finite-template autocovariance gives

```math
R_x'(0^+)=-\frac{h_x(x)^2}{2E_x}.
```

Thus

```math
\boxed{
a_x\equiv-R_x'(0^+)
=\frac{2x^2e^{-2x}}{\eta(x)}
}
```

and

```math
\boxed{
R_x(y)=1-a_x|y|+O(y^2).
}
```

Therefore

```math
\boxed{
E[(z(u+h)-z(u))^2]\sim2a_x|h|.
}
```

The finite hard-window scan is locally Brownian-like / mean-square nondifferentiable for every finite `x` in ideal white noise. A grid maximum therefore misses between-grid maxima with slow continuum convergence. Near the feasibility boundary, small threshold errors cause large `X_D` and crossover errors.

The full-template limit is smooth,

```math
R_\infty(y)=(1+|y|)e^{-|y|}=1-y^2/2+\cdots,
```

so the finite-hard-window and `x->infinity` limits do not commute. This explains why Step-08 smooth-process Rice theory cannot simply solve the exact finite-duration numerical problem.

See `NUMERICAL_SCAN_CONVERGENCE_STEP.md` and `numerics/correlated_scan_mc.py`.

---

## 3. Current frontier

The analytic regime structure is intact. The numerical problem is now sharply identified:

```text
Gamma(x,ell,alpha)
    exact continuous supremum threshold of a locally rough finite-window Gaussian scan
```

A simple fixed timing grid is not yet a controlled continuum solver near the crossover.

The next step should either:

1. derive/implement a justified between-grid or adaptive continuous-supremum correction for the cusp process; or
2. introduce a physical finite readout/noise bandwidth that regularizes the scan and then test whether the fast/slow task boundary survives.

---

## 4. What has been established

- Equal scalar reference `D*` does not determine arbitrary temporal-signal SNR.
- Complete `D*(f)` is sufficient only for the restricted full-observation known-waveform problem.
- Finite observation can make magnitude `D*(f)` insufficient because temporal phase/dispersion controls finite-time SNR.
- Exact finite-record SNR is `rho_t^2=<s_t,C_t^-1s_t>`.
- Unknown timing raises a global threshold governed by timing covariance, not sample count.
- Finite SNR and timing search must be derived from the same finite filter.
- The controlled family admits a conditional cross-detector ranking reversal and an exact task-regime boundary.
- **NEGATIVE RESULT:** no finite interior filter optimum exists for this family.
- **DERIVED:** slow-only feasibility is possible; fast-only feasibility is not under equal eventual SNR.
- **IMPLEMENTED:** direct correlated finite-scan Monte Carlo without independent-trials replacement.
- **FAILED / REJECTED:** coarse grid crossover estimates are not continuum-converged.
- **DERIVED:** exact finite-window cusp coefficient `a_x=2x^2 exp(-2x)/eta(x)` and local Brownian roughness explain the numerical failure.

---

## 5. What has not been established

- No converged continuous-time `Gamma(x,ell,alpha)` table.
- No trustworthy numerical crossover `L_x` or publishable phase diagram yet.
- No crossover uniqueness proof.
- No continuum correction for missed between-grid maxima.
- No rare-event method for `alpha~1e-6` yet.
- No universal speed/detectivity metric or detector ranking.
- No exact global-rejection/localization surface, Bayes-optimal unknown-time detector, sequential stopping, unknown amplitude/phase, signal-dependent noise, nonlinear response, saturation, dead time, or nonstationarity.
- No novelty claim.

---

## 6. Single natural next question — DO NOT ANSWER YET

> What is the cleanest controlled way to recover the continuous-time finite-window supremum — by a justified between-grid/adaptive treatment of the cusp process or by adding physical finite readout bandwidth — and does the fast/slow task boundary survive that regularization?
