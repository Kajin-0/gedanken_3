# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-12 19:53 EDT  
**Status:** forty-nine logical steps completed. **HARD-STOP TRIGGERED.** Step 49 executes the only mathematical target permitted after Step 48: the higher-order exact finite-window covariance remainder beyond the mixed Brownian-parabola tangent. The exact covariance is simulated through an exact two-state linear-filter representation with delayed subtraction, so no cusp/quadratic approximation is used in this final transfer test. Two independent `3000`-path runs (`6000` paired paths) comparing the physical `dt=.001` grid with a `32x` refinement give exact-covariance relative grid loss `8.3682629e-4`, paired SE `6.8953e-6`, approximate normal 95% interval `[8.2331e-4,8.5034e-4]`. The exact pure-`alpha=1` benchmark for the same refinement is `8.3657896e-4`, so the higher-order exact-covariance transfer residual is only `+2.47e-7 +/- 6.90e-6` (1 SE). Thus the exact covariance does not provide an order-`1e-4` cancellation of the rough-grid effect. The remaining layer would be a publication-grade theorem translating this exact-covariance spectral-intensity ratio to the exact finite-search false-alarm event at `u~4.96`; under the imposed stopping rule this is no longer proportionate to the detector question. The mathematical closure branch stops here. Next research action: consolidate the detector/detection-theory core, separate the mathematical companion material, and perform a serious prior-art/novelty audit. No novelty claim.

---

## Detector/detection-theory core — Steps 01–12
- Equal scalar reference `D*` does not determine arbitrary temporal-signal performance; an explicit 1 Hz construction gives `SNR_A/SNR_B~6.36` under additive post-pole noise.
- Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation stationary-Gaussian maximum-SNR problem.
- Finite observation windows make phase/time placement operationally relevant even when `|D*(f)|` is identical; an all-pass construction removes the trivial pure-delay objection.
- Finite-time optimal SNR is `rho_T^2=<s_T,C_T^-1 s_T>`.
- Unknown arrival introduces a global-false-alarm timing-search penalty governed by the continuous scan covariance, not ADC sample count.
- In the controlled equal-eventual-SNR family, faster response accumulates evidence sooner but also shortens timing correlation length. Under the defined scanning protocol those effects can reverse the fast/slow ranking.
- Task-level detection time obeys `T_D=tau X_D(rho0,alpha,beta,L/tau)` for the constructed family.
- **Scope:** protocol/task theorem only; no universal detector ordering and no claim that faster detectors are generally worse.

## Steps 13–23 — rough-window obstruction and finite information bandwidth
- **FAILED NUMERICAL ESTIMATE:** early rough-grid crossover `ell~49` invalid; hard-window scan is locally Brownian-like.
- Genuine finite information bandwidth removes the cusp; an invertible noiseless low-pass does not because optimal whitening cancels it.
- Fixed physical signal/noise yields a shallow finite bandwidth optimum.
- Rice's apparent upper switch near `kappa_f~130` is **INVALIDATED**; Palm preserves only the lower switch `~21.7 +/- .3`.
- Rough endpoint `Lambda_cross^infinity~.905 +/- .004`; original `Lambda=.895` remains numerically fast-preferred.

## Steps 24–30 — mixed smooth/rough generalized Pickands structure
- Finite bandwidth yields `g_{chi,zeta}=t^2+sqrt(2)chi F_zeta` and generalized Pickands constant `H(chi,zeta)`.
- Brown-Resnick Slepian gives exact coordinatewise monotonicity in `chi,zeta`, but not physical-boundary monotonicity.
- **INVALIDATED INTERMEDIATE:** coupling coefficient `.8131`; corrected pointwise coefficient `.8906480701 sqrt(chi/zeta)`.
- Brownian-parabola double scaling uses `mu=sqrt(2)zeta chi^(1/3)`.
- **INVALIDATED NUMERICAL INTERPRETATION:** raw tiny-chi Step-27 data were grid biased; continuum-extrapolated/canonical calculations correct them.

## Steps 31–41 — finite-u high-band closure machinery
- Crossing moments separate through `kappa_f~170`, then fail from micro-upcrossing multiplicity.
- Finite-amplitude excursion clusters replace crossings; exact occupation-Palm moment identities are derived.
- Step 34 gives a paired numerical high-band closure; its original q-interpolation allowance was empirical.
- Step 35 proves `L2` regularity in `q=kappa^-1/2`; generic Gaussian anti-concentration is too coarse at `alpha=1e-6`.
- Step 36 gives a rare-event-scaled fixed-cluster maximum strip measure.
- Steps 37–38 derive high-threshold overshoot scale and exact generalized-Pickands cross-elasticity ordering.
- Step 39 finds `R=N_a/N_tan~1.56`; **REJECTED SHORTCUT:** finite-u correction is not a small-amplitude remainder.
- Step 40 gives Cameron-Martin exact-event threshold translation.
- Step 41 analytically controls interpolation between sampled q nodes.
- **INVALIDATED NUMERICAL VALUE:** Step-35 tiny-q pair RMS `~5.4e-5`; corrected asymptotic value `~2.69e-5`.

## Steps 42–44 — finite-sample endpoint statistics
- Raw inverse-duration Palm weights are formally bounded but generic empirical Bernstein is useless because the range is enormous.
- Duration truncation at `L0=.02` gives exactly `P_FA<=E[C_long]+P(C_short>=1)` and reduces long-weight support by 40x.
- Step 43 gives `P(C_short>=1)<3.9e-11<3.9e-5 alpha`, conditional on conservative numerical covariance/metric constants.
- Step 44 pools four independent 50k long-cluster runs (`n=200000`) and obtains a true pointwise finite-grid empirical-Bernstein certificate:

```text
mean/alpha          .992616066144
EB radius/alpha     .00730270506
short bound/alpha   .000039
finite-grid UCB     .999957771204 alpha
```

The finite-grid margin is only `.00004223 alpha`; continuum timing-grid bias dominates.

## Step 45 — witness-time test
- `X=7.50` gains fast `~.001575 alpha` while slow lower remains `~1.089`.
- `X=7.70` gains `~.002006 alpha` but slow lower falls to `~1.013`.
- **NEGATIVE RESULT:** witness shifting alone trades one knife-edge for another.

## Step 46 — rough-grid mechanism
Nested common-path grids `.001,.0005,.00025`, pooled 24k paths:

```text
fine(.00025)-coarse(.001)  = +.00053010 alpha +/- .00025069
fine(.00025)-medium(.0005) = +.00015785 alpha +/- .00015069
```

Five missed fine-grid successes contribute `.00052149 alpha`; duration-only interpolation contributes `(8.61 +/-4.13)e-6 alpha`.

**WORDING CORRECTION:** because this estimate is driven by five events with ~47% relative SE, it is only statistically consistent with the parameter-free Brownian prediction in sign and scale; it does not precisely verify the coefficient.

## Step 47 — exact canonical alpha=1 finite-grid correction
For pure rough tangent `W(s)=sqrt(2)B(s)-|s|`, physical `dt` maps to `delta=a_Xu^2dt` and

```math
H_1^delta
=delta^-1 exp[-2 sum_{n>=1} n^-1 Phi(-sqrt(n delta/2))]
=nu(sqrt(2delta)).
```

At `X=7.16`:

```text
dt=.00100   H=.998983867710   loss=1.016132290e-3
dt=.00050   H=.999281378993   loss=7.186210075e-4
dt=.00025   H=.999491804717   loss=5.081952830e-4
```

**EXACT CANONICAL FINITE-GRID CORRECTION.** Do not identify this with the actual finite-u physical false-alarm ratio.

## Step 48 — hard-gated mixed-tangent transfer
At `X=7.16`:

```text
a_X   = 6.1914157127e-5
b_X   = 1.0001238283
u     = 4.9589834838
chi   = 3.0701227479e-4
Delta = 3.506747946e-3
delta = 1.5225630594e-6
```

Exact cellwise identity:

```math
W(t_k+theta Delta)
=(1-theta)W_k+theta W_{k+1]
+sqrt(2delta)B_bridge(theta)
+Delta^2 theta(1-theta).
```

Paired generalized Dieker-Yakir calculation (`9000` paths, `Delta` vs `Delta/128`) gives mixed relative loss `9.3748649e-4`, paired SE `5.5146e-6`; exact pure-alpha1 loss is `9.2635965e-4`. Transfer residual `-1.11268e-5 +/-5.5088e-6` (1 SE). **HARD-GATE PASSED:** mixed finite-u transfer is `O(1e-5)`, much smaller than the `O(9e-4)` grid effect.

## Step 49 — exact finite-window covariance transfer / HARD STOP
Exact covariance:

```math
R_x(y)=e^{-y}[I_2(x-y)+yI_1(x-y)]/D_x,
```

with `I_1(A)=[1-(1+2A)e^-2A]/4`, `I_2(A)=[1-(1+2A+2A^2)e^-2A]/4`, `D_x=I_2(x)`.

Exact two-state representation:

```math
dU=-Udt+dW,
\qquad dV=(U-V)dt,
```

```math
Z_raw(t)=V(t)-e^{-x}[V(t-x)+xU(t-x)].
```

This reproduces `R_x` exactly after normalization. The exact finite-u spectral variogram is

```math
g_u^{exact}(t)=u^2[1-R_x(sqrt(2)|t|/(u sqrt(b_X)))].
```

Two independent `3000`-path exact-covariance runs, physical `dt=.001` versus `dt/32`, pooled `6000` paired paths:

```text
H_exact^Delta          .5528146649
H_exact^(Delta/32)     .5532776622
relative loss          8.3682629e-4
paired SE              6.8953e-6
approx 95% interval    [8.2331e-4, 8.5034e-4]
```

Exact pure-alpha1 loss over the same refinement:

```text
8.3657896e-4.
```

Exact-covariance minus pure loss residual:

```text
+2.47e-7 +/- 6.90e-6 (1 SE)
approx 95% residual interval ~[-1.33e-5,+1.38e-5].
```

**PAIRED EXACT-COVARIANCE TRANSFER INTERVAL:** higher-order finite-window covariance terms do not generate an order-`1e-4` cancellation of the grid loss. `T=3` and `T=5` sensitivity pilots overlap the `T=4` result.

**HARD-STOP TRIGGERED:** the remaining publication-grade finite-u mapping from exact-covariance spectral intensity to the exact finite-search false-alarm event is no longer proportionate to the detector question. Stop this mathematical closure chain.

See `EXACT_COVARIANCE_GRID_TRANSFER_STOP_STEP.md` and `numerics/exact_covariance_grid_transfer.py`.

---

## Active next phase
Do **not** continue to Step 50 of the same proof chain by default.

Next work should be:
1. consolidate the detector/detection-theory core into a clean theorem/task statement;
2. separate Steps 13–49 into a technical mathematical companion/appendix track;
3. perform a serious prior-art/novelty audit before any novelty language;
4. only reopen the mathematical closure branch if external review identifies a decision-relevant gap.

## Scope boundary
Do not claim: faster universally better/worse; a universal scalar replacement for `D*`; the scanning protocol universally optimal; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 values as continuum truth; Step-31 empirical fit exact/required; Step-34 fully formal theorem; Step-36 uniform hazard theorem; `R~1`; numerical covariance constants interval-certified; `L0=.02` optimal; Step-44 as a continuum certificate; Step-46 coefficient precisely verified; Step-47 canonical ratio as the exact finite-u false-alarm ratio; Step-48/49 Monte Carlo intervals as distribution-free theorem-level results; `X=7.16` mathematically optimal; no re-entrant pocket for all task parameters; novelty.
