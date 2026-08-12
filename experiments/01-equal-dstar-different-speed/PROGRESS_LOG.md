# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 20:29 EDT:** compact chronology preserving every consequential result, correction, rejected shortcut, invalidation, numerical validation, asymptotic qualification, and current stopping point. Full derivations remain in dedicated step files.

---

## Steps 01–04 — scalar `D*`, full-observation equivalence, finite-window phase
Equal scalar reference `D*` does not determine arbitrary temporal-signal SNR; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation maximum-linear-SNR problem. **NEGATIVE RESULT:** unknown timing alone does not break that ideal equivalence. Finite windows can because magnitude `D*(f)` discards temporal phase/placement.

## Steps 05–12 — finite-record SNR and task boundary
Derived finite-record optimal SNR, deadline detection, and

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

In the controlled `t exp(-t/tau)` family, faster SNR accumulation can be offset by unknown-time search burden.

**REJECTED SHORTCUT:** finite-window SNR cannot be combined directly with full-template timing bandwidth.

**NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family.

## Step 13 — rough hard-window obstruction
Finite hard-window ideal-white-noise timing scan has

```math
R_x(y)=1-a_x|y|+... .
```

**FAILED NUMERICAL ESTIMATE:** rough-grid crossover `ell~49` invalid.

## Steps 14–17 — finite timing-information bandwidth and Palm rare events
A genuine information-band limitation removes the cusp. Exact smooth Palm identity:

```math
P_{FA}=Q(u)+\lambda_u E_\uparrow[1_{z(0)\le u}/N_u^+].
```

Rice/EC is an upper bound. For finite hard windows `sigma_kappa^2~a_x kappa/sqrt(pi)`, so Rice accuracy is nonuniform toward the rough limit.

## Step 18 — common physical bandwidth, accessible SNR forced equal
With `kappa_i=Omega_B tau_i`, crossover moves from electronics-limited `~1/Omega_B` to detector-limited `~tau_f`.

**NEGATIVE RESULT:** no finite bandwidth optimum under artificial equal-accessible-SNR normalization.

## Step 19 — fixed physical signal/noise; finite bandwidth optimum
Restoring bandwidth-dependent accessible SNR gives full-template SNR loss `O(kappa^-2)` but timing-search simplification `O(kappa^-1)`.

**DERIVED / CONDITIONAL:** a finite large-r bandwidth optimum exists. Later Palm validation confirms survival beyond Rice.

## Step 20 — finite-r Rice double reversal
For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=0.90`, `Lambda=0.895`, converged Rice gave apparent switches `25.4898402` and `130.1945883`.

## Step 21 — Palm correction changes topology
- lower switch survives at `kappa_f~21.7 +/-0.3`;
- **INVALIDATED:** upper Rice switch `130.1945883` is not a Palm switch;
- Palm checks at `130,160,300` keep fast preferred for `Lambda=0.895`.

## Step 22 — Palm boundary map and finite optimum
Representative finite-r Palm boundary:

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

High-band slow-preferred tasks survive above the lifted boundary. The large-r full-template Palm objective has a shallow finite optimum around `kappa~50–65`, only `~0.3–0.4%` above infinity.

## Step 23 — matched rough/smooth infinite-band limit
Derived

```math
R_x(y)=1-a_x|y|-b_x y^2/2+...,
\qquad
\chi_x=a_xu/\sqrt{b_x}.
```

At `kappa=infinity`, tangent variance is `t^2+sqrt(2)chi|t|`.

At `u~5`, introduced exact occupation-time rare-event identity

```math
P(\sup z>u)=\ell Q(u)E_{occ}[1/V_u].
```

Direct rough-limit boundary for the `r=2` calibration:

```math
\Lambda_{cross}^{\infty}\approx0.905\pm0.004,
\qquad X\approx7.75.
```

Thus `Lambda=0.895` remains fast-preferred at the rough endpoint.

## Step 24 — finite-band tangent bridge is two-parameter
Finite bandwidth adds

```math
\zeta_x=\kappa/(\sqrt2u\sqrt{b_x}).
```

The two-parameter tangent variogram connects the smooth finite-band and rough infinite-band fields.

**REJECTED SHORTCUT:** `H_mix(chi)` alone cannot control finite-band convergence.

## Step 25 — generalized Dieker–Yakir representation and monotonicity

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

## Step 26 — physical high-band derivative
For physical admissible timing intervals `A_f,A_s`, exact implicit differentiation gives

```math
\frac{d\Lambda_\times}{d\kappa}
=\frac{A_{f,X}A_{s,\kappa}-A_{s,X}A_{f,\kappa}}
{A_{f,X}-A_{s,X}}.
```

Finite-hard-window SNR recovery is `O(kappa^-1)`:

```math
\rho(x,\kappa)
=\rho_\infty(x)[1-a_x/(\sqrt\pi\kappa)+o(\kappa^{-1})].
```

Dieker–Yakir data support a positive `H_mix-H ~ C_H/sqrt(zeta)` law. Conditional on that law, the `r=2` boundary approaches the rough endpoint from above with eventual negative slope.

## Step 27 — exact Gaussian-mollifier coupling scale
Use one white-noise field for the rough Brownian endpoint and Gaussian-smoothed endpoint. The kernel is

```math
K_\zeta(t)=\sqrt2\zeta/\sqrt\pi\;e^{-2\zeta^2t^2}.
```

Exact deterministic gap:

```math
0\le|t|-F_\zeta(t)\le1/(\sqrt\pi\zeta).
```

Exact random difference scaling gives

```text
s_*   = 0.7016406021...
v_max = 0.2804576359...
```

and

```math
\sup_t SD[W_\infty-W_\zeta]_{random}
\le0.8906480701\sqrt{\chi/\zeta}.
```

**INVALIDATED INTERMEDIATE:** earlier `0.8131` coefficient used the large-lag variance instead of the true supremum.

A conservative fixed-window bound gives

```math
0\le H_{mix}-H\le C_\chi\sqrt{\log\zeta/\zeta}.
```

Paired simulations strongly resolve positive square-root scaling along the actual fast/slow endpoint `chi` values.

**NEGATIVE RESULT:** the coupling proves the scale but not a positive lower coefficient.

## Step 28 — 20:29 EDT — Bessel zoom-in identifies a positive mollifier coefficient
Let

```math
\sigma_\chi=2^{3/4}\sqrt\chi.
```

Around the unique rough-field maximum `tau_*`, Brownian-extremum zoom-in gives, under the standard stable-convergence conditions,

```math
\frac{M_\infty-W_\infty(\tau_*+\varepsilon s)}
{\sigma_\chi\sqrt\varepsilon}
\Longrightarrow R_*(s),
```

where `R_*` is a two-sided BES(3)-type extremal field and `epsilon=1/zeta`.

Gaussian smoothing acts through

```math
K_1(s)=\sqrt{2/\pi}\,e^{-2s^2}.
```

Define

```math
\mathcal M_K(R)
=\inf_u\int K_1(v)R(u-v)dv.
```

The mollified maximum has

```math
M_\infty-M_\zeta
=\sigma_\chi\zeta^{-1/2}\mathcal M_K(R_*)
+o_p(\zeta^{-1/2}).
```

Since the Gaussian kernel is strictly positive and a two-sided BES(3) profile is positive away from its unique zero,

```math
\boxed{\mathcal M_K(R_*)>0\quad a.s.}
```

The stationary high-pass residual has amplitude `O(sqrt(epsilon))` but correlation length `O(epsilon)`, so its contribution to the **integrated** Dieker–Yakir denominator averages down to `O_p(epsilon)` under the stated localization/moment conditions. It cannot cancel the `O_p(sqrt(epsilon))` maximum loss.

Hence, under uniform integrability,

```math
\boxed{
H_{mix}(\chi)-H(\chi,\zeta)
=\frac{C_H(\chi)}{\sqrt\zeta}+o(\zeta^{-1/2}),
}
```

with

```math
\boxed{
C_H(\chi)
=2^{3/4}\sqrt\chi\;
E[\Psi(W_\infty)\mathcal M_K(R_*)]
>0.
}
```

**REJECTED SHORTCUT:** do not assume `Psi` and the local Bessel functional are independent. Direct unweighted BES simulation gives `E[M_K]~0.87`, whereas the paired Pickands results imply an effective weighted factor around `0.67–0.70` in the tested cases.

**REFINEMENT:** Step 26's positive square-root sign now has a concrete Brownian-extremum mechanism rather than being only an empirical fit.

**OPEN:** existing Brownian zoom-in theorems do not give the quantitative uniform remainder needed to certify a finite exact onset bandwidth `K`.

Full derivation: `BESSEL_MOLLIFIER_CONTINUITY_STEP.md`.  
Diagnostic: `numerics/bessel_mollifier_continuity.py`.

---

## Current stopping point

The structural positivity gap is closed conditionally on standard stable Bessel zoom-in/localization/uniform-integrability assumptions. The remaining gap is quantitative.

### Single natural next question

> Can the Bessel/mollifier asymptotic be strengthened to a **uniform quantitative remainder bound** over the detector-relevant `chi` interval, so that a concrete finite `kappa_f=K` can be certified beyond which the exact fast/slow boundary is monotone decreasing and the remaining high-band re-entrant pocket can be ruled out?
