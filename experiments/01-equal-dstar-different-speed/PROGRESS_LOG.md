# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 21:49 EDT:** compact chronology preserving consequential results, corrections, invalidations, rejected shortcuts, numerical validations, asymptotic qualifications, and current stopping point. Full derivations remain in dedicated step files.

---

## Steps 01–04
Equal scalar reference `D*` does not determine arbitrary temporal-signal SNR; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation problem. **NEGATIVE RESULT:** unknown timing alone does not break that ideal equivalence. Finite windows can because magnitude `D*(f)` discards temporal phase/placement.

## Steps 05–12
Derived finite-record optimal SNR and task-level detection time. Faster SNR accumulation can be offset by unknown-time search burden. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed directly with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family.

## Step 13
Finite hard-window ideal-white-noise scan is locally Brownian-like. **FAILED NUMERICAL ESTIMATE:** rough-grid crossover near `ell~49` invalid.

## Steps 14–17
A genuine finite timing bandwidth removes the cusp. Exact smooth Palm identity available; Rice/EC is an upper bound. Finite hard windows have `sigma_kappa^2~a_x kappa/sqrt(pi)`, making Rice nonuniform toward the rough limit.

## Steps 18–19
With `kappa_i=Omega_B tau_i`, forcing accessible SNR equal gives no finite bandwidth optimum. Holding physical signal/noise fixed produces a finite large-`r` optimum; later Palm work confirms a shallow optimum survives beyond Rice.

## Steps 20–21
For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=0.90`, `Lambda=0.895`, Rice gave apparent switches `25.4898402` and `130.1945883`. Palm preserves only the lower switch `kappa_cross~21.7 +/-0.3`. **INVALIDATED:** upper Rice switch. Palm checks at `130,160,300` keep fast preferred.

## Steps 22–23
Palm boundary rises to about `Lambda~0.91` at moderate/high finite bandwidth. High-band slow-preferred tasks survive above it. Direct occupation-time rough endpoint gives `Lambda_cross^infinity~0.905 +/-0.004`; `Lambda=0.895` remains fast-preferred.

## Steps 24–28
Finite bandwidth adds `zeta=kappa/(sqrt(2)u sqrt(b))`; generalized Pickands structure is two-parameter. Brown–Resnick Slepian comparison proves local monotonicity but not detector-boundary monotonicity. Common-white-noise coupling gives the rough/smoothed path scale. **INVALIDATED INTERMEDIATE:** `0.8131` coupling coefficient; correct pointwise RMS coefficient is `0.8906480701 sqrt(chi/zeta)`. Two-sided-BES(3) Brownian-extremum zoom-in identifies a positive `zeta^-1/2` mollifier correction under stable-convergence/localization/UI.

## Steps 29–30
Small `chi` introduces Brownian–parabola scales

```math
h_chi=sqrt(2) chi^(1/3),
\qquad m_chi=2chi^(2/3),
\qquad mu=sqrt(2)zeta chi^(1/3).
```

At the `r=2` endpoint, `mu_f~0.009776 kappa_f`, `mu_s~0.16139 kappa_f`. The small-`chi` crossover reduces to

```math
F(mu)=\frac{2}{\sqrt\pi}E[M_inf-M_mu].
```

Representative continuum values: `F(0)~.892`, `F(.5,1,2,3,5,10,20)~.806,.729,.597,.512,.410,.297,.213`; `sqrt(mu)F(mu)->~0.98`. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` fast values were biased low by rough-maximum grid under-resolution. Refined full-field values agree with the canonical curve; fast asymptotic `C_H` refines to about `0.0088`.

## Step 31
Insert `F(mu)` into the finite-`u` coupled tangent boundary and anchor residual finite-threshold offset to Palm points plus the rough endpoint. Central bridge has one shallow maximum near `kappa_f~94.9`, `Lambda~0.91068`, then decreases toward `Lambda_infinity~0.90513`. **NUMERICAL CLOSURE:** original `Lambda=0.895` task has no numerically supported bounded high-band re-entrant pocket. **CONDITIONAL:** the finite-`u` offset was empirical.

## Step 32 — direct finite-`u` Rice moment enclosure
For a smooth finite-band scan define

```math
X_u=1_{\{z(0)\le u\}}N_u^+.
```

Then exactly

```math
P_FA=Q(u)+P(X_u\ge1).
```

With `m1=E[X_u]`, `lambda=E[N_u^+]`, and `lambda2=E[N_u^+(N_u^+-1)]`,

```math
\boxed{
Q(u)+\frac{m_1^2}{\lambda+\lambda_2}
\le P_FA
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

**PARTIAL CERTIFICATE:** fast preference is directly enclosed through at least `kappa_f=170` in the tested sequence, without Step-31's empirical bridge.

**NEGATIVE RESULT:** around `kappa_f~175–200`, raw crossing second moments lose sharpness because one physical slow-channel excursion contains many micro-upcrossings.

Full derivation: `FINITE_U_RICE_MOMENT_ENCLOSURE_STEP.md`.  
Calculator: `numerics/finite_u_rice_moment_enclosure.py`.

## Step 33 — 21:49 EDT — excursion-cluster moment renormalization
Choose a finite amplitude gap `Delta>0`, define

```math
\boxed{a=u-\Delta,}
```

and decompose the lower excursion set `{t:z(t)>a}` into connected components. Count a component only if its maximum exceeds `u`; call the successful-component count `C_Delta`.

Pathwise,

```math
\boxed{\sup z>u\iff C_\Delta\ge1.}
```

For fixed `Delta`, the count remains finite on continuous compact paths even when raw level-`u` upcrossings proliferate.

Moment enclosure:

```math
\boxed{
\frac{E[C_\Delta]^2}{E[C_\Delta^2]}
\le P_FA
\le E[C_\Delta].
}
```

Choose a uniform time and condition on `z(T)>a`. Under the lower-level occupation-Palm law `Q_a`, let `L` be the selected lower-component duration, `S` indicate whether it reaches `u`, and `C_Delta` be the path's total successful count. Exact Fubini identities:

```math
\boxed{
E[C_\Delta]=\ell Q(a)E_{Q_a}[S/L],
}
```

```math
\boxed{
E[C_\Delta^2]=\ell Q(a)E_{Q_a}[S C_\Delta/L].
}
```

No derivative or micro-upcrossing statistic is used.

For the original task at `X=7.16`, `Delta=0.15`, representative `20000`-path results are

```text
kappa_f    detector    lower/alpha    upper/alpha
300        fast          0.98604        0.98624
300        slow          1.19896        1.19990
1000       fast          0.98417        0.98423
1000       slow          1.21537        1.21725
```

At the direct rough endpoint, using `50000` paths and grid spacing about `0.001`:

```text
             lower/alpha    upper/alpha    SE[E(C)]/alpha
fast           0.98940        0.98968          0.00429
slow           1.22367        1.22583          0.00474
```

**NUMERICAL ENDPOINT CERTIFICATE / CLUSTER-RENORMALIZED ENCLOSURE:** the cluster moment interval remains sharp at `kappa=infinity` and separates fast/slow at the same physical time. The high-band divergence in Step 32 was a property of raw crossing multiplicity, not the excursion event.

**OPEN:** the exact inequalities are analytic, but the displayed moments are finite-grid Monte Carlo estimates. The continuous interval from the Step-32 certificate (`kappa_f~170`) to `infinity` still needs adaptive bandwidth/grid/statistical certification.

Full derivation: `EXCURSION_CLUSTER_MOMENT_ENCLOSURE_STEP.md`.  
Calculator: `numerics/excursion_cluster_moment_enclosure.py`.

---

## Current stopping point

A cluster-renormalized finite-`u` variable now survives the rough limit and is sharp at representative high-band points plus the endpoint.

### Single natural next question

> Can the excursion-cluster enclosure be evaluated on an adaptive bandwidth grid with controlled Monte Carlo/grid error and optimized `Delta`, so that the entire interval from `kappa_f~170` to the rough endpoint is closed without the empirical Step-31 boundary fit?
