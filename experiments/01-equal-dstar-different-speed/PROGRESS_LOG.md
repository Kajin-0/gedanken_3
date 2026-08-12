# Progress Log — Experiment 01

**Consolidation note — 2026-08-12 01:11 EDT:** compact chronology preserving consequential derivations, corrections, invalidations, rejected shortcuts, numerical validations, asymptotic qualifications, and the current stopping point. Full derivations remain in dedicated step files.

---

## Steps 01–12
Equal scalar reference `D*` does not determine arbitrary temporal-signal SNR; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation problem. **NEGATIVE RESULT:** unknown timing alone does not break that ideal equivalence. Finite windows can because magnitude-only `D*(f)` discards temporal phase/placement. Derived finite-record optimal SNR and task-level detection time. Faster SNR accumulation can be offset by unknown-time search burden. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed directly with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family.

## Step 13
Finite hard-window ideal-white-noise scan is locally Brownian-like. **FAILED NUMERICAL ESTIMATE:** rough-grid crossover near `ell~49` invalid.

## Steps 14–19
A genuine finite timing bandwidth removes the hard-window cusp. Exact smooth Palm identity available; Rice/EC is an upper bound and nonuniform as bandwidth grows. With common physical bandwidth, forcing accessible SNR equal gives no finite optimum. Holding physical signal/noise fixed produces a genuine finite large-`r` optimum; later Palm work confirms a shallow optimum near `kappa~50–65`, about `0.3–0.4%` above infinity.

## Steps 20–23
For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=0.90`, `Lambda=0.895`, Rice gave apparent switches `25.4898402` and `130.1945883`. Palm preserves only `kappa_cross~21.7 +/-0.3`; **INVALIDATED:** upper Rice switch. Palm boundary reaches about `Lambda~0.91` around `kappa_f~60–200`. Direct occupation sampling at `kappa=infinity` gives `Lambda_cross^infinity~0.905 +/-0.004`; `Lambda=0.895` remains fast-preferred.

## Steps 24–30
Finite bandwidth adds `zeta=kappa/(sqrt(2)u sqrt(b))`; generalized Pickands structure is two-parameter. Common-white-noise coupling and Bessel extremum zoom-in identify the rough/smoothed high-band correction. **INVALIDATED INTERMEDIATE:** `0.8131`; correct pointwise coupling coefficient is `0.8906480701 sqrt(chi/zeta)`. Small `chi` introduces Brownian–parabola scales and crossover `mu=sqrt(2)zeta chi^(1/3)`; the fast channel reduces to

```math
F(mu)=(2/sqrt(pi))E[M_inf-M_mu].
```

**INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` fast values were grid biased; continuum-extrapolated full-field values agree with the canonical curve. Fast asymptotic `C_H` refines to about `0.0088`.

## Step 31
Canonical crossover inserted into the finite-`r` boundary; Palm/occupation anchoring gave a one-hump central bridge peaking near `kappa_f~94.9`, `Lambda~0.91068`, then descending toward `Lambda_infinity~0.90513`. **NUMERICAL CLOSURE:** no high-band re-entrant pocket supported for `Lambda=0.895`. **CONDITIONAL:** finite-`u` offset was empirical; later direct finite-`u` steps remove dependence on this fit for the original conclusion.

## Step 32
Finite-`u` first-/second-order Rice moment enclosure

```math
Q(u)+m1^2/(lambda+lambda2) <= P_FA <= Q(u)+m1
```

certifies fast feasible / slow infeasible through at least `kappa_f=170`. **PARTIAL CERTIFICATE.** Around `175–200`, raw crossing moments lose sharpness because one physical slow excursion contains many micro-upcrossings. **NEGATIVE RESULT:** raw crossing multiplicity is the wrong rough-tail variable.

Full derivation: `FINITE_U_RICE_MOMENT_ENCLOSURE_STEP.md`.  
Calculator: `numerics/finite_u_rice_moment_enclosure.py`.

## Step 33
Finite-amplitude excursion-cluster count `C_Delta` satisfies

```math
sup z>u iff C_Delta>=1,
```

and

```math
E[C_Delta]^2/E[C_Delta^2] <= P_FA <= E[C_Delta].
```

Occupation-Palm identities for `E[C_Delta]` and `E[C_Delta^2]` use selected-component duration `L` and success indicator `S`, with no derivative/upcrossing count. Cluster bounds remain sharp at `kappa_f=300`, `1000`, and `infinity`; rough endpoint fast `0.98940–0.98968 alpha`, slow `1.22367–1.22583 alpha`. **NUMERICAL ENDPOINT CERTIFICATE.**

Full derivation: `EXCURSION_CLUSTER_MOMENT_ENCLOSURE_STEP.md`.  
Calculator: `numerics/excursion_cluster_moment_enclosure.py`.

## Step 34
Use `q=kappa_f^-1/2` and common-random-number pairing to the rough endpoint. Dense paired scan plus measured grid/inter-node allowances gives fast envelope `U_f/alpha~<0.99955` and slow envelope `L_s/alpha~>1.10` across `170<=kappa_f<=infinity`. **PAIRED NUMERICAL INTERVAL CLOSURE:** original high-band conclusion no longer depends on Step-31 empirical `delta(kappa)`. **QUALIFICATION:** inter-node allowance is empirical, not theorem-level continuity.

Full derivation: `ADAPTIVE_CLUSTER_TAIL_CLOSURE_STEP.md`.  
Calculator: `numerics/adaptive_cluster_tail_closure.py`.

## Step 35
For normalized spectral amplitude

```math
A_q(w)=|H_x(w)|exp(-w^2q^4/2)/sqrt(I_x(q)),
```

exactly

```math
dA_q/dq=-2q^3(w^2-M2(q))A_q,
||dA_q/dq||_2^2=4q^6 Var_q(w^2).
```

The finite-window `1/w^2` spectral-mass tail makes the `q->0` derivative finite, so the common-noise field is `L2`-Lipschitz through the rough endpoint. Fast `x=7.16`, `Delta q=0.005` gives pointwise RMS process change `~<7.5e-5`; threshold motion `~<2.8e-5`. **REJECTED SHORTCUT:** cluster moments are not pathwise Lipschitz. **NEGATIVE RESULT:** generic Gaussian-supremum anti-concentration is orders of magnitude too coarse at `alpha=1e-6`.

Full derivation: `Q_COUPLING_CONTINUITY_OBSTRUCTION_STEP.md`.  
Calculator: `numerics/q_coupling_continuity.py`.

## Step 36
Freeze a lower level `a`; let `M_j` be maxima of connected components of `{z>a}` and define the cluster-maximum measure

```math
nu_a(B)=ell Q(a)E_a[1_{M_I in B}/L].
```

Then

```math
P(y1<sup z<=y2)<=nu_a((y1,y2]).
```

This is exact, finite-threshold, derivative-free, and rough-endpoint valid. Fast high-band diagnostics near `u~4.959` give local strip intensity `~5 alpha` per unit threshold across `kappa_f=170,300,1000,infinity`, hence observed symmetric-strip scaling `~10 delta alpha`. **TAIL-SENSITIVE ENVELOPE / NUMERICAL VALIDATION.**

Full derivation: `TAIL_SENSITIVE_CLUSTER_STRIP_CONTINUITY_STEP.md`.  
Calculator: `numerics/cluster_maximum_strip.py`.

## Step 37
For fixed local Gaussian covariance class

```math
R(t)=1-c|t|^gamma+o(|t|^gamma),
0<gamma<=2,
```

Pickands' high-threshold tail plus asymptotic single-successful-cluster separation gives

```math
N_a(u+s/u)/N_a(u)->exp(-s),
```

hence the rare-event hazard scale `h_a(u)~uN_a(u)` in the iterated local limit. This analytically explains the Step-36 `O(u delta alpha)` scaling for both smooth and rough endpoint classes.

**REFINEMENT / REJECTED SHORTCUT:** fixed-class asymptotics are nonuniform through `q->0` at physical `u~4.96`. The matched tangent intensity

```math
N_tan=ell[u sqrt(b)/sqrt(2)]H(chi,zeta)Q(u)
```

has formal hazard

```math
h_tan/N_tan
=phi/Q-1/u
 -(chi/u)d_chi log H
 +(zeta/u)d_zeta log H,
```

so Step 37 left the finite-crossover multiplier as a Pickands-elasticity problem.

Full derivation: `CLUSTER_HAZARD_OVERSHOOT_STEP.md`.  
Calculator: `numerics/cluster_hazard_overshoot.py`.

## Step 38 — 01:11 EDT — exact Pickands cross-elasticity ordering
For

```math
F_zeta(t)=|t|erf(zeta|t|)+(e^{-zeta^2t^2}-1)/(sqrt(pi)zeta),
```

exact differentiation and a convexity argument give

```math
\boxed{0<=zeta d_zeta F_zeta(t)<=F_zeta(t).}
```

Integrating this multiplicative derivative bound yields, for every `lambda>=1`,

```math
F_{lambda zeta}(t)<=lambda F_zeta(t).
```

Hence the tangent variograms obey

```math
g_{chi,lambda zeta}(t)<=g_{lambda chi,zeta}(t),
```

and Brown–Resnick Slepian comparison gives the exact generalized-Pickands cross-ordering

```math
\boxed{H(chi,lambda zeta)<=H(lambda chi,zeta).}
```

Where logarithmic derivatives exist,

```math
\boxed{0<=zeta d_zeta log H<=chi d_chi log H.}
```

The finite-`lambda` statement also yields the corresponding one-sided Dini-derivative inequality without assuming differentiability.

Along a fixed-`kappa` threshold path, `chi~u` and `zeta~1/u`, so `H` is exactly nondecreasing with `u`. Therefore the matched tangent hazard has the explicit uniform bound

```math
\boxed{h_tan/N_tan<=phi(u)/Q(u)-1/u.}
```

At the physical fast threshold `u~4.959`, this is `~4.9452`. Finite-difference monotonicity also gives an exact symmetric tangent-strip factor

```math
B(u,delta)
=((u-delta)/u)Q(u-delta)/Q(u)
-((u+delta)/u)Q(u+delta)/Q(u).
```

For `delta=1e-4`, `B~9.89e-4`, so if `N_tan~alpha=1e-6` the tangent strip is bounded at about `9.9e-10` absolute scale.

**NEGATIVE RESULT / REFINEMENT:** Step-36 exact finite-`u` strip diagnostics (`~5.0–5.5 alpha` per threshold unit) can exceed the tangent coefficient `~4.9452`. Therefore the positive `zeta` elasticity is not the source of the finite-crossover excess. The remaining discrepancy is the finite-threshold correction from the leading tangent/Pickands intensity to the exact cluster-maximum measure.

Full derivation: `PICKANDS_ELASTICITY_ORDERING_STEP.md`.  
Calculator: `numerics/pickands_elasticity_ordering.py`.

---

## Current stopping point

The generalized Pickands elasticity is now controlled exactly enough for the matched tangent hazard. The remaining theorem gap is one layer outward: finite-`u` remainder control between the tangent approximation and the exact physical excursion-cluster first moment, especially its threshold variation near `u~5`.

### Single natural next question

> Can the exact cluster first moment be factorized as `N_a(u,q)=N_tan(u,q) R(u,q)` with a controlled finite-threshold remainder, and can the threshold variation of `R` be bounded tightly enough at `u~5` to account for the observed `~5–10%` excess in the Step-36 strip intensity?
