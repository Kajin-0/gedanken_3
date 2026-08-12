# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-12 18:55 EDT  
**Status:** forty-six logical steps completed. Step 46 decomposes the remaining rough-endpoint timing-grid bias. Nested common-path meshes `dt=.001,.0005,.00025` show that essentially the entire positive coarse-to-fine correction comes from missed between-sample level-`u` maxima; the duration-weight interpolation error among components seen on both grids is only `~8.6e-6 alpha`. The rough covariance cusp `R(h)=1-a|h|+O(h^2)`, `a~6.19142e-5`, implies local Brownian variance rate `2a`, and classical Brownian extreme-value discretization predicts a `sqrt(dt)` maximum correction with coefficient `beta=-zeta(1/2)/sqrt(2pi)~.582597`. Combining this with the measured high-level cluster hazard `~5 alpha` per threshold unit predicts a continuum correction `~1.03e-3 alpha` from the `.001` grid and a `.001 -> .00025` difference `~5.13e-4 alpha`, in excellent agreement with the paired result `(5.30 +/- 2.51)e-4 alpha`. The old `.002 alpha` grid allowance was conservative but guarded a real rough-grid effect. The Brownian correction is asymptotic, not yet a finite-`dt` one-sided theorem. No universal scalar replacement metric and no novelty claim.

---

## Surviving chain

### Steps 01–13
Equal scalar reference `D*` does not determine arbitrary temporal-signal performance. Full magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation stationary-Gaussian problem. Finite records create task-level timing/search effects. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed directly with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum. Step 13 identifies Brownian-like local roughness. **FAILED NUMERICAL ESTIMATE:** rough-grid crossover `ell~49` invalid.

### Steps 14–23
A genuine timing-information bandwidth removes the cusp. Fixed physical signal/noise produces a shallow finite bandwidth optimum. Rice's apparent upper switch near `130.19` is **INVALIDATED**; Palm preserves only the lower switch `~21.7 +/- .3`. Rough endpoint `Lambda_cross^infinity~.905 +/- .004`, leaving `.895` fast-preferred.

### Steps 24–30
Finite bandwidth produces a two-parameter generalized Pickands problem. **INVALIDATED INTERMEDIATE:** coupling coefficient `.8131`; correct pointwise coefficient `.8906480701 sqrt(chi/zeta)`. Brownian-parabola scaling gives `mu=sqrt(2)zeta chi^(1/3)` and a model-reduced canonical crossover. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-chi values were grid biased.

### Steps 31–34
Step 31 empirical Palm bridge is superseded for the original high-band conclusion. Step 32 directly certifies through `kappa_f~170`, then raw crossing moments fail from micro-upcrossing multiplicity. Step 33 replaces crossings by finite-amplitude excursion clusters and exact occupation-Palm moments. Step 34 obtains a paired numerical high-band closure; its original continuous-q interpolation allowance was empirical.

### Steps 35–41
Step 35 proves `L2` regularity in `q`; generic Gaussian anti-concentration is too coarse. Step 36 supplies a rare-event-scaled cluster strip measure. Steps 37–38 derive high-threshold overshoot scale and exact generalized-Pickands elasticity ordering. Step 39 rejects a small-amplitude finite-u remainder (`R~1.56`). Step 40 gives Cameron-Martin exact-event threshold translation. Step 41 replaces the empirical inter-node allowance with analytic Gaussian-process interpolation. **INVALIDATED NUMERICAL VALUE:** Step-35 tiny-q `0->.005` RMS `~5.4e-5` was cancellation damaged; asymptotics give `~2.69e-5`.

### Step 42
Raw inverse-duration Palm concentration is distribution-free but useless because the formal support is huge. Duration truncation gives exactly `P_FA<=E[C_long]+P(C_short>=1)` and reduces support 40x for `L0=.02`.

### Step 43
A short successful cluster must execute a `.15` excursion near the `~5 sigma` level inside `.02`. Fine-net Gaussian discordance gives `P(C_short>=1)<3.9e-11<3.9e-5 alpha`, conditional on conservative numerical covariance/metric constants.

### Step 44
Dedicated `L0=.02` rough-endpoint long-cluster runs pooled to `n=200000` give `mean=.992616066 alpha`, 95% empirical-Bernstein radius `.007302705 alpha`, and Step-43 short bound `.000039 alpha`, yielding

```math
P_FA^{finite-grid,95\%}/alpha<.999957771<1.
```

**RIGOROUS FINITE-GRID STATISTICAL CERTIFICATE.** Margin only `.00004223 alpha`; continuum grid bias dominates.

### Step 45
Common-random-number witness scan: `X=7.50` lowers fast mean by `~.001575 alpha` while slow lower remains `~1.089 alpha`; `X=7.70` gains `~.002006 alpha` but slow lower falls to `~1.013 alpha`. **NEGATIVE RESULT:** witness tuning alone does not remove the need to understand discretization.

### Step 46 — rough-grid discretization mechanism
Nested common-path meshes, pooled `24000` paths:

```text
fine(.00025)-coarse(.001)  = +.00053010 alpha +/- .00025069
fine(.00025)-medium(.0005) = +.00015785 alpha +/- .00015069
```

For `.001 -> .00025`, five fine-grid successful components were missed by the coarse grid and contributed `.00052149 alpha`; duration-weight change on components successful on both grids contributed only `(8.61 +/- 4.13)e-6 alpha`.

At `X=7.16`, `a_X~6.19142e-5`, so local increment variance is `~2a_X|h|`. Brownian extreme-value discretization gives leading maximum bias

```math
Delta M_dt ~ beta sqrt(2 a_X dt),
qquad beta=-zeta(1/2)/sqrt(2pi)~.582597.
```

With cluster hazard `h_a(u)~5 alpha`, leading false-alarm correction is

```math
Delta p_dt/alpha ~ 5 beta sqrt(2 a_X dt).
```

Thus

```text
dt=.00100  continuum correction ~1.025e-3 alpha
dt=.00050  continuum correction ~7.248e-4 alpha
dt=.00025  continuum correction ~5.125e-4 alpha
```

and predicted `.001 -> .00025` shift `5.125e-4 alpha`, matching paired `5.301e-4 alpha` without fitting the coefficient. **ASYMPTOTIC / NUMERICAL VALIDATION.** The correction is not yet a one-sided finite-grid theorem.

See `ROUGH_GRID_DISCRETIZATION_SCALING_STEP.md` and `numerics/rough_grid_discretization_scaling.py`.

---

## Current frontier
The timing-grid bias is no longer an undifferentiated numerical allowance. Missed between-sample high maxima dominate and follow a physically expected `sqrt(dt)` rough-extreme continuity correction; duration interpolation is negligible at the present scale. At `X=7.16`, the leading `.001` continuum correction `~.00103 alpha` is still about 24 times the Step-44 certified margin, so brute refinement to preserve that tiny margin would require an unattractive `dt~1.7e-6` by the asymptotic estimate.

### Single next question — DO NOT ANSWER YET
> Can the Brownian/Bessel extreme-value discretization limit be converted into an explicit one-sided finite-`dt` upper envelope for the present Gaussian timing process, sharp enough to certify the `~1e-3 alpha` continuum correction rather than merely estimate it asymptotically?

---

## Scope boundary
Do not claim: faster universally better/worse; a universal scalar replacement for `D*`; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 fast values as continuum data; Step-31 empirical fit exact/required; Step-34 fully formal theorem; Step-36 uniform hazard theorem; `R~1`; `L_R=.8` analytic; numerical spectral/covariance constants as formal interval constants; raw empirical Bernstein certifies Step-33; `L0=.02` optimal; Step-44 as continuum certificate; Step-45 witness differences as formal confidence statements; Step-46 Brownian correction as a finite-`dt` bound; `X=7.16` mathematically optimal; simultaneous 95% coverage across q nodes; no re-entrant pocket for other task parameters; uniqueness of bandwidth optimum; hardware meaning of illustrative GHz scales; novelty.
