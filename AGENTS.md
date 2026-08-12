# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Forty-one logical steps completed. Step 41 replaces Step-34's empirical `0.0006 alpha` inter-node allowance with analytic Gaussian-process interpolation. Near the rough endpoint, a deterministic time net plus Brownian-type modulus comparison controls the nondifferentiable common-noise difference field. For every strictly positive finite-`q` pair, the difference field is differentiable and an exact Rice upcrossing envelope controls its sup norm. These bounds feed directly into the Step-40 Cameron–Martin threshold translation. Conditional on the existing numerical node/grid envelopes and conservative spectral constants, `p_f(q)<alpha` for every `0<=q<=.0767` (`170<=kappa_f<=infinity`). Step 41 also corrects one Step-35 numerical value: the reported `q=0 -> .005` pair RMS `~5.4e-5` was a cancellation-damaged tiny-`q` quadrature result; the endpoint chord asymptotic gives `~2.69e-5`. The Step-35 `L2` regularity result survives. The active frontier is now rigorous finite-sample concentration for the weighted occupation-Palm node estimators and formal grid/spectral certification, not continuous-`q` interpolation. No universal scalar replacement metric and no novelty claim.

Read first:
1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. latest step: `experiments/01-equal-dstar-different-speed/GAUSSIAN_Q_SUPNORM_INTERPOLATION_STEP.md`
4. latest helper: `experiments/01-equal-dstar-different-speed/numerics/q_supnorm_interpolation.py`
5. preceding step: `experiments/01-equal-dstar-different-speed/CAMERON_MARTIN_BARRIER_STEP.md`

Live `main` overrides chat summaries or stale notes.

---

## Mandatory repository protocol
Before material writes: fetch live target; fetch exact blob SHA before replacement; never overwrite stale state; preserve corrections/failed branches; update `CURRENT_STATE.md` and `PROGRESS_LOG.md` when frontier changes.

Useful epistemic labels include: **DEFINED, ASSUMED, DERIVED, CONDITIONAL, CONDITIONAL THEOREM SKETCH, CONDITIONAL CLUSTER EXTENSION, COUNTEREXAMPLE, REFINEMENT, NEGATIVE RESULT, REJECTED SHORTCUT, FAILED NUMERICAL ESTIMATE, NUMERICAL VALIDATION, NUMERICAL COLLAPSE, NUMERICAL ASYMPTOTIC, NUMERICAL CLOSURE, PARTIAL CERTIFICATE, NUMERICAL ENDPOINT CERTIFICATE, PAIRED NUMERICAL INTERVAL CLOSURE, TAIL-SENSITIVE ENVELOPE, EXACT VARIOGRAM ORDERING, ANALYTIC INTER-NODE ENVELOPE, INVALIDATED, INVALIDATED INTERMEDIATE, INVALIDATED NUMERICAL VALUE, INVALIDATED NUMERICAL INTERPRETATION, ASYMPTOTIC, OPEN, NON-CLAIM.**

Do not use `novel`, `universal`, `fundamental`, `first`, etc. without a separate prior-art audit. `Universal` is allowed only for the explicitly model-reduced canonical crossover function.

---

## Compact surviving chain

### Steps 01–13
Equal scalar `D*` does not determine arbitrary temporal-signal performance. Full magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation Gaussian problem. Finite records create a task-level timing-search problem. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family. **FAILED NUMERICAL ESTIMATE:** Step-13 `ell~49` invalid; hard-window scan is locally Brownian-like.

### Steps 14–23
A genuine information bandwidth removes the cusp. With fixed physical signal/noise, a shallow finite bandwidth optimum exists. For `r=2`, `Lambda=.895`, Rice's upper switch at `130.1945883` is **INVALIDATED**; Palm preserves only the lower switch `~21.7 +/-0.3`. Rough endpoint `Lambda_cross^infinity~.905 +/- .004`, so `.895` remains fast-preferred.

### Steps 24–30
Finite bandwidth produces a two-parameter generalized Pickands problem. **INVALIDATED INTERMEDIATE:** coupling coefficient `.8131`; correct pointwise RMS coefficient `.8906480701 sqrt(chi/zeta)`. Bessel extremum zoom-in and Brownian-parabola scaling yield `mu=sqrt(2)zeta chi^(1/3)` and canonical fast crossover `F(mu)`. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` values were grid biased.

### Steps 31–34
Step 31 empirical Palm bridge is superseded for the original high-band conclusion. Step 32 gives direct finite-`u` crossing-moment certification through `kappa_f~170`, then raw crossing moments fail from micro-upcrossing multiplicity. Step 33 replaces crossings with finite-amplitude excursion clusters and exact occupation-Palm moment identities. Step 34 uses `q=kappa_f^-1/2` plus paired endpoint coupling to give fast `~<.99955 alpha`, slow `~>1.10 alpha` over `170<=kappa_f<=infinity`; its `0.0006 alpha` inter-node allowance was empirical.

### Steps 35–36
The normalized common-noise field is `L2`-regular/Lipschitz in `q` through `q=0`; threshold motion is also small. **NEGATIVE RESULT:** generic Gaussian-supremum anti-concentration is far too coarse at `alpha=1e-6`. Step 36 defines the exact fixed-cluster maximum measure `nu_a`, giving `P(y1<sup z<=y2)<=nu_a((y1,y2])`. Fast high-band local strip intensity is numerically `~5 alpha` per threshold unit.

### Steps 37–38
Fixed-class Pickands theory gives high-threshold exponential overshoot and hazard scale `h_a~uN_a`. Step 38 proves exact cross-elasticity ordering `H(chi,lambda zeta)<=H(lambda chi,zeta)` and `0<=zeta d_zeta logH<=chi d_chi logH`, giving matched tangent hazard `h_tan/N_tan<=phi/Q-1/u`. At `u~4.959`, tangent coefficient `~4.9452`; symmetric `delta=1e-4` tangent strip `~9.89e-4`. **REFINEMENT:** Step-36 excess is finite-`u` remainder physics, not positive smoothing elasticity.

### Step 39
Factorize `R=N_a/N_tan`. At the fast witness `R~1.56`, so a small-amplitude second-order remainder is false at `u~5`. Numerical `-d_u logR` is only `~0.07–0.68`; `L_R=.8` is only a working envelope. **REJECTED SHORTCUT:** proving `R~1` is the wrong target.

### Step 40
Cameron–Martin likelihood rearrangement plus a positive covariance-kernel RKHS barrier gives direct exact-event threshold translation. With numerical midpoint covariance floor `m_q~.92524` and conservative `.92`, a `1e-4` threshold decrease raises the rough-endpoint fast upper only from `.98968 alpha` to `~.990213 alpha`. **PARTIAL CERTIFICATE:** finite-threshold buffering is controlled without tangent/remainder modeling.

### Step 41 — current frontier
For the common-noise difference field

```math
d_{q,r}=z_q-z_r,
```

high-frequency mass asymptotics give

```math
I(q)=I(0)-2sqrt(pi)c_X^2q^2+o(q^2)
```

and

```math
\boxed{
sigma_{0,r}^2=(sqrt(2)-1)L_0^2r^2+o(r^2),
}
```

with `L_0~.00835839`. Therefore the true leading `0 -> .005` chord RMS is `~2.69e-5` and `0 -> .0025` is `~1.34e-5`.

**INVALIDATED NUMERICAL VALUE:** Step-35 helper's `~5.4e-5` tiny-`q` `exact pairwise` value came from ill-conditioned subtraction/cancellation in quadrature. The Step-35 exact formula and `L2` regularity result survive.

For `0<=q<=.0035`, endpoint metric domination plus a fine deterministic time net, Sudakov–Fernique Brownian modulus comparison, and Borell concentration yield a rough difference-field sup bound. With Step-40 translation the fast upper satisfies `p/alpha<=.999970`.

For `q,r>0`, the difference process is differentiable. With `sigma^2=Var d(0)` and `lambda_d=sqrt(Var d'(0))/sigma`, the exact two-sided Rice envelope is

```math
\boxed{
P(||d||_infinity>epsilon)
<=2Q(v)+ell lambda_d/pi e^{-v^2/2},
\qquad v=epsilon/sigma.
}
```

Conservative half-cell spectral envelopes plus Step-34 node envelopes and Step-40 translation remain below `alpha` on every cell; the tightest rounded row is near `q=.055`, `p/alpha~.999997`.

**ANALYTIC INTER-NODE ENVELOPE / PARTIAL CERTIFICATE:** the empirical Step-34 `0.0006 alpha` interpolation allowance is no longer required. Conditional on the numerical node/grid envelopes,

```math
p_f(q)<alpha\quad\forall\ 0<=q<=.0767.
```

---

## Current frontier

Replace Gaussian Monte Carlo standard-error allowances for the weighted occupation-Palm node estimators with rigorous finite-sample concentration/confidence bounds. If a formal theorem-level certificate is desired, also intervalize the remaining spectral and continuum-grid constants.

### Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can the weighted occupation-Palm node estimators be given rigorous finite-sample concentration bounds strong enough to preserve the fast/slow separation, replacing the Gaussian standard-error allowances used in Steps 33–34?

---

## Scope boundary
Do not claim: faster universally better/worse; universal scalar replacement for `D*`; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 fast values as continuum data; Step-31 empirical fit exact/required for original high-band conclusion; Step-33/34 node Monte Carlo estimates are formal interval arithmetic; Step-36 uniform hazard theorem; Step-38 tangent hazard as exact finite-`u` physical-cluster bound; `R~1`; `L_R=.8` analytic; `m_*=.92` formal interval arithmetic; Step-41 makes node/grid statistics theorem-level; no re-entrant pocket for other task parameters; uniqueness of bandwidth optimum; illustrative GHz scales as hardware recommendations; novelty.