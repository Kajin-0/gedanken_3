# Step 30 — Universal Brownian–Parabola / Gaussian-Mollifier Crossover Function

**Date:** 2026-08-11 20:57 EDT  
**Status:** DERIVED / NUMERICAL VALIDATION / REFINEMENT / INVALIDATED NUMERICAL INTERPRETATION / OPEN. Step 29 identified the correct double-scaling coordinate `mu = sqrt(2) zeta chi^(1/3)`. This step eliminates the full detector process from the small-`chi` crossover and derives a universal canonical function from Brownian motion minus a parabola. A continuum-extrapolated common-noise simulation computes that function directly and reproduces independently refined full-field fast-channel Dieker–Yakir gaps at the percent level. The previously reported **raw** Step-27 tiny-`chi` fast points are shown to be biased low by rough-maximum grid discretization; the Step-29 scaling structure survives, but those raw points must not be treated as continuum ground truth. The universal crossover also supplies a continuous fast-channel bridge into the Step-28 Bessel tail and refines the asymptotic fast `C_H` coefficient. No finite certified onset bandwidth and no novelty claim.

---

## 1. Question

Step 29 proposed the joint small-`chi` / large-bandwidth form

```math
H_{mix}(\chi)-H(\chi,\zeta)
=\chi^{2/3}\,\mathcal F(\mu)+o(\chi^{2/3}),
```

with

```math
\mu=\sqrt2\,\zeta\chi^{1/3}.
```

Can `F(mu)` be computed without simulating the full generalized-Pickands detector field?

The answer is **yes**.

---

## 2. Canonical Brownian–parabola reduction

At the rough endpoint,

```math
W_{\chi,\infty}(t)
=\sqrt2 Zt-t^2
+2^{3/4}\sqrt\chi\,B(t)
-\sqrt2\chi|t|.
```

The smooth quadratic maximum is at

```math
t_0=Z/\sqrt2.
```

Step 29 found the natural local width and height

```math
h_\chi=\sqrt2\chi^{1/3},
\qquad
m_\chi=h_\chi^2=2\chi^{2/3}.
```

Write

```math
t=t_0+h_\chi s.
```

Away from the measure-small event that `t_0` lies within `O(h_chi)` of the `|t|` cusp, Brownian scaling gives

```math
\boxed{
\frac{W_{\chi,\infty}(t_0+h_\chi s)-W_{\chi,\infty}(t_0)}
{m_\chi}
\Longrightarrow
Y_\infty(s)=B(s)-s^2.
}
```

The Gaussian derivative smoothing multiplier

```math
e^{-\omega^2/(8\zeta^2)}
```

becomes, on the `s` coordinate,

```math
\boxed{
e^{-q^2/(8\mu^2)}}
```

with

```math
\mu=\zeta h_\chi.
```

Let `B_mu` be the Gaussian-smoothed Brownian process obtained by filtering the white derivative of `B` with this multiplier and integrating from zero. Define

```math
Y_\mu(s)=B_\mu(s)-s^2.
```

Then the canonical rough and smoothed maxima are

```math
M_\infty=\sup_s Y_\infty(s),
\qquad
M_\mu=\sup_s Y_\mu(s).
```

---

## 3. Universal crossover formula

For the pure quadratic Brown–Resnick spectral path

```math
W_0(t)=\sqrt2 Zt-t^2,
```

the Dieker–Yakir ratio is path-independent:

```math
\Psi_0
=\frac{e^{\sup W_0}}{\int e^{W_0(t)}dt}
=\frac1{\sqrt\pi}.
```

In the Step-29 joint scaling, the maximum-height difference is `O(chi^(2/3))`. The integrated denominator difference produced by the high-pass residual is lower order under the same localization/moment conditions used in Step 28. Therefore the leading generalized-Pickands gap is

```math
H_{mix}(\chi)-H(\chi,\zeta)
=\frac1{\sqrt\pi}\,m_\chi\,
E[M_\infty-M_\mu]
+o(\chi^{2/3}).
```

Since `m_chi=2 chi^(2/3)`, the universal function is

```math
\boxed{
\mathcal F(\mu)
=\frac{2}{\sqrt\pi}
E[M_\infty-M_\mu].
}
```

This contains no detector-specific parameter.

**DERIVED / CONDITIONAL:** under the same double-scaling localization and uniform-integrability conditions already required by Steps 28–29, the small-`chi` finite-band crossover reduces to a single canonical Brownian-minus-parabola maximum-loss function.

---

## 4. Endpoint and Bessel-tail limits

### Broad-smoothing endpoint

As

```math
\mu\to0,
```

the smoothed derivative vanishes on the canonical `O(1)` scale, so

```math
M_\mu\to0.
```

Hence

```math
\boxed{
\mathcal F(0)
=\frac{2}{\sqrt\pi}E[M_\infty].
}
```

A continuum-extrapolated Brownian-parabola simulation gives approximately

```text
F(0) ~ 0.892.
```

### Narrow-smoothing / Bessel endpoint

For

```math
\mu\to\infty,
```

the smoothing probes only the Brownian extremum neighborhood. Step 28 therefore gives

```math
E[M_\infty-M_\mu]
\sim \frac{E[\mathcal M_K]}{\sqrt\mu},
```

with the Gaussian-kernel two-sided-BES(3) functional `M_K`.

Thus

```math
\boxed{
\mathcal F(\mu)
\sim \frac{A_K}{\sqrt\mu},
\qquad
A_K=\frac{2}{\sqrt\pi}E[\mathcal M_K].
}
```

Using the Step-28 unweighted canonical BES diagnostic

```text
E[M_K] ~ 0.87
```

gives

```text
A_K ~ 0.98.
```

Unlike the finite-`chi` Step-28 coefficient, there is no unknown Dieker–Yakir weighting in this **small-chi universal limit** because the leading quadratic ratio is the deterministic `1/sqrt(pi)`.

---

## 5. Numerical evaluation and the rough-grid issue

The canonical function is estimated from one common white-noise realization for `B_infinity` and `B_mu`.

A critical numerical fact is that the rough maximum

```math
\sup_s[B(s)-s^2]
```

has a leading discretization error of Brownian order

```math
O(\sqrt{\Delta s}).
```

Therefore simply decreasing `Delta s` and reading the last value is inefficient and biases the gap downward, because the rough endpoint maximum is under-resolved more strongly than the smoothed maximum.

The Step-30 calculator evaluates each `mu` on nested grids and extrapolates

```math
D(\Delta s)
=E[M_\infty^{\Delta s}-M_\mu^{\Delta s}]
=D_0+c\sqrt{\Delta s}+... .
```

This continuum extrapolation is essential for the tiny-`chi` fast channel.

---

## 6. Universal crossover table

Representative continuum-extrapolated results are

```text
mu        F(mu)       sqrt(mu) F(mu)
-------------------------------------
0         ~0.892       --
0.5       ~0.806       ~0.570
1         ~0.729       ~0.729
2         ~0.597       ~0.844
3         ~0.512       ~0.886
5         ~0.410       ~0.917
10        ~0.297       ~0.939
20        ~0.213       ~0.955
infinity   --          ~A_K ~0.98
```

The function decreases smoothly from the broad-smoothing endpoint while

```math
\sqrt\mu\,\mathcal F(\mu)
```

approaches the Bessel constant from below.

**NUMERICAL VALIDATION:** the nested-grid extrapolation is stable between three- and four-grid fits in the tested range. The quoted values are crossover-function estimates, not exact analytic constants.

---

## 7. Full-field validation at the actual fast endpoint

The Step-27 raw fast values used

```text
chi_f ~ 1.1395e-4
zeta = 20, 40, 80.
```

Because `h_chi` is small, the original default time spacings were coarse on the Brownian-parabola peak scale. Recompute the **full** paired Dieker–Yakir gaps on nested time grids and extrapolate linearly in `sqrt(dt)`.

This gives

```text
zeta      mu       F_full,extrap     F_canonical
-------------------------------------------------
20       1.371         ~0.675           ~0.68
40       2.743         ~0.531           ~0.53
80       5.485         ~0.394           ~0.40
```

Agreement is at approximately the percent level.

By contrast, the raw Step-27/29 fast values before continuum extrapolation were approximately

```text
0.551, 0.438, 0.324.
```

**INVALIDATED NUMERICAL INTERPRETATION:** those raw fast values are not continuum estimates of the crossover function. Their low values are primarily rough-maximum grid bias. Step 29's identification of `mu` remains valid; its use of the raw fast points as evidence for the shape of the continuum crossover is refined by the present calculation.

The slow-channel Step-27 grid was already much finer relative to its larger `h_chi`, so the same bias was substantially smaller there.

---

## 8. Continuous bridge for the fast detector

For the `r=2` endpoint trajectory, Step 29 found

```math
\mu_f\approx0.009776\,\kappa_f.
```

Hence the universal curve directly bridges the difficult fast channel:

```text
kappa_f     mu_f       F(mu_f) approximately
---------------------------------------------
100         0.98       0.73
200         1.96       0.60
300         2.93       0.52
500         4.89       0.42
1000        9.78       0.30
2000       19.55       0.22
```

For larger `mu`, use

```math
\mathcal F(\mu)\sim A_K/\sqrt\mu.
```

Thus the crossover can be propagated continuously without re-running the full detector Gaussian process at every bandwidth.

---

## 9. Effective `C_H` bridge and refinement of Step 26

Define the finite-band effective coefficient

```math
C_{H,eff}(\chi,\mu)
=\sqrt\zeta\,[H_{mix}(\chi)-H(\chi,\zeta)].
```

Using

```math
\mu=\sqrt2\zeta\chi^{1/3}
```

and the universal form gives

```math
\boxed{
C_{H,eff}
=2^{-1/4}\sqrt\chi\;
\sqrt\mu\,\mathcal F(\mu).
}
```

Therefore

```math
\boxed{
C_H(\chi)
\to
2^{-1/4}A_K\sqrt\chi
}
```

in the large-`mu` tail.

For the fast endpoint

```text
chi_f ~ 1.1395e-4,
```

this gives

```text
C_H,fast(infinity) ~ 0.0088
```

using `A_K~0.98`.

The Step-26 value

```text
C_H,fast ~0.0061
```

was therefore indeed a pre-asymptotic/grid-affected effective coefficient.

If the same Step-26 finite-`u` tangent surrogate is recomputed with the universal-tail fast coefficient while leaving its other inputs fixed, the illustrative coupled coefficient moves from roughly

```text
C_Lambda ~0.020
```

to

```text
C_Lambda ~0.032.
```

**REFINEMENT:** this strengthens the positive high-band boundary coefficient sign but is still only a surrogate scale estimate, not a precision prediction and not a finite-`K` certificate.

---

## 10. First nontrivial consequence

The difficult small-`chi` fast-channel smoothing problem does not require a separate generalized-Pickands Monte Carlo at every bandwidth.

It reduces to the reusable one-dimensional crossover

```math
\boxed{
\mathcal F(\mu)
=\frac{2}{\sqrt\pi}
E\left[
\sup_s(B(s)-s^2)
-
\sup_s(B_\mu(s)-s^2)
\right].
}
```

This function bridges continuously from broad smoothing to the Bessel tail and reproduces the continuum-extrapolated full fast-channel calculation.

That is the first point at which the small-`chi` high-band crossover has been separated cleanly from the full detector simulation.

---

## 11. What remains open

- publication-grade proof of the double-scaling limit and denominator remainder;
- certified deterministic or very-high-precision evaluation of `F(mu)`;
- rigorous monotonicity / error bounds for the numerical crossover interpolation;
- insertion of the universal bridge into the finite-`r` physical boundary equation;
- closure of any bounded re-entrant pocket;
- finite certified onset bandwidth;
- hardware interpretation;
- novelty.

---

## 12. Stopping point

The universal crossover function is now directly computable and validated against the refined full fast-channel field. The remaining detector-level question is to propagate this universal bridge through the coupled fast/slow boundary rather than using either raw finite-band Rice/Palm points or a prematurely asymptotic constant.

### Single natural next question

> If the universal `F(mu)` bridge is inserted into the coupled finite-`r` boundary equation, does the corrected boundary remain monotone on the entire high-band interval from the existing Palm map into the rough endpoint, thereby eliminating the last plausible bounded re-entrant pocket without requiring full-process Monte Carlo at every bandwidth?
