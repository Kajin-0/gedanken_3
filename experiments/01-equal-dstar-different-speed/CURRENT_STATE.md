# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 21:39 EDT  
**Status:** thirty-two logical steps completed. Step 32 derives a direct finite-`u` false-alarm enclosure from first- and second-order Rice moments. For the original `r=2`, `Lambda=0.895` task, this analytically bounds the exact finite-threshold event and independently certifies fast preference through at least `kappa_f=170` in the tested sequence, without the empirical Step-31 `delta(kappa)` bridge. The enclosure loses sharpness around `kappa_f~175–200` because the slow channel develops many micro-upcrossings inside one physical excursion; the next frontier is therefore cluster/occupation-time renormalization, not another ordinary crossing-count correction. No universal replacement metric and no novelty claim.

---

## 1. Original question

Two hypothetical detectors have equal conventional specific detectivity but radically different temporal responses. Does equal `D*` imply equal ability to detect an arbitrary optical signal?

---

## 2. Surviving logical chain

### Steps 01–04 — scalar and magnitude-only `D*`
Equal scalar reference `D*` does not determine arbitrary temporal-signal SNR; an explicit 1 Hz example gave `SNR_A/SNR_B~6.36`. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation Gaussian maximum-SNR problem. **NEGATIVE RESULT:** unknown timing alone does not break that ideal full-observation equivalence. Finite observation can because magnitude `D*(f)` discards temporal phase/placement.

### Steps 05–12 — finite records and task-level timing search
Derived finite-record optimal SNR

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle
```

and task-level detection time

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

For the controlled `t exp(-t/tau)` family, faster SNR accumulation can be offset by unknown-time search burden. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed directly with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family.

### Step 13 — rough hard-window obstruction
Finite hard-window ideal-white-noise scans have `R_x(y)=1-a_x|y|+...` and are locally Brownian-like. **FAILED NUMERICAL ESTIMATE:** rough-grid `ell~49` crossover invalid.

### Steps 14–17 — genuine timing bandwidth and exact rare events
A genuine finite timing-information bandwidth removes the cusp. Exact smooth Palm identity is available; Rice/EC is an upper bound. For finite hard windows `sigma_kappa^2~a_x kappa/sqrt(pi)`, so Rice accuracy is nonuniform toward the rough limit.

### Steps 18–19 — shared physical bandwidth and finite optimum
Use `kappa_i=Omega_B tau_i`. Artificially forcing accessible eventual SNR equal gives no finite bandwidth optimum. Holding physical signal/noise fixed restores bandwidth-dependent SNR and produces a finite large-`r` optimum; later Palm work confirms a shallow optimum survives beyond Rice.

### Steps 20–21 — finite-`r` Rice double reversal corrected by Palm
For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=0.90`, `Lambda=0.895`, converged Rice gave apparent switches `25.4898402` and `130.1945883`. Palm preserves only the lower switch:

```math
\kappa_{\times,1}^{Palm}\approx21.7\pm0.3.
```

**INVALIDATED:** upper Rice switch. Palm checks at `130,160,300` keep fast preferred for that slice.

### Step 22 — Palm boundary map and finite optimum
Representative finite-`r` Palm boundary rises from `Lambda~0.895` near `kappa_f~21.7` to about `0.91` around `kappa_f~60–200`. High-band slow-preferred tasks survive above that boundary. The large-`r` full-template Palm optimum is broad near `kappa~50–65` and only `~0.3–0.4%` above infinity.

### Step 23 — matched rough/smooth infinite-band limit
Finite hard-window local covariance:

```math
R_x(y)=1-a_x|y|-\frac{b_x}{2}y^2+O(|y|^3),
\qquad
\chi_x=a_xu/\sqrt{b_x}.
```

Exact occupation-time importance sampling gives the direct rough endpoint

```math
\Lambda_{cross}^{\infty}\approx0.905\pm0.004,
\qquad X\approx7.75.
```

Thus `Lambda=0.895` remains fast-preferred at the endpoint.

### Steps 24–25 — two-parameter tangent field and generalized Pickands constant
Finite bandwidth adds

```math
\zeta=\kappa/(\sqrt2u\sqrt b).
```

**REJECTED SHORTCUT:** `H_mix(chi)` alone is only the infinite-band endpoint. The two-parameter generalized Pickands constant has Dieker–Yakir form

```math
H(\chi,\zeta)=E[\sup e^W/\int e^W].
```

Brown–Resnick Slepian comparison proves monotonicity in `chi` and `zeta`, but that alone does not prove monotonic detector preference.

### Steps 26–28 — high-band derivative, Gaussian coupling, Bessel continuity correction
Finite-hard-window SNR recovery is `O(kappa^-1)`. Common-white-noise Gaussian coupling proves the rough/smoothed path difference is `O(sqrt(chi/zeta))`; **INVALIDATED INTERMEDIATE:** `0.8131` was the wrong RMS coefficient, corrected to `0.8906480701`. A two-sided-BES(3) Brownian-extremum zoom-in then identifies a positive Gaussian-mollifier `zeta^-1/2` Pickands correction under stable-convergence/localization/UI assumptions. The Dieker–Yakir denominator is lower order.

### Steps 29–30 — Brownian–parabola crossover and canonical function
Small `chi` introduces

```math
h_\chi=\sqrt2\chi^{1/3},
\qquad
m_\chi=2\chi^{2/3},
\qquad
\mu=\sqrt2\zeta\chi^{1/3}.
```

At the `r=2` endpoint,

```math
\mu_f\approx0.009776\kappa_f,
\qquad
\mu_s\approx0.16139\kappa_f.
```

The small-`chi` fast crossover reduces to the detector-independent canonical Brownian-minus-parabola function

```math
\boxed{
F(\mu)=\frac{2}{\sqrt\pi}E[M_\infty-M_\mu].
}
```

Representative continuum values are `F(0)~0.892`, `F(0.5,1,2,3,5,10,20)~0.806,0.729,0.597,0.512,0.410,0.297,0.213`, with `sqrt(mu)F(mu)->~0.98`. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` fast values were biased low by rough-maximum grid under-resolution. Refined full-field values agree with the canonical function at percent level. Fast asymptotic `C_H` refines to about `0.0088`.

### Step 31 — Palm-anchored universal high-band bridge
Insert `F(mu)` into the finite-`u` coupled tangent boundary and anchor the remaining finite-threshold offset to Palm points at `kappa_f=60,100,200` plus the occupation endpoint. The central bridge has one shallow maximum near

```math
\kappa_f\approx94.9,
\qquad
\Lambda_{max}\approx0.91068,
```

then decreases toward `Lambda_infinity~0.90513`. **NUMERICAL CLOSURE:** for the original `Lambda=0.895` task, no bounded high-band re-entrant pocket is numerically supported. **CONDITIONAL:** the finite-`u` offset was still empirical.

### Step 32 — direct finite-`u` Rice moment enclosure
For a smooth finite-band scan define

```math
X_u=1_{\{z(0)\le u\}}N_u^+.
```

Then exactly

```math
P_{FA}=Q(u)+P(X_u\ge1).
```

Let

```math
m_1=E[X_u],
\quad
\lambda=E[N_u^+],
\quad
\lambda_2=E[N_u^+(N_u^+-1)].
```

Since `X_u^2 <= (N_u^+)^2`, Cauchy–Schwarz gives

```math
\boxed{
Q(u)+\frac{m_1^2}{\lambda+\lambda_2}
\le P_{FA}
\le Q(u)+m_1.
}
```

All terms are finite-`u` first-/second-order Rice integrals of the known covariance. At `Lambda=0.895`, common physical time `X=7.04`, deterministic quadrature gives representative ratios

```text
kappa_f   fast P_FA upper/alpha   slow P_FA lower/alpha
100              0.99737                  1.04649
130              0.99861                  1.02562
160              0.99961                  1.00950
170              0.99990                  1.00491
175              1.00004                  1.00275
```

Hence fast preference is directly enclosed through at least `kappa_f=170` in this sequence without the Step-31 empirical correction. At `~175–200` the bounds overlap because the slow-channel second factorial moment grows rapidly from clustered micro-upcrossings. **NEGATIVE RESULT:** ordinary second crossing moments do not remain sharp into the rough tail; this is a clustering limitation, not evidence for a reversal.

See `FINITE_U_RICE_MOMENT_ENCLOSURE_STEP.md` and `numerics/finite_u_rice_moment_enclosure.py`.

---

## 3. Current frontier

Replace raw upcrossing multiplicity in the clustered high-band regime by an excursion-cluster or occupation-time variable whose moments remain finite and informative as `kappa_f -> infinity`.

### Single next question — DO NOT ANSWER YET

> Can an excursion-cluster or occupation-time moment variable provide a finite-`u` upper/lower enclosure that remains sharp as micro-upcrossing multiplicity diverges, thereby extending the Step-32 direct certificate continuously to the rough endpoint?

---

## 4. Scope boundary

Do not claim:
- faster detectors are universally better or worse;
- a universal scalar replacement for `D*`;
- Step-13 `ell~49` is valid;
- arbitrary low-pass filtering is a true information-band limitation;
- Gaussian information weighting is a literal circuit transfer function;
- Rice is uniformly accurate at high finite-window bandwidth;
- Step-20 double reversal is exact;
- raw Step-27 fast values are continuum crossover data;
- Step-31 empirical `delta(kappa)` is exact;
- Step-32 second-moment crossing enclosure stays sharp in the rough limit;
- the deterministic floating-point quadrature is formal interval arithmetic;
- no re-entrant pocket can occur for other task parameters;
- the Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.
