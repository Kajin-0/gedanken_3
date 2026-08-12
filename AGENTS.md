# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Forty-four logical steps completed. Step 44 performs the dedicated `L0=.02` truncated occupation-Palm fast rough-endpoint run. Four independent 50k batches (`n=200000`) give pooled long-cluster mean `.992616066 alpha`, sample SD `9.61850e-7`, and a genuine 95% one-sided empirical-Bernstein radius `.007302705 alpha`. Adding the Step-43 analytic short-cluster envelope `<.000039 alpha` yields `P_FA^(finite-grid,95%)/alpha<.999957771<1`. Thus finite-grid endpoint statistics are now certified pointwise. The margin is only `.00004223 alpha`; the old conservative `.002 alpha` timing-grid allowance overwhelms it, so the active frontier is continuum timing-grid bias or redesign of the witness time to create more margin. No universal scalar replacement metric and no novelty claim.

Read first:
1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. latest step: `experiments/01-equal-dstar-different-speed/TRUNCATED_PALM_ENDPOINT_CERTIFICATE_STEP.md`
4. latest helper: `experiments/01-equal-dstar-different-speed/numerics/truncated_palm_endpoint_certificate.py`
5. preceding step: `experiments/01-equal-dstar-different-speed/SHORT_CLUSTER_OSCILLATION_BOUND_STEP.md`

Live `main` overrides chat summaries or stale notes.

---

## Mandatory repository protocol
Before material writes: fetch live target; fetch exact blob SHA before replacement; never overwrite stale state; preserve corrections/failed branches; update `CURRENT_STATE.md` and `PROGRESS_LOG.md` when frontier changes.

Useful epistemic labels include: **DEFINED, ASSUMED, DERIVED, CONDITIONAL, COUNTEREXAMPLE, REFINEMENT, NEGATIVE RESULT, REJECTED SHORTCUT, FAILED NUMERICAL ESTIMATE, NUMERICAL VALIDATION, NUMERICAL CLOSURE, PARTIAL CERTIFICATE, NUMERICAL ENDPOINT CERTIFICATE, PAIRED NUMERICAL INTERVAL CLOSURE, TAIL-SENSITIVE ENVELOPE, EXACT VARIOGRAM ORDERING, ANALYTIC INTER-NODE ENVELOPE, RIGOROUS FINITE-GRID CONCENTRATION TEST, SHORT-CLUSTER GAUSSIAN ENVELOPE, RIGOROUS FINITE-GRID STATISTICAL CERTIFICATE, INVALIDATED, INVALIDATED INTERMEDIATE, INVALIDATED NUMERICAL VALUE, INVALIDATED NUMERICAL INTERPRETATION, ASYMPTOTIC, OPEN, NON-CLAIM.**

Do not use `novel`, `universal`, `fundamental`, `first`, etc. without a separate prior-art audit. `Universal` is allowed only for the explicitly model-reduced canonical crossover function.

---

## Compact surviving chain

### Steps 01–13
Equal scalar `D*` does not determine arbitrary temporal-signal performance. Full magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation Gaussian problem. Finite records create a task-level timing-search problem. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum. **FAILED NUMERICAL ESTIMATE:** Step-13 `ell~49` invalid; hard-window scan is locally Brownian-like.

### Steps 14–23
A genuine information bandwidth removes the cusp. Fixed physical signal/noise yields a shallow finite bandwidth optimum. For `r=2`, `Lambda=.895`, Rice's upper switch near `130.19` is **INVALIDATED**; Palm preserves only the lower switch `~21.7 +/- .3`. Rough endpoint `Lambda_cross^infinity~.905 +/- .004`, so `.895` remains fast-preferred.

### Steps 24–30
Finite bandwidth produces a two-parameter generalized Pickands problem. **INVALIDATED INTERMEDIATE:** coupling coefficient `.8131`; correct pointwise coefficient `.8906480701 sqrt(chi/zeta)`. Brownian-parabola scaling yields `mu=sqrt(2) zeta chi^(1/3)` and model-reduced canonical fast crossover `F(mu)`. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-chi values were grid biased.

### Steps 31–34
Step 31 empirical Palm bridge is superseded for the original high-band conclusion. Step 32 directly certifies through `kappa_f~170`, then raw crossing moments fail from micro-upcrossing multiplicity. Step 33 replaces crossings with finite-amplitude excursion clusters and exact occupation-Palm moments. Step 34 uses `q=kappa_f^-1/2` plus paired endpoint coupling to obtain a numerical high-band closure; its original inter-node allowance was empirical.

### Steps 35–36
The common-noise field is `L2`-regular in `q`; generic Gaussian supremum anti-concentration is far too coarse at `alpha=1e-6`. Step 36 supplies a rare-event-scaled fixed-cluster strip measure.

### Steps 37–38
Fixed-class Pickands theory gives high-threshold overshoot/hazard scale. Step 38 proves exact cross-elasticity ordering for the generalized Pickands constant. **REFINEMENT:** finite-u strip excess is remainder physics, not positive smoothing elasticity.

### Step 39
`R=N_a/N_tan~1.56`; small-amplitude second-order Pickands remainder is false at `u~5`. **REJECTED SHORTCUT:** proving `R~1` is the wrong target.

### Step 40
Cameron-Martin likelihood rearrangement plus a covariance-kernel RKHS barrier gives direct exact-event threshold translation. Numerical covariance constants remain non-interval.

### Step 41
Analytic common-noise interpolation replaces Step-34's empirical mesh allowance. Rough endpoint: deterministic net plus Brownian-type modulus/Borell. Finite q: exact Rice sup-tail envelope. **INVALIDATED NUMERICAL VALUE:** Step-35 tiny-q `0->.005` RMS `~5.4e-5` was cancellation damaged; asymptotics give `~2.69e-5`.

### Step 42
Raw inverse-duration Palm concentration fails distribution-free because the formal support is huge. Duration truncation gives exactly `P_FA<=E[C_long]+P(C_short>=1)`; at `L0=.02`, long-cluster support falls 40x.

### Step 43
A short successful cluster must execute a `.15` drop/rise near the `~5 sigma` decision level inside `.02`. Fine-net Gaussian discordance gives `P(C_short>=1)<3.9e-11<3.9e-5 alpha`, conditional on conservative numerical `rho_*` and `K_*`.

### Step 44 — current frontier
Dedicated rough-endpoint `L0=.02` long-cluster runs:

```text
seed       n       mean/alpha      sample SD
20260812   50000   .994615198      9.57248e-7
20260813   50000   .984590252      9.55595e-7
20260814   50000   .995087976      9.65325e-7
20260815   50000   .996170838      9.69148e-7
```

Pooled `n=200000`:

```text
mean/alpha          .992616066144
EB variance/alpha   .00584190324
EB range/alpha      .00146080182
EB radius/alpha     .00730270506
short bound/alpha   .000039
finite-grid UCB     .999957771204 alpha
```

**RIGOROUS FINITE-GRID STATISTICAL CERTIFICATE:** the implemented fast rough-endpoint statistic has a true 95% pointwise finite-sample upper confidence bound below `alpha`. This does not use a Gaussian Monte Carlo SE approximation.

The margin is only `.00004223 alpha`. The old conservative timing-grid allowance `.002 alpha` is ~47 times larger; adding it gives `1.00195777 alpha`. Therefore the finite-grid-to-continuum error is now the dominant fast endpoint gap.

---

## Current frontier
Either derive a sharp continuum timing-grid bias bound for the duration-truncated cluster statistic or shift the common witness time `X` slightly to create a materially larger fast proof margin before continuum certification. Later gaps: simultaneous confidence across high-band nodes, slow lower-ratio concentration, formal interval arithmetic.

### Single next question — DO NOT ANSWER UNTIL PROMPTED
> Can the finite-grid-to-continuum bias be controlled below the current `.000042 alpha` margin, or should `X` first be shifted to create more room?

---

## Scope boundary
Do not claim: faster universally better/worse; a universal scalar replacement for `D*`; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 fast values as continuum data; Step-31 empirical fit exact/required; Step-34 fully formal theorem; Step-36 uniform hazard theorem; `R~1`; `L_R=.8` analytic; numerical spectral/covariance constants as formal interval constants; raw empirical Bernstein certifies Step-33; `L0=.02` optimal; Step-44 as a continuum certificate; simultaneous 95% coverage across all q nodes; no re-entrant pocket for other task parameters; uniqueness of bandwidth optimum; illustrative GHz scales as hardware recommendation; novelty.
