# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 14:33 EDT  
**Status:** sixteen logical steps completed. Step 16 develops an exact Palm/upcrossing rare-event estimator for the smooth finite-`kappa` timing scan and validates the `alpha=10^-6` false-alarm threshold without brute-force Monte Carlo. For the tested `kappa=8`, `r=1.2`, `rho_0=6.2`, `beta=0.90` task, the rare-event-corrected fast/slow crossover is `ell_s ~=0.5721 +/-0.001`, only about `0.12%` above the Rice prediction `0.57144`. No universal replacement metric and no novelty claim.

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

## 2. Surviving logical path

### Step 01 — scalar reference `D*` insufficiency
A physically allowed first-order + additive-output-noise example gives unequal temporal-signal SNR despite equal reference `D*`; the explicit 1 Hz example gives `SNR_A/SNR_B ~6.36`.

**QUALIFICATION:** signal/noise filtering can cancel. Do not infer `fast is always better`.

### Step 02 — full-observation known-waveform SNR

```math
\rho_\infty^2
=\int |P(f)|^2\frac{|G(f)|^2}{S_n(f)}df
=\frac1A\int |P(f)|^2D^{*2}(f)df.
```

Complete magnitude `D*(f)` is sufficient for this restricted full-observation problem.

### Step 03 — unknown timing negative result; finite truncation failure
**NEGATIVE RESULT:** identical complete `D*(f)` gives identical stationary-Gaussian full-observation timing-search statistics. Finite truncation can break equivalence because magnitude `D*(f)` discards phase/placement.

### Step 04 — pure-delay loophole removed
A stable causal all-pass phase factor preserves complete magnitude `D*(f)` and total infinite-time SNR while changing finite-window SNR after latency compensation.

### Step 05 — exact finite-time SNR

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
\qquad
\eta(t)=\rho_t^2/\rho_\infty^2.
```

### Step 06 — known-time Gaussian decision

```math
P_D(t;\alpha)=\Phi[\rho_t-\Phi^{-1}(1-\alpha)].
```

### Step 07 — independent-slot unknown-time penalty

```math
\gamma_{M,\alpha}=\Phi^{-1}[(1-\alpha)^{1/M}].
```

`M` is not digital sample count in a continuous timing scan.

### Step 08 — continuous full-template timing covariance
Timing-search covariance is the autocorrelation of the noise-whitened template. When the second spectral moment exists, `f_rms` controls local covariance curvature and Rice upcrossing density. Sample rate alone does not determine timing trials.

### Step 09 — exact finite-deadline scan and conditional cross-detector reversal
The actual finite search must use

```math
q_t=C_t^{-1}s_t
```

and its own scan covariance.

**REJECTED SHORTCUT:** do not combine finite-window `eta(t)` directly with full-template `f_rms` as one exact finite-deadline statistic.

A controlled equal-eventual-SNR family was introduced:

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
\qquad
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
```

Faster members accumulate more finite-time SNR but can face a larger fixed-physical-`L` unknown-time search burden. Under standard convergence assumptions the cross-detector ranking can reverse.

### Step 10 — task-level detection-time surface

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t>0:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

This is task-level, not a detector-only replacement for `D*`.

### Step 11 — dimensionless collapse; no finite interior filter optimum
For the controlled scaled family,

```math
x=t/\tau,
\qquad
\ell=L/\tau,
```

```math
\mathcal T_D
=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

Pointwise covariance ordering plus Slepian comparison makes the global search threshold nonincreasing with filter duration while SNR rises strictly.

**NEGATIVE RESULT:** no finite interior `t_opt`; use all data allowed by the deadline.

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

Task space partitions into both-feasible, slow-only, and neither-feasible regions; fast-only feasibility is impossible under equal eventual SNR. Physical timing-uncertainty feasibility scales as `L_crit=tau ell_crit`. At least one finite fast-to-slow crossover exists under standard continuity/extreme-value conditions; uniqueness remains open.

### Step 13 — direct correlated-scan numerics and continuum obstruction
A direct FFT moving-average Monte Carlo simulated the correlated **grid-sampled** finite-duration scan without independent-trials replacement.

**FAILED NUMERICAL ESTIMATE:** diagnostic crossover values around `ell~49` are not continuum-converged and must never be quoted as results.

The exact reason is the finite-hard-window covariance cusp:

```math
\boxed{
a_x=-R_x'(0^+)=\frac{2x^2e^{-2x}}{\eta(x)}}
```

and

```math
R_x(y)=1-a_x|y|+O(y^2),
```

so the ideal-white-noise finite scan is locally Brownian-like / mean-square nondifferentiable.

### Step 14 — true finite-information-band regularization
**REJECTED SHORTCUT:** an invertible noiseless common low-pass does not necessarily reduce optimal-detection information bandwidth because whitening cancels it.

A genuine finite accessible information band makes the timing spectrum have finite second moment:

```math
-r_{t,B}''(0)=\int\omega^2W_{t,B}(\omega)d\omega.
```

The cusp disappears and the scan becomes differentiable.

For a similarity-preserving family with fixed dimensionless bandwidth

```math
\kappa=\Omega_B\tau,
```

the task surface and fast/slow boundary retain their scaled forms. Thus the Step-13 cusp is not the source of the regime reversal.

### Step 15 — smooth-band numerical validation
Choose

```math
J_{x,\kappa}(\nu)=|H_x(\nu)|^2e^{-(\nu/\kappa)^2},
```

with

```math
H_x(\nu)=\frac{1-e^{-(1+i\nu)x}[1+(1+i\nu)x]}{(1+i\nu)^2}.
```

A direct periodic FFT simulation of the correlated smooth scan is implemented in

```text
numerics/regularized_scan_mc.py
```

and is stable under practical timing-grid refinement at the validation points. Rice/Euler-characteristic thresholds agree within Monte Carlo uncertainty.

For the moderate `rho_0=5`, `r=1.2`, `alpha=0.01`, `beta=0.90` trend study:

```text
kappa      ell_cross^Rice
2             75.56
4             61.58
8             54.75
16            51.43
32            49.89
```

**CONDITIONAL TREND:** restoring more high-frequency timing information moves the fast-to-slow switch to smaller `L/tau_s` in this tested regularization.

These are approximate Rice trends, not exact phase boundaries.

### Step 16 — rare-event Palm/upcrossing calculation at `alpha=10^-6`

#### Initial grid-event importance sampler
For an `n`-point correlated Gaussian timing grid, choose one index uniformly and condition it above `u`. If `K_u` grid samples exceed the threshold, the exact importance weight is

```math
\boxed{w=nQ(u)/K_u.}
```

This efficiently estimates the **grid maximum** but retains finite-grid continuum bias.

#### Exact continuous Palm identity
For a differentiable stationary unit-variance Gaussian scan, let `N_u^+` be the number of upcrossings and

```math
\lambda_u
=E[N_u^+]
=L\frac{\sigma}{2\pi}e^{-u^2/2}.
```

Under the upcrossing Palm law,

```math
\boxed{
P_{FA}(u)
=Q(u)
+\lambda_u
E_\uparrow\!\left[
\frac{1_{\{z(0)\le u\}}}{N_u^+}
\right].
}
```

Thus

```math
\boxed{P_{FA}(u)\le Q(u)+\lambda_u.}
```

The first-order Rice/EC expression is an upper bound; its error comes exactly from endpoint/upcrossing overlap and multiple high excursions.

At an upcrossing the Palm slope has

```math
\boxed{z'(T)\sim\mathrm{Rayleigh}(\sigma).}
```

The low-variance implementation is in

```text
numerics/upcrossing_importance_sampling.py
```

#### `alpha=10^-6` validation task
`rho_0=5` is infeasible even at known time because the required margin is about `6.035`. Therefore use

```text
rho_0=6.2
r=1.2
alpha=1e-6
beta=0.90
kappa=8.
```

Rice predicts

```text
ell_s^Rice ~=0.571441752
x_s ~=4.473364397
x_f ~=5.368037276
u_s ~=4.895464822
u_f ~=4.913100340.
```

At those Rice thresholds, `5000` Palm paths give

```text
slow P_FA ~=9.9949037e-7, SE ~=2.04e-10
fast P_FA ~=9.9922753e-7, SE ~=2.70e-10.
```

Multiple-upcrossing and endpoint-overlap fractions are each only about `10^-3` in the Palm ensemble. Rice therefore overestimates the exact false-alarm probability by less than `0.1%` in this test, with threshold corrections only of order `10^-4`.

Propagating the Palm correction through the decision-time equations gives

```math
\boxed{\ell_\times^{Palm}\approx0.5721}
```

with a conservative numerical summary

```text
ell_cross^Palm ~=0.5721 +/-0.001.
```

Rice gives `0.57144`, a difference of only about `0.12%` in normalized timing uncertainty.

A direct re-evaluation near `ell_s~=0.57210` leaves the corrected crossover residual statistically consistent with zero.

**NUMERICAL VALIDATION / CONDITIONAL:** for this smooth `kappa=8`, `alpha=10^-6` validation task, Rice theory is quantitatively extremely accurate and the rare-event geometry is dominated by isolated single excursions.

See `RARE_EVENT_UPCROSSING_STEP.md` and `numerics/upcrossing_importance_sampling.py`.

---

## 3. Current frontier

The project now has a controlled rare-event route for smooth finite-bandwidth scans. At high threshold, the exact Palm identity explains why Rice becomes especially effective: the correction is governed only by multiple excursions and endpoint overlap.

The next scientific question is no longer whether `alpha=10^-6` is numerically accessible. It is:

```text
how the Palm/Rice correction and fast/slow crossover scale with
kappa, r, rho_0, and beta,
and whether a simple high-threshold asymptotic crossover law emerges.
```

---

## 4. What is established

- Equal scalar reference `D*` does not determine arbitrary temporal-signal SNR.
- Complete `D*(f)` is sufficient only for the restricted full-observation known-waveform problem.
- Finite observation can make magnitude `D*(f)` insufficient because temporal phase/placement controls SNR accumulation.
- Exact finite-record SNR is `rho_t^2=<s_t,C_t^-1s_t>`.
- Unknown timing raises a global threshold governed by scan covariance, not digital sample count.
- Finite SNR and timing search must be derived from the same finite filter.
- The controlled equal-eventual-SNR family admits a conditional cross-detector ranking reversal and an exact task-regime boundary.
- **NEGATIVE RESULT:** no finite interior filter optimum exists for this family.
- Slow-only feasibility can occur; fast-only feasibility cannot under the equal-eventual-SNR scaled assumptions.
- **FAILED NUMERICAL ESTIMATE:** the Step-13 rough-grid `ell~49` crossover is invalid.
- True finite information bandwidth removes the hard-window covariance cusp without removing the task-regime mechanism.
- Smooth finite-`kappa` correlated scans can be simulated with controlled grid behavior.
- **DERIVED:** exact Palm rare-event identity and Rice upper bound for the differentiable one-dimensional scan.
- **NUMERICAL VALIDATION:** `alpha=10^-6` is tractable with thousands of Palm paths; Rice is accurate to about `0.1%` in the tested task.

---

## 5. What is not established

- No universal statement that faster detectors are better or worse.
- No universal speed-detectivity tradeoff or scalar replacement for `D*`.
- No proof of crossover uniqueness.
- No broad rare-event phase diagram across `kappa`, `r`, `rho_0`, and `beta`.
- No original extreme `r=10^9` rare-event crossover yet.
- No same-fixed-physical-bandwidth comparison across unequal `tau` detectors.
- The Palm implementation still uses a fine grid for rare secondary-crossing and endpoint-overlap corrections; no analytic discretization-error bound yet.
- No exact global-rejection/localization surface, Bayes-optimal unknown-time detector, sequential stopping, unknown amplitude/phase, signal-dependent noise, nonlinear response, saturation, dead time, or nonstationarity.
- No novelty claim.

---

## 6. Single natural next question — DO NOT ANSWER YET

> Does the near-exact Rice/Palm behavior persist as the dimensionless timing bandwidth `kappa` and speed ratio `r` are varied, and can the high-threshold limit yield a simple asymptotic law for the fast/slow crossover?