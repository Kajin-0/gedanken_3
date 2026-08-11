# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 15:00 EDT  
**Status:** seventeen logical steps completed. Step 17 derives an endpoint-retaining Palm/Rice crossover identity, proves that Rice accuracy is not uniform as finite-window timing bandwidth is taken to infinity, and obtains a simple extreme-speed-ratio law: on the tracked fast-to-slow branch, `r ell_cross -> ell_crit,kappa`, so the physical crossover tends to `L_cross -> tau_fast ell_crit,kappa`. No universal replacement metric and no novelty claim.

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
**NEGATIVE RESULT:** identical complete `D*(f)` gives identical stationary-Gaussian full-observation timing-search statistics. Finite truncation can break equivalence because magnitude `D*(f)` discards temporal phase/placement.

### Step 04 — pure-delay loophole removed
A stable causal all-pass phase factor preserves complete magnitude `D*(f)` and total infinite-time SNR while changing latency-compensated finite-window SNR.

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
The actual finite search must use `q_t=C_t^-1s_t` and its own covariance.

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

Task-level, not a detector-only replacement for `D*`.

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

Task space partitions into both-feasible, slow-only, and neither-feasible regions; fast-only feasibility is impossible under equal eventual SNR. At least one finite fast-to-slow crossover exists under standard continuity/extreme-value conditions; uniqueness remains open.

### Step 13 — direct correlated-scan numerics and continuum obstruction
A direct FFT moving-average Monte Carlo simulated the correlated grid-sampled finite-duration scan without independent-trials replacement.

**FAILED NUMERICAL ESTIMATE:** diagnostic crossover values near `ell~49` are not continuum-converged and must never be quoted.

The finite hard-window covariance has

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

A genuine finite information band makes the timing spectrum have finite second moment and removes the Step-13 cusp. For a similarity-preserving family with fixed dimensionless bandwidth `kappa=Omega_B tau`, the scaled task surface and fast/slow boundary survive.

### Step 15 — smooth-band numerical validation
Use the explicit Gaussian information weighting

```math
J_{x,\kappa}(\nu)=|H_x(\nu)|^2e^{-(\nu/\kappa)^2}.
```

Direct correlated FFT simulation is stable under practical timing-grid refinement and agrees with Rice/Euler-characteristic predictions at moderate false-alarm validation points.

For `rho_0=5`, `r=1.2`, `alpha=0.01`, `beta=0.90`, Rice gives the approximate trend

```text
kappa      ell_cross^Rice
2             75.56
4             61.58
8             54.75
16            51.43
32            49.89
```

These are trends, not exact phase boundaries.

### Step 16 — rare-event Palm/upcrossing method
For a differentiable stationary Gaussian timing scan,

```math
\lambda_u=E[N_u^+]
=L\frac{\sigma}{2\pi}e^{-u^2/2},
```

and under the upcrossing Palm law

```math
\boxed{
P_{FA}(u)
=Q(u)+\lambda_u
E_\uparrow\!\left[
\frac{1_{\{z(0)\le u\}}}{N_u^+}
\right].
}
```

Therefore

```math
\boxed{P_{FA}(u)\le Q(u)+\lambda_u.}
```

The first-order Rice/EC expression is an upper bound; its error is exactly due to endpoint/upcrossing overlap and multiple high excursions.

At an upcrossing,

```math
z'(T)\sim\mathrm{Rayleigh}(\sigma).
```

For the rare-event validation task

```text
rho_0=6.2
r=1.2
alpha=1e-6
beta=0.90
kappa=8,
```

Rice predicts `ell_cross ~=0.571441752`. A Palm rare-event solve gives

```math
\boxed{\ell_\times^{Palm}\approx0.5721}
```

with conservative numerical summary `0.5721 +/-0.001`, only about `0.12%` above Rice.

### Step 17 — high-threshold crossover law and large-`r` asymptote

At a crossover write

```math
x_s=x,
\qquad x_f=rx,
\qquad
\ell_s=\ell,
\qquad \ell_f=r\ell,
```

and

```math
u_s=\rho_0\mathcal R_\kappa(x)-\Phi^{-1}(\beta),
```

```math
u_f=\rho_0\mathcal R_\kappa(rx)-\Phi^{-1}(\beta).
```

Define the Palm correction factor

```math
C_\uparrow
=E_\uparrow\!\left[
1_{\{z(0)\le u\}}/N_u^+
\right].
```

The exact smooth-process crossover identity is

```math
\boxed{
\frac{[\alpha-Q(u_f)]e^{u_f^2/2}}
{\sigma_f C_f}
=
r\frac{[\alpha-Q(u_s)]e^{u_s^2/2}}
{\sigma_s C_s}.
}
```

In the isolated-excursion limit `C_s,C_f ->1`, this becomes the compact endpoint-retaining Rice law

```math
\boxed{
u_f^2-u_s^2
\approx
2\ln\!\left[
r\frac{\sigma_f}{\sigma_s}
\frac{\alpha-Q(u_s)}{\alpha-Q(u_f)}
\right].}
```

**REJECTED SHORTCUT:** `alpha <<1` does not imply `Q(u)<<alpha`. In the Step-16 task, `Q(u_s)/alpha ~=0.49` and `Q(u_f)/alpha ~=0.45`; dropping the endpoint term moves the predicted crossover from `~0.571` to about `1.0`.

#### Bandwidth nonuniformity
For finite hard-window duration `x`,

```math
H_x(\nu)\sim ixe^{-x}e^{-i\nu x}/\nu,
```

so under the Gaussian regularizer

```math
\boxed{
\sigma_\kappa^2(x)
\sim
\frac{a_x}{\sqrt\pi}\kappa
\qquad(\kappa\to\infty).
}
```

Thus the Rice expected upcrossing count grows as `sqrt(kappa)` at fixed `u,ell`, while the exact excursion probability remains bounded. Consequently the Palm factor must shrink at least as

```math
C_\uparrow=O(\kappa^{-1/2}).
```

**DERIVED:** the near-exact Step-16 Rice/Palm agreement cannot remain uniform all the way to the Step-13 rough limit.

A `3000`-path Palm sweep at `r=1.2`, `alpha=1e-6` shows this trend: corrections are below resolution at `kappa=2`, about `0.1%` at `kappa=8`, a few `0.1%` at `kappa=16`, and roughly `0.4–0.7%` at `kappa=32`, with multiple-upcrossing fractions rising toward the percent level.

#### Extreme speed-ratio law
Track the fast-to-slow crossover branch as

```math
r=\tau_s/\tau_f\to\infty.
```

The slow normalized search interval tends to zero, so the slow detector approaches its known-time decision duration. Then `x_f=rx_s -> infinity`, so the fast detector uses its full template.

Define

```math
u_\infty=\rho_0-\Phi^{-1}(\beta)
```

and the fast full-template feasibility edge

```math
\boxed{
\Gamma_{\infty,\kappa}(\ell_{crit,\kappa},\alpha)
=u_\infty.
}
```

Then, on the tracked branch and under the same continuity assumptions,

```math
\boxed{
r\ell_\times\to\ell_{crit,\kappa},}
```

```math
\boxed{
\ell_\times\sim\ell_{crit,\kappa}/r,}
```

and in physical time

```math
\boxed{
L_\times\to\tau_f\ell_{crit,\kappa}.}
```

The slow time constant drops out at leading order.

Rice gives

```math
\ell_{crit,\kappa}^{Rice}
=\frac{2\pi[\alpha-Q(u_\infty)]}{\sigma_{\infty,\kappa}}
e^{u_\infty^2/2}.
```

For the Step-16 rare-event task:

```text
kappa       ell_crit^Rice
2              0.988282
4              0.811380
8              0.723222
16             0.678958
32             0.656729
```

Finite-`r` Rice solutions converge extremely rapidly: at `r=2`, `r ell_cross` is within about `0.06–0.11%` of `ell_crit`; at `r=3`, within about `5e-4%` across representative `kappa=2,8,32`.

For the original `tau_f=1 ns`, `tau_s=1 s` ratio and **only** the Step-16 validation parameters with `kappa=8`, the large-`r` Rice law gives the illustrative crossover

```text
L_cross ~0.723 ns.
```

A full-template Palm spot check indicates only a sub-percent upward correction. This is structural, not a real-detector prediction.

#### Noncommuting limits
At fixed finite `r`, `kappa->infinity` recreates finite-window roughness and invalidates uniform Rice accuracy. If `r->infinity` is taken first, the fast crossover filter becomes the full template and remains smooth as bandwidth is removed; `sigma_infinity,kappa ->1`. Thus the extreme-speed-ratio limit is mathematically cleaner than the finite-`r` infinite-bandwidth route.

See `HIGH_THRESHOLD_CROSSOVER_ASYMPTOTICS_STEP.md` and `numerics/asymptotic_crossover.py`.

---

## 3. Current frontier

The co-scaled finite-bandwidth family now has:

```text
exact Palm rare-event identity
endpoint-retaining high-threshold crossover law
proof of nonuniform Rice accuracy as kappa -> infinity at finite x
simple large-r crossover law L_cross -> tau_fast ell_crit,kappa
```

The leading unresolved physical branch is the one deliberately postponed in Step 14: both detectors connected to the **same physical electronics bandwidth**, for which `kappa_f=Omega_B tau_f` and `kappa_s=Omega_B tau_s` are different.

---

## 4. What is established

- Equal scalar reference `D*` does not determine arbitrary temporal-signal SNR.
- Complete `D*(f)` is sufficient only for the restricted full-observation known-waveform problem.
- Finite observation can make phase/temporal placement operationally relevant.
- Exact finite-record SNR and finite-search covariance must come from the same finite measurement problem.
- The controlled equal-eventual-SNR family admits a conditional fast/slow ranking reversal and task-regime boundary.
- **NEGATIVE RESULT:** no finite interior filter optimum exists for the original scaled white-noise family.
- **FAILED NUMERICAL ESTIMATE:** the Step-13 rough-grid `ell~49` crossover is invalid.
- True finite information bandwidth removes the hard-window cusp without removing the task-regime mechanism.
- Smooth finite-`kappa` scans admit efficient Palm rare-event evaluation at `alpha=1e-6`.
- **DERIVED:** exact Palm-corrected crossover identity and compact endpoint-retaining Rice limit.
- **DERIVED:** Rice accuracy cannot remain uniform as finite-window `kappa->infinity` because `sigma_kappa^2 ~ a_x kappa/sqrt(pi)`.
- **DERIVED / CONDITIONAL:** `r ell_cross -> ell_crit,kappa` and `L_cross -> tau_fast ell_crit,kappa` as the speed ratio becomes extreme.

---

## 5. What is not established

- No universal statement that faster detectors are better or worse.
- No universal speed-detectivity tradeoff or scalar replacement for `D*`.
- No proof of crossover uniqueness for all parameters.
- No exact rough finite-`r`, infinite-bandwidth crossover.
- No universal Palm correction law across all `kappa,r,rho_0,beta`.
- No claim that the illustrative `0.723 ns` applies to real detectors.
- No same-fixed-physical-bandwidth result yet.
- No exact global-rejection/localization surface, Bayes-optimal unknown-time detector, sequential stopping, unknown amplitude/phase, signal-dependent noise, nonlinear response, saturation, dead time, or nonstationarity.
- No novelty claim.

---

## 6. Single natural next question — DO NOT ANSWER YET

> If both detectors are connected to the **same physical readout bandwidth** rather than the same dimensionless `kappa`, does the large-`r` crossover law survive, and can the electronics bandwidth itself change or optimize which detector wins?
