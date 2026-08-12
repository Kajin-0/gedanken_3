# Progress Log — Experiment 01

**Consolidation note — 2026-08-12 15:25 EDT:** compact chronology preserving consequential results, corrections, invalidations, rejected shortcuts, numerical validations, asymptotic qualifications, and current stopping point. Full derivations remain in dedicated step files.

---

## Steps 01–13
Equal scalar `D*` does not determine arbitrary temporal-signal performance; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`. Full magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation Gaussian problem. Finite records produce a task-level detection-time problem. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family. **FAILED NUMERICAL ESTIMATE:** Step-13 rough-grid crossover `ell~49` invalid; hard-window scan is locally Brownian-like.

## Steps 14–23
A genuine finite information bandwidth removes the cusp. Holding physical signal/noise fixed yields a shallow finite bandwidth optimum. For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=.90`, `Lambda=.895`, Rice produced apparent switches at `25.4898402` and `130.1945883`; Palm preserves only `~21.7 +/-0.3`. **INVALIDATED:** upper Rice switch. Rough-endpoint occupation sampling gives `Lambda_cross^infinity~.905 +/- .004`; `.895` remains fast-preferred.

## Steps 24–30
Finite bandwidth produces a two-parameter generalized Pickands problem. **INVALIDATED INTERMEDIATE:** coupling coefficient `.8131`; correct pointwise coefficient `.8906480701 sqrt(chi/zeta)`. Bessel extremum zoom-in and Brownian-parabola scaling yield `mu=sqrt(2)zeta chi^(1/3)` and canonical fast crossover `F(mu)`. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` values were grid biased.

## Steps 31–34
Step 31 empirical Palm bridge is superseded for the original high-band conclusion. Step 32 directly certifies through `kappa_f~170`, then raw crossing moments fail from micro-upcrossing multiplicity. Step 33 replaces crossings with finite-amplitude excursion clusters and exact occupation-Palm moment identities. Step 34 uses `q=kappa_f^-1/2` plus paired endpoint coupling to give fast `~<.99955 alpha`, slow `~>1.10 alpha` over `170<=kappa_f<=infinity`; its `0.0006 alpha` inter-node allowance was empirical.

## Steps 35–36
The normalized common-noise field is `L2`-regular/Lipschitz in `q`; threshold motion is also small. **NEGATIVE RESULT:** generic Gaussian-supremum anti-concentration is far too coarse at `alpha=1e-6`. Step 36 defines the exact fixed-cluster maximum measure `nu_a`, giving a tail-sensitive threshold-strip envelope; fast local strip intensity is numerically `~5 alpha` per threshold unit.

## Steps 37–38
Fixed-class Pickands theory gives high-threshold exponential overshoot and hazard scale `h_a~uN_a`. Step 38 proves `H(chi,lambda zeta)<=H(lambda chi,zeta)` and `0<=zeta d_zeta logH<=chi d_chi logH`, yielding matched tangent hazard `h_tan/N_tan<=phi/Q-1/u`. **REFINEMENT:** the Step-36 excess is finite-`u` remainder physics, not positive smoothing elasticity.

## Step 39
Factorize `R=N_a/N_tan`. At the fast witness `R~1.56`; a small-amplitude second-order Pickands remainder is false at `u~5`. Numerical `-d_u logR~.07–.68`; `L_R=.8` is only a working envelope. **REJECTED SHORTCUT:** proving `R~1` is the wrong target.

## Step 40
Cameron–Martin likelihood rearrangement plus a positive covariance-kernel RKHS barrier gives direct exact-event threshold translation. With numerical midpoint covariance floor `~.92524` and conservative `.92`, a `1e-4` threshold decrease raises the rough-endpoint fast upper only from `.98968 alpha` to `~.990213 alpha`. **PARTIAL CERTIFICATE.**

## Step 41
Analytic interpolation replaces Step-34's empirical `0.0006 alpha` mesh allowance. Near `q=0`, a deterministic net plus Brownian-type modulus/Borell argument controls the nondifferentiable common-noise difference field; for `q,r>0`, an exact Rice upcrossing envelope controls its sup norm. **INVALIDATED NUMERICAL VALUE:** Step-35's tiny-`q` reported `0->.005` RMS `~5.4e-5` was cancellation damaged; high-frequency asymptotics give `~2.69e-5`. Conditional on existing node/grid numerics, `p_f(q)<alpha` for every `0<=q<=.0767`. **ANALYTIC INTER-NODE ENVELOPE.**

Full derivation: `GAUSSIAN_Q_SUPNORM_INTERPOLATION_STEP.md`.  
Helper: `numerics/q_supnorm_interpolation.py`.

## Step 42 — 15:25 EDT — finite-sample occupation-Palm concentration
The Step-33 finite-grid first-moment contribution is

```math
Y=m_a S/L,
```

and the implementation enforces `L>=delta_t/2`, so exactly on that grid

```math
0<=Y<=B=2m_a/delta_t.
```

At the fast rough endpoint (`X=7.16`, `Lambda=.895`, `Delta=.15`, `delta_t~.001`, `n=50000`):

```text
u ~= 4.95898348
a ~= 4.80898348
Q(a) ~= 7.58499e-7
m_a ~= 6.78856e-7
B ~= 1.35771e-3
mean/alpha = .98968
SE(mean)/alpha = .00429
sample SD ~= 9.59e-7.
```

Maurer-Pontil empirical Bernstein gives a 95% one-sided radius

```text
variance term / alpha ~= .01165
range term / alpha    ~= .23373
total radius / alpha  ~= .24538.
```

**NEGATIVE RESULT / REJECTED SHORTCUT:** simply replacing the Gaussian `1.645 SE` allowance with generic rigorous bounded-variable concentration makes the current node certificate useless. The failure is dominated by the formal short-duration range, not by observed variance. The raw range term alone cannot fit the current endpoint margin until `n~>1.40e6`.

Introduce a deterministic duration threshold `L0` and split successful clusters into long/short. Exactly,

```math
P_FA <= E[C_long] + P(C_short>=1).
```

The long-cluster occupation-Palm weight is bounded by

```math
B0=m_a/L0.
```

For `L0=.02`, `B0~3.3943e-5`, a factor-40 support reduction; at `n=50000`, 95% the empirical-Bernstein range penalty falls to `~.00584 alpha`. The remaining problem is the Gaussian probability of traversing amplitude `Delta=.15` in a successful cluster shorter than `L0`, plus a new truncated-Palm run to obtain its actual sample variance.

Full derivation: `FINITE_SAMPLE_PALM_CONCENTRATION_STEP.md`.  
Helper: `numerics/palm_empirical_bernstein.py`.

---

## Current stopping point

Continuous-`q` interpolation is analytically controlled, but raw finite-grid occupation-Palm weights are too heavy in formal range for generic finite-sample concentration. The next step is to isolate very short successful clusters analytically, allowing rigorous concentration on a duration-truncated long-cluster estimator.

### Single natural next question

> Can a successful amplitude-`Delta=.15` cluster shorter than a chosen `L0` be bounded directly by the Gaussian short-time increment/modulus structure tightly enough that the duration-truncated empirical-Bernstein estimator yields a rigorous endpoint node certificate?
