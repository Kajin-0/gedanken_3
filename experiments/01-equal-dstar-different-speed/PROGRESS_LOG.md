# Progress Log — Experiment 01

**Consolidation note — 2026-08-12 09:42 EDT:** compact chronology preserving consequential results, corrections, invalidations, rejected shortcuts, numerical validations, asymptotic qualifications, and current stopping point. Full derivations remain in dedicated step files.

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
Use `q=kappa_f^-1/2` and common-random-number pairing to the rough endpoint. Dense scan plus measured grid/inter-node allowances gives fast envelope `U_f/alpha~<0.99955` and slow envelope `L_s/alpha~>1.10` over `170<=kappa_f<=infinity`. **PAIRED NUMERICAL INTERVAL CLOSURE.** Inter-node allowance was empirical.

## Step 35
The normalized common-noise Gaussian field is `L2`-Lipschitz in `q` through the rough endpoint. Fast `Delta q=.005` pointwise RMS is bounded by `~7.5e-5`; threshold motion `~<2.8e-5`. **REJECTED SHORTCUT:** cluster moments are not pathwise Lipschitz. **NEGATIVE RESULT:** generic Gaussian-supremum anti-concentration is orders too coarse at `alpha=1e-6`.

## Step 36
Fix a lower excursion level `a` and define the cluster-maximum measure `nu_a`. Exact finite-threshold strip envelope:

```math
P(y1<sup z<=y2)<=nu_a((y1,y2]).
```

Fast high-band diagnostics near `u~4.959` give local strip intensity `~5 alpha` per threshold unit over `kappa_f=170,300,1000,infinity`. **TAIL-SENSITIVE ENVELOPE / NUMERICAL VALIDATION.**

## Step 37
Fixed-class Pickands theory plus asymptotic single-successful-cluster separation gives `N_a(u+s/u)/N_a(u)->exp(-s)` and hence rare-event hazard scale `h_a~uN_a`. **REFINEMENT:** fixed-class asymptotics are nonuniform through `q->0` at physical `u~4.96`.

## Step 38
Exact smoothing inequality `0<=zeta d_zeta F_zeta<=F_zeta` implies `H(chi,lambda zeta)<=H(lambda chi,zeta)` and therefore `0<=zeta d_zeta logH<=chi d_chi logH`. Along fixed physical `kappa`, `H` is nondecreasing with threshold, giving `h_tan/N_tan<=phi/Q-1/u`. At `u~4.959`, bound `~4.9452`; symmetric tangent-strip factor at `delta=1e-4` is `~9.89e-4`. **REFINEMENT / NEGATIVE RESULT:** Step-36 exact strip excess is finite-`u` remainder physics, not positive `zeta` elasticity.

## Step 39
Define `R=N_a/N_tan`. Exact-cluster first moment exceeds the canonical tangent intensity by about `56%` (`R~1.56`), so `R~1` is false at `u~5`. But `-d_u logR` is inferred numerically to be only `~0.07–0.68`; `L_R=.8` is merely a working numerical envelope. **REJECTED SHORTCUT:** a small-amplitude second-order Pickands remainder is the wrong theorem target.

Full derivation: `FINITE_U_REMAINDER_FACTOR_STEP.md`.  
Helper: `numerics/finite_u_remainder_factor.py`.

## Step 40
Cameron–Martin likelihood rearrangement gives, for arbitrary Gaussian event `A` of probability `p` and Cameron–Martin shift norm `r`,

```math
Phi(Phi^-1(p)-r)<=mu(A+h)<=Phi(Phi^-1(p)+r).
```

For the timing exceedance event, a positive covariance-kernel RKHS barrier converts a threshold displacement directly into a rare-event-scaled probit displacement. With midpoint covariance floor `m_q~.92524` and conservative numerical floor `.92`, `delta=1e-4` raises the rough-endpoint fast upper only from `.98968 alpha` to about `.990213 alpha`. **PARTIAL CERTIFICATE:** threshold buffering is controlled at exact-event level; `.92` is not formal interval arithmetic.

Full derivation: `CAMERON_MARTIN_BARRIER_STEP.md`.  
Helper: `numerics/cameron_martin_barrier.py`.

## Step 41 — 09:42 EDT — analytic common-noise sup-norm interpolation
For the common-white-noise difference process

```math
d_{q,r}(t)=z_q(t)-z_r(t),
```

Step 41 replaces the empirical Step-34 inter-node probability allowance by analytic Gaussian-process bounds.

### Tiny-`q` correction
High-frequency mass gives

```math
I(q)=I(0)-2sqrt(pi)c_X^2q^2+o(q^2)
```

and therefore

```math
\boxed{
sigma_{0,r}^2=(sqrt(2)-1)L_0^2r^2+o(r^2),
}
```

with `L_0~.00835839` at `X=7.16`. Hence the `q=0 -> .005` common-noise chord has leading RMS `~2.69e-5`, and `0 -> .0025` gives `~1.34e-5`.

**INVALIDATED NUMERICAL VALUE:** Step-35 helper's quoted `exact pairwise` `0 -> .005` value `~5.4e-5` was produced by ill-conditioned quadrature/cancellation of nearly equal spectral masses. The exact overlap formula and Step-35 `L2` regularity result remain valid.

### Rough endpoint interval
For tiny `r`, `|A_0-A_r|<=A_0`, so the difference increment metric obeys

```math
E[(d(t+s)-d(t))^2]<=2[1-R_0(s)].
```

Use a deliberately loose local envelope `K_*|s|`, `K_*=2e-4`, point-SD envelope `sigma_*=2.1e-5`, mathematical time-net spacing `h=1e-9`, and Gaussian grid/modulus failure budgets `9e-12` and `3e-13`. A grid union bound + Sudakov–Fernique Brownian modulus + Borell concentration gives `epsilon~2.079e-4` on `0<=q<=.0035`. After maximum threshold motion `1.96e-5` and Step-40 translation,

```math
\boxed{p_f/alpha<=.999970.}
```

### Strictly positive finite `q`
For `q,r>0`, the difference field is differentiable. With

```math
sigma^2=Var d(0),
qquad
lambda_d=sqrt(Var d'(0))/sigma,
```

Rice's expected upcrossing formula gives the exact two-sided sup envelope

```math
\boxed{
P(||d||_infinity>epsilon)
<=2Q(v)+ell lambda_d/pi e^{-v^2/2},
\qquad v=epsilon/sigma.
}
```

Conservative positive-integrand spectral envelopes for each half-cell, combined with Step-34 node envelopes and Step-40 translation, remain below `alpha` on every cell. Representative final ratios include `.999983` near `q=.005`, `.999970` near `.035`, `.999880` near `.045`, and the tightest rounded row `.999997` near `.055`; higher-`q` cells have larger node margins.

**PARTIAL CERTIFICATE / REFINEMENT:** conditional on the Step-34 numerical node/grid envelopes and conservative floating-point spectral constants,

```math
\boxed{p_f(q)<alpha\quad\forall\ 0<=q<=.0767.}
```

The old empirical `0.0006 alpha` inter-node allowance is no longer required. The remaining certification gap is rigorous finite-sample/statistical control of the sampled occupation-Palm node estimators and formal continuum/grid arithmetic—not continuous-`q` interpolation itself.

Full derivation: `GAUSSIAN_Q_SUPNORM_INTERPOLATION_STEP.md`.  
Helper: `numerics/q_supnorm_interpolation.py`.

---

## Current stopping point

The continuous high-band `q` interval is analytically interpolated conditional on the existing node estimates. The next natural target is rigorous finite-sample concentration for the weighted occupation-Palm node estimators, replacing Gaussian standard-error allowances.

### Single natural next question

> Can the weighted occupation-Palm node estimators be given rigorous finite-sample concentration bounds strong enough to preserve the fast/slow separation, replacing the Gaussian standard-error allowances used in Steps 33–34?