# Progress Log — Experiment 01

**Consolidation note — 2026-08-12 17:02 EDT:** compact chronology preserving consequential results, corrections, invalidations, rejected shortcuts, numerical validations, asymptotic qualifications, and current stopping point. Full derivations remain in dedicated step files.

---

## Steps 01–13
Equal scalar `D*` does not determine arbitrary temporal-signal performance; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`. Full magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation Gaussian problem. Finite records produce a task-level detection-time problem. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum. **FAILED NUMERICAL ESTIMATE:** Step-13 rough-grid crossover `ell~49` invalid; hard-window scan is locally Brownian-like.

## Steps 14–23
A genuine finite information bandwidth removes the cusp. Holding physical signal/noise fixed yields a shallow finite bandwidth optimum. For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=.90`, `Lambda=.895`, Rice produced apparent switches at `25.4898402` and `130.1945883`; Palm preserves only `~21.7 +/-0.3`. **INVALIDATED:** upper Rice switch. Rough-endpoint occupation sampling gives `Lambda_cross^infinity~.905 +/- .004`; `.895` remains fast-preferred.

## Steps 24–30
Finite bandwidth produces a two-parameter generalized Pickands problem. **INVALIDATED INTERMEDIATE:** coupling coefficient `.8131`; correct pointwise coefficient `.8906480701 sqrt(chi/zeta)`. Bessel extremum zoom-in and Brownian-parabola scaling yield `mu=sqrt(2)zeta chi^(1/3)` and canonical fast crossover `F(mu)`. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` values were grid biased.

## Steps 31–34
Step 31 empirical Palm bridge is superseded for the original high-band conclusion. Step 32 directly certifies through `kappa_f~170`, then raw crossing moments fail from micro-upcrossing multiplicity. Step 33 replaces crossings with finite-amplitude excursion clusters and exact occupation-Palm moment identities. Step 34 uses `q=kappa_f^-1/2` plus paired endpoint coupling to give fast `~<.99955 alpha`, slow `~>1.10 alpha` over `170<=kappa_f<=infinity`; its `0.0006 alpha` inter-node allowance was empirical.

## Steps 35–36
The normalized common-noise field is `L2`-regular/Lipschitz in `q`; threshold motion is small. **NEGATIVE RESULT:** generic Gaussian-supremum anti-concentration is far too coarse at `alpha=1e-6`. Step 36 defines an exact fixed-cluster maximum measure giving a tail-sensitive threshold-strip envelope; fast local strip intensity is numerically `~5 alpha` per threshold unit.

## Steps 37–38
Fixed-class Pickands theory gives high-threshold exponential overshoot and hazard scale `h_a~uN_a`. Step 38 proves exact generalized-Pickands cross-elasticity ordering and matched tangent hazard `h_tan/N_tan<=phi/Q-1/u`. **REFINEMENT:** the Step-36 excess is finite-`u` remainder physics, not positive smoothing elasticity.

## Step 39
Factorize `R=N_a/N_tan`. At the fast witness `R~1.56`; a small-amplitude second-order Pickands remainder is false at `u~5`. Numerical `-d_u logR~.07–.68`; `L_R=.8` is only a working envelope. **REJECTED SHORTCUT:** proving `R~1` is the wrong target.

## Step 40
Cameron–Martin likelihood rearrangement plus a positive covariance-kernel RKHS barrier gives direct exact-event threshold translation. With numerical midpoint covariance floor `~.92524` and conservative `.92`, a `1e-4` threshold decrease raises the rough-endpoint fast upper only from `.98968 alpha` to `~.990213 alpha`. **PARTIAL CERTIFICATE.**

## Step 41
Analytic interpolation replaces Step-34's empirical `0.0006 alpha` mesh allowance. Near `q=0`, a deterministic net plus Brownian-type modulus/Borell argument controls the nondifferentiable difference field; for `q,r>0`, an exact Rice upcrossing envelope controls its sup norm. **INVALIDATED NUMERICAL VALUE:** Step-35's tiny-`q` reported `0->.005` RMS `~5.4e-5` was cancellation damaged; asymptotics give `~2.69e-5`. Conditional on existing node/grid numerics, `p_f(q)<alpha` for every `0<=q<=.0767`. **ANALYTIC INTER-NODE ENVELOPE.**

## Step 42
For the finite-grid Palm contribution `Y=m_aS/L`, `L>=delta_t/2` gives exact support `B=2m_a/delta_t`. At the fast rough endpoint (`n=50000`), Maurer-Pontil empirical Bernstein gives 95% radius `~.24538 alpha`, dominated by the range term `~.23373 alpha`. **NEGATIVE RESULT / REJECTED SHORTCUT:** generic concentration on the raw inverse-duration estimator is far too weak. Duration truncation gives exactly

```math
P_FA<=E[C_long]+P(C_short>=1),
```

with long-cluster support `B0=m_a/L0`. At `L0=.02`, support falls 40x and the 50k-path range penalty becomes `~.00584 alpha`.

Full derivation: `FINITE_SAMPLE_PALM_CONCENTRATION_STEP.md`.  
Helper: `numerics/palm_empirical_bernstein.py`.

## Step 43 — 17:02 EDT — short-cluster high-level Gaussian bound
If a successful lower-level component has duration `<L0<ell`, at least one component boundary lies inside the search interval and has value exactly `a=u-Delta`, while some point inside exceeds `u`. Therefore the event forces a full amplitude-`Delta` change over lag `<L0` while at the rare high level.

For the established fast family:

```text
u ~= 4.95898348
a ~= 4.80898348
Delta=.15
L0=.02
ell=.895
h=1e-5
gamma=.0025.
```

On the good time-net event, any short successful cluster yields an ordered net pair with

```text
X>=U=4.95648348
Y<=A=4.81148348
lag<=.02002.
```

The exact rough covariance gives `R_0(.02002)~.9998009903`; deterministic finite-band checks are slightly larger. Retain conservative numerical `rho_*=.99980`. Gaussian regression gives

```math
P(X>=U,Y<=A)
<=Q(U)Phi((A-rho_*U)/sqrt(1-rho_*^2))
<1.075e-19.
```

At most `358451505` ordered candidate pairs gives pair-union `<3.86e-11`. The local metric envelope `K_*=2e-4` with the same net gives `log10 P(net-modulus failure)<-654`. Therefore

```math
\boxed{P(C_short>=1)<3.9e-11<3.9e-5 alpha.}
```

**SHORT-CLUSTER GAUSSIAN ENVELOPE / PARTIAL CERTIFICATE:** the short-duration term is negligible relative to `alpha`. The probability inequality is analytic conditional on conservative deterministic floating-point constants `rho_*` and `K_*`; these are not formal interval arithmetic.

**REFINEMENT:** the enormous raw support from tiny `L` is an importance-weight support pathology, not a meaningful false-alarm contribution at `L0=.02`.

Full derivation: `SHORT_CLUSTER_OSCILLATION_BOUND_STEP.md`.  
Helper: `numerics/short_cluster_oscillation_bound.py`.

---

## Current stopping point

The short-cluster penalty introduced by duration truncation is analytically negligible. The next step is a dedicated `L0=.02` long-cluster occupation-Palm run that stores the bounded per-path contributions and applies a genuine finite-sample empirical-Bernstein upper confidence bound. Later gaps: simultaneous confidence allocation, slow lower-ratio concentration, continuum timing-grid bias, interval arithmetic.

### Single natural next question

> With `P(C_short>=1)` negligible, does a dedicated `L0=.02` truncated occupation-Palm run give a rigorous empirical-Bernstein upper confidence bound on `E[C_long]` below the remaining fast endpoint budget?
