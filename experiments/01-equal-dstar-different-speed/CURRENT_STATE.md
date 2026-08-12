# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-12 18:41 EDT  
**Status:** forty-five logical steps completed. Step 45 tests whether shifting the common witness time can create enough extra fast-detector proof margin to avoid a difficult finite-grid-to-continuum analysis. Common-random-number rough-endpoint scans show only a modest fast gain before the slow detector approaches feasibility: `X=7.50` lowers the fast truncated Palm mean by about `0.0016 alpha` relative to `X=7.16`, but this is still smaller than the old `0.002 alpha` grid allowance; `X=7.70` gains about `0.0020 alpha`, but the slow rough-endpoint lower estimate falls to only `~1.0134 alpha`. **NEGATIVE RESULT:** witness-time redesign alone trades the fast grid knife-edge for a slow decision-time knife-edge and does not create a comfortable proof margin. The active frontier is now a direct decomposition and bound of the timing-grid bias of the `L0=.02` duration-truncated cluster statistic. No universal scalar replacement metric and no novelty claim.

---

## Original question
Two hypothetical photodetectors satisfy `D_A^*=D_B^*` but have radically different temporal responses. Does equal conventional specific detectivity imply equal ability to detect arbitrary optical signals?

## Surviving logical chain

### Steps 01–13 — scalar D*, finite records, rough-window obstruction
Equal scalar reference `D*` does not determine arbitrary temporal-signal performance; explicit 1 Hz construction gave `SNR_A/SNR_B~6.36`. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation stationary-Gaussian problem. Finite observation creates task-level timing/search effects. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed directly with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum. Step 13 identifies Brownian-like local roughness. **FAILED NUMERICAL ESTIMATE:** rough-grid crossover `ell~49` invalid.

### Steps 14–23 — genuine information bandwidth; Rice reversal corrected
A genuine timing-information bandwidth removes the cusp. Fixed physical signal/noise produces a shallow finite bandwidth optimum. For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=.90`, `Lambda=.895`, Rice gave switches near `25.49` and `130.19`; Palm preserves only the lower switch `~21.7 +/- .3`. **INVALIDATED:** upper Rice switch. Rough endpoint `Lambda_cross^infinity~.905 +/- .004`, leaving `.895` fast-preferred.

### Steps 24–30 — generalized Pickands crossover
Finite bandwidth produces a two-parameter local-extreme problem. **INVALIDATED INTERMEDIATE:** coupling coefficient `.8131`; correct pointwise coefficient `.8906480701 sqrt(chi/zeta)`. Brownian-parabola scaling gives `mu=sqrt(2) zeta chi^(1/3)` and the model-reduced canonical crossover `F(mu)`. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-chi values were grid biased.

### Steps 31–34 — direct finite-u high-band closure
Step 31's empirical Palm bridge is superseded for the original conclusion. Step 32 directly certifies through `kappa_f~170`, then raw crossing moments fail from micro-upcrossing multiplicity. Step 33 replaces crossings with finite-amplitude excursion clusters and exact occupation-Palm moments. Step 34 uses `q=kappa_f^-1/2` plus paired endpoint coupling to give a numerical high-band closure; its original `0.0006 alpha` inter-node allowance was empirical.

### Steps 35–41 — analytic continuity and rare-event threshold control
Step 35 proves `L2` regularity in `q`; generic Gaussian supremum anti-concentration is too coarse. Step 36 gives a rare-event-scaled fixed-cluster strip measure. Steps 37–38 derive high-threshold overshoot scale and exact generalized-Pickands cross-elasticity ordering. Step 39 shows `R=N_a/N_tan~1.56`, rejecting a small-amplitude remainder expansion. Step 40 uses a Cameron-Martin covariance-kernel barrier for direct exact-event threshold translation. Step 41 analytically controls interpolation between sampled `q` nodes. **INVALIDATED NUMERICAL VALUE:** Step-35 tiny-q `0->.005` RMS `~5.4e-5` was cancellation damaged; asymptotics give `~2.69e-5`.

### Step 42 — raw Palm concentration obstruction
The raw inverse-duration finite-grid Palm estimator is bounded but has an enormous formal range. Empirical Bernstein at `n=50000` gives radius `~.24538 alpha`, dominated by the support term. **NEGATIVE RESULT / REJECTED SHORTCUT:** generic bounded-variable concentration is useless on the raw estimator. Duration truncation gives exactly

```math
P_FA <= E[C_long] + P(C_short>=1).
```

For `L0=.02`, long-cluster support falls 40x.

### Step 43 — short-cluster Gaussian envelope
A successful cluster shorter than `.02` must traverse amplitude `.15` near the `~5 sigma` level inside `.02`. Fine-net Gaussian discordance plus conservative numerical `rho_*=.99980`, `K_*=2e-4` gives

```math
P(C_short>=1)<3.9e-11<3.9e-5 alpha.
```

**SHORT-CLUSTER GAUSSIAN ENVELOPE / PARTIAL CERTIFICATE.**

### Step 44 — finite-grid statistical certificate
Dedicated rough-endpoint `L0=.02` runs, four independent batches of `50000`, pooled `n=200000`:

```text
mean/alpha          .992616066144
sample SD           9.6184951e-7
EB variance/alpha   .00584190324
EB range/alpha      .00146080182
EB radius/alpha     .00730270506
short bound/alpha   .000039
finite-grid UCB     .999957771204 alpha
```

Therefore

```math
\boxed{P_FA^{finite-grid,95\%}/alpha<.9999578<1.}
```

**RIGOROUS FINITE-GRID STATISTICAL CERTIFICATE.** The margin is only `.00004223 alpha`; the old conservative timing-grid allowance `.002 alpha` overwhelms it.

### Step 45 — witness-time margin scan
Use common random numbers to compare the fast rough-endpoint duration-truncated Palm estimator across `X`.

A `50000`-path paired check gives

```text
X       mean/alpha     change from X=7.16 / alpha     paired SE / alpha
7.16    .998787                  0                          --
7.50    .997212               -.001575                    .000789
7.70    .996781               -.002006                    .000735
```

Separate `30000`-path slow rough-endpoint pilots give

```text
X       slow lower/alpha     slow E[C]/alpha     SE[E(C)]/alpha
7.50       1.08933              1.09003              .00537
7.70       1.01340              1.01396              .00508
```

**NEGATIVE RESULT:** `X~7.5` keeps a strong slow margin but gains less fast margin than the old `.002 alpha` continuum allowance. Pushing to `X~7.7` only barely matches that allowance while making the slow branch another near-boundary problem. Witness-time tuning is not a robust substitute for a continuum discretization bound.

See `WITNESS_TIME_MARGIN_SCAN_STEP.md` and `numerics/witness_time_margin_scan.py`.

---

## Current frontier
Attack the timing-grid bias directly for the `L0=.02` duration-truncated fast cluster statistic. The error should now be decomposed into (1) missed between-sample successful maxima inside otherwise long lower-level components and (2) error in linearly interpolated long-component durations. A small later adjustment of `X` may be useful after the actual continuum-bias scale is known, but there is no evidence that witness redesign removes the need for the bound.

### Single next question — DO NOT ANSWER YET
> Can the finite-grid error be decomposed into a missed-between-sample-success term and a long-component duration-interpolation term, and can each be bounded sharply enough to replace the old undifferentiated `0.002 alpha` allowance?

---

## Scope boundary
Do not claim: faster universally better/worse; a universal scalar replacement for `D*`; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 fast values as continuum data; Step-31 empirical fit exact/required; Step-34 fully formal theorem; Step-36 uniform hazard theorem; `R~1`; `L_R=.8` analytic; numerical spectral/covariance constants as formal interval constants; raw empirical Bernstein certifies Step-33; `L0=.02` optimal; Step-44 as a continuum certificate; Step-45 witness differences as formal confidence statements; `X=7.16` as mathematically optimal; simultaneous 95% coverage across all q nodes; no re-entrant pocket for other task parameters; uniqueness of bandwidth optimum; hardware meaning of illustrative GHz scales; novelty.
