# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Forty-six logical steps completed. Step 46 decomposes the remaining rough-endpoint timing-grid bias. Nested common-path meshes show that essentially all positive coarse-to-fine correction comes from missed between-sample final-threshold maxima, while duration-weight interpolation is negligible. The hard-window covariance cusp gives local Brownian variance rate `2a_X`, `a_X~6.19142e-5`, so classical Brownian extreme-value discretization predicts a `sqrt(dt)` maximum correction with coefficient `beta=-zeta(1/2)/sqrt(2pi)~.582597`. Combining with the measured high-threshold cluster hazard predicts a `.001`-grid continuum correction `~1.03e-3 alpha` and a `.001 -> .00025` shift `~5.13e-4 alpha`, matching the paired nested-grid result `~5.30e-4 alpha`. The old `.002 alpha` allowance was conservative but represented a real rough-grid effect. The active frontier is to turn this Brownian/Bessel asymptotic into an explicit one-sided finite-`dt` bound. No universal scalar replacement metric and no novelty claim.

Read first:
1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. latest step: `experiments/01-equal-dstar-different-speed/ROUGH_GRID_DISCRETIZATION_SCALING_STEP.md`
4. latest helper: `experiments/01-equal-dstar-different-speed/numerics/rough_grid_discretization_scaling.py`
5. preceding step: `experiments/01-equal-dstar-different-speed/WITNESS_TIME_MARGIN_SCAN_STEP.md`

Live `main` overrides chat summaries or stale notes.

---

## Mandatory repository protocol
Before material writes: fetch live target; fetch exact blob SHA before replacement; never overwrite stale state; preserve corrections/failed branches; update `CURRENT_STATE.md` and `PROGRESS_LOG.md` whenever the frontier changes.

Useful epistemic labels include: **DEFINED, ASSUMED, DERIVED, CONDITIONAL, COUNTEREXAMPLE, REFINEMENT, NEGATIVE RESULT, REJECTED SHORTCUT, FAILED NUMERICAL ESTIMATE, NUMERICAL VALIDATION, NUMERICAL CLOSURE, PARTIAL CERTIFICATE, NUMERICAL ENDPOINT CERTIFICATE, PAIRED NUMERICAL INTERVAL CLOSURE, TAIL-SENSITIVE ENVELOPE, EXACT VARIOGRAM ORDERING, ANALYTIC INTER-NODE ENVELOPE, RIGOROUS FINITE-GRID CONCENTRATION TEST, SHORT-CLUSTER GAUSSIAN ENVELOPE, RIGOROUS FINITE-GRID STATISTICAL CERTIFICATE, PAIRED NUMERICAL WITNESS SCAN, PAIRED NESTED-GRID DIAGNOSTIC, ASYMPTOTIC, INVALIDATED, INVALIDATED INTERMEDIATE, INVALIDATED NUMERICAL VALUE, INVALIDATED NUMERICAL INTERPRETATION, OPEN, NON-CLAIM.**

Do not use `novel`, `universal`, `fundamental`, `first`, etc. without a separate prior-art audit. `Universal` is allowed only for the explicitly model-reduced canonical crossover function.

---

## Compact surviving chain

### Steps 01–13
Equal scalar `D*` does not determine arbitrary temporal-signal performance. Full magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation Gaussian problem. Finite records create task-level timing/search effects. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum. **FAILED NUMERICAL ESTIMATE:** Step-13 `ell~49` invalid; hard-window scan is locally Brownian-like.

### Steps 14–23
A genuine information bandwidth removes the cusp. Fixed physical signal/noise yields a shallow finite bandwidth optimum. Rice's upper switch near `130.19` is **INVALIDATED**; Palm preserves only lower switch `~21.7 +/- .3`. Rough endpoint `Lambda_cross^infinity~.905 +/- .004`, leaving `.895` fast-preferred.

### Steps 24–30
Finite bandwidth produces a two-parameter generalized Pickands problem. **INVALIDATED INTERMEDIATE:** coupling coefficient `.8131`; correct pointwise coefficient `.8906480701 sqrt(chi/zeta)`. Brownian-parabola scaling yields the model-reduced canonical fast crossover. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-chi values were grid biased.

### Steps 31–34
Step 31 empirical Palm bridge is superseded for the original high-band conclusion. Step 32 directly certifies through `kappa_f~170`, then raw crossing moments fail from micro-upcrossing multiplicity. Step 33 replaces crossings with finite-amplitude excursion clusters and exact occupation-Palm moments. Step 34 obtains a paired numerical high-band closure; its original interpolation allowance was empirical.

### Steps 35–41
Step 35 proves `L2` regularity in `q`; generic Gaussian anti-concentration is too coarse. Step 36 supplies a rare-event-scaled cluster strip measure. Steps 37–38 derive high-threshold overshoot scale and exact generalized-Pickands elasticity ordering. Step 39 rejects a small-amplitude finite-u remainder (`R~1.56`). Step 40 gives Cameron-Martin exact-event threshold translation. Step 41 replaces empirical inter-node interpolation with analytic Gaussian-process control. **INVALIDATED NUMERICAL VALUE:** Step-35 tiny-q `0->.005` RMS `~5.4e-5` was cancellation damaged; asymptotics give `~2.69e-5`.

### Step 42
Raw inverse-duration Palm concentration is bounded but useless because formal support is huge. Duration truncation gives exactly `P_FA<=E[C_long]+P(C_short>=1)` and reduces support 40x at `L0=.02`.

### Step 43
A short successful cluster must traverse `.15` near the `~5 sigma` level within `.02`. Fine-net Gaussian discordance gives `P(C_short>=1)<3.9e-11<3.9e-5 alpha`, conditional on conservative numerical covariance/metric constants.

### Step 44
Dedicated `L0=.02` rough-endpoint runs pooled to `n=200000` give a genuine 95% finite-grid upper confidence bound `P_FA/alpha<.999957771`. **RIGOROUS FINITE-GRID STATISTICAL CERTIFICATE.** Remaining margin `.00004223 alpha`; continuum grid bias dominates.

### Step 45
Witness-time scan: `X=7.50` gains fast `~.001575 alpha` with slow lower `~1.089`; `X=7.70` gains `~.002006 alpha` but slow lower falls to `~1.013`. **NEGATIVE RESULT:** witness shifting alone does not remove the need for discretization analysis.

### Step 46 — current frontier
Nested rough-endpoint timing meshes, pooled `24000` common paths:

```text
fine(.00025)-coarse(.001)  = +.00053010 alpha +/- .00025069
fine(.00025)-medium(.0005) = +.00015785 alpha +/- .00015069
```

For `.001 -> .00025`, five missed fine-grid successful long components contribute `.00052149 alpha`; duration-only weight change on components seen on both grids contributes only `(8.61 +/- 4.13)e-6 alpha`.

**REFINEMENT:** missed between-sample `u` maxima dominate; long-duration interpolation is negligible.

With rough cusp `R(h)=1-a_X|h|+O(h^2)`, `a_X~6.19142e-5`, local variance rate is `2a_X`. Classical Brownian extreme-value discretization gives

```math
Delta M_dt ~ beta sqrt(2a_Xdt),
beta=-zeta(1/2)/sqrt(2pi)~.582597.
```

Using Step-36 hazard `~5 alpha` per threshold unit:

```text
dt=.001    leading continuum correction ~1.025e-3 alpha
dt=.0005   ~7.248e-4 alpha
dt=.00025  ~5.125e-4 alpha
```

Predicted `.001 -> .00025` shift `5.125e-4 alpha` agrees with paired `5.301e-4 alpha` without fitted coefficient. **PAIRED NESTED-GRID DIAGNOSTIC / ASYMPTOTIC / NUMERICAL VALIDATION.** This is not a finite-`dt` one-sided theorem.

---

## Current frontier
Promote the Brownian/Bessel extreme-value continuity correction from an asymptotic description into an explicit one-sided finite-`dt` envelope for the detector timing covariance. Generic modulus bounds are too loose; the bound must exploit the local high-extreme Brownian/Bessel structure. A later moderate witness shift such as `X~7.5` may become useful once this finite-`dt` correction is certified.

### Single next question — DO NOT ANSWER UNTIL PROMPTED
> Can the Brownian/Bessel extreme-value discretization limit be converted into an explicit one-sided finite-`dt` upper envelope for the present Gaussian timing process, sharp enough to certify the `~1e-3 alpha` continuum correction rather than merely estimate it asymptotically?

---

## Scope boundary
Do not claim: faster universally better/worse; a universal scalar replacement for `D*`; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 fast values as continuum data; Step-31 empirical fit exact/required; Step-34 fully formal theorem; Step-36 uniform hazard theorem; `R~1`; `L_R=.8` analytic; numerical spectral/covariance constants as formal interval constants; raw empirical Bernstein certifies Step-33; `L0=.02` optimal; Step-44 as continuum certificate; Step-45 witness differences as formal confidence statements; Step-46 Brownian correction as a finite-`dt` upper bound; `X=7.16` mathematically optimal; simultaneous 95% coverage across q nodes; no re-entrant pocket for other task parameters; uniqueness of bandwidth optimum; hardware meaning of illustrative GHz scales; novelty.
