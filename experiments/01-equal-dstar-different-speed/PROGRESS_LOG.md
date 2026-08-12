# Progress Log — Experiment 01

**Consolidation note — 2026-08-12 18:55 EDT:** compact chronology preserving consequential results, corrections, invalidations, numerical validations, negative results, and the current stopping point. Full derivations remain in dedicated step files.

---

## Steps 01–13
Equal scalar `D*` does not determine arbitrary temporal-signal performance; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`. Full magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation Gaussian problem. Finite records create task-level timing/search effects. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum. **FAILED NUMERICAL ESTIMATE:** Step-13 rough-grid crossover `ell~49` invalid; hard-window scan is Brownian-like locally.

## Steps 14–23
A genuine information bandwidth removes the cusp. Fixed physical signal/noise yields a shallow finite bandwidth optimum. Rice's apparent upper switch near `130.19` is **INVALIDATED**; Palm preserves only the lower switch `~21.7 +/- .3`. Rough endpoint `Lambda_cross^infinity~.905 +/- .004`, so `.895` remains fast-preferred.

## Steps 24–30
Finite bandwidth yields a two-parameter generalized Pickands problem. **INVALIDATED INTERMEDIATE:** coupling coefficient `.8131`; correct pointwise coefficient `.8906480701 sqrt(chi/zeta)`. Brownian-parabola scaling gives the model-reduced canonical fast crossover. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-chi values were grid biased.

## Steps 31–34
Step 31 empirical Palm bridge is superseded for the original high-band conclusion. Step 32 directly certifies through `kappa_f~170`, then raw crossing moments fail from micro-upcrossing multiplicity. Step 33 replaces crossings with finite-amplitude excursion clusters and exact occupation-Palm moments. Step 34 obtains a paired numerical high-band closure; its original continuous-q interpolation allowance was empirical.

## Steps 35–41
Step 35 proves `L2` regularity in `q`; generic Gaussian supremum anti-concentration is too coarse. Step 36 supplies a rare-event-scaled cluster strip measure. Steps 37–38 obtain high-threshold overshoot scale and exact generalized-Pickands elasticity ordering. Step 39 rejects a small-amplitude finite-u remainder (`R~1.56`). Step 40 gives Cameron-Martin exact-event threshold translation. Step 41 replaces the empirical inter-node allowance with analytic Gaussian-process interpolation. **INVALIDATED NUMERICAL VALUE:** Step-35 tiny-q `0->.005` RMS `~5.4e-5` was cancellation damaged; asymptotics give `~2.69e-5`.

## Step 42
Raw inverse-duration Palm concentration fails distribution-free because the formal support is huge. Duration truncation yields exactly `P_FA<=E[C_long]+P(C_short>=1)` and reduces support 40x for `L0=.02`.

## Step 43
A successful cluster shorter than `.02` must traverse amplitude `.15` near the `~5 sigma` level inside `.02`. Fine-net Gaussian discordance plus conservative numerical covariance/metric envelopes gives `P(C_short>=1)<3.9e-11<3.9e-5 alpha`. **SHORT-CLUSTER GAUSSIAN ENVELOPE / PARTIAL CERTIFICATE.**

## Step 44
Dedicated `L0=.02` rough-endpoint long-cluster runs pooled to `n=200000` give `mean=.992616066 alpha`, 95% empirical-Bernstein radius `.007302705 alpha`, and Step-43 short bound `.000039 alpha`, yielding

```math
P_FA^{finite-grid,95\%}/alpha<.999957771<1.
```

**RIGOROUS FINITE-GRID STATISTICAL CERTIFICATE.** The remaining margin is only `.00004223 alpha`; timing-grid bias dominates.

## Step 45
Common-random-number witness-time scan: `X=7.50` gains fast margin `~.001575 alpha` with slow lower `~1.089 alpha`; `X=7.70` gains `~.002006 alpha` but slow lower falls to `~1.013 alpha`. **NEGATIVE RESULT / REFINEMENT:** witness shifting alone does not eliminate the need for a continuum discretization analysis.

## Step 46 — 18:55 EDT — rough-grid bias decomposition and Brownian scaling
Use common continuous-spectrum paths sampled at nested timing meshes `dt=.001,.0005,.00025`. Pool two independent `12000`-path runs.

Paired differences:

```text
fine(.00025)-coarse(.001)  = +.00053010 alpha +/- .00025069
fine(.00025)-medium(.0005) = +.00015785 alpha +/- .00015069
```

For `.001 -> .00025`, exactly five fine-grid successful long components were missed on the coarse grid. Their total mean contribution is `.00052149 alpha`. On paths where both meshes detect the same long success, the duration-weight change contributes only `(8.61 +/- 4.13)e-6 alpha`.

**REFINEMENT:** missed between-sample final-threshold maxima dominate the continuum bias; linearly interpolated long-component duration is negligible at this scale.

The hard-window rough endpoint has

```math
R(h)=1-a_X|h|+O(h^2),
\qquad a_X\simeq6.19142e-5,
```

so local increment variance is `2a_X|h|`. Classical Brownian extreme-value discretization has `sqrt(dt)` error with mean continuity-correction constant

```math
beta=-zeta(1/2)/sqrt(2pi)~.582597.
```

Thus the leading maximum amplitude correction is

```math
Delta M_dt ~ beta sqrt(2a_Xdt).
```

Combining with Step-36 cluster hazard `h_a(u)~5 alpha` per threshold unit gives

```math
Delta p_dt/alpha ~ 5 beta sqrt(2a_Xdt).
```

Numerically:

```text
dt=.00100   continuum correction ~1.025e-3 alpha
dt=.00050   continuum correction ~7.248e-4 alpha
dt=.00025   continuum correction ~5.125e-4 alpha
```

Predicted `.001 -> .00025` shift is `5.125e-4 alpha`, versus paired observed `(5.301 +/- 2.507)e-4 alpha`; the coefficient was not fit to the paired data. **ASYMPTOTIC / NUMERICAL VALIDATION.**

At `X=7.16`, the leading `.001` continuum correction is about 24 times the Step-44 certified finite-grid margin. Requiring that leading correction alone to fit the tiny Step-44 margin would need `dt~1.7e-6`, so brute-force refinement is unattractive.

**QUALIFICATION:** the Brownian continuity correction is asymptotic and is not yet a one-sided finite-`dt` theorem for the present Gaussian timing process.

Full derivation: `ROUGH_GRID_DISCRETIZATION_SCALING_STEP.md`.  
Helper: `numerics/rough_grid_discretization_scaling.py`.

---

## Current stopping point
The old `.002 alpha` grid allowance is now physically explained rather than opaque. The dominant missed-maximum bias follows the expected rough `sqrt(dt)` law and is about `.001 alpha` at the Step-44 mesh; duration interpolation is negligible. The next task is to promote the Brownian/Bessel extreme-value discretization asymptotic into a sharp one-sided finite-`dt` upper envelope for this covariance family.

### Single natural next question
> Can the Brownian/Bessel extreme-value discretization limit be converted into an explicit one-sided finite-`dt` upper envelope for the detector timing process, sharp enough to certify the `~1e-3 alpha` continuum correction rather than merely estimate it asymptotically?
