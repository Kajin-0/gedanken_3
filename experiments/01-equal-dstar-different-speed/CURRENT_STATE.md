# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-12 07:24 EDT  
**Status:** forty logical steps completed. Step 40 bypasses the Step-39 finite-`u` remainder factor for threshold continuity. Cameron–Martin change of measure gives a sharp probit translation bound for arbitrary Gaussian path events. An exactly constant shift is unnecessary: if the timing covariance has a positive floor `m_q` from the search midpoint, the normalized covariance kernel section is an RKHS barrier with norm `delta/m_q` and raises the entire path by at least `delta`. Therefore the exact false-alarm event obeys `p_q(u-delta)<=Phi(Phi^-1(p_q(u))+delta/m_q)` and `p_q(u+delta)>=Phi(Phi^-1(p_q(u))-delta/m_q)`. For the established high-band fast trajectory, deterministic covariance quadrature gives `m_q~0.92524`; using conservative numerical floor `m_*=0.92`, a `delta=1e-4` threshold decrease raises the Step-33 rough-endpoint fast upper probability only from `0.98968 alpha` to about `0.990213 alpha<alpha`. The threshold-buffer piece is therefore analytically controlled once a positive covariance floor is certified; the main remaining theorem gap is the sup-norm common-noise `q`-coupling tail `eta`. No universal scalar replacement metric and no novelty claim.

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
Define `R=N_a/N_tan`. At the fast witness, `R~1.56`, so a small-amplitude second-order Pickands remainder is false at `u~5`. However, `-d_u log R=h_a/N_a-h_tan/N_tan` is inferred numerically to be only `~0.07–0.68`; `L_R=.8` was retained solely as a numerical working envelope. **REJECTED SHORTCUT:** proving `R~1` is neither true nor necessary.

### Step 40 — Cameron–Martin covariance barrier
For a centered Gaussian measure with Cameron–Martin vector `h`, `r=||h||_H`, and arbitrary event `A` of probability `p`, Cameron–Martin likelihood rearrangement gives the sharp translation bracket

```math
Phi(Phi^-1(p)-r) <= mu(A+h) <= Phi(Phi^-1(p)+r).
```

For the timing exceedance event `A_u={sup z>u}`, any RKHS function `h_delta>=delta` implies

```math
\boxed{
p(u-delta)<=Phi(Phi^-1(p(u))+||h_delta||_H),
}
```

```math
\boxed{
p(u+delta)>=Phi(Phi^-1(p(u))-||h_delta||_H).
}
```

Choose midpoint `t0=ell/2`. The kernel section `R_q(t-t0)` has RKHS norm `1`. With

```math
m_q=inf_{t in [0,ell]}R_q(t-t0)>0,
```

the barrier

```math
h_delta(t)=delta R_q(t-t0)/m_q
```

satisfies `h_delta>=delta` and has exact norm `delta/m_q`. Hence

```math
\boxed{
p_q(u-delta)-p_q(u+delta)
<=Phi(z+delta/m_q)-Phi(z-delta/m_q),
\quad z=Phi^-1(p_q(u)).
}
```

The rough covariance is a positive autocorrelation; finite Gaussian information weighting convolves it with a positive Gaussian, so `m_q>0` for every high-band `q`, and compact continuity gives a uniform positive floor. Deterministic quadrature gives `m_q~0.92524` over `170<=kappa_f<=infinity`; conservative working floor `m_*=0.92` yields, from Step-33 endpoint upper `p_f(u)<=0.98968 alpha`,

```math
p_f(u-10^-4) <= 0.990213 alpha < alpha.
```

**PARTIAL CERTIFICATE:** the exact finite-threshold buffer is now controlled at event level without the tangent model or `R`. **QUALIFICATION:** `m_*=0.92` is a conservative numerical floor, not formal interval arithmetic.

See `CAMERON_MARTIN_BARRIER_STEP.md` and `numerics/cameron_martin_barrier.py`.

---

## Current frontier

The threshold anti-concentration/remainder problem is no longer the principal obstacle. The remaining theorem-level continuous-`q` gap is the probability that the **common-white-noise difference process** between neighboring bandwidths has a large sup norm. A useful result must bound

```math
eta=P(||z_q-z_r||_infinity>epsilon)
```

for `|q-r|<=.005` sharply enough to fit inside the remaining fast false-alarm margin.

### Single next question — DO NOT ANSWER YET

> Can the common-white-noise difference process `d_{q,r}(t)=z_q(t)-z_r(t)` be given a sharp Borell–TIS / metric-entropy sup-norm tail bound at `|q-r|<=0.005`, small enough that its failure probability `eta` fits inside the remaining `~1e-8` fast false-alarm margin?

---

## Scope boundary

Do not claim: faster is universally better/worse; a universal scalar replacement for `D*`; Step-13 `ell~49`; the Step-20 double reversal; raw Step-27 fast values as continuum data; Step-31 empirical fit is exact or still necessary for the original conclusion; Step-34 is theorem-level continuous-parameter closure; Step-36 proves a uniform hazard density; Step-38 tangent hazard is an exact finite-`u` physical-cluster bound; `R~1`; `L_R=.8` is analytic; `m_*=.92` is formal interval arithmetic; Step-40 alone closes the continuous-`q` problem; no re-entrant pocket for other task parameters; uniqueness of the bandwidth optimum; hardware meaning of illustrative GHz scales; novelty.