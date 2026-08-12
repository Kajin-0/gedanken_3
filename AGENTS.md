# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Forty-five logical steps completed. Step 45 tests witness-time redesign after Step 44's finite-grid endpoint certificate. A common-random-number rough-endpoint scan shows that increasing `X` only modestly lowers the fast truncated-Palm mean before the slow detector approaches feasibility: `X=7.50` gains about `.0016 alpha` while preserving a large slow margin, still less than the old `.002 alpha` continuum allowance; `X=7.70` gains about `.0020 alpha` but the slow rough-endpoint lower estimate falls to only `~1.0134 alpha`. **NEGATIVE RESULT:** witness-time tuning cannot robustly replace a continuum discretization bound. The active frontier is direct finite-grid-to-continuum control of the `L0=.02` duration-truncated fast cluster statistic, split into missed between-sample maxima and long-component duration-interpolation error. No universal scalar replacement metric and no novelty claim.

Read first:
1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. latest step: `experiments/01-equal-dstar-different-speed/WITNESS_TIME_MARGIN_SCAN_STEP.md`
4. latest helper: `experiments/01-equal-dstar-different-speed/numerics/witness_time_margin_scan.py`
5. preceding step: `experiments/01-equal-dstar-different-speed/TRUNCATED_PALM_ENDPOINT_CERTIFICATE_STEP.md`

Live `main` overrides chat summaries or stale notes.

---

## Mandatory repository protocol
Before material writes: fetch live target; fetch exact blob SHA before replacement; never overwrite stale state; preserve corrections/failed branches; update `CURRENT_STATE.md` and `PROGRESS_LOG.md` whenever the frontier changes.

Useful epistemic labels include: **DEFINED, ASSUMED, DERIVED, CONDITIONAL, COUNTEREXAMPLE, REFINEMENT, NEGATIVE RESULT, REJECTED SHORTCUT, FAILED NUMERICAL ESTIMATE, NUMERICAL VALIDATION, NUMERICAL CLOSURE, PARTIAL CERTIFICATE, NUMERICAL ENDPOINT CERTIFICATE, PAIRED NUMERICAL INTERVAL CLOSURE, TAIL-SENSITIVE ENVELOPE, EXACT VARIOGRAM ORDERING, ANALYTIC INTER-NODE ENVELOPE, RIGOROUS FINITE-GRID CONCENTRATION TEST, SHORT-CLUSTER GAUSSIAN ENVELOPE, RIGOROUS FINITE-GRID STATISTICAL CERTIFICATE, PAIRED NUMERICAL WITNESS SCAN, INVALIDATED, INVALIDATED INTERMEDIATE, INVALIDATED NUMERICAL VALUE, INVALIDATED NUMERICAL INTERPRETATION, ASYMPTOTIC, OPEN, NON-CLAIM.**

Do not use `novel`, `universal`, `fundamental`, `first`, etc. without a separate prior-art audit. `Universal` is allowed only for the explicitly model-reduced canonical crossover function.

---

## Compact surviving chain

### Steps 01–13
Equal scalar `D*` does not determine arbitrary temporal-signal performance. Full magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation Gaussian problem. Finite records create task-level timing/search effects. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum. **FAILED NUMERICAL ESTIMATE:** Step-13 `ell~49` invalid; hard-window scan is locally Brownian-like.

### Steps 14–23
A genuine information bandwidth removes the cusp. Fixed physical signal/noise yields a shallow finite bandwidth optimum. Rice's upper switch near `130.19` is **INVALIDATED**; Palm preserves only the lower switch `~21.7 +/- .3`. Rough endpoint `Lambda_cross^infinity~.905 +/- .004`, leaving `.895` fast-preferred.

### Steps 24–30
Finite bandwidth produces a two-parameter generalized Pickands problem. **INVALIDATED INTERMEDIATE:** coupling coefficient `.8131`; correct pointwise coefficient `.8906480701 sqrt(chi/zeta)`. Brownian-parabola scaling yields `mu=sqrt(2) zeta chi^(1/3)` and the model-reduced canonical fast crossover. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-chi values were grid biased.

### Steps 31–34
Step 31 empirical Palm bridge is superseded for the original high-band conclusion. Step 32 directly certifies through `kappa_f~170`, then raw crossing moments fail from micro-upcrossing multiplicity. Step 33 replaces crossings with finite-amplitude excursion clusters and exact occupation-Palm moments. Step 34 obtains a paired numerical high-band closure; its original interpolation allowance was empirical.

### Steps 35–41
Step 35 proves `L2` regularity in `q`; generic Gaussian anti-concentration is too coarse. Step 36 supplies a rare-event-scaled cluster strip measure. Steps 37–38 derive high-threshold overshoot scale and exact generalized-Pickands elasticity ordering. Step 39 rejects a small-amplitude finite-u remainder (`R~1.56`). Step 40 gives Cameron-Martin exact-event threshold translation. Step 41 replaces the empirical inter-node allowance with analytic Gaussian-process interpolation. **INVALIDATED NUMERICAL VALUE:** Step-35 tiny-q `0->.005` RMS `~5.4e-5` was cancellation damaged; asymptotics give `~2.69e-5`.

### Step 42
Raw inverse-duration Palm concentration is distribution-free but useless because of enormous formal support. Duration truncation gives exactly `P_FA<=E[C_long]+P(C_short>=1)` and reduces support 40x for `L0=.02`.

### Step 43
A short successful cluster must execute a `.15` excursion near the `~5 sigma` level inside `.02`. Fine-net Gaussian discordance gives `P(C_short>=1)<3.9e-11<3.9e-5 alpha`, conditional on conservative numerical covariance/metric constants.

### Step 44
Dedicated `L0=.02` rough-endpoint long-cluster runs pooled to `n=200000` give

```text
mean/alpha          .992616066144
EB radius/alpha     .00730270506
short bound/alpha   .000039
finite-grid UCB     .999957771204 alpha
```

**RIGOROUS FINITE-GRID STATISTICAL CERTIFICATE:** the implemented fast rough-endpoint statistic has a true 95% pointwise finite-sample upper bound below `alpha`. The margin is only `.00004223 alpha`; the old `.002 alpha` grid allowance overwhelms it.

### Step 45 — current frontier
Common-random-number witness-time scan:

```text
fast rough endpoint, 50000 paired paths
X       change from 7.16 / alpha     paired SE / alpha
7.50           -.001575                    .000789
7.70           -.002006                    .000735
```

Separate slow rough-endpoint pilots:

```text
X       slow lower/alpha     slow E[C]/alpha     SE[E(C)]/alpha
7.50       1.08933              1.09003              .00537
7.70       1.01340              1.01396              .00508
```

**PAIRED NUMERICAL WITNESS SCAN / NEGATIVE RESULT:** `X~7.5` is slow-safe but gains less fast margin than the old `.002 alpha` grid allowance. `X~7.7` only barely matches that allowance and makes the slow detector itself near-boundary. Witness retuning does not eliminate the need for a continuum timing-grid bound.

---

## Current frontier
Decompose the duration-truncated fast finite-grid error into two mechanisms: (1) missed between-sample level-u maxima inside otherwise long lower-level components and (2) error in the linearly interpolated component duration `L` for `L>=.02`. Replace the old undifferentiated `.002 alpha` allowance with explicit bounds on these mechanisms. A later small `X` adjustment may be revisited after the actual continuum-bias scale is known.

### Single next question — DO NOT ANSWER UNTIL PROMPTED
> Can the finite-grid error be decomposed into a missed-between-sample-success term and a long-component duration-interpolation term, and can each be bounded sharply enough to replace the old `0.002 alpha` allowance?

---

## Scope boundary
Do not claim: faster universally better/worse; a universal scalar replacement for `D*`; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 fast values as continuum data; Step-31 empirical fit exact/required; Step-34 fully formal theorem; Step-36 uniform hazard theorem; `R~1`; `L_R=.8` analytic; numerical spectral/covariance constants as formal interval constants; raw empirical Bernstein certifies Step-33; `L0=.02` optimal; Step-44 as continuum certificate; Step-45 witness differences as formal confidence statements; `X=7.16` as mathematically optimal; simultaneous 95% coverage across all q nodes; no re-entrant pocket for other task parameters; uniqueness of bandwidth optimum; hardware meaning of illustrative GHz scales; novelty.
