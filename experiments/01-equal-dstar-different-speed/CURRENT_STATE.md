# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 19:38 EDT  
**Status:** twenty-five logical steps completed. Step 25 proves that the two-parameter generalized Pickands constant `H(chi,zeta)` admits a continuous Dieker–Yakir expectation representation and is coordinatewise nondecreasing in both `chi` and `zeta` by Brown–Resnick Slepian comparison. A practical FFT estimator reproduces the exact smooth endpoint and the monotonic trend. This removes oscillation of the local extreme constant as a mechanism for a bounded high-band re-entrant detector-preference pocket, but does not yet prove the full fast/slow boundary monotone because the physical bandwidth sweep changes SNR, threshold, integration time, `chi`, and `zeta` simultaneously. No universal replacement metric and no novelty claim.

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
- Equal scalar reference `D*` does not guarantee equal arbitrary temporal-signal SNR; explicit 1 Hz example gave `SNR_A/SNR_B~6.36`.
- For known waveform/full observation,

```math
\rho_\infty^2=\int |P|^2|G|^2/S_n\,df
=\frac1A\int|P|^2D^{*2}(f)\,df.
```

- **NEGATIVE RESULT:** unknown timing alone does not break complete-magnitude `D*(f)` equivalence under stationary Gaussian full observation.
- Finite windows can break equivalence because magnitude `D*(f)` discards phase/temporal placement; a causal all-pass construction removes the pure-delay loophole.

### Steps 05–12 — finite-record SNR and task boundary

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
```

```math
P_D(t;\alpha)=\Phi[\rho_t-\Phi^{-1}(1-\alpha)],
```

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

For the controlled family `s_tau(t)=A_tau t exp(-t/tau)u(t)`, faster SNR accumulation can be offset by larger unknown-time search burden.

**REJECTED SHORTCUT:** finite-window SNR cannot be combined directly with full-template timing bandwidth as one exact statistic.

**NEGATIVE RESULT:** no finite interior integration-duration optimum exists in the original scaled family.

### Step 13 — rough hard-window obstruction

```math
R_x(y)=1-a_x|y|+O(y^2),
\qquad a_x=2x^2e^{-2x}/\eta(x).
```

The ideal-white-noise hard-window timing scan is locally Brownian-like.

**FAILED NUMERICAL ESTIMATE:** Step-13 `ell~49` rough-grid crossover is invalid.

### Steps 14–17 — genuine timing bandwidth and exact rare-event structure
Use the smooth information weighting

```math
J_{x,\kappa}(\nu)=|H_x(\nu)|^2e^{-(\nu/\kappa)^2}.
```

Finite `kappa` removes the cusp.

Exact smooth Palm identity:

```math
P_{FA}=Q(u)+\lambda_u E_\uparrow[1_{z(0)\le u}/N_u^+].
```

Rice/EC is an upper bound; Palm importance sampling makes `alpha=1e-6` practical.

For finite hard windows,

```math
\sigma_\kappa^2(x)\sim a_x\kappa/\sqrt\pi,
```

so Rice accuracy is not uniform as bandwidth tends to infinity.

### Steps 18–19 — common physical bandwidth and finite optimum
Use `kappa_i=Omega_B tau_i`.

With accessible SNR artificially held fixed: electronics-limited `~1/Omega_B` to detector-limited `~tau_f`, but **no** finite bandwidth optimum.

Hold underlying physical signal/noise fixed instead. Wide-band SNR loss is `O(1/kappa^2)` while timing-search simplification is `O(1/kappa)`.

**DERIVED / CONDITIONAL:** a finite large-r bandwidth optimum exists. Later Palm work confirms survival beyond Rice.

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

Large-r full-template Palm scan:

```text
kappa~50–65: ell_crit^Palm ~0.912
infinity:    ell_crit^Palm ~0.90897
```

**NUMERICAL VALIDATION / CONDITIONAL:** finite bandwidth optimum survives Palm correction with only `~0.3–0.4%` gain.

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
\boxed{\chi_x=a_xu/\sqrt{b_x}}.
```

On `q(u)=sqrt(2)/(u sqrt(b_x))`, tangent variance is

```math
\operatorname{Var}\eta_\chi(t)=t^2+\sqrt2\chi|t|.
```

At `u~5`, leading asymptotics are not percent-level accurate enough. Exact occupation-time identity:

```math
\boxed{P(\sup z>u)=\ell Q(u)E_{occ}[1/V_u].}
```

Direct `kappa=infinity` calculation for the `r=2` calibration gives

```math
\Lambda_{cross}^{\infty}\approx0.905\pm0.004,
\qquad X_{cross}\approx7.75.
```

Thus `Lambda=0.895` is fast-preferred at the direct rough endpoint too.

### Step 24 — finite-band tangent bridge is two-parameter
The exact Gaussian smoothing integral for the hard-endpoint `1/nu^2` tail is

```math
J(y,\kappa)=
\frac{\pi|y|}{2}\operatorname{erf}(\kappa|y|/2)
+\frac{\sqrt\pi}{\kappa}[e^{-(\kappa y)^2/4}-1].
```

Matched local covariance:

```math
1-R_{x,\kappa}(y)
\sim\frac{b_x}{2}y^2+\frac{2a_x}{\pi}J(y,\kappa).
```

Finite bandwidth introduces

```math
\boxed{
\zeta_x=\frac{\kappa}{\sqrt2u\sqrt{b_x}}.
}
```

Together with `chi`, the tangent variogram is

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

`zeta->infinity` recovers Step 23; `zeta->0` gives the smooth finite-band quadratic tangent.

**REJECTED SHORTCUT:** `H_mix(chi)` alone cannot control finite-band convergence. The proper local object is `H(chi,zeta)` plus finite-threshold control.

### Step 25 — Dieker–Yakir evaluation and exact monotonicity
Define

```math
W_{\chi,\zeta}(t)
=\sqrt2\eta_{\chi,\zeta}(t)-g_{\chi,\zeta}(t).
```

Because `g_{chi,zeta}(t)=t^2+O(|t|)`, the continuous generalized Dieker–Yakir representation applies:

```math
\boxed{
\mathcal H(\chi,\zeta)
=E\left[\frac{\sup_t e^{W(t)}}{\int_{\mathbb R}e^{W(t)}dt}\right].
}
```

Efficient decomposition:

```math
\boxed{
\eta_{\chi,\zeta}(t)
=Zt+2^{1/4}\sqrt\chi\,B_\zeta(t),
}
```

where `Z~N(0,1)` and `B_zeta'(t)` is stationary Gaussian with

```math
\boxed{
E[B_\zeta'(0)B_\zeta'(t)]
=\frac{\zeta}{\sqrt\pi}e^{-\zeta^2t^2}.
}
```

Thus the finite-`zeta` field is generated efficiently by FFT synthesis of the derivative and one integration.

Exact derivatives:

```math
\frac{\partial g}{\partial\zeta}
=\frac{\sqrt2\chi}{\sqrt\pi\zeta^2}
(1-e^{-\zeta^2t^2})\ge0,
```

```math
\frac{\partial g}{\partial\chi}
=\sqrt2F_\zeta(t)\ge0.
```

Brown–Resnick Slepian comparison therefore gives

```math
\boxed{
\partial_\zeta\mathcal H\ge0,
\qquad
\partial_\chi\mathcal H\ge0.
}
```

and the deterministic bracket

```math
\boxed{
1/\sqrt\pi
\le\mathcal H(\chi,\zeta)
\le\mathcal H_{mix}(\chi).
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

Grid refinement at `zeta=9,19` is smaller than Monte Carlo uncertainty, and `chi=0` reproduces the exact `1/sqrt(pi)` checkpoint.

**REFINEMENT / REJECTED SHORTCUT:** the local extreme constant itself cannot oscillate with bandwidth, but its monotonicity does **not** imply monotonicity of the full detector boundary because changing physical bandwidth also changes `rho(x,kappa)`, `u`, `x`, `chi`, and `zeta` differently for fast and slow channels.

See `TWO_PARAMETER_PICKANDS_DY_STEP.md` and `numerics/two_parameter_pickands_dy.py`.

---

## 3. Current frontier

The remaining re-entrant-pocket question has been narrowed. Any re-entrance cannot arise from nonmonotonic `H(chi,zeta)` itself; it must arise from the coupled detector trajectories through SNR recovery, threshold, integration time, and the two tangent coordinates.

### Single next question — DO NOT ANSWER YET

> Can the deterministic Dieker–Yakir estimates of `H(chi,zeta)` be inserted into the finite-`u` boundary equation and asymptotically expanded along the actual fast and slow detector trajectories to determine the sign of `d Lambda_cross / d kappa_f` at high bandwidth, rather than relying on monotonicity of `H` alone?
