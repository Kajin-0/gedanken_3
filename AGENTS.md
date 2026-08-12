# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Forty logical steps completed. Step 40 bypasses the Step-39 finite-`u` remainder factor for threshold continuity. Cameron–Martin likelihood rearrangement gives a sharp Gaussian-probit translation bound for arbitrary path events. A positive covariance-kernel RKHS barrier `h_delta(t)=delta R_q(t-ell/2)/m_q`, with `m_q=inf R_q(t-ell/2)`, raises the entire timing path by at least `delta` and has exact Cameron–Martin norm `delta/m_q`. Thus the exact false-alarm event obeys `p_q(u-delta)<=Phi(Phi^-1(p_q(u))+delta/m_q)` and the corresponding lower bound at `u+delta`. Deterministic high-band covariance quadrature gives `m_q~0.92524`; using conservative numerical floor `.92`, `delta=1e-4` raises the Step-33 fast rough-endpoint upper from `.98968 alpha` only to `.990213 alpha<alpha`. The finite-threshold anti-concentration/remainder issue is therefore no longer the main theorem obstacle. The active frontier is a sharp sup-norm tail for the common-white-noise difference process between neighboring `q` values. No universal scalar replacement metric and no novelty claim.

Read first:
1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. latest step: `experiments/01-equal-dstar-different-speed/CAMERON_MARTIN_BARRIER_STEP.md`
4. latest helper: `experiments/01-equal-dstar-different-speed/numerics/cameron_martin_barrier.py`
5. preceding step: `experiments/01-equal-dstar-different-speed/FINITE_U_REMAINDER_FACTOR_STEP.md`

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

### Step 39
Factorize `R=N_a/N_tan`. At the fast witness `R~1.56`, so a small-amplitude second-order remainder is false at `u~5`. The numerical logarithmic threshold slope is much smaller (`~0.07–0.68`); `L_R=.8` is only a working numerical envelope. **REJECTED SHORTCUT:** proving `R~1` is the wrong target.

### Step 40 — current frontier
For any Gaussian path event `A` of probability `p` and Cameron–Martin vector `h`, `r=||h||_H`, Cameron–Martin likelihood rearrangement gives

```math
Phi(Phi^-1(p)-r)<=mu(A+h)<=Phi(Phi^-1(p)+r).
```

For `A_u={sup z>u}`, any RKHS barrier `h_delta>=delta` yields

```math
p(u-delta)<=Phi(Phi^-1(p(u))+||h_delta||_H),
```

```math
p(u+delta)>=Phi(Phi^-1(p(u))-||h_delta||_H).
```

Choose the covariance representer at the search midpoint. With

```math
m_q=inf_{t in [0,ell]}R_q(t-ell/2),
```

```math
h_delta(t)=delta R_q(t-ell/2)/m_q
```

has exact RKHS norm `delta/m_q` and stays above `delta`. Therefore

```math
p_q(u-delta)-p_q(u+delta)
<=Phi(z+delta/m_q)-Phi(z-delta/m_q).
```

The covariance floor is positive for every high-band `q`; deterministic quadrature gives `m_q~.92524` over `170<=kappa_f<=infinity`. Conservative working floor `.92` gives

```math
p_f(u-10^-4)<=.990213 alpha<alpha
```

from the Step-33 rough-endpoint fast upper `.98968 alpha`.

**PARTIAL CERTIFICATE:** exact finite-threshold buffering is now controlled directly at the false-alarm event level without `R` or tangent/Pickands remainder modeling. **QUALIFICATION:** `.92` is a numerical floor, not formal interval arithmetic.

---

## Current frontier

Bound the common-white-noise difference process

```math
d_{q,r}(t)=z_q(t)-z_r(t)
```

in sup norm over neighboring `q` values. The remaining quantity from Step 35 is

```math
eta=P(||d_{q,r}||_infinity>epsilon).
```

A theorem-level continuous-parameter closure needs `eta` small enough to fit inside the remaining fast false-alarm margin.

### Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can `d_{q,r}` be given a sharp Borell–TIS / metric-entropy sup-norm tail bound at `|q-r|<=0.005`, small enough that `eta` fits inside the remaining `~1e-8` fast false-alarm margin?

---

## Scope boundary
Do not claim: faster universally better/worse; universal scalar replacement for `D*`; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 fast values as continuum data; Step-31 empirical fit exact/required for original high-band conclusion; Step-34 theorem-level continuous-parameter closure; Step-36 uniform hazard theorem; Step-38 tangent hazard as exact finite-`u` physical cluster bound; `R~1`; `L_R=.8` analytic; `m_*=.92` formal interval arithmetic; Step-40 alone closes continuous `q`; no re-entrant pocket for other task parameters; uniqueness of bandwidth optimum; illustrative GHz scales as hardware recommendation; novelty.