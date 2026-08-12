# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 19:48 EDT:** compact chronology preserving every consequential result, correction, rejected shortcut, invalidation, numerical validation, asymptotic qualification, and stopping point. Full derivations live in dedicated step files.

---

## Steps 01–04 — scalar `D*`, full-observation equivalence, finite-window phase
Equal scalar reference `D*` does not determine arbitrary temporal-signal SNR; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation maximum-linear-SNR problem. **NEGATIVE RESULT:** unknown timing alone does not break that ideal equivalence. Finite windows can because magnitude `D*(f)` discards phase/temporal placement.

## Steps 05–12 — finite-record SNR, deadline detection, and task boundary
Derived `rho_t^2=<s_t,C_t^-1s_t>`, Gaussian deadline detection, and task-level `T_D(alpha,beta,L)`. In the controlled `t exp(-t/tau)` family, faster SNR acquisition can be offset by larger unknown-time search burden.

**REJECTED SHORTCUT:** finite-window SNR cannot be combined directly with full-template timing bandwidth.

**NEGATIVE RESULT:** no finite interior integration-duration optimum exists in the original scaled family.

## Step 13 — rough finite-window obstruction
`R_x(y)=1-a_x|y|+...`; ideal-white-noise hard-window scan is locally Brownian-like.

**FAILED NUMERICAL ESTIMATE:** Step-13 `ell~49` crossover is invalid.

## Steps 14–17 — genuine timing bandwidth and exact Palm rare events
A genuine information-band limitation removes the cusp. Exact smooth Palm identity:

```math
P_{FA}=Q(u)+\lambda_u E_\uparrow[1_{z(0)\le u}/N_u^+].
```

Rice/EC is an upper bound. For finite hard windows `sigma_kappa^2~a_x kappa/sqrt(pi)`, so Rice accuracy is nonuniform as bandwidth grows.

## Step 18 — common physical bandwidth, accessible SNR forced equal
With `kappa_i=Omega_B tau_i`, crossover moves from electronics-limited `~1/Omega_B` to detector-limited `~tau_f`.

**NEGATIVE RESULT:** no finite bandwidth optimum under artificial equal-accessible-SNR normalization.

## Step 19 — fixed physical signal/noise; finite bandwidth optimum
Restoring bandwidth-dependent accessible SNR gives full-template SNR loss `O(1/kappa^2)` but timing-search simplification `O(1/kappa)`.

**DERIVED / CONDITIONAL:** large-r Rice objective has a finite bandwidth optimum. Later Palm validation confirms survival beyond Rice.

## Step 20 — finite-r Rice double reversal
For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=0.90`, `Lambda=0.895`, converged Rice gave apparent switches `25.4898402` and `130.1945883`.

## Step 21 — Palm correction changes topology
- lower switch survives at `kappa_f~21.7 +/-0.3`;
- **INVALIDATED:** upper Rice switch `130.1945883` is not a Palm switch;
- Palm checks at `130,160,300` keep fast preferred for `Lambda=0.895`.

## Step 22 — Palm boundary map and survival of finite optimum
Representative finite-r boundary:

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

**REFINEMENT:** high-band slow-preferred tasks survive above the lifted boundary.

Large-r Palm scan has a shallow finite optimum near `kappa~50–65`, about `0.3–0.4%` above infinity.

## Step 23 — matched infinite-band rough/smooth limit
Derived exact finite-hard-window local expansion `R_x(y)=1-a_x|y|-b_x y^2/2+...` and matching coordinate `chi_x=a_xu/sqrt(b_x)`. At `kappa=infinity`, tangent variance is `t^2+sqrt(2)chi|t|`.

Because `u~5`, introduced exact occupation-time rare-event identity

```math
P(\sup z>u)=\ell Q(u)E_{occ}[1/V_u].
```

Direct rough-limit boundary for the `r=2` calibration:

```math
\Lambda_{cross}^{\infty}\approx0.905\pm0.004,
\qquad X\approx7.75.
```

Thus `Lambda=0.895` stays fast-preferred at the rough endpoint.

## Step 24 — finite-band tangent bridge is two-parameter
Finite bandwidth adds

```math
\zeta_x=\kappa/(\sqrt2u\sqrt{b_x}).
```

The two-parameter tangent variogram continuously connects the smooth finite-band and rough infinite-band fields.

**REJECTED SHORTCUT:** `H_mix(chi)` alone cannot control finite-band convergence.

## Step 25 — generalized Dieker–Yakir representation and exact monotonicity
The two-parameter generalized Pickands constant has the continuous Dieker–Yakir representation

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

## Step 26 — 19:48 EDT — coupled high-band physical derivative
Let `A_f(X,kappa)` and `A_s(X,kappa)` denote admissible physical timing uncertainty from the two channels. Their common-time equality gives the exact implicit derivative

```math
\boxed{
\frac{d\Lambda_\times}{d\kappa}
=\frac{A_{f,X}A_{s,\kappa}-A_{s,X}A_{f,\kappa}}
{A_{f,X}-A_{s,X}}.
}
```

For a **finite hard window**, endpoint spectral leakage gives

```math
\boxed{
\rho(x,\kappa)=\rho_\infty(x)
[1-a_x/(\sqrt\pi\kappa)+o(\kappa^{-1})].
}
```

Thus finite-window SNR recovery is `O(kappa^-1)`.

Step-25 Dieker–Yakir values at `chi=0.1` satisfy an exceptionally clean

```math
H_{mix}-H(\chi,\zeta)\propto\zeta^{-1/2}
```

sequence over `zeta=9,19,40`. Additional endpoint-trajectory runs support the same rate at approximately `chi_fast~1.1e-4` and `chi_slow~6.4e-2`.

**NUMERICAL ASYMPTOTIC / NOT YET A THEOREM:** assume

```math
H_{mix}(\chi)-H(\chi,\zeta)
=C_H(\chi)\zeta^{-1/2}+O(\zeta^{-1}),
\qquad C_H>0.
```

Then local extreme-statistics recovery is `O(kappa^-1/2)`, which dominates the finite-window SNR correction `O(kappa^-1)`.

The coupled physical boundary therefore has

```math
\boxed{
\Lambda_\times(\kappa_f)
=\Lambda_\infty+C_\Lambda\kappa_f^{-1/2}+O(\kappa_f^{-1}).
}
```

For the `r=2` calibration, the finite-u tangent surrogate gives roughly

```text
A_f,X ~4.9e-3
A_s,X ~4.5e-1
C_H,fast ~0.006
C_H,slow ~0.20
C_Lambda ~+2e-2
```

so the leading derivative is negative:

```math
\boxed{d\Lambda_\times/d\kappa_f<0}
```

for sufficiently large bandwidth.

**REFINEMENT / CONDITIONAL:** the high-band boundary approaches the direct rough endpoint from above. Any hypothetical additional slow-preferred pocket must therefore be bounded and pre-asymptotic; it cannot persist or recur arbitrarily far into the high-band tail.

**OPEN:** prove the square-root smoothing law and a uniform remainder strongly enough to certify a finite bandwidth beyond which the exact-process boundary is guaranteed monotone decreasing.

Full derivation: `HIGH_BAND_BOUNDARY_DERIVATIVE_STEP.md`.  
Calculator: `numerics/high_band_boundary_derivative.py`.

---

## Current stopping point

The coupled detector trajectory has an eventual negative boundary slope **conditional on the numerically stable `zeta^-1/2` generalized-Pickands convergence law**. The remaining task is to turn that observed local smoothing rate into a rigorous bound with a certified onset bandwidth.

### Single natural next question

> Can `H_mix(chi)-H(chi,zeta) ~ C_H(chi)/sqrt(zeta)` be derived or bounded rigorously for the Gaussian-smoothed Brownian endpoint field, with a uniform remainder strong enough to certify a finite `kappa` beyond which the exact detector boundary must be monotone decreasing?
