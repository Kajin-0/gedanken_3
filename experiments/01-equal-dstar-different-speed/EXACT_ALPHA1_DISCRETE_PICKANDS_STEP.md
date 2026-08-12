# Step 47 — Exact finite-grid correction for the alpha=1 canonical rough tangent

**Date:** 2026-08-12 19:12 EDT  
**Status:** DERIVED / EXACT CANONICAL FINITE-GRID CORRECTION / REFINEMENT / NEGATIVE RESULT / OPEN. Step 46 identified the rough-endpoint grid bias as a missed-maximum effect with the Brownian `sqrt(dt)` continuity-correction constant. This step sharpens only that canonical rough-tangent part. For the `alpha=1` Pickands tangent, the discrete Pickands constant is available in closed random-walk form, so its continuum-to-grid intensity loss can be evaluated at finite grid spacing without taking `dt -> 0`. At the present `X=7.16`, `u~4.95898`, `a_X~6.19142e-5`, and physical grid `dt=.001`, the exact canonical tangent loss is `1.0161323e-3`, essentially the Step-46 `1.025e-3` estimate. The `.001 -> .00025` canonical difference is `5.07937e-4`, again matching the paired nested-grid result `(5.301 +/- 2.507)e-4`. **REFINEMENT:** finite grid spacing is not the unresolved issue inside the alpha=1 Brownian tangent. The surviving theorem gap is transfer from that canonical high-threshold tangent to the actual finite-`u~4.96` mixed smooth/rough Gaussian process. No novelty claim.

---

## 1. Canonical alpha=1 tangent

For a stationary unit Gaussian process with local covariance

```math
R(h)=1-a|h|+o(|h|),
```

Pickands scaling around a high threshold `u` uses the local time coordinate

```math
s=a u^2 t.
```

The canonical alpha=1 tangent field is

```math
W(s)=\sqrt{2}B(s)-|s|,
```

with `B` standard Brownian motion.

A physical timing grid of spacing `dt` therefore becomes the canonical grid

```math
\boxed{\delta=a u^2 dt.}
```

The continuous Pickands constant is exactly

```math
\mathcal H_1^0=1.
```

For `delta>0`, the discrete constant can be reduced to a Gaussian random walk and Spitzer/Wiener-Hopf factorization gives

```math
\boxed{
\mathcal H_1^\delta
=\frac{1}{\delta}
\exp\!\left[
-2\sum_{n=1}^{\infty}\frac1n
\Phi\!\left(-\sqrt{\frac{n\delta}{2}}\right)
\right].
}
```

Equivalently, with the standard Gaussian overshoot function

```math
\nu(x)
=\frac{2}{x^2}
\exp\!\left[
-2\sum_{n=1}^{\infty}\frac1n
\Phi\!\left(-\frac{x\sqrt n}{2}\right)
\right],
```

we have

```math
\boxed{\mathcal H_1^\delta=\nu(\sqrt{2\delta}).}
```

The general discrete Pickands representation and the high-threshold continuous/discrete Gaussian extreme asymptotics are given in Bisewski, Hashorva & Shevchenko, *The harmonic mean formula for random processes*, arXiv:2106.11707, Theorem 2.3 and Remark 2.4. Bisewski & Jasnovidov, *On the speed of convergence of discrete Pickands constants to continuous ones*, arXiv:2108.00756 / J. Appl. Probab. 62 (2025), prove a one-sided discretization-error rate for the Pickands constants, with the correct order for `alpha<=1`.

The explicit alpha=1 expression above is obtained by applying the Gaussian random-walk factorization to that discrete representation.

---

## 2. Small-grid expansion is exceptionally accurate here

Set

```math
x=\sqrt{2\delta}.
```

Writing `t=x^2/8` and differentiating the defining series gives a polylogarithm expansion. After integrating and fixing the constant by `nu(0)=1`,

```math
\boxed{
\log\nu(x)
=-\beta x
-\frac{\zeta(-1/2)}{24\sqrt{2\pi}}x^3
+\frac{\zeta(-3/2)}{640\sqrt{2\pi}}x^5
+O(x^7),
}
```

where

```math
\boxed{
\beta=-\frac{\zeta(1/2)}{\sqrt{2\pi}}
=0.5825971579\ldots
}
```

is the same continuity-correction constant used in Step 46.

For the present problem `x<.002`, so the cubic correction to `log nu` is only of order `1e-11`. Numerically, `exp(-beta x)` already reproduces the exact canonical finite-grid correction to much better precision than anything required by the detector calculation.

Thus Step 46's `sqrt(dt)` law was not merely getting the scaling right: it was already operating in a regime where the exact finite-grid alpha=1 correction is almost indistinguishable from its first term.

---

## 3. Exact canonical correction at X=7.16

Use

```text
X      = 7.16
u      = 4.9589834838
a_X    = 6.1914157127e-5.
```

For each physical grid spacing,

```math
\delta=a_Xu^2dt,
\qquad
x=\sqrt{2\delta}=u\sqrt{2a_Xdt}.
```

The resulting canonical discrete constants are

```text
dt         delta              x                 H_1^delta          loss 1-H_1^delta
------------------------------------------------------------------------------------------------
.00100     1.52256306e-6      .00174502897      .998983867710      1.016132290e-3
.00050     7.61281530e-7      .00123392182      .999281378993      7.186210075e-4
.00025     3.80640765e-7      .00087251449      .999491804717      5.081952830e-4
```

Therefore the exact canonical tangent prediction for the coarse-to-fine change is

```math
\boxed{
(1-\mathcal H_1^{\delta_{.001}})
-(1-\mathcal H_1^{\delta_{.00025}})
=5.07937007\times10^{-4}.
}
```

Step 46's paired nested-grid result was

```math
\boxed{
(5.3010\pm2.5069)\times10^{-4}\,\alpha.
}
```

The agreement remains essentially exact at the available Monte Carlo precision, now without replacing the canonical finite-grid correction by its `dt->0` first-order term.

---

## 4. Relation to the Step-46 hazard conversion

At high threshold the alpha=1 Pickands law gives

```math
p_{cont}
\sim \ell\,a u^2 Q(u)\,\mathcal H_1^0,
```

while a physical grid `dt` gives

```math
p_{grid}
\sim \ell\,a u^2 Q(u)\,\mathcal H_1^{a u^2dt}.
```

Hence within the canonical high-threshold tangent

```math
\boxed{
\frac{p_{grid}}{p_{cont}}
=\nu\!\left(u\sqrt{2a\,dt}\right)
}
```

at finite canonical grid spacing.

For a small loss,

```math
1-\nu(u\sqrt{2a dt})
\sim \beta u\sqrt{2a dt}.
```

Step 46 instead wrote the probability correction as

```math
h_a(u)\,\beta\sqrt{2a dt}.
```

Since the measured rare-cluster hazard satisfies `h_a/N_a~5` and `u~4.959`, these are the same leading mechanism. The exact discrete Pickands expression explains why the numerical coefficient matched so well.

---

## 5. What has actually been closed

The following question is no longer open **inside the canonical alpha=1 tangent model**:

```text
How large is the continuum-to-grid correction at a finite timing step?
```

It is exactly encoded by

```math
\boxed{
1-\mathcal H_1^{a u^2dt}
=1-\nu(u\sqrt{2a dt}).
}
```

At `X=7.16`, `dt=.001`, this is

```math
\boxed{1.0161323\times10^{-3}.}
```

So the Step-46 central continuum correction was not being driven by an uncontrolled `dt->0` extrapolation.

---

## 6. NEGATIVE RESULT — this is not yet the desired finite-u theorem

The physical detector timing process at the working threshold is not literally the asymptotic alpha=1 tangent.

The canonical relation above follows after the high-threshold Pickands zoom-in. Our operating threshold is only

```text
u ~ 4.96,
```

and earlier Steps 24–30 showed that the finite-`u` local field retains an important smooth Brownian-parabola component in addition to the cusp. Step 39 likewise showed that finite-`u` cluster intensity differs substantially in amplitude from its leading tangent approximation.

Therefore the exact identity

```math
p_grid/p_cont = H_1^delta
```

must **not** be asserted for the actual finite-`u` timing process.

The remaining theorem gap has become narrower and more precise:

```math
\boxed{
\text{bound the finite-}u\text{ transfer error between the actual grid/continuum ratio and }
\mathcal H_1^{a u^2dt}.
}
```

This is different from the Step-46 formulation. We no longer need a finite-`dt` theorem for Brownian discretization itself; that canonical finite-grid problem is explicit. We need a finite-threshold comparison between the true mixed Gaussian extremum and its alpha=1 canonical discretization ratio.

---

## 7. First nontrivial consequence

Step 46's asymptotic `~1.03e-3 alpha` correction can be replaced, at the canonical-tangent level, by the finite-grid value

```math
\boxed{1.01613\times10^{-3}\,\alpha}
```

when the continuum event is itself of order `alpha`.

The numerical difference is small; the conceptual change is substantial. **Finite grid spacing is no longer the uncertain part of the Brownian correction. Finite threshold is.**

---

## 8. Stopping point

The alpha=1 discrete Pickands constant supplies the full finite-grid Brownian continuity correction. The next step should not seek another `sqrt(dt)` estimate. It should compare the actual finite-`u` mixed tangent/grid problem against this exact alpha=1 discrete benchmark.

### Single natural next question

> Can the mixed Brownian-parabola tangent from Steps 24–30 be compared monotonically with the pure alpha=1 Pickands tangent strongly enough to bound the finite-`u` grid/continuum ratio around the exact value `H_1^{a u^2 dt}`?
