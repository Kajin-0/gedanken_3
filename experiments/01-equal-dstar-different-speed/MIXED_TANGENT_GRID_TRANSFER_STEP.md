# Step 48 — Finite-u mixed-tangent transfer to the alpha=1 grid benchmark

**Date:** 2026-08-12 19:31 EDT  
**Status:** DERIVED / EXACT CELLWISE BRIDGE DECOMPOSITION / PAIRED FINITE-LEVEL TRANSFER INTERVAL / HARD-GATE PASSED / REFINEMENT / CORRECTION OF WORDING / OPEN. Step 47 left exactly one allowed target under the new stopping discipline: quantify the finite-threshold transfer between the mixed Brownian-parabola tangent and the pure `alpha=1` discrete-Pickands benchmark. This step materially reduces that uncertainty. The mixed tangent admits an exact cellwise Brownian-bridge decomposition; a paired generalized Dieker-Yakir calculation on nested grids shows that the mixed finite-grid loss differs from the exact pure-`alpha=1` loss by only `O(1e-5)` in relative intensity at the detector parameters. The result is a controlled Monte Carlo interval, not a theorem-level monotone comparison. It is nevertheless strong enough to show that, **within the mixed tangent**, the `.001`-grid correction is orders larger than the Step-44 finite-grid proof margin. No novelty claim.

---

## 1. Hard stopping rule

Following the Step-47 external review, no new conceptual branch is permitted unless it does one of the following:

1. gives an explicit one-sided finite-`u` comparison;
2. gives a controlled numerical interval for the mixed-to-`alpha=1` transfer strong enough to settle the present witness direction;
3. shows that no useful bound is available and stops the mathematical closure branch.

This step qualifies under item 2. It does **not** open another asymptotic branch.

---

## 2. Mixed rough-endpoint tangent at finite threshold

At the hard-window rough endpoint, the Step-29 tangent can be written

```math
\boxed{
W_\chi(t)
=\sqrt2 Zt-t^2
+2^{3/4}\sqrt\chi\,B(t)
-\sqrt2\chi|t|,
}
```

where `Z~N(0,1)` is independent of two-sided standard Brownian motion `B`.

For the Step-44 fast witness

```text
X = 7.16
u = 4.9589834838
```

and the exact rough covariance coefficients are

```text
a_X = 6.1914157127e-5
b_X = 1.0001238283.
```

Hence

```math
\chi=\frac{a_Xu}{\sqrt{b_X}}
=3.0701227479\times10^{-4}.
```

The physical timing step `dt` maps to tangent spacing

```math
\boxed{
\Delta
=\frac{u\sqrt{b_X}}{\sqrt2}\,dt.
}
```

At `dt=.001`,

```text
Delta = 0.003506747946.
```

The rough canonical spacing is therefore

```math
\boxed{
\delta
=\sqrt2\chi\Delta
=a_Xu^2dt
=1.5225630594\times10^{-6},
}
```

which is exactly the Step-47 `alpha=1` spacing.

---

## 3. Exact cellwise Brownian-bridge decomposition

Take one grid cell

```math
[t_k,t_{k+1}]=[k\Delta,(k+1)\Delta]
```

and write

```math
t=t_k+\theta\Delta,
\qquad 0\le\theta\le1.
```

The grid is aligned so that zero is a grid point. Therefore, on every open cell:

- `sqrt(2) Z t` is affine;
- `-sqrt(2) chi |t|` is affine;
- only `-t^2` has curvature;
- the Brownian component conditional on its cell endpoints is a standard Brownian bridge.

Consequently, conditional on the two mixed-tangent endpoint values,

```math
\boxed{
W_\chi(t_k+\theta\Delta)
=(1-\theta)W_k+\theta W_{k+1}
+\sqrt{2\delta}\,\mathbb B_k(\theta)
+\Delta^2\theta(1-\theta),
}
```

where `B_k` is a standard Brownian bridge on `[0,1]`, independent of the endpoint values and independent across cells given the Brownian grid skeleton.

This identity is exact for the mixed tangent. It is not a high-threshold approximation inside the tangent model.

The smooth finite-`u` contribution *inside a cell* is therefore just the deterministic concave bulge

```math
0\le\Delta^2\theta(1-\theta)
\le\frac{\Delta^2}{4}.
```

At the Step-44 grid,

```math
\boxed{
\varepsilon_{par}
=\frac{\Delta^2}{4}
=3.07432029\times10^{-6}.
}
```

Thus the cellwise departure from a piecewise-linear Brownian reconstruction is already tiny in tangent-height units.

---

## 4. Why Slepian monotonicity does not finish the problem

The mixed variogram at the rough endpoint is

```math
g_{mix}(t)=t^2+\sqrt2\chi|t|,
```

which pointwise dominates the pure rough variogram

```math
g_r(t)=\sqrt2\chi|t|.
```

Brown-Resnick Slepian comparison therefore orders the **continuous** generalized Pickands constants, and separately orders their **discrete** analogues on a fixed lattice.

But it does not order the ratio

```math
\frac{H^{\Delta}}{H^0}.
```

Both numerator and denominator move in the same direction under the variogram comparison, so no ratio ordering follows.

**REJECTED SHORTCUT:** coordinatewise variogram ordering is not by itself a finite-u discretization-ratio theorem.

This is consistent with the broader Step-25 warning that monotonicity of a generalized Pickands constant does not automatically lift to a coupled physical ratio.

---

## 5. Paired finite-level transfer calculation

Because the monotone-ratio shortcut fails, evaluate the transfer directly with common random numbers.

Use the exact two-sided Brownian mixed tangent above on

```text
-T <= t <= T,
T = 4,
```

and evaluate the generalized discrete Dieker-Yakir ratio

```math
H_{mix}^{\Delta}
=E\left[\frac{M_{\Delta}}{S_{\Delta}}\right]
```

on two nested lattices:

```text
coarse: Delta
fine:   Delta/128.
```

The same `Z`, Brownian increments, and path are used for both lattices. Three independent seeds of `3000` paths each give `9000` paired paths total.

The pooled estimates are

```text
H_mix^Delta        = 0.5677632065
H_mix^(Delta/128)  = 0.5682959763
```

so

```math
\boxed{
1-\frac{H_{mix}^{\Delta}}{H_{mix}^{\Delta/128}}
=9.374864864\times10^{-4}.
}
```

The paired standard error of this relative loss is approximately

```math
\boxed{5.5146\times10^{-6}.}
```

A normal Monte Carlo 95% interval is therefore approximately

```math
\boxed{
[9.2668,\ 9.4829]\times10^{-4}.
}
```

**QUALIFICATION:** this is a Monte Carlo interval, not a distribution-free finite-sample confidence theorem. The purpose is paired transfer control, not a publication-grade probability certificate.

---

## 6. Compare against the exact alpha=1 finite-level ratio

Step 47 gives the exact pure-rough constants. For the same two canonical spacings,

```text
H_1^delta          = 0.998983867710
H_1^(delta/128)    = 0.999910144119.
```

Thus

```math
\boxed{
1-\frac{H_1^{\delta}}{H_1^{\delta/128}}
=9.263596477\times10^{-4}.
}
```

The mixed-to-pure transfer residual is

```math
\boxed{
\mathcal E_{128}
:=
\frac{H_{mix}^{\Delta}}{H_{mix}^{\Delta/128}}
-
\frac{H_1^{\delta}}{H_1^{\delta/128}}
=-1.11268\times10^{-5}.
}
```

A directly paired estimator of this residual has standard error

```math
\boxed{5.5088\times10^{-6},}
```

corresponding to an approximate normal 95% interval

```math
\boxed{
[-2.1924\times10^{-5},\ -3.30\times10^{-7}].
}
```

The central result says that the finite-u mixed tangent loses about `1.1e-5` more relative intensity than the pure `alpha=1` benchmark between these two resolutions. The effect is about **1.2% of the discretization loss itself**, not an order-one transfer correction.

A separate `Delta/32` calculation with `20000` paired paths gave transfer residual

```text
-5.13e-6 +/- 3.58e-6 (1 SE),
```

and `T=3,4,5` sensitivity pilots all overlap statistically. These checks support the same `O(1e-5)` transfer scale.

---

## 7. Exact monotonic consequence inside the mixed tangent

For nested lattices, the generalized Pickands constant is nondecreasing as the lattice is refined:

```math
H_{mix}^{\Delta}
\le H_{mix}^{\Delta/128}
\le H_{mix}^{0}.
```

Therefore, without extrapolating the fine lattice to the continuum,

```math
\boxed{
1-\frac{H_{mix}^{\Delta}}{H_{mix}^{0}}
\ge
1-\frac{H_{mix}^{\Delta}}{H_{mix}^{\Delta/128}}.
}
```

The mixed-tangent continuum loss from the Step-44 grid is therefore at least the measured coarse-to-fine loss. Numerically that scale is about

```text
9.37e-4 relative intensity,
```

before any remaining `Delta/128 -> 0` correction.

This is more than twenty times the Step-44 finite-grid statistical margin

```text
4.22e-5 alpha.
```

**FIRST CONSEQUENCE:** within the finite-u mixed tangent, the `X=7.16`, `dt~.001` grid is not a plausible continuum certificate. This conclusion no longer depends on transferring the full Step-47 `alpha=1` correction all the way to the continuum; a directly resolved finite-level mixed correction is already much larger than the knife-edge margin.

Do not overstate this as a theorem for the full finite-window detector process. Higher-order covariance/tangent-transfer and the numerical constants outside the mixed tangent remain separate.

---

## 8. CORRECTION OF WORDING from Steps 46–47

The Step-46 paired value

```text
(5.3010 +/- 2.5069)e-4 alpha
```

was driven by five missed events and has about `47%` relative standard error.

Therefore earlier wording such as

```text
"almost exactly"
"essentially exact agreement"
```

is withdrawn as an empirical claim.

The defensible statement is:

> The observed nested-grid correction has the predicted sign and scale and is statistically consistent with the parameter-free Brownian/discrete-Pickands prediction; the Step-46 experiment did not verify the coefficient to high relative precision.

This wording correction does not change the numerical values or the mathematical Step-47 canonical identity.

---

## 9. What the hard gate decides

Step 48 **does reduce the designated finite-u transfer uncertainty**, so the closure branch is not stopped at this step.

What is now known:

```text
pure alpha=1 finite-grid correction:
    exact;

mixed Brownian-parabola cell structure:
    exact;

mixed-vs-pure finite-level transfer at the working parameters:
    numerically O(1e-5), with paired uncertainty quantified;

mixed coarse -> Delta/128 correction:
    ~9.37e-4 relative intensity, already >> Step-44 margin.
```

What is not known:

```text
- a theorem-level one-sided mixed/pure ratio comparison;
- a distribution-free confidence interval for the paired DY transfer;
- the higher-order transfer from the mixed tangent to the exact finite-window Gaussian scan at u~4.96;
- formal interval arithmetic for the covariance constants.
```

The next step, if any, must attack the **exact-process remainder beyond the mixed tangent**. Another Pickands constant, another witness scan, or another leading asymptotic would violate the hard stopping rule.

---

## 10. Stopping point

The pure `alpha=1` benchmark is not being distorted by an order-one finite-u Brownian-parabola effect at the detector parameters. Direct paired finite-level calculations place that transfer at the `1e-5` relative-intensity scale, while the resolved mixed grid correction itself is `~9e-4`.

### Single natural next question

> Can the exact finite-window covariance be bracketed around the mixed tangent on the `Delta/128` extremal neighborhood strongly enough to bound the remaining exact-process remainder, or does that final remainder fail the hard stopping test and force consolidation?
