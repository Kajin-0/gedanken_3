# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Forty-two logical steps completed. Step 42 tests rigorous finite-sample concentration for the weighted occupation-Palm node estimator. On the implemented finite grid, the inverse-duration contribution `Y=m_a S/L` is bounded because `L>=delta_t/2`, but the formal support is enormous relative to the observed variance. At the fast rough endpoint (`n=50000`) Maurer-Pontil empirical Bernstein gives a 95% radius `~.245 alpha`, dominated by the support/range term, so generic bounded-variable concentration does not certify the raw estimator. Step 42 derives the exact duration-truncated decomposition `P_FA<=E[C_long]+P(C_short>=1)`. For `L0=.02`, the long-cluster support is reduced 40x and the empirical-Bernstein range penalty drops from `~.2337 alpha` to `~.00584 alpha`. The active frontier is a Gaussian short-time excursion bound for a successful amplitude-`.15` cluster of duration `<L0`, followed by a new truncated-Palm run and rigorous concentration. No universal scalar replacement metric and no novelty claim.

Read first:
1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. latest step: `experiments/01-equal-dstar-different-speed/FINITE_SAMPLE_PALM_CONCENTRATION_STEP.md`
4. latest helper: `experiments/01-equal-dstar-different-speed/numerics/palm_empirical_bernstein.py`
5. preceding step: `experiments/01-equal-dstar-different-speed/GAUSSIAN_Q_SUPNORM_INTERPOLATION_STEP.md`

Live `main` overrides chat summaries or stale notes.

---

## Mandatory repository protocol
Before material writes: fetch live target; fetch exact blob SHA before replacement; never overwrite stale state; preserve corrections/failed branches; update `CURRENT_STATE.md` and `PROGRESS_LOG.md` when frontier changes.

Useful epistemic labels include: **DEFINED, ASSUMED, DERIVED, CONDITIONAL, CONDITIONAL THEOREM SKETCH, CONDITIONAL CLUSTER EXTENSION, COUNTEREXAMPLE, REFINEMENT, NEGATIVE RESULT, REJECTED SHORTCUT, FAILED NUMERICAL ESTIMATE, NUMERICAL VALIDATION, NUMERICAL COLLAPSE, NUMERICAL ASYMPTOTIC, NUMERICAL CLOSURE, PARTIAL CERTIFICATE, NUMERICAL ENDPOINT CERTIFICATE, PAIRED NUMERICAL INTERVAL CLOSURE, TAIL-SENSITIVE ENVELOPE, EXACT VARIOGRAM ORDERING, ANALYTIC INTER-NODE ENVELOPE, RIGOROUS FINITE-GRID CONCENTRATION TEST, INVALIDATED, INVALIDATED INTERMEDIATE, INVALIDATED NUMERICAL VALUE, INVALIDATED NUMERICAL INTERPRETATION, ASYMPTOTIC, OPEN, NON-CLAIM.**

Do not use `novel`, `universal`, `fundamental`, `first`, etc. without a separate prior-art audit. `Universal` is allowed only for the explicitly model-reduced canonical crossover function.

---

## Compact surviving chain

### Steps 01–13
Equal scalar `D*` does not determine arbitrary temporal-signal performance. Full magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation Gaussian problem. Finite records create a task-level timing-search problem. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum. **FAILED NUMERICAL ESTIMATE:** Step-13 `ell~49` invalid; hard-window scan is locally Brownian-like.

### Steps 14–23
A genuine information bandwidth removes the cusp. Fixed physical signal/noise yields a shallow finite bandwidth optimum. For `r=2`, `Lambda=.895`, Rice's upper switch at `130.1945883` is **INVALIDATED**; Palm preserves only the lower switch `~21.7 +/-0.3`. Rough endpoint `Lambda_cross^infinity~.905 +/- .004`, so `.895` remains fast-preferred.

### Steps 24–30
Finite bandwidth produces a two-parameter generalized Pickands problem. **INVALIDATED INTERMEDIATE:** coupling coefficient `.8131`; correct pointwise coefficient `.8906480701 sqrt(chi/zeta)`. Bessel extremum zoom-in and Brownian-parabola scaling yield `mu=sqrt(2)zeta chi^(1/3)` and canonical fast crossover `F(mu)`. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` values were grid biased.

### Steps 31–34
Step 31 empirical Palm bridge is superseded for the original high-band conclusion. Step 32 directly certifies through `kappa_f~170`, then raw crossing moments fail from micro-upcrossing multiplicity. Step 33 replaces crossings with finite-amplitude excursion clusters and exact occupation-Palm moment identities. Step 34 uses `q=kappa_f^-1/2` plus paired endpoint coupling to obtain fast `~<.99955 alpha`, slow `~>1.10 alpha`; its `0.0006 alpha` interpolation allowance was empirical.

### Steps 35–36
The normalized common-noise field is `L2`-regular/Lipschitz in `q`; generic Gaussian supremum anti-concentration is far too coarse at `alpha=1e-6`. Step 36 defines an exact fixed-cluster maximum measure giving a rare-event-scaled threshold-strip envelope.

### Steps 37–38
Fixed-class Pickands theory gives high-threshold exponential overshoot and hazard scale `h_a~uN_a`. Step 38 proves exact Pickands cross-elasticity ordering and matched tangent hazard `h_tan/N_tan<=phi/Q-1/u`. **REFINEMENT:** the exact finite-`u` strip excess is remainder physics, not positive smoothing elasticity.

### Step 39
Factorize `R=N_a/N_tan`. At the fast witness `R~1.56`, so `R~1` is false at `u~5`; numerical threshold slope is much smaller. **REJECTED SHORTCUT:** small-amplitude second-order Pickands remainder is the wrong theorem target.

### Step 40
Cameron–Martin likelihood rearrangement plus a positive covariance-kernel RKHS barrier gives direct exact-event threshold translation. Numerical midpoint covariance floor `~.92524` makes `1e-4` threshold motion harmless at the fast endpoint. **PARTIAL CERTIFICATE.**

### Step 41
Analytic common-noise interpolation replaces Step-34's empirical `0.0006 alpha` mesh allowance. Near `q=0` use a deterministic net plus Brownian-type modulus/Borell bound; for `q,r>0` use an exact Rice upcrossing sup-tail envelope. **INVALIDATED NUMERICAL VALUE:** Step-35's tiny-`q` `0->.005` RMS `~5.4e-5` was cancellation damaged; asymptotic value is `~2.69e-5`. Conditional on sampled node/grid numerics, `p_f(q)<alpha` for every `0<=q<=.0767`. **ANALYTIC INTER-NODE ENVELOPE.**

### Step 42 — current frontier
For the implemented Step-33 first-moment Palm contribution

```math
Y=m_a S/L,
```

`L>=delta_t/2` implies exact finite-grid support `B=2m_a/delta_t`. At the fast rough endpoint:

```text
B ~= 1.35771e-3
sample SD ~= 9.59e-7
n=50000.
```

Maurer-Pontil empirical Bernstein at 95% gives radius

```text
~.24538 alpha
```

with `~.23373 alpha` coming from the range term alone. **NEGATIVE RESULT / REJECTED SHORTCUT:** generic bounded-variable concentration on the raw inverse-duration estimator is far too weak. The range term alone requires `n~>1.40e6` to fit the current endpoint margin.

Choose duration cutoff `L0` and split successful clusters into long/short. Exactly,

```math
P_FA<=E[C_long]+P(C_short>=1).
```

The long-cluster Palm contribution has support `B0=m_a/L0`. At `L0=.02`, support falls 40x and the 50k-path 95% range penalty becomes `~.00584 alpha`. The short term is a physically structured event: the Gaussian path must traverse amplitude `Delta=.15` in less than `L0`.

---

## Current frontier

Bound `P(C_short>=1)` analytically from the Gaussian short-time increment/modulus structure, preferably uniformly across the high-band family. Then rerun/store the truncated long-cluster Palm contributions and use rigorous empirical-Bernstein confidence bounds. Later gaps: simultaneous confidence allocation, slow lower-ratio concentration, continuum timing-grid bias, interval arithmetic.

### Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can a successful amplitude-`Delta=.15` cluster shorter than a chosen `L0` be bounded directly by the Gaussian short-time increment/modulus structure tightly enough that the duration-truncated empirical-Bernstein estimator yields a rigorous endpoint node certificate?

---

## Scope boundary
Do not claim: faster universally better/worse; universal scalar replacement for `D*`; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 fast values as continuum data; Step-31 empirical fit exact/required for original high-band conclusion; Step-34 as fully formal theorem; Step-36 as uniform hazard theorem; `R~1`; `L_R=.8` analytic; `m_*=.92` formal interval arithmetic; Step-41 node estimates themselves rigorous; raw empirical Bernstein certifies Step-33; `L0=.02` optimal; no re-entrant pocket for other task parameters; uniqueness of bandwidth optimum; illustrative GHz scales as hardware recommendation; novelty.