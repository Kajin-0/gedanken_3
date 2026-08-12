# Progress Log — Experiment 01

**Consolidation note — 2026-08-12 19:31 EDT:** compact chronology preserving consequential results, corrections, invalidations, hard-stop decisions, and current frontier. Full derivations remain in dedicated step files.

---

## Steps 01–12 — detector/detection-theory core
Equal scalar reference `D*` does not determine arbitrary temporal-signal performance; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36` under the stated additive-noise construction. Full magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation stationary-Gaussian problem. Finite windows make phase/time placement operationally relevant even with identical magnitude response. Unknown arrival introduces global false-alarm search complexity; in the defined continuous scanning protocol, a controlled equal-eventual-SNR fast/slow family can reverse ranking because temporal compression changes both early evidence accumulation and timing-search complexity. This is a task/protocol result, not a universal detector theorem.

## Steps 13–23 — continuous search, rough-window obstruction, finite bandwidth
Hard-window timing scans are locally Brownian-like. **FAILED NUMERICAL ESTIMATE:** early rough-grid crossover `ell~49` invalid. Genuine finite information bandwidth removes the cusp; an invertible noiseless low-pass does not. With fixed physical signal/noise a shallow finite bandwidth optimum appears. Rice's upper switch near `kappa_f~130` is **INVALIDATED**; Palm preserves only the lower switch `~21.7 +/- .3`. Rough endpoint `Lambda_cross^infinity~.905 +/- .004` leaves original `Lambda=.895` numerically fast-preferred.

## Steps 24–30 — generalized Pickands / Brownian-parabola structure
Finite bandwidth yields `g_{chi,zeta}=t^2+sqrt(2)chi F_zeta` and generalized Pickands constant `H(chi,zeta)`. Brown-Resnick Slepian gives exact coordinatewise monotonicity but not physical-boundary monotonicity. **INVALIDATED INTERMEDIATE:** coupling coefficient `.8131`; corrected pointwise coefficient `.8906480701 sqrt(chi/zeta)`. Brownian-parabola scaling introduces `mu=sqrt(2)zeta chi^(1/3)`. **INVALIDATED NUMERICAL INTERPRETATION:** raw tiny-chi Step-27 data were grid biased.

## Steps 31–41 — finite-u high-band closure machinery
Step 31 empirical bridge is superseded for the original conclusion. Step 32 crossing moments separate through `kappa_f~170`, then fail from micro-upcrossing multiplicity. Step 33 replaces crossings with finite-amplitude clusters and exact occupation-Palm moment identities. Step 34 gives paired numerical high-band closure but originally used an empirical inter-node allowance. Step 35 proves `L2` regularity in `q`; generic anti-concentration is too coarse. Step 36 gives a rare-event-scaled cluster maximum strip measure. Steps 37–38 obtain high-threshold overshoot scale and exact cross-elasticity ordering. Step 39 finds `R=N_a/N_tan~1.56`, rejecting a small-amplitude finite-u remainder. Step 40 gives Cameron-Martin exact-event threshold translation. Step 41 replaces empirical q interpolation with analytic Gaussian-process control. **INVALIDATED NUMERICAL VALUE:** Step-35 tiny-q `0->.005` RMS `~5.4e-5` was cancellation damaged; corrected asymptotic value `~2.69e-5`.

## Step 42 — raw Palm concentration obstruction
Raw inverse-duration Palm weights are formally bounded but generic empirical Bernstein is useless because of enormous support. At 50k paths the 95% radius is `~.245 alpha`, dominated by the range term. Duration truncation at `L0=.02` yields exactly `P_FA<=E[C_long]+P(C_short>=1)` and reduces support 40x.

## Step 43 — short-cluster Gaussian envelope
A successful cluster shorter than `.02` must traverse amplitude `.15` near the `~5 sigma` level within `.02`. Fine-net Gaussian discordance plus conservative numerical covariance/metric envelopes gives `P(C_short>=1)<3.9e-11<3.9e-5 alpha`. **PARTIAL CERTIFICATE.**

## Step 44 — finite-grid statistical certificate
Four independent 50k truncated-Palm runs pooled to `n=200000`:

```text
mean/alpha          .992616066144
EB radius/alpha     .00730270506
short bound/alpha   .000039
finite-grid UCB     .999957771204 alpha
```

**RIGOROUS FINITE-GRID STATISTICAL CERTIFICATE:** pointwise 95% finite-sample upper bound below `alpha` on the implemented grid. Remaining margin only `.00004223 alpha`; continuum bias dominates.

## Step 45 — witness-time test
Common-random-number scan: `X=7.50` gains fast `~.001575 alpha` while slow lower remains `~1.089`; `X=7.70` gains `~.002006 alpha` but slow lower falls to `~1.013`. **NEGATIVE RESULT:** witness retuning alone trades one knife-edge for another.

## Step 46 — rough-grid mechanism
Nested common-path grids `.001,.0005,.00025`, pooled 24k paths:

```text
fine(.00025)-coarse(.001)  = +.00053010 alpha +/- .00025069
fine(.00025)-medium(.0005) = +.00015785 alpha +/- .00015069
```

Five missed fine-grid successful components contribute `.00052149 alpha`; duration-only interpolation contributes only `(8.61 +/-4.13)e-6 alpha`. The rough cusp gives Brownian `sqrt(dt)` continuity scale with `beta=-zeta(1/2)/sqrt(2pi)`. **WORDING CORRECTION:** because the coarse/fine estimate is driven by five events and has ~47% relative SE, it is only statistically consistent with the parameter-free theoretical sign/scale; it does not precisely verify the coefficient.

## Step 47 — exact canonical alpha=1 finite-grid correction
For pure rough tangent `W(s)=sqrt(2)B(s)-|s|`, physical `dt` maps to `delta=a_Xu^2dt`, and

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

**EXACT CANONICAL FINITE-GRID CORRECTION.** Do not identify this exact canonical identity with the actual finite-u physical ratio. Earlier phrase "essentially exact agreement" between the five-event Step-46 Monte Carlo and theory is withdrawn as an empirical claim.

## Step 48 — 19:31 EDT — hard-gated mixed-tangent transfer
The Step-47 external assessment imposed a hard stop: proceed only if the next step directly reduces the mixed-to-`alpha=1` finite-u transfer uncertainty.

At the rough endpoint the mixed tangent is

```math
W_chi(t)=sqrt(2)Zt-t^2+2^(3/4)sqrt(chi)B(t)-sqrt(2)chi|t|.
```

For `X=7.16`, `u=4.9589834838`, exact rough coefficients give

```text
a_X   = 6.1914157127e-5
b_X   = 1.0001238283
chi   = 3.0701227479e-4
Delta = 3.506747946e-3   (tangent grid for physical dt=.001)
delta = 1.5225630594e-6  (canonical alpha=1 grid)
```

Exact cellwise identity on every grid cell:

```math
W(t_k+theta Delta)
=(1-theta)W_k+theta W_{k+1}
+sqrt(2delta) B_bridge(theta)
+Delta^2 theta(1-theta).
```

The finite-u parabolic within-cell bulge is at most `Delta^2/4=3.07432e-6`.

**REJECTED SHORTCUT:** Slepian/variogram ordering separately orders continuous and discrete generalized Pickands constants but does not order their discretization ratio.

Paired generalized Dieker-Yakir calculation on three independent 3000-path seeds (`9000` paths total), comparing `Delta` to `Delta/128`:

```text
H_mix^Delta           .5677632065
H_mix^(Delta/128)     .5682959763
mixed relative loss   9.3748649e-4
paired SE(loss)       5.5146e-6
```

Exact pure-alpha=1 loss over the same two canonical resolutions:

```text
9.2635965e-4.
```

Transfer residual:

```text
mixed ratio - pure ratio = -1.11268e-5
paired SE                 =  5.5088e-6
approx normal 95% interval [-2.1924e-5, -3.30e-7].
```

A separate `Delta/32` run with 20k paired paths gives residual `-5.13e-6 +/-3.58e-6` (1 SE); `T=3,4,5` pilots overlap statistically.

**PAIRED FINITE-LEVEL TRANSFER INTERVAL / HARD-GATE PASSED:** the finite-u Brownian-parabola transfer is `O(1e-5)` at the working parameters, while the resolved mixed grid loss itself is `O(9e-4)`. The interval is a paired Monte Carlo diagnostic, not a distribution-free theorem. Since nested-grid generalized constants increase under refinement, the mixed-tangent continuum loss is at least the resolved coarse-to-`Delta/128` loss; within the mixed tangent, the Step-44 `.001` grid cannot plausibly retain its `4.22e-5 alpha` knife-edge margin.

Full derivation: `MIXED_TANGENT_GRID_TRANSFER_STEP.md`.  
Helper: `numerics/mixed_tangent_grid_transfer.py`.

---

## Current stopping point / hard gate
The next and only allowed closure task is the exact finite-window process remainder beyond the mixed tangent. A legitimate next step must either bracket that remainder, give a controlled numerical interval strong enough to settle the witness, or conclude that the remainder is not worth closing and stop the mathematical branch. No new witness scan, asymptotic constant, or side branch should be opened first.

### Single next question
> Can the exact finite-window covariance be bracketed around the mixed tangent on the `Delta/128` extremal neighborhood strongly enough to bound the remaining exact-process remainder, or does that final remainder fail the hard stopping test and force consolidation?
