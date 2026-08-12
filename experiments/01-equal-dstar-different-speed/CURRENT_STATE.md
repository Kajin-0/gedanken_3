# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 20:29 EDT  
**Status:** twenty-eight logical steps completed. Step 28 adapts the Brownian-extremum/two-sided-BES(3) zoom-in mechanism to Gaussian mollification of the finite-band tangent field. Under the stated stable-convergence, localization, and uniform-integrability conditions, the generalized Pickands correction has a strictly positive leading `zeta^-1/2` coefficient. The Dieker–Yakir denominator is lower order (`O(zeta^-1)`) under the stationary high-pass coupling, so it cannot cancel the extremum-local square-root loss. A concrete finite onset bandwidth `K` is still not certified because a quantitative uniform remainder for the mollifier/Bessel expansion is not yet available. No universal replacement metric and no novelty claim.

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

### Steps 01–04 — limits of scalar and magnitude-only `D*`
- Equal scalar reference `D*` does not guarantee equal arbitrary temporal-signal SNR; an explicit 1 Hz example gave `SNR_A/SNR_B~6.36`.
- For a known waveform with unrestricted full observation,

```math
\rho_\infty^2
=\int |P|^2|G|^2/S_n\,df
=\frac1A\int |P|^2D^{*2}(f)\,df.
```

- **NEGATIVE RESULT:** unknown timing alone does not break complete-magnitude `D*(f)` equivalence under stationary Gaussian full observation.
- Finite observation can break equivalence because magnitude `D*(f)` discards temporal phase/placement.

### Steps 05–12 — finite records and task-level timing search

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
```

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

For the controlled `t exp(-t/tau)` family, faster SNR accumulation can be offset by a larger unknown-time search burden.

**REJECTED SHORTCUT:** finite-window SNR cannot be combined directly with full-template timing bandwidth as one exact finite-deadline statistic.

**NEGATIVE RESULT:** no finite interior integration-duration optimum exists in the original scaled family.

### Step 13 — rough hard-window obstruction

```math
R_x(y)=1-a_x|y|+O(y^2),
\qquad a_x=2x^2e^{-2x}/\eta(x).
```

The ideal-white-noise finite hard-window scan is locally Brownian-like.

**FAILED NUMERICAL ESTIMATE:** the rough-grid crossover near `ell~49` moved under grid refinement and is invalid.

### Steps 14–17 — genuine timing bandwidth and exact rare events
Use smooth information weighting

```math
|H_x(\nu)|^2e^{-(\nu/\kappa)^2}.
```

Finite `kappa` removes the cusp. Exact smooth Palm identity:

```math
P_{FA}=Q(u)+\lambda_u E_\uparrow[1_{\{z(0)\le u\}}/N_u^+].
```

Rice/EC is an upper bound. For finite hard windows,

```math
\sigma_\kappa^2\sim a_x\kappa/\sqrt\pi,
```

so Rice accuracy is nonuniform as `kappa->infinity`.

### Steps 18–19 — shared physical bandwidth and a true finite optimum
Use `kappa_i=Omega_B tau_i`.

With accessible eventual SNR artificially fixed, the crossover moves from electronics-limited `~1/Omega_B` to detector-limited `~tau_f`, but there is **no** interior bandwidth optimum.

Holding the physical signal/noise fixed restores bandwidth-dependent accessible SNR. For the full template, SNR loss is `O(kappa^-2)` while search simplification is `O(kappa^-1)`, giving a finite large-r bandwidth optimum. Later Palm calculations confirm a shallow finite optimum survives beyond Rice.

### Steps 20–21 — finite-r Rice double reversal corrected by Palm
For

```text
r=2
rho_full=6.2407571
alpha=1e-6
beta=0.90
Lambda=0.895
```

converged finite-duration Rice gave apparent switches at `25.4898402` and `130.1945883`.

Palm correction gives

```math
\boxed{\kappa_{\times,1}^{Palm}\approx21.7\pm0.3}
```

for the surviving lower switch and **INVALIDATES** the upper Rice switch. Direct Palm checks at `kappa_f=130,160,300` keep the fast detector preferred for `Lambda=0.895`.

### Step 22 — Palm boundary map and Palm bandwidth optimum
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

Large-r full-template Palm scan gives a broad finite optimum near `kappa~50–65`, only about `0.3–0.4%` above the infinite-band boundary.

### Step 23 — matched infinite-band rough/smooth limit
Exact local expansion:

```math
R_x(y)=1-a_x|y|-\frac{b_x}{2}y^2+O(|y|^3),
```

with high-excursion matching coordinate

```math
\chi_x=a_xu/\sqrt{b_x}.
```

At `kappa=infinity`, tangent variance is

```math
\operatorname{Var}\eta_\chi(t)=t^2+\sqrt2\chi|t|.
```

At the present `u~5`, leading high-threshold asymptotics are not accurate enough. Exact occupation-time identity:

```math
P(\sup z>u)=\ell Q(u)E_{occ}[1/V_u].
```

Direct rough-limit calculation for the `r=2` calibration gives

```math
\Lambda_{cross}^{\infty}\approx0.905\pm0.004,
\qquad X\approx7.75.
```

Thus `Lambda=0.895` is fast-preferred at the direct rough endpoint too.

### Step 24 — finite-band tangent bridge is two-parameter
Finite bandwidth introduces

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

### Step 25 — generalized Dieker–Yakir evaluation and exact monotonicity

```math
\mathcal H(\chi,\zeta)
=E\left[\frac{\sup_t e^{W(t)}}{\int_{\mathbb R}e^{W(t)}dt}\right].
```

Efficient simulation uses FFT synthesis of a stationary Gaussian derivative and one integration.

Brown–Resnick Slepian comparison gives exact coordinatewise monotonicity:

```math
\partial_\zeta H\ge0,
\qquad
\partial_\chi H\ge0.
```

**REFINEMENT:** the local extreme constant cannot oscillate with bandwidth, but this alone does not make the physical fast/slow boundary monotone.

### Step 26 — coupled physical high-band derivative
For physical admissible timing intervals `A_f,A_s`, exact implicit differentiation gives

```math
\frac{d\Lambda_\times}{d\kappa}
=\frac{A_{f,X}A_{s,\kappa}-A_{s,X}A_{f,\kappa}}
{A_{f,X}-A_{s,X}}.
```

For a finite hard window,

```math
\rho(x,\kappa)
=\rho_\infty(x)[1-a_x/(\sqrt\pi\kappa)+o(\kappa^{-1})],
```

so finite-window SNR recovery is `O(kappa^-1)`.

Dieker–Yakir data show

```math
H_{mix}(\chi)-H(\chi,\zeta)
\approx C_H(\chi)\zeta^{-1/2}.
```

Conditional on a positive coefficient, the `r=2` boundary has

```math
\Lambda_\times(\kappa_f)
=\Lambda_\infty+C_\Lambda\kappa_f^{-1/2}+O(\kappa_f^{-1}),
```

with `C_Lambda>0`, hence eventual negative boundary slope.

### Step 27 — exact Gaussian-mollifier coupling scale
Use one white-noise field for the Brownian endpoint and its Gaussian-smoothed version. The amplitude transfer is

```math
e^{-\omega^2/(8\zeta^2)}
```

and the time-domain kernel is

```math
K_\zeta(t)=\sqrt2\zeta/\sqrt\pi\;e^{-2\zeta^2t^2}.
```

Exact deterministic gap:

```math
0\le|t|-F_\zeta(t)\le1/(\sqrt\pi\zeta).
```

For the coupled random difference,

```math
\operatorname{Var}[B_\infty-B_\zeta]
=\zeta^{-1}v(\zeta|t|),
```

with

```text
s_*   = 0.7016406021...
v_max = 0.2804576359...
```

and therefore

```math
\sup_t SD[W_\infty-W_\zeta]_{random}
\le0.8906480701\sqrt{\chi/\zeta}.
```

**INVALIDATED INTERMEDIATE:** an earlier same-turn `0.8131` coefficient used the large-lag variance rather than the true supremum.

A conservative fixed-window bound gives

```math
0\le H_{mix}(\chi)-H(\chi,\zeta)
\le C_\chi\sqrt{\log\zeta/\zeta}.
```

Paired common-random-number simulations sharply confirm positive square-root scaling along the actual fast/slow endpoint `chi` values.

**NEGATIVE RESULT:** this coupling proves the scale but not a positive lower asymptotic coefficient.

### Step 28 — two-sided-Bessel Gaussian-mollifier continuity correction
Let

```math
\sigma_\chi=2^{3/4}\sqrt\chi.
```

Around the almost-sure unique rough-field maximizer `tau_*`, the Brownian-extremum zoom-in has the form

```math
\frac{M_\infty-W_\infty(\tau_*+\varepsilon s)}
{\sigma_\chi\sqrt\varepsilon}
\Longrightarrow R_*(s),
\qquad \varepsilon=1/\zeta,
```

with `R_*` a two-sided BES(3)-type extremal field.

Gaussian smoothing acts on that local field through

```math
K_1(s)=\sqrt{2/\pi}\,e^{-2s^2}.
```

Define

```math
\boxed{
\mathcal M_K(R)
=\inf_u\int K_1(v)R(u-v)dv.
}
```

Then, under the stated stable-convergence/localization assumptions,

```math
M_\infty-M_\zeta
=\sigma_\chi\zeta^{-1/2}\mathcal M_K(R_*)
+o_p(\zeta^{-1/2}).
```

Because the Gaussian kernel is strictly positive and the two-sided BES(3) profile is positive away from its unique zero,

```math
\boxed{\mathcal M_K(R_*)>0\quad a.s.}
```

The stationary high-pass coupling shows the integrated Dieker–Yakir denominator perturbation averages down to `O_p(zeta^-1)`, lower order than the maximum loss. Therefore, with sufficient uniform integrability,

```math
\boxed{
H_{mix}(\chi)-H(\chi,\zeta)
=\frac{C_H(\chi)}{\sqrt\zeta}
+o(\zeta^{-1/2}),
}
```

where

```math
\boxed{
C_H(\chi)
=2^{3/4}\sqrt\chi\;
E[\Psi(W_\infty)\mathcal M_K(R_*)]
>0.
}
```

**REJECTED SHORTCUT:** do not factor this weighted expectation into `E[Psi]E[M_K]` without an independence theorem. A direct unweighted standard two-sided-BES(3) simulation gives `E[M_K]~0.87`, while the paired Pickands calculations imply a smaller effective Dieker–Yakir-weighted factor (`~0.67–0.70` in the tested cases).

**REFINEMENT:** the positive square-root coefficient is now structurally identified rather than merely fitted numerically.

**OPEN:** existing Brownian zoom-in results do not provide the quantitative uniform remainder required to certify a concrete finite `kappa_f=K` beyond which the exact physical boundary derivative is guaranteed negative.

See `BESSEL_MOLLIFIER_CONTINUITY_STEP.md` and `numerics/bessel_mollifier_continuity.py`.

---

## 3. Current frontier

The structural sign problem is largely closed: Gaussian smoothing produces a positive extremum-local `zeta^-1/2` continuity correction, while finite-hard-window SNR recovery is only `O(kappa^-1)`.

The remaining problem is quantitative:

> strengthen the Bessel/mollifier expansion to a **uniform remainder bound** over the detector-relevant `chi` interval, then derive an explicit finite bandwidth `K` beyond which `d Lambda_cross/d kappa_f < 0` is certified and close the remaining compact bandwidth interval.

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
- a publication-grade proof of the Step-28 weighted Bessel coefficient is complete;
- a finite certified onset bandwidth `K` is known;
- the unweighted Bessel mean `E[M_K]` equals the Pickands coefficient;
- the invalidated `0.8131` coupling coefficient is valid;
- no bounded pre-asymptotic pocket exists yet;
- the Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.
