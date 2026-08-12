# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 22:22 EDT  
**Status:** thirty-four logical steps completed. Step 34 uses the Step-33 excursion-cluster variable in the natural high-band coordinate `q=kappa_f^(-1/2)` and common-random-number coupling to the rough endpoint. For the original `r=2`, `Lambda=0.895` task, a dense paired `q` scan plus explicit Monte Carlo, timing-grid, and inter-node allowances gives a conservative fast upper envelope `U_f/alpha~<0.99955` and slow lower envelope `L_s/alpha~>1.10` across the adaptively sampled/interpolated tail `170<=kappa_f<=infinity`. This removes the empirical Step-31 `delta(kappa)` fit from the high-band conclusion. It is a **paired numerical interval closure**, not formal interval arithmetic or a theorem-level continuity result. No universal scalar replacement metric and no novelty claim.

---

## 1. Original question

Two hypothetical photodetectors satisfy

```math
D_A^*=D_B^*
```

but have radically different temporal responses. Does equal conventional specific detectivity imply equal ability to detect arbitrary optical signals?

---

## 2. Surviving logical chain

### Steps 01–04 — scalar and magnitude-only `D*`
Equal scalar reference `D*` does **not** determine arbitrary temporal-signal SNR; an explicit 1 Hz construction gave `SNR_A/SNR_B~6.36`. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation stationary-Gaussian maximum-SNR problem. **NEGATIVE RESULT:** unknown timing alone does not break that ideal equivalence. Finite observation can because magnitude-only `D*(f)` discards temporal phase/placement.

### Steps 05–12 — finite records and timing-search task
Derived finite-record optimal SNR

```math
rho_t^2=<s_t,C_t^{-1}s_t>
```

and task-level detection time

```math
T_D(alpha,beta,L)=inf{t:rho_t-gamma_t(L,alpha)>=Phi^{-1}(beta)}.
```

For the controlled `t exp(-t/tau)` family, faster SNR accumulation can be offset by unknown-time search burden. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed directly with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family.

### Step 13 — rough hard-window obstruction
Finite hard-window ideal-white-noise scans have

```math
R_x(y)=1-a_x|y|+O(y^2)
```

and are locally Brownian-like. **FAILED NUMERICAL ESTIMATE:** rough-grid crossover near `ell~49` moved under refinement and is invalid.

### Steps 14–19 — genuine timing bandwidth and fixed physical signal/noise
A genuine finite timing-information bandwidth removes the cusp. Exact smooth Palm rare-event identity is available; Rice/EC is an upper bound. For finite hard windows `sigma_kappa^2~a_x kappa/sqrt(pi)`, so Rice accuracy is nonuniform as bandwidth grows.

With common physical bandwidth `kappa_i=Omega_B tau_i`, forcing accessible eventual SNR equal gives **no** finite bandwidth optimum. Holding the physical signal/noise fixed restores bandwidth-dependent accessible SNR and yields a finite large-`r` optimum; later Palm work confirms a shallow optimum broadly near `kappa~50–65`, only `~0.3–0.4%` above infinity.

### Steps 20–23 — finite-`r` Rice reversal corrected, Palm map, rough endpoint
For

```text
r=2, rho_full=6.2407571, alpha=1e-6, beta=0.90, Lambda=0.895
```

converged Rice produced apparent switches at `25.4898402` and `130.1945883`. Continuous Palm preserves only

```math
kappa_cross^Palm ~ 21.7 +/- 0.3
```

and **INVALIDATES** the upper Rice switch. Palm maps the high-band finite-`r` boundary near `Lambda~0.91` around `kappa_f~60–200`; high-band slow-preferred tasks still exist above that boundary.

Exact occupation-time importance sampling at `kappa=infinity` gives

```math
Lambda_cross^infinity ~ 0.905 +/- 0.004,
X ~ 7.75.
```

Thus `Lambda=0.895` remains fast-preferred at the rough endpoint.

### Steps 24–28 — two-parameter tangent, generalized Pickands, Bessel correction
Finite bandwidth adds

```math
zeta=kappa/(sqrt(2)u sqrt(b)).
```

**REJECTED SHORTCUT:** `H_mix(chi)` alone is only the infinite-band endpoint. The generalized Pickands constant has Dieker–Yakir form

```math
H(chi,zeta)=E[sup e^W / integral e^W].
```

Brown–Resnick Slepian comparison proves monotonicity in `chi` and `zeta`, but not monotonicity of the physical detector boundary.

Common-white-noise Gaussian coupling gives a rough/smoothed path difference `O(sqrt(chi/zeta))`. **INVALIDATED INTERMEDIATE:** `0.8131` was the wrong RMS coefficient; the correct pointwise value is

```math
0.8906480701 sqrt(chi/zeta).
```

A two-sided-BES(3) Brownian-extremum zoom-in identifies a positive `zeta^-1/2` mollifier correction under stable-convergence/localization/UI assumptions.

### Steps 29–30 — Brownian–parabola crossover and canonical function
Small `chi` introduces

```math
h_chi=sqrt(2)chi^(1/3),
m_chi=2chi^(2/3),
mu=sqrt(2)zeta chi^(1/3).
```

At the `r=2` endpoint,

```math
mu_f~0.009776 kappa_f,
mu_s~0.16139 kappa_f.
```

The difficult small-`chi` fast crossover reduces to the canonical Brownian-minus-parabola function

```math
F(mu)=(2/sqrt(pi)) E[M_infinity-M_mu].
```

Representative continuum values:

```text
mu:       0     .5     1      2      3      5      10     20
F(mu):  .892   .806   .729   .597   .512   .410   .297   .213
```

with `sqrt(mu)F(mu)->~0.98`.

**INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` fast values were biased low by rough-maximum grid under-resolution. Refined full-field values agree with the canonical function at percent level. Fast asymptotic `C_H` refines to about `0.0088`.

### Step 31 — Palm-anchored universal high-band bridge
Insert `F(mu)` into the finite-`u` coupled tangent boundary and anchor only the residual finite-threshold offset to Palm points plus the occupation endpoint. The central bridge has one shallow maximum near

```math
kappa_f~94.9,
Lambda_max~0.91068,
```

then decreases toward `Lambda_infinity~0.90513`.

**NUMERICAL CLOSURE:** for the original `Lambda=0.895` task, no bounded high-band re-entrant pocket is numerically supported. **CONDITIONAL:** the Step-31 finite-`u` discrepancy law was empirical.

### Step 32 — direct finite-`u` Rice moment enclosure
For a smooth finite-band scan define

```math
X_u=1_{z(0)<=u} N_u^+.
```

Then exactly

```math
P_FA=Q(u)+P(X_u>=1).
```

With `m1=E[X_u]`, `lambda=E[N_u^+]`, and `lambda2=E[N_u^+(N_u^+-1)]`,

```math
Q(u)+m1^2/(lambda+lambda2) <= P_FA <= Q(u)+m1.
```

At `Lambda=0.895`, `X=7.04`:

```text
kappa_f   fast upper/alpha   slow lower/alpha
100           0.99737             1.04649
130           0.99861             1.02562
160           0.99961             1.00950
170           0.99990             1.00491
175           1.00004             1.00275
```

**PARTIAL CERTIFICATE:** fast preference is directly enclosed through at least `kappa_f=170` in the tested sequence without Step-31's empirical bridge.

**NEGATIVE RESULT:** around `kappa_f~175–200`, raw crossing second moments lose sharpness because one physical slow-channel excursion contains many micro-upcrossings. This is a variable-choice failure, not evidence for reversal.

### Step 33 — excursion-cluster moment renormalization
Choose `Delta>0`, set

```math
a=u-Delta,
```

and decompose `{t:z(t)>a}` into connected components. Count only components whose maximum exceeds `u`; call this `C_Delta`.

Pathwise,

```math
sup z>u iff C_Delta>=1.
```

For fixed finite amplitude gap, `C_Delta` remains finite on continuous compact paths even as level-`u` upcrossings proliferate.

Moment enclosure:

```math
E[C_Delta]^2/E[C_Delta^2] <= P_FA <= E[C_Delta].
```

Under the lower-level occupation-Palm law `Q_a`, with selected-component duration `L`, success indicator `S`, and total successful count `C_Delta`, exact identities are

```math
E[C_Delta]=ell Q(a) E_a[S/L],
E[C_Delta^2]=ell Q(a) E_a[S C_Delta/L].
```

No derivative/upcrossing count appears.

For the original task at `X=7.16`, `Delta=0.15`:

```text
kappa_f    detector    lower/alpha    upper/alpha
300        fast          0.98604        0.98624
300        slow          1.19896        1.19990
1000       fast          0.98417        0.98423
1000       slow          1.21537        1.21725
```

At the direct rough endpoint (`50000` paths, grid `~0.001`):

```text
             lower/alpha    upper/alpha    SE[E(C)]/alpha
fast           0.98940        0.98968          0.00429
slow           1.22367        1.22583          0.00474
```

**NUMERICAL ENDPOINT CERTIFICATE / CLUSTER-RENORMALIZED ENCLOSURE:** the cluster bounds remain sharp at `kappa=infinity` and separate fast/slow at the same physical time.

### Step 34 — adaptive paired cluster tail closure
Use the natural high-band coordinate

```math
q=kappa_f^(-1/2),
```

so the unresolved tail is the finite interval

```math
0<=q<=0.0767
```

corresponding to `infinity>=kappa_f>=~170`.

A preliminary `Delta` screen shows a broad variance minimum around `Delta~0.08–0.15`; no unique optimum is resolved. Retain `Delta=0.15` conservatively because Step 33 already validated it on the finest rough grid and its multiple-successful-cluster fraction is negligible.

For the fast first cluster moment `U_f(q)=E[C_Delta(q)]`, generate finite-`q` and rough-endpoint fields from common white noise, common truncated-normal uniforms, and common selected occupation times. This gives an unbiased paired difference estimator

```math
E[Uhat_f(q)-Uhat_f(0)]=U_f(q)-U_f(0)
```

with much smaller variance than independent absolute estimates.

Anchor at Step 33:

```text
U_f(0)/alpha = 0.98968
SE/alpha     = 0.00429.
```

Dense paired scan with `3000` paths on

```text
q=0,0.005,0.010,...,0.075,0.0767
```

plus refined midpoints in the steepest region gives:

```text
max sampled positive finite-q correction/alpha ~= +1.9e-8
min correction/alpha                         ~= -0.00188
max paired SE/alpha                          ~= 0.00106
max adjacent 0.005-node change/alpha         ~= 0.000548.
```

A paired nested-grid rough-endpoint check, evaluating the same conditioned rough path on multiple timing grids, gives coarse-minus-fine shifts of only

```text
~0.00150 grid: -0.000929 alpha +/-0.000655
~0.00300 grid: -0.001341 alpha +/-0.000778
```

relative to a fine `~0.000751` grid. Use conservative fast allowances

```text
grid allowance      = 0.002 alpha
inter-node allowance= 0.0006 alpha.
```

Combining the independent endpoint-anchor and paired-profile Monte Carlo errors with one-sided Gaussian factor `1.645` gives

```math
U_f/alpha
~< 0.98968
   +1.645 sqrt(0.00429^2+0.00106^2)
   +0.002
   +0.0006
~ 0.99955 < 1.
```

The slow lower cluster bound is much farther from threshold. An absolute `3000`-path scan on the same `q` nodes gives a minimum central lower ratio near the finite end,

```text
L_s/alpha ~= 1.18296 at q=0.0767 (~kappa_f=170),
```

with maximum lower-bound SE `~0.01949 alpha` and maximum adjacent-node change `~0.0165 alpha`. Even subtracting deliberately conservative allowances

```text
1.645*0.01949 + 0.03 grid + 0.02 inter-node
```

gives

```math
L_s/alpha ~> 1.10 > 1.
```

**PAIRED NUMERICAL INTERVAL CLOSURE:** at the common witness time `X=7.16`, the original `Lambda=0.895` task is numerically separated over the entire adaptively sampled/interpolated tail

```math
170 <= kappa_f <= infinity
```

without the Step-31 empirical `delta(kappa)` fit.

**QUALIFICATION:** the allowances are measured/conservative numerical scales, not theorem-level continuity or formal interval/confidence bounds for every unsampled `q`.

See `ADAPTIVE_CLUSTER_TAIL_CLOSURE_STEP.md` and `numerics/adaptive_cluster_tail_closure.py`.

---

## 3. Current frontier

For the original calibration, the high-band re-entrant-pocket question is now supported by direct finite-`u` enclosures through the rough endpoint without the empirical Step-31 boundary fit. The remaining mathematical gap is to replace the empirical inter-node allowance by an analytic continuity modulus for the cluster moments in `q=kappa_f^(-1/2)`.

### Single next question — DO NOT ANSWER YET

> Can the common-white-noise coupling be converted into an analytic continuity modulus for the excursion-cluster moments as a function of `q=kappa_f^(-1/2)`, replacing the empirical inter-node allowance and turning the Step-34 numerical tail closure into a theorem-level parameter-interval enclosure?

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
- Step-31 empirical `delta(kappa)` is exact or still required for the original high-band conclusion;
- Step-32 raw crossing moments stay sharp in the rough limit;
- Step-33/34 Monte Carlo estimates and allowances are formal interval arithmetic;
- Step-34 proves a theorem-level continuous-parameter enclosure;
- no re-entrant pocket can occur for other task parameters;
- the Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.
