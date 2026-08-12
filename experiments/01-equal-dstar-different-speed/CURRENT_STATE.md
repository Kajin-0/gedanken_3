# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-12 09:42 EDT  
**Status:** forty-one logical steps completed. Step 41 replaces Step 34's empirical `0.0006 alpha` inter-node allowance with analytic Gaussian-process interpolation. The rough endpoint is handled by a deterministic time net plus a Brownian-type modulus bound; every strictly positive finite-`q` pair is differentiable and is handled by an exact Rice upcrossing sup-tail envelope. Both feed directly into the Step-40 Cameron–Martin threshold translation. Conditional on the existing Step-34 numerical node/grid envelopes and conservative spectral constants, the fast false-alarm probability remains below `alpha` for every `0<=q<=0.0767` (`170<=kappa_f<=infinity`). Step 41 also corrects one Step-35 tiny-`q` numerical value: the reported `q=0 -> .005` pair RMS `~5.4e-5` was a cancellation-damaged quadrature value; the endpoint chord asymptotic gives `~2.69e-5`, while the Step-35 `L2` regularity conclusion remains valid. The remaining certification gap is no longer continuous-`q` interpolation; it is rigorous finite-sample/statistical and continuum-grid control of the sampled node quantities. No universal scalar replacement metric and no novelty claim.

---

## Original question

Two hypothetical photodetectors satisfy

```math
D_A^*=D_B^*
```

but have radically different temporal responses. Does equal conventional specific detectivity imply equal ability to detect arbitrary optical signals?

---

## Surviving logical chain

### Steps 01–13 — scalar `D*`, finite records, rough-window obstruction
- Equal scalar reference `D*` does **not** determine arbitrary temporal-signal SNR; explicit 1 Hz construction gave `SNR_A/SNR_B~6.36`.
- Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation stationary-Gaussian maximum-SNR problem.
- **NEGATIVE RESULT:** unknown timing alone does not break that full-observation equivalence.
- Finite observation can because magnitude-only `D*(f)` discards temporal placement/phase.
- Exact finite-record optimal SNR and task-level detection time were derived.
- Faster SNR accumulation can be offset by unknown-time search burden.
- **REJECTED SHORTCUT:** finite-window SNR cannot be mixed directly with full-template timing bandwidth.
- **NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family.
- Step 13: hard-window timing scan is locally Brownian-like. **FAILED NUMERICAL ESTIMATE:** rough-grid crossover `ell~49` is invalid.

### Steps 14–23 — genuine information bandwidth; Rice reversal corrected
- A genuine finite timing-information bandwidth removes the hard-window cusp.
- Holding physical signal/noise fixed creates a shallow finite bandwidth optimum.
- For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=.90`, `Lambda=.895`, Rice gave apparent switches `25.4898402` and `130.1945883`.
- Palm preserves only the lower switch `~21.7 +/-0.3`. **INVALIDATED:** upper Rice switch.
- Palm high-band boundary sits near `Lambda~.91`; direct rough-endpoint occupation sampling gives `Lambda_cross^infinity~.905 +/- .004`, leaving `Lambda=.895` fast-preferred.

### Steps 24–30 — two-parameter generalized Pickands crossover
- Finite bandwidth introduces `zeta=kappa/(sqrt(2)u sqrt(b))`; the local extreme problem is two-parameter.
- **INVALIDATED INTERMEDIATE:** rough/smoothed pointwise coupling coefficient `.8131`; correct value `.8906480701 sqrt(chi/zeta)`.
- Bessel extremum zoom-in and Brownian–parabola scaling introduce `mu=sqrt(2)zeta chi^(1/3)`.
- Small-`chi` fast channel reduces to the canonical model-reduced crossover `F(mu)=(2/sqrt(pi))E[M_inf-M_mu]`.
- **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` values were grid biased; continuum-extrapolated full-field values agree with the canonical reduction.

### Steps 31–34 — direct finite-`u` high-band closure
- Step 31: empirical Palm-anchored one-hump boundary; later direct finite-`u` work removes dependence on this fit for the original conclusion.
- Step 32: first/second Rice moment enclosure directly certifies fast feasible / slow infeasible through at least `kappa_f=170`; raw crossing moments then fail from micro-upcrossing multiplicity.
- Step 33: finite-amplitude excursion clusters `C_Delta` replace microcrossings. Exact occupation-Palm first/second-moment identities remain meaningful at the rough endpoint. **NUMERICAL ENDPOINT CERTIFICATE.**
- Step 34: natural coordinate `q=kappa_f^-1/2`; paired endpoint coupling gives fast numerical envelope `U_f/alpha~<.99955`, slow lower envelope `~>1.10` over `170<=kappa_f<=infinity`. **PAIRED NUMERICAL INTERVAL CLOSURE.** Old inter-node allowance `0.0006 alpha` was empirical.

### Steps 35–36 — analytic `q` regularity and rare-event strip measure
- Step 35: normalized common-noise field is `L2`-Lipschitz in `q` through `q=0`; threshold motion is also Lipschitz. **REJECTED SHORTCUT:** cluster counts are not pathwise Lipschitz. **NEGATIVE RESULT:** generic Gaussian-supremum anti-concentration is orders too coarse at `alpha=1e-6`.
- Step 36: freeze a lower excursion level and define the physical cluster-maximum measure `nu_a`; exact strip bound `P(y1<sup z<=y2)<=nu_a((y1,y2])`. Numerical local strip intensity near `u~4.959` is `~5 alpha` per threshold unit.

### Steps 37–38 — overshoot scale and exact Pickands elasticity ordering
- Fixed-class Pickands theory gives `N_a(u+s/u)/N_a(u)->exp(-s)` and rare-event hazard scale `h_a~uN_a` under asymptotic single-cluster separation.
- Step 38 proves exact cross-ordering `H(chi,lambda zeta)<=H(lambda chi,zeta)` and hence `0<=zeta d_zeta logH<=chi d_chi logH` wherever derivatives exist.
- Along fixed physical `kappa`, `H` is nondecreasing with threshold; matched tangent hazard obeys `h_tan/N_tan<=phi/Q-1/u`.
- At `u~4.959`, tangent coefficient `~4.9452`; symmetric `delta=1e-4` tangent strip factor `~9.89e-4`.
- **REFINEMENT:** exact Step-36 excess is finite-`u` remainder physics, not positive smoothing elasticity.

### Step 39 — finite-`u` remainder factor
Define `R=N_a/N_tan`. At the fast witness `R~1.56`, so a small-amplitude second-order Pickands remainder is false at `u~5`. But `-d_u logR` is numerically only `~0.07–0.68`; `L_R=.8` was retained solely as a working numerical envelope. **REJECTED SHORTCUT:** proving `R~1` is neither true nor necessary.

### Step 40 — Cameron–Martin covariance barrier
For any Gaussian path event `A` of probability `p` and Cameron–Martin vector `h`, `r=||h||_H`, likelihood rearrangement gives

```math
Phi(Phi^-1(p)-r)<=mu(A+h)<=Phi(Phi^-1(p)+r).
```

For `A_u={sup z>u}`, a positive RKHS barrier `h_delta>=delta` gives a direct exact-event threshold translation. Choosing the midpoint covariance representer,

```math
m_q=inf_{t in [0,ell]}R_q(t-ell/2),
```

```math
h_delta(t)=delta R_q(t-ell/2)/m_q,
```

has norm `delta/m_q`. Deterministic high-band covariance evaluation gives `m_q~.92524`; conservative numerical floor `.92` yields `p_f(u-1e-4)<=.990213 alpha` from the rough-endpoint fast upper `.98968 alpha`. **PARTIAL CERTIFICATE:** finite-threshold buffering is directly controlled without tangent/remainder modeling.

### Step 41 — analytic continuous-`q` interpolation
The common-noise difference field is

```math
d_{q,r}(t)=z_q(t)-z_r(t),
```

with point variance `||A_q-A_r||_2^2`.

**REFINEMENT / INVALIDATED NUMERICAL VALUE:** high-frequency mass asymptotics give

```math
I(q)=I(0)-2sqrt(pi)c_X^2q^2+o(q^2),
```

and therefore

```math
sigma_{0,r}^2=(sqrt(2)-1)L_0^2r^2+o(r^2),
```

with `L_0~.00835839`. Thus `q=0 -> .005` has leading RMS `~2.69e-5`, not the Step-35 helper's cancellation-damaged `~5.4e-5`; `0 -> .0025` is `~1.34e-5`. Step-35 field regularity remains valid.

For the rough endpoint interval `0<=q<=.0035`, use a deterministic time net plus the exact metric domination

```math
E[(d(t+s)-d(t))^2]<=2[1-R_0(s)]
```

and a deliberately loose local `K_*|s|` bound. A Gaussian grid union bound, Sudakov–Fernique Brownian modulus comparison, and Borell concentration give `p_f/alpha<=.999970` after Step-40 threshold translation.

For every strictly positive finite-`q` pair, `d_{q,r}` is differentiable. If `sigma^2=Var d(0)` and `lambda_d=sqrt(Var d'(0))/sigma`, the two-sided Rice envelope is

```math
\boxed{
P(||d||_infinity>epsilon)
<=2Q(v)+ell lambda_d/pi e^{-v^2/2},
\qquad v=epsilon/sigma.
}
```

Combining conservative deterministic half-cell spectral envelopes with Step-34 node probability envelopes and Step-40 translation gives `p_f(q)<alpha` on every finite cell. The tightest rounded cell is near `q=.055`, with final conservative ratio `p/alpha~.999997`.

**PARTIAL CERTIFICATE / REFINEMENT:** the Step-34 empirical `0.0006 alpha` inter-node allowance is no longer needed. Conditional on the existing numerical node/grid envelopes and conservative floating-point spectral constants,

```math
\boxed{
p_f(q)<alpha\quad\forall\ 0<=q<=.0767.}
```

See `GAUSSIAN_Q_SUPNORM_INTERPOLATION_STEP.md` and `numerics/q_supnorm_interpolation.py`.

---

## Current frontier

Continuous-parameter interpolation is no longer the principal gap. The remaining certification problem is the **sampled node/grid quantities themselves**: replace Gaussian Monte Carlo standard-error allowances for the weighted occupation-Palm estimators with rigorous finite-sample concentration/confidence bounds, and formalize the remaining spectral/grid constants if a theorem-level certificate is desired.

### Single next question — DO NOT ANSWER YET

> Can the weighted occupation-Palm node estimators be given rigorous finite-sample concentration bounds strong enough to preserve the fast/slow separation, replacing the Gaussian standard-error allowances used in Steps 33–34?

---

## Scope boundary

Do not claim: faster is universally better/worse; a universal scalar replacement for `D*`; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 fast values as continuum data; Step-31 empirical fit exact/required for the original conclusion; Step-33/34 Monte Carlo estimates are formal interval arithmetic; Step-36 proves a uniform hazard density; Step-38 tangent hazard is an exact finite-`u` physical-cluster bound; `R~1`; `L_R=.8` analytic; `m_*=.92` formal interval arithmetic; Step-41 makes the node Monte Carlo/grid estimates theorem-level; no re-entrant pocket for other task parameters; uniqueness of bandwidth optimum; illustrative GHz scales as hardware recommendations; novelty.