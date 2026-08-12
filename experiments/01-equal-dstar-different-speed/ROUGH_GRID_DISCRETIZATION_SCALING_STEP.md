# Step 46 — Rough-Endpoint Grid Bias Is a Missed-Maximum `sqrt(dt)` Effect

**Date:** 2026-08-12 18:55 EDT  
**Status:** DERIVED / PAIRED NESTED-GRID DIAGNOSTIC / NUMERICAL VALIDATION / ASYMPTOTIC / REFINEMENT / OPEN. Step 45 showed that witness-time tuning alone does not comfortably absorb the old `0.002 alpha` timing-grid allowance. This step decomposes the duration-truncated rough-endpoint grid error using common continuous-spectrum paths sampled at nested meshes `dt=.001`, `.0005`, and `.00025`. The result is sharp: essentially the entire positive coarse-to-fine correction comes from **missed between-sample level-`u` maxima**, while the error in the interpolated long-component weight `1/L` is two orders smaller. The size of the missed-maximum correction is quantitatively explained by the Brownian local cusp `R(h)=1-a|h|+O(h^2)` and the classical `sqrt(dt)` Brownian extreme-value discretization law with continuity-correction constant `beta=-zeta(1/2)/sqrt(2pi)`. At `X=7.16`, the leading model predicts a continuum correction of about `1.03e-3 alpha` from a `.001` grid and predicts the observed `.001 -> .00025` paired shift almost exactly. This is an asymptotic/numerically validated correction, not yet a finite-`dt` one-sided theorem. No novelty claim.

---

## 1. Separate the two grid errors

For the Step-44 duration-truncated contribution

```math
Y_{dt}=m_a\frac{S_{dt}}{L_{dt}}1_{\{L_{dt}\ge L_0\}},
```

with `L0=.02`, there are two conceptually different finite-grid errors:

1. **missed success:** the finer/continuum path exceeds `u` inside the selected lower-level component, but the coarse grid samples do not;
2. **duration-weight error:** both grids identify the component as successful and long, but the interpolated duration `L_dt` changes the weight `1/L_dt`.

These can be measured path by path on nested meshes generated from the same stationary Gaussian spectral realization and the same occupation-Palm conditioning variables.

---

## 2. Nested common-path construction

At the fast rough endpoint use

```text
X      = 7.16
Lambda = .895
Delta  = .15
L0     = .02
u      ~= 4.95898348
a       = u-Delta ~= 4.80898348.
```

Generate the rough endpoint process on the finest mesh

```text
dt_fine = .00025
```

with FFT period `16.384`, then evaluate the same conditioned path after subsampling by factors two and four:

```text
fine    dt=.00025
medium  dt=.00050
coarse  dt=.00100.
```

The same white-noise realization, Palm tail uniform, and selected physical occupation time are used at all three resolutions. Therefore differences between resolutions have far lower variance than independent absolute estimates.

Two independent `12000`-path paired runs were pooled, for `24000` paths total.

---

## 3. Paired coarse-to-fine result

Pooling the two runs gives

```text
quantity                                      value / alpha
----------------------------------------------------------------
fine(.00025) - coarse(.001) mean              +0.00053010
paired SE                                      0.00025069

fine(.00025) - medium(.0005) mean             +0.00015785
paired SE                                      0.00015069
```

The absolute Palm means fluctuate at the `~1e-2 alpha` scale in these modest runs, so they are not used here. Only paired differences are interpreted.

---

## 4. Missed maxima dominate the `.001 -> .00025` correction

Across the pooled `24000` paths:

```text
fine-long successful, coarse not successful: 5 paths.
```

Those five missed components contribute

```math
\boxed{0.00052149\,\alpha}
```

to the total coarse-to-fine mean shift.

Among components classified successful and long on **both** meshes, the total duration-weight correction is only

```math
\boxed{(8.61\pm4.13)\times10^{-6}\,\alpha.}
```

Thus

```math
\boxed{\text{missed maxima account for about 98\% of the observed positive grid correction.}}
```

The old grid problem is therefore not primarily error in linearly interpolating `L`. It is the possibility that the rough process crosses the final success threshold `u` between timing samples.

For `.0005 -> .00025`, one missed fine-grid success was observed in `24000` paths; duration-only change again remained at the few `1e-6 alpha` scale. The small number of missed events makes direct Monte Carlo calibration noisy, which motivates the local asymptotic calculation below.

---

## 5. Rough local covariance fixes the convergence rate

At finite `X`, the hard-window rough endpoint has

```math
R(h)=1-a_X|h|-\frac{b_X}{2}h^2+o(h^2).
```

At `X=7.16`, previous exact covariance work gives

```math
\boxed{a_X\simeq6.19142\times10^{-5}.}
```

Hence, on sufficiently short scales,

```math
Var[z(t+h)-z(t)]\sim2a_X|h|.
```

The local rough fluctuation is therefore Brownian with variance rate

```math
\sigma_B^2=2a_X.
```

Classical Brownian extreme-value discretization has error of order `sqrt(dt)`. The mean continuity-correction constant appearing in the limiting Brownian maximum/grid error is

```math
\boxed{
\beta=-\frac{\zeta(1/2)}{\sqrt{2\pi}}
\simeq0.582597.
}
```

Therefore the leading amplitude gap between the continuum maximum and a regular grid maximum is

```math
\boxed{
\Delta M_{dt}
\sim\beta\sqrt{2a_Xdt}.
}
```

This is an **asymptotic local model**, not yet a finite-grid stochastic domination bound for the present Gaussian process.

Primary references used for this scaling are Asmussen-Glynn-Pitman (1995), which establishes `1/2`-order Brownian discretization error, and Dieker-Lagos (2017/2026 revision), which derives normalized extreme-event discretization limits and identifies the constant `-zeta(1/2)/sqrt(2pi)` as a mean of the limiting laws.

---

## 6. Convert amplitude bias to rare-event probability bias

Step 36 measured the fast cluster-maximum intensity near the operating threshold as approximately

```math
h_a(u)\sim5\alpha
```

per unit threshold.

Therefore the leading false-alarm discretization correction is

```math
\boxed{
\frac{\Delta p_{dt}}{\alpha}
\sim
5\beta\sqrt{2a_Xdt}.
}
```

At `X=7.16`:

```text
dt            amplitude correction      probability correction / alpha
------------------------------------------------------------------------
.00100        2.0501e-4                 1.0251e-3
.00050        1.4497e-4                 7.2483e-4
.00025        1.0251e-4                 5.1253e-4
```

The predicted difference between the `.001` and `.00025` meshes is

```math
1.0251\times10^{-3}-5.1253\times10^{-4}
=
\boxed{5.1253\times10^{-4}\,\alpha}.
```

The paired numerical result was

```math
\boxed{(5.3010\pm2.5069)\times10^{-4}\,\alpha.}
```

The agreement is striking given that no coefficient was fit to the paired data.

For `.0005 -> .00025`, the asymptotic prediction is

```text
2.1230e-4 alpha,
```

while the noisy paired estimate is

```text
(1.5785 +/- 1.5069)e-4 alpha.
```

Again the scale is consistent.

**NUMERICAL VALIDATION / ASYMPTOTIC:** the rough `sqrt(dt)` continuity correction explains both the convergence rate and the observed coarse-to-fine magnitude.

---

## 7. Consequence for the Step-44 knife-edge

Step 44's finite-grid 95% upper bound at `dt~.001` has only

```text
4.22e-5 alpha
```

of certified margin.

The leading rough-grid continuum correction at that mesh is instead approximately

```text
1.03e-3 alpha,
```

roughly 24 times larger.

Thus the `.001` finite-grid certificate should **not** be expected to survive continuum recovery at `X=7.16` merely by replacing the old `.002 alpha` allowance with a sharper central estimate.

If one insisted on making the leading `sqrt(dt)` correction smaller than the current Step-44 margin without moving the witness, the asymptotic estimate would require roughly

```math
\boxed{dt\lesssim1.7\times10^{-6}.}
```

That is not an attractive brute-force simulation route.

**REFINEMENT:** the old `.002 alpha` grid allowance was conservative by roughly a factor of two, but it was guarding a real rough-grid effect rather than numerical noise.

---

## 8. What this changes about Step 45

Step 45 concluded that moving `X` did not comfortably absorb the **old** `.002 alpha` allowance. The present step shows the physically relevant leading correction is closer to `.001 alpha` at `dt=.001`.

Therefore the moderate witness shift around

```text
X~7.5,
```

which numerically gained `~.0016 alpha` on the fast branch while preserving a broad slow margin, may become useful **after** a finite-`dt` upper control of the rough continuity correction is available.

This does not invalidate Step 45's negative result: witness shifting alone did not remove the need to understand discretization. It refines the design tradeoff now that the discretization scale is understood.

---

## 9. Remaining theorem gap

The Brownian continuity correction used here is asymptotic. What is still missing is a one-sided finite-`dt` statement of the form

```math
p_{continuum}(u)
\le
p_{grid}(u-\delta_{dt})+\varepsilon_{dt}
```

with explicit `delta_dt` and `epsilon_dt` valid for the present Gaussian covariance, and sharp enough to retain the rare-event scale.

A generic modulus bound is too loose; the useful theorem must exploit the local Brownian/Bessel extreme structure near the high maximum.

---

## 10. Stopping point

The timing-grid bias is now decomposed and its dominant mechanism identified. Duration interpolation is negligible at the present scale; missed between-sample maxima generate a genuine `sqrt(dt)` rough-endpoint correction whose leading coefficient agrees with paired nested-grid data.

### Single natural next question

> Can the Brownian/Bessel extreme-value discretization limit be converted into an explicit one-sided finite-`dt` upper envelope for this Gaussian timing process, so that the `~1e-3 alpha` continuum correction can be certified rather than merely estimated asymptotically?
