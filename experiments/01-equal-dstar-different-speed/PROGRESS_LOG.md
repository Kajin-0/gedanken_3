# Progress Log — Experiment 01

**Consolidation note — 2026-08-12 18:41 EDT:** compact chronology preserving consequential results, corrections, invalidations, numerical validations, negative results, and the current stopping point. Full derivations remain in dedicated step files.

---

## Steps 01–13
Equal scalar `D*` does not determine arbitrary temporal-signal performance; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`. Full magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation Gaussian problem. Finite records create task-level timing/search effects. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum. **FAILED NUMERICAL ESTIMATE:** Step-13 rough-grid crossover `ell~49` invalid; hard-window scan is Brownian-like locally.

## Steps 14–23
A genuine information bandwidth removes the cusp. Fixed physical signal/noise yields a shallow finite bandwidth optimum. For `r=2`, `Lambda=.895`, Rice's apparent upper switch near `130.19` is **INVALIDATED**; Palm preserves only the lower switch `~21.7 +/- .3`. Rough endpoint `Lambda_cross^infinity~.905 +/- .004`, so `.895` remains fast-preferred.

## Steps 24–30
Finite bandwidth yields a two-parameter generalized Pickands problem. **INVALIDATED INTERMEDIATE:** coupling coefficient `.8131`; correct pointwise coefficient `.8906480701 sqrt(chi/zeta)`. Brownian-parabola scaling gives `mu=sqrt(2) zeta chi^(1/3)` and the model-reduced canonical fast crossover. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-chi values were grid biased.

## Steps 31–34
Step 31 empirical Palm bridge is superseded for the original high-band conclusion. Step 32 directly certifies through `kappa_f~170`, then raw crossing moments fail from micro-upcrossing multiplicity. Step 33 replaces crossings with finite-amplitude excursion clusters and exact occupation-Palm moments. Step 34 uses `q=kappa_f^-1/2` plus paired endpoint coupling to obtain a numerical high-band closure; its original inter-node allowance was empirical.

## Steps 35–41
Step 35 proves `L2` regularity in `q`; generic Gaussian supremum anti-concentration is too coarse. Step 36 supplies a rare-event-scaled cluster strip measure. Steps 37–38 obtain high-threshold overshoot scale and exact generalized-Pickands elasticity ordering. Step 39 rejects a small-amplitude finite-u remainder expansion (`R~1.56`). Step 40 gives Cameron-Martin exact-event threshold translation. Step 41 replaces the empirical inter-node allowance with analytic Gaussian-process interpolation. **INVALIDATED NUMERICAL VALUE:** Step-35 tiny-q `0->.005` RMS `~5.4e-5` was cancellation damaged; asymptotics give `~2.69e-5`.

## Step 42
Raw inverse-duration Palm concentration fails distribution-free because the formal support is huge. At `n=50000`, empirical Bernstein radius is `~.24538 alpha`, dominated by the range term. Duration truncation yields exactly

```math
P_FA<=E[C_long]+P(C_short>=1)
```

and reduces support 40x for `L0=.02`.

## Step 43
A successful cluster shorter than `.02` must traverse amplitude `.15` near the `~5 sigma` level within `.02`. Fine-net Gaussian discordance plus conservative numerical `rho_*=.99980`, `K_*=2e-4` gives

```math
P(C_short>=1)<3.9e-11<3.9e-5 alpha.
```

**SHORT-CLUSTER GAUSSIAN ENVELOPE / PARTIAL CERTIFICATE.**

## Step 44
Dedicated `L0=.02` fast rough-endpoint runs, pooled `n=200000`:

```text
mean/alpha          .992616066144
sample SD           9.6184951e-7
EB variance/alpha   .00584190324
EB range/alpha      .00146080182
EB radius/alpha     .00730270506
short bound/alpha   .000039
finite-grid UCB     .999957771204 alpha
```

**RIGOROUS FINITE-GRID STATISTICAL CERTIFICATE:** `P_FA^(finite-grid,95%)/alpha<.9999578`. The remaining margin is only `.00004223 alpha`; the old `.002 alpha` grid allowance overwhelms it.

Full derivation: `TRUNCATED_PALM_ENDPOINT_CERTIFICATE_STEP.md`.  
Helper: `numerics/truncated_palm_endpoint_certificate.py`.

## Step 45 — 18:41 EDT — witness-time margin scan
Before attempting a sharp continuum discretization theorem, test whether moving the common witness time creates a larger fast proof margin.

A common-random-number `50000`-path fast rough-endpoint scan gives

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

**NEGATIVE RESULT / REFINEMENT:** increasing `X` only weakly improves the already-saturated fast endpoint. `X=7.5` keeps a robust slow margin but gains only `~.0016 alpha`, less than the old `.002 alpha` grid allowance. `X=7.7` gains `~.0020 alpha` but moves the slow detector itself close to feasibility. Witness-time redesign therefore does not create a comfortable continuum-proof margin and merely trades one near-boundary issue for another.

Full derivation: `WITNESS_TIME_MARGIN_SCAN_STEP.md`.  
Helper: `numerics/witness_time_margin_scan.py`.

---

## Current stopping point
The next logical task is the continuum timing-grid bias itself. For the duration-truncated fast statistic, split that error into (1) missed between-sample level-u successes inside otherwise long lower-level components and (2) error in the linearly interpolated long-component duration. The old undifferentiated `.002 alpha` allowance should be replaced by explicit bounds on these two mechanisms.

### Single natural next question
> Can the finite-grid error be decomposed into a missed-between-sample-success term and a long-component duration-interpolation term, and can each be bounded sharply enough to replace the old `0.002 alpha` allowance?
