# Progress Log — Experiment 01

**Consolidation note — 2026-08-12 19:12 EDT:** compact chronology preserving consequential results, corrections, invalidations, negative results, numerical validations, and the current stopping point. Full derivations remain in dedicated step files.

---

## Steps 01–13
Equal scalar `D*` does not determine arbitrary temporal-signal performance; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`. Full magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation Gaussian problem. Finite records create task-level timing/search effects. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum. **FAILED NUMERICAL ESTIMATE:** Step-13 rough-grid crossover `ell~49` invalid; hard-window scan is Brownian-like locally.

## Steps 14–23
A genuine information bandwidth removes the cusp. Fixed physical signal/noise yields a shallow finite bandwidth optimum. Rice's apparent upper switch near `130.19` is **INVALIDATED**; Palm preserves only the lower switch `~21.7 +/- .3`. Rough endpoint `Lambda_cross^infinity~.905 +/- .004`, so `.895` remains fast-preferred.

## Steps 24–30
Finite bandwidth yields a two-parameter generalized Pickands problem. **INVALIDATED INTERMEDIATE:** coupling coefficient `.8131`; correct pointwise coefficient `.8906480701 sqrt(chi/zeta)`. Brownian-parabola scaling gives a model-reduced canonical fast crossover. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-chi values were grid biased.

## Steps 31–34
Step 31 empirical Palm bridge is superseded for the original high-band conclusion. Step 32 directly certifies through `kappa_f~170`, then raw crossing moments fail from micro-upcrossing multiplicity. Step 33 replaces crossings with finite-amplitude excursion clusters and exact occupation-Palm moments. Step 34 obtains a paired numerical high-band closure; its original continuous-q interpolation allowance was empirical.

## Steps 35–41
Step 35 proves `L2` regularity in `q`; generic Gaussian supremum anti-concentration is too coarse. Step 36 supplies a rare-event-scaled cluster strip measure. Steps 37–38 obtain high-threshold overshoot scale and exact generalized-Pickands elasticity ordering. Step 39 rejects a small-amplitude finite-u remainder (`R~1.56`). Step 40 gives Cameron-Martin exact-event threshold translation. Step 41 replaces empirical inter-node interpolation with analytic Gaussian-process control. **INVALIDATED NUMERICAL VALUE:** Step-35 tiny-q `0->.005` RMS `~5.4e-5` was cancellation damaged; endpoint asymptotics give `~2.69e-5`.

## Step 42
Raw inverse-duration Palm concentration fails distribution-free because the formal support is huge. Duration truncation yields exactly `P_FA<=E[C_long]+P(C_short>=1)` and reduces support 40x at `L0=.02`.

## Step 43
A successful cluster shorter than `.02` must traverse amplitude `.15` near the `~5 sigma` level inside `.02`. Fine-net Gaussian discordance plus conservative numerical covariance/metric envelopes gives `P(C_short>=1)<3.9e-11<3.9e-5 alpha`. **SHORT-CLUSTER GAUSSIAN ENVELOPE / PARTIAL CERTIFICATE.**

## Step 44
Dedicated `L0=.02` rough-endpoint long-cluster runs pooled to `n=200000` give

```text
mean/alpha          .992616066144
EB radius/alpha     .00730270506
short bound/alpha   .000039
finite-grid UCB     .999957771204 alpha
```

**RIGOROUS FINITE-GRID STATISTICAL CERTIFICATE:** `P_FA^(finite-grid,95%)/alpha<.9999578`. The remaining margin is only `.00004223 alpha`; timing-grid bias dominates.

## Step 45
Common-random-number witness-time scan: `X=7.50` gains fast margin `~.001575 alpha` with slow lower `~1.089 alpha`; `X=7.70` gains `~.002006 alpha` but slow lower falls to `~1.013 alpha`. **NEGATIVE RESULT / REFINEMENT:** witness shifting alone does not eliminate the need for continuum discretization analysis.

## Step 46
Nested common-path meshes `dt=.001,.0005,.00025`, pooled `24000` paths:

```text
fine(.00025)-coarse(.001)  = +.00053010 alpha +/- .00025069
fine(.00025)-medium(.0005) = +.00015785 alpha +/- .00015069
```

For `.001 -> .00025`, five fine-grid successful long components missed by the coarse grid contribute `.00052149 alpha`; duration-only weight change contributes only `(8.61 +/- 4.13)e-6 alpha`. **REFINEMENT:** missed between-sample threshold maxima dominate.

The rough cusp `R(h)=1-a_X|h|+O(h^2)`, `a_X~6.19142e-5`, gives local Brownian variance rate `2a_X`. Classical Brownian extreme discretization predicts

```math
Delta M_dt ~ beta sqrt(2a_Xdt),
qquad beta=-zeta(1/2)/sqrt(2pi)~.582597.
```

With the measured high-level cluster hazard, Step 46 predicts `.001` continuum correction `~1.025e-3 alpha` and `.001 -> .00025` shift `~5.125e-4 alpha`, matching paired `(5.301 +/- 2.507)e-4 alpha`. **ASYMPTOTIC / NUMERICAL VALIDATION.** The finite-dt one-sided problem remained open.

## Step 47 — 19:12 EDT — exact alpha=1 discrete Pickands correction
For the canonical rough Pickands tangent

```math
W(s)=sqrt(2)B(s)-|s|,
```

a physical timing step maps to canonical spacing

```math
\delta=a_Xu^2dt.
```

The continuous constant is `H_1^0=1`. Gaussian random-walk factorization of the discrete Pickands representation gives

```math
\boxed{
H_1^\delta
=\frac1\delta
\exp\left[-2\sum_{n>=1}\frac1n
\Phi\left(-\sqrt{n\delta/2}\right)\right]
=\nu(\sqrt{2\delta}).
}
```

At `X=7.16`, `u~4.95898348`, `a_X~6.1914157e-5`:

```text
dt         H_1^delta          loss
.00100     .998983867710      1.016132290e-3
.00050     .999281378993      7.186210075e-4
.00025     .999491804717      5.081952830e-4
```

Exact canonical `.001 -> .00025` loss difference is `5.07937007e-4`, versus the Step-46 paired `(5.3010 +/- 2.5069)e-4 alpha`.

**EXACT CANONICAL FINITE-GRID CORRECTION / REFINEMENT:** finite grid spacing is explicit inside the pure `alpha=1` Brownian tangent; Step 46's first-order `sqrt(dt)` law was already extremely accurate because the canonical spacing is tiny.

**NEGATIVE RESULT:** this does not give the exact finite-u physical grid/continuum ratio at `u~4.96`. The actual local extremal field retains the mixed Brownian-parabola structure of Steps 24–30, and finite-u cluster intensity is not equal to its leading tangent value.

Full derivation: `EXACT_ALPHA1_DISCRETE_PICKANDS_STEP.md`.  
Helper: `numerics/discrete_pickands_alpha1_correction.py`.

---

## Current stopping point
The finite-grid Brownian correction itself is no longer the theorem gap. The remaining task is to control **finite-threshold transfer** from the actual mixed Gaussian extreme problem to the exact pure-`alpha=1` discrete-Pickands ratio

```math
H_1^{a_Xu^2dt}=nu(u sqrt(2a_Xdt)).
```

### Single natural next question
> Can the mixed Brownian-parabola tangent from Steps 24–30 be compared monotonically with the pure `alpha=1` Pickands tangent strongly enough to bound the finite-u grid/continuum ratio around the exact value `H_1^{a_Xu^2dt}`?
