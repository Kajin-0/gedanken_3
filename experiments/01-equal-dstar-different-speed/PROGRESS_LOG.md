# Progress Log — Experiment 01

**Consolidation note — 2026-08-12 18:18 EDT:** compact chronology preserving consequential results, corrections, invalidations, rejected shortcuts, numerical validations, and current stopping point. Full derivations remain in dedicated step files.

---

## Steps 01–13
Equal scalar `D*` does not determine arbitrary temporal-signal performance; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`. Full magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation Gaussian problem. Finite records produce a task-level timing-search problem. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum. **FAILED NUMERICAL ESTIMATE:** Step-13 rough-grid crossover `ell~49` invalid; hard-window scan is locally Brownian-like.

## Steps 14–23
A genuine finite information bandwidth removes the cusp. Fixed physical signal/noise yields a shallow finite bandwidth optimum. For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=.90`, `Lambda=.895`, Rice produced apparent switches near `25.49` and `130.19`; Palm preserves only the lower switch `~21.7 +/- .3`. **INVALIDATED:** upper Rice switch. Rough endpoint `Lambda_cross^infinity~.905 +/- .004`; `.895` remains fast-preferred.

## Steps 24–30
Finite bandwidth produces a two-parameter generalized Pickands problem. **INVALIDATED INTERMEDIATE:** coupling coefficient `.8131`; correct pointwise coefficient `.8906480701 sqrt(chi/zeta)`. Brownian-parabola scaling gives `mu=sqrt(2) zeta chi^(1/3)` and canonical fast crossover `F(mu)`. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-chi values were grid biased.

## Steps 31–34
Step 31 empirical Palm bridge is superseded for the original high-band conclusion. Step 32 directly certifies through `kappa_f~170`, then raw crossing moments fail from micro-upcrossing multiplicity. Step 33 replaces crossings with finite-amplitude excursion clusters and exact occupation-Palm moments. Step 34 uses `q=kappa_f^-1/2` plus paired endpoint coupling to give fast `<alpha`, slow `>alpha` over `170<=kappa_f<=infinity`; its original `0.0006 alpha` inter-node allowance was empirical.

## Steps 35–36
The common-noise field is `L2`-regular in `q`; generic Gaussian supremum anti-concentration is far too coarse at `alpha=1e-6`. Step 36 defines an exact fixed-cluster maximum measure yielding rare-event-scaled threshold-strip control.

## Steps 37–38
Fixed-class Pickands theory gives high-threshold overshoot/hazard scale `h_a~uN_a`. Step 38 proves exact generalized-Pickands cross-elasticity ordering and matched tangent hazard bound. **REFINEMENT:** finite-u strip excess is remainder physics, not positive smoothing elasticity.

## Step 39
`R=N_a/N_tan~1.56` at the fast witness, so small-amplitude second-order Pickands correction is false at `u~5`. **REJECTED SHORTCUT:** proving `R~1` is the wrong target.

## Step 40
Cameron-Martin likelihood rearrangement plus a covariance-kernel RKHS barrier gives direct rare-event threshold translation. Numerical midpoint covariance floor `~.92524` makes `1e-4` threshold motion harmless. **PARTIAL CERTIFICATE.**

## Step 41
Analytic common-noise interpolation replaces Step-34's empirical mesh allowance. Rough endpoint: deterministic time net plus Brownian-type modulus/Borell bound. Finite q: exact Rice upcrossing sup-tail bound. **INVALIDATED NUMERICAL VALUE:** Step-35 tiny-q `0->.005` RMS `~5.4e-5` was cancellation damaged; asymptotics give `~2.69e-5`. Conditional on node/grid numerics, continuous-q interpolation is controlled.

## Step 42
Raw inverse-duration Palm estimator is formally bounded but generic empirical Bernstein is useless: at the rough endpoint `n=50000`, 95% radius `~.24538 alpha`, dominated by the range term. Duration truncation yields

```math
P_FA<=E[C_long]+P(C_short>=1)
```

and reduces the long-cluster support by 40x at `L0=.02`.

## Step 43
A successful cluster shorter than `.02` must traverse amplitude `.15` between a level-a boundary and a point near `u~4.959` within `.02`. Fine-net Gaussian discordance plus conservative `rho_*=.99980`, `K_*=2e-4` gives

```math
P(C_short>=1)<3.9e-11<3.9e-5 alpha.
```

**SHORT-CLUSTER GAUSSIAN ENVELOPE / PARTIAL CERTIFICATE.**

## Step 44 — 18:18 EDT — dedicated truncated-Palm endpoint run
Dedicated `L0=.02` fast rough-endpoint runs on the Step-33 finite grid:

```text
seed       paths     mean/alpha       sample SD
20260812   50000     .994615198       9.57248e-7
20260813   50000     .984590252       9.55595e-7
20260814   50000     .995087976       9.65325e-7
20260815   50000     .996170838       9.69148e-7
```

All observed zero selected successful clusters with `L<.02`; this observation is not used for the short-cluster probability.

Pooling the four independent batches (`n=200000`) gives

```text
mean/alpha          .992616066144
sample SD           9.6184951e-7
EB variance/alpha   .00584190324
EB range/alpha      .00146080182
EB radius/alpha     .00730270506
short bound/alpha   .000039
```

Therefore

```math
\boxed{P_FA^{finite-grid,95\%}/alpha<.999957771<1.}
```

**RIGOROUS FINITE-GRID STATISTICAL CERTIFICATE:** the implemented fast rough-endpoint statistic now has a genuine 95% pointwise finite-sample upper confidence bound below `alpha`, not a Gaussian-SE heuristic.

The margin is only `.00004223 alpha`. The prior conservative grid allowance `.002 alpha` is about 47x larger; adding it gives `1.00195777 alpha`. Thus the main endpoint bottleneck is now continuum timing-grid bias rather than Monte Carlo sampling.

Full derivation: `TRUNCATED_PALM_ENDPOINT_CERTIFICATE_STEP.md`.  
Helper: `numerics/truncated_palm_endpoint_certificate.py`.

---

## Current stopping point
Finite-grid endpoint sampling statistics are certified; continuous-q interpolation is analytically controlled; short-cluster probability is negligible. The next issue is the finite-grid-to-continuum bias of the duration-truncated cluster statistic, or alternatively whether moving the common witness time slightly can create a larger proof margin before attempting continuum certification. Simultaneous multi-node confidence, slow lower-ratio concentration, and interval arithmetic remain later gaps.

### Single natural next question
> Can the finite-grid-to-continuum bias be bounded below `.000042 alpha`, or should the common witness time `X` be shifted first to create a materially larger fast margin?
