# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 14:18 EDT  
**Status:** fifteen logical steps completed. Step 15 validates a smooth finite-information-band numerical model of the correlated timing scan: unlike the Step-13 rough hard-white-noise process, timing-grid refinement is stable within Monte Carlo uncertainty and agrees with Rice/Euler-characteristic continuous-time predictions at the validation points. A Rice-based trend study shows the fast/slow crossover moving to smaller normalized timing uncertainty as the accessible high-frequency scale increases. Those crossover values are approximate, not exact phase-boundary results. No universal replacement metric and no novelty claim.

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

Equal reference `D*` does not guarantee equal SNR for arbitrary temporal signals. The explicit 1 Hz first-order/additive-output-noise counterexample gave `SNR_A/SNR_B ~6.36`.

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

A stable causal all-pass phase factor preserves complete magnitude `D*(f)` and total infinite-time SNR while changing finite-window SNR after latency compensation.

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

### Step 09 — finite-deadline scan and conditional cross-detector reversal

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

### Step 11 — dimensionless collapse; no finite interior filter optimum

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

so the finite hard-window scan is locally Brownian-like / mean-square nondifferentiable in ideal white noise. Fixed timing grids therefore converge slowly to the continuous supremum.

### Step 14 — true finite-bandwidth regularization

**REJECTED SHORTCUT:** a noiseless invertible common low-pass does not necessarily reduce optimal-detection information bandwidth because whitening cancels its magnitude wherever the transfer is nonzero.

A genuine regularizer must remove accessible high-frequency information or otherwise force the noise-weighted timing spectrum to have finite second moment.

For a true accessible band `|omega|<=Omega_B`,

```math
\boxed{
-r_{t,B}''(0)
=\int\omega^2W_{t,B}(\omega)d\omega
\le\Omega_B^2.
}
```

The Step-13 cusp disappears and the finite scan is mean-square differentiable.

For a similarity-preserving regularized family define

```math
\kappa=\Omega_B\tau
```

and normalize all members to the same band-limited eventual SNR `rho_0`. Then

```math
\mathcal T_{D,\kappa}
=\tau X_{D,\kappa}(\rho_0,\alpha,\beta,L/\tau),
```

and the regularized fast/slow boundary retains the form

```math
X_{D,\kappa}(r\ell)-rX_{D,\kappa}(\ell)=0.
```

Thus the Step-12 task-regime mechanism survives finite-bandwidth regularization.

### Step 15 — smooth-band numerical validation

For the first controlled numerical regularization choose the explicit smooth information weighting

```math
\boxed{
J_{x,\kappa}(\nu)
=|H_x(\nu)|^2e^{-(\nu/\kappa)^2},
}
```

where

```math
H_x(\nu)
=\frac{1-e^{-(1+i\nu)x}[1+(1+i\nu)x]}{(1+i\nu)^2}.
```

This Gaussian factor is an explicit high-frequency information/processing penalty, **not** an invertible common low-pass. It is one controlled finite-second-moment surrogate within the Step-14 regularized class.

The corresponding scan is differentiable with finite

```math
\sigma_\nu^2
=\frac{\int\nu^2J_{x,\kappa}d\nu}{\int J_{x,\kappa}d\nu}.
```

A direct periodic FFT spectral-synthesis Monte Carlo was implemented in

```text
numerics/regularized_scan_mc.py
```

with no independent-trials approximation.

For the retained validation task

```text
rho_0=5
r=1.2
alpha=0.01
beta=0.90
kappa=8
```

the Rice-based provisional crossover is `ell_s ~=54.7489`, with test points

```text
slow: x ~=3.78390, ell ~=54.7489, Gamma_Rice ~=3.66373
fast: x ~=4.54068, ell ~=65.6986, Gamma_Rice ~=3.70181.
```

Direct 99th-percentile thresholds:

```text
slow, delta=0.05, 15000 paths:
    3.6401, bootstrap95 [3.5967,3.6821]
slow, delta=0.025, 12000 paths:
    3.6470, bootstrap95 [3.5924,3.7012]

fast, delta=0.05, 15000 paths:
    3.7041, bootstrap95 [3.6480,3.7530]
fast, delta=0.025, 12000 paths:
    3.6649, bootstrap95 [3.6325,3.7017]
```

The two grid resolutions overlap within Monte Carlo tail uncertainty and are compatible with the Rice/Euler-characteristic continuous predictions. Unlike Step 13, there is no systematic upward drift under refinement. Doubling the periodic synthesis domain changes the threshold by less than the present Monte Carlo uncertainty.

**NUMERICAL VALIDATION:** the dominant Step-13 grid-to-continuum pathology is absent in the smooth finite-`kappa` model.

Using Rice/Euler-characteristic theory only as a trend estimator, the approximate crossover moves as

```text
kappa      ell_cross^Rice
2             75.56
4             61.58
8             54.75
16            51.43
32            49.89
```

**CONDITIONAL TREND:** over this tested model/parameter range, restoring more high-frequency timing information moves the fast-to-slow switch to smaller `L/tau_s`.

These are not exact Monte Carlo phase-boundary values and must not be used to rehabilitate the rejected Step-13 `ell~49` result.

See `FINITE_BANDWIDTH_NUMERICAL_STEP.md` and `numerics/regularized_scan_mc.py`.

---

## 3. Current frontier

The smooth finite-bandwidth scan can now be simulated in a numerically controlled way at moderate false-alarm levels. The next unresolved numerical problem is **rare-event accuracy**:

```text
Gamma_kappa(x,ell,alpha)
for alpha << 10^-2, especially alpha ~ 10^-6.
```

Ordinary Monte Carlo becomes inefficient there. The next step is to build or adapt a rare-event/high-threshold method for the smooth correlated scan and compare it against Rice theory before attempting detector-relevant phase boundaries.

---

## 4. Scope boundary

Do not claim:

- faster is universally better or worse;
- a universal speed-detectivity tradeoff or scalar replacement for `D*`;
- the rejected Step-13 `ell~49` numerical estimate is real;
- an arbitrary invertible low-pass regularizes optimal information bandwidth;
- the Step-15 Gaussian information weighting is a unique physical readout model;
- the Rice crossover table is an exact phase boundary;
- crossover uniqueness;
- fixed physical bandwidth has the same ordering as fixed dimensionless bandwidth;
- true-alignment crossing equals exact global rejection/localization;
- novelty.

Unknown amplitudes/phases, signal-dependent shot noise, sequential stopping, nonlinear response, saturation, dead time, nonstationarity, and globally optimal non-Gaussian decisions remain untouched.

---

## 5. Single next question — DO NOT ANSWER YET

> Can a rare-event / high-threshold numerical method be built for the smooth regularized scan so that `Gamma_kappa(x,ell,alpha)` and the fast/slow crossover can be solved directly at detector-relevant false-alarm probabilities such as `alpha=10^-6`, and how different is that result from the Rice prediction?
