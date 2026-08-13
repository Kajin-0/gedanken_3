# Progress Log — Experiment 01

**Consolidation note — 2026-08-12 19:53 EDT:** compact chronology preserving consequential results, invalidations, numerical corrections, hard-gate decisions, and final stopping point. Full derivations remain in dedicated step files.

---

## Steps 01–12 — detector/detection-theory core
Equal scalar reference `D*` does not determine arbitrary temporal-signal performance. Full magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation stationary-Gaussian problem. Finite records make phase/time placement relevant. Unknown arrival introduces global false-alarm timing-search complexity. In the defined scanning protocol, a controlled equal-eventual-SNR family can reverse fast/slow ranking because temporal compression changes both early evidence accumulation and timing-search complexity. This is protocol/task specific, not a universal detector theorem.

## Steps 13–23 — continuous search / bandwidth
Hard-window scan is locally Brownian-like. **FAILED NUMERICAL ESTIMATE:** early `ell~49` crossover invalid. Genuine finite information bandwidth removes the cusp; fixed physical signal/noise gives a shallow finite bandwidth optimum. Rice upper switch near `130` is **INVALIDATED**; Palm preserves only lower switch `~21.7 +/- .3`. Rough endpoint `Lambda_cross^infinity~.905 +/- .004` leaves original `.895` numerically fast-preferred.

## Steps 24–30 — generalized Pickands structure
Finite bandwidth gives generalized Pickands variogram `t^2+sqrt(2)chi F_zeta`. Exact Brown-Resnick Slepian monotonicity does not imply physical-boundary monotonicity. **INVALIDATED INTERMEDIATE:** `.8131` coupling coefficient; corrected `.8906480701 sqrt(chi/zeta)`. Brownian-parabola scaling uses `mu=sqrt(2)zeta chi^(1/3)`. Raw tiny-chi Step-27 values were grid biased and invalidated as continuum values.

## Steps 31–41 — finite-u closure machinery
Crossing moments work through `kappa_f~170`, then fail from micro-upcrossings; finite-amplitude excursion clusters replace them. Step 34 gives paired numerical high-band closure. Step 35 proves `L2` q-regularity; generic anti-concentration is too coarse. Step 36 gives rare-event cluster-strip control. Steps 37–38 derive overshoot scale and exact Pickands cross-elasticity. Step 39 finds `R=N_a/N_tan~1.56`, rejecting a small-amplitude remainder. Step 40 gives Cameron-Martin exact-event threshold translation. Step 41 gives analytic inter-node q control. **INVALIDATED NUMERICAL VALUE:** Step-35 tiny-q pair RMS `~5.4e-5`; corrected asymptotic `~2.69e-5`.

## Steps 42–44 — finite-sample endpoint statistics
Raw inverse-duration Palm concentration is formally bounded but useless because support is huge. Duration truncation at `L0=.02` separates bounded long weights from analytically negligible short clusters. Step 44 pools `n=200000` and gives genuine pointwise finite-grid 95% upper bound

```text
P_FA/alpha < .999957771
```

with only `.00004223 alpha` margin. Continuum timing-grid bias becomes dominant.

## Step 45 — witness-time test
`X=7.50` gains fast `~.001575 alpha` while slow lower remains `~1.089`; `X=7.70` gains `~.002006 alpha` but slow lower falls to `~1.013`. **NEGATIVE RESULT:** witness retuning alone trades one knife-edge for another.

## Step 46 — rough-grid mechanism
Nested `.001,.0005,.00025` grids, 24k paired paths:

```text
fine(.00025)-coarse(.001)  = +.00053010 alpha +/- .00025069
```

Five missed fine-grid successes contribute `.00052149 alpha`; duration-only interpolation contributes only `(8.61 +/-4.13)e-6 alpha`. **WORDING CORRECTION:** because this result is driven by five events with ~47% relative SE, it is only statistically consistent with theory in sign/scale, not a precise coefficient verification.

## Step 47 — exact canonical alpha=1 correction
For pure rough tangent `W(s)=sqrt(2)B(s)-|s|`, `delta=a_Xu^2dt` and

```math
H_1^delta=nu(sqrt(2delta)).
```

At `dt=.001`, exact canonical loss is `1.0161323e-3`. Exact `.001 -> .00025` loss difference is `5.07937e-4`. **EXACT CANONICAL FINITE-GRID CORRECTION.** Do not equate this with the exact finite-u physical false-alarm ratio.

## Step 48 — hard-gated mixed-tangent transfer
Mixed finite-u tangent has exact Brownian-bridge cell decomposition. Paired DY on `9000` paths, `Delta` versus `Delta/128`:

```text
mixed relative loss      9.3748649e-4
paired SE                5.5146e-6
pure alpha=1 loss        9.2635965e-4
mixed-pure residual     -1.11268e-5 +/-5.5088e-6
```

**HARD-GATE PASSED:** finite-u Brownian-parabola transfer is `O(1e-5)`, much smaller than the `O(9e-4)` grid effect.

## Step 49 — 19:53 EDT — exact finite-window covariance transfer / HARD STOP
The exact finite-window covariance is

```math
R_x(y)=e^{-y}[I_2(x-y)+yI_1(x-y)]/D_x,
```

and the truncated template admits the exact two-state representation

```math
dU=-Udt+dW,
\qquad dV=(U-V)dt,
```

```math
Z_raw(t)=V(t)-e^{-x}[V(t-x)+xU(t-x)].
```

This permits exact-covariance finite-u spectral simulation without the mixed tangent approximation.

Two independent `3000`-path runs, physical `dt=.001` versus `dt/32`, pooled `6000` paired paths:

```text
H_exact^Delta          .5528146649
H_exact^(Delta/32)     .5532776622
relative loss          8.3682629e-4
paired SE              6.8953e-6
approx 95% interval    [8.2331e-4,8.5034e-4]
```

Exact pure-alpha1 loss for the same refinement:

```text
8.3657896e-4.
```

Exact-covariance minus pure loss residual:

```text
+2.47e-7 +/-6.90e-6 (1 SE)
approx 95% residual interval ~[-1.33e-5,+1.38e-5].
```

`T=3` and `T=5` sensitivity pilots overlap the `T=4` result.

**PAIRED EXACT-COVARIANCE TRANSFER INTERVAL:** higher-order finite-window covariance terms do not generate an order-`1e-4` cancellation of the discretization effect.

**HARD-STOP TRIGGERED:** the remaining publication-grade finite-u theorem connecting exact-covariance spectral intensity to the exact finite-search false-alarm event is no longer proportionate to the detector question. Stop this mathematical closure branch.

Full derivation: `EXACT_COVARIANCE_GRID_TRANSFER_STOP_STEP.md`.  
Helper: `numerics/exact_covariance_grid_transfer.py`.

---

## Final stopping point
Do not continue to Step 50 of this proof chain by default.

Next work should be detector-facing consolidation:
1. extract the core task theorem/result from Steps 01–12;
2. separate Steps 13–49 as a technical mathematical companion/appendix track;
3. perform a serious prior-art/novelty audit before novelty language;
4. reopen the closure branch only if external review identifies a decision-relevant gap.
