# Step 25 — Generalized Dieker–Yakir Representation and Exact Monotonicity of the Two-Parameter Constant

**Date:** 2026-08-11 19:38 EDT  
**Status:** DERIVED / NUMERICAL VALIDATION / REFINEMENT / REJECTED SHORTCUT / OPEN. Step 24 identified the finite-band tangent field `g_{chi,zeta}`. This step proves that its generalized Pickands constant admits a continuous Dieker–Yakir expectation representation, derives an efficient FFT simulation decomposition, and proves that the constant is nondecreasing in both `chi` and `zeta` by Brown–Resnick Slepian comparison. This removes one possible mechanism for a bounded re-entrant detector-preference pocket: the local extreme constant itself cannot oscillate with bandwidth. However, monotonicity of the local constant is not sufficient to prove monotonicity of the full detector preference boundary because the physical sweep also changes finite-duration SNR, available threshold, `chi`, `zeta`, and the common decision time differently for the two detectors. No re-entrant-pocket theorem and no novelty claim.

---

## 1. Question

Step 24 showed that the correct local finite-band object is

```math
\mathcal H(\chi,\zeta),
```

not merely the infinite-band endpoint `H_mix(chi)`.

The next questions are:

1. can `H(chi,zeta)` be evaluated efficiently without returning to rare maxima of the full detector process?;
2. does its `zeta` dependence have enough monotonic structure to control the finite-band approach?;

The first answer is **yes**. The second answer is **partly**: `H` is rigorously monotone in `zeta`, but that alone does not prove monotonicity of the full fast/slow boundary.

---

## 2. Tangent variogram from Step 24

Write

```math
\boxed{
\begin{aligned}
g_{\chi,\zeta}(t)
&=t^2
+\sqrt2\chi F_\zeta(t),\\
F_\zeta(t)
&=|t|\operatorname{erf}(\zeta|t|)
+\frac{e^{-\zeta^2t^2}-1}{\sqrt\pi\,\zeta}.
\end{aligned}
}
```

Let `eta_{chi,zeta}` be a centered Gaussian process with stationary increments and variance

```math
\operatorname{Var}\eta_{\chi,\zeta}(t)=g_{\chi,\zeta}(t).
```

Define the Brown–Resnick spectral process

```math
\boxed{
W_{\chi,\zeta}(t)
=\sqrt2\,\eta_{\chi,\zeta}(t)
-g_{\chi,\zeta}(t).
}
```

Since

```math
\operatorname{Var}[\sqrt2\eta_{\chi,\zeta}(t)]
=2g_{\chi,\zeta}(t),
```

this has the canonical Gaussian Brown–Resnick form

```math
B(t)-\frac12\operatorname{Var}B(t).
```

---

## 3. Dieker–Yakir representation applies directly

For fixed finite `(chi,zeta)`,

```math
g_{\chi,\zeta}(t)
=t^2+O(|t|)
\qquad(|t|\to\infty).
```

Thus the Gaussian variance grows quadratically and dominates logarithmic growth at infinity. The generalized Gaussian Pickands theory of Dębicki, Engelke & Hashorva therefore applies to this process.

The continuous generalized Pickands constant admits the Dieker–Yakir expectation representation

```math
\boxed{
\mathcal H(\chi,\zeta)
=E\left[\frac{M}{S}\right],
}
```

where

```math
\boxed{
M=\sup_{t\in\mathbb R}e^{W_{\chi,\zeta}(t)},
\qquad
S=\int_{\mathbb R}e^{W_{\chi,\zeta}(t)}dt.
}
```

Unlike the defining limit

```math
T^{-1}E\sup_{0\le t\le T}e^{W(t)},
```

this is a single expectation over the whole spectral shape. Numerically one still truncates the real line and discretizes time, but there is no outer `T -> infinity` normalization to estimate.

Primary reference: Dębicki, Engelke & Hashorva, *Generalized Pickands constants and stationary max-stable processes*, 2017, Theorem 2 and the continuous Dieker–Yakir representation.

---

## 4. Efficient process decomposition

The smoothed rough component has a particularly simple Gaussian construction.

For `t >= 0`,

```math
F_\zeta''(t)
=\frac{2\zeta}{\sqrt\pi}e^{-\zeta^2t^2}.
```

Hence there exists a stationary zero-mean Gaussian derivative process `Y_zeta` with covariance

```math
\boxed{
E[Y_\zeta(0)Y_\zeta(t)]
=\frac{\zeta}{\sqrt\pi}e^{-\zeta^2t^2}.
}
```

Let

```math
B_\zeta(t)=\int_0^tY_\zeta(s)ds.
```

Then

```math
\operatorname{Var}B_\zeta(t)=F_\zeta(t).
```

Therefore

```math
\boxed{
\eta_{\chi,\zeta}(t)
=Zt+2^{1/4}\sqrt\chi\,B_\zeta(t),
}
```

with `Z ~ N(0,1)` independent of `B_zeta`.

The derivative process has spectral density

```math
\boxed{
S_Y(\omega)=e^{-\omega^2/(4\zeta^2)}.
}
```

So a finite-`zeta` sample can be generated efficiently by FFT spectral synthesis of a smooth stationary Gaussian process followed by one cumulative integration. No dense covariance factorization is required.

The implementation is stored in

```text
numerics/two_parameter_pickands_dy.py
```

---

## 5. Exact monotonicity in `zeta`

Differentiate `F_zeta` at fixed nonzero `t`:

```math
\boxed{
\frac{\partial F_\zeta(t)}{\partial\zeta}
=
\frac{1-e^{-\zeta^2t^2}}
{\sqrt\pi\,\zeta^2}
>0.
}
```

Therefore

```math
\boxed{
\frac{\partial g_{\chi,\zeta}(t)}{\partial\zeta}
=
\frac{\sqrt2\chi}{\sqrt\pi\,\zeta^2}
\left(1-e^{-\zeta^2t^2}\right)
\ge0.
}
```

Thus for `zeta_2 > zeta_1`,

```math
g_{\chi,\zeta_2}(t)
\ge
g_{\chi,\zeta_1}(t)
\qquad\forall t.
```

For Brown–Resnick stationary max-stable processes, the Slepian comparison theorem states that pointwise ordering of the Gaussian stationary-increment variograms orders both compact-set supremum tails and the corresponding Pickands constants.

Hence

```math
\boxed{
\zeta_2>\zeta_1
\Longrightarrow
\mathcal H(\chi,\zeta_2)
\ge
\mathcal H(\chi,\zeta_1).
}
```

This monotonicity is exact, not asymptotic.

Primary reference: Dębicki & Hashorva, *Approximation of Supremum of Max-Stable Stationary Processes and Pickands Constants*, Theorem 3.1 (Brown–Resnick Slepian inequality).

---

## 6. Exact monotonicity in `chi`

Since

```math
F_\zeta(t)\ge0,
```

we also have

```math
\boxed{
\frac{\partial g_{\chi,\zeta}(t)}{\partial\chi}
=\sqrt2F_\zeta(t)
\ge0.
}
```

The same Brown–Resnick Slepian comparison gives

```math
\boxed{
\chi_2>\chi_1
\Longrightarrow
\mathcal H(\chi_2,\zeta)
\ge
\mathcal H(\chi_1,\zeta).
}
```

So the local generalized Pickands constant is coordinatewise nondecreasing on the `(chi,zeta)` plane.

---

## 7. Immediate deterministic bounds

At fixed `chi`, the strong-smoothing endpoint is purely quadratic:

```math
\zeta\to0
\quad\Rightarrow\quad
g_{\chi,\zeta}(t)\to t^2.
```

Therefore

```math
\mathcal H(\chi,0)=\frac1{\sqrt\pi}.
```

At the opposite endpoint,

```math
\mathcal H(\chi,\infty)=\mathcal H_{mix}(\chi).
```

Monotonicity gives the bracket

```math
\boxed{
\frac1{\sqrt\pi}
\le
\mathcal H(\chi,\zeta)
\le
\mathcal H_{mix}(\chi).
}
```

Thus finite-band smoothing can only lower the local extreme constant relative to the hard-band endpoint; it cannot overshoot and return.

---

## 8. Direct Dieker–Yakir numerical validation

A continuous-ratio Monte Carlo estimator was implemented using the FFT derivative construction above. The real line is truncated at `|t|<=8` and the time grid is refined with `zeta` so the smoothing scale `1/zeta` remains resolved.

For representative

```text
chi = 0.1
```

the estimates are

```text
zeta      H_hat(0.1,zeta)      MC standard error
-------------------------------------------------
1         0.58683               0.00054
3         0.62310               0.00092
9         0.67671               0.00111
19        0.70538               0.00117
40        0.72422               0.00151
infinity  0.76698               0.00105
```

The sequence agrees with the exact monotonicity theorem.

Representative grid refinement checks:

```text
chi=0.1, zeta=9:
    coarse ~0.6742
    fine   ~0.6748

chi=0.1, zeta=19:
    coarse ~0.7058
    fine   ~0.7061
```

with differences smaller than the corresponding Monte Carlo uncertainty.

The exact smooth checkpoint `chi=0` gives

```math
\mathcal H(0,\zeta)=1/\sqrt\pi
```

for every `zeta`, and the implementation reproduces this to numerical precision.

**NUMERICAL VALIDATION:** the generalized Dieker–Yakir estimator is practical for the `(chi,zeta)` range relevant to the high-band detector problem and reproduces both the exact smooth endpoint and the theorem-level monotonic trend.

---

## 9. Does monotonicity rule out the detector re-entrant pocket?

No—not by itself.

The physical bandwidth sweep does not move only `zeta` at fixed tangent field.

For each detector, changing `kappa` also changes:

```text
finite-duration accessible SNR rho(x,kappa)
available decision threshold u = rho - z_beta
chi = a_x u / sqrt(b_x)
zeta = kappa/(sqrt(2) u sqrt(b_x))
common physical decision time X
and therefore x_f=X, x_s=X/r.
```

The fast/slow boundary compares two different generalized constants evaluated along two different trajectories in `(chi,zeta,x,u)` space.

Therefore

```math
\mathcal H(\chi,\zeta)
\text{ monotone in }\zeta
```

does **not** imply

```math
\Lambda_\times(\kappa_f)
\text{ monotone in }\kappa_f.
```

**REJECTED SHORTCUT:** Brown–Resnick Slepian monotonicity of the local constant is insufficient to prove global monotonicity of the detector preference boundary.

---

## 10. First nontrivial consequence

A bounded high-band re-entrant detector-preference pocket, if it exists, cannot be caused by an oscillatory or nonmonotone finite-band generalized Pickands constant.

The local extreme constant satisfies

```math
\boxed{
\partial_\zeta\mathcal H\ge0,
\qquad
\partial_\chi\mathcal H\ge0.
}
```

Any re-entrance must therefore emerge from the **coupled detector problem**: competing bandwidth dependence of SNR recovery, available threshold, finite integration duration, and the fact that the fast and slow channels trace different paths through `(chi,zeta)`.

This substantially narrows the remaining mechanism even though it does not yet exclude it.

---

## 11. What remains open

- deterministic evaluation of `H(chi,zeta)` over the full detector trajectory with quantified grid/truncation error;
- controlled finite-`u` correction connecting the tangent constant to the exact finite-window false-alarm probability at `u~5`;
- a uniform high-band expansion for the *difference* between the fast and slow detector boundaries;
- proof or counterexample for monotonic convergence of `Lambda_cross(kappa_f)`;
- exclusion or construction of a bounded high-band re-entrant preference pocket;
- hardware interpretation;
- novelty.

---

## 12. Stopping point

The two-parameter generalized Pickands constant is now computationally tractable and has exact coordinatewise monotonicity, but that monotonicity does not automatically lift to the physical detector preference boundary.

### Single natural next question

> Can the deterministic Dieker–Yakir estimates of `H(chi,zeta)` be inserted into the finite-`u` boundary equation and asymptotically expanded along the *actual fast and slow detector trajectories* to determine the sign of `d Lambda_cross / d kappa_f` at high bandwidth, rather than relying on monotonicity of `H` alone?
