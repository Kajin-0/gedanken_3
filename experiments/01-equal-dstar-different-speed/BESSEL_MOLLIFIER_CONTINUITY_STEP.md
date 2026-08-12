# Step 28 — Two-Sided-Bessel Zoom-In for Gaussian Mollification

**Date:** 2026-08-11 20:29 EDT  
**Status:** DERIVED / CONDITIONAL THEOREM SKETCH / NUMERICAL VALIDATION / REJECTED SHORTCUT / OPEN. Step 27 proved the `O(zeta^-1/2)` path-amplitude scale but not a positive lower Pickands correction. This step adapts the Brownian-extremum zoom-in structure to the Gaussian mollifier. Under the standard unique-maximizer, stable local Bessel convergence, localization, and uniform-integrability conditions stated below, the leading correction to the generalized Dieker–Yakir constant is positive and of exact order `zeta^-1/2`. The coefficient is a positive Dieker–Yakir-weighted two-sided-BES(3) Gaussian-kernel functional. The denominator of the Dieker–Yakir ratio contributes only `O(zeta^-1)` under the common-noise high-pass coupling, so it cannot cancel the `O(zeta^-1/2)` extremum correction. This closes the missing **positive-coefficient mechanism**, but does not yet provide a rigorous explicit finite onset bandwidth `K` because a quantitative uniform remainder for the Bessel zoom-in is still absent. No novelty claim.

---

## 1. Question

Step 27 established

```math
W_{\chi,\zeta}\to W_{\chi,\infty}
```

under a strong Gaussian coupling, with pointwise random difference of scale

```math
O\!\left(\sqrt{\chi/\zeta}\right).
```

The unresolved issue was whether the generalized Pickands correction actually inherits a **strictly positive** amount of that square-root scale:

```math
\sqrt\zeta\,[H_{mix}(\chi)-H(\chi,\zeta)]
\to C_H(\chi)>0.
```

The natural place to look is the unique random maximizer of the rough spectral path, because Brownian extrema have a universal two-sided-Bessel zoom-in law.

Primary related Brownian results:

- Dieker & Lagos, *On the Euler discretization error of Brownian motion about random times*, arXiv:1708.04356: Brownian paths zoomed around extrema converge to a two-sided BES(3)-based field and the extreme-value height error is `O(sqrt(delta))`.
- Bisewski & Jasnovidov, *On the speed of convergence of discrete Pickands constants to continuous ones*, arXiv:2108.00756 / J. Appl. Probab. 62 (2025): the classical `alpha=1` Pickands grid correction is exactly square-root order.

Gaussian convolution is not grid discretization, so only the **zoom-in machinery**, not the grid coefficient, is reused.

---

## 2. Rough spectral field and local Brownian scale

At `zeta=infinity`, the Step-24/25 tangent spectral process is

```math
W_\infty(t)
=\sqrt2\,\eta_{\chi,\infty}(t)-g_{\chi,\infty}(t),
```

with

```math
g_{\chi,\infty}(t)=t^2+\sqrt2\chi|t|.
```

Its locally rough random part has Brownian increment variance

```math
\operatorname{Var}[W_\infty(t+h)-W_\infty(t)]
=2\sqrt2\chi|h|+O(h^2).
```

Define

```math
\boxed{
\sigma_\chi=2^{3/4}\sqrt\chi.
}
```

Let `tau_*` be the almost-sure unique maximizer of `W_infinity`, and

```math
M_\infty=W_\infty(\tau_*).
```

The Brownian-extremum zoom-in statement has the local form

```math
\boxed{
\frac{M_\infty-W_\infty(\tau_*+\varepsilon s)}
{\sigma_\chi\sqrt\varepsilon}
\Longrightarrow R_*(s),
}
```

where `R_*` is a two-sided BES(3)-type extremal field, with the positive and negative sides given by the standard Brownian extremum decomposition.

The smooth linear/quadratic pieces contribute only `O(epsilon)` on this time scale and therefore disappear from the leading `sqrt(epsilon)` zoom-in.

Set

```math
\varepsilon=1/\zeta.
```

---

## 3. Gaussian mollifier on the extremum scale

Step 27 showed that the finite-band Brownian component is obtained with the Gaussian kernel

```math
K_\zeta(t)
=\frac1\varepsilon K_1(t/\varepsilon),
```

where

```math
\boxed{
K_1(s)=\sqrt{\frac2\pi}\,e^{-2s^2},
\qquad
\int_{\mathbb R}K_1(s)ds=1.
}
```

On the local variable

```math
t=\tau_*+\varepsilon u,
```

Gaussian smoothing therefore acts directly on the Bessel zoom-in profile.

To leading order,

```math
W_\zeta(\tau_*+\varepsilon u)
=
M_\infty
-\sigma_\chi\sqrt\varepsilon
(K_1*R_*)(u)
+o_p(\sqrt\varepsilon),
```

up to additive path constants irrelevant to the Dieker–Yakir ratio and `O(epsilon)` deterministic drift corrections.

Hence the smoothed maximum obeys

```math
\boxed{
M_\infty-M_\zeta
=
\sigma_\chi\sqrt\varepsilon\,\mathcal M_K(R_*)
+o_p(\sqrt\varepsilon),
}
```

with kernel-specific Bessel functional

```math
\boxed{
\mathcal M_K(R)
=
\inf_{u\in\mathbb R}
\int_{\mathbb R}K_1(v)R(u-v)dv.
}
```

---

## 4. Strict positivity of the local mollifier loss

For a two-sided BES(3) extremal profile:

```text
R(0)=0,
R(s)>0 for every s != 0 almost surely,
R(s)->infinity in probability/pathwise growth as |s|->infinity.
```

The Gaussian kernel satisfies

```text
K_1(v)>0 for every finite v.
```

Therefore, for every fixed `u`,

```math
(K_1*R)(u)>0
```

almost surely. Continuity and growth at large `|u|` imply the convolution attains a finite positive minimum.

Thus

```math
\boxed{
\mathcal M_K(R_*)>0
\quad\text{almost surely}.
}
```

So Gaussian smoothing lowers the rough maximum by a strictly positive `sqrt(epsilon)` amount at leading order.

**DERIVED / CONDITIONAL:** once the Brownian-extremum zoom-in is transferred to this spectral field, the maximum correction has a positive kernel-specific coefficient. This is stronger than the Step-27 upper-scale coupling.

---

## 5. Why the Dieker–Yakir denominator is lower order

The generalized Pickands functional is

```math
\Psi(W)
=\frac{e^{\sup W}}
{\int_{\mathbb R}e^{W(t)}dt}.
```

A maximum-height result alone would be insufficient if the denominator changed by the same `sqrt(epsilon)` order.

Use the shift-invariant high-pass coupling from Step 27. The random residual between rough and smoothed fields can be represented as a **stationary** Gaussian high-pass field

```math
U_\varepsilon(t)
```

with

```text
point variance  = O(epsilon),
correlation length = O(epsilon).
```

Equivalently,

```math
U_\varepsilon(t)
\overset{d}=\sqrt\varepsilon\,U_1(t/\varepsilon).
```

For a localized weight `w(t)` with the exponential/quadratic moment control supplied by the `t^2` drift,

```math
\int w(t)U_\varepsilon(t)dt
```

has variance `O(epsilon^2)` when the unit-scale covariance is integrable. Its standard deviation is therefore `O(epsilon)`.

The quadratic term from

```math
e^{U_\varepsilon}-1-U_\varepsilon
```

is also `O_p(epsilon)` after integration because `E U_epsilon^2=O(epsilon)`.

Consequently, under the stated localization/moment conditions,

```math
\boxed{
\log S_\infty-\log S_\zeta
=O_p(\varepsilon),
\qquad
S=\int e^W.
}
```

This is lower order than the maximum correction

```math
M_\infty-M_\zeta=O_p(\sqrt\varepsilon).
```

### Numerical check

Paired common-noise simulations at `chi=0.1`, `zeta=80`, with Brownian grid refinement show exactly this separation:

```text
sqrt(zeta) * denominator-log correction:
    statistically compatible with 0

sqrt(zeta) * [H_infinity-H_zeta]:
    converges to the same value as the Psi_infinity-weighted maximum-loss contribution.
```

**REFINEMENT:** the leading Pickands correction is extremum-local. The Dieker–Yakir denominator does not cancel the square-root maximum loss.

---

## 6. Positive coefficient formula

Expand

```math
\Psi(W_\zeta)
=\Psi(W_\infty)
\left[
1-(M_\infty-M_\zeta)+o_p(\sqrt\varepsilon)
\right]
```

using the lower-order denominator result above.

Under uniform integrability sufficient to exchange the limit and expectation,

```math
\boxed{
H_{mix}(\chi)-H(\chi,\zeta)
=
\frac{C_H(\chi)}{\sqrt\zeta}
+o(\zeta^{-1/2}),
}
```

with

```math
\boxed{
C_H(\chi)
=
2^{3/4}\sqrt\chi\;
E\!\left[
\Psi(W_\infty)\,
\mathcal M_K(R_*)
\right].
}
```

Because

```math
\Psi(W_\infty)>0
```

and

```math
\mathcal M_K(R_*)>0
```

almost surely,

```math
\boxed{
C_H(\chi)>0
\qquad\text{for every }\chi>0.
}
```

This is the desired positive-coefficient mechanism.

### Important non-factorization

A tempting shortcut would be

```math
E[\Psi\,\mathcal M_K]
\stackrel{?}=E[\Psi]E[\mathcal M_K].
```

That independence is **not established** and should not be assumed.

A direct standard two-sided-BES(3) simulation gives approximately

```text
E[M_K] ~ 0.87
```

for the Gaussian kernel above, whereas the Step-27 Pickands data imply a smaller effective Dieker–Yakir-weighted factor of roughly `0.67–0.70` over the tested endpoint `chi` values.

**REJECTED SHORTCUT:** do not replace the weighted Bessel coefficient by the unweighted Bessel mean.

---

## 7. Relation to Step 26

Step 26 required a positive coefficient in

```math
H_{mix}(\chi)-H(\chi,\zeta)
=C_H(\chi)\zeta^{-1/2}+O(\zeta^{-1}).
```

Step 28 now supplies the structural positivity

```math
\boxed{C_H(\chi)>0}
```

under the Bessel zoom-in/localization/uniform-integrability assumptions.

Therefore the Step-26 ordering

```text
extreme-statistics correction = O(kappa^-1/2)
finite-window SNR correction  = O(kappa^-1)
```

has the correct nonzero leading sign rather than merely an empirically fitted one.

For the `r=2` calibration this strongly supports the asymptotic expansion

```math
\Lambda_\times(\kappa_f)
=\Lambda_\infty
+C_\Lambda\kappa_f^{-1/2}
+o(\kappa_f^{-1/2}),
\qquad C_\Lambda>0,
```

and therefore eventual

```math
\frac{d\Lambda_\times}{d\kappa_f}<0.
```

---

## 8. Why a finite certified onset bandwidth still does not follow

The existing Brownian-extremum zoom-in results are weak/stable limit theorems. The argument above identifies the leading positive coefficient, but an explicit detector bandwidth `K` requires a quantitative remainder such as

```math
\left|
H_{mix}(\chi)-H(\chi,\zeta)
-\frac{C_H(\chi)}{\sqrt\zeta}
\right|
\le\frac{R(\chi)}{\zeta}
```

uniformly over the relevant fast/slow `chi` interval.

We do not yet have such a theorem for Gaussian mollification.

Without that uniform remainder, one cannot certify a specific finite `K` for which

```math
d\Lambda_\times/d\kappa_f<0
```

holds for every larger bandwidth.

**NEGATIVE RESULT / SCOPE LIMIT:** adapting the two-sided-Bessel zoom-in closes the positive-coefficient gap but does **not** by itself close the quantitative finite-`K` gap.

---

## 9. What is established

### DERIVED / CONDITIONAL THEOREM SKETCH

- Gaussian mollification acts on the Brownian-extremum scale through the kernel `K_1`.
- The smoothed maximum loss is `sigma_chi sqrt(epsilon) M_K + o_p(sqrt(epsilon))`.
- `M_K>0` almost surely.
- The integrated Dieker–Yakir denominator perturbation is lower order, `O_p(epsilon)`, under the stationary high-pass/localization moment assumptions.
- Therefore

```math
H_{mix}(\chi)-H(\chi,\zeta)
=C_H(\chi)\zeta^{-1/2}+o(\zeta^{-1/2})
```

with

```math
C_H(\chi)>0.
```

### NUMERICAL VALIDATION

- standard unweighted two-sided-BES(3) Gaussian-kernel functional: `E[M_K] ~0.87`;
- paired full-field calculation confirms the denominator contribution is lower order on the square-root scale;
- Step-27 data imply a positive Dieker–Yakir-weighted effective local coefficient across the fast, slow, and `chi=0.1` diagnostics.

### OPEN

- full publication-grade proof of stable joint convergence with the Dieker–Yakir weight;
- explicit analytic or certified numerical value of `C_H(chi)`;
- uniform `O(1/zeta)` remainder over the detector-relevant `chi` interval;
- explicit finite onset bandwidth `K`;
- compact-interval closure of the hypothetical re-entrant pocket;
- hardware interpretation;
- novelty.

---

## 10. First nontrivial consequence

The missing square-root correction is not merely a generic Gaussian continuity effect. Its positive leading term is localized at the **random Brownian maximum** and is governed by a Gaussian-kernel functional of the two-sided BES(3) extremal profile:

```math
\boxed{
C_H(\chi)
=
2^{3/4}\sqrt\chi\;
E[\Psi_\infty\,\mathcal M_K(R_*)]
>0.
}
```

That converts Step 26 from a purely empirical sign mechanism into a mathematically identified positive continuity correction, while leaving only the quantitative remainder needed for a finite certified onset bandwidth.

---

## 11. Stopping point

The asymptotic positive coefficient is now identified. The remaining problem is quantitative rather than structural.

### Single natural next question

> Can the Bessel/mollifier expansion be strengthened to a **uniform quantitative remainder bound** over the detector-relevant `chi` interval, so that a concrete finite `kappa_f=K` can be certified beyond which the exact fast/slow boundary is monotone decreasing and the remaining high-band re-entrant pocket can be ruled out?
