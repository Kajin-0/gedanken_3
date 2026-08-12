# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-12 15:25 EDT  
**Status:** forty-two logical steps completed. Step 42 tests rigorous finite-sample concentration for the weighted occupation-Palm node estimator left open by Step 41. The finite-grid estimator is bounded because the implementation enforces `L>=delta_t/2`, so Maurer-Pontil empirical Bernstein applies exactly. However, the inverse-duration support is enormous relative to the observed variance: at the fast rough endpoint (`n=50000`, `delta_t~.001`) the formal support is `B~1.3577e-3`, while the sample SD inferred from the quoted SE is only `~9.59e-7`. A 95% one-sided empirical-Bernstein radius is therefore `~0.245 alpha`, dominated by the `B/n` term, and cannot certify the node. This rejects the shortcut of simply replacing Gaussian SE allowances by a generic bounded-variable inequality. Step 42 then derives an exact duration-truncated decomposition `P_FA <= E[C_long] + P(C_short>=1)`. With `L0=.02`, the long-cluster support falls by a factor 40 and the empirical-Bernstein range penalty at `n=50000` drops from `~.2337 alpha` to `~.00584 alpha`. The active frontier is now an analytic Gaussian bound on a successful amplitude-`.15` cluster of duration `<L0`, plus a new truncated-Palm run for rigorous bounded-weight concentration. No universal scalar replacement metric and no novelty claim.

---

## Original question

Two hypothetical photodetectors satisfy `D_A^*=D_B^*` but have radically different temporal responses. Does equal conventional specific detectivity imply equal ability to detect arbitrary optical signals?

---

## Surviving chain

### Steps 01–13 — scalar `D*`, finite records, rough-window obstruction
Equal scalar reference `D*` does not determine arbitrary temporal-signal performance; an explicit 1 Hz construction gave `SNR_A/SNR_B~6.36`. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation stationary-Gaussian problem. Finite records create a task-level timing-search problem. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed directly with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family. Step 13 identifies hard-window Brownian-like local roughness. **FAILED NUMERICAL ESTIMATE:** rough-grid crossover `ell~49` is invalid.

### Steps 14–23 — genuine information bandwidth; Rice reversal corrected
A genuine finite timing-information bandwidth removes the hard-window cusp. Holding physical signal/noise fixed creates a shallow finite bandwidth optimum. For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=.90`, `Lambda=.895`, Rice gave apparent switches at `25.4898402` and `130.1945883`; Palm preserves only the lower switch `~21.7 +/-0.3`. **INVALIDATED:** upper Rice switch. Direct rough-endpoint occupation sampling gives `Lambda_cross^infinity~.905 +/- .004`, leaving `Lambda=.895` fast-preferred.

### Steps 24–30 — two-parameter generalized Pickands crossover
Finite bandwidth introduces `zeta=kappa/(sqrt(2)u sqrt(b))`. **INVALIDATED INTERMEDIATE:** coupling coefficient `.8131`; correct pointwise value `.8906480701 sqrt(chi/zeta)`. Bessel extremum zoom-in and Brownian-parabola scaling introduce `mu=sqrt(2)zeta chi^(1/3)`. The small-`chi` fast channel reduces to the model-reduced canonical function `F(mu)=(2/sqrt(pi))E[M_inf-M_mu]`. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` data were grid biased; continuum-extrapolated full-field values agree with the canonical reduction.

### Steps 31–34 — direct finite-`u` high-band closure
Step 31's Palm-anchored high-band bridge used an empirical finite-`u` correction; later work removes dependence on it for the original conclusion. Step 32 directly certifies fast feasible / slow infeasible through at least `kappa_f=170`, then raw crossing moments fail because one physical excursion contains many micro-upcrossings. Step 33 replaces crossings by finite-amplitude excursion clusters `C_Delta`, with exact occupation-Palm first/second-moment identities and sharp endpoint numerics. Step 34 uses `q=kappa_f^-1/2` and paired endpoint coupling to obtain fast `~<.99955 alpha`, slow `~>1.10 alpha` over `170<=kappa_f<=infinity`; its `0.0006 alpha` inter-node allowance was empirical.

### Steps 35–36 — analytic `q` regularity and tail-sensitive strip measure
The normalized common-noise field is `L2`-regular/Lipschitz in `q` through `q=0`; threshold motion is also small. **REJECTED SHORTCUT:** cluster counts are not pathwise Lipschitz. **NEGATIVE RESULT:** generic Gaussian-supremum anti-concentration is far too coarse at `alpha=1e-6`. Step 36 defines a fixed-cluster maximum measure `nu_a` with exact strip bound `P(y1<sup z<=y2)<=nu_a((y1,y2])`; fast local strip intensity is numerically `~5 alpha` per threshold unit.

### Steps 37–38 — overshoot scale and exact Pickands elasticity ordering
Fixed-class Pickands theory gives high-threshold exponential overshoot and hazard scale `h_a~uN_a`. Step 38 proves `H(chi,lambda zeta)<=H(lambda chi,zeta)` and hence `0<=zeta d_zeta logH<=chi d_chi logH`. Along fixed physical `kappa`, the matched tangent hazard obeys `h_tan/N_tan<=phi/Q-1/u`; at `u~4.959`, coefficient `~4.9452` and symmetric `delta=1e-4` tangent strip `~9.89e-4`. **REFINEMENT:** Step-36 excess is finite-`u` remainder physics, not positive smoothing elasticity.

### Step 39 — finite-`u` remainder factor
Factorize `R=N_a/N_tan`. At the fast witness `R~1.56`, so a small-amplitude second-order Pickands remainder is false at `u~5`. Numerical `-d_u logR~.07–.68`; `L_R=.8` is only a working envelope. **REJECTED SHORTCUT:** proving `R~1` is the wrong target.

### Step 40 — Cameron–Martin covariance barrier
Cameron–Martin likelihood rearrangement plus a positive covariance-kernel RKHS barrier gives direct exact-event threshold translation. With numerical midpoint covariance floor `m_q~.92524` and conservative `.92`, a `1e-4` threshold decrease raises the rough-endpoint fast upper only from `.98968 alpha` to `~.990213 alpha`. **PARTIAL CERTIFICATE:** threshold buffering is controlled without tangent/remainder modeling.

### Step 41 — analytic inter-node Gaussian-process envelope
The common-noise difference process `d_{q,r}=z_q-z_r` is controlled between sampled `q` nodes. **INVALIDATED NUMERICAL VALUE:** Step-35's tiny-`q` reported `0->.005` pair RMS `~5.4e-5` was cancellation damaged; high-frequency asymptotics give `~2.69e-5`. Near `q=0`, a deterministic net plus Brownian-type modulus/Borell argument covers the nondifferentiable endpoint. For `q,r>0`, an exact Rice upcrossing envelope controls `||d||_infinity`. Combined with Step 40, the old empirical `0.0006 alpha` interpolation allowance is no longer needed. **ANALYTIC INTER-NODE ENVELOPE:** conditional on the existing node/grid numerics, `p_f(q)<alpha` for every `0<=q<=.0767`.

### Step 42 — finite-sample concentration obstruction and truncation
For the finite-grid Step-33 first-moment contribution

```math
Y=m_a S/L,
```

the implementation guarantees `L>=delta_t/2`, so

```math
0<=Y<=B=2m_a/delta_t.
```

At the fast rough endpoint:

```text
u ~= 4.95898348
a  ~= 4.80898348
Q(a) ~= 7.58499e-7
m_a  ~= 6.78856e-7
B    ~= 1.35771e-3
n    = 50000
mean/alpha = .98968
SE(mean)/alpha = .00429
sample SD ~= 9.59e-7.
```

Maurer-Pontil empirical Bernstein gives at 95%:

```text
variance term / alpha ~= .01165
range term / alpha    ~= .23373
total radius / alpha  ~= .24538.
```

**NEGATIVE RESULT / REJECTED SHORTCUT:** generic bounded-variable concentration on the raw inverse-duration estimator is much too weak; the formal short-duration range dominates. The range term alone needs `n~>1.40e6` to fit the current endpoint margin.

Choose a duration threshold `L0` and split successful clusters into long/short. Exactly,

```math
P_FA <= E[C_long] + P(C_short>=1).
```

The long-cluster Palm weight is bounded by `B0=m_a/L0`. For `L0=.02`, `B0~3.3943e-5`, a 40x reduction, and the 50k-path 95% range term drops to `~.00584 alpha`. This converts the remaining statistical problem into bounded-weight Monte Carlo plus a Gaussian short-time excursion event.

See `FINITE_SAMPLE_PALM_CONCENTRATION_STEP.md` and `numerics/palm_empirical_bernstein.py`.

---

## Current frontier

Derive a rigorous high-band bound on

```math
P(C_short>=1)
```

for a successful lower-level excursion that traverses amplitude `Delta=.15` in duration `<L0` (candidate `L0~.01–.02`). Then rerun/store the long-cluster Palm contributions and apply a genuine finite-sample empirical-Bernstein confidence bound. Continuum timing-grid bias and formal interval arithmetic remain separate later gaps.

### Single next question — DO NOT ANSWER YET

> Can a successful amplitude-`Delta=.15` cluster shorter than `L0` be bounded directly by the Gaussian short-time increment/modulus structure, tightly enough that the duration-truncated empirical-Bernstein estimator yields a rigorous endpoint node certificate?

---

## Scope boundary

Do not claim: faster universally better/worse; a universal scalar replacement for `D*`; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 fast values as continuum data; Step-31 empirical fit exact/required for the original high-band conclusion; Step-34 as a fully formal theorem; Step-36 as a uniform hazard theorem; `R~1`; `L_R=.8` analytic; `m_*=.92` formal interval arithmetic; Step-41 node estimates themselves rigorous; raw empirical Bernstein certifies Step-33; `L0=.02` is optimal; no re-entrant pocket for other task parameters; uniqueness of bandwidth optimum; illustrative GHz scales as hardware recommendation; novelty.