# Progress Log — Experiment 01

**Consolidation note — 2026-08-12 07:24 EDT:** compact chronology preserving consequential results, corrections, invalidations, rejected shortcuts, numerical validations, asymptotic qualifications, and current stopping point. Full derivations remain in dedicated step files.

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

## Step 39
Define `R=N_a/N_tan`. The exact-cluster first moment exceeds the canonical tangent intensity by about `56%` (`R~1.56`), so `R~1` is false at `u~5`. But `-d_u log R=h_a/N_a-h_tan/N_tan` is inferred numerically to be only `~0.07–0.68`; `L_R=.8` is merely a conservative numerical working envelope. **REJECTED SHORTCUT:** a small-amplitude second-order Pickands remainder is the wrong theorem target.

Full derivation: `FINITE_U_REMAINDER_FACTOR_STEP.md`.  
Helper: `numerics/finite_u_remainder_factor.py`.

## Step 40 — 07:24 EDT — Cameron–Martin RKHS barrier
For a centered Gaussian measure and Cameron–Martin vector `h` with `r=||h||_H`, the Cameron–Martin density plus one-dimensional monotone rearrangement gives, for any event `A` of probability `p`,

```math
\boxed{
Phi(Phi^-1(p)-r) <= mu(A+h) <= Phi(Phi^-1(p)+r).
}
```

For the timing exceedance event `A_u={sup z>u}`, any RKHS barrier `h_delta(t)>=delta` gives

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

An exactly constant Cameron–Martin shift is unnecessary. For a unit-variance covariance `R_q`, choose midpoint `t0=ell/2` and

```math
m_q=inf_{t in [0,ell]}R_q(t-t0).
```

The covariance kernel section has RKHS norm `1`, so

```math
h_delta(t)=delta R_q(t-t0)/m_q
```

is an exact barrier with norm `delta/m_q`. Therefore

```math
\boxed{
p_q(u-delta)-p_q(u+delta)
<=Phi(z+delta/m_q)-Phi(z-delta/m_q),
\quad z=Phi^-1(p_q(u)).
}
```

The rough covariance is a positive template autocorrelation; finite Gaussian bandwidth convolves its covariance numerator with a positive Gaussian. Hence `m_q>0` for every high-band `q`, and compact continuity gives existence of a uniform positive floor. Deterministic spectral quadrature gives

```text
kappa_f        m_q (midpoint barrier floor)
170             ~0.925258
200             ~0.925252
300             ~0.925245
500             ~0.925240
1000            ~0.925239
infinity        ~0.925238
```

so retain deliberately conservative numerical working floor `m_*=0.92`.

Using Step-33 rough-endpoint fast upper `p_f(u)<=0.98968 alpha`, `alpha=1e-6`, and `delta=1e-4` gives

```math
\boxed{
p_f(u-delta)<=0.990213 alpha<alpha.
}
```

At the observed floor, the corresponding symmetric strip is about `1.06e-9` absolute. This is a direct exact-event rare-threshold bound and does not use the tangent model or `R`.

**PARTIAL CERTIFICATE:** the finite-`u` threshold-buffer/remainder problem is no longer the conceptual bottleneck. **QUALIFICATION:** `m_*=0.92` is numerical rather than formal interval arithmetic.

Full derivation: `CAMERON_MARTIN_BARRIER_STEP.md`.  
Helper: `numerics/cameron_martin_barrier.py`.

---

## Current stopping point

The threshold-buffer piece is now directly controlled by Cameron–Martin geometry. The main remaining continuous-parameter theorem gap is the sup-norm common-noise coupling failure probability

```math
eta=P(||z_q-z_r||_infinity>epsilon)
```

for neighboring `q` values.

### Single natural next question

> Can the common-white-noise difference process `d_{q,r}(t)=z_q(t)-z_r(t)` be given a sharp Borell–TIS / metric-entropy sup-norm tail bound at `|q-r|<=0.005`, small enough that its failure probability `eta` fits inside the remaining `~1e-8` fast false-alarm margin?