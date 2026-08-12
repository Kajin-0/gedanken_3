# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 20:09 EDT  
**Status:** twenty-seven logical steps completed. Step 27 constructs the finite-band tangent field and the infinite-band Brownian endpoint on one white-noise probability space. The coupling proves an exact `O(zeta^-1/2)` pointwise path-amplitude scale, an explicit uniform drift/variogram gap, and a conservative `O(sqrt(log zeta/zeta))` convergence envelope for the generalized Dieker–Yakir functional. A paired common-random-number estimator gives much sharper numerical evidence for a positive `1/sqrt(zeta)` Pickands correction along the actual fast/slow endpoint trajectories. However, a rigorous positive lower asymptotic coefficient is still missing, so no exact finite onset bandwidth `K` for monotone boundary decrease has yet been certified. No universal replacement metric and no novelty claim.

---

## 1. Original question

Two hypothetical detectors satisfy

```math
D_A^*=D_B^*
```

but initially have

```math
\tau_A=1\ \mathrm{ns},
\qquad
\tau_B=1\ \mathrm{s}.
```

Does equal conventional specific detectivity imply equal ability to detect an arbitrary optical signal?

---

## 2. Surviving logical chain

### Steps 01–04 — scalar `D*`, full-observation equivalence, finite-window phase
- Equal reference scalar `D*` does not guarantee equal arbitrary temporal-signal SNR; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`.
- For known waveform/full observation, `rho_inf^2 = integral |P|^2 |G|^2/S_n df = A^-1 integral |P|^2 D*^2 df`.
- **NEGATIVE RESULT:** unknown timing alone does not break complete-magnitude `D*(f)` equivalence under stationary Gaussian full observation.
- Finite windows can break equivalence because magnitude `D*(f)` discards temporal phase/placement.

### Steps 05–12 — finite-record SNR and task-level boundary

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
```

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

For the controlled `t exp(-t/tau)` family, faster SNR acquisition can be offset by larger unknown-time search burden.

**REJECTED SHORTCUT:** finite-window SNR cannot be combined directly with full-template timing bandwidth as one exact statistic.

**NEGATIVE RESULT:** no finite interior integration-duration optimum exists in the original scaled family.

### Step 13 — rough hard-window obstruction

```math
R_x(y)=1-a_x|y|+O(y^2),
\qquad a_x=2x^2e^{-2x}/\eta(x).
```

The ideal-white-noise finite-window scan is locally Brownian-like.

**FAILED NUMERICAL ESTIMATE:** the rough-grid Step-13 crossover near `ell~49` is invalid.

### Steps 14–17 — genuine timing bandwidth and exact rare-event structure
Use smooth information weighting `|H_x(nu)|^2 exp[-(nu/kappa)^2]`. Finite `kappa` removes the covariance cusp.

Exact smooth Palm identity:

```math
P_{FA}=Q(u)+\lambda_u E_\uparrow[1_{\{z(0)\le u\}}/N_u^+].
```

Rice/EC is an upper bound. For finite hard windows `sigma_kappa^2~a_x kappa/sqrt(pi)`, so Rice accuracy is nonuniform toward the rough limit.

### Steps 18–19 — shared physical bandwidth and a genuine finite optimum
With `kappa_i=Omega_B tau_i`, forcing accessible eventual SNR equal gives electronics- and detector-limited regimes but **no** finite bandwidth optimum.

Holding physical signal/noise fixed instead restores bandwidth-dependent SNR. For the full template, SNR loss is `O(kappa^-2)` while timing-search simplification is `O(kappa^-1)`, producing a finite large-r optimum. Later Palm work confirms a shallow finite optimum survives beyond Rice.

### Steps 20–21 — finite-r Rice double reversal corrected by Palm
For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=0.90`, `Lambda=0.895`, converged Rice gave apparent switches `25.4898402` and `130.1945883`.

Palm correction gives

```math
\boxed{\kappa_{\times,1}^{Palm}\approx21.7\pm0.3}
```

for the surviving lower switch and **INVALIDATES** the upper Rice switch. Palm checks at `kappa_f=130,160,300` keep fast preferred for `Lambda=0.895`.

### Step 22 — Palm boundary map and Palm finite optimum
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

**REFINEMENT:** high-band slow-preferred tasks survive above the lifted boundary.

Large-r full-template Palm scan has a shallow finite optimum near `kappa~50–65`, only `~0.3–0.4%` above the infinite-band boundary.

### Step 23 — matched infinite-band rough/smooth limit
Exact local expansion:

```math
R_x(y)=1-a_x|y|-\frac{b_x}{2}y^2+O(|y|^3).
```

Infinite-band matching coordinate:

```math
\chi_x=a_xu/\sqrt{b_x}.
```

On the high-excursion scale, tangent variance is `t^2+sqrt(2)chi|t|`.

At `u~5`, leading asymptotics are insufficient. Exact occupation-time identity:

```math
P(\sup z>u)=\ell Q(u)E_{occ}[1/V_u].
```

Direct rough-limit calculation gives

```math
\Lambda_{cross}^{\infty}\approx0.905\pm0.004,
\qquad X\approx7.75.
```

Thus `Lambda=0.895` is fast-preferred at the rough endpoint too.

### Step 24 — finite-band tangent bridge is two-parameter
Finite bandwidth introduces

```math
\zeta_x=\kappa/(\sqrt2u\sqrt{b_x}).
```

Together with `chi`, the tangent variogram is

```math
\begin{aligned}
g_{\chi,\zeta}(t)
&=t^2+\sqrt2\chi\Big[
|t|\operatorname{erf}(\zeta|t|)\\
&\qquad+(e^{-\zeta^2t^2}-1)/(\sqrt\pi\zeta)
\Big].
\end{aligned}
```

**REJECTED SHORTCUT:** the one-parameter `H_mix(chi)` is only the `zeta=infinity` endpoint.

### Step 25 — generalized Dieker–Yakir representation and exact monotonicity

```math
\mathcal H(\chi,\zeta)
=E\left[\frac{\sup_t e^{W(t)}}{\int e^{W(t)}dt}\right].
```

Efficient simulation uses FFT synthesis of a stationary Gaussian derivative and one integration.

Brown–Resnick Slepian comparison gives

```math
\partial_\zeta H\ge0,
\qquad
\partial_\chi H\ge0.
```

**REFINEMENT:** the local extreme constant cannot oscillate with bandwidth, but this alone does not make the physical detector boundary monotone.

### Step 26 — coupled physical high-band derivative
Let `A_f(X,kappa)` and `A_s(X,kappa)` be admissible physical timing uncertainty from the fast and slow channels. Their common-time equality gives

```math
\boxed{
\frac{d\Lambda_\times}{d\kappa}
=\frac{A_{f,X}A_{s,\kappa}-A_{s,X}A_{f,\kappa}}
{A_{f,X}-A_{s,X}}.
}
```

For a finite hard window,

```math
\rho(x,\kappa)
=\rho_\infty(x)
[1-a_x/(\sqrt\pi\kappa)+o(\kappa^{-1})],
```

so finite-window SNR recovery is `O(kappa^-1)`.

Dieker–Yakir data support

```math
H_{mix}(\chi)-H(\chi,\zeta)
\approx C_H(\chi)\zeta^{-1/2},
\qquad C_H>0.
```

**NUMERICAL ASYMPTOTIC / NOT YET A THEOREM:** conditional on that law,

```math
\Lambda_\times(\kappa_f)
=\Lambda_\infty+C_\Lambda\kappa_f^{-1/2}+O(\kappa_f^{-1}),
```

with `C_Lambda>0` for the `r=2` calibration, hence eventual negative boundary slope and approach to the rough endpoint from above.

### Step 27 — exact Gaussian-mollifier coupling scale
Use one white-noise field for the Brownian endpoint `B_infinity` and its Gaussian-smoothed version `B_zeta`. The smoothing amplitude transfer is

```math
e^{-\omega^2/(8\zeta^2)},
```

with time-domain kernel

```math
K_\zeta(t)=\sqrt{2}\zeta/\sqrt\pi\;e^{-2\zeta^2t^2}.
```

The deterministic variance gap obeys exactly

```math
\boxed{
0\le |t|-F_\zeta(t)\le\frac1{\sqrt\pi\zeta}.
}
```

For the coupled random difference `D_zeta=B_infinity-B_zeta`,

```math
\operatorname{Var}D_\zeta(t)
=\frac1\zeta v(\zeta|t|),
```

with

```math
v(s)=s+f(s)-\sqrt2 f(\sqrt2s),
```

and explicit maximum

```text
s_*       = 0.7016406021...
v(s_*)    = 0.2804576359...
```

Therefore the random part of the Brown–Resnick spectral-field perturbation satisfies

```math
\boxed{
\sup_t SD[W_\infty-W_\zeta]_{random}
\le0.8906480701\frac{\sqrt\chi}{\sqrt\zeta}.
}
```

**INVALIDATED INTERMEDIATE:** an earlier in-turn coefficient `0.8131` used the large-lag variance instead of the true supremum and must not be reused.

On a fixed Dieker–Yakir truncation interval, Gaussian maximal inequalities plus the exact coupling give the conservative envelope

```math
\boxed{
0\le H_{mix}(\chi)-H(\chi,\zeta)
\le C_\chi\sqrt{\frac{\log\zeta}{\zeta}}
}
```

for large `zeta`.

A paired common-random-number Dieker–Yakir estimator sharply reduces sampling variance. Representative normalized gaps:

```text
chi_fast ~1.14e-4:
  zeta=20: 0.00579 +/-0.00005
  zeta=40: 0.00651 +/-0.00004
  zeta=80: 0.00681 +/-0.00006

chi_slow ~0.0645:
  zeta=20: 0.2037 +/-0.0015
  zeta=40: 0.2072 +/-0.0014
  zeta=80: 0.2116 +/-0.0021

chi=0.1:
  zeta=20: 0.2757 +/-0.0021
  zeta=40: 0.2760 +/-0.0021
  zeta=80: 0.2783 +/-0.0028
```

where each reported number is `sqrt(zeta)[H_mix-H(chi,zeta)]`.

**NUMERICAL VALIDATION / NUMERICAL ASYMPTOTIC:** the positive square-root correction is now much more sharply resolved numerically and has an exact `O(sqrt(chi/zeta))` pathwise origin.

**NEGATIVE RESULT:** the coupling is still an upper-scale argument. It does not by itself prove a positive lower bound `c(chi)/sqrt(zeta)`, so it does not yet certify a finite exact `K` beyond which the detector boundary derivative is guaranteed negative.

Primary related Brownian results show exact `sqrt(delta)` continuity corrections for **grid discretization** and a two-sided-Bessel zoom-in law around Brownian extrema, but Gaussian mollification is a different approximation and cannot inherit that theorem without a new argument.

See `GAUSSIAN_MOLLIFIER_COUPLING_STEP.md` and `numerics/gaussian_mollifier_coupling.py`.

---

## 3. Current frontier

The square-root smoothing **scale** is now derived exactly. What remains is specifically a positive continuity-correction theorem at the random Brownian maximum.

### Single next question — DO NOT ANSWER YET

> Can the Brownian-extremum zoom-in / two-sided-Bessel theorem be adapted from grid discretization to Gaussian mollification of the Dieker–Yakir spectral field, yielding a positive kernel-specific continuity-correction constant `C_H(chi)` and finally converting the Step-26 eventual negative slope into a theorem with a finite certified onset bandwidth?

---

## 4. Scope boundary

Do not claim:
- faster detectors are universally better or worse;
- a universal speed-detectivity tradeoff or scalar replacement for `D*`;
- Step-13 `ell~49` is valid;
- arbitrary low-pass filtering is a true information-band limitation;
- Gaussian information weighting is a literal circuit transfer function;
- Rice is uniformly accurate at high finite-window bandwidth;
- Step-20 double reversal is an exact physical result;
- monotonic `H(chi,zeta)` alone proves monotonic detector preference;
- the positive `1/sqrt(zeta)` Pickands coefficient is already a theorem for Gaussian mollification;
- the invalidated `0.8131` coupling coefficient is valid;
- no bounded pre-asymptotic pocket exists yet;
- the Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.
