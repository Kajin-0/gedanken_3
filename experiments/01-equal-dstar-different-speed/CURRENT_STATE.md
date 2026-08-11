# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 14:10 EDT  
**Status:** fourteen logical steps completed. Step 14 shows that a true finite accessible measurement bandwidth removes the Step-13 finite-window covariance cusp and restores a smooth continuous timing scan. It also shows that merely appending a noiseless invertible common low-pass is not enough, because optimal whitening can cancel it. For a similarity-preserving finite-bandwidth version of the controlled family, the fast/slow task-regime boundary survives with an added dimensionless bandwidth parameter. No universal replacement metric and no novelty claim.

---

## 1. Original question

Two hypothetical detectors satisfy

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

### Step 01 — scalar reference D* insufficiency

Equal reference `D*` does not guarantee equal SNR for arbitrary temporal signals. The explicit 1 Hz first-order/additive-output-noise counterexample gave `SNR_A/SNR_B ~ 6.36`.

**QUALIFICATION:** signal/noise filtering can cancel; do not infer `fast is always better`.

### Step 02 — known-waveform full-observation SNR

```math
\rho_\infty^2
=\int |P(f)|^2\frac{|G(f)|^2}{S_n(f)}df
=\frac1A\int |P(f)|^2D^{*2}(f)df.
```

Complete magnitude `D*(f)` is sufficient for this restricted known-waveform/full-observation problem.

### Step 03 — unknown timing negative result; finite truncation failure

Under stationary Gaussian full observation, identical complete `D*(f)` gives identical timing-search statistics.

**NEGATIVE RESULT:** unknown timing alone does not break that equivalence.

Finite truncation can break it because magnitude `D*(f)` discards temporal phase/placement.

### Step 04 — pure-delay loophole removed

A stable causal all-pass phase factor preserves complete magnitude `D*(f)` and total infinite-time SNR while changing finite-window SNR after constant-latency compensation.

### Step 05 — exact finite-time SNR

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
\qquad
\eta(t)=\rho_t^2/\rho_\infty^2.
```

This separates eventual detectability from rate of access to it.

### Step 06 — known-time Gaussian decision

```math
P_D(t;\alpha)=\Phi[\rho_t-\Phi^{-1}(1-\alpha)].
```

### Step 07 — independent-slot unknown-time penalty

```math
\gamma_{M,\alpha}=\Phi^{-1}[(1-\alpha)^{1/M}].
```

**WARNING:** `M` is not digital sample count in a continuous scan.

### Step 08 — continuous full-template timing covariance

With noise-whitened template `K=GP/sqrt(S_n)` and normalized spectral weight `W`,

```math
r(\Delta)=\int W(f)e^{i2\pi f\Delta}df.
```

When the second spectral moment exists, local curvature and Rice upcrossing density follow from the SNR-weighted RMS frequency.

**REFINEMENT:** sample rate alone does not determine timing-search complexity. Identical complete `D*(f)` gives identical full-observation timing covariance for the same waveform.

### Step 09 — exact finite-deadline scan and conditional cross-detector reversal

The actual finite scan uses

```math
q_t=C_t^{-1}s_t
```

and its own timing covariance.

**REJECTED SHORTCUT:** finite-window `eta(t)` cannot be combined directly with full-template `f_rms` as one exact finite-deadline statistic.

A controlled equal-eventual-SNR family was introduced:

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
\qquad
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
```

Faster members accumulate more finite-time SNR at every finite duration but face a larger fixed-physical-`L` timing-search burden. Under standard convergence assumptions the cross-detector ranking can reverse.

### Step 10 — task-level detection-time surface

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t>0:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

This is task-level, not a detector-only replacement for `D*`.

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

**NEGATIVE RESULT:** this family has no finite interior `t_opt`; use all data allowed by the deadline.

### Step 12 — exact fast/slow task-regime boundary

For

```math
r=\tau_s/\tau_f>1,
\qquad
\ell=L/\tau_s,
```

the exact preference boundary is

```math
X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)=0.
```

**REJECTED SHORTCUT:** asymptotic-margin equality is not the minimum-decision-time boundary.

With `c=rho_0-Phi^{-1}(beta)` and full-template threshold `Gamma_infinity(ell,alpha)`, task space partitions into both-feasible, slow-only, and neither-feasible regions. Fast-only feasibility is impossible under equal eventual SNR. Physical timing-uncertainty feasibility obeys `L_crit=tau ell_crit`.

Under standard continuity/extreme-value growth, at least one finite fast-to-slow crossover exists; uniqueness remains open.

### Step 13 — direct correlated-scan numerics and continuum obstruction

A direct FFT moving-average Monte Carlo simulated the **correlated grid-sampled** finite-duration Gaussian timing scan; no effective independent-trial count was used.

Validation parameters were

```text
rho_0=5
r=1.2
alpha=0.01
beta=0.90
```

Broad Step-12 behavior appeared, but the apparent crossover moved materially under timing-grid refinement.

**FAILED NUMERICAL ESTIMATE:** diagnostic values around `ell~49` are not a valid continuous-time crossover and must not be reused.

The failure was explained exactly. For the finite hard-window template,

```math
\boxed{
a_x=-R_x'(0^+)=\frac{2x^2e^{-2x}}{\eta(x)}}
```

and

```math
R_x(y)=1-a_x|y|+O(y^2).
```

Thus

```math
E[(z(u+h)-z(u))^2]\sim2a_x|h|,
```

so the finite hard-window scan is locally Brownian-like / mean-square nondifferentiable in ideal white noise. Fixed timing grids therefore converge slowly to the continuous supremum. The full-template limit is smooth, so the finite-hard-window and full-template limits do not commute.

### Step 14 — true finite-bandwidth regularization

**REJECTED SHORTCUT:** a noiseless invertible common low-pass does not necessarily reduce optimal-detection information bandwidth because whitening cancels its magnitude wherever the transfer is nonzero:

```math
|FS|^2/(|F|^2S_n)=|S|^2/S_n.
```

A genuine regularizer must remove accessible high-frequency information or otherwise force the noise-weighted timing spectrum to have finite second moment.

For a true accessible angular-frequency band

```math
|\omega|\le\Omega_B,
```

the finite-duration scan covariance is

```math
r_{t,B}(\Delta)
=\frac{\int_{-\Omega_B}^{\Omega_B}|Q_{t,B}|^2S_{n,B}e^{i\omega\Delta}d\omega}
{\int_{-\Omega_B}^{\Omega_B}|Q_{t,B}|^2S_{n,B}d\omega}.
```

Therefore

```math
\boxed{
-r_{t,B}''(0)
=\int\omega^2W_{t,B}(\omega)d\omega
\le\Omega_B^2.
}
```

The Step-13 linear cusp is removed and the finite-duration scan is mean-square differentiable. Rice-type continuous-time crossing methods are mathematically admissible again.

For a similarity-preserving regularized version of the Step-09 family define

```math
\kappa=\Omega_B\tau
```

and hold `kappa` fixed as `tau` changes, while normalizing all members to the same **band-limited eventual SNR** `rho_0`.

Then

```math
\boxed{
\mathcal T_{D,\kappa}
=\tau X_{D,\kappa}(\rho_0,\alpha,\beta,L/\tau).
}
```

For two members with `r=tau_s/tau_f`, the regularized boundary remains

```math
\boxed{
X_{D,\kappa}(r\ell)-rX_{D,\kappa}(\ell)=0.
}
```

The full-template threshold remains nondecreasing with normalized search length, so the both-feasible / slow-only / neither-feasible structure and the exclusion of fast-only feasibility survive within the co-scaled finite-bandwidth family. Under the same continuity/mixing conditions, at least one fast-to-slow crossover survives.

**REFINEMENT:** the Step-13 roughness is a genuine feature of the infinite-white-bandwidth hard-window idealization, but it is not the source of the fast/slow regime reversal.

If the same **physical** bandwidth is imposed on both unequal-`tau` detectors, then `kappa_f != kappa_s`; that comparison is a separate open problem.

See `FINITE_BANDWIDTH_REGULARIZATION_STEP.md`.

---

## 3. Current frontier

The clean numerical target is now the smooth regularized scan

```math
\Gamma_\kappa(x,\ell,\alpha)
```

for finite `kappa`.

The next step is to simulate it with controlled grid convergence and cross-check the resulting thresholds against Rice/extreme-value predictions, then trace how the fast/slow crossover moves as `kappa` increases toward the rough white-noise limit.

---

## 4. Scope boundary

Do not claim:

- faster is universally better or worse;
- a universal speed-detectivity tradeoff or scalar replacement for `D*`;
- the rejected `ell~49` numerical estimate is real;
- an arbitrary invertible low-pass regularizes optimal information bandwidth;
- crossover uniqueness;
- fixed physical bandwidth has the same ordering as fixed dimensionless `kappa`;
- true-alignment crossing equals exact global rejection/localization;
- novelty.

Unknown amplitudes/phases, signal-dependent shot noise, sequential stopping, nonlinear response, saturation, dead time, nonstationarity, and globally optimal non-Gaussian decisions remain untouched.

---

## 5. Single next question — DO NOT ANSWER UNTIL PROMPTED

> For finite dimensionless bandwidth `kappa`, can the now-smooth Gaussian timing scan be simulated with controlled grid convergence and Rice/extreme-value cross-checks to obtain a trustworthy `Gamma_kappa(x,ell,alpha)` and fast/slow crossover, and how does that crossover move as `kappa` is increased toward the rough white-noise limit?
