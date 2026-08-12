# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 20:40 EDT  
**Status:** twenty-nine logical steps completed. Step 29 shows that the Step-28 Gaussian-mollifier/Bessel asymptotic is not quantitatively uniform in raw `zeta` when `chi` is small. The mixed rough/smooth endpoint has a Brownian-minus-parabola width `h_chi=sqrt(2) chi^(1/3)` and height `2 chi^(2/3)`, so the correct finite-band crossover coordinate is `mu=sqrt(2) zeta chi^(1/3)`. Step-27 paired data collapse strongly in these variables. For the `r=2` endpoint trajectory, the slow channel is already in the large-`mu` Bessel regime at the mapped high bandwidths, while the tiny-`chi` fast channel remains in crossover through `kappa_f=300`. This refines the numerical interpretation of Step 26 but does not invalidate its eventual fixed-`chi` sign. No finite certified onset bandwidth, universal replacement metric, or novelty claim.

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

### Steps 01–04 — limits of scalar and magnitude-only `D*`
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
For

```text
r=2, rho_full=6.2407571, alpha=1e-6, beta=0.90, Lambda=0.895
```

converged Rice gave apparent switches `25.4898402` and `130.1945883`. Palm correction preserves only the lower switch:

```math
\kappa_{\times,1}^{Palm}\approx21.7\pm0.3.
```

The upper Rice switch is **INVALIDATED**. Direct Palm checks at `kappa_f=130,160,300` keep fast preferred for `Lambda=0.895`.

### Step 22 — Palm boundary map and Palm bandwidth optimum
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
Use one white-noise field for rough and smoothed endpoints. The kernel is

```math
K_\zeta(t)=\sqrt2\zeta/\sqrt\pi\;e^{-2\zeta^2t^2}.
```

Exact coupled residual variance has maximum `v_max=0.2804576359...`, giving

```math
\sup_t SD[W_\infty-W_\zeta]_{random}
\le0.8906480701\sqrt{\chi/\zeta}.
```

**INVALIDATED INTERMEDIATE:** `0.8131` used the large-lag variance instead of the true maximum. A conservative fixed-window bound gives `0 <= H_mix-H <= C_chi sqrt(log zeta/zeta)`. Paired common-random-number calculations sharply resolve the positive correction but do not by themselves prove a positive lower coefficient.

### Step 28 — two-sided-Bessel Gaussian-mollifier correction
Define

```math
\sigma_\chi=2^{3/4}\sqrt\chi.
```

Under the standard Brownian-extremum stable zoom-in/localization assumptions,

```math
\frac{M_\infty-W_\infty(\tau_*+\varepsilon s)}
{\sigma_\chi\sqrt\varepsilon}
\Longrightarrow R_*(s),
\qquad \varepsilon=1/\zeta,
```

with `R_*` a two-sided BES(3)-type extremal field. Gaussian smoothing uses `K_1(s)=sqrt(2/pi) exp(-2s^2)`. The local mollifier loss

```math
\mathcal M_K(R)=\inf_u\int K_1(v)R(u-v)dv
```

is strictly positive almost surely. The integrated Dieker–Yakir denominator perturbation is lower order under the stationary high-pass coupling. Thus, under stable convergence and uniform integrability,

```math
H_{mix}(\chi)-H(\chi,\zeta)
=C_H(\chi)\zeta^{-1/2}+o(\zeta^{-1/2}),
```

with

```math
C_H(\chi)=2^{3/4}\sqrt\chi\,E[\Psi(W_\infty)\mathcal M_K(R_*)]>0.
```

**REJECTED SHORTCUT:** do not factor the weighted expectation without an independence theorem. A finite certified onset bandwidth still requires quantitative remainder control.

### Step 29 — Brownian–parabola double scaling and nonuniformity in `chi`
The fixed-`chi` Step-28 expansion is singular as `chi -> 0`. Around the smooth quadratic maximum, balance

```text
sigma_chi sqrt(h)  ~  h^2
```

to obtain the natural Brownian–parabola scales

```math
\boxed{
h_\chi=\sqrt2\chi^{1/3},
\qquad m_\chi=2\chi^{2/3}.}
```

Gaussian smoothing of width `~1/zeta` is therefore controlled by

```math
\boxed{
\mu=\zeta h_\chi
=\sqrt2\zeta\chi^{1/3}.}
```

In the joint small-`chi`/large-`zeta` limit with `mu` fixed, the natural crossover form is

```math
\boxed{
H_{mix}(\chi)-H(\chi,\zeta)
=\chi^{2/3}\mathcal F(\mu)+o(\chi^{2/3}),
}
```

with large-`mu` behavior `F(mu)~A_K mu^-1/2`, which recovers Step 28.

**NUMERICAL COLLAPSE:** converting the Step-27 paired data to `(mu, Delta H/chi^(2/3))` collapses the slow endpoint and `chi=0.1` cases closely; for `mu >= ~10`, `sqrt(mu) F_emp` is approximately constant near one. The tiny-`chi` fast data at `mu=1.37,2.74,5.49` remain visibly pre-asymptotic.

At the `r=2` endpoint trajectory,

```math
\boxed{
\mu_f\approx0.009776\,\kappa_f,
\qquad
\mu_s\approx0.16139\,\kappa_f.}
```

Thus at `kappa_f=100,200,300`, `mu_f~0.98,1.96,2.93`, while `mu_s~16.1,32.3,48.4`. The slow channel is already in the large-`mu` Bessel tail; the fast channel is still in crossover. **REFINEMENT:** the Step-26 fast `C_H~0.006` value from `zeta<=80` is an effective crossover coefficient, not a clean asymptotic coefficient. This changes the coefficient interpretation, not the eventual fixed-`chi` sign.

See `BROWNIAN_PARABOLA_DOUBLE_SCALING_STEP.md` and `numerics/double_scaling_crossover.py`.

---

## 3. Current frontier

The quantitative high-band problem is now better posed. A remainder theorem uniform in raw `zeta` is not the natural target for the small-`chi` fast channel. The next object is the one-dimensional Brownian-minus-parabola/Gaussian-mollifier crossover function

```math
\boxed{\mathcal F(\mu)}.
```

### Single next question — DO NOT ANSWER YET

> Can `F(mu)` be computed directly from the universal Brownian-minus-parabola local process, without simulating the full detector field, and can it provide a one-dimensional envelope from the crossover regime through the Bessel tail strong enough to close the remaining high-band interval?

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
- the Step-28 fixed-`chi` expansion is quantitatively uniform in `chi` at moderate `zeta`;
- the Step-26 fast `C_H~0.006` value is the final asymptotic coefficient;
- a finite certified onset bandwidth is known;
- the invalidated `0.8131` coupling coefficient is valid;
- no bounded pre-asymptotic pocket exists yet;
- the Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.
