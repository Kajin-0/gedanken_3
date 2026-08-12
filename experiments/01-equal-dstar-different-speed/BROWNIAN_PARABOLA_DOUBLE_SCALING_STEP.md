# Step 29 — Brownian–Parabola Double Scaling: the Uniform Remainder Is Controlled by `mu`, Not `zeta` Alone

**Date:** 2026-08-11 20:40 EDT  
**Status:** DERIVED / REFINEMENT / NUMERICAL COLLAPSE / REJECTED SHORTCUT / OPEN. Step 28 identified a positive fixed-`chi`, `zeta -> infinity` Gaussian-mollifier correction `H_mix(chi)-H(chi,zeta) ~ C_H(chi)/sqrt(zeta)`. This step asks whether that expansion can be made quantitatively uniform over the detector-relevant `chi` interval. The answer is that a uniform expansion in `zeta` alone is the wrong asymptotic organization. For small `chi`, the mixed rough/smooth endpoint develops a Brownian-minus-parabola scale of width `h_chi = sqrt(2) chi^(1/3)` and height `h_chi^2 = 2 chi^(2/3)`. Gaussian smoothing of width `~1/zeta` is therefore controlled by the combined variable `mu = zeta h_chi = sqrt(2) zeta chi^(1/3)`. Step-27 paired data collapse strongly when expressed as `Delta H / chi^(2/3)` versus `mu`. The slow endpoint is already in the large-`mu` Bessel regime over the tested high-band range, while the tiny-`chi` fast endpoint is still in crossover through the existing `kappa_f <= 300` Palm checks. This refines, but does not invalidate, the eventual-negative-slope result: the Step-26 fast `C_H ~ 0.006` number is a pre-asymptotic effective coefficient, not the true fixed-`chi` `zeta -> infinity` coefficient. No finite certified onset bandwidth and no novelty claim.

---

## 1. Why the Step-28 expansion is singular as `chi -> 0`

At the rough endpoint, the Step-25 tangent spectral field can be written

```math
W_{\chi,\infty}(t)
=\sqrt2 Z t-t^2
+2^{3/4}\sqrt\chi\,B(t)
-\sqrt2\chi|t|,
```

where `Z ~ N(0,1)` is independent of a two-sided standard Brownian motion `B`.

Define

```math
\boxed{\sigma_\chi=2^{3/4}\sqrt\chi.}
```

Ignoring the Brownian perturbation, the smooth quadratic part has its maximum at

```math
t_0=Z/\sqrt2.
```

Write

```math
t=t_0+h s.
```

The two leading changes around `t_0` are

```text
Brownian fluctuation:    sigma_chi sqrt(h)
parabolic drop:          h^2.
```

Balancing them gives

```math
\sigma_\chi\sqrt h\sim h^2,
```

hence

```math
\boxed{
h_\chi=\sigma_\chi^{2/3}
=\sqrt2\,\chi^{1/3}.
}
```

The associated height scale is

```math
\boxed{
m_\chi=h_\chi^2=2\chi^{2/3}.}
```

Indeed, Brownian scaling gives

```math
\sigma_\chi
[B(t_0+h_\chi s)-B(t_0)]
\overset d=
\sigma_\chi\sqrt{h_\chi}\,B(s)
=h_\chi^2 B(s),
```

while

```math
-(t-t_0)^2=-h_\chi^2s^2.
```

Thus, away from the measure-small event that the smooth maximum lies within `O(h_chi)` of the `|t|` cusp at zero,

```math
\boxed{
\frac{W_{\chi,\infty}(t_0+h_\chi s)-W_{\chi,\infty}(t_0)}
{h_\chi^2}
\Rightarrow
B(s)-s^2
}
```

as `chi -> 0`, up to lower-order terms.

The maximum of Brownian motion with negative parabolic drift is a classical separate extremal object; the present scaling follows directly from the field above and is not imported as an assumption.

---

## 2. The correct mollifier coordinate

Step 27 showed that Gaussian information smoothing uses

```math
K_\zeta(t)
=\frac{\sqrt2\zeta}{\sqrt\pi}e^{-2\zeta^2t^2},
```

whose width is `O(1/zeta)`.

On the Brownian–parabola coordinate `t=t_0+h_chi s`, the kernel becomes

```math
h_\chi K_\zeta(h_\chi s)
=
\frac{\sqrt2\mu}{\sqrt\pi}e^{-2\mu^2s^2},
```

with

```math
\boxed{
\mu
=\zeta h_\chi
=\sqrt2\,\zeta\chi^{1/3}.
}
```

Therefore the ratio

```text
Brownian-parabola peak width / Gaussian smoothing width
```

is controlled by `mu`, not by `zeta` alone.

### Interpretation

```text
mu << 1   : smoothing is broad on the natural rough/smooth peak scale;
mu ~ 1    : crossover regime;
mu >> 1   : Gaussian smoothing resolves only a small neighborhood of the rough maximum, so the Step-28 two-sided-Bessel continuity correction becomes appropriate.
```

**REJECTED SHORTCUT:** `zeta >> 1` alone is not sufficient to claim that the fixed-`chi` Bessel asymptotic is quantitatively mature uniformly over a range containing very small `chi`.

---

## 3. Double-scaling form of the Pickands correction

The local height scale is `m_chi = 2 chi^(2/3)`. In the joint limit

```text
chi -> 0,
zeta -> infinity,
mu = sqrt(2) zeta chi^(1/3) fixed,
```

the natural form is therefore

```math
\boxed{
H_{mix}(\chi)-H(\chi,\zeta)
=\chi^{2/3}\,\mathcal F(\mu)
+o(\chi^{2/3}),
}
```

under the same localization/uniform-integrability type conditions used in Step 28.

The exact normalization of `F` absorbs the factor `2` from `m_chi` and the limiting Dieker–Yakir weight.

For `mu -> infinity`, Step 28 must be recovered. Since

```math
\chi^{2/3}\mu^{-1/2}
=2^{-1/4}\frac{\sqrt\chi}{\sqrt\zeta},
```

the large-`mu` crossover necessarily has

```math
\boxed{
\mathcal F(\mu)
\sim A_K\mu^{-1/2},
\qquad \mu\to\infty,
}
```

and hence

```math
C_H(\chi)
\sim 2^{-1/4}A_K\sqrt\chi
```

as `chi -> 0`.

This is consistent with the Step-28 coefficient formula, which already contains an explicit prefactor `sqrt(chi)`.

---

## 4. Numerical collapse of the Step-27 paired data

Let

```math
\Delta H(\chi,\zeta)
=H_{mix}(\chi)-H(\chi,\zeta).
```

Step 27 reported the paired quantity

```math
G=\sqrt\zeta\,\Delta H.
```

Convert those same data to

```math
\mu=\sqrt2\zeta\chi^{1/3},
\qquad
F_{emp}=\Delta H/\chi^{2/3}.
```

The result is

```text
chi ~1.1395e-4  (fast endpoint)
---------------------------------------------------------
zeta      mu        F_emp       sqrt(mu) F_emp
20        1.371     0.5508      0.6450
40        2.743     0.4379      0.7252
80        5.485     0.3239      0.7586

chi ~0.06455  (slow endpoint)
---------------------------------------------------------
zeta      mu        F_emp       sqrt(mu) F_emp
20       11.346     0.2831      0.9535
40       22.692     0.2036      0.9699
80       45.383     0.1470      0.9905

chi =0.1
---------------------------------------------------------
zeta      mu        F_emp       sqrt(mu) F_emp
20       13.128     0.2861      1.0368
40       26.257     0.2026      1.0379
80       52.514     0.1444      1.0466
```

Two features are difficult to see in the raw `sqrt(zeta) Delta H` table but become clear here:

1. the slow-endpoint and `chi=0.1` data nearly collapse onto the same curve for comparable `mu`;
2. once `mu` reaches roughly `10` or larger, `sqrt(mu) F_emp` is already close to a constant of order one, whereas the fast endpoint at `mu=1.4–5.5` is visibly still approaching that regime.

**NUMERICAL COLLAPSE / NUMERICAL ASYMPTOTIC:** the paired data strongly support the Brownian–parabola double-scaling organization and explain the different convergence rates observed at the fast and slow endpoint values.

---

## 5. Independent small-`chi` consistency check from `H_mix`

The same Brownian–parabola scaling predicts that the *rough-endpoint* departure from the pure quadratic value

```math
H_0=1/\sqrt\pi
```

should naturally be `O(chi^(2/3))` for small `chi`.

Using the Step-25/26 endpoint values:

```text
chi             H_mix-H_0       chi^(2/3)       ratio
------------------------------------------------------
1.1395e-4       0.001810         0.002350        0.770
0.06455         0.14911          0.16091         0.927
0.1             0.20279          0.21544         0.941
```

The scaling is consistent across nearly three orders of magnitude in `chi`.

This is not used as a proof of a universal constant; it is an independent numerical check that the `chi^(1/3)` width / `chi^(2/3)` height scaling is the right singular organization.

---

## 6. Consequence for the actual `r=2` physical bandwidth sweep

At the Step-26 rough-endpoint equality trajectory,

```text
chi_f ~ 1.1395e-4
chi_s ~ 0.06455
u_f   ~ 4.9591
u_s   ~ 4.9061
b_f   ~ 1.00005
b_s   ~ 1.02666
r     = 2.
```

Since

```math
\zeta_i
=\frac{\kappa_i}{\sqrt2u_i\sqrt{b_i}},
```

the double-scaling coordinate can be written especially simply as

```math
\boxed{
\mu_i
=\frac{\kappa_i\chi_i^{1/3}}
{u_i\sqrt{b_i}}.
}
```

Numerically,

```math
\boxed{
\mu_f\approx0.009776\,\kappa_f,
\qquad
\mu_s\approx0.16139\,\kappa_f.
}
```

Therefore

```text
kappa_f      mu_f        mu_s
--------------------------------
100          0.978       16.1
200          1.96        32.3
300          2.93        48.4
1000         9.78       161
10000       97.8       1614
```

This has an immediate interpretation:

- the slow detector is already well into the large-`mu` Brownian/Bessel smoothing regime throughout the high-band Palm map;
- the fast detector is still in the Brownian–parabola crossover at `kappa_f=100–300` and only begins to reach `mu_f~10` near `kappa_f~1.0e3`;
- a very clean `mu_f~100` asymptotic regime would not occur until `kappa_f~1.0e4` for this calibration.

These are dimensionless model bandwidths, not hardware recommendations.

---

## 7. Refinement of Step 26

Step 26 used an effective fast-channel value near

```text
C_H,fast ~0.006
```

from paired runs at `zeta=20–80`.

The present scaling shows that those fast runs had only

```text
mu_f ~1.37–5.49.
```

They were therefore **pre-asymptotic crossover estimates**, not clean measurements of the fixed-`chi`, `zeta -> infinity` coefficient.

This does **not** invalidate the Step-26 eventual sign argument. For every fixed positive `chi_f`, `mu_f -> infinity` as `kappa_f -> infinity`, so the Bessel asymptotic is still the correct endpoint law.

It does refine the numerical coefficient:

```text
- the previously quoted C_Lambda ~2e-2 should remain a sign/scale diagnostic, not an asymptotic precision estimate;
- the true fast-channel C_H is expected to be larger than the `zeta<=80` effective value because the normalized fast gap is still rising toward its large-mu plateau;
- this strengthens rather than weakens the previously found positive C_Lambda sign, but delays the bandwidth at which the leading asymptotic can be expected to be quantitatively accurate.
```

**REFINEMENT:** Step 26's eventual negative derivative remains the surviving asymptotic conclusion under the Step-28 assumptions; only the interpretation of the fast finite-`zeta` coefficient as already asymptotic is rejected.

---

## 8. What this says about a uniform remainder

The Step-28 leading maximum correction is

```math
O\!\left(\frac{\sqrt\chi}{\sqrt\zeta}\right).
```

On the Brownian–parabola scale, the first smooth-background correction over one smoothing width is naturally

```math
O\!\left(\frac{\chi^{1/3}}{\zeta}\right).
```

Their ratio is

```math
\boxed{
\frac{\chi^{1/3}/\zeta}
{\sqrt\chi/\sqrt\zeta}
=\frac1{\sqrt{\zeta\chi^{1/3}}}
=O(\mu^{-1/2}).
}
```

Thus the natural relative remainder parameter is `mu^-1/2`.

A quantitative remainder theorem should therefore be sought in a form such as

```math
\boxed{
H_{mix}(\chi)-H(\chi,\zeta)
=\chi^{2/3}\left[
\mathcal F(\mu)+R(\chi,\mu)
\right],
}
```

with control uniform in `mu`, followed by the large-`mu` expansion

```math
\mathcal F(\mu)
=A_K\mu^{-1/2}+O(\mu^{-1}).
```

Trying instead to prove a remainder uniform in raw `zeta` while ignoring `chi^(1/3)` obscures the singular small-`chi` structure and produces a needlessly pessimistic or nonuniform bound.

---

## 9. First nontrivial consequence

The unresolved high-band problem has been reduced again:

```math
\boxed{
(\chi,\zeta)
\quad\longrightarrow\quad
\mu=\sqrt2\zeta\chi^{1/3}
}
```

for the small-`chi` rough/smooth crossover that controls the difficult fast channel.

The existing finite-band checks through `kappa_f=300` are **not** tests of the asymptotic fast-channel Bessel coefficient; they are direct checks inside the crossover regime. This is scientifically useful because it explains why those Palm calculations remain necessary even after the Step-28 asymptotic sign mechanism is known.

---

## 10. What remains open

- rigorous derivation of the double-scaling limit `chi^(-2/3) Delta H -> F(mu)` including the Dieker–Yakir weight;
- direct computation of the universal Brownian-minus-parabola/Gaussian-mollifier crossover function `F(mu)`;
- a uniform large-`mu` remainder for `F(mu)`;
- a certified finite `mu_*`, then physical `kappa_*`, beyond which the asymptotic boundary derivative sign is guaranteed;
- closure of the remaining finite crossover interval for any bounded re-entrant pocket;
- hardware interpretation;
- novelty.

---

## 11. Stopping point

The attempted uniform-in-`zeta` remainder has exposed an additional singular matching structure rather than producing a trustworthy finite `K`.

### Single natural next question

> Can the universal Brownian-minus-parabola/Gaussian-mollifier crossover function `F(mu)` be computed directly—without simulating the full detector process—and can it provide a uniform one-dimensional envelope from the smooth crossover through the Bessel tail that is strong enough to close the remaining high-band interval?
