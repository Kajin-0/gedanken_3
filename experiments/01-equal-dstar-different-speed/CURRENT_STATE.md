# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-12 17:02 EDT  
**Status:** forty-three logical steps completed. Step 43 resolves the short-duration term introduced by Step 42. A successful lower-level excursion cluster of duration `<L0` must contain a level-`u` point and an interior level-`a=u-Delta` boundary point within lag `<L0`, so it forces a highly discordant Gaussian pair while already at the rare high threshold. For the established fast high-band family (`Delta=.15`, `L0=.02`, `u~4.95898`), a deterministic time net with `h=1e-5`, conservative short-lag correlation floor `rho_*=.99980`, and local metric envelope `K_*=2e-4` gives `P(C_short>=1)<3.9e-11`, i.e. `<3.9e-5 alpha` at `alpha=1e-6`. The net-modulus failure term is below `10^-654`. Thus the inverse-duration support pathology is not physically important for false alarms; the active statistical target is now the bounded `L>=.02` long-cluster occupation-Palm estimator. The short-cluster probability inequality is analytic conditional on `rho_*` and `K_*`; those constants are conservative deterministic floating-point envelopes, not formal interval arithmetic. No universal scalar replacement metric and no novelty claim.

---

## Original question

Two hypothetical photodetectors satisfy `D_A^*=D_B^*` but have radically different temporal responses. Does equal conventional specific detectivity imply equal ability to detect arbitrary optical signals?

---

## Surviving logical chain

### Steps 01–13 — scalar `D*`, finite records, rough-window obstruction
Equal scalar reference `D*` does not determine arbitrary temporal-signal performance; an explicit 1 Hz construction gave `SNR_A/SNR_B~6.36`. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation stationary-Gaussian problem. Finite records create a task-level timing-search problem. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed directly with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum. Step 13 identifies hard-window Brownian-like local roughness. **FAILED NUMERICAL ESTIMATE:** rough-grid crossover `ell~49` is invalid.

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
For the finite-grid Step-33 first-moment contribution `Y=m_aS/L`, the implementation guarantees `L>=delta_t/2`, so `0<=Y<=2m_a/delta_t`. At the fast rough endpoint (`n=50000`), Maurer-Pontil empirical Bernstein gives a 95% radius `~.24538 alpha`, dominated by the support/range term `~.23373 alpha`. **NEGATIVE RESULT / REJECTED SHORTCUT:** generic bounded-variable concentration on the raw inverse-duration estimator is much too weak. Choose duration cutoff `L0`; then exactly `P_FA<=E[C_long]+P(C_short>=1)`, and the long-cluster support becomes `m_a/L0`. For `L0=.02`, support falls 40x and the 50k-path range penalty becomes `~.00584 alpha`.

### Step 43 — short successful-cluster Gaussian envelope
A successful cluster `I` with `|I|<L0<ell` cannot touch both search endpoints. At least one interior boundary has `z=a`, while some point inside has `z>u`; therefore it forces a full amplitude change `Delta=u-a` over lag `<L0`.

Use the established fast endpoint values

```text
u ~= 4.95898348
a ~= 4.80898348
Delta=.15
L0=.02
ell=.895.
```

On a deterministic time net with `h=1e-5`, `gamma=.0025`, a short cluster produces a net pair with

```text
X >= U=u-gamma=4.95648348
Y <= A=a+gamma=4.81148348
lag <= .02002.
```

The rough endpoint has exact covariance `R_0(.02002)~.9998009903`; deterministic finite-band checks are slightly larger. Retain conservative `rho_*=.99980`. For any standard Gaussian pair with correlation `rho>=rho_*`, conditional Gaussian regression gives

```math
P(X>=U,Y<=A)
<=Q(U) Phi((A-rho_*U)/sqrt(1-rho_*^2))
<1.075e-19.
```

There are at most `358451505` ordered candidate net pairs, so their union is `<3.86e-11`. A local increment envelope `E[(z(t+s)-z(t))^2]<=K_*|s|`, `K_*=2e-4`, gives `log10 P(net-modulus failure)<-654`. Hence

```math
\boxed{P(C_short>=1)<3.9e-11<3.9e-5 alpha.}
```

**SHORT-CLUSTER GAUSSIAN ENVELOPE / PARTIAL CERTIFICATE:** the short-duration term is negligible at the false-alarm scale. The inequality is analytic conditional on the conservative numerical `rho_*` and `K_*`; they are not formal interval constants.

See `SHORT_CLUSTER_OSCILLATION_BOUND_STEP.md` and `numerics/short_cluster_oscillation_bound.py`.

---

## Current frontier

The inverse-duration support pathology has been isolated and shown to carry negligible false-alarm probability for `L0=.02`. The next statistical calculation should rerun/store only the duration-truncated long-cluster occupation-Palm contributions and apply a genuine empirical-Bernstein upper confidence bound to `E[C_long]`. Later gaps remain: simultaneous confidence allocation, slow lower-ratio concentration, continuum timing-grid bias, and formal interval arithmetic for spectral constants.

### Single next question — DO NOT ANSWER YET

> With `P(C_short>=1)` negligible, does a dedicated `L0=.02` truncated occupation-Palm run give a rigorous empirical-Bernstein upper confidence bound on `E[C_long]` below the remaining fast endpoint budget?

---

## Scope boundary

Do not claim: faster universally better/worse; a universal scalar replacement for `D*`; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 fast values as continuum data; Step-31 empirical fit exact/required for the original high-band conclusion; Step-34 as a fully formal theorem; Step-36 as a uniform hazard theorem; `R~1`; `L_R=.8` analytic; `m_*=.92`, `rho_*=.99980`, or `K_*=2e-4` as formal interval constants; Step-41 node estimates themselves rigorous; raw empirical Bernstein certifies Step-33; `L0=.02` is optimal; no re-entrant pocket for other task parameters; uniqueness of bandwidth optimum; illustrative GHz scales as hardware recommendation; novelty.