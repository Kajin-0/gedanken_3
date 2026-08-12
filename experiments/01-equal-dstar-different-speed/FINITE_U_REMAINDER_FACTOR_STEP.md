# Step 39 — Finite-`u` Remainder Factor: Large Amplitude, Small Threshold Slope

**Date:** 2026-08-12 06:14 EDT  
**Status:** DEFINED / DERIVED / NUMERICAL REFINEMENT / REJECTED SHORTCUT / OPEN. Step 38 bounded the matched tangent hazard exactly, but the exact Step-36 cluster strip remained somewhat larger. This step factorizes the exact physical cluster first moment as `N_a(u,q)=N_tan(u,q) R(u,q)` and shows that the finite-`u` correction is not a small-amplitude perturbation at `u~4.96`: `R` is about `1.56` on the fast high-band trajectory. However, the threshold-continuity problem depends on the logarithmic slope of `R`, not on `R-1`. Combining the Step-36 strip intensity, Step-33/34 cluster first moments, and the Step-38 tangent hazard gives a numerically inferred `-d_u log R` of order `0.1–0.7` per threshold unit over the tested tail. A conservative numerical slope scale `L_R~0.8` accounts for the observed strip excess and increases the `delta=1e-4` symmetric-strip factor only from about `9.89e-4` to about `1.149e-3`. This is a numerical finite-`u` remainder-slope diagnostic, not a theorem-level bound on `R`. No novelty claim.

---

## 1. Factorization

Define the exact successful-cluster first moment from Steps 33/36,

```math
N_a(u,q)=E[C_a(u)],
```

and the matched tangent/Pickands intensity from Steps 37/38,

```math
N_{tan}(u,q)
=\ell\frac{u\sqrt b}{\sqrt2}\,
\mathcal H(\chi(u),\zeta(u))\,Q(u).
```

Define the finite-threshold correction factor

```math
\boxed{
R(u,q)=\frac{N_a(u,q)}{N_{tan}(u,q)}.
}
```

This identity is exact wherever `N_tan>0`; no approximation has yet been made.

The key continuity identity is

```math
\boxed{
-\partial_u\log R
=\frac{h_a}{N_a}-\frac{h_{tan}}{N_{tan}},
}
```

whenever the local derivatives exist, where

```math
h_a=-\partial_uN_a,
\qquad
h_{tan}=-\partial_uN_{tan}.
```

Thus the threshold-continuity problem depends on the logarithmic slope of `R`, not directly on its amplitude.

---

## 2. Tangent intensity for the Step-34 fast witness

Use the common witness time

```text
X = x_f = 7.16
ell = Lambda = 0.895
u = u_f ~= 4.959.
```

For the hard-window covariance coefficients,

```math
\eta(x)=1-e^{-2x}(1+2x+2x^2),
```

```math
a_x=\frac{2x^2e^{-2x}}{\eta(x)},
```

```math
b_x=\frac{1+e^{-2x}(2x^2-2x-1)}{\eta(x)}.
```

At `x=7.16`,

```text
eta ~= 0.99992884
a_x ~= 6.1914e-5
b_x ~= 1.00012383.
```

Hence

```text
chi ~= 3.07e-4
```

throughout the high-band tail.

For the small-`chi` fast channel, use the Step-30 canonical approximation

```math
\mathcal H(\chi,\zeta)
\approx
\frac1{\sqrt\pi}
+\chi^{2/3}[F(0)-F(\mu)],
```

with

```math
\mu=\sqrt2\zeta\chi^{1/3},
```

and at the rough endpoint

```math
\mathcal H_{mix}(\chi)
\approx
\frac1{\sqrt\pi}+\chi^{2/3}F(0),
\qquad F(0)\approx0.892.
```

This is the same model-reduced canonical approximation already validated at percent level in Step 30; it is not a new exact identity.

Representative tangent first moments are then

```text
kappa_f      N_tan/alpha
------------------------
170             0.6294
300             0.6297
1000            0.6306
infinity        0.6319
```

for `alpha=1e-6`.

---

## 3. The finite-`u` amplitude correction is large

Compare with the directly estimated exact cluster first moments from Steps 33/34:

```text
kappa_f      N_a/alpha      N_tan/alpha      R=N_a/N_tan
----------------------------------------------------------------
170            ~0.9878          0.6294          ~1.570
300             0.9862          0.6297          ~1.566
1000            0.9842          0.6306          ~1.561
infinity        0.9897          0.6319          ~1.566
```

The `170` value uses the Step-34 endpoint anchor plus paired correction; the `300`, `1000`, and `infinity` values use the Step-33 cluster calculations. Their Monte Carlo uncertainty is larger than the displayed digits.

**REFINEMENT:** the phrase "remaining `~5–10%` excess" from Step 38 refers to the **local hazard/strip coefficient**, not the amplitude of the first-moment correction. At `u~5`, the tangent intensity underestimates the exact finite-amplitude cluster first moment by roughly `55–60%`:

```math
\boxed{R\sim1.56.}
```

Therefore a perturbation expansion in `R-1` is inappropriate at this threshold.

At the same time, `R` is nearly constant across the high-band `q` trajectory within the numerical precision of the existing cluster estimates. The amplitude mismatch is therefore not automatically dangerous for inter-node threshold continuity.

---

## 4. Infer the threshold slope of `R`

Step 36 measured the local cluster-maximum strip intensity. Using the central diagnostic half-width

```text
w=0.01,
```

the approximate exact cluster hazard ratios are

```math
\frac{h_a}{N_a}
\approx
\frac{\nu_a((u-w,u+w])}{2wN_a(u)}.
```

Combining Step-36 strip coefficients with the exact first moments above gives approximately

```text
kappa_f      h_a/N_a      h_tan/N_tan      inferred -d_u log R
----------------------------------------------------------------
170            5.01           4.945              ~0.07
300            5.13           4.945              ~0.19
1000           5.39           4.945              ~0.45
infinity       5.38           4.944              ~0.43
```

The tangent hazards were evaluated deterministically from the Step-30 canonical `H` approximation; Step 38 independently proves the upper envelope `h_tan/N_tan <= phi/Q-1/u ~=4.9452`.

Repeating the inference with the Step-36 widths `w=.005` and `.02` gives a broader numerical range roughly

```math
\boxed{
0.07\lesssim-\partial_u\log R\lesssim0.68
}
```

across the tested high-band points.

This range includes Monte Carlo and finite-strip-width effects and is not a confidence interval.

**NUMERICAL REFINEMENT:** the finite-`u` remainder is large in value but changes relatively slowly with threshold.

---

## 5. Why a log-slope bound is enough

Suppose on a threshold neighborhood `[u-delta,u+delta]` we have

```math
\boxed{
|\log R(v,q)-\log R(u,q)|
\le L_R|v-u|.
}
```

Then

```math
R(u-\delta)\le R(u)e^{L_R\delta},
```

```math
R(u+\delta)\ge R(u)e^{-L_R\delta}.
```

Step 38 gives the tangent finite-strip ratios

```math
\frac{N_{tan}(u-\delta)}{N_{tan}(u)}
\le A_-(u,\delta),
```

```math
\frac{N_{tan}(u+\delta)}{N_{tan}(u)}
\ge A_+(u,\delta),
```

where

```math
A_-(u,\delta)
=\frac{u-\delta}{u}\frac{Q(u-\delta)}{Q(u)},
```

```math
A_+(u,\delta)
=\frac{u+\delta}{u}\frac{Q(u+\delta)}{Q(u)}.
```

Therefore

```math
\boxed{
\frac{N_a(u-\delta)-N_a(u+\delta)}{N_a(u)}
\le
A_-e^{L_R\delta}-A_+e^{-L_R\delta}.
}
```

This is an exact algebraic consequence of a log-Lipschitz remainder bound; it does not require `R` to be close to one.

For small `delta`,

```math
A_-e^{L_R\delta}-A_+e^{-L_R\delta}
=
B(u,\delta)+2L_R\delta+O(\delta^2),
```

where `B` is the Step-38 tangent strip factor.

---

## 6. Numerical consequence at `delta=1e-4`

At

```text
u ~= 4.959
delta = 1e-4,
```

Step 38 gives

```text
B(u,delta) ~= 9.8904e-4.
```

The existing strip diagnostics suggest that a conservative **numerical** working scale

```math
L_R=0.8
```

covers the observed inferred slopes.

Then

```math
\boxed{
A_-e^{L_R\delta}-A_+e^{-L_R\delta}
\approx1.1490\times10^{-3}.
}
```

Thus the remainder-slope allowance increases the tangent strip factor by only

```text
~1.60e-4
```

relative to `N_a(u)`.

When `N_a(u)` is of order `alpha=1e-6`, this corresponds to an absolute symmetric-strip scale of approximately

```math
\boxed{
1.15\times10^{-9}.
}
```

This is consistent with the direct Step-36 strip measurements. The observed `5–10%`-level hazard excess requires only a modest logarithmic slope even though `R` itself is about `1.56`.

---

## 7. REJECTED SHORTCUT — bounding `R-1` is the wrong problem

A natural second-order-asymptotic strategy would try to prove

```math
|R-1|\ll1.
```

At the actual operating threshold this is false numerically:

```math
R-1\sim0.56.
```

Yet the threshold continuity can still be excellent because it depends on

```math
\partial_u\log R,
```

not on `R-1`.

**REJECTED SHORTCUT:** requiring a uniformly small multiplicative Pickands remainder would be unnecessarily strong and would fail at `u~5` even though the required narrow-strip continuity can still hold.

---

## 8. Literature check and scope

A targeted search of current primary Gaussian-extremes literature found strong exact/asymptotic results for high excursions, Pickands/Piterbarg constants, and overshoots, but no off-the-shelf theorem providing a numerical uniform second-order remainder for this threshold-dependent smooth-to-rough family at `u~5`.

Accordingly, this step does **not** promote `L_R=0.8` to an analytic theorem constant. It is a transparent numerical envelope inferred from the existing exact-cluster calculations.

---

## 9. First nontrivial consequence

The remaining finite-threshold correction has now been separated into two very different properties:

```text
amplitude:
    R ~ 1.56     (large; nonperturbative at u~5)

threshold slope:
    -d_u log R ~ O(0.1–1) numerically
    (small enough that a 1e-4 threshold shift changes R only by O(1e-4)).
```

Therefore the Step-34 theorem gap should **not** be framed as proving a small second-order Pickands remainder. The narrower useful theorem would be a local log-Lipschitz or finite-ratio bound for `R`.

---

## 10. What remains open

- derive an analytic finite-threshold ratio bound for `R(u+delta,q)/R(u,q)` without requiring `R~1`;
- determine whether Gaussian change-of-level / Cameron-Martin methods can bound `|log R(u+delta)-log R(u)|` directly;
- make the `L_R~0.8` numerical envelope statistically and grid rigorous;
- combine such a bound with the Step-35 sup-norm `q`-coupling tail `eta`;
- formal interval treatment of the Step-30 canonical approximation used for `N_tan`;
- extension to other task parameters and detector models;
- hardware interpretation;
- novelty.

---

## 11. Stopping point

The finite-`u` correction is not a small-amplitude remainder, but its threshold variation is modest on the scale relevant to the inter-band continuity problem. The correct next target is a **local ratio theorem for `R`**, not a proof that `R` is close to unity.

### Single natural next question

> Can a Gaussian level-shift / Cameron-Martin argument produce a direct finite-ratio bound on `R(u+delta,q)/R(u,q)`—or on the exact cluster first moment itself—over `delta~1e-4`, avoiding any need for a small-amplitude second-order Pickands expansion?
