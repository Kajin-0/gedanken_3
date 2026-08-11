# Step 17 — High-Threshold Crossover Law and Large-Speed-Ratio Asymptote

**Date:** 2026-08-11 15:00 EDT  
**Status:** DERIVED / ASYMPTOTIC / NUMERICAL VALIDATION / REFINEMENT. The smooth finite-`kappa` fast/slow crossover admits a compact endpoint-retaining high-threshold law. The Step-16 near-equality between Rice and Palm is not uniform in `kappa`: for every finite hard-window duration `x`, the regularized timing curvature diverges as `sigma_kappa^2 ~ a_x kappa/sqrt(pi)` as `kappa -> infinity`, forcing the Palm correction away from one and recovering the Step-13 rough limit. In contrast, the large speed-ratio limit `r=tau_s/tau_f -> infinity` is especially simple: the crossover approaches the fast detector's full-template timing-feasibility edge, so `L_cross/tau_f -> ell_crit,kappa` and `L_cross/tau_s ~ ell_crit,kappa/r`. This large-`r` law is numerically reached very rapidly. No uniqueness or novelty claim.

---

## 1. Question

Step 16 showed that at

```text
alpha = 1e-6
rho_0 = 6.2
beta = 0.90
kappa = 8
r = 1.2
```

the exact Palm correction to the Rice/Euler-characteristic crossover is only about `0.1%`.

The next questions are:

1. does that near-exact Rice behavior persist as `kappa` and `r` vary?;
2. can the crossover itself be written in a compact high-threshold form?;
3. what happens in the original extreme speed-ratio limit?

The answers are:

- a compact crossover equation exists;
- Rice accuracy is **not uniform in bandwidth**;
- the `r -> infinity` crossover has a particularly simple task-level asymptote.

---

## 2. Regularized finite-time quantities

Retain the Step-15 smooth information spectrum

```math
J_{x,\kappa}(\nu)
=|H_x(\nu)|^2e^{-(\nu/\kappa)^2},
```

with

```math
H_x(\nu)
=\frac{1-e^{-(1+i\nu)x}[1+(1+i\nu)x]}
{(1+i\nu)^2}.
```

Define the regularized finite-time SNR fraction

```math
\mathcal R_\kappa(x)
=\frac{\rho_{x,\kappa}}{\rho_0}
```

and timing-derivative standard deviation

```math
\boxed{
\sigma_\kappa^2(x)
=\frac{\int \nu^2J_{x,\kappa}(\nu)d\nu}
{\int J_{x,\kappa}(\nu)d\nu}.
}
```

At a fast/slow detection-time crossover write

```math
x_s=x,
\qquad
x_f=rx,
```

and

```math
\ell_s=\ell,
\qquad
\ell_f=r\ell,
```

where

```math
r=\frac{\tau_s}{\tau_f}>1.
```

Let

```math
z_\beta=\Phi^{-1}(\beta).
```

The Gaussian thresholds that exactly exhaust the available signal margins at the crossover are

```math
\boxed{
u_s(x)=\rho_0\mathcal R_\kappa(x)-z_\beta,}
```

```math
\boxed{
u_f(x)=\rho_0\mathcal R_\kappa(rx)-z_\beta.}
```

---

## 3. Exact Palm-corrected crossover identity for the smooth scan

From Step 16, for a differentiable one-dimensional stationary Gaussian timing scan,

```math
\alpha
=Q(u)
+\ell\frac{\sigma}{2\pi}e^{-u^2/2}
C_\uparrow,
```

where

```math
\boxed{
C_\uparrow
\equiv
E_\uparrow\!\left[
\frac{1_{\{z(0)\le u\}}}{N_u^+}
\right]
\le1.
}
```

Therefore

```math
\boxed{
\ell
=\frac{2\pi[\alpha-Q(u)]e^{u^2/2}}
{\sigma C_\uparrow}.
}
```

Apply this to the slow and fast scans and impose `ell_f=r ell_s`. The exact smooth-process crossover identity is

```math
\boxed{
\frac{[\alpha-Q(u_f)]e^{u_f^2/2}}
{\sigma_f C_f}
=
r
\frac{[\alpha-Q(u_s)]e^{u_s^2/2}}
{\sigma_s C_s}.
}
```

Equivalently,

```math
\boxed{
u_f^2-u_s^2
=2\ln\!\left[
r\frac{\sigma_f C_f}{\sigma_s C_s}
\frac{\alpha-Q(u_s)}{\alpha-Q(u_f)}
\right].}
```

This is not yet closed because the Palm factors `C_s,C_f` depend on the rare-excursion geometry, but it separates the crossover into four physically interpretable pieces:

```text
finite-time signal accumulation       -> u_s, u_f
local timing bandwidth                -> sigma_s, sigma_f
endpoint false-alarm contribution     -> Q(u_s), Q(u_f)
multiple/overlapping excursions       -> C_s, C_f
```

---

## 4. Endpoint-retaining Rice crossover law

In the isolated-high-excursion limit,

```math
C_s\approx C_f\approx1.
```

Then the crossover is determined by the single scalar equation

```math
\boxed{
u_f^2-u_s^2
\approx
2\ln\!\left[
r\frac{\sigma_f}{\sigma_s}
\frac{\alpha-Q(u_s)}{\alpha-Q(u_f)}
\right].}
```

Once its physically relevant root `x` is found,

```math
\boxed{
\ell_\times^{Rice}
=\frac{2\pi[\alpha-Q(u_s)]}{\sigma_s}
e^{u_s^2/2}.
}
```

This is the compact high-threshold crossover law for the chosen smooth regularized family.

It eliminates the need to solve two independent detection-time problems for every trial `ell`: one scalar root in `x` determines the crossover.

---

## 5. REJECTED SHORTCUT — `high threshold` does not imply `Q(u) << alpha`

A tempting further simplification is

```math
\alpha-Q(u)\approx\alpha.
```

Then

```math
u_f^2-u_s^2
\approx
2\ln\!\left(r\frac{\sigma_f}{\sigma_s}\right).
```

This is valid only when the left-endpoint exceedance probability is negligible compared with the requested global false alarm.

It is **not** valid for the Step-16 near-feasibility task.

At the `kappa=8`, `r=1.2`, `alpha=1e-6` Rice crossover,

```text
Q(u_s)/alpha ~= 0.490
Q(u_f)/alpha ~= 0.448.
```

Almost half of the false-alarm budget is the single-time endpoint term.

Dropping `Q` moves the high-threshold root from the correct Rice value

```text
ell_cross ~= 0.57144
```

to an erroneous search-dominated estimate near

```text
ell_cross ~= 1.00
```

for this task.

**REJECTED SHORTCUT:** small `alpha` alone does not justify deleting the endpoint term. The endpoint-retaining equation is the appropriate compact law.

---

## 6. Rice/Palm accuracy is not uniform in `kappa`

A small Palm sweep was performed at

```text
rho_0 = 6.2
r = 1.2
alpha = 1e-6
beta = 0.90
```

using the Rice crossover at each `kappa` and a local Palm grid target near `0.0025` with `3000` paths per slow/fast point.

The approximate relative deficit of the exact/Palm false-alarm probability from the Rice upper bound was:

```text
kappa     slow deficit      fast deficit
  2       below sampling     below sampling
  8       ~0.08%             below ~0.05%
 16       ~0.19%             ~0.30%
 32       ~0.68%             ~0.41%
```

At `kappa=32`, the Palm ensemble also showed multiple-upcrossing fractions at roughly the percent level rather than the `10^-3` level seen at `kappa=8`.

These values retain some local-grid/systematic uncertainty and are not phase-boundary corrections. Their accepted meaning is the trend:

```text
Rice near-exactness at kappa=8 is not uniform as kappa increases.
```

---

## 7. Why the Rice correction must eventually grow — exact curvature asymptotic

Step 13 derived the hard-window cusp coefficient

```math
\boxed{
a_x=\frac{2x^2e^{-2x}}{\eta(x)},}
```

where

```math
\eta(x)=1-e^{-2x}(1+2x+2x^2).
```

For finite `x`, the Fourier transform has the high-frequency asymptotic

```math
H_x(\nu)
\sim
\frac{i x e^{-x}e^{-i\nu x}}{\nu},
\qquad |\nu|\to\infty.
```

Hence

```math
|H_x(\nu)|^2
\sim
\frac{x^2e^{-2x}}{\nu^2}.
```

For the Gaussian regularizer,

```math
I_0(x,\kappa)
=\int |H_x|^2e^{-(\nu/\kappa)^2}d\nu
\to
2\pi\int_0^x v^2e^{-2v}dv
=\frac{\pi}{2}\eta(x),
```

while

```math
I_2(x,\kappa)
=\int \nu^2|H_x|^2e^{-(\nu/\kappa)^2}d\nu
\sim
\sqrt\pi\,x^2e^{-2x}\kappa.
```

Therefore

```math
\boxed{
\sigma_\kappa^2(x)
\sim
\frac{a_x}{\sqrt\pi}\,\kappa,
\qquad
\kappa\to\infty
\quad\text{for every finite }x.
}
```

This explicitly connects the Step-14 smooth curvature to the Step-13 cusp coefficient.

The Rice mean upcrossing count at fixed `u,ell` therefore grows as

```math
\lambda_u
=\ell\frac{\sigma_\kappa}{2\pi}e^{-u^2/2}
\propto\sqrt\kappa.
```

But the exact false-alarm probability cannot grow without bound. Since

```math
P_{FA}-Q(u)=\lambda_u C_\uparrow\le1,
```

we must have at least

```math
\boxed{
C_\uparrow=O(\kappa^{-1/2})
}
```

along any fixed-`u`, fixed-`ell`, finite-`x` sequence as `kappa -> infinity`.

**DERIVED:** the first-order Rice approximation cannot remain uniformly accurate all the way to the Step-13 rough limit. The Palm factor must collapse to compensate the diverging number of smooth micro-upcrossings inside each rough excursion.

This explains the increasing Palm corrections observed numerically by `kappa=16–32`.

---

## 8. Large speed ratio: the crossover simplifies drastically

Now take

```math
r=\frac{\tau_s}{\tau_f}\to\infty
```

while keeping the physical task parameters and fixed dimensionless regularization model.

Track the fast-to-slow crossover branch from Step 12.

At the crossover,

```math
x_f=rx_s.
```

The slow detector's normalized search interval is

```math
\ell_s=\frac{\ell_f}{r}.
```

As `r -> infinity`, the slow search becomes known-time:

```math
\ell_s\to0,
```

so `x_s` approaches the finite known-time decision duration `x_KT`.

Therefore

```math
x_f=rx_s\to\infty.
```

The fast detector is effectively using its full template.

Define

```math
u_\infty
\equiv
\rho_0-\Phi^{-1}(\beta).
```

Define the fast detector's exact full-template normalized timing-feasibility edge by

```math
\boxed{
\Gamma_{\infty,\kappa}(\ell_{crit,\kappa},\alpha)
=u_\infty.
}
```

Equivalently, `ell_crit,kappa` is the largest normalized unknown-arrival interval for which the full-template fast detector can still meet the requested `(alpha,beta)` operating point.

Then, under the same continuity assumptions used for the crossover branch,

```math
\boxed{
r\ell_\times
\to
\ell_{crit,\kappa},}
```

and therefore

```math
\boxed{
\ell_\times
\sim
\frac{\ell_{crit,\kappa}}{r}.}
```

Returning to physical time,

```math
L_\times
=\tau_s\ell_\times
=\tau_f(r\ell_\times),
```

so

```math
\boxed{
L_\times
\to
\tau_f\ell_{crit,\kappa}.
}
```

**DERIVED / CONDITIONAL LARGE-`r` LAW:** for an extreme speed ratio, the physical timing uncertainty at which the preferred detector switches is set by the **fast detector's time constant times its own full-template search-feasibility length**. The slow time constant drops out at leading order.

---

## 9. Rice form of the large-`r` law

In the isolated-excursion/Rice limit, the full-template feasibility edge is

```math
\boxed{
\ell_{crit,\kappa}^{Rice}
=
\frac{2\pi[\alpha-Q(u_\infty)]}
{\sigma_{\infty,\kappa}}
 e^{u_\infty^2/2},
}
```

where

```math
\sigma_{\infty,\kappa}
```

is the timing-derivative standard deviation of the regularized full template.

For the Step-16 rare-event task

```text
rho_0=6.2
alpha=1e-6
beta=0.90
```

so

```text
u_infinity ~= 4.918448434.
```

The Rice feasibility lengths are

```text
kappa       ell_crit,kappa^Rice
  2              0.988282
  4              0.811380
  8              0.723222
 16              0.678958
 32              0.656729
```

---

## 10. Numerical convergence to the large-`r` law is extremely rapid

Direct Rice crossover solutions give the following fast-detector normalized crossover length `r ell_cross`:

```text
kappa   ell_crit     r=2 result   error       r=3 result   error
  2     0.988282     0.987703    -0.059%      0.988281    -0.00012%
  8     0.723222     0.722497    -0.100%      0.723220    -0.00037%
 32     0.656729     0.656037    -0.105%      0.656726    -0.00043%
```

By `r=3`, the large-speed-ratio asymptote is already numerically indistinguishable at the displayed precision for this task.

This is much faster convergence than one might expect from the original `r=10^9` thought experiment.

---

## 11. Palm spot check of the large-`r` feasibility edge

The large-`r` asymptote uses the **full template**, not the finite hard-window template responsible for the Step-13 cusp.

Palm simulations at the Rice full-template feasibility edge with `3000` paths and local target spacing near `0.0025` gave:

```text
kappa   Rice ell_crit   P_FA at Rice edge
  2       0.988282       ~9.99995e-7
  8       0.723222       ~9.98212e-7
 32       0.656729       ~9.94266e-7
```

Rice remains an upper bound, so the exact/Palm feasibility length is slightly larger. A local constant-Palm-factor correction suggests only sub-percent changes over this range, although a dedicated root solve was not performed here.

Thus the large-`r` structural law is much more robust than applying Rice to a finite-`x`, very-large-`kappa` scan.

---

## 12. Application to the original extreme response-time ratio — illustrative only

For the original thought-experiment scales

```text
tau_f = 1 ns
tau_s = 1 s
r = 1e9
```

and **only** for the Step-16 validation task parameters

```text
rho_0=6.2
alpha=1e-6
beta=0.90
kappa=8,
```

the large-`r` Rice law gives

```math
\boxed{
L_\times^{Rice}
\approx
0.723\,\mathrm{ns}.
}
```

A Palm spot check of the full-template feasibility edge indicates a sub-percent upward correction, not an order-of-magnitude change.

This number is not a prediction for a real photodetector. Its importance is structural:

```text
with an enormous speed ratio,
the switch scale is O(tau_fast),
not O(tau_slow).
```

---

## 13. A new noncommuting-limit result

Two limits behave differently.

### Fixed finite `r`, then `kappa -> infinity`

Both crossover filters remain finite-duration objects. Their hard endpoint produces

```math
\sigma_\kappa^2\propto\kappa,
```

so smooth-process Rice upcrossing counts diverge and the Palm correction becomes essential. This route approaches the Step-13 rough process nonuniformly.

### `r -> infinity` first, then `kappa -> infinity`

The fast crossover filter becomes the **full template**,

```math
x_f\to\infty,
```

while the slow timing-search interval tends to zero.

The full-template spectrum decays as `1/nu^4`, so its second moment stays finite even as the regularizer is removed. In fact for this family

```math
\sigma_{\infty,\kappa}\to1
\qquad (\kappa\to\infty).
```

Thus the large-`r` asymptote remains regular.

The Rice leading estimate then tends

```math
\boxed{
\ell_{crit,\infty}^{Rice}
=
2\pi[\alpha-Q(u_\infty)]e^{u_\infty^2/2}.
}
```

For the Step-16 validation parameters this limit is approximately

```text
0.634411.
```

**DERIVED / REFINEMENT:** the bandwidth-removal and extreme-speed-ratio limits do not commute. The original enormous speed-ratio problem is therefore mathematically cleaner than a moderate-ratio finite-window scan taken directly to infinite bandwidth.

---

## 14. What has been established

- **DERIVED:** an exact Palm-corrected smooth-process crossover identity separating SNR accumulation, timing curvature, endpoint probability, and multiple-excursion correction.
- **DERIVED / CONDITIONAL:** setting the Palm factors to one gives a compact endpoint-retaining Rice crossover equation.
- **REJECTED SHORTCUT:** `alpha << 1` does not imply `Q(u) << alpha`; dropping the endpoint term is badly wrong for the Step-16 near-feasibility task.
- **NUMERICAL REFINEMENT:** Rice/Palm agreement degrades systematically as `kappa` rises at fixed finite `r`.
- **DERIVED:** for finite hard-window `x`, `sigma_kappa^2 ~ a_x kappa/sqrt(pi)`; therefore the Rice approximation cannot remain uniformly accurate as `kappa -> infinity`.
- **DERIVED / CONDITIONAL:** on the tracked fast-to-slow branch, `r ell_cross -> ell_crit,kappa` and `L_cross -> tau_f ell_crit,kappa` as `r -> infinity`.
- **NUMERICAL VALIDATION:** the large-`r` asymptote is reached extremely rapidly in the tested Rice solutions; `r=2` is within about `0.1%` and `r=3` within about `5e-4%` across representative `kappa` values.
- **REFINEMENT:** taking `r -> infinity` first removes the finite-window cusp from the fast side and yields a regular bandwidth-removal limit.

---

## 15. What has not been established

- No proof that the fast/slow crossover is unique for all parameters.
- No universal Palm correction law across all `kappa`, `r`, `rho_0`, and `beta`.
- No exact analytic value of the rough finite-`r`, `kappa -> infinity` crossover.
- No dedicated Palm root solve for the large-`r` full-template feasibility edge at every `kappa`.
- No claim that the illustrative `0.723 ns` crossover is representative of real detectors.
- No same-fixed-physical-bandwidth comparison across unequal detector time constants.
- No universal speed/detectivity metric or detector ranking.
- No novelty claim.

---

## 16. Stopping point

The co-scaled finite-bandwidth family now has a compact high-threshold crossover law and a simple extreme-speed-ratio asymptote.

### Single natural next question

> If the two detectors are connected to the **same physical readout bandwidth** rather than the same dimensionless `kappa`, does the large-`r` crossover law survive, and can the electronics bandwidth itself change or optimize which detector wins?
