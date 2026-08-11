# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 19:21 EDT:** compact chronology preserving every consequential result, correction, rejected shortcut, invalidation, numerical validation, asymptotic qualification, and stopping point. Full derivations live in dedicated step files.

---

## Steps 01–04 — scalar `D*`, full-observation equivalence, finite-window phase
Equal scalar reference `D*` does not determine arbitrary temporal-signal SNR; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`. Complete magnitude `D*(f)` is sufficient for the restricted known-waveform/full-observation maximum-linear-SNR problem. **NEGATIVE RESULT:** unknown timing alone does not break that ideal equivalence. Finite windows can because magnitude `D*(f)` discards phase/temporal placement; causal all-pass construction removes the pure-delay loophole.

## Steps 05–12 — finite-record SNR, deadline detection, and task boundary
Derived `rho_t^2=<s_t,C_t^-1s_t>`, Gaussian deadline detection, and task-level `T_D(alpha,beta,L)`. Unknown timing raises a global threshold governed by timing-scan covariance rather than digital sample count. In the controlled `t exp(-t/tau)` family, faster SNR accumulation can be offset by larger unknown-time search burden.

**REJECTED SHORTCUT:** finite-window SNR cannot be combined directly with full-template timing bandwidth.

**NEGATIVE RESULT:** no finite interior integration-duration optimum exists in the original scaled family.

## Step 13 — rough finite-window obstruction
`R_x(y)=1-a_x|y|+...`; the ideal-white-noise finite hard-window scan is locally Brownian-like.

**FAILED NUMERICAL ESTIMATE:** Step-13 rough-grid `ell~49` crossover is invalid.

## Steps 14–15 — genuine finite timing-information bandwidth
**REJECTED SHORTCUT:** an invertible common low-pass is not necessarily a true information-band limit because whitening can undo it. Smooth Gaussian information weighting removes the cusp and gives controlled correlated-scan numerics.

## Step 16 — exact smooth Palm rare-event identity

```math
P_{FA}=Q(u)+\lambda_u E_\uparrow[1_{z(0)\le u}/N_u^+].
```

Rice/EC is an upper bound; Palm importance sampling makes `alpha=1e-6` practical.

## Step 17 — nonuniform Rice limit and extreme speed ratio
For finite hard windows `sigma_kappa^2~a_x kappa/sqrt(pi)`, so Rice accuracy is nonuniform as bandwidth grows. Co-scaled large-r crossover tends to the fast full-template feasibility edge.

## Step 18 — common physical bandwidth, accessible SNR forced equal
With `kappa_i=Omega_B tau_i`, crossover moves from electronics-limited `~1/Omega_B` to detector-limited `~tau_f`.

**NEGATIVE RESULT:** no finite bandwidth optimum under artificial equal-accessible-SNR normalization.

## Step 19 — fixed physical signal/noise; finite bandwidth optimum
Restoring bandwidth-dependent accessible SNR gives wide-band SNR loss `O(1/kappa^2)` but timing-search simplification `O(1/kappa)`.

**DERIVED / CONDITIONAL:** large-r Rice unknown-time objective has a finite bandwidth optimum. Palm validation later confirms the optimum survives exact rare-event correction.

## Step 20 — finite-r Rice double reversal
For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=0.90`, `Lambda=0.895`, converged finite-duration Rice gave apparent switches `25.4898402` and `130.1945883`, i.e. apparent `slow -> fast -> slow`.

## Step 21 — Palm correction changes topology
Use `u_avail=rho(x)-Phi^-1(beta)` and test `P_FA^Palm(u_avail)<=alpha` directly.

- lower switch survives at `kappa_f~21.7 +/-0.3`;
- **INVALIDATED:** upper Rice switch `130.1945883` is not a Palm switch;
- Palm checks at `kappa_f=130,160,300` keep fast preferred for `Lambda=0.895`;
- cause: nonuniform Rice micro-upcrossing overcount, strongest for the shorter slow-detector finite window.

## Step 22 — Palm boundary map and survival of finite optimum
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

**REFINEMENT:** high-band slow-preferred tasks survive; Palm lifts the boundary above the old `Lambda=0.895` slice rather than eliminating the slow-preferred region.

Higher-statistics large-r full-template Palm scan:

```text
kappa       ell_crit^Palm
50          ~0.91162
55          ~0.91185
60          ~0.9120
65          ~0.91136
infinity    ~0.90897
```

**NUMERICAL VALIDATION / CONDITIONAL:** finite bandwidth optimum survives Palm correction. It is broad (`kappa~50–65`) and shallow (`~0.3–0.4%` gain over infinite bandwidth).

## Step 23 — matched infinite-band rough/smooth limit
Derived exact finite-hard-window covariance and local expansion

```math
R_x(y)=1-a_x|y|-\frac{b_x}{2}y^2+O(|y|^3),
```

with

```math
a_x=\frac{2x^2e^{-2x}}{\eta(x)},
\qquad
b_x=\frac{1+e^{-2x}(2x^2-2x-1)}{\eta(x)}.
```

At threshold `u`, the `kappa=infinity` rough/smooth high-excursion field is organized by

```math
\boxed{\chi_x=a_xu/\sqrt{b_x}}.
```

On `q(u)=sqrt(2)/(u sqrt(b_x))`, tangent variance is

```math
\operatorname{Var}\eta_\chi(t)=t^2+\sqrt2\chi|t|.
```

A generalized Pickands constant `H_mix(chi)` bridges smooth and rough high-threshold limits.

Because `u~5`, leading asymptotics retain percent-level finite-threshold error. Derived exact rough-process occupation identity

```math
P(\sup z>u)=\ell Q(u)E_{occ}[1/V_u].
```

Direct `kappa=infinity` occupation-time importance sampling for the `r=2` calibration gives

```math
\Lambda_{cross}^{kappa=\infty}\approx0.905\pm0.004,
\qquad X_{cross}\approx7.75.
```

**REFINEMENT:** `Lambda=0.895` is fast-preferred in the direct infinite-band rough limit; the invalid Step-20 upper reversal does not reappear asymptotically.

**OPEN:** a bounded re-entrant pocket at untested very high finite bandwidth was not yet excluded.

## Step 24 — 19:21 EDT — finite-band tangent bridge is two-parameter
The Step-23 one-parameter `H_mix(chi)` was tested as a possible deterministic finite-band continuation and rejected as incomplete.

The hard endpoint gives a universal `1/nu^2` tail. Under the Gaussian information cutoff,

```math
J(y,\kappa)
=\int_0^\infty\frac{1-\cos(\nu y)}{\nu^2}e^{-(\nu/\kappa)^2}d\nu
```

has the exact form

```math
\boxed{
J(y,\kappa)=
\frac{\pi|y|}{2}\operatorname{erf}(\kappa|y|/2)
+\frac{\sqrt\pi}{\kappa}[e^{-(\kappa y)^2/4}-1].
}
```

Matching to the hard-window coefficients gives

```math
1-R_{x,\kappa}(y)
\sim\frac{b_x}{2}y^2+\frac{2a_x}{\pi}J(y,\kappa).
```

For `kappa|y|<<1`,

```math
-R_{x,\kappa}''(0)
\sim b_x+\frac{a_x\kappa}{\sqrt\pi},
```

which recovers the Step-17 curvature growth directly.

On the high-excursion scale, finite bandwidth introduces a second coordinate

```math
\boxed{
\zeta_x=\frac{\kappa}{\sqrt2u\sqrt{b_x}}.
}
```

Together with

```math
\chi_x=\frac{a_xu}{\sqrt{b_x}},
```

the tangent variogram is

```math
\boxed{
\begin{aligned}
g_{\chi,\zeta}(t)
&=t^2+\sqrt2\chi\Bigg[
|t|\operatorname{erf}(\zeta|t|)\\
&\qquad+\frac{e^{-\zeta^2t^2}-1}{\sqrt\pi\zeta}
\Bigg].
\end{aligned}
}
```

Limits:

```math
g_{\chi,\infty}(t)=t^2+\sqrt2\chi|t|
```

recovers Step 23; `zeta->0` recovers a purely quadratic finite-band tangent.

Define the two-parameter generalized constant `H(chi,zeta)` from this stationary-increment tangent field. Then

```math
\boxed{H(chi,\infty)=H_mix(chi).}
```

**REJECTED SHORTCUT / REFINEMENT:** `H_mix(chi)` alone cannot determine finite-band convergence or rule out a bounded re-entrant pocket. At least the two-parameter object `H(chi,zeta)` plus finite-`u` control is required.

Full derivation: `FINITE_BAND_TANGENT_BRIDGE_STEP.md`.  
Calculator: `numerics/finite_band_tangent_bridge.py`.

---

## Current stopping point

The local finite-band problem is now reduced to a two-parameter generalized Pickands field.

### Single natural next question

> Can `H(chi,zeta)` be evaluated efficiently using a Dieker–Yakir representation, and does its dependence on `zeta` have enough monotonic structure to control the finite-band approach and rule out a bounded re-entrant preference pocket?
