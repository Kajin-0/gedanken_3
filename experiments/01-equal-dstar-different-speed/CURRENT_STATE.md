# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-12 06:14 EDT  
**Status:** thirty-nine logical steps completed. Step 39 factorizes the exact physical excursion-cluster first moment as `N_a(u,q)=N_tan(u,q) R(u,q)`. For the established fast high-band witness (`X=7.16`, `Lambda=0.895`, `u~4.959`), the finite-threshold correction is **large in amplitude** (`R~1.56`) but **modest in threshold slope**. Combining Step-36 strip intensities with Step-33/34 first moments and the Step-38 tangent hazard gives an inferred `-d_u log R` roughly `0.07–0.68` across tested high-band points; `L_R~0.8` is retained only as a conservative numerical working envelope. Under a log-Lipschitz remainder assumption, the exact-cluster symmetric strip obeys an explicit ratio bound; at `delta=1e-4`, `L_R=0.8` raises the Step-38 tangent strip factor from `~9.89e-4` to only `~1.149e-3`, i.e. `~1.15e-9` absolute when `N_a~alpha=1e-6`. The next mathematical target is therefore a local finite-ratio/log-Lipschitz theorem for `R`, not a proof that `R` is close to one. No universal scalar replacement metric and no novelty claim.

---

## Surviving chain

### Steps 01–13 — scalar `D*`, finite records, rough-window obstruction
Equal scalar reference `D*` does not determine arbitrary temporal-signal performance; an explicit 1 Hz construction gave `SNR_A/SNR_B~6.36`. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation stationary-Gaussian problem. Finite observation can make phase/placement operationally relevant. Finite-record optimal SNR and task-level detection time were derived. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family. **FAILED NUMERICAL ESTIMATE:** Step-13 rough-grid crossover `ell~49` is invalid; the hard-window scan is locally Brownian-like.

### Steps 14–23 — genuine information bandwidth; Rice reversal corrected
A genuine finite information bandwidth removes the cusp. Holding physical signal/noise fixed produces a shallow finite bandwidth optimum. For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=.90`, `Lambda=.895`, Rice produced apparent switches at `25.4898402` and `130.1945883`; Palm preserves only the lower switch `~21.7 +/-0.3`. **INVALIDATED:** upper Rice switch. Direct rough-endpoint occupation sampling gives `Lambda_cross^infinity~0.905 +/-0.004`, leaving `Lambda=.895` fast-preferred.

### Steps 24–30 — generalized Pickands crossover
Finite bandwidth adds `zeta=kappa/(sqrt(2)u sqrt(b))`; the local problem is two-parameter. **INVALIDATED INTERMEDIATE:** coupling coefficient `0.8131`; correct pointwise RMS coefficient is `0.8906480701 sqrt(chi/zeta)`. Bessel extremum zoom-in and Brownian-parabola scaling introduce `mu=sqrt(2) zeta chi^(1/3)`. The difficult small-`chi` fast channel reduces to the canonical function `F(mu)=(2/sqrt(pi))E[M_inf-M_mu]`. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` values were grid biased; continuum values agree with the canonical reduction.

### Steps 31–34 — direct finite-`u` high-band closure
Step 31 gave an empirical Palm-anchored one-hump boundary, but later steps remove dependence on that fit. Step 32 gives a direct finite-`u` Rice-moment certificate through `kappa_f~170`; raw crossing moments then fail because micro-upcrossing multiplicity diverges inside one physical excursion. Step 33 replaces crossings by finite-amplitude excursion clusters `C_Delta`, with exact occupation-Palm first/second-moment identities and sharp endpoint bounds. Step 34 uses `q=kappa_f^-1/2` plus common-random-number pairing to obtain a **PAIRED NUMERICAL INTERVAL CLOSURE** over `170<=kappa_f<=infinity`: fast upper envelope `~<0.99955 alpha`, slow lower envelope `~>1.10 alpha`. Inter-node allowance remains numerical, not theorem-level.

### Steps 35–36 — analytic `q` continuity and tail-sensitive strip measure
The normalized common-noise field is `L2`-Lipschitz in `q` through the rough endpoint; for `Delta q=.005`, fast pointwise RMS process change is `~<7.5e-5` and threshold motion `~<2.8e-5`. **NEGATIVE RESULT:** generic Gaussian-supremum anti-concentration is orders too coarse at `alpha=1e-6`. Step 36 freezes a lower excursion level and defines a cluster-maximum measure `nu_a`, yielding the exact strip envelope `P(y1<sup z<=y2)<=nu_a((y1,y2])`. Numerical local strip intensity near `u~4.959` is `~5 alpha` per threshold unit across `kappa_f=170,300,1000,infinity`.

### Steps 37–38 — overshoot scale and exact Pickands elasticity ordering
Fixed-class Pickands theory gives the high-threshold overshoot relation `N_a(u+s/u)/N_a(u)->exp(-s)` and therefore the rare-event scale `h_a~uN_a`. Step 38 proves the exact cross-ordering `H(chi,lambda zeta)<=H(lambda chi,zeta)` and hence `0<=zeta d_zeta log H<=chi d_chi log H`. Along fixed physical `kappa`, `H` is nondecreasing with threshold, so the matched tangent hazard satisfies `h_tan/N_tan<=phi/Q-1/u`. At `u~4.959`, this is `~4.9452`; the exact symmetric tangent-strip factor at `delta=1e-4` is `~9.89e-4`. **REFINEMENT:** the Step-36 excess is not caused by positive `zeta` elasticity; it is finite-`u` remainder physics.

### Step 39 — finite-`u` remainder factor
Define

```math
R(u,q)=N_a(u,q)/N_{tan}(u,q).
```

For the fast witness, Step-30 canonical tangent intensities are approximately

```text
kappa_f      N_tan/alpha      N_a/alpha      R
170             .6294           .9878       1.570
300             .6297           .9862       1.566
1000            .6306           .9842       1.561
infinity        .6319           .9897       1.566
```

Thus `R-1~0.56`: a small-amplitude second-order expansion is inappropriate at `u~5`. But

```math
-\partial_u\log R=h_a/N_a-h_tan/N_tan
```

is inferred numerically to be only `~0.07–0.68` over the tested tail. If

```math
|log R(v)-log R(u)|<=L_R|v-u|,
```

then with the Step-38 tangent ratios `A_-,A_+`,

```math
\boxed{
[N_a(u-d)-N_a(u+d)]/N_a(u)
<=A_-e^{L_R d}-A_+e^{-L_R d}.
}
```

At `u~4.959`, `d=1e-4`, numerical working value `L_R=.8` gives `~1.149e-3`, consistent with Step-36 exact strip measurements. **QUALIFICATION:** `L_R=.8` is not an analytic bound or confidence interval.

See `FINITE_U_REMAINDER_FACTOR_STEP.md` and `numerics/finite_u_remainder_factor.py`.

---

## Current frontier

The finite-`u` correction is nonperturbative in amplitude but slowly varying in threshold. The useful theorem is therefore a local finite-ratio/log-Lipschitz bound for `R`, ideally derived directly from Gaussian level shifting or Cameron-Martin comparison.

### Single next question — DO NOT ANSWER YET

> Can a Gaussian level-shift / Cameron-Martin argument produce a direct finite-ratio bound on `R(u+delta,q)/R(u,q)`—or on the exact cluster first moment itself—over `delta~1e-4`, avoiding any need for a small-amplitude second-order Pickands expansion?

---

## Scope boundary

Do not claim: faster is universally better/worse; a universal scalar replacement for `D*`; Step-13 `ell~49`; the Step-20 double reversal; raw Step-27 fast values as continuum data; Step-31 empirical fit is exact or still necessary for the original conclusion; Step-34 is theorem-level continuous-parameter closure; Step-36 proves a uniform hazard density; Step-38 tangent hazard is an exact finite-`u` physical-cluster bound; `R~1`; `L_R=.8` is analytic; no re-entrant pocket for other task parameters; uniqueness of the bandwidth optimum; hardware meaning of illustrative GHz scales; novelty.
