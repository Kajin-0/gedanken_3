# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Thirty-nine logical steps completed. Step 39 factorizes the exact cluster first moment as `N_a=N_tan R`. At the established fast high-band witness (`X=7.16`, `Lambda=.895`, `u~4.959`), the finite-threshold correction is large in amplitude (`R~1.56`) but numerically modest in logarithmic threshold slope (`-d_u log R~0.07–0.68` across tested points). A working numerical envelope `L_R=.8` raises the Step-38 `delta=1e-4` tangent strip factor from `~9.89e-4` to only `~1.149e-3`. Therefore the active frontier is a direct local finite-ratio/log-Lipschitz theorem for `R` or the exact cluster first moment; proving `R~1` is neither true nor necessary at `u~5`. No universal scalar replacement metric and no novelty claim.

Read first:
1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. latest step: `experiments/01-equal-dstar-different-speed/FINITE_U_REMAINDER_FACTOR_STEP.md`
4. latest helper: `experiments/01-equal-dstar-different-speed/numerics/finite_u_remainder_factor.py`
5. preceding step: `experiments/01-equal-dstar-different-speed/PICKANDS_ELASTICITY_ORDERING_STEP.md`

Live `main` overrides chat summaries or stale notes.

---

## Mandatory repository protocol
Before material writes: fetch live target; fetch exact blob SHA before replacement; never overwrite stale state; preserve corrections/failed branches; update `CURRENT_STATE.md` and `PROGRESS_LOG.md` when frontier changes.

Useful epistemic labels include: **DEFINED, ASSUMED, DERIVED, CONDITIONAL, CONDITIONAL THEOREM SKETCH, CONDITIONAL CLUSTER EXTENSION, COUNTEREXAMPLE, REFINEMENT, NEGATIVE RESULT, REJECTED SHORTCUT, FAILED NUMERICAL ESTIMATE, NUMERICAL VALIDATION, NUMERICAL COLLAPSE, NUMERICAL ASYMPTOTIC, NUMERICAL CLOSURE, PARTIAL CERTIFICATE, NUMERICAL ENDPOINT CERTIFICATE, PAIRED NUMERICAL INTERVAL CLOSURE, TAIL-SENSITIVE ENVELOPE, EXACT VARIOGRAM ORDERING, INVALIDATED, INVALIDATED INTERMEDIATE, INVALIDATED NUMERICAL INTERPRETATION, ASYMPTOTIC, OPEN, NON-CLAIM.**

Do not use `novel`, `universal`, `fundamental`, `first`, etc. without a separate prior-art audit. `Universal` is allowed only for the explicitly model-reduced canonical crossover function.

---

## Compact surviving chain

### Steps 01–13
Equal scalar `D*` does not determine arbitrary temporal-signal performance. Full magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation Gaussian problem. Finite records create a task-level timing-search problem. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum in original scaled family. **FAILED NUMERICAL ESTIMATE:** Step-13 `ell~49` invalid; hard-window scan is locally Brownian-like.

### Steps 14–23
A genuine information bandwidth removes the cusp. With fixed physical signal/noise, a shallow finite bandwidth optimum exists. For `r=2`, `Lambda=.895`, Rice's upper switch at `130.1945883` is **INVALIDATED**; Palm preserves only the lower switch `~21.7 +/-0.3`. Rough endpoint `Lambda_cross^infinity~.905 +/- .004`, so `.895` remains fast-preferred.

### Steps 24–30
Finite bandwidth produces a two-parameter generalized Pickands problem. **INVALIDATED INTERMEDIATE:** coupling coefficient `.8131`; correct pointwise RMS coefficient `.8906480701 sqrt(chi/zeta)`. Bessel extremum zoom-in and Brownian-parabola scaling yield `mu=sqrt(2)zeta chi^(1/3)` and canonical fast crossover `F(mu)`. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` values were grid biased.

### Steps 31–34
Step 31 empirical Palm bridge is superseded for the original high-band conclusion. Step 32 gives direct finite-`u` crossing-moment certification through `kappa_f~170`, then raw crossing moments fail from micro-upcrossing multiplicity. Step 33 replaces crossings with finite-amplitude excursion clusters and exact occupation-Palm moment identities. Step 34 uses `q=kappa_f^-1/2` plus paired coupling to give **PAIRED NUMERICAL INTERVAL CLOSURE** over `170<=kappa_f<=infinity`: fast `~<.99955 alpha`, slow `~>1.10 alpha`; inter-node allowance remains numerical.

### Steps 35–36
The normalized common-noise field is `L2`-Lipschitz in `q` through the rough endpoint. **NEGATIVE RESULT:** generic Gaussian-supremum anti-concentration is far too coarse at `alpha=1e-6`. Step 36 defines the exact fixed-cluster maximum measure `nu_a`, giving `P(y1<sup z<=y2)<=nu_a((y1,y2])`. Fast high-band local strip intensity is numerically `~5 alpha` per threshold unit.

### Steps 37–38
Fixed-class Pickands theory gives high-threshold exponential overshoot and hazard scale `h_a~uN_a`. Step 38 proves exact cross-elasticity ordering `H(chi,lambda zeta)<=H(lambda chi,zeta)` and `0<=zeta d_zeta logH<=chi d_chi logH`, giving matched tangent hazard `h_tan/N_tan<=phi/Q-1/u`. At `u~4.959`, tangent coefficient `~4.9452`; symmetric `delta=1e-4` tangent-strip factor `~9.89e-4`. **REFINEMENT:** Step-36 excess is finite-`u` remainder physics, not positive smoothing elasticity.

### Step 39 — current frontier
Factorize

```math
R(u,q)=N_a(u,q)/N_{tan}(u,q).
```

Representative fast high-band values:

```text
kappa_f      N_tan/alpha      N_a/alpha      R
170             .6294           .9878       1.570
300             .6297           .9862       1.566
1000            .6306           .9842       1.561
infinity        .6319           .9897       1.566
```

**REFINEMENT:** the prior `~5–10%` statement concerns the hazard/strip coefficient. The first-moment amplitude correction is `~56%`; `R~1` is false at `u~5`.

Threshold-continuity identity:

```math
-\partial_u log R=h_a/N_a-h_tan/N_tan.
```

Existing strip diagnostics infer `~0.07–0.68`; `L_R=.8` is only a conservative numerical working envelope. If locally `|logR(v)-logR(u)|<=L_R|v-u|`, then

```math
[N_a(u-d)-N_a(u+d)]/N_a(u)
<=A_-e^{L_R d}-A_+e^{-L_R d}.
```

At `u~4.959`, `d=1e-4`, `L_R=.8`, factor `~1.149e-3`, or `~1.15e-9` absolute for `N_a~alpha`.

**REJECTED SHORTCUT:** a small-amplitude second-order Pickands remainder is the wrong target. The useful theorem is a local finite-ratio/log-Lipschitz bound.

---

## Current frontier

Try a Gaussian level-shift / Cameron-Martin comparison to bound `R(u+delta,q)/R(u,q)` or `N_a(u+delta,q)/N_a(u,q)` directly over `delta~1e-4`.

### Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can a Gaussian level-shift / Cameron-Martin argument produce a direct finite-ratio bound on `R(u+delta,q)/R(u,q)`—or on the exact cluster first moment itself—over `delta~1e-4`, avoiding any need for a small-amplitude second-order Pickands expansion?

---

## Scope boundary
Do not claim: faster universally better/worse; universal scalar replacement for `D*`; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 fast values as continuum data; Step-31 empirical fit exact/required for original high-band conclusion; Step-34 theorem-level continuous-parameter closure; Step-36 uniform hazard theorem; Step-38 tangent hazard as exact finite-`u` physical cluster bound; `R~1`; `L_R=.8` analytic; no re-entrant pocket for other task parameters; uniqueness of bandwidth optimum; illustrative GHz scales as hardware recommendation; novelty.
