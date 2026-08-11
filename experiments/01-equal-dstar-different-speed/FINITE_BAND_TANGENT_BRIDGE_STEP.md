# Step 24 — Finite-Band Tangent Bridge: `H_mix(chi)` Is Not Enough

**Date:** 2026-08-11 19:21 EDT  
**Status:** DERIVED / REFINEMENT / REJECTED SHORTCUT / OPEN. Step 23 reduced the `kappa=infinity` finite-window problem to a mixed smooth/rough tangent process governed by `chi=a_x u/sqrt(b_x)`. This step asks whether computing that one-parameter generalized Pickands constant is enough to determine the *finite-kappa* high-band approach and exclude a bounded re-entrant preference pocket. It is not. The Gaussian information cutoff introduces a second independent local parameter, and the endpoint-cusp smoothing can be integrated in closed form. The finite-band tangent field is therefore governed by a two-parameter generalized Pickands problem `H(chi,zeta)`, with `zeta=kappa/(sqrt(2) u sqrt(b_x))`. No re-entrant-pocket theorem or novelty claim.

---

## 1. Question

Step 23 found the infinite-band matched coordinate

```math
\chi_x=\frac{a_xu}{\sqrt{b_x}},
```

with local tangent variance

```math
\operatorname{Var}\eta_\chi(t)
=t^2+\sqrt2\chi|t|.
```

The proposed next shortcut was:

> Compute `H_mix(chi)` accurately and use it as the deterministic finite-band high-kappa boundary formula.

That is insufficient because `H_mix(chi)` already assumes the information-band cutoff has been removed.

At finite `kappa`, the cutoff smooths the cusp below a physical lag of order `1/kappa`. Whether that smoothing is visible on the high-excursion scale is a separate question from whether the hard-window cusp coefficient `a_x` is small.

---

## 2. Universal Gaussian smoothing of the `1/nu^2` endpoint tail

The hard endpoint of

```math
h_x(v)=v e^{-v}1_{[0,x]}(v)
```

produces the high-frequency timing-spectrum tail responsible for the covariance cusp. The leading tail contribution has the universal form `const/nu^2`.

Under the Step-15 Gaussian information penalty

```math
e^{-(\nu/\kappa)^2},
```

the local cusp contribution reduces to

```math
J(y,\kappa)
=
\int_0^\infty
\frac{1-\cos(\nu y)}{\nu^2}
 e^{-(\nu/\kappa)^2}d\nu.
```

Differentiate twice:

```math
\frac{\partial^2J}{\partial y^2}
=
\int_0^\infty
\cos(\nu y)e^{-(\nu/\kappa)^2}d\nu
=
\frac{\sqrt\pi\kappa}{2}
 e^{-(\kappa y)^2/4}.
```

Using `J(0,kappa)=J_y(0,kappa)=0` gives the exact closed form

```math
\boxed{
J(y,\kappa)
=
\frac{\pi|y|}{2}
\operatorname{erf}\!\left(\frac{\kappa|y|}{2}\right)
+
\frac{\sqrt\pi}{\kappa}
\left[e^{-(\kappa y)^2/4}-1\right].
}
```

This is not an empirical interpolation.

Its two local limits are

```math
J(y,\kappa)
\sim
\frac{\sqrt\pi\kappa}{4}y^2,
\qquad
\kappa|y|\ll1,
```

and

```math
J(y,\kappa)
=
\frac{\pi|y|}{2}
-\frac{\sqrt\pi}{\kappa}
+o(\kappa^{-1}),
\qquad
\kappa|y|\gg1.
```

Thus a finite information band is locally quadratic at sufficiently tiny lag but recovers the hard-window cusp outside the `~1/kappa` boundary layer.

---

## 3. Matched finite-band local covariance

Step 23 gave the unregularized local law

```math
1-R_x(y)
= a_x|y|+\frac{b_x}{2}y^2+\cdots.
```

Matching the `J` outer limit to the cusp coefficient gives the joint local/high-band approximation

```math
\boxed{
1-R_{x,\kappa}(y)
\sim
\frac{b_x}{2}y^2
+
\frac{2a_x}{\pi}J(y,\kappa).
}
```

This immediately reproduces the Step-17 divergent smooth curvature. For `kappa|y| << 1`,

```math
1-R_{x,\kappa}(y)
\sim
\frac12
\left(
 b_x+\frac{a_x\kappa}{\sqrt\pi}
\right)y^2,
```

so

```math
\boxed{
-R_{x,\kappa}''(0)
\sim
b_x+\frac{a_x\kappa}{\sqrt\pi}.
}
```

The previously derived `a_x kappa/sqrt(pi)` growth is therefore exactly the small-lag Gaussian smoothing of the hard-window endpoint tail.

---

## 4. A second dimensionless parameter is unavoidable

Retain the Step-23 smooth high-excursion scale

```math
q(u)=\frac{\sqrt2}{u\sqrt{b_x}}.
```

The finite bandwidth boundary-layer coordinate on this scale is

```math
\frac{\kappa q(u)}{2}
=
\boxed{
\zeta_x
=
\frac{\kappa}
{\sqrt2\,u\sqrt{b_x}}.
}
```

Thus there are **two** independent local coordinates:

```math
\boxed{
\chi_x=\frac{a_xu}{\sqrt{b_x}},
\qquad
\zeta_x=\frac{\kappa}{\sqrt2\,u\sqrt{b_x}}.
}
```

`chi` measures rough-endpoint strength relative to the smooth core.

`zeta` measures whether the finite-band smoothing layer `1/kappa` is resolved on the high-excursion scale `q(u)`.

**REJECTED SHORTCUT:** `H_mix(chi)` alone cannot describe the finite-`kappa` approach to the rough limit, because two processes with identical `(x,u)` and hence identical `chi` but different `kappa` have different local excursion fields.

---

## 5. Exact two-parameter tangent variogram

Insert

```math
y=q(u)t
```

into the matched local covariance and multiply by `u^2`.

Using

```math
\chi=\frac{a_xu}{\sqrt{b_x}},
\qquad
\zeta=\frac{\kappa}{\sqrt2u\sqrt{b_x}},
```

gives

```math
\boxed{
\begin{aligned}
g_{\chi,\zeta}(t)
&=\lim u^2[1-R_{x,\kappa}(q(u)t)]\\
&=t^2
+\sqrt2\chi
\left[
|t|\operatorname{erf}(\zeta|t|)
+\frac{e^{-\zeta^2t^2}-1}
{\sqrt\pi\,\zeta}
\right].
\end{aligned}
}
```

This is the finite-band extension of the Step-23 tangent variance.

### Infinite-band endpoint

As

```math
\zeta\to\infty,
```

```math
\operatorname{erf}(\zeta|t|)\to1,
```

and the exponential correction vanishes, so

```math
\boxed{
g_{\chi,\infty}(t)=t^2+\sqrt2\chi|t|.}
```

This recovers Step 23 exactly.

### Strong local smoothing endpoint

As

```math
\zeta\to0,
```

the bracket is

```math
\frac{\zeta t^2}{\sqrt\pi}+O(\zeta^3t^4),
```

hence

```math
\boxed{
g_{\chi,\zeta}(t)
=
\left[1+
\frac{\sqrt2\chi\zeta}{\sqrt\pi}
\right]t^2+\cdots.}
```

Since

```math
\sqrt2\chi\zeta
=\frac{a_x\kappa}{b_x},
```

this is precisely the finite-band curvature result above.

So the smooth finite-`kappa` and rough `kappa=infinity` timing scans are themselves the two limits of **one two-parameter tangent field**.

---

## 6. The correct generalized Pickands object

Let `eta_{chi,zeta}` be a centered Gaussian process with stationary increments and variance function

```math
\operatorname{Var}\eta_{\chi,\zeta}(t)
=g_{\chi,\zeta}(t).
```

The finite-band matched high-threshold constant is therefore

```math
\boxed{
\mathcal H(\chi,\zeta)
=\lim_{T\to\infty}\frac1T
E\exp\!\left[
\sup_{0\le t\le T}
\left(
\sqrt2\eta_{\chi,\zeta}(t)
-g_{\chi,\zeta}(t)
\right)
\right].
}
```

It satisfies

```math
\boxed{
\mathcal H(\chi,\infty)
=\mathcal H_{mix}(\chi).
}
```

At the opposite endpoint, `zeta -> 0`, the tangent becomes purely quadratic and therefore tends to the corresponding scaled `alpha=2` Pickands constant.

Generalized Pickands constants for broad stationary-increment Gaussian processes and Dieker–Yakir-type expectation representations are established in the probability literature; this two-parameter tangent falls naturally into that framework. See Dębicki, Engelke & Hashorva, *Generalized Pickands constants and stationary max-stable processes*, arXiv:1602.01613, especially their Gaussian stationary-increment setting and generalized Dieker–Yakir representation.

---

## 7. Why this matters for the re-entrant-pocket question

Step 23 anchored only the endpoint

```text
kappa = infinity.
```

A bounded re-entrant pocket, if it exists, is a property of the *approach* to that endpoint.

That approach cannot be determined from

```math
\mathcal H_{mix}(\chi)
```

alone because `zeta` changes continuously with `kappa` even when `chi` is held fixed.

For the Step-20/23 task, `u` is only about `5`, so in the high-band region

```text
kappa ~ 20   -> zeta = O(3)
kappa ~ 60   -> zeta = O(9)
kappa ~130   -> zeta = O(19)
kappa ~300   -> zeta = O(40+)
```

for `b_x ~ 1`.

Thus the finite-band field is already moving toward the `zeta=infinity` mixed limit in the region of interest, but its residual correction is a distinct asymptotic variable and cannot be deleted a priori.

---

## 8. What this step establishes

### DERIVED

- exact Gaussian smoothing integral `J(y,kappa)` for the endpoint `1/nu^2` timing-spectrum tail;
- recovery of the Step-17 curvature divergence from that smoothing layer;
- second dimensionless high-excursion coordinate

```math
\boxed{\zeta=\kappa/(\sqrt2u\sqrt b)};
```

- two-parameter tangent variogram `g_{chi,zeta}`;
- exact recovery of the Step-23 mixed rough/smooth field as `zeta -> infinity`;
- exact recovery of the smooth finite-band quadratic field as `zeta -> 0`.

### REFINEMENT / REJECTED SHORTCUT

Computing only `H_mix(chi)` cannot by itself produce a deterministic finite-band boundary or rule out a bounded re-entrant pocket. The finite-band approach requires at least the two-parameter generalized constant

```math
\boxed{\mathcal H(\chi,\zeta)}.
```

### OPEN

- numerical evaluation of `H(chi,zeta)` with controlled continuous-time discretization error;
- finite-`u` correction at `u~5`;
- a uniform finite-`kappa` error bound connecting the tangent law to the exact finite-window process;
- monotonicity, if any, of the resulting finite-`kappa` preference boundary;
- exclusion or construction of a bounded re-entrant slow-preferred pocket;
- hardware interpretation;
- novelty.

---

## 9. First nontrivial consequence

The high-band problem has **two independent singular limits**, not one:

```text
hard-window strength relative to smooth excursion core -> chi
finite information-band smoothing relative to excursion scale -> zeta
```

The one-parameter Step-23 constant is therefore an endpoint theory, not the complete finite-band bridge.

---

## 10. Stopping point

The correct local object for deterministic high-band continuation is now identified.

### Single natural next question

> Can the two-parameter generalized Pickands constant `H(chi,zeta)` be evaluated efficiently using a Dieker–Yakir representation, and does its dependence on `zeta` have enough monotonic structure to control the finite-band approach and rule out a bounded re-entrant preference pocket?
