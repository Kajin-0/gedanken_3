# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 19:48 EDT  
**Status:** twenty-six logical steps completed. Step 26 expands the actual finite-r fast/slow task boundary along the common physical-bandwidth trajectory. Finite-hard-window SNR recovery is `O(kappa^-1)`, while Dieker–Yakir data show `H_mix(chi)-H(chi,zeta) ~ C_H(chi)/sqrt(zeta)` along the relevant fast/slow tangent fields. Conditional on that numerically stable leading smoothing law, the `r=2` boundary has `Lambda_cross(kappa_f)=Lambda_infinity+C_Lambda/sqrt(kappa_f)+O(kappa_f^-1)` with `C_Lambda>0`, hence eventual negative slope and approach to the rough endpoint from above. A bounded pre-asymptotic re-entrant pocket is still not rigorously excluded because the square-root smoothing law and uniform remainder are not yet proved. No universal replacement metric and no novelty claim.

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

## 2. Surviving chain

### Steps 01–04 — scalar `D*`, full-observation equivalence, finite-window phase
- Equal reference scalar `D*` does not guarantee equal arbitrary temporal-signal SNR; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`.
- For known waveform/full observation, `rho_inf^2 = integral |P|^2 |G|^2/S_n df = A^-1 integral |P|^2 D*^2(f) df`.
- **NEGATIVE RESULT:** unknown timing alone does not break complete-magnitude `D*(f)` equivalence under stationary Gaussian full observation.
- Finite windows can break equivalence because magnitude `D*(f)` discards phase/temporal placement; a causal all-pass construction removes the pure-delay loophole.

### Steps 05–12 — finite-record SNR and task boundary

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

The ideal-white-noise hard-window scan is locally Brownian-like.

**FAILED NUMERICAL ESTIMATE:** Step-13 `ell~49` rough-grid crossover is invalid.

### Steps 14–17 — genuine timing bandwidth and exact rare-event structure
Use smooth information weighting `J_{x,kappa}(nu)=|H_x(nu)|^2 exp[-(nu/kappa)^2]`. Finite `kappa` removes the cusp.

Exact smooth Palm identity:

```math
P_{FA}=Q(u)+\lambda_u E_\uparrow[1_{z(0)\le u}/N_u^+].
```

Rice/EC is an upper bound. For finite hard windows `sigma_kappa^2~a_x kappa/sqrt(pi)`, so Rice accuracy is nonuniform toward the rough limit.

### Steps 18–19 — common physical bandwidth and finite optimum
Use `kappa_i=Omega_B tau_i`.

With accessible SNR artificially fixed, the crossover moves from electronics-limited `~1/Omega_B` to detector-limited `~tau_f` but has **no** finite bandwidth optimum.

Holding physical signal/noise fixed restores bandwidth-dependent SNR. For the **full template**, SNR loss is `O(kappa^-2)` while timing-search simplification is `O(kappa^-1)`, giving a finite large-r bandwidth optimum. Later Palm work confirms that a shallow finite optimum survives beyond Rice.

### Steps 20–21 — finite-r Rice double reversal corrected by Palm
For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=0.90`, `Lambda=0.895`, converged Rice gave apparent switches `25.4898402` and `130.1945883`.

Palm correction gives

```math
\boxed{\kappa_{\times,1}^{Palm}\approx21.7\pm0.3}
```

for the surviving lower switch and **INVALIDATES** the upper Rice switch. Palm checks at `kappa_f=130,160,300` keep fast preferred for `Lambda=0.895`.

### Step 22 — Palm boundary map and true finite optimum
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
R_x(y)=1-a_x|y|-\frac{b_x}{2}y^2+O(|y|^3),
```

with

```math
a_x=\frac{2x^2e^{-2x}}{\eta(x)},
\qquad
b_x=\frac{1+e^{-2x}(2x^2-2x-1)}{\eta(x)}.
```

Infinite-band rough/smooth coordinate:

```math
\chi_x=a_xu/\sqrt{b_x}.
```

On the high-excursion scale, tangent variance is `t^2+sqrt(2) chi |t|`.

At `u~5`, leading asymptotics are not accurate enough. Exact occupation-time identity:

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

The exact tangent variogram is

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

### Step 25 — Dieker–Yakir evaluation and exact monotonicity
For `W=sqrt(2) eta-g`, the generalized continuous Dieker–Yakir representation is

```math
\mathcal H(\chi,\zeta)
=E\left[\frac{\sup_t e^{W(t)}}{\int e^{W(t)}dt}\right].
```

Efficient decomposition:

```math
\eta_{\chi,\zeta}(t)=Zt+2^{1/4}\sqrt\chi B_\zeta(t),
```

with stationary derivative covariance `zeta/sqrt(pi) exp(-zeta^2 t^2)`.

Brown–Resnick Slepian comparison gives

```math
\partial_\zeta H\ge0,
\qquad
\partial_\chi H\ge0,
```

and `1/sqrt(pi) <= H(chi,zeta) <= H_mix(chi)`.

**REFINEMENT:** the local extreme constant cannot oscillate with bandwidth, but this alone does not make the physical detector boundary monotone.

### Step 26 — coupled high-band physical boundary derivative
Let `A_f(X,kappa)` and `A_s(X,kappa)` be the admissible **physical** timing uncertainty inferred from fast and slow channels. The common-time boundary obeys `A_f=A_s`. Exact implicit differentiation gives

```math
\boxed{
\frac{d\Lambda_\times}{d\kappa}
=\frac{A_{f,X}A_{s,\kappa}-A_{s,X}A_{f,\kappa}}
{A_{f,X}-A_{s,X}}.
}
```

For a finite hard window,

```math
\boxed{
\rho(x,\kappa)=\rho_\infty(x)
\left[1-\frac{a_x}{\sqrt\pi\kappa}+o(\kappa^{-1})\right],
}
```

so finite-window SNR recovery is `O(kappa^-1)`.

Dieker–Yakir data show a much slower local-extreme convergence:

```math
\boxed{
H_{mix}(\chi)-H(\chi,\zeta)
\approx\frac{C_H(\chi)}{\sqrt\zeta},
\qquad C_H>0,
}
```

with an exceptionally clean sequence at `chi=0.1` and compatible behavior at the actual endpoint values `chi_fast~1.1e-4`, `chi_slow~6.4e-2`.

**NUMERICAL ASYMPTOTIC / NOT YET A THEOREM:** the square-root smoothing rate is strongly supported but not yet proved uniformly for this field.

Conditional on that leading law,

```math
A_i(X,\kappa_f)
=A_i^\infty(X)+d_i(X)\kappa_f^{-1/2}+O(\kappa_f^{-1}),
```

and

```math
\boxed{
\Lambda_\times(\kappa_f)
=\Lambda_\infty+C_\Lambda\kappa_f^{-1/2}+O(\kappa_f^{-1}).
}
```

For the `r=2` calibration the finite-u tangent surrogate gives approximately

```text
A_f,X ~4.9e-3
A_s,X ~4.5e-1
C_H,fast ~0.006
C_H,slow ~0.20
C_Lambda ~ +2e-2
```

so

```math
\boxed{
\frac{d\Lambda_\times}{d\kappa_f}<0
}
```

for sufficiently large bandwidth: the boundary approaches the rough endpoint from above.

**REFINEMENT / CONDITIONAL:** an additional slow-preferred pocket cannot persist or reappear arbitrarily far into the high-band tail. If one exists, it must be a bounded pre-asymptotic feature. No such pocket has appeared in Palm checks through `kappa_f=300`, the mapped boundary, or the direct rough endpoint.

**OPEN:** proving the `zeta^-1/2` smoothing law with positive coefficient and a uniform remainder is still required to certify an exact finite bandwidth beyond which the detector boundary is guaranteed monotone decreasing.

See `HIGH_BAND_BOUNDARY_DERIVATIVE_STEP.md` and `numerics/high_band_boundary_derivative.py`.

---

## 3. Current frontier

The physical high-band derivative has a definite **conditional asymptotic sign**. The remaining task is no longer to discover the correct local object, but to prove its smoothing rate strongly enough to turn eventual monotonicity into a certified exact-process statement.

### Single next question — DO NOT ANSWER YET

> Can `H_mix(chi)-H(chi,zeta) ~ C_H(chi)/sqrt(zeta)` be derived or bounded rigorously for the Gaussian-smoothed Brownian endpoint field, with a uniform remainder strong enough to certify a finite `kappa` beyond which the exact detector boundary must be monotone decreasing?

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
- the `zeta^-1/2` smoothing law is already a proved theorem for this field;
- no bounded pre-asymptotic pocket exists yet;
- the Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.
