# Step 27 — Gaussian-Mollifier Coupling Bound and the Remaining Continuity-Correction Gap

**Date:** 2026-08-11 20:09 EDT  
**Status:** DERIVED / NUMERICAL VALIDATION / REFINEMENT / INVALIDATED INTERMEDIATE / NEGATIVE RESULT / OPEN. Step 26 inferred an eventual negative high-band boundary slope conditional on the numerical law `H_mix(chi)-H(chi,zeta) ~ C_H(chi)/sqrt(zeta)`. This step constructs the finite-`zeta` rough component and the `zeta=infinity` Brownian component on the same white-noise field. The coupling gives an exact `O(zeta^-1/2)` pointwise path-amplitude scale, an explicit uniform variogram/drift gap, and a conservative compact-window `O(sqrt(log zeta / zeta))` envelope for the Dieker–Yakir functional. A paired common-random-number estimator then resolves the square-root correction with much smaller variance than the unpaired Step-26 calculation. However, the coupling provides only an upper scale bound; it does not by itself prove a strictly positive `C_H(chi)` or a uniform `1/sqrt(zeta)` lower bound. Therefore no rigorous finite onset bandwidth `K` is certified yet. No novelty claim.

---

## 1. Question

Step 26 found numerically that

```math
\mathcal H_{mix}(\chi)-\mathcal H(\chi,\zeta)
\approx \frac{C_H(\chi)}{\sqrt\zeta},
\qquad C_H(\chi)>0,
```

and used that rate to obtain

```math
\Lambda_\times(\kappa_f)
=\Lambda_\infty+C_\Lambda\kappa_f^{-1/2}+O(\kappa_f^{-1}),
\qquad C_\Lambda>0.
```

The remaining issue is whether the square-root correction can be obtained from the Gaussian smoothing construction itself rather than inferred from Monte Carlo.

The present step asks two narrower questions:

1. what is the exact size of the path perturbation produced by Gaussian smoothing of the Brownian endpoint field?;
2. is that alone sufficient to prove a positive `1/sqrt(zeta)` correction to the generalized Pickands constant?

The first answer is **yes**. The second is **no**.

---

## 2. Common-white-noise construction

Step 25 wrote the finite-band tangent process as

```math
\eta_{\chi,\zeta}(t)
=Zt+2^{1/4}\sqrt\chi\,B_\zeta(t),
```

where `Z ~ N(0,1)` and `B_zeta` has stationary increments with

```math
\operatorname{Var}B_\zeta(t)=F_\zeta(t),
```

```math
F_\zeta(t)
=|t|\operatorname{erf}(\zeta|t|)
+\frac{e^{-\zeta^2t^2}-1}{\sqrt\pi\,\zeta}.
```

The derivative of `B_zeta` has spectral density

```math
S_{Y_\zeta}(\omega)=e^{-\omega^2/(4\zeta^2)}.
```

Hence, if `xi` is unit white noise, we may construct

```math
Y_\zeta
=G_\zeta * \xi,
```

with Fourier multiplier

```math
\widehat G_\zeta(\omega)
=e^{-\omega^2/(8\zeta^2)}.
```

The infinite-band endpoint is ordinary Brownian motion,

```math
B_\infty(t)=\int_0^t\xi(s)ds.
```

Using the **same** white noise for both gives a canonical strong coupling

```math
\boxed{
B_\zeta
=\text{Gaussian-low-pass}_{\zeta}(B_\infty)
}
```

up to an additive random constant, which is irrelevant to the Dieker–Yakir ratio because adding the same constant to the whole spectral path multiplies numerator and denominator equally.

The time-domain smoothing kernel is

```math
\boxed{
K_\zeta(t)
=\frac{\sqrt2\,\zeta}{\sqrt\pi}
 e^{-2\zeta^2t^2},
}
```

which has unit integral and width `O(1/zeta)`.

---

## 3. Exact deterministic variogram gap

Write

```math
f(s)=s\operatorname{erf}(s)
+\frac{e^{-s^2}-1}{\sqrt\pi}.
```

Then

```math
F_\zeta(t)=\frac1\zeta f(\zeta|t|).
```

The difference between Brownian variance and the smoothed variance is

```math
|t|-F_\zeta(t)
=\frac1\zeta d(\zeta|t|),
```

with

```math
\boxed{
d(s)
=s\operatorname{erfc}(s)
+\frac{1-e^{-s^2}}{\sqrt\pi}
=\int_0^s\operatorname{erfc}(v)dv.
}
```

Therefore `d(s)` is increasing and

```math
0\le d(s)\le\frac1{\sqrt\pi}.
```

So

```math
\boxed{
0\le |t|-F_\zeta(t)
\le\frac1{\sqrt\pi\,\zeta}
\qquad\forall t.
}
```

For the Brown–Resnick spectral process

```math
W_{\chi,\zeta}(t)
=\sqrt2\eta_{\chi,\zeta}(t)-g_{\chi,\zeta}(t),
```

the deterministic drift difference therefore satisfies

```math
\boxed{
0\le
\sqrt2\chi\left[|t|-F_\zeta(t)\right]
\le
\frac{\sqrt2\chi}{\sqrt\pi\,\zeta}.
}
```

Thus the deterministic part of the finite-band correction is only `O(zeta^-1)`.

---

## 4. Exact variance profile of the coupled random difference

Let

```math
D_\zeta(t)=B_\infty(t)-B_\zeta(t).
```

Because the cross-spectrum between white noise and the filtered derivative has multiplier

```math
e^{-\omega^2/(8\zeta^2)},
```

the cross derivative covariance is the same Gaussian family with scale `sqrt(2) zeta`. Hence

```math
\operatorname{Cov}[B_\infty(t),B_\zeta(t)]
=F_{\sqrt2\zeta}(t).
```

Therefore

```math
\boxed{
\operatorname{Var}D_\zeta(t)
=|t|+F_\zeta(t)-2F_{\sqrt2\zeta}(t).
}
```

Writing

```math
s=\zeta|t|
```

gives the exact scaling

```math
\boxed{
\operatorname{Var}D_\zeta(t)
=\frac1\zeta v(s),
}
```

where

```math
\boxed{
v(s)=s+f(s)-\sqrt2\,f(\sqrt2s).
}
```

Its derivative is

```math
v'(s)
=1+\operatorname{erf}(s)
-2\operatorname{erf}(\sqrt2s).
```

The unique interior maximum solves `v'(s)=0`, numerically

```text
s_* = 0.7016406021...
```

and

```text
v(s_*) = 0.2804576359...
```

so

```math
\boxed{
\sup_t\operatorname{Var}[B_\infty(t)-B_\zeta(t)]
=\frac{0.2804576359\ldots}{\zeta}.
}
```

This is the exact pointwise coupling variance bound.

### Corrected intermediate estimate

During the derivation an intermediate value

```text
(sqrt(2)-1)/sqrt(pi) ~= 0.233695
```

was initially mistaken for the supremum. It is only the **large-lag limit** of `v(s)`, not the maximum.

**INVALIDATED INTERMEDIATE:** the corresponding spectral-field RMS coefficient `0.8131 sqrt(chi/zeta)` must not be reused.

The correct maximum gives

```math
2^{3/2}\,v(s_*)
=0.7932539848\ldots
```

for the variance of the random part of `W_infinity-W_zeta`, hence

```math
\boxed{
\sup_t
\operatorname{SD}
\left[
2^{3/4}\sqrt\chi\,D_\zeta(t)
\right]
\le
0.8906480701\ldots
\frac{\sqrt\chi}{\sqrt\zeta}.
}
```

This is a theorem-level origin for the square-root **path-amplitude** scale.

---

## 5. Compact-window uniform coupling envelope

The difference field also admits a stationary high-pass representation. In frequency space its transfer function relative to white noise is

```math
\frac{1-e^{-\omega^2/(8\zeta^2)}}{i\omega}.
```

After rescaling `omega=zeta q`, the field has correlation length `O(1/zeta)` and pointwise variance `O(1/zeta)`.

On any fixed interval `[-T,T]`, standard Gaussian maximal inequalities therefore give the conservative order

```math
\boxed{
E\sup_{|t|\le T}
|W_{\chi,\infty}(t)-W_{\chi,\zeta}(t)|
\le
C_{\chi,T}
\sqrt{\frac{\log(1+\zeta T)}{\zeta}}
+O(\zeta^{-1}).
}
```

The logarithm is the cost of controlling the **largest** of roughly `O(zeta T)` high-frequency residual cells. It is not observed in the Pickands correction itself because the extreme-value functional localizes around the random maximizer rather than following the largest residual anywhere in the entire truncation window.

For the truncated Dieker–Yakir functional

```math
\Psi_T(W)
=\frac{\sup_{|t|\le T}e^{W(t)}}
{\int_{-T}^{T}e^{W(t)}dt},
```

if

```math
\|W-\widetilde W\|_\infty\le\epsilon,
```

then deterministically

```math
\boxed{
e^{-2\epsilon}\Psi_T(W)
\le\Psi_T(\widetilde W)
\le e^{2\epsilon}\Psi_T(W).
}
```

Together with the quadratic `t^2` drift, which exponentially localizes the full Dieker–Yakir integral, this yields the conservative convergence envelope

```math
\boxed{
0\le
\mathcal H_{mix}(\chi)-\mathcal H(\chi,\zeta)
\le
C_\chi
\sqrt{\frac{\log\zeta}{\zeta}}
}
```

for sufficiently large `zeta`, with a non-sharp constant `C_chi`.

**DERIVED / CONSERVATIVE:** the coupling rigorously controls convergence to the rough endpoint on essentially the Brownian `1/sqrt(zeta)` scale, up to the logarithm introduced by uniform sup-norm control.

---

## 6. Paired Dieker–Yakir estimator

The same coupling gives a much better numerical estimator of the small difference

```math
\Delta_H(\chi,\zeta)
=\mathcal H_{mix}(\chi)-\mathcal H(\chi,\zeta).
```

Instead of estimating the two constants from independent path ensembles and subtracting them, generate one white-noise path and evaluate both the Brownian endpoint and its Gaussian-smoothed version on that **same** realization.

The paired estimator measures

```math
\Psi(W_{\infty})-\Psi(W_\zeta)
```

path by path. Because the two ratios are highly correlated, the Monte Carlo variance of their difference is far smaller than the variance of two independent estimates.

The implementation is stored in

```text
numerics/gaussian_mollifier_coupling.py
```

and also reports the analytic variance/drift bounds above.

---

## 7. Paired square-root diagnostic along the detector trajectories

Use the Step-23/26 endpoint tangent values

```text
chi_fast ~ 1.14e-4
chi_slow ~ 0.0645
```

and also the Step-25 diagnostic `chi=0.1`.

Representative paired estimates are:

```text
chi ~= 1.14e-4
zeta     sqrt(zeta) * Delta_H
20       0.00579 +/- 0.00005
40       0.00651 +/- 0.00004
80       0.00681 +/- 0.00006

chi ~= 0.0645
zeta     sqrt(zeta) * Delta_H
20       0.2037 +/- 0.0015
40       0.2072 +/- 0.0014
80       0.2116 +/- 0.0021

chi = 0.1
zeta     sqrt(zeta) * Delta_H
20       0.2757 +/- 0.0021
40       0.2760 +/- 0.0021
80       0.2783 +/- 0.0028
```

The paired calculation makes the square-root scaling much clearer than the independent Step-26 subtraction.

The coefficient is positive in all tested cases and is nearly constant from `zeta=20` to `80`, with mild pre-asymptotic drift at the very small fast-channel `chi`.

**NUMERICAL VALIDATION / NUMERICAL ASYMPTOTIC:** the positive `1/sqrt(zeta)` law is now supported by a common-random-number calculation whose uncertainty is small compared with the observed correction.

---

## 8. Relation to rigorous Brownian continuity corrections

For the **different** problem of observing Brownian extrema only on a grid with spacing `delta`, rigorous results establish a square-root continuity correction. In particular, the classical Brownian Pickands discretization error satisfies

```math
\mathcal H_1-\mathcal H_1^\delta
\sim
-\frac{\zeta_R(1/2)}{\sqrt\pi}\sqrt\delta,
```

and Brownian paths zoomed around their extrema have a two-sided Bessel local limit.

Relevant primary references:

- Bisewski & Jasnovidov, *On the speed of convergence of discrete Pickands constants to continuous ones*, arXiv:2108.00756 / J. Appl. Probab. 62 (2025), especially the exact `alpha=1` `sqrt(delta)` result.
- Dieker & Lagos, *On the Euler discretization error of Brownian motion about random times*, arXiv:1708.04356, especially the `sqrt(n)` height-error normalization and two-sided Bessel zoom-in process around extrema.

These theorems strongly support the mechanism found here: a Brownian local field perturbed over time scale `epsilon` naturally produces an extreme-height correction of order `sqrt(epsilon)`.

But Gaussian mollification is **not** Euler/grid discretization.

**REJECTED SHORTCUT:** the Brownian-grid continuity-correction theorem cannot simply be substituted for a proof of the Gaussian-mollifier coefficient `C_H(chi)`.

---

## 9. Why the rigorous `K` certificate still does not follow

Step 26 needs more than an upper convergence rate. To prove that the search-statistics correction eventually dominates the finite-window SNR penalty, one needs a **positive lower bound** such as

```math
\mathcal H_{mix}(\chi)-\mathcal H(\chi,\zeta)
\ge
\frac{c(\chi)}{\sqrt\zeta}
```

for all sufficiently large `zeta`, with `c(chi)>0` uniformly over the relevant fast/slow `chi` interval.

The common-white-noise coupling proves

```text
path perturbation amplitude = O(zeta^-1/2)
```

and the paired estimator shows numerically that the Pickands loss is indeed positive and of that order.

However, a small path perturbation can in principle have a functional effect smaller than its RMS amplitude. The upper coupling bound alone cannot exclude

```text
Delta_H = o(zeta^-1/2)
```

without additional information about the process **at its random maximizer**.

That is exactly where the Brownian Bessel zoom-in structure enters.

**NEGATIVE RESULT:** Step 27 does **not** yet produce a rigorous finite `K` beyond which the exact detector boundary derivative is certified negative.

The Step-26 eventual-negative-slope statement therefore remains **conditional**, although the square-root mechanism now has an exact pathwise origin and substantially stronger paired numerical support.

---

## 10. What a sharp proof now has to establish

The remaining mathematical problem is much smaller than before.

For the rough endpoint spectral field, let `tau_*` be its almost surely unique maximizer. On the smoothing time scale

```math
\epsilon=1/\zeta,
```

the Brownian part viewed around `tau_*` should have the standard two-sided Bessel extreme-point limit after height normalization by `sqrt(epsilon)`.

Gaussian low-pass smoothing has the rescaled kernel

```math
K_1(s)=\sqrt{2/\pi}\,e^{-2s^2}.
```

A sharp continuity-correction theorem would therefore identify a positive kernel-specific random functional of the two-sided Bessel limit and prove

```math
\boxed{
\sqrt\zeta
\left[
\mathcal H_{mix}(\chi)-\mathcal H(\chi,\zeta)
\right]
\longrightarrow C_H(\chi)>0.
}
```

The existing Brownian discretization literature supplies the correct **zoom-in architecture**, but the Gaussian convolution functional and its effect on the full Dieker–Yakir numerator/denominator ratio still have to be treated.

---

## 11. First nontrivial consequence

The numerical `1/sqrt(zeta)` law from Step 26 is no longer merely an unexplained fit.

The exact common-noise coupling proves that Gaussian smoothing changes the Brownian endpoint spectral path on the scale

```math
\boxed{
\Delta W=O_P\!\left(\sqrt{\chi/\zeta}\right),
}
```

while its deterministic drift correction is only `O(chi/zeta)`.

Thus the observed hierarchy

```text
extreme-statistics correction ~ zeta^-1/2
SNR correction               ~ kappa^-1
```

has a precise stochastic origin: **Brownian high-frequency path amplitude**, not the deterministic covariance correction.

The remaining gap is now specifically a continuity-correction theorem at the random maximum, not uncertainty about the underlying scale.

---

## 12. Stopping point

The Gaussian smoothing perturbation scale is derived exactly and the square-root Pickands correction is validated with a paired estimator, but a positive lower asymptotic coefficient has not yet been proved.

### Single natural next question

> Can the Brownian-extremum zoom-in / two-sided-Bessel theorem be adapted from grid discretization to Gaussian mollification of the Dieker–Yakir spectral field, yielding a positive kernel-specific continuity-correction constant `C_H(chi)` and finally converting the Step-26 eventual negative slope into a theorem with a finite certified onset bandwidth?
