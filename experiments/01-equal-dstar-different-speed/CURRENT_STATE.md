# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-12 19:31 EDT  
**Status:** forty-eight logical steps completed. Step 48 obeys the hard stopping rule imposed after the Step-47 external assessment: it attacks only the finite-`u` mixed-to-`alpha=1` discretization transfer. The mixed Brownian-parabola tangent has an exact cellwise Brownian-bridge decomposition. At `X=7.16`, physical `dt=.001` maps to tangent `Delta=.003506747946` and canonical `delta=a_Xu^2dt=1.5225630594e-6`; the only curved within-cell smooth term is `Delta^2 theta(1-theta)<=3.07432e-6`. A paired generalized Dieker-Yakir calculation on `9000` paths comparing `Delta` with `Delta/128` gives mixed relative grid loss `9.3748649e-4` with paired SE `5.5146e-6`. The exact pure-`alpha=1` loss over the same two finite resolutions is `9.2635965e-4`; the mixed-to-pure transfer residual is `-1.11268e-5` with paired SE `5.5088e-6`. Thus the finite-u Brownian-parabola transfer is `O(1e-5)` at the working parameters, while the resolved mixed grid loss itself is `O(9e-4)`. This is a controlled paired Monte Carlo diagnostic, not a theorem-level ratio bound. The next allowed target is the higher-order exact-process remainder beyond the mixed tangent; any unrelated asymptotic or witness branch should stop the closure program. No novelty claim.

---

## Original question
Two hypothetical detectors satisfy `D_A^*=D_B^*` but have radically different temporal response times. Does equal conventional specific detectivity imply equal ability to detect arbitrary optical signals?

## Surviving logical chain

### Steps 01–12 — detector/detection-theory core
- Equal scalar reference `D*` does not determine arbitrary temporal-signal performance; an explicit 1 Hz construction gave `SNR_A/SNR_B~6.36` under additive post-pole noise.
- Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation stationary-Gaussian maximum-SNR problem.
- Finite records make phase/time placement operationally relevant even when `|D*(f)|` is identical; an all-pass construction removes the trivial pure-delay objection.
- Finite-time matched-filter SNR is `rho_T^2=<s_T,C_T^-1 s_T>`; for an exponential response `eta(T)=1-exp(-2T/tau)`.
- Unknown arrival introduces a global-false-alarm search penalty. Continuous timing search is governed by the normalized template covariance, not ADC sample count.
- A controlled equal-eventual-SNR family shows competing effects: faster response accumulates evidence sooner but shortens timing correlation length and can increase search complexity.
- Task-level detection time is `T_D=tau X_D(rho0,alpha,beta,L/tau)`. In the defined scanning protocol a fast/slow ranking reversal can occur; this is a protocol-specific task theorem, not a universal detector ordering.

### Steps 13–23 — rough-window obstruction and finite bandwidth
- **FAILED NUMERICAL ESTIMATE:** early rough-grid crossover `ell~49` invalid; hard-window scan is locally Brownian-like.
- Genuine finite information bandwidth removes the cusp; an invertible noiseless low-pass is not sufficient because optimal whitening cancels it.
- With fixed physical signal/noise a shallow finite bandwidth optimum appears.
- Rice's apparent upper switch near `kappa_f~130` is **INVALIDATED**; Palm analysis preserves only the lower switch near `21.7 +/- .3`.
- Rough endpoint `Lambda_cross^infinity~.905 +/- .004`; original `Lambda=.895` remains numerically fast-preferred.

### Steps 24–30 — mixed smooth/rough generalized Pickands structure
- Finite bandwidth yields `g_{chi,zeta}(t)=t^2+sqrt(2)chi F_zeta(t)` and generalized Pickands constant `H(chi,zeta)`.
- Exact Brown-Resnick Slepian comparison gives coordinatewise monotonicity in `chi,zeta` but does not order the full detector boundary.
- **INVALIDATED INTERMEDIATE:** rough/smoothed coupling coefficient `.8131`; corrected pointwise coefficient `.8906480701 sqrt(chi/zeta)`.
- Brownian-parabola double scaling uses `mu=sqrt(2)zeta chi^(1/3)`; raw tiny-`chi` Step-27 data were grid biased and **INVALIDATED AS CONTINUUM VALUES**.
- Model-reduced canonical crossover numerics recover the corrected tiny-`chi` behavior.

### Steps 31–41 — finite-u high-band closure machinery
- Step 31 empirical high-band bridge is superseded for the original conclusion.
- Step 32 gives direct finite-u crossing-moment separation through `kappa_f~170`, then raw crossing moments fail because one physical excursion contains many micro-upcrossings.
- Step 33 replaces crossings with finite-amplitude excursion clusters and exact occupation-Palm moment identities.
- Step 34 gives paired numerical high-band closure; its original inter-node allowance was empirical.
- Step 35 proves `L2` regularity in `q=kappa^-1/2`; generic Gaussian anti-concentration is far too coarse at `alpha=1e-6`.
- Step 36 defines a rare-event-scaled fixed-cluster maximum strip measure; local strip intensity is numerically `~5 alpha` per threshold unit.
- Steps 37–38 derive high-threshold overshoot scale and exact generalized-Pickands cross-elasticity ordering; tangent hazard obeys `h_tan/N_tan<=phi/Q-1/u`.
- Step 39 finds `R=N_a/N_tan~1.56`; **REJECTED SHORTCUT:** the finite-u correction is not a small-amplitude remainder.
- Step 40 uses a Cameron-Martin covariance-kernel barrier for direct rare-event threshold translation.
- Step 41 analytically controls interpolation between sampled `q` nodes; **INVALIDATED NUMERICAL VALUE:** Step-35 tiny-q `0->.005` RMS `~5.4e-5` was cancellation damaged; corrected asymptotic value is `~2.69e-5`.

### Steps 42–44 — finite-sample endpoint statistics
- Raw inverse-duration Palm weights are formally bounded but generic empirical Bernstein is useless: at 50k paths the 95% radius is `~.245 alpha`, dominated by the support term.
- Duration truncation at `L0=.02` gives exactly `P_FA<=E[C_long]+P(C_short>=1)` and cuts the long-weight support by 40x.
- Step 43 analytically bounds short successful clusters: `P(C_short>=1)<3.9e-11<3.9e-5 alpha`, conditional on conservative numerical covariance/metric constants.
- Step 44 pools four independent 50k long-cluster runs (`n=200000`) and obtains a genuine pointwise finite-grid empirical-Bernstein certificate:

```text
mean/alpha          .992616066144
EB radius/alpha     .00730270506
short bound/alpha   .000039
finite-grid UCB     .999957771204 alpha
```

The finite-grid margin is only `.00004223 alpha`, so continuum timing-grid bias dominates.

### Step 45 — witness-time test
- Common-random-number scan: `X=7.50` gains fast `~.001575 alpha` while slow lower remains `~1.089`; `X=7.70` gains `~.002006 alpha` but slow lower falls to `~1.013`.
- **NEGATIVE RESULT:** witness shifting alone trades one near-boundary problem for another.

### Step 46 — grid-bias mechanism
- Nested common-path grids `.001,.0005,.00025`, pooled 24k paths:

```text
fine(.00025)-coarse(.001)  = +.00053010 alpha +/- .00025069
fine(.00025)-medium(.0005) = +.00015785 alpha +/- .00015069
```

- Five missed fine-grid successes contribute `.00052149 alpha`; duration-only interpolation contributes only `(8.61 +/-4.13)e-6 alpha`.
- Rough cusp `R(h)=1-a_X|h|+O(h^2)`, `a_X~6.19142e-5`, gives Brownian `sqrt(dt)` continuity scale with `beta=-zeta(1/2)/sqrt(2pi)`.
- **WORDING CORRECTION:** because the coarse/fine result is driven by five events with ~47% relative SE, it is only statistically consistent with the parameter-free theoretical prediction in sign and scale; it does not verify the coefficient precisely.

### Step 47 — exact canonical alpha=1 grid correction
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

**EXACT CANONICAL FINITE-GRID CORRECTION.** Do not identify this with the finite-u physical ratio. Earlier language calling the five-event numerical agreement "essentially exact" is withdrawn; the canonical identity is exact, the empirical validation is not.

### Step 48 — hard-gated finite-u mixed transfer
At `X=7.16`:

```text
a_X   = 6.1914157127e-5
b_X   = 1.0001238283
u     = 4.9589834838
chi   = 3.0701227479e-4
Delta = 3.506747946e-3       (tangent grid for physical dt=.001)
delta = 1.5225630594e-6      (pure rough canonical grid)
```

Exact cellwise mixed-tangent decomposition:

```math
W(t_k+theta Delta)
=(1-theta)W_k+theta W_{k+1}
+sqrt(2delta) B_bridge(theta)
+Delta^2 theta(1-theta).
```

The finite-u parabolic cell bulge is bounded by `Delta^2/4=3.07432e-6`.

Paired generalized Dieker-Yakir calculation, `9000` paths, grids `Delta` and `Delta/128`:

```text
H_mix^Delta            .5677632065
H_mix^(Delta/128)      .5682959763
mixed relative loss    9.3748649e-4
paired SE(loss)        5.5146e-6
```

Exact pure-`alpha=1` loss across the same two canonical resolutions:

```text
9.2635965e-4.
```

Transfer residual:

```text
mixed ratio - pure ratio = -1.11268e-5
paired SE                 =  5.5088e-6
approx normal 95% interval [-2.1924e-5, -3.30e-7].
```

**PAIRED FINITE-LEVEL TRANSFER INTERVAL / HARD-GATE PASSED:** the mixed Brownian-parabola transfer is `O(1e-5)` at the working parameters, far smaller than the `O(9e-4)` grid loss. This is a controlled Monte Carlo diagnostic, not a distribution-free theorem. On nested lattices `H_mix^Delta<=H_mix^(Delta/128)<=H_mix^0`, so the mixed-tangent continuum loss is at least the resolved coarse-to-fine loss; within the mixed tangent the Step-44 `.001` grid is therefore not a plausible continuum certificate.

See `MIXED_TANGENT_GRID_TRANSFER_STEP.md` and `numerics/mixed_tangent_grid_transfer.py`.

---

## Current frontier / hard stop
The next and only allowed mathematical closure target is the **exact finite-window process remainder beyond the mixed tangent** on the extremal neighborhood. A legitimate next step must either:

1. bracket the exact covariance/rescaled process around the mixed tangent tightly enough to control this remainder;
2. produce a controlled numerical interval for that exact-process remainder strong enough to settle the witness;
3. show that this remainder is not worth closing, at which point the mathematical branch stops and the detector result is consolidated.

No further witness scans, new asymptotic constants, or unrelated Pickands refinements should be opened before this decision.

### Single next question — DO NOT ANSWER UNTIL PROMPTED
> Can the exact finite-window covariance be bracketed around the mixed tangent on the `Delta/128` extremal neighborhood strongly enough to bound the remaining exact-process remainder, or does that final remainder fail the hard stopping test and force consolidation?

---

## Scope boundary
Do not claim: faster universally better/worse; a universal scalar replacement for `D*`; the scanning protocol universally optimal; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 tiny-chi values as continuum truth; Step-31 empirical fit exact/required; Step-34 fully formal theorem; Step-36 uniform hazard theorem; `R~1`; `L_R=.8` analytic; numerical covariance constants as formal interval constants; raw empirical Bernstein certifies Step-33; `L0=.02` optimal; Step-44 as a continuum certificate; Step-45 witness differences as formal confidence statements; Step-46 coefficient empirically verified precisely; Step-47 `H_1^delta` as the finite-u physical ratio; Step-48 paired interval as distribution-free/theorem-level; `X=7.16` mathematically optimal; simultaneous 95% coverage across all q nodes; no re-entrant pocket for other task parameters; uniqueness of bandwidth optimum; illustrative hardware interpretations; novelty.