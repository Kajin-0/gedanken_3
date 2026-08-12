# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 20:40 EDT:** compact chronology preserving every consequential result, correction, rejected shortcut, invalidation, numerical validation, asymptotic qualification, and current stopping point. Full derivations remain in dedicated step files.

---

## Steps 01–04 — scalar `D*`, full-observation equivalence, finite-window phase
Equal scalar reference `D*` does not determine arbitrary temporal-signal SNR; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation maximum-linear-SNR problem. **NEGATIVE RESULT:** unknown timing alone does not break that ideal equivalence. Finite windows can because magnitude `D*(f)` discards temporal phase/placement.

## Steps 05–12 — finite-record SNR and task boundary
Derived finite-record optimal SNR and task-level detection time

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

In the controlled `t exp(-t/tau)` family, faster SNR accumulation can be offset by unknown-time search burden. **REJECTED SHORTCUT:** finite-window SNR cannot be combined directly with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family.

## Step 13 — rough hard-window obstruction
Finite hard-window ideal-white-noise timing scan has `R_x(y)=1-a_x|y|+...`. **FAILED NUMERICAL ESTIMATE:** rough-grid crossover `ell~49` invalid.

## Steps 14–17 — finite timing-information bandwidth and Palm rare events
A genuine information-band limitation removes the cusp. Exact smooth Palm identity:

```math
P_FA=Q(u)+\lambda_u E_\uparrow[1_{z(0)\le u}/N_u^+].
```

Rice/EC is an upper bound. For finite hard windows `sigma_kappa^2~a_x kappa/sqrt(pi)`, so Rice accuracy is nonuniform toward the rough limit.

## Step 18 — common physical bandwidth, accessible SNR forced equal
With `kappa_i=Omega_B tau_i`, crossover moves from electronics-limited `~1/Omega_B` to detector-limited `~tau_f`. **NEGATIVE RESULT:** no finite bandwidth optimum under artificial equal-accessible-SNR normalization.

## Step 19 — fixed physical signal/noise; finite bandwidth optimum
Restoring bandwidth-dependent accessible SNR gives full-template SNR loss `O(kappa^-2)` but timing-search simplification `O(kappa^-1)`. A finite large-`r` optimum appears; later Palm validation confirms a shallow optimum survives beyond Rice.

## Step 20 — finite-`r` Rice double reversal
For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=0.90`, `Lambda=0.895`, converged Rice gave apparent switches `25.4898402` and `130.1945883`.

## Step 21 — Palm correction changes topology
Lower switch survives at `kappa_f~21.7 +/-0.3`. **INVALIDATED:** upper Rice switch `130.1945883` is not a Palm switch. Palm checks at `130,160,300` keep fast preferred for `Lambda=0.895`.

## Step 22 — Palm boundary map and finite optimum
Representative finite-`r` boundary:

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

High-band slow-preferred tasks survive above the lifted boundary. Large-`r` Palm optimum is broad near `kappa~50–65`, about `0.3–0.4%` above infinity.

## Step 23 — matched rough/smooth infinite-band limit
Derived `R_x(y)=1-a_x|y|-b_x y^2/2+...` and `chi_x=a_xu/sqrt(b_x)`. At `kappa=infinity`, tangent variance is `t^2+sqrt(2)chi|t|`. At `u~5`, introduced exact occupation-time rare-event identity

```math
P(\sup z>u)=\ell Q(u)E_{occ}[1/V_u].
```

Direct rough-limit boundary for `r=2` is `Lambda_cross^infinity~0.905 +/-0.004`, `X~7.75`; therefore `Lambda=0.895` remains fast-preferred at the endpoint.

## Step 24 — finite-band tangent bridge is two-parameter
Finite bandwidth adds `zeta=kappa/(sqrt(2)u sqrt(b))`. The tangent variogram connects smooth finite-band and rough infinite-band fields. **REJECTED SHORTCUT:** `H_mix(chi)` alone cannot control finite-band convergence.

## Step 25 — generalized Dieker–Yakir representation and monotonicity

```math
H(\chi,\zeta)=E[\sup e^W/\int e^W].
```

Efficient simulation uses FFT synthesis of a stationary Gaussian derivative followed by integration. Brown–Resnick Slepian comparison gives `partial_zeta H>=0`, `partial_chi H>=0`. Local extreme statistics cannot oscillate with bandwidth, but this alone does not prove the physical boundary monotone.

## Step 26 — physical high-band derivative
Exact implicit derivative:

```math
\frac{d\Lambda_\times}{d\kappa}
=\frac{A_{f,X}A_{s,\kappa}-A_{s,X}A_{f,\kappa}}
{A_{f,X}-A_{s,X}}.
```

Finite-hard-window SNR recovery is `O(kappa^-1)`. Paired Dieker–Yakir data supported `H_mix-H~C_H/sqrt(zeta)`. Conditional on positive coefficient, the `r=2` boundary approaches the rough endpoint from above with eventual negative slope.

## Step 27 — exact Gaussian-mollifier coupling scale
Common-white-noise Gaussian smoothing uses

```math
K_\zeta(t)=\sqrt2\zeta/\sqrt\pi\;e^{-2\zeta^2t^2}.
```

Exact coupled residual variance yields

```math
\sup_t SD[W_\infty-W_\zeta]_{random}
\le0.8906480701\sqrt{\chi/\zeta}.
```

**INVALIDATED INTERMEDIATE:** `0.8131` used the large-lag variance instead of the true supremum. Conservative convergence envelope: `0<=H_mix-H<=C_chi sqrt(log zeta/zeta)`. Paired simulations sharply resolve positive square-root scaling, but the coupling alone supplies no positive lower coefficient.

## Step 28 — Bessel zoom-in identifies a positive mollifier coefficient
With `sigma_chi=2^(3/4)sqrt(chi)`, Brownian-extremum zoom-in around the unique rough-field maximum gives a two-sided BES(3)-type local field. Gaussian smoothing acts through `K_1(s)=sqrt(2/pi) exp(-2s^2)`. The local mollifier functional

```math
M_K(R)=inf_u integral K_1(v)R(u-v)dv
```

is positive almost surely. The integrated Dieker–Yakir denominator perturbation is lower order under the stationary high-pass coupling. Under stable convergence/localization/UI,

```math
H_mix(chi)-H(chi,zeta)
=C_H(chi) zeta^-1/2+o(zeta^-1/2),
```

with

```math
C_H(chi)=2^(3/4)sqrt(chi) E[Psi(W_inf) M_K(R_*)]>0.
```

**REJECTED SHORTCUT:** do not factor the weighted expectation without an independence theorem. **OPEN:** quantitative uniform remainder / finite onset bandwidth.

## Step 29 — 20:40 EDT — Brownian–parabola double scaling exposes the correct uniformity variable
The Step-28 fixed-`chi` asymptotic is singular as `chi -> 0`. Around the smooth quadratic maximum, Brownian fluctuation `sigma_chi sqrt(h)` balances parabolic drop `h^2` at

```math
\boxed{h_\chi=\sqrt2\chi^{1/3}},
```

with height scale

```math
\boxed{m_\chi=2\chi^{2/3}}.
```

Therefore Gaussian smoothing is controlled by

```math
\boxed{\mu=\zeta h_\chi=\sqrt2\zeta\chi^{1/3}},
```

not by raw `zeta` alone.

Natural double-scaling form:

```math
H_mix(\chi)-H(\chi,\zeta)
=\chi^{2/3} F(\mu)+o(\chi^{2/3}),
```

with `F(mu)~A_K mu^-1/2` for `mu->infinity`, recovering Step 28.

**NUMERICAL COLLAPSE:** Step-27 paired data expressed as `Delta H/chi^(2/3)` versus `mu` form one continuous crossover. For the slow endpoint and `chi=0.1`, `sqrt(mu)F_emp` is already approximately constant near one for `mu~10–50`. The fast endpoint values at `mu=1.37,2.74,5.49` remain visibly pre-asymptotic.

At the `r=2` rough-endpoint trajectory,

```math
\boxed{
\mu_f\approx0.009776\kappa_f,
\qquad
\mu_s\approx0.16139\kappa_f.}
```

Thus

```text
kappa_f=100: mu_f~0.98, mu_s~16.1
kappa_f=200: mu_f~1.96, mu_s~32.3
kappa_f=300: mu_f~2.93, mu_s~48.4
```

The slow channel is already in the Bessel tail, while the fast channel is still in the Brownian-parabola crossover. **REFINEMENT:** the Step-26 fast `C_H~0.006` measured from `zeta<=80` is a crossover effective coefficient, not the final fixed-`chi` asymptotic coefficient. This does not invalidate the eventual sign; it means the numerical asymptotic onset is later than previously implied.

The natural relative remainder scale is `mu^-1/2`, because the smooth-background correction `chi^(1/3)/zeta` divided by the leading `sqrt(chi/zeta)` term is `1/sqrt(zeta chi^(1/3))`.

Full derivation: `BROWNIAN_PARABOLA_DOUBLE_SCALING_STEP.md`.  
Calculator: `numerics/double_scaling_crossover.py`.

---

## Current stopping point

A uniform-in-raw-`zeta` remainder is the wrong target for the difficult small-`chi` fast channel. The correct reduced problem is a one-dimensional Brownian-minus-parabola/Gaussian-mollifier crossover function `F(mu)`.

### Single natural next question

> Can `F(mu)` be computed directly from the universal Brownian-minus-parabola local process, without full detector simulation, and can it provide a one-dimensional envelope from crossover through the Bessel tail strong enough to close the remaining high-band interval?
