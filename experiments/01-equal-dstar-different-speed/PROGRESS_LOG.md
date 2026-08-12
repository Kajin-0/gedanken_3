# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 20:09 EDT:** compact chronology preserving every consequential result, correction, rejected shortcut, invalidation, numerical validation, asymptotic qualification, and stopping point. Full derivations live in dedicated step files.

---

## Steps 01–04 — scalar `D*`, full-observation equivalence, finite-window phase
Equal scalar reference `D*` does not determine arbitrary temporal-signal SNR; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation maximum-linear-SNR problem. **NEGATIVE RESULT:** unknown timing alone does not break that ideal equivalence. Finite windows can because magnitude `D*(f)` discards phase/temporal placement.

## Steps 05–12 — finite-record SNR, deadline detection, and task boundary
Derived `rho_t^2=<s_t,C_t^-1s_t>`, Gaussian deadline detection, and task-level `T_D(alpha,beta,L)`. In the controlled `t exp(-t/tau)` family, faster SNR accumulation can be offset by larger unknown-time search burden.

**REJECTED SHORTCUT:** finite-window SNR cannot be combined directly with full-template timing bandwidth.

**NEGATIVE RESULT:** no finite interior integration-duration optimum exists in the original scaled family.

## Step 13 — rough finite-window obstruction
`R_x(y)=1-a_x|y|+...`; ideal-white-noise hard-window scan is locally Brownian-like.

**FAILED NUMERICAL ESTIMATE:** Step-13 `ell~49` crossover is invalid.

## Steps 14–17 — genuine timing bandwidth and exact Palm rare events
A genuine information-band limitation removes the cusp. Exact smooth Palm identity:

```math
P_{FA}=Q(u)+\lambda_u E_\uparrow[1_{z(0)\le u}/N_u^+].
```

Rice/EC is an upper bound. For finite hard windows `sigma_kappa^2~a_x kappa/sqrt(pi)`, so Rice accuracy is nonuniform as bandwidth grows.

## Step 18 — common physical bandwidth, accessible SNR forced equal
With `kappa_i=Omega_B tau_i`, crossover moves from electronics-limited `~1/Omega_B` to detector-limited `~tau_f`.

**NEGATIVE RESULT:** no finite bandwidth optimum under artificial equal-accessible-SNR normalization.

## Step 19 — fixed physical signal/noise; finite bandwidth optimum
Restoring bandwidth-dependent accessible SNR gives full-template SNR loss `O(1/kappa^2)` but timing-search simplification `O(1/kappa)`.

**DERIVED / CONDITIONAL:** large-r objective has a finite bandwidth optimum. Later Palm validation confirms survival beyond Rice.

## Step 20 — finite-r Rice double reversal
For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=0.90`, `Lambda=0.895`, converged Rice gave apparent switches `25.4898402` and `130.1945883`.

## Step 21 — Palm correction changes topology
- lower switch survives at `kappa_f~21.7 +/-0.3`;
- **INVALIDATED:** upper Rice switch `130.1945883` is not a Palm switch;
- Palm checks at `130,160,300` keep fast preferred for `Lambda=0.895`.

## Step 22 — Palm boundary map and survival of finite optimum
Representative finite-r boundary:

```text
kappa_f     Lambda_cross^Palm
~10         ~0.794
~20         ~0.891
21.7         0.895
30          ~0.9052
60          ~0.9098
100         ~0.9103
200         ~0.9099
```

**REFINEMENT:** high-band slow-preferred tasks survive above the lifted boundary.

Large-r Palm scan has a shallow finite optimum near `kappa~50–65`, about `0.3–0.4%` above infinity.

## Step 23 — matched infinite-band rough/smooth limit
Derived exact local expansion `R_x(y)=1-a_x|y|-b_x y^2/2+...` and matching coordinate `chi_x=a_xu/sqrt(b_x)`. At `kappa=infinity`, tangent variance is `t^2+sqrt(2)chi|t|`.

Because `u~5`, introduced exact occupation-time rare-event identity

```math
P(\sup z>u)=\ell Q(u)E_{occ}[1/V_u].
```

Direct rough-limit boundary for the `r=2` calibration:

```math
\Lambda_{cross}^{\infty}\approx0.905\pm0.004,
\qquad X\approx7.75.
```

Thus `Lambda=0.895` stays fast-preferred at the rough endpoint.

## Step 24 — finite-band tangent bridge is two-parameter
Finite bandwidth adds

```math
\zeta_x=\kappa/(\sqrt2u\sqrt{b_x}).
```

The two-parameter tangent variogram connects the smooth finite-band and rough infinite-band fields.

**REJECTED SHORTCUT:** `H_mix(chi)` alone cannot control finite-band convergence.

## Step 25 — generalized Dieker–Yakir representation and exact monotonicity
The generalized Pickands constant has

```math
H(\chi,\zeta)=E[\sup e^W/\int e^W].
```

Efficient simulation uses FFT synthesis of a stationary Gaussian derivative followed by integration.

Brown–Resnick Slepian comparison gives

```math
\partial_\zeta H\ge0,
\qquad
\partial_\chi H\ge0.
```

**REFINEMENT:** local extreme statistics cannot oscillate with bandwidth. Any re-entrant detector preference must arise from the coupled physical trajectory.

## Step 26 — coupled high-band physical derivative
For physical admissible search intervals `A_f,A_s`, exact implicit differentiation gives

```math
\frac{d\Lambda_\times}{d\kappa}
=\frac{A_{f,X}A_{s,\kappa}-A_{s,X}A_{f,\kappa}}
{A_{f,X}-A_{s,X}}.
```

Finite-hard-window endpoint leakage gives

```math
\rho(x,\kappa)
=\rho_\infty(x)[1-a_x/(\sqrt\pi\kappa)+o(\kappa^{-1})],
```

so SNR recovery is `O(kappa^-1)`.

Dieker–Yakir data support

```math
H_{mix}(\chi)-H(\chi,\zeta)
\approx C_H(\chi)\zeta^{-1/2},
```

with positive coefficient. Conditional on that law,

```math
\Lambda_\times(\kappa_f)
=\Lambda_\infty+C_\Lambda\kappa_f^{-1/2}+O(\kappa_f^{-1}),
```

and the `r=2` finite-u tangent surrogate gives `C_Lambda>0`, hence eventual negative high-band boundary slope.

**OPEN:** prove the square-root smoothing law and uniform remainder.

## Step 27 — 20:09 EDT — exact Gaussian-mollifier coupling scale
Construct `B_infinity` and `B_zeta` from the same white noise. Gaussian smoothing has amplitude transfer

```math
e^{-\omega^2/(8\zeta^2)}
```

and kernel

```math
K_\zeta(t)=\sqrt2\zeta/\sqrt\pi\;e^{-2\zeta^2t^2}.
```

Exact deterministic gap:

```math
0\le|t|-F_\zeta(t)\le1/(\sqrt\pi\zeta).
```

For `D_zeta=B_infinity-B_zeta`,

```math
\operatorname{Var}D_\zeta(t)
=\zeta^{-1}v(\zeta|t|),
```

with

```text
s_*    = 0.7016406021...
v_max  = 0.2804576359...
```

so the random Brown–Resnick spectral-field perturbation satisfies

```math
\boxed{
\sup_t SD[W_\infty-W_\zeta]_{random}
\le0.8906480701\sqrt{\chi/\zeta}.
}
```

**INVALIDATED INTERMEDIATE:** an earlier same-turn coefficient `0.8131` used the large-lag variance instead of the true supremum.

A fixed-window Gaussian maximal bound plus multiplicative stability of the Dieker–Yakir ratio gives the conservative endpoint convergence envelope

```math
0\le H_{mix}(\chi)-H(\chi,\zeta)
\le C_\chi\sqrt{\log\zeta/\zeta}.
```

A paired common-random-number Dieker–Yakir estimator greatly reduces the variance of the small difference. Representative normalized gaps `sqrt(zeta)[H_mix-H]`:

```text
chi_fast ~1.14e-4:
  zeta 20: 0.00579 +/-0.00005
  zeta 40: 0.00651 +/-0.00004
  zeta 80: 0.00681 +/-0.00006

chi_slow ~0.0645:
  zeta 20: 0.2037 +/-0.0015
  zeta 40: 0.2072 +/-0.0014
  zeta 80: 0.2116 +/-0.0021

chi=0.1:
  zeta 20: 0.2757 +/-0.0021
  zeta 40: 0.2760 +/-0.0021
  zeta 80: 0.2783 +/-0.0028
```

**NUMERICAL VALIDATION / NUMERICAL ASYMPTOTIC:** the positive square-root correction is now sharply resolved and has an exact `O(sqrt(chi/zeta))` path-amplitude origin.

**NEGATIVE RESULT:** the coupling supplies an upper scale, not a positive lower asymptotic coefficient. It therefore does not yet certify a finite exact `K` beyond which the detector boundary is guaranteed monotone decreasing.

The classical Brownian-grid literature rigorously gives `sqrt(delta)` continuity corrections and a two-sided-Bessel zoom-in process around extrema, but Gaussian mollification is a different approximation and cannot inherit that theorem without adaptation.

Full derivation: `GAUSSIAN_MOLLIFIER_COUPLING_STEP.md`.  
Calculator: `numerics/gaussian_mollifier_coupling.py`.

---

## Current stopping point

The square-root perturbation **scale** is now exact and the positive Pickands correction is strongly validated with paired simulation. The missing ingredient is a Brownian-extremum continuity-correction theorem for Gaussian convolution, strong enough to supply a positive lower coefficient and uniform remainder.

### Single natural next question

> Can the Brownian-extremum zoom-in / two-sided-Bessel theorem be adapted from grid discretization to Gaussian mollification of the Dieker–Yakir spectral field, yielding a positive kernel-specific continuity-correction constant `C_H(chi)` and finally converting the Step-26 eventual negative slope into a theorem with a finite certified onset bandwidth?
