# Progress Log — Experiment 01

**Consolidation note — 2026-08-12 06:14 EDT:** compact chronology preserving consequential results, corrections, invalidations, rejected shortcuts, numerical validations, asymptotic qualifications, and current stopping point. Full derivations remain in dedicated step files.

---

## Steps 01–13
Equal scalar `D*` does not determine arbitrary temporal-signal performance; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`. Full magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation Gaussian problem. Finite records produce a task-level detection-time problem. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family. **FAILED NUMERICAL ESTIMATE:** Step-13 rough-grid crossover `ell~49` invalid; the hard-window scan is locally Brownian-like.

## Steps 14–23
A genuine finite information bandwidth removes the cusp. Holding physical signal/noise fixed yields a shallow finite bandwidth optimum. For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=.90`, `Lambda=.895`, Rice produced switches at `25.4898402` and `130.1945883`; Palm preserves only `~21.7 +/-0.3`. **INVALIDATED:** upper Rice switch. Rough-endpoint occupation sampling gives `Lambda_cross^infinity~0.905 +/-0.004`; `Lambda=.895` remains fast-preferred.

## Steps 24–30
Finite bandwidth introduces the two-parameter generalized Pickands problem. **INVALIDATED INTERMEDIATE:** coupling coefficient `0.8131`; correct pointwise RMS coefficient is `0.8906480701 sqrt(chi/zeta)`. Bessel extremum zoom-in and Brownian-parabola scaling give `mu=sqrt(2) zeta chi^(1/3)` and the canonical fast crossover `F(mu)=(2/sqrt(pi))E[M_inf-M_mu]`. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` values were grid biased; continuum-extrapolated full-field values agree with the canonical reduction.

## Step 31
Palm-anchored canonical bridge gave a one-hump high-band boundary, but its finite-`u` correction was empirical. Later steps remove dependence on that fit for the original `Lambda=.895` conclusion.

## Step 32
Direct finite-`u` Rice first/second-moment enclosure certifies fast feasible / slow infeasible through at least `kappa_f=170`. **NEGATIVE RESULT:** raw crossing moments fail around `175–200` because one physical slow excursion contains many micro-upcrossings.

## Step 33
Finite-amplitude excursion-cluster count `C_Delta` satisfies `sup z>u iff C_Delta>=1` and gives exact occupation-Palm first/second-moment bounds. Cluster bounds remain sharp at `kappa_f=300`, `1000`, and `infinity`. **NUMERICAL ENDPOINT CERTIFICATE.**

## Step 34
Use `q=kappa_f^-1/2` and common-random-number pairing to the rough endpoint. Dense scan plus measured grid/inter-node allowances gives fast envelope `U_f/alpha~<0.99955` and slow envelope `L_s/alpha~>1.10` over `170<=kappa_f<=infinity`. **PAIRED NUMERICAL INTERVAL CLOSURE.** Inter-node allowance is empirical, not theorem-level.

## Step 35
The normalized common-noise Gaussian field is `L2`-Lipschitz in `q` through the rough endpoint. For fast `Delta q=.005`, pointwise RMS process change is `~<7.5e-5`; threshold motion is `~<2.8e-5`. **REJECTED SHORTCUT:** cluster moments are not pathwise Lipschitz. **NEGATIVE RESULT:** generic Gaussian-supremum anti-concentration is orders too coarse at `alpha=1e-6`.

## Step 36
Fix a lower excursion level `a` and define the cluster-maximum measure `nu_a`. Exact finite-threshold strip envelope:

```math
P(y1<sup z<=y2)<=nu_a((y1,y2]).
```

Fast high-band diagnostics near `u~4.959` give local strip intensity `~5 alpha` per threshold unit over `kappa_f=170,300,1000,infinity`. **TAIL-SENSITIVE ENVELOPE / NUMERICAL VALIDATION.**

## Step 37
Fixed-class Pickands theory plus asymptotic single-successful-cluster separation gives `N_a(u+s/u)/N_a(u)->exp(-s)` and hence rare-event hazard scale `h_a~uN_a`. **REFINEMENT:** fixed-class asymptotics are nonuniform through `q->0` at physical `u~4.96`.

## Step 38
Exact smoothing inequality `0<=zeta d_zeta F_zeta<=F_zeta` implies `H(chi,lambda zeta)<=H(lambda chi,zeta)` and therefore `0<=zeta d_zeta log H<=chi d_chi log H`. Along fixed physical `kappa`, `H` is nondecreasing with threshold, giving

```math
h_tan/N_tan<=phi/Q-1/u.
```

At `u~4.959`, bound `~4.9452`; symmetric tangent-strip factor at `delta=1e-4` is `~9.89e-4`. **REFINEMENT / NEGATIVE RESULT:** Step-36 exact strip excess is finite-`u` remainder physics, not positive `zeta` elasticity.

## Step 39 — 06:14 EDT — finite-`u` remainder factor
Define

```math
R(u,q)=N_a(u,q)/N_tan(u,q).
```

Using the Step-30 canonical fast tangent model and Step-33/34 exact-cluster first moments:

```text
kappa_f      N_tan/alpha      N_a/alpha      R
170             .6294           .9878       1.570
300             .6297           .9862       1.566
1000            .6306           .9842       1.561
infinity        .6319           .9897       1.566
```

**REFINEMENT:** the prior `~5–10% excess` refers to the local hazard/strip coefficient. The first-moment amplitude correction is much larger: `R~1.56`, so a perturbation expansion in `R-1` is inappropriate at `u~5`.

The continuity identity is

```math
-\partial_u log R=h_a/N_a-h_tan/N_tan.
```

Combining Step-36 strip intensities with Step-33/34 `N_a` and deterministic tangent hazards gives inferred slopes `~0.07–0.68` over the tested high-band points. `L_R=.8` is retained only as a conservative **numerical working envelope**, not an analytic bound.

If locally

```math
|log R(v)-log R(u)|<=L_R|v-u|,
```

then the Step-38 tangent ratios imply

```math
\boxed{
[N_a(u-d)-N_a(u+d)]/N_a(u)
<=A_-e^{L_R d}-A_+e^{-L_R d}.
}
```

At `u~4.959`, `d=1e-4`, `L_R=.8`, this is `~1.149e-3`, versus tangent-only `~9.89e-4`; when `N_a~alpha`, absolute scale is `~1.15e-9`. The large amplitude mismatch therefore does not imply poor narrow-threshold continuity.

**REJECTED SHORTCUT:** proving `R~1` is unnecessarily strong and false at the operating threshold. The correct next target is a local finite-ratio/log-Lipschitz theorem for `R`.

Full derivation: `FINITE_U_REMAINDER_FACTOR_STEP.md`.  
Helper: `numerics/finite_u_remainder_factor.py`.

---

## Current stopping point

The finite-`u` correction is nonperturbative in amplitude but modest in threshold slope. The remaining theorem gap is a direct local ratio bound for `R`—or for the exact cluster first moment—over `delta~1e-4`, ideally from Gaussian level shifting/Cameron-Martin comparison.

### Single natural next question

> Can a Gaussian level-shift / Cameron-Martin argument produce a direct finite-ratio bound on `R(u+delta,q)/R(u,q)`—or on the exact cluster first moment itself—over `delta~1e-4`, avoiding any need for a small-amplitude second-order Pickands expansion?
