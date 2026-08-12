# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 21:17 EDT:** compact chronology preserving consequential results, corrections, invalidations, rejected shortcuts, numerical validations, asymptotic qualifications, and current stopping point. Full derivations remain in dedicated step files.

---

## Steps 01–04
Equal scalar reference `D*` does not determine arbitrary temporal-signal SNR; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation problem. **NEGATIVE RESULT:** unknown timing alone does not break that ideal equivalence. Finite windows can because magnitude `D*(f)` discards temporal phase/placement.

## Steps 05–12
Derived finite-record optimal SNR and task-level detection time. Faster SNR accumulation can be offset by unknown-time search burden. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed directly with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family.

## Step 13
Finite hard-window ideal-white-noise scan is locally Brownian-like. **FAILED NUMERICAL ESTIMATE:** rough-grid `ell~49` crossover invalid.

## Steps 14–17
A genuine finite timing bandwidth removes the cusp. Exact smooth Palm identity available; Rice/EC is an upper bound. Finite hard windows have `sigma_kappa^2~a_x kappa/sqrt(pi)`, making Rice nonuniform toward the rough limit.

## Steps 18–19
With `kappa_i=Omega_B tau_i`, forcing accessible SNR equal gives no finite bandwidth optimum. Holding physical signal/noise fixed produces a finite large-`r` optimum; later Palm work confirms a shallow optimum survives beyond Rice.

## Steps 20–21
For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=0.90`, `Lambda=0.895`, Rice gave switches `25.4898402` and `130.1945883`. Palm preserves only the lower switch `kappa_cross~21.7 +/-0.3`. **INVALIDATED:** upper Rice switch. Palm checks at `130,160,300` keep fast preferred.

## Step 22
Palm boundary rises to about `Lambda~0.91` at moderate/high finite bandwidth. High-band slow-preferred tasks survive above it. Large-`r` Palm optimum broad near `kappa~50–65`, about `0.3–0.4%` above infinity.

## Step 23
Matched rough/smooth finite-window limit and exact occupation-time importance sampling. Direct rough endpoint: `Lambda_cross^infinity~0.905 +/-0.004`; `Lambda=0.895` remains fast-preferred.

## Step 24
Finite bandwidth adds `zeta=kappa/(sqrt(2)u sqrt(b))`. **REJECTED SHORTCUT:** `H_mix(chi)` alone is only the infinite-band endpoint.

## Step 25
Generalized Pickands constant has continuous Dieker–Yakir representation. Brown–Resnick Slepian comparison proves monotonicity in `chi` and `zeta`, but not monotonicity of the physical detector boundary.

## Step 26
Exact implicit physical boundary derivative derived. Finite-hard-window SNR recovery is `O(kappa^-1)`. Positive `H_mix-H~C_H/sqrt(zeta)` would force eventual negative boundary slope.

## Step 27
Common-white-noise coupling gives exact `O(sqrt(chi/zeta))` path-amplitude scale and conservative convergence bound. **INVALIDATED INTERMEDIATE:** `0.8131` coupling coefficient; correct pointwise RMS coefficient is `0.8906480701`. Coupling alone gives no positive lower coefficient.

## Step 28
Two-sided-BES(3) Brownian-extremum zoom-in plus Gaussian mollification identifies a positive `zeta^-1/2` coefficient under stable convergence/localization/UI. Dieker–Yakir denominator is lower order. Quantitative finite-band remainder remains open.

## Step 29
Small `chi` is singular. Brownian–parabola scales `h_chi=sqrt(2)chi^(1/3)`, `m_chi=2chi^(2/3)` give crossover variable `mu=sqrt(2)zeta chi^(1/3)`. At the `r=2` endpoint, `mu_f~0.009776 kappa_f`, `mu_s~0.16139 kappa_f`; slow already in Bessel tail at `100–300`, fast still in crossover. **REFINEMENT:** Step-26 fast `C_H~0.0061` is pre-asymptotic.

## Step 30
Small-`chi` crossover reduces to canonical Brownian-minus-parabola maximum loss

```math
F(mu)=\frac{2}{\sqrt\pi}E[M_inf-M_mu].
```

Continuum-extrapolated values:

```text
mu:       0     .5     1      2      3      5      10     20
F(mu):  .892   .806   .729   .597   .512   .410   .297   .213
```

with `sqrt(mu)F(mu)->~0.98`. Nested-grid full fast-channel calculations agree at percent level. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` fast values were biased low by under-resolving the rough maximum. Fast endpoint asymptotic `C_H` refines to about `0.0088`.

## Step 31 — 21:17 EDT — Palm-anchored universal high-band boundary closure
Insert the canonical fast-channel `F(mu)` bridge into the finite-`u` tangent boundary. Representative tangent shape:

```text
kappa_f      Lambda_tan
60           .88255
100          .88604
200          .88715
300          .88714
1000         .88660
infinity      .88564
```

The absolute tangent boundary has a known finite-`u` rare-event offset. Use Step-22 Palm anchors

```text
kappa_f:      60       100      200
Lambda_Palm: .9098    .9103    .9099
```

and Step-23 central rough endpoint `Lambda_inf=0.90513`. Define `delta=Lambda_exact-Lambda_tan`, fix `delta_inf=0.01949`, and fit the minimal relaxation

```math
delta(kappa)=delta_inf+A kappa^{-p}.
```

Fit:

```text
A ~0.18206
p ~0.77501
```

Central bridge:

```text
kappa_f      Lambda_bridge
60           .90966
80           .91056
100          .91066
130          .91042
160          .91008
200          .90964
300          .90882
500          .90790
1000         .90695
2000         .90632
5000         .90583
10000        .90559
infinity      .90513
```

Dense interpolation gives one shallow maximum near `kappa_f~94.9`, `Lambda~0.91068`, then a strictly decreasing central bridge for `kappa_f>=100`.

**NUMERICAL CLOSURE for original task:** `Lambda=0.895` remains below the whole high-band bridge and the rough endpoint. Even subtracting the previously reported `0.004` endpoint uncertainty gives about `0.9011>0.895`. No bounded high-band re-entrant slow-preferred pocket is numerically supported for this calibration.

**CONDITIONAL / OPEN:** the finite-`u` discrepancy relaxation is empirical, so this is not a theorem-level interval enclosure and does not exclude other topologies for other task parameters.

Full derivation: `UNIVERSAL_BRIDGE_BOUNDARY_CLOSURE_STEP.md`.  
Calculator: `numerics/universal_bridge_boundary.py`.

---

## Current stopping point

For the original `r=2`, `Lambda=0.895` task, the high-band re-entrant pocket is numerically closed. The remaining mathematical gap is the exact finite-`u` correction between the tangent/cluster description and the Palm/occupation boundary.

### Single natural next question

> Can the finite-`u` Palm/occupation discrepancy be derived or bounded directly, replacing the empirical `delta_infinity+A kappa^-p` anchoring with a certified interval enclosure for `Lambda_cross(kappa_f)`?
