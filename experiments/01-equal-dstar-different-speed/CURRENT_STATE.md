# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-12 18:18 EDT  
**Status:** forty-four logical steps completed. Step 44 performs the dedicated `L0=.02` truncated occupation-Palm rough-endpoint calculation. Four independent 50k-path batches (`n=200000`) give pooled long-cluster mean `0.992616066 alpha`, sample SD `9.61850e-7`, and a genuine 95% one-sided Maurer-Pontil empirical-Bernstein radius `0.007302705 alpha`. Adding the Step-43 analytic short-cluster envelope `<3.9e-5 alpha` yields `P_FA^(finite-grid,95%)/alpha < 0.999957771 < 1`. Thus the implemented finite-grid fast rough-endpoint statistic is now statistically certified at 95% pointwise confidence. The certified margin is only `4.22e-5 alpha`; adding the older conservative `0.002 alpha` timing-grid allowance gives `1.00195777 alpha`, so the dominant remaining gap is continuum timing-grid bias, not Monte Carlo sampling. No universal scalar replacement metric and no novelty claim.

---

## Original question
Two hypothetical photodetectors satisfy `D_A^*=D_B^*` but have radically different temporal responses. Does equal conventional specific detectivity imply equal ability to detect arbitrary optical signals?

## Surviving logical chain

### Steps 01–13 — scalar D*, finite records, rough-window obstruction
Equal scalar reference `D*` does not determine arbitrary temporal-signal performance; explicit 1 Hz construction gave `SNR_A/SNR_B~6.36`. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation stationary-Gaussian problem. Finite observation creates task-level timing/search effects. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed directly with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family. Step 13 identifies Brownian-like local roughness. **FAILED NUMERICAL ESTIMATE:** rough-grid crossover `ell~49` invalid.

### Steps 14–23 — genuine information bandwidth; Rice reversal corrected
A genuine finite timing-information bandwidth removes the hard-window cusp. Fixed physical signal/noise produces a shallow finite bandwidth optimum. For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=.90`, `Lambda=.895`, Rice gave switches near `25.49` and `130.19`; Palm preserves only the lower switch `~21.7 +/- .3`. **INVALIDATED:** upper Rice switch. Direct rough-endpoint occupation sampling gives `Lambda_cross^infinity~.905 +/- .004`, leaving `.895` fast-preferred.

### Steps 24–30 — generalized Pickands crossover
Finite bandwidth introduces a two-parameter local-extreme problem. **INVALIDATED INTERMEDIATE:** coupling coefficient `.8131`; correct pointwise coefficient `.8906480701 sqrt(chi/zeta)`. Bessel extremum zoom-in and Brownian-parabola scaling give `mu=sqrt(2) zeta chi^(1/3)` and the model-reduced canonical crossover `F(mu)`. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-chi values were grid biased; continuum-extrapolated values agree with the canonical reduction.

### Steps 31–34 — direct finite-u high-band closure
Step 31's empirical Palm bridge is superseded for the original high-band conclusion. Step 32 directly certifies fast feasible / slow infeasible through `kappa_f~170`, then raw crossing moments fail from micro-upcrossing multiplicity. Step 33 replaces crossings with finite-amplitude excursion clusters `C_Delta` and exact occupation-Palm first/second-moment identities. Step 34 uses `q=kappa_f^-1/2` plus paired endpoint coupling to give a numerical high-band closure: fast `<alpha`, slow `>alpha` over `170<=kappa_f<=infinity`; its original `0.0006 alpha` inter-node allowance was empirical.

### Steps 35–36 — q regularity and tail-sensitive strips
The common-noise field is `L2`-regular/Lipschitz in `q`; generic Gaussian supremum anti-concentration is far too coarse at `alpha=1e-6`. Step 36 defines an exact fixed-cluster maximum measure giving a rare-event-scaled threshold-strip envelope; fast local strip intensity near `u~4.959` is numerically `~5 alpha` per threshold unit.

### Steps 37–38 — overshoot scale and Pickands elasticity
Fixed-class Pickands theory gives high-threshold exponential overshoot and hazard scale `h_a~uN_a`. Step 38 proves exact cross-elasticity ordering `H(chi,lambda zeta)<=H(lambda chi,zeta)` and matched tangent hazard `h_tan/N_tan<=phi/Q-1/u`. **REFINEMENT:** the finite-u strip excess is remainder physics, not positive smoothing elasticity.

### Step 39 — finite-u remainder factor
Factorize `R=N_a/N_tan`. At the fast witness `R~1.56`, so a small-amplitude second-order Pickands remainder is false at `u~5`; numerical logarithmic threshold slope is much smaller. **REJECTED SHORTCUT:** proving `R~1` is the wrong target.

### Step 40 — Cameron-Martin covariance barrier
Cameron-Martin likelihood rearrangement plus a positive covariance-kernel RKHS barrier gives direct exact-event threshold translation. Numerical midpoint covariance floor `~.92524` makes `1e-4` threshold motion harmless at the fast endpoint. **PARTIAL CERTIFICATE.** Numerical covariance constants are not formal interval arithmetic.

### Step 41 — analytic inter-node interpolation
The common-noise difference process is analytically controlled between sampled `q` nodes. Near `q=0` use a deterministic net plus Brownian-type modulus/Borell bound; for `q,r>0` use an exact Rice upcrossing sup-tail envelope. **INVALIDATED NUMERICAL VALUE:** Step-35 tiny-q `0->.005` RMS `~5.4e-5` was cancellation damaged; endpoint asymptotics give `~2.69e-5`. Conditional on node/grid numerics, `p_f(q)<alpha` for every `0<=q<=.0767`. The old empirical `0.0006 alpha` interpolation allowance is no longer needed.

### Step 42 — raw Palm concentration obstruction
For raw finite-grid contribution `Y=m_aS/L`, the implementation enforces `L>=delta_t/2`, so it is bounded, but the support is huge. At the endpoint `n=50000`, empirical Bernstein gives radius `~.24538 alpha`, dominated by the range term. **NEGATIVE RESULT / REJECTED SHORTCUT:** generic concentration on the raw inverse-duration estimator is useless. Duration truncation gives exactly

```math
P_FA <= E[C_long] + P(C_short>=1).
```

For `L0=.02`, long-cluster support falls by 40x.

### Step 43 — short-cluster Gaussian envelope
A successful cluster shorter than `.02` must traverse the full amplitude gap `.15` between a level-`a` boundary and a point near `u~4.959` within `.02`. A fine time net plus conservative correlation floor `rho_*=.99980` and metric envelope `K_*=2e-4` gives

```math
P(C_short>=1)<3.9e-11<3.9e-5 alpha.
```

The inequality is analytic conditional on the conservative numerical covariance/metric constants.

### Step 44 — dedicated truncated-Palm finite-grid certificate
Use

```text
X=7.16, Lambda=.895, Delta=.15, L0=.02,
kappa_f=infinity, timing grid ~=.001.
```

Four independent batches:

```text
seed       n       mean/alpha      sample SD
20260812   50000   .994615198      9.57248e-7
20260813   50000   .984590252      9.55595e-7
20260814   50000   .995087976      9.65325e-7
20260815   50000   .996170838      9.69148e-7
```

All four observed zero selected successful clusters with `L<.02`; this observation is not used as the short-cluster bound.

Pooled `n=200000`:

```text
mean/alpha              = .992616066144
sample SD               = 9.6184951e-7
variance term/alpha     = .00584190324
range term/alpha        = .00146080182
EB radius/alpha         = .00730270506
short bound/alpha       = .000039
finite-grid upper/alpha = .999957771204
```

Therefore

```math
\boxed{P_FA^{finite-grid,95\%}/alpha < .9999578 < 1.}
```

**RIGOROUS FINITE-GRID STATISTICAL CERTIFICATE:** this is a genuine finite-sample pointwise endpoint confidence bound for the implemented grid, not a Gaussian-SE heuristic.

However the certified margin is only `.00004223 alpha`. The old conservative timing-grid allowance `.002 alpha` is ~47x larger and destroys the certificate if added unchanged:

```text
.999957771 + .002 = 1.001957771.
```

See `TRUNCATED_PALM_ENDPOINT_CERTIFICATE_STEP.md` and `numerics/truncated_palm_endpoint_certificate.py`.

---

## Current frontier
The dominant fast endpoint uncertainty is now continuum timing-grid bias, not Monte Carlo sampling or continuous-q interpolation. The next logical choice is either (a) derive a sharp finite-grid-to-continuum bound for the duration-truncated cluster statistic, replacing the old `.002 alpha` allowance, or (b) shift the common witness time `X` slightly to create a materially larger fast statistical margin before attempting continuum certification. Simultaneous multi-node confidence, slow lower-ratio concentration, and formal interval arithmetic remain later gaps.

### Single next question — DO NOT ANSWER YET
> Can the finite-grid-to-continuum bias of the duration-truncated cluster upper bound be controlled sharply enough to replace the old `0.002 alpha` allowance, or should the common witness time `X` first be shifted slightly to create a larger proof margin?

---

## Scope boundary
Do not claim: faster universally better/worse; a universal scalar replacement for `D*`; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 fast values as continuum data; Step-31 empirical fit exact/required; Step-34 as a fully formal theorem; Step-36 as a uniform hazard theorem; `R~1`; `L_R=.8` analytic; `m_*=.92`, `rho_*=.99980`, or `K_*=2e-4` as formal interval constants; Step-41 node estimates themselves rigorous; raw empirical Bernstein certifies Step-33; `L0=.02` optimal; Step-44 as a continuum certificate; simultaneous 95% coverage across all q nodes; no re-entrant pocket for other task parameters; uniqueness of bandwidth optimum; illustrative GHz scales as hardware recommendation; novelty.
