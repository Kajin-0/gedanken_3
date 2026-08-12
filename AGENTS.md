# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Forty-three logical steps completed. Step 43 resolves the short-cluster probability introduced by the Step-42 duration truncation. A successful cluster shorter than `L0=.02` must traverse the full amplitude gap `Delta=.15` between a level-`a` boundary and a level-`u~4.959` point within lag `<.02`. A fine time net plus conservative high-band correlation floor `rho_*=.99980` and local increment metric `K_*=2e-4` reduces the event to highly discordant Gaussian pairs and gives `P(C_short>=1)<3.9e-11`, or `<3.9e-5 alpha` at `alpha=1e-6`; the net-modulus failure is below `10^-654`. Thus the huge raw inverse-duration support is an importance-weight support pathology, not a meaningful false-alarm contribution for `L0=.02`. The active frontier is a dedicated bounded long-cluster Palm run and rigorous empirical-Bernstein concentration. `rho_*` and `K_*` remain deterministic floating-point envelopes, not formal interval constants. No universal scalar replacement metric and no novelty claim.

Read first:
1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. latest step: `experiments/01-equal-dstar-different-speed/SHORT_CLUSTER_OSCILLATION_BOUND_STEP.md`
4. latest helper: `experiments/01-equal-dstar-different-speed/numerics/short_cluster_oscillation_bound.py`
5. preceding step: `experiments/01-equal-dstar-different-speed/FINITE_SAMPLE_PALM_CONCENTRATION_STEP.md`

Live `main` overrides chat summaries or stale notes.

---

## Mandatory repository protocol
Before material writes: fetch live target; fetch exact blob SHA before replacement; never overwrite stale state; preserve corrections/failed branches; update `CURRENT_STATE.md` and `PROGRESS_LOG.md` when frontier changes.

Useful epistemic labels include: **DEFINED, ASSUMED, DERIVED, CONDITIONAL, CONDITIONAL THEOREM SKETCH, CONDITIONAL CLUSTER EXTENSION, COUNTEREXAMPLE, REFINEMENT, NEGATIVE RESULT, REJECTED SHORTCUT, FAILED NUMERICAL ESTIMATE, NUMERICAL VALIDATION, NUMERICAL COLLAPSE, NUMERICAL ASYMPTOTIC, NUMERICAL CLOSURE, PARTIAL CERTIFICATE, NUMERICAL ENDPOINT CERTIFICATE, PAIRED NUMERICAL INTERVAL CLOSURE, TAIL-SENSITIVE ENVELOPE, EXACT VARIOGRAM ORDERING, ANALYTIC INTER-NODE ENVELOPE, RIGOROUS FINITE-GRID CONCENTRATION TEST, SHORT-CLUSTER GAUSSIAN ENVELOPE, INVALIDATED, INVALIDATED INTERMEDIATE, INVALIDATED NUMERICAL VALUE, INVALIDATED NUMERICAL INTERPRETATION, ASYMPTOTIC, OPEN, NON-CLAIM.**

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

### Step 42
For the implemented Step-33 first-moment Palm contribution `Y=m_aS/L`, `L>=delta_t/2` implies exact finite-grid support `B=2m_a/delta_t`. At the fast rough endpoint, Maurer-Pontil empirical Bernstein at 95% gives radius `~.24538 alpha`, dominated by the range term. **NEGATIVE RESULT / REJECTED SHORTCUT:** generic bounded-variable concentration on the raw inverse-duration estimator is too weak. Duration truncation gives exactly `P_FA<=E[C_long]+P(C_short>=1)`. At `L0=.02`, the long-cluster support falls 40x and the 50k-path range penalty becomes `~.00584 alpha`.

### Step 43 — current frontier
A successful cluster shorter than `L0<ell` has an interior component boundary at `z=a` and a point exceeding `u` within lag `<L0`. On a `h=1e-5` net with `gamma=.0025`, it creates a Gaussian pair satisfying `X>=4.95648348`, `Y<=4.81148348`, lag `<=.02002`.

The rough endpoint covariance is `R_0(.02002)~.9998009903`; finite-band deterministic checks are slightly larger. Retain `rho_*=.99980`. Conditional Gaussian regression gives pair probability `<1.075e-19`; at most `358451505` ordered candidate pairs gives `<3.86e-11`. A local metric envelope `K_*=2e-4` makes the net-modulus failure `<10^-654`. Hence

```math
\boxed{P(C_short>=1)<3.9e-11<3.9e-5 alpha.}
```

**SHORT-CLUSTER GAUSSIAN ENVELOPE / PARTIAL CERTIFICATE:** the short-duration term is negligible at the task false-alarm scale. The analytic probability bound is conditional on conservative numerical `rho_*` and `K_*` rather than formal interval constants.

---

## Current frontier

Run/store the `L0=.02` long-cluster occupation-Palm contributions and apply a genuine empirical-Bernstein upper confidence bound. The short-cluster probability no longer needs Monte Carlo. Later gaps: simultaneous confidence allocation, slow lower-ratio concentration, continuum timing-grid bias, formal interval arithmetic.

### Single next question — DO NOT ANSWER UNTIL PROMPTED

> With `P(C_short>=1)` negligible, does a dedicated `L0=.02` truncated occupation-Palm run give a rigorous empirical-Bernstein upper confidence bound on `E[C_long]` below the remaining fast endpoint budget?

---

## Scope boundary
Do not claim: faster universally better/worse; universal scalar replacement for `D*`; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 fast values as continuum data; Step-31 empirical fit exact/required for original high-band conclusion; Step-34 as fully formal theorem; Step-36 as uniform hazard theorem; `R~1`; `L_R=.8` analytic; `m_*=.92`, `rho_*=.99980`, or `K_*=2e-4` as formal interval constants; Step-41 node estimates themselves rigorous; raw empirical Bernstein certifies Step-33; `L0=.02` optimal; no re-entrant pocket for other task parameters; uniqueness of bandwidth optimum; illustrative GHz scales as hardware recommendation; novelty.