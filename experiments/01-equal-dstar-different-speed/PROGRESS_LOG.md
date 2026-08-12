# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 20:57 EDT:** compact chronology preserving consequential results, corrections, rejected shortcuts, invalidations, numerical validations, asymptotic qualifications, and the current stopping point. Full derivations remain in dedicated step files.

---

## Steps 01–04 — scalar `D*`, full-observation equivalence, finite-window phase
Equal scalar reference `D*` does not determine arbitrary temporal-signal SNR; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation problem. **NEGATIVE RESULT:** unknown timing alone does not break that ideal equivalence. Finite windows can because magnitude `D*(f)` discards temporal phase/placement.

## Steps 05–12 — finite records and task boundary
Derived finite-record optimal SNR and task-level detection time. In the controlled `t exp(-t/tau)` family, faster SNR accumulation can be offset by unknown-time search burden. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed directly with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family.

## Step 13 — rough hard-window obstruction
Finite hard-window ideal-white-noise scan has `R_x(y)=1-a_x|y|+...`. **FAILED NUMERICAL ESTIMATE:** rough-grid crossover near `ell~49` invalid.

## Steps 14–17 — finite timing bandwidth and Palm rare events
A genuine information-band limitation removes the cusp. Exact smooth Palm identity is available; Rice/EC is an upper bound. For finite hard windows `sigma_kappa^2~a_x kappa/sqrt(pi)`, so Rice accuracy is nonuniform toward the rough limit.

## Steps 18–19 — common physical bandwidth and finite optimum
With `kappa_i=Omega_B tau_i`, forcing accessible SNR equal gives no finite bandwidth optimum. Holding physical signal/noise fixed restores bandwidth-dependent SNR and produces a finite large-`r` optimum; later Palm work confirms a shallow optimum survives beyond Rice.

## Steps 20–21 — finite-`r` Rice double reversal corrected by Palm
For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=0.90`, `Lambda=0.895`, converged Rice gave apparent switches `25.4898402` and `130.1945883`. Palm preserves only the lower switch:

```math
\kappa_{\times,1}^{Palm}\approx21.7\pm0.3.
```

**INVALIDATED:** upper Rice switch. Palm checks at `130,160,300` keep fast preferred for that slice.

## Step 22 — Palm boundary map and finite optimum
Boundary rises to about `Lambda~0.91` at moderate/high finite bandwidth; high-band slow-preferred tasks survive above it. Large-`r` Palm optimum is broad near `kappa~50–65`, only `~0.3–0.4%` above infinity.

## Step 23 — matched infinite-band rough/smooth limit
Derived finite-window cusp/quadratic local expansion and `chi_x=a_xu/sqrt(b_x)`. Exact occupation-time importance sampling handles `u~5`. Direct rough endpoint gives `Lambda_cross^infinity~0.905 +/-0.004`; `Lambda=0.895` remains fast-preferred.

## Step 24 — finite-band tangent bridge
Finite bandwidth adds `zeta=kappa/(sqrt(2)u sqrt(b))`. **REJECTED SHORTCUT:** `H_mix(chi)` alone is only the `zeta=infinity` endpoint.

## Step 25 — Dieker–Yakir representation and monotonicity
Generalized Pickands constant has continuous Dieker–Yakir form. Brown–Resnick Slepian comparison proves `partial_zeta H>=0` and `partial_chi H>=0`. Local extreme statistics cannot oscillate with bandwidth, but that alone does not make the physical boundary monotone.

## Step 26 — physical high-band derivative
Exact implicit boundary derivative derived. Finite-hard-window SNR recovery is `O(kappa^-1)`. Paired Dieker–Yakir data supported positive `H_mix-H~C_H/sqrt(zeta)`. Conditional on that law, the `r=2` boundary approaches the rough endpoint from above with eventual negative slope.

## Step 27 — exact Gaussian-mollifier coupling scale
Common-white-noise coupling yields

```math
\sup_t SD[W_\infty-W_\zeta]_{random}
\le0.8906480701\sqrt{\chi/\zeta}.
```

**INVALIDATED INTERMEDIATE:** `0.8131` used the large-lag variance instead of the true maximum. Conservative convergence envelope `0<=H_mix-H<=C_chi sqrt(log zeta/zeta)`. Paired simulations resolve positive square-root scaling but do not alone prove a positive lower coefficient.

## Step 28 — Bessel zoom-in positive coefficient
Under stable Brownian-extremum zoom-in/localization/UI,

```math
H_mix(chi)-H(chi,zeta)
=C_H(chi) zeta^-1/2+o(zeta^-1/2),
```

with positive kernel-specific `C_H`. The Dieker–Yakir denominator is lower order. **REJECTED SHORTCUT:** do not factor the weighted Bessel expectation without independence. Finite onset bandwidth still requires quantitative control.

## Step 29 — Brownian–parabola double scaling
Small `chi` introduces

```math
h_chi=sqrt(2) chi^(1/3),
qquad
m_chi=2 chi^(2/3),
```

so the correct crossover coordinate is

```math
mu=sqrt(2) zeta chi^(1/3).
```

Natural form `H_mix-H=chi^(2/3)F(mu)+...`, with `F(mu)~A_K/sqrt(mu)`. At the `r=2` endpoint,

```math
mu_f~0.009776 kappa_f,
qquad
mu_s~0.16139 kappa_f.
```

Slow is already in the Bessel tail at `kappa_f~100–300`; fast is still in crossover. **REFINEMENT:** Step-26 fast `C_H~0.0061` is a crossover effective coefficient, not final asymptotic.

## Step 30 — 20:57 EDT — universal Brownian–parabola crossover function
The small-`chi` crossover can be simulated without the detector field. Define

```math
Y_inf(s)=B(s)-s^2,
```

and obtain `B_mu` by Gaussian filtering the white derivative with amplitude transfer `exp[-q^2/(8 mu^2)]`. Let

```math
M_inf=sup_s[B(s)-s^2],
qquad
M_mu=sup_s[B_mu(s)-s^2].
```

Because the pure quadratic Dieker–Yakir ratio is exactly `1/sqrt(pi)`, the universal function is

```math
\boxed{
F(mu)=\frac{2}{\sqrt\pi}E[M_inf-M_mu].
}
```

Endpoint/tail:

```text
F(0) ~0.892
F(mu) ~ A_K/sqrt(mu), A_K~0.98
```

using the Step-28 canonical BES diagnostic.

Continuum-extrapolated canonical values:

```text
mu:       0     .5     1      2      3      5      10     20
F(mu):  .892   .806   .729   .597   .512   .410   .297   .213
```

The rough maximum has `O(sqrt(ds))` discretization bias. Nested-grid continuum extrapolation is therefore mandatory.

**NUMERICAL VALIDATION / INVALIDATED NUMERICAL INTERPRETATION:** full fast-channel paired Dieker–Yakir gaps, re-evaluated on nested grids and extrapolated in `sqrt(dt)`, agree with the canonical function at the percent level:

```text
zeta=20, mu=1.371: F_full~0.675 vs canonical~0.68
zeta=40, mu=2.743: F_full~0.531 vs canonical~0.53
zeta=80, mu=5.485: F_full~0.394 vs canonical~0.40
```

The original raw Step-27/29 fast values `~0.551,0.438,0.324` were biased low by rough-maximum grid under-resolution and must not be treated as continuum `F(mu)` data. Step 29's scaling variable remains valid.

Universal bridge:

```math
C_H,eff=2^{-1/4}\sqrt\chi\,\sqrt\mu F(mu).
```

For the fast endpoint `chi_f~1.1395e-4`, the Bessel-tail limit is `C_H,fast~0.0088`, not the pre-asymptotic `~0.0061`. Holding the other Step-26 surrogate inputs fixed moves illustrative `C_Lambda` from `~0.020` to `~0.032`; sign remains positive and is strengthened.

Full derivation: `UNIVERSAL_CROSSOVER_FUNCTION_STEP.md`.  
Calculator: `numerics/universal_crossover_function.py`.

---

## Current stopping point

The difficult small-`chi` fast-channel bandwidth dependence is now represented by one reusable canonical function rather than full detector Monte Carlo.

### Single natural next question

> If the universal `F(mu)` bridge is inserted into the coupled finite-`r` boundary equation, does the corrected boundary remain monotone from the mapped Palm high-band region into the rough endpoint, eliminating the last plausible bounded re-entrant pocket without full-process Monte Carlo at every bandwidth?
