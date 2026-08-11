# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 19:38 EDT:** compact chronology preserving every consequential result, correction, rejected shortcut, invalidation, numerical validation, asymptotic qualification, and stopping point. Full derivations live in dedicated step files.

---

## Steps 01–04 — scalar `D*`, full-observation equivalence, finite-window phase
Equal scalar reference `D*` does not determine arbitrary temporal-signal SNR; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`. Complete magnitude `D*(f)` is sufficient for the restricted known-waveform/full-observation maximum-linear-SNR problem. **NEGATIVE RESULT:** unknown timing alone does not break that ideal equivalence. Finite windows can because magnitude `D*(f)` discards phase/temporal placement; causal all-pass construction removes the pure-delay loophole.

## Steps 05–12 — finite-record SNR, deadline detection, and task boundary
Derived `rho_t^2=<s_t,C_t^-1s_t>`, Gaussian deadline detection, and task-level `T_D(alpha,beta,L)`. In the controlled `t exp(-t/tau)` family, faster SNR accumulation can be offset by larger unknown-time search burden.

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
Restoring bandwidth-dependent accessible SNR gives wide-band SNR loss `O(1/kappa^2)` but timing-search simplification `O(1/kappa)`.

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
Derived

```math
R_x(y)=1-a_x|y|-\frac{b_x}{2}y^2+O(|y|^3)
```

and matching coordinate

```math
\chi_x=a_xu/\sqrt{b_x}.
```

At `kappa=infinity`, tangent variance is `t^2+sqrt(2)chi|t|`.

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
Exact Gaussian smoothing integral for the hard endpoint tail:

```math
J(y,\kappa)=
\frac{\pi|y|}{2}\operatorname{erf}(\kappa|y|/2)
+\frac{\sqrt\pi}{\kappa}[e^{-(\kappa y)^2/4}-1].
```

Finite bandwidth adds

```math
\zeta_x=\kappa/(\sqrt2u\sqrt{b_x}).
```

The tangent variogram is

```math
\begin{aligned}
g_{\chi,\zeta}(t)
&=t^2+\sqrt2\chi\Big[
|t|\operatorname{erf}(\zeta|t|)\\
&\qquad+(e^{-\zeta^2t^2}-1)/(\sqrt\pi\zeta)
\Big].
\end{aligned}
```

**REJECTED SHORTCUT:** the one-parameter `H_mix(chi)` is only the `zeta=infinity` endpoint and cannot control finite-band convergence.

## Step 25 — 19:38 EDT — generalized Dieker–Yakir representation and exact monotonicity
For

```math
W_{\chi,\zeta}(t)=\sqrt2\eta_{\chi,\zeta}(t)-g_{\chi,\zeta}(t),
```

quadratic variance growth allows the continuous generalized Dieker–Yakir representation

```math
\boxed{
\mathcal H(\chi,\zeta)
=E\left[\frac{\sup_t e^{W(t)}}{\int e^{W(t)}dt}\right].
}
```

Efficient simulation decomposition:

```math
\eta_{\chi,\zeta}(t)
=Zt+2^{1/4}\sqrt\chi B_\zeta(t),
```

where `B_zeta'(t)` is stationary Gaussian with covariance

```math
E[B_\zeta'(0)B_\zeta'(t)]
=\frac{\zeta}{\sqrt\pi}e^{-\zeta^2t^2}.
```

Hence finite-`zeta` simulation is FFT synthesis of a smooth stationary derivative followed by one integration.

Exact derivatives:

```math
\partial_\zeta g
=\frac{\sqrt2\chi}{\sqrt\pi\zeta^2}(1-e^{-\zeta^2t^2})\ge0,
```

```math
\partial_\chi g=\sqrt2F_\zeta(t)\ge0.
```

Brown–Resnick Slepian comparison yields

```math
\boxed{
\partial_\zeta\mathcal H\ge0,
\qquad
\partial_\chi\mathcal H\ge0.
}
```

and

```math
\boxed{
1/\sqrt\pi\le H(\chi,\zeta)\le H_{mix}(\chi).
}
```

Representative Dieker–Yakir estimates for `chi=0.1`:

```text
zeta      H_hat
1         0.58683 +/-0.00054
3         0.62310 +/-0.00092
9         0.67671 +/-0.00111
19        0.70538 +/-0.00117
40        0.72422 +/-0.00151
infinity  0.76698 +/-0.00105
```

Grid refinement at `zeta=9,19` is below Monte Carlo uncertainty; `chi=0` reproduces exact `1/sqrt(pi)`.

**REFINEMENT:** the local generalized Pickands constant cannot oscillate with bandwidth. Any bounded re-entrant detector-preference pocket must come from the coupled bandwidth dependence of SNR, threshold, decision time, `chi`, and `zeta` for the two detectors.

**REJECTED SHORTCUT:** monotonicity of `H` does not by itself prove monotonicity of `Lambda_cross(kappa_f)`.

Full derivation: `TWO_PARAMETER_PICKANDS_DY_STEP.md`.  
Code: `numerics/two_parameter_pickands_dy.py`.

---

## Current stopping point

The local extreme constant is now both efficiently computable and rigorously coordinatewise monotone. The remaining question is the sign of the *physical boundary derivative* along the actual fast/slow trajectories.

### Single natural next question

> Can deterministic Dieker–Yakir estimates of `H(chi,zeta)` be inserted into the finite-`u` boundary equation and asymptotically expanded along the actual fast and slow detector trajectories to determine the sign of `d Lambda_cross / d kappa_f` at high bandwidth?
