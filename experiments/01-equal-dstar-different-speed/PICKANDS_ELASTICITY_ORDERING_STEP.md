# Step 38 — Cross-Elasticity Ordering of the Two-Parameter Pickands Constant

**Date:** 2026-08-12 01:11 EDT  
**Status:** DERIVED / EXACT VARIOGRAM ORDERING / EXACT TANGENT-HAZARD BOUND / REFINEMENT / NEGATIVE RESULT / OPEN. Step 37 reduced the finite-crossover hazard problem to logarithmic elasticities of the two-parameter generalized Pickands constant `H(chi,zeta)`. This step proves an exact cross-ordering between the `chi` and `zeta` directions. The finite-band smoothing function satisfies `0 <= zeta d_zeta F_zeta <= F_zeta`, which implies `H(chi,lambda zeta) <= H(lambda chi,zeta)` for every `lambda>=1` by Brown–Resnick Slepian comparison. Hence, wherever logarithmic derivatives exist, `0 <= zeta d_zeta log H <= chi d_chi log H`. Along the physical threshold trajectory at fixed `kappa`, where `chi proportional u` and `zeta proportional 1/u`, `H` is therefore nondecreasing with `u`. The matched tangent hazard obeys the explicit uniform bound `h_tan/N_tan <= phi(u)/Q(u)-1/u`, independent of the crossover coordinates. At the operating `u~4.959`, this gives `~4.9452`, and an exact finite-strip tangent factor of `~9.89e-4` for a symmetric `delta=1e-4` buffer. This is on the correct `~1e-9` absolute scale when `N~alpha`. However, Step-36 exact cluster-strip numerics give a somewhat larger coefficient (`~5.0–5.5`), proving that the remaining discrepancy is a finite-`u` correction between the exact cluster measure and the tangent/Pickands leading model, not a positive `zeta`-elasticity effect. No novelty claim.

---

## 1. Finite-band tangent smoothing function

Recall

```math
F_\zeta(t)
=|t|\operatorname{erf}(\zeta|t|)
+\frac{e^{-\zeta^2t^2}-1}{\sqrt\pi\,\zeta},
```

and

```math
g_{\chi,\zeta}(t)
=t^2+\sqrt2\chi F_\zeta(t).
```

Step 25 proved that the corresponding generalized Pickands constant

```math
\mathcal H(\chi,\zeta)
```

is nondecreasing separately in `chi` and `zeta` by Brown–Resnick Slepian comparison.

The missing question from Step 37 was whether the two logarithmic elasticities can be compared to one another.

---

## 2. Exact differential inequality for `F_zeta`

Set

```math
s=\zeta|t|.
```

Step 25 already gives

```math
\boxed{
\partial_\zeta F_\zeta(t)
=\frac{1-e^{-s^2}}{\sqrt\pi\,\zeta^2}
\ge0.
}
```

Therefore

```math
\zeta\partial_\zeta F_\zeta(t)
=\frac{1-e^{-s^2}}{\sqrt\pi\,\zeta}.
```

To compare this with `F_zeta`, compute

```math
F_\zeta(t)-\zeta\partial_\zeta F_\zeta(t)
=
\frac1\zeta
\left[
 s\operatorname{erf}(s)
 -\frac{2(1-e^{-s^2})}{\sqrt\pi}
\right].
```

Define

```math
R(s)
=s\operatorname{erf}(s)
-\frac{2(1-e^{-s^2})}{\sqrt\pi}.
```

Then

```math
R(0)=0,
```

```math
R'(s)
=\operatorname{erf}(s)
-\frac{2s}{\sqrt\pi}e^{-s^2},
```

and

```math
\boxed{
R''(s)
=\frac{4s^2}{\sqrt\pi}e^{-s^2}
\ge0.
}
```

Since `R'(0)=0`, it follows that `R'(s)>=0` and hence `R(s)>=0` for `s>=0`.

Thus

```math
\boxed{
0\le
\zeta\partial_\zeta F_\zeta(t)
\le
F_\zeta(t)
\qquad\forall t,\zeta>0.
}
```

This inequality is exact.

---

## 3. Finite multiplicative scaling bound

Where `F_zeta(t)>0`, the previous result is

```math
0\le
\partial_{\log\zeta}\log F_\zeta(t)
\le1.
```

Integrating between `zeta` and `lambda zeta`, for any `lambda>=1`, gives

```math
\boxed{
F_{\lambda\zeta}(t)
\le
\lambda F_\zeta(t).
}
```

At `t=0` both sides vanish, so the same inequality holds trivially.

Therefore

```math
\begin{aligned}
g_{\chi,\lambda\zeta}(t)
&=t^2+\sqrt2\chi F_{\lambda\zeta}(t)\\
&\le t^2+\sqrt2\lambda\chi F_\zeta(t)\\
&=g_{\lambda\chi,\zeta}(t).
\end{aligned}
```

Hence

```math
\boxed{
g_{\chi,\lambda\zeta}(t)
\le
g_{\lambda\chi,\zeta}(t)
\quad\forall t,\lambda\ge1.
}
```

---

## 4. Brown–Resnick Slepian gives cross-ordering of `H`

The Brown–Resnick Slepian inequality orders the corresponding generalized Pickands constants whenever the stationary-increment Gaussian variograms are pointwise ordered. Therefore

```math
\boxed{
\mathcal H(\chi,\lambda\zeta)
\le
\mathcal H(\lambda\chi,\zeta),
\qquad \lambda\ge1.
}
```

This is stronger than separate coordinatewise monotonicity.

Primary comparison source: Dębicki & Hashorva, *Approximation of Supremum of Max-Stable Stationary Processes and Pickands Constants*, Brown–Resnick Slepian inequality (arXiv:1712.04243; later Journal of Theoretical Probability).

Taking one-sided logarithmic derivatives, wherever ordinary derivatives exist,

```math
\boxed{
0\le
\zeta\,\partial_\zeta\log\mathcal H
\le
\chi\,\partial_\chi\log\mathcal H.
}
```

Without assuming differentiability, the corresponding statement holds for upper/right Dini derivatives obtained from the finite `lambda` inequality.

---

## 5. Exact monotonicity along the physical threshold hyperbola

For fixed observation shape parameters and fixed physical information bandwidth `kappa`, Step 37 uses

```math
\chi(u)=A u,
\qquad
\zeta(u)=\frac{B}{u},
```

so

```math
\chi(u)\zeta(u)=AB
```

is constant.

Take `u_2=lambda u_1`, `lambda>=1`. Then

```math
\chi_2=\lambda\chi_1,
\qquad
\zeta_2=\zeta_1/\lambda.
```

Apply the cross-ordering with base point `(chi_1,zeta_1/lambda)`:

```math
\mathcal H(\chi_1,\zeta_1)
=\mathcal H(\chi_1,\lambda(\zeta_1/\lambda))
\le
\mathcal H(\lambda\chi_1,\zeta_1/\lambda).
```

Therefore

```math
\boxed{
\mathcal H(\chi(u),\zeta(u))
\text{ is nondecreasing in }u
}
```

along every fixed-`kappa` physical tangent trajectory.

This finite-difference statement does not require differentiability of `H`.

---

## 6. Explicit uniform tangent-hazard bound

The matched tangent cluster/exceedance intensity from Step 37 is

```math
N_{tan}(u)
=C\,u\,\mathcal H(\chi(u),\zeta(u))\,Q(u),
```

where

```math
C=\ell\sqrt b/\sqrt2
```

is independent of threshold.

If logarithmic derivatives exist,

```math
\frac{h_{tan}}{N_{tan}}
=\frac{\phi(u)}{Q(u)}-\frac1u
-\frac{\chi}{u}\partial_\chi\log\mathcal H
+\frac{\zeta}{u}\partial_\zeta\log\mathcal H.
```

Since

```math
\zeta\partial_\zeta\log\mathcal H
\le
\chi\partial_\chi\log\mathcal H,
```

the crossover terms are nonpositive in the hazard:

```math
\boxed{
\frac{h_{tan}(u)}{N_{tan}(u)}
\le
\frac{\phi(u)}{Q(u)}-\frac1u.
}
```

Thus the positive `zeta` elasticity can never raise the matched tangent hazard above the smooth Gaussian-peak benchmark.

At the Step-34/36 fast operating threshold

```text
u ~= 4.959,
```

```math
\frac{\phi(u)}{Q(u)}-\frac1u
\approx4.9452.
```

Equivalently,

```math
\frac{h_{tan}}{uN_{tan}}
\lesssim0.9973.
```

This multiplier is uniform in `(chi,zeta)` inside the matched tangent model.

---

## 7. Finite-strip bound without differentiating `H`

The finite-difference monotonicity of `H` gives an even cleaner threshold-strip result.

For `delta>0`, define

```math
u_-=u-\delta,
\qquad
u_+=u+\delta.
```

Because the physical tangent `H(u)` is nondecreasing,

```math
\frac{N_{tan}(u_+)}{N_{tan}(u)}
\ge
\frac{u_+}{u}\frac{Q(u_+)}{Q(u)},
```

and

```math
\frac{N_{tan}(u_-)}{N_{tan}(u)}
\le
\frac{u_-}{u}\frac{Q(u_-)}{Q(u)}.
```

Therefore the symmetric threshold-strip mass of the tangent intensity satisfies

```math
\boxed{
\frac{N_{tan}(u-\delta)-N_{tan}(u+\delta)}{N_{tan}(u)}
\le
B(u,\delta),
}
```

with the explicit Gaussian factor

```math
\boxed{
B(u,\delta)
=\frac{u-\delta}{u}\frac{Q(u-\delta)}{Q(u)}
-\frac{u+\delta}{u}\frac{Q(u+\delta)}{Q(u)}.
}
```

No derivative of `H` appears.

As `delta->0`,

```math
\frac{B(u,\delta)}{2\delta}
\to
\frac{\phi(u)}{Q(u)}-\frac1u.
```

At

```text
u ~= 4.959,
delta = 1e-4,
```

one obtains

```math
\boxed{
B(u,10^{-4})\approx9.89\times10^{-4}.
}
```

Thus if `N_tan(u)` is of order

```math
\alpha=10^{-6},
```

the symmetric tangent strip is bounded at approximately

```math
\boxed{
9.9\times10^{-10}
}
```

in absolute probability/count scale.

This independently lands on the scale inferred numerically in Step 36.

---

## 8. High-band fast threshold range

For the Step-34 fast channel at `X=7.16`, the available threshold changes only slightly over

```text
170 <= kappa_f <= infinity.
```

Representative values are

```text
kappa_f       u_f
-------------------------
170           4.958875
300           4.958948
1000          4.958980
infinity      4.958983
```

Across this full range,

```math
\frac{\phi(u)}{Q(u)}-\frac1u
\approx4.9451\text{ to }4.9452,
```

and

```math
B(u,10^{-4})\approx9.890\times10^{-4}.
```

So the matched-tangent hazard multiplier is essentially constant over the physical high-band tail.

---

## 9. NEGATIVE RESULT — this does not yet certify the exact finite-u cluster measure

Step 36 directly estimated the exact fixed-cluster strip intensity near the same threshold as roughly

```text
5.0 to 5.5 alpha per unit threshold,
```

while the tangent upper hazard coefficient from this step is only

```text
~4.9452.
```

Therefore the numerical exact cluster measure can lie above the leading matched-tangent hazard prediction at the physical finite threshold.

This is not a contradiction: `N_tan` is the leading high-threshold/tangent approximation, whereas the Step-36 `nu_a` measure is the exact finite-threshold excursion-cluster object.

**NEGATIVE RESULT / REFINEMENT:** the two-parameter generalized Pickands elasticity is **not** the source of the Step-36 coefficient being above the pure smooth/rough leading models. The remaining excess must come from the finite-`u` correction that maps the tangent extreme approximation to the exact cluster-maximum measure.

Hence the Step-37 concern about an uncontrolled positive `zeta d_zeta log H` term is resolved inside the tangent model, but the Step-34 theorem-level closure is still blocked by finite-threshold remainder control.

---

## 10. First nontrivial consequence

Variogram ordering supplies the exact cross-elasticity inequality

```math
\boxed{
0\le
\zeta\partial_\zeta\log\mathcal H
\le
\chi\partial_\chi\log\mathcal H.
}
```

Consequently the matched tangent crossover cannot increase the cluster hazard above

```math
\boxed{
\phi(u)/Q(u)-1/u.
}
```

The outstanding uncertainty has moved one layer outward:

```text
resolved:
    tangent Pickands crossover elasticity;

still open:
    finite-u correction from tangent intensity to exact cluster-max measure.
```

This is a materially narrower theorem gap.

---

## 11. What remains open

- bound the finite-threshold correction factor between the exact cluster first moment `N_a(u,q)` and the matched tangent model `N_tan(u,q)`;
- especially bound its threshold variation, e.g. if `N_a=N_tan R`, control `-d_u log R` or a finite-strip ratio without assuming differentiability;
- combine that correction bound with the Step-35 sup-norm `q` coupling tail;
- formal interval/concentration treatment of remaining numerical constants;
- extension to other task parameters and detector models;
- hardware interpretation;
- novelty.

---

## 12. Stopping point

The positive smoothing elasticity is now exactly dominated by the roughness elasticity, and the matched tangent hazard has an explicit uniform Gaussian upper multiplier. The remaining theorem gap is no longer inside `H(chi,zeta)`; it is the finite-threshold remainder between the tangent approximation and the exact physical excursion-cluster measure.

### Single natural next question

> Can the exact cluster first moment be factorized as `N_a(u,q)=N_tan(u,q) R(u,q)` with a controlled finite-threshold remainder, and can the threshold variation of `R` be bounded tightly enough at `u~5` to account for the observed `~5–10%` excess in the Step-36 strip intensity?
