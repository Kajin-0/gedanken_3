# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 22:22 EDT:** compact chronology preserving consequential results, corrections, invalidations, rejected shortcuts, numerical validations, asymptotic qualifications, and current stopping point. Full derivations remain in dedicated step files.

---

## Steps 01–04
Equal scalar reference `D*` does not determine arbitrary temporal-signal SNR; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation problem. **NEGATIVE RESULT:** unknown timing alone does not break that ideal equivalence. Finite windows can because magnitude-only `D*(f)` discards temporal phase/placement.

## Steps 05–12
Derived finite-record optimal SNR and task-level detection time. Faster SNR accumulation can be offset by unknown-time search burden. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed directly with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family.

## Step 13
Finite hard-window ideal-white-noise scan is locally Brownian-like. **FAILED NUMERICAL ESTIMATE:** rough-grid crossover near `ell~49` invalid.

## Steps 14–19
A genuine finite timing bandwidth removes the hard-window cusp. Exact smooth Palm identity available; Rice/EC is an upper bound and nonuniform as bandwidth grows. With common physical bandwidth, forcing accessible SNR equal gives no finite optimum. Holding physical signal/noise fixed produces a genuine finite large-`r` optimum; later Palm work confirms a shallow optimum broadly near `kappa~50–65`, about `0.3–0.4%` above infinity.

## Steps 20–23
For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=0.90`, `Lambda=0.895`, Rice gave switches `25.4898402` and `130.1945883`. Palm preserves only `kappa_cross~21.7 +/-0.3`; **INVALIDATED:** upper Rice switch. Palm boundary reaches about `Lambda~0.91` around `kappa_f~60–200`. Direct occupation sampling at `kappa=infinity` gives `Lambda_cross^infinity~0.905 +/-0.004`; `Lambda=0.895` remains fast-preferred.

## Steps 24–28
Finite bandwidth adds `zeta=kappa/(sqrt(2)u sqrt(b))`; generalized Pickands structure is two-parameter. Brown–Resnick Slepian comparison proves local monotonicity but not physical-boundary monotonicity. Common-white-noise coupling gives the rough/smoothed path scale. **INVALIDATED INTERMEDIATE:** `0.8131`; correct pointwise RMS coefficient is `0.8906480701 sqrt(chi/zeta)`. Two-sided-BES(3) Brownian-extremum zoom-in identifies a positive `zeta^-1/2` Gaussian-mollifier correction under stable-convergence/localization/UI.

## Steps 29–30
Small `chi` introduces Brownian–parabola scales

```math
h_chi=sqrt(2)chi^(1/3),
m_chi=2chi^(2/3),
mu=sqrt(2)zeta chi^(1/3).
```

At the `r=2` endpoint, `mu_f~0.009776 kappa_f`, `mu_s~0.16139 kappa_f`. The small-`chi` fast crossover reduces to

```math
F(mu)=(2/sqrt(pi))E[M_inf-M_mu].
```

Representative continuum values: `F(0)~.892`, `F(.5,1,2,3,5,10,20)~.806,.729,.597,.512,.410,.297,.213`; `sqrt(mu)F(mu)->~0.98`. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` fast values were biased low by rough-maximum grid under-resolution. Refined full-field values agree with the canonical curve; fast asymptotic `C_H` refines to about `0.0088`.

## Step 31
Insert `F(mu)` into the finite-`u` coupled tangent boundary and anchor residual finite-threshold offset to Palm points plus the rough endpoint. Central bridge peaks near `kappa_f~94.9`, `Lambda~0.91068`, then decreases toward `Lambda_infinity~0.90513`. **NUMERICAL CLOSURE:** original `Lambda=0.895` task has no numerically supported bounded high-band re-entrant pocket. **CONDITIONAL:** the finite-`u` offset was empirical.

## Step 32 — direct finite-`u` Rice moment enclosure
For a smooth finite-band scan,

```math
X_u=1_{z(0)<=u}N_u^+,
P_FA=Q(u)+P(X_u>=1).
```

With `m1=E[X_u]`, `lambda=E[N_u^+]`, `lambda2=E[N_u^+(N_u^+-1)]`,

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

**PARTIAL CERTIFICATE:** fast preference directly enclosed through at least `kappa_f=170` in the tested sequence. **NEGATIVE RESULT:** around `175–200`, raw crossing second moments lose sharpness because one physical excursion contains many micro-upcrossings.

Full derivation: `FINITE_U_RICE_MOMENT_ENCLOSURE_STEP.md`.  
Calculator: `numerics/finite_u_rice_moment_enclosure.py`.

## Step 33 — excursion-cluster moment renormalization
Choose finite amplitude gap `Delta>0`, set `a=u-Delta`, decompose `{t:z(t)>a}` into connected components, and count only components whose maximum exceeds `u`; call this `C_Delta`.

Pathwise,

```math
sup z>u iff C_Delta>=1.
```

For fixed `Delta`, the count remains finite on continuous compact paths even when raw level-`u` upcrossings proliferate.

```math
E[C_Delta]^2/E[C_Delta^2] <= P_FA <= E[C_Delta].
```

Under lower-level occupation-Palm measure `Q_a`, with selected-component duration `L`, success indicator `S`, and total successful count `C_Delta`, exact identities are

```math
E[C_Delta]=ell Q(a)E_a[S/L],
E[C_Delta^2]=ell Q(a)E_a[S C_Delta/L].
```

For the original task at `X=7.16`, `Delta=0.15`:

```text
kappa_f    detector    lower/alpha    upper/alpha
300        fast          0.98604        0.98624
300        slow          1.19896        1.19990
1000       fast          0.98417        0.98423
1000       slow          1.21537        1.21725
```

Rough endpoint (`50000` paths, grid `~0.001`):

```text
             lower/alpha    upper/alpha    SE[E(C)]/alpha
fast           0.98940        0.98968          0.00429
slow           1.22367        1.22583          0.00474
```

**NUMERICAL ENDPOINT CERTIFICATE / CLUSTER-RENORMALIZED ENCLOSURE:** cluster moments remain sharp at `kappa=infinity`; Step-32 divergence belongs to micro-upcrossing multiplicity, not the physical excursion event.

Full derivation: `EXCURSION_CLUSTER_MOMENT_ENCLOSURE_STEP.md`.  
Calculator: `numerics/excursion_cluster_moment_enclosure.py`.

## Step 34 — 22:22 EDT — adaptive paired cluster tail closure
Use

```math
q=kappa_f^(-1/2)
```

so the unresolved tail becomes finite:

```math
0<=q<=0.0767
<->
infinity>=kappa_f>=~170.
```

A preliminary declustering-gap screen finds a broad low-variance region around `Delta~0.08–0.15`; no unique optimum. Retain `Delta=0.15` because Step 33 already validated it on the finest rough grid and its multiple-successful-cluster fraction is negligible.

For the fast first cluster moment `U_f(q)=E[C_Delta(q)]`, generate all finite-`q` and endpoint fields from the same white noise, truncated-normal uniform, and selected occupation time. This gives an unbiased paired difference estimator with much lower variance:

```math
E[Uhat_f(q)-Uhat_f(0)]=U_f(q)-U_f(0).
```

Endpoint anchor from Step 33:

```text
U_f(0)/alpha = 0.98968
SE/alpha     = 0.00429.
```

Dense `3000`-path paired scan on

```text
q=0,0.005,0.010,...,0.075,0.0767
```

plus extra midpoints in the steepest region gives

```text
max sampled positive correction/alpha ~= +1.9e-8
min correction/alpha                  ~= -0.00188
max paired SE/alpha                   ~= 0.00106
max adjacent 0.005-node change/alpha  ~= 0.000548.
```

Paired nested-grid rough-endpoint check relative to a fine `~0.000751` grid:

```text
~0.00150 grid: -0.000929 alpha +/-0.000655
~0.00300 grid: -0.001341 alpha +/-0.000778.
```

Use conservative fast allowances `0.002 alpha` for grid and `0.0006 alpha` for inter-node variation. With one-sided Gaussian factor `1.645`,

```math
U_f/alpha
~<0.98968
 +1.645 sqrt(0.00429^2+0.00106^2)
 +0.002+0.0006
~0.99955<1.
```

The slow lower cluster bound is far from threshold. Absolute `3000`-path scan on the same `q` nodes has minimum central value

```text
L_s/alpha ~=1.18296 at q=0.0767 (~kappa_f=170),
```

maximum lower-bound SE `~0.01949 alpha`, and maximum adjacent-node change `~0.0165 alpha`. Even subtracting conservative allowances

```text
1.645*0.01949 + 0.03 grid + 0.02 inter-node
```

gives

```math
L_s/alpha ~>1.10>1.
```

**PAIRED NUMERICAL INTERVAL CLOSURE:** at common witness time `X=7.16`, the original `Lambda=0.895` task is numerically separated over the adaptively sampled/interpolated tail

```math
170<=kappa_f<=infinity
```

without the empirical Step-31 `delta(kappa)` fit.

**QUALIFICATION:** the allowances are explicit measured/conservative numerical scales, not formal interval arithmetic, rigorous confidence sequences, or a theorem-level continuity modulus for unsampled `q`.

Full derivation: `ADAPTIVE_CLUSTER_TAIL_CLOSURE_STEP.md`.  
Calculator: `numerics/adaptive_cluster_tail_closure.py`.

---

## Current stopping point

For the original calibration, the high-band re-entrant-pocket conclusion no longer relies on the empirical Step-31 boundary fit. Direct finite-`u` enclosures plus paired cluster coupling support fast preference through the rough endpoint. The remaining mathematical gap is analytic continuity of cluster moments in `q`.

### Single natural next question

> Can the common-white-noise coupling be converted into an analytic continuity modulus for the excursion-cluster moments as a function of `q=kappa_f^(-1/2)`, replacing the empirical inter-node allowance and turning the Step-34 numerical tail closure into a theorem-level parameter-interval enclosure?
