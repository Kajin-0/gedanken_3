# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 21:39 EDT:** compact chronology preserving consequential results, corrections, invalidations, rejected shortcuts, numerical validations, asymptotic qualifications, and current stopping point. Full derivations remain in dedicated step files.

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
For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=0.90`, `Lambda=0.895`, Rice gave switches `25.4898402` and `130.1945883`. Palm preserves only the lower switch `kappa_cross~21.7 +/-0.3`. **INVALIDATED:** upper Rice switch. Palm checks at `130,160,300` keep fast preferred.

## Step 22
Palm boundary rises to about `Lambda~0.91` at moderate/high finite bandwidth. High-band slow-preferred tasks survive above it. Large-`r` Palm optimum broad near `kappa~50–65`, about `0.3–0.4%` above infinity.

## Step 23
Matched rough/smooth finite-window limit and exact occupation-time importance sampling. Direct rough endpoint: `Lambda_cross^infinity~0.905 +/-0.004`; `Lambda=0.895` remains fast-preferred.

## Step 24
Finite bandwidth adds `zeta=kappa/(sqrt(2)u sqrt(b))`. **REJECTED SHORTCUT:** `H_mix(chi)` alone is only the infinite-band endpoint.

## Step 25
Generalized Pickands constant has continuous Dieker–Yakir representation. Brown–Resnick Slepian comparison proves monotonicity in `chi,zeta`, but not monotonicity of the physical detector boundary.

## Step 26
Exact implicit physical boundary derivative derived. Finite-hard-window SNR recovery is `O(kappa^-1)`. Positive `H_mix-H~C_H/sqrt(zeta)` would force eventual negative boundary slope.

## Step 27
Common-white-noise coupling gives exact `O(sqrt(chi/zeta))` path-amplitude scale and conservative convergence bound. **INVALIDATED INTERMEDIATE:** `0.8131` coupling coefficient; correct pointwise RMS coefficient is `0.8906480701`. Coupling alone gives no positive lower coefficient.

## Step 28
Two-sided-BES(3) Brownian-extremum zoom-in plus Gaussian mollification identifies a positive `zeta^-1/2` coefficient under stable convergence/localization/UI. Dieker–Yakir denominator is lower order. Quantitative finite-band remainder remains open.

## Steps 29–30
Small `chi` introduces Brownian–parabola scales

```math
h_chi=sqrt(2) chi^(1/3),
\qquad m_chi=2chi^(2/3),
\qquad mu=sqrt(2)zeta chi^(1/3).
```

At the `r=2` endpoint, `mu_f~0.009776 kappa_f`, `mu_s~0.16139 kappa_f`. The small-`chi` crossover reduces to the canonical Brownian-minus-parabola maximum loss

```math
F(mu)=\frac{2}{\sqrt\pi}E[M_inf-M_mu].
```

Representative continuum values: `F(0)~.892`, `F(.5,1,2,3,5,10,20)~.806,.729,.597,.512,.410,.297,.213`; `sqrt(mu)F(mu)->~0.98`. Nested-grid full fast-channel calculations agree at percent level. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` fast values were biased low by rough-maximum grid under-resolution. Fast endpoint asymptotic `C_H` refines to about `0.0088`.

## Step 31
Insert `F(mu)` into the finite-`u` coupled tangent boundary and anchor the residual finite-threshold offset to Palm points plus the rough endpoint. Central bridge has one shallow maximum near `kappa_f~94.9`, `Lambda~0.91068`, then decreases toward `Lambda_infinity~0.90513`. **NUMERICAL CLOSURE:** for the original `Lambda=0.895` task, no bounded high-band re-entrant pocket is numerically supported. **CONDITIONAL:** the finite-`u` offset was empirical.

## Step 32 — 21:39 EDT — direct finite-`u` Rice moment enclosure
For a smooth finite-band scan define

```math
X_u=1_{\{z(0)\le u\}}N_u^+.
```

Then exactly

```math
P_FA=Q(u)+P(X_u\ge1).
```

With

```math
m_1=E[X_u],
\lambda=E[N_u^+],
\lambda_2=E[N_u^+(N_u^+-1)],
```

Cauchy–Schwarz and `X_u^2 <= (N_u^+)^2` give the finite-threshold enclosure

```math
\boxed{
Q(u)+\frac{m_1^2}{\lambda+\lambda_2}
\le P_FA
\le Q(u)+m_1.
}
```

`m_1` is the ordinary Rice mean minus an endpoint-above overlap integral; `lambda_2` is a second-order Rice integral. Both are computed deterministically from `R,R',R''` of the finite-band Gaussian scan.

For the original task at common time `X=7.04`:

```text
kappa_f   fast upper/alpha   slow lower/alpha
100           0.99737             1.04649
130           0.99861             1.02562
160           0.99961             1.00950
170           0.99990             1.00491
175           1.00004             1.00275
```

Thus fast preference is directly enclosed through at least `kappa_f=170` in the tested sequence, without Step-31's empirical finite-`u` bridge. Resolution refinement at `kappa_f=160` changes the displayed ratios only in the last few `1e-6` relative digits.

**NEGATIVE RESULT:** around `kappa_f~175–200` the second-moment enclosure loses separation because the slow channel's `lambda_2` grows rapidly from clustered micro-upcrossings. This is exactly the nonuniform clustering mechanism that invalidated raw Rice counting earlier; it is not evidence for a renewed detector-preference reversal.

Full derivation: `FINITE_U_RICE_MOMENT_ENCLOSURE_STEP.md`.  
Calculator: `numerics/finite_u_rice_moment_enclosure.py`.

---

## Current stopping point

The finite-`u` correction is now directly bounded over a substantial high-band interval. The remaining hard regime is specifically the roughening slow-channel tail where many micro-upcrossings belong to one physical excursion.

### Single natural next question

> Can an excursion-cluster or occupation-time variable replace raw upcrossing multiplicity so that a finite-`u` moment enclosure remains sharp as `kappa_f -> infinity`, extending the Step-32 direct certificate continuously to the rough endpoint?
