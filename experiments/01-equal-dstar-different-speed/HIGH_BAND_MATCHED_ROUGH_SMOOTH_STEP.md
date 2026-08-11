# Step 23 — Matched Rough/Smooth High-Band Limit and Occupation-Time Rare Events

**Date:** 2026-08-11 18:54 EDT  
**Status:** DERIVED / ASYMPTOTIC / NUMERICAL VALIDATION / REFINEMENT / OPEN. The finite-`r` `kappa_f -> infinity` problem is reduced to a matched rough/smooth local Gaussian field governed by one dimensionless transition parameter. A generalized Pickands constant gives the correct high-threshold bridge between the finite-hard-window cusp and the smooth full-template limit. Because the present task operates at `u ~ 5`, the leading high-threshold expansion alone is not accurate enough at the percent level, so an exact occupation-time rare-event identity is introduced that remains valid for the nondifferentiable rough process. Applied directly at `kappa_f = infinity`, it places the `r=2` boundary near `Lambda ~ 0.905`, above the old `Lambda=0.895` slice. Thus the high-band asymptotic state of that slice is fast-preferred; a different bounded re-entrant pocket at some untested finite bandwidth is not rigorously excluded. No novelty claim.

---

## 1. Question

Step 22 mapped the Palm-corrected finite-`r` boundary through `kappa_f ~ 200`, where the boundary stayed near

```text
Lambda_cross ~ 0.91.
```

The unresolved issue was the true `kappa_f -> infinity` limit. For every finite hard window, infinite information bandwidth restores the covariance cusp, while sending the integration duration to infinity first restores the smooth full template. The two limits do not commute.

Question:

> Can the rough finite-window excursion law and smooth full-template law be matched into one high-band asymptotic description, and what does that imply for the `Lambda=0.895` slice and the limiting boundary?

---

## 2. Exact hard-window covariance

For

```math
h_x(v)=v e^{-v}1_{[0,x]}(v),
```

the unnormalized covariance for `0 <= y < x` is

```math
C_x(y)
=\frac14\Big[(1+y)e^{-y}
-e^{-2x+y}(2x^2-2xy+2x-y+1)\Big].
```

The energy is

```math
E_x=C_x(0)=\frac14\eta(x),
```

with

```math
\eta(x)=1-e^{-2x}(1+2x+2x^2).
```

Hence the exact normalized covariance is

```math
\boxed{
R_x(y)=
\frac{(1+y)e^{-y}
-e^{-2x+y}(2x^2-2xy+2x-y+1)}
{\eta(x)},
\qquad 0\le y<x.
}
```

For `y >= x`, the windows do not overlap and `R_x(y)=0`.

---

## 3. Mixed local expansion

Expanding from the right at zero gives

```math
\boxed{
R_x(y)
=1-a_x|y|-\frac{b_x}{2}y^2+O(|y|^3),
}
```

where the cusp coefficient is the Step-13 result

```math
\boxed{
a_x=\frac{2x^2e^{-2x}}{\eta(x)},
}
```

and the quadratic coefficient is

```math
\boxed{
b_x
=\frac{1+e^{-2x}(2x^2-2x-1)}{\eta(x)}.
}
```

As `x -> infinity`,

```math
a_x\sim2x^2e^{-2x}\to0,
\qquad
b_x\to1,
```

and for every fixed nonzero lag the covariance approaches the smooth full-template law

```math
R_\infty(y)=(1+|y|)e^{-|y|}.
```

Thus the cusp survives mathematically at every finite `x`, but its coefficient becomes exponentially small.

---

## 4. Distinguished rough/smooth matching parameter

Let `u` be the high decision threshold. On the smooth local-extreme scale

```math
q(u)=\frac{\sqrt2}{u\sqrt{b_x}},
```

one obtains

```math
u^2\left[1-R_x(q(u)t)\right]
\to
t^2+\sqrt2\,\chi_x|t|,
```

with the single dimensionless transition parameter

```math
\boxed{
\chi_x=\frac{a_xu}{\sqrt{b_x}}.
}
```

This is the missing matching coordinate.

Interpretation:

```text
chi_x << 1:
    distinct high excursions are controlled mainly by the smooth quadratic core;
    the cusp creates microscopic recrossings inside those excursions.

chi_x >> 1:
    the rough linear cusp controls the excursion geometry.
```

The mathematical statement `a_x > 0` is therefore not enough to decide the operational high-threshold geometry at finite `u`.

For the present `r=2` calibration around the high-band common decision times `X ~ 6.5–8`, representative values are

```text
X       chi_fast          chi_slow
6.5     ~9.5e-4           ~0.155
7.0     ~4.0e-4           ~0.110
7.5     ~1.7e-4           ~0.0765
8.0     ~7.1e-5           ~0.0529
```

So the fast channel is extremely close to the smooth-cluster regime, while the shorter slow window retains a much larger rough correction.

---

## 5. Generalized Pickands bridge

The matched tangent process can be represented by a centered Gaussian process with stationary increments and variance

```math
\boxed{
\operatorname{Var}\eta_\chi(t)
=t^2+\sqrt2\,\chi|t|.
}
```

Equivalently one may write

```math
\eta_\chi(t)
=Zt+2^{1/4}\sqrt\chi\,B(t),
```

where `Z ~ N(0,1)` and `B` is standard two-sided Brownian motion, independent of `Z`.

Define the corresponding generalized Pickands constant

```math
\boxed{
\mathcal H_{mix}(\chi)
=\lim_{T\to\infty}
\frac1T
E\exp\!\left[
\sup_{0\le t\le T}
\left(
\sqrt2\eta_\chi(t)
-\operatorname{Var}\eta_\chi(t)
\right)
\right].
}
```

The matched high-threshold excursion law has the form

```math
\boxed{
P_{FA}(u)
\sim
Q(u)
+\ell\,
\frac{u\sqrt{b_x}}{\sqrt2}
\mathcal H_{mix}(\chi_x)
Q(u).
}
```

The two endpoint limits are correct automatically:

```math
\mathcal H_{mix}(0)=\frac1{\sqrt\pi}
```

recovers the smooth `alpha=2` Pickands/Rice coefficient, while

```math
\mathcal H_{mix}(\chi)
\sim\sqrt2\,\chi
\qquad(\chi\to\infty)
```

recovers the rough `alpha=1` law

```math
P_{FA}-Q(u)
\sim \ell a_x u^2 Q(u).
```

**DERIVED / ASYMPTOTIC:** the rough and smooth formulas are not competing unrelated approximations. They are the two limits of one mixed generalized-Pickands problem parameterized by `chi_x`.

---

## 6. Why the leading asymptotic alone is not sufficient here

The operating thresholds are only about

```text
u ~ 4.9–5.0.
```

At that level,

```math
\frac{\phi(u)}{uQ(u)}-1
=O(u^{-2})
```

is still a few percent.

That is larger than the `~1%` displacement needed to decide whether the limiting boundary lies above or below `Lambda=0.895`.

A raw leading generalized-Pickands calculation therefore cannot be used as a percent-level finite-`alpha` boundary prediction without an additional finite-threshold anchor.

**REJECTED SHORTCUT:** do not settle the finite-`alpha` `kappa=infinity` boundary by inserting only the leading high-threshold Pickands term.

---

## 7. Exact occupation-time rare-event identity for the rough process

The rough process has infinitely many microscopic level recrossings, so an upcrossing count is the wrong exact object at `kappa=infinity`.

Instead define the excursion occupation time

```math
\boxed{
V_u=\int_0^\ell 1_{\{z(t)>u\}}\,dt.
}
```

Construct a proposal by:

1. drawing `T` uniformly on `[0,ell]`;
2. drawing the Gaussian path conditional on `z(T)>u`.

The proposal density relative to the original stationary path measure is

```math
\frac{dQ_{occ}}{dP}
=\frac{V_u}{\ell Q(u)}.
```

Therefore

```math
\boxed{
P\!\left(\sup_{0\le t\le\ell}z(t)>u\right)
=\ell Q(u)
E_{occ}\!\left[\frac1{V_u}\right].
}
```

This identity is exact for a continuous process and does **not** require differentiability or a finite number of crossings.

**DERIVED:** occupation-time importance sampling is the natural exact rare-event continuation of the Step-16 Palm method into the rough hard-window limit.

---

## 8. Direct `kappa=infinity` boundary calculation

Use the same fixed-physics finite-`r` calibration as Steps 20–22:

```text
r        = 2
rho_full = 6.2407571
alpha    = 1e-6
beta     = 0.90.
```

At `kappa=infinity`, the accessible finite-duration SNR is exactly

```math
\boxed{
\rho(x)=\rho_{full}\sqrt{\eta(x)}.
}
```

A matched search of the rough-limit problem places the common decision point near

```text
X = T/tau_f ~ 7.75
Lambda = L/tau_f ~ 0.905.
```

At the representative candidate

```text
X      = 7.7528
Lambda = 0.90513
```

a `40000`-path occupation-time importance calculation with timing spacing about `0.002` gives

```text
fast:
    P_FA / alpha = 1.0049 +/- 0.0080

slow:
    P_FA / alpha = 0.9954 +/- 0.0094
```

at the same physical decision time.

A separate factor-of-two local spacing check (`~0.0025 -> ~0.00125`) was statistically compatible with the same equality region.

A conservative summary is

```math
\boxed{
\Lambda_{\times}^{kappa=\infty}
\approx0.905\pm0.004
}
```

for this particular `r=2`, `(rho_full,alpha,beta)` calibration.

This value is also constrained from above by the fast detector's full-template Palm feasibility edge (`~0.909`), which the finite-window fast detector cannot exceed.

---

## 9. Consequence for the old `Lambda=0.895` slice

The limiting boundary satisfies

```math
\Lambda_{\times}^{kappa=\infty}
>0.895
```

within the numerical uncertainty above.

Therefore the `Lambda=0.895` task remains on the **fast-preferred** side in the infinite-band hard-window limit.

Together with the direct Palm checks at

```text
kappa_f = 130, 160, 300,
```

this gives the corrected high-band picture

```text
Lambda = 0.895:
    fast preferred at all directly checked high bandwidths
    and fast preferred again in the kappa=infinity limit.
```

**REFINEMENT:** the Step-20 second reversal does not reappear asymptotically at infinite bandwidth.

**OPEN:** this does not constitute a proof that no bounded re-entrant slow-preferred pocket exists somewhere between the largest finite-band check and the asymptotic regime. Such a pocket would have to disappear again before `kappa=infinity`; no evidence for one has been found.

---

## 10. High-band slow-preferred region still survives

The asymptotic boundary near

```text
Lambda ~ 0.905
```

is above the old `0.895` slice but finite.

Therefore tasks with larger timing uncertainty still lie on the slow-preferred side of the limiting boundary.

This sharpens Step 22:

```text
finite high bandwidth (~60–200):
    Lambda_cross ~0.91

infinite-band hard-window limit:
    Lambda_cross ~0.905
```

within present numerical precision.

So the high-band slow-preferred region survives all the way to the rough limit; the boundary is lifted relative to the invalid Rice result, not eliminated.

---

## 11. What is established

### DERIVED / ASYMPTOTIC

- exact finite-hard-window covariance in closed form;
- mixed local coefficients `a_x` and `b_x`;
- distinguished rough/smooth parameter `chi_x=a_x u/sqrt(b_x)`;
- matched stationary-increment tangent variance `t^2 + sqrt(2) chi |t|`;
- generalized-Pickands bridge between smooth and rough high-threshold excursion laws;
- exact occupation-time importance identity valid in the nondifferentiable rough limit.

### NUMERICAL VALIDATION / CONDITIONAL

- for the Step-20 `r=2` calibration, the direct rough-limit boundary is approximately `Lambda~0.905 +/-0.004`;
- the old `Lambda=0.895` task is fast-preferred in the `kappa=infinity` limit;
- high-band slow-preferred tasks still exist for larger `Lambda`.

### OPEN

- rigorous monotonic convergence of the finite-`kappa` Palm boundary to the rough-limit boundary;
- a proof excluding a bounded re-entrant pocket at some untested very high finite bandwidth;
- a closed-form expression for `H_mix(chi)`;
- controlled finite-`u` correction to the generalized-Pickands law sufficient to replace occupation-time Monte Carlo at `alpha=1e-6`;
- arbitrary `r`, `rho_full`, `alpha`, `beta` classification;
- hardware interpretation of the Gaussian information-band parameter;
- novelty.

---

## 12. First nontrivial consequence

**REFINEMENT:** the noncommuting rough/full-template limits can be organized by a single transition coordinate

```math
\boxed{\chi_x=a_xu/\sqrt{b_x}}.
```

The infinite-band finite-window process may be mathematically nondifferentiable while its **distinct high excursions** remain smooth-core dominated when `chi_x << 1`; the rough cusp then manifests primarily as microscopic recrossing inside an excursion.

That resolves the conceptual conflict behind Steps 17–22 and explains why finite-window Rice diverged while the exact excursion probability remained well behaved.

---

## 13. Stopping point

The `kappa_f -> infinity` finite-`r` boundary is now structurally matched and numerically anchored without relying on upcrossing counts.

### Single natural next question

> Can the mixed generalized Pickands constant `H_mix(chi)` and its finite-threshold correction be computed accurately enough to turn the Step-23 matched boundary into a deterministic analytic/numerical formula, and thereby prove or exclude any bounded high-band re-entrant preference pocket without further full-process Monte Carlo?
