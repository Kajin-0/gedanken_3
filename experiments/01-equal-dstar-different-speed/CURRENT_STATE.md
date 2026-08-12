# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 21:49 EDT  
**Status:** thirty-three logical steps completed. Step 33 replaces divergent raw level-upcrossing multiplicity by a finite-amplitude excursion-cluster count. The cluster event is exactly the false-alarm event, its first two moments admit a lower-level occupation-Palm representation, and the resulting moment enclosure remains sharp at finite high bandwidth and directly at the nondifferentiable rough endpoint. For the original `r=2`, `Lambda=0.895` task, representative cluster calculations separate fast and slow at `kappa_f=300`, `1000`, and `infinity`. The remaining gap is continuous-interval numerical/statistical certification, not a failure of the cluster variable. No universal scalar replacement metric and no novelty claim.

---

## 1. Original question

Two hypothetical photodetectors have equal conventional specific detectivity,

```math
D_A^*=D_B^*,
```

but radically different temporal responses. Does equal conventional `D*` imply equal ability to detect arbitrary optical signals?

---

## 2. Surviving logical chain

### Steps 01–04 — scalar and magnitude-only `D*`
- Equal scalar reference `D*` does **not** determine arbitrary temporal-signal SNR; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`.
- Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation stationary-Gaussian maximum-SNR problem.
- **NEGATIVE RESULT:** unknown timing alone does not break that full-observation equivalence.
- Finite observation can because magnitude `D*(f)` discards temporal phase/placement.

### Steps 05–12 — finite records and timing-search task
Derived finite-record optimal SNR

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle
```

and task-level detection time

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

For the controlled `t exp(-t/tau)` family, faster SNR accumulation can be offset by unknown-time search burden.

**REJECTED SHORTCUT:** finite-window SNR cannot be mixed directly with full-template timing bandwidth.  
**NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family.

### Step 13 — rough hard-window obstruction
Finite hard-window ideal-white-noise scans have

```math
R_x(y)=1-a_x|y|+O(y^2)
```

and are locally Brownian-like.

**FAILED NUMERICAL ESTIMATE:** rough-grid crossover near `ell~49` moved under refinement and is invalid.

### Steps 14–17 — genuine timing bandwidth and exact rare events
A genuine finite information bandwidth removes the cusp. Exact smooth Palm identity is available; Rice/EC is an upper bound. For finite hard windows,

```math
\sigma_\kappa^2\sim a_x\kappa/\sqrt\pi,
```

so Rice accuracy is nonuniform as bandwidth grows.

### Steps 18–19 — physical bandwidth and finite optimum
Use one physical information bandwidth with `kappa_i=Omega_B tau_i`.

- Artificially forcing accessible eventual SNR equal gives **no** finite bandwidth optimum.
- Holding the physical signal/noise fixed restores bandwidth-dependent SNR and gives a finite large-`r` optimum.
- Later Palm work confirms a shallow optimum survives beyond Rice, broadly near `kappa~50–65`, only `~0.3–0.4%` above infinity.

### Steps 20–21 — finite-`r` Rice double reversal corrected by Palm
For

```text
r=2, rho_full=6.2407571, alpha=1e-6, beta=0.90, Lambda=0.895
```

converged Rice gave apparent switches at `25.4898402` and `130.1945883`.

Palm preserves only

```math
\boxed{\kappa_{\times,1}^{Palm}\approx21.7\pm0.3}
```

and **INVALIDATES** the upper Rice switch. Direct Palm checks at `130,160,300` keep fast preferred for that slice.

### Steps 22–23 — Palm boundary map and direct rough endpoint
Representative finite-`r` Palm boundary rises from `Lambda~0.895` near `kappa_f~21.7` to about `0.91` around `kappa_f~60–200`. High-band slow-preferred tasks still exist above that boundary.

Exact occupation-time importance sampling at `kappa=infinity` gives

```math
\Lambda_{cross}^{\infty}\approx0.905\pm0.004,
\qquad X\approx7.75.
```

Thus `Lambda=0.895` remains fast-preferred at the rough endpoint.

### Steps 24–28 — two-parameter tangent, Pickands structure, Bessel correction
Finite bandwidth adds

```math
\zeta=\kappa/(\sqrt2u\sqrt b).
```

**REJECTED SHORTCUT:** `H_mix(chi)` alone is only the infinite-band endpoint.

The generalized Pickands constant has Dieker–Yakir form

```math
H(\chi,\zeta)=E[\sup e^W/\int e^W].
```

Brown–Resnick Slepian comparison proves monotonicity in `chi` and `zeta`, but not monotonicity of the physical detector boundary.

Common-white-noise Gaussian coupling gives rough/smoothed path difference `O(sqrt(chi/zeta))`.

**INVALIDATED INTERMEDIATE:** `0.8131` was the wrong coupling RMS coefficient; correct pointwise value is

```math
0.8906480701\sqrt{\chi/\zeta}.
```

A two-sided-BES(3) Brownian-extremum zoom-in identifies a positive `zeta^-1/2` mollifier correction under stable-convergence/localization/UI assumptions.

### Steps 29–30 — Brownian–parabola crossover and canonical function
Small `chi` introduces

```math
h_\chi=\sqrt2\chi^{1/3},
\qquad m_\chi=2\chi^{2/3},
\qquad \mu=\sqrt2\zeta\chi^{1/3}.
```

At the `r=2` endpoint,

```math
\mu_f\approx0.009776\kappa_f,
\qquad
\mu_s\approx0.16139\kappa_f.
```

The difficult small-`chi` fast crossover reduces to the canonical Brownian-minus-parabola function

```math
\boxed{
F(\mu)=\frac{2}{\sqrt\pi}E[M_\infty-M_\mu].
}
```

Representative continuum values are

```text
mu:       0     .5     1      2      3      5      10     20
F(mu):  .892   .806   .729   .597   .512   .410   .297   .213
```

with `sqrt(mu)F(mu)->~0.98`.

**INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` fast values were biased low by rough-maximum grid under-resolution. Refined full-field values agree with the canonical function at percent level. Fast asymptotic `C_H` refines to about `0.0088`.

### Step 31 — Palm-anchored universal high-band bridge
Insert `F(mu)` into the finite-`u` coupled tangent boundary and anchor the residual finite-threshold offset to Palm points plus the occupation endpoint.

Central bridge has one shallow maximum near

```math
\kappa_f\approx94.9,
\qquad
\Lambda_{max}\approx0.91068,
```

then decreases toward `Lambda_infinity~0.90513`.

**NUMERICAL CLOSURE:** for the original `Lambda=0.895` task, no bounded high-band re-entrant pocket is numerically supported.

**CONDITIONAL:** the Step-31 finite-`u` discrepancy law was empirical.

### Step 32 — direct finite-`u` Rice moment enclosure
For a smooth finite-band scan define

```math
X_u=1_{\{z(0)\le u\}}N_u^+.
```

Then exactly

```math
P_{FA}=Q(u)+P(X_u\ge1).
```

With `m1=E[X_u]`, `lambda=E[N_u^+]`, and `lambda2=E[N_u^+(N_u^+-1)]`,

```math
\boxed{
Q(u)+\frac{m_1^2}{\lambda+\lambda_2}
\le P_{FA}
\le Q(u)+m_1.
}
```

At `Lambda=0.895`, common physical time `X=7.04`:

```text
kappa_f   fast upper/alpha   slow lower/alpha
100           0.99737             1.04649
130           0.99861             1.02562
160           0.99961             1.00950
170           0.99990             1.00491
175           1.00004             1.00275
```

**PARTIAL CERTIFICATE:** fast preference is directly enclosed through at least `kappa_f=170` in the tested sequence without Step-31's empirical bridge.

**NEGATIVE RESULT:** around `kappa_f~175–200`, the second-moment crossing enclosure loses sharpness because slow-channel micro-upcrossing multiplicity drives `lambda2` upward. This is a variable-choice failure, not evidence for reversal.

### Step 33 — excursion-cluster moment enclosure
Choose `Delta>0`, set

```math
\boxed{a=u-\Delta,}
```

and decompose the lower excursion set `{t:z(t)>a}` into connected components. Count a component only if its maximum exceeds `u`; call the number of successful components `C_Delta`.

Pathwise,

```math
\boxed{
\sup z>u\iff C_\Delta\ge1.
}
```

For fixed `Delta>0`, `C_Delta` is finite on continuous compact paths even when the level-`u` upcrossing count diverges.

Thus

```math
\boxed{
\frac{E[C_\Delta]^2}{E[C_\Delta^2]}
\le P_{FA}
\le E[C_\Delta].
}
```

Choose a uniform search time and condition on `z(T)>a`. Under this lower-level occupation-Palm law `Q_a`, let `L` be the duration of the selected lower component, `S` indicate whether it reaches `u`, and `C_Delta` be the path's total successful count. Then exactly

```math
\boxed{
E[C_\Delta]
=\ell Q(a)E_{Q_a}[S/L],
}
```

```math
\boxed{
E[C_\Delta^2]
=\ell Q(a)E_{Q_a}[S C_\Delta/L].
}
```

No derivative or micro-upcrossing count appears.

For the original task at common time `X=7.16`, `Delta=0.15`, representative cluster calculations give

```text
kappa_f    detector    lower/alpha    upper/alpha
300        fast          0.98604        0.98624
300        slow          1.19896        1.19990
1000       fast          0.98417        0.98423
1000       slow          1.21537        1.21725
```

using `20000` lower-level occupation-Palm paths per detector.

Directly at `kappa=infinity`, using `50000` paths and grid spacing about `0.001`:

```text
             lower/alpha    upper/alpha    SE[E(C)]/alpha
fast           0.98940        0.98968          0.00429
slow           1.22367        1.22583          0.00474
```

**NUMERICAL ENDPOINT CERTIFICATE:** the cluster enclosure remains sharp at the nondifferentiable endpoint and separates fast/slow at the same `X=7.16`, independently of the Step-31 empirical bridge.

**OPEN:** the exact inequalities are analytic, but the displayed cluster moments are finite-grid Monte Carlo estimates rather than formal interval bounds. A continuous adaptive bandwidth scan with controlled grid/Monte Carlo error is still needed to certify the whole interval from the Step-32 endpoint (`~170`) to `infinity`.

See `EXCURSION_CLUSTER_MOMENT_ENCLOSURE_STEP.md` and `numerics/excursion_cluster_moment_enclosure.py`.

---

## 3. Current frontier

The micro-upcrossing divergence has been removed by counting finite-amplitude excursion clusters. The remaining task is numerical/statistical certification over the **continuous** high-band interval rather than isolated finite points plus the rough endpoint.

### Single next question — DO NOT ANSWER YET

> Can the excursion-cluster enclosure be evaluated on an adaptive bandwidth grid with controlled Monte Carlo/grid error and an optimized `Delta`, so that the entire interval from `kappa_f~170` to the rough endpoint is closed without the empirical Step-31 boundary fit?

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
- Step-32 crossing moments remain sharp in the rough limit;
- Step-33 Monte Carlo moment estimates are formal interval arithmetic;
- the continuous `170<kappa_f<infinity` interval is certified yet;
- no re-entrant pocket can occur for other task parameters;
- the Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.
