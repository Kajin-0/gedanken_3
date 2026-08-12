# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 20:57 EDT  
**Status:** thirty logical steps completed. Step 30 derives a detector-independent small-`chi` Brownian-minus-parabola/Gaussian-mollifier crossover function `F(mu)=(2/sqrt(pi)) E[M_inf-M_mu]`. Continuum-extrapolated canonical simulations reproduce independently refined full fast-channel Dieker–Yakir gaps at the percent level. This exposes a numerical-resolution bias in the raw Step-27 tiny-`chi` fast points: the Brownian endpoint maximum was under-resolved on the shrinking `h_chi` scale. Step 29's `mu` scaling remains valid, but those raw fast values are not continuum crossover values. The universal bridge yields a refined fast asymptotic `C_H~0.0088` rather than the pre-asymptotic `~0.0061` used in Step 26, strengthening the eventual negative high-band boundary coefficient sign. No finite certified onset bandwidth, universal replacement metric, or novelty claim.

---

## 1. Original question

Two hypothetical detectors satisfy

```math
D_A^*=D_B^*
```

but have radically different temporal responses, initially

```math
\tau_A=1\,ns,
\qquad
\tau_B=1\,s.
```

Does equal conventional specific detectivity imply equal ability to detect an arbitrary optical signal?

---

## 2. Surviving logical chain

### Steps 01–04 — scalar / magnitude-only `D*`
Equal scalar reference `D*` does not guarantee equal arbitrary temporal-signal SNR; an explicit 1 Hz example gave `SNR_A/SNR_B~6.36`. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation maximum-linear-SNR problem. **NEGATIVE RESULT:** unknown timing alone does not break that ideal stationary-Gaussian equivalence. Finite observation can because magnitude `D*(f)` discards temporal phase/placement.

### Steps 05–12 — finite records and task-level timing search

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
```

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

For the controlled `t exp(-t/tau)` family, faster SNR accumulation can be offset by larger unknown-time search burden. **REJECTED SHORTCUT:** finite-window SNR cannot be combined directly with full-template timing bandwidth as one exact finite-deadline statistic. **NEGATIVE RESULT:** no finite interior integration-duration optimum exists in the original scaled family.

### Step 13 — rough hard-window obstruction

```math
R_x(y)=1-a_x|y|+O(y^2).
```

Ideal-white-noise finite hard-window scans are locally Brownian-like. **FAILED NUMERICAL ESTIMATE:** the rough-grid crossover near `ell~49` moved under grid refinement and is invalid.

### Steps 14–17 — genuine timing bandwidth and exact rare events
Use smooth information weighting `|H_x(nu)|^2 exp[-(nu/kappa)^2]`. Finite `kappa` removes the cusp. Exact smooth Palm identity:

```math
P_FA=Q(u)+\lambda_u E_\uparrow[1_{z(0)\le u}/N_u^+].
```

Rice/EC is an upper bound. For finite hard windows,

```math
\sigma_\kappa^2\sim a_x\kappa/\sqrt\pi,
```

so Rice accuracy is nonuniform as `kappa -> infinity`.

### Steps 18–19 — shared physical bandwidth and true finite optimum
Use `kappa_i=Omega_B tau_i`. Artificially forcing accessible eventual SNR equal gives electronics- and detector-limited regimes but **no** finite bandwidth optimum. Holding physical signal/noise fixed restores bandwidth-dependent SNR. For the full template, SNR loss is `O(kappa^-2)` while search simplification is `O(kappa^-1)`, giving a finite large-`r` optimum. Later Palm work confirms a shallow finite optimum survives beyond Rice.

### Steps 20–21 — finite-`r` Rice double reversal corrected by Palm
For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=0.90`, `Lambda=0.895`, converged Rice gave apparent switches `25.4898402` and `130.1945883`. Palm correction preserves only the lower switch:

```math
\kappa_{\times,1}^{Palm}\approx21.7\pm0.3.
```

The upper Rice switch is **INVALIDATED**. Direct Palm checks at `kappa_f=130,160,300` keep fast preferred for `Lambda=0.895`.

### Step 22 — Palm boundary map and Palm finite optimum
Representative finite-`r` Palm boundary:

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

High-band slow-preferred tasks survive above the lifted boundary. The large-`r` full-template Palm objective has a broad finite optimum near `kappa~50–65`, only `~0.3–0.4%` above infinity.

### Step 23 — matched rough/smooth infinite-band limit

```math
R_x(y)=1-a_x|y|-\frac{b_x}{2}y^2+O(|y|^3),
\qquad
\chi_x=a_xu/\sqrt{b_x}.
```

At `kappa=infinity`, tangent variance is `t^2+sqrt(2) chi |t|`. Because `u~5`, leading high-threshold asymptotics are insufficient. Exact occupation-time identity:

```math
P(\sup z>u)=\ell Q(u)E_{occ}[1/V_u].
```

Direct rough-limit calculation gives

```math
\Lambda_{cross}^{\infty}\approx0.905\pm0.004,
\qquad X\approx7.75.
```

Thus `Lambda=0.895` is fast-preferred at the direct rough endpoint too.

### Step 24 — finite-band tangent bridge is two-parameter
Finite bandwidth introduces

```math
\zeta_x=\kappa/(\sqrt2u\sqrt{b_x}).
```

The two-parameter tangent variogram connects smooth finite-band and rough infinite-band fields. **REJECTED SHORTCUT:** `H_mix(chi)` alone is only the `zeta=infinity` endpoint.

### Step 25 — generalized Dieker–Yakir evaluation and monotonicity

```math
H(\chi,\zeta)=E[\sup e^W/\int e^W].
```

Efficient simulation uses FFT synthesis of a stationary Gaussian derivative and one integration. Brown–Resnick Slepian comparison gives

```math
\partial_\zeta H\ge0,
\qquad
\partial_\chi H\ge0.
```

The local extreme constant cannot oscillate with bandwidth, but this alone does not make the physical fast/slow boundary monotone.

### Step 26 — physical high-band derivative
For physical admissible timing intervals `A_f,A_s`, exact implicit differentiation gives

```math
\frac{d\Lambda_\times}{d\kappa}
=\frac{A_{f,X}A_{s,\kappa}-A_{s,X}A_{f,\kappa}}
{A_{f,X}-A_{s,X}}.
```

Finite-hard-window SNR recovery is `O(kappa^-1)`. Paired Dieker–Yakir data indicated `H_mix-H ~ C_H/sqrt(zeta)`. Conditional on a positive coefficient, the `r=2` boundary approaches the rough endpoint from above with eventual negative slope.

### Step 27 — exact Gaussian-mollifier coupling scale
Use one white-noise field for rough and smoothed endpoints. Exact coupled residual variance gives

```math
\sup_t SD[W_\infty-W_\zeta]_{random}
\le0.8906480701\sqrt{\chi/\zeta}.
```

**INVALIDATED INTERMEDIATE:** `0.8131` used the large-lag variance instead of the true maximum. A conservative fixed-window bound gives `0 <= H_mix-H <= C_chi sqrt(log zeta/zeta)`. Paired common-random-number calculations sharply resolve the positive correction but do not by themselves prove a positive lower coefficient.

### Step 28 — two-sided-Bessel Gaussian-mollifier correction
Under standard Brownian-extremum stable zoom-in/localization/UI assumptions,

```math
H_{mix}(\chi)-H(\chi,\zeta)
=C_H(\chi)\zeta^{-1/2}+o(\zeta^{-1/2}),
```

with

```math
C_H(\chi)=2^{3/4}\sqrt\chi\,E[\Psi(W_\infty)\mathcal M_K(R_*)]>0.
```

The integrated Dieker–Yakir denominator perturbation is lower order. **REJECTED SHORTCUT:** do not factor the weighted expectation without an independence theorem. A finite certified onset bandwidth still requires quantitative remainder control.

### Step 29 — Brownian–parabola double scaling
The fixed-`chi` Step-28 expansion is singular as `chi -> 0`. Around the smooth quadratic maximum,

```math
\boxed{
h_\chi=\sqrt2\chi^{1/3},
\qquad m_\chi=2\chi^{2/3}.}
```

Gaussian smoothing is controlled by

```math
\boxed{
\mu=\zeta h_\chi=\sqrt2\zeta\chi^{1/3}.}
```

Natural joint scaling:

```math
H_{mix}(\chi)-H(\chi,\zeta)
=\chi^{2/3}\mathcal F(\mu)+o(\chi^{2/3}),
```

with `F(mu)~A_K mu^-1/2` for large `mu`. At the `r=2` endpoint,

```math
\mu_f\approx0.009776\kappa_f,
\qquad
\mu_s\approx0.16139\kappa_f.
```

Thus the slow channel is already in the Bessel tail at mapped high bandwidths while the tiny-`chi` fast channel is still in crossover through `kappa_f=300`. **REFINEMENT:** Step-26 fast `C_H~0.006` is a crossover effective coefficient, not a clean fixed-`chi` endpoint coefficient.

### Step 30 — universal Brownian–parabola crossover function
On the Step-29 local coordinate,

```math
Y_\infty(s)=B(s)-s^2,
```

and finite smoothing filters the white derivative of `B` with amplitude transfer

```math
e^{-q^2/(8\mu^2)}.
```

Let

```math
M_\infty=\sup_s[B(s)-s^2],
\qquad
M_\mu=\sup_s[B_\mu(s)-s^2].
```

Because the pure quadratic Dieker–Yakir ratio is exactly `1/sqrt(pi)`, the small-`chi` crossover reduces to

```math
\boxed{
\mathcal F(\mu)
=\frac{2}{\sqrt\pi}E[M_\infty-M_\mu].
}
```

This is detector-independent. Endpoint and tail:

```math
F(0)=\frac{2}{\sqrt\pi}E[M_\infty]\approx0.892,
```

```math
F(\mu)\sim A_K/\sqrt\mu,
\qquad
A_K=(2/\sqrt\pi)E[M_K]\approx0.98
```

using the Step-28 unweighted canonical BES diagnostic `E[M_K]~0.87`.

Continuum-extrapolated canonical estimates:

```text
mu        F(mu)      sqrt(mu)F
0         ~0.892      --
0.5       ~0.806      ~0.570
1         ~0.729      ~0.729
2         ~0.597      ~0.844
3         ~0.512      ~0.886
5         ~0.410      ~0.917
10        ~0.297      ~0.939
20        ~0.213      ~0.955
infinity   --         ~0.98
```

The rough endpoint maximum has `O(sqrt(ds))` discretization bias, so Step 30 uses nested grids and extrapolates linearly in `sqrt(ds)`.

**NUMERICAL VALIDATION / CORRECTION:** refining the full fast-channel paired Dieker–Yakir calculation in the same way gives

```text
zeta    mu      F_full,extrap   F_canonical
20      1.371       ~0.675         ~0.68
40      2.743       ~0.531         ~0.53
80      5.485       ~0.394         ~0.40
```

The original raw Step-27/29 fast values `~0.551,0.438,0.324` were biased low because the rough maximum was under-resolved on the shrinking `h_chi` scale. **INVALIDATED NUMERICAL INTERPRETATION:** do not use those raw fast values as continuum `F(mu)` points. Step 29's scaling variable remains valid.

The universal bridge gives

```math
C_{H,eff}=2^{-1/4}\sqrt\chi\,\sqrt\mu F(\mu),
```

so for `chi_f~1.1395e-4`,

```text
C_H,fast(infinity) ~0.0088,
```

rather than the pre-asymptotic `~0.0061` used in Step 26. Holding the other Step-26 surrogate inputs fixed moves the illustrative `C_Lambda` from `~0.020` to `~0.032`; the sign remains positive and is strengthened, but this is still not a finite-`K` proof.

See `UNIVERSAL_CROSSOVER_FUNCTION_STEP.md` and `numerics/universal_crossover_function.py`.

---

## 3. Current frontier

The difficult small-`chi` fast-channel finite-band correction is now separated from the full detector process through a reusable one-dimensional function `F(mu)` and validated against refined full-field calculations.

### Single next question — DO NOT ANSWER YET

> If the universal `F(mu)` bridge is inserted into the coupled finite-`r` boundary equation, does the corrected boundary remain monotone on the entire high-band interval from the existing Palm map into the rough endpoint, thereby eliminating the last plausible bounded re-entrant pocket without requiring full-process Monte Carlo at every bandwidth?

---

## 4. Scope boundary

Do not claim:
- faster detectors are universally better or worse;
- a universal speed-detectivity tradeoff or scalar replacement for `D*`;
- Step-13 `ell~49` is valid;
- arbitrary low-pass filtering is a true information-band limitation;
- Gaussian information weighting is a literal circuit transfer function;
- Rice is uniformly accurate at high finite-window bandwidth;
- Step-20 double reversal is exact;
- monotonic `H(chi,zeta)` alone proves monotonic detector preference;
- Step-28 is quantitatively uniform in `chi` at moderate `zeta`;
- the raw Step-27 tiny-`chi` fast points are continuum crossover values;
- Step-26 fast `C_H~0.0061` is the final asymptotic coefficient;
- the universal crossover table is an exact analytic evaluation;
- a finite certified onset bandwidth is known;
- no bounded pre-asymptotic pocket exists yet;
- the Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.
