# Discrete optical-depth ladder — finite-section implementation test

**Date:** 2026-08-13  
**Status:** CONSTRUCTIVE REDUCED-ORDER PASS / THREE EQUAL SECTIONS CLEAR 30% GATE AT CURRENT FLOOR / NOT MAXWELL OR TCAD / NOVELTY NOT ESTABLISHED

## 1. Why this step exists

The continuous-map surrogate assumed that the conditional mean absorption depth could vary smoothly with optical propagation coordinate. A real device may instead be easier to realize as a finite staircase: a small number of longitudinal absorbing sections, each with a localized transverse absorption depth.

The purpose of this step is to answer:

1. how many depth sections are required before most of the continuous timing benefit is recovered;
2. whether equal-length sections are already adequate or require delicate nonuniform optimization;
3. how much section-to-section mean timing error can be tolerated before the 30% RMS-improvement gate is lost;
4. whether the forward/reverse timing signature survives discretization.

This is still a reduced-order construction. It does not demonstrate a realizable Maxwell mode or epitaxial device.

The companion script is `numerics/discrete_depth_ladder.py`.

---

## 2. Normalized absorption coordinate

Keep the same 90%-absorption benchmark

```math
U=X/L,\qquad 0\le U\le1,
```

with

```math
p(U)=\frac{b e^{-bU}}{1-e^{-b}},\qquad b=\ln 10.
```

The full distributed depth variance is

```math
A\equiv Var(U)=0.06515490689.
```

The present device scale remains

```text
d = 2 um
L = 3 mm
T0 = d/v0 = 40 ps
v0 = 5e4 m/s
vg = 7.5e7 m/s
```

and the already-established combined stochastic floor is

```math
F\equiv \sigma_{floor}^2/T_0^2=0.03478633258.
```

Thus

```text
direct depth-sensitive RMS = 12.6454 ps
continuous matched RMS      =  7.4604 ps
continuous ideal reduction  = 41.00%
```

---

## 3. Staircase map

Divide the optical path into `N` sections. In section `j`, replace the continuous normalized mean depth `U` by a constant depth level

```math
Q_N(U)=q_j.
```

The normalized forward deterministic timestamp is

```math
\frac{T_f}{T_0}=U+1-Q_N(U).
```

Therefore only

```math
\epsilon_N(U)=U-Q_N(U)
```

contributes to the residual between-section/within-section deterministic spread.

For fixed section boundaries, the mean-square-optimal depth is simply the conditional centroid

```math
\boxed{q_j=E[U\mid j].}
```

This is ordinary centroid quantization mathematics, not a novelty claim.

The forward deterministic residual is then

```math
\boxed{D_N=Var[U-Q_N(U)].}
```

---

## 4. Exact simplification for equal longitudinal sections

Set every longitudinal section to the same normalized width

```math
h=1/N.
```

Because the source density is exponential, the conditional distribution inside every equal-width interval has exactly the same shape after translation. Therefore each optimal centroid has the form

```math
q_j=(j-1)h+\mu_h,
```

where

```math
\boxed{
\mu_h=\frac1b-\frac{h}{e^{bh}-1}.
}
```

Hence the depth levels themselves are equally spaced by

```math
\Delta z=d/N.
```

The optical delay between neighboring section centroids is likewise

```math
\Delta t_o=T_0/N,
```

or equivalently the physical propagation increment is

```math
\Delta x=L/N.
```

Most importantly, the quantization variance is exactly the conditional variance of one section:

```math
\boxed{
D_N=
\frac1{b^2}
-\frac{h^2 e^{bh}}{(e^{bh}-1)^2}.
}
```

For large `N`,

```math
D_N\sim\frac{1}{12N^2}.
```

Thus the continuous limit is approached quadratically in section count.

---

## 5. Exact forward/reverse relation

Because

```math
Q_N(U)=E[U\mid\text{section}],
```

the quantization error is orthogonal to every function of the section label, in particular to `Q_N`:

```math
Cov(U-Q_N,Q_N)=0.
```

Therefore

```math
Cov(U,Q_N)=Var(Q_N).
```

Since

```math
D_N=Var(U-Q_N)=A-Var(Q_N),
```

the reverse deterministic timestamp, proportional to `U+Q_N`, obeys

```math
\boxed{
R_N\equiv Var(U+Q_N)=4A-3D_N.
}
```

This is useful experimentally: in this reciprocal staircase surrogate, reducing the forward discretization error automatically drives the reverse device toward the full anti-matched variance `4A`.

The nominal total RMS values are therefore

```math
\sigma_{f,N}=T_0\sqrt{F+D_N},
```

```math
\sigma_{r,N}=T_0\sqrt{F+4A-3D_N}.
```

---

## 6. Section-count result

For equal-length sections:

| N | `D_N` | forward RMS | reduction vs direct | fraction of continuous reduction | reverse RMS |
|---:|---:|---:|---:|---:|---:|
| 1 | 0.0651549 | 12.645 ps | 0.00% | 0.0% | 12.645 ps |
| 2 | 0.0195220 | 9.322 ps | 26.28% | 64.1% | 19.467 ps |
| 3 | 0.0089928 | 8.369 ps | **33.81%** | 82.5% | 20.724 ps |
| 4 | 0.0051232 | 7.991 ps | **36.81%** | 89.8% | 21.167 ps |
| 5 | 0.0032983 | 7.806 ps | 38.27% | 93.3% | 21.373 ps |
| 6 | 0.0022979 | 7.703 ps | 39.09% | 95.3% | 21.485 ps |
| 8 | 0.0012967 | 7.598 ps | 39.91% | 97.3% | 21.597 ps |
| 9 | 0.0010254 | 7.570 ps | **40.14%** | 97.9% | 21.627 ps |

At the current residual floor:

```text
minimum N for >=20% RMS improvement = 2
minimum N for >=30% RMS improvement = 3
minimum N for >=40% RMS improvement = 9
```

The most important practical result is therefore

```math
\boxed{N=3\ \text{already clears the 30% gate}.}
```

A four-section staircase recovers almost 90% of the total RMS improvement available from the continuous map.

This is substantially more favorable than a requirement for a finely continuous transverse mode migration.

---

## 7. Concrete three- and four-section geometries

### Three equal sections

Each section is `1.0 mm` long and neighboring optical centroids differ by

```text
13.333 ps
```

at the current `vg` scale.

The optimal transverse mean depths are

```text
section 1: z = 0.2911 um
section 2: z = 0.9578 um
section 3: z = 1.6244 um
```

so neighboring depth levels differ by exactly

```text
0.6667 um.
```

Predicted total timing:

```text
forward =  8.369 ps RMS
reverse = 20.724 ps RMS
```

### Four equal sections

Each section is `0.75 mm` long and neighboring optical centroids differ by

```text
10.000 ps.
```

The optimal mean depths are

```text
section 1: z = 0.2261 um
section 2: z = 0.7261 um
section 3: z = 1.2261 um
section 4: z = 1.7261 um
```

with exactly `0.5000 um` depth spacing.

Predicted total timing:

```text
forward =  7.991 ps RMS
reverse = 21.167 ps RMS.
```

These are not proposed final layer structures. They are the first explicit geometric targets for a future optical-mode calculation.

---

## 8. Nonuniform optimization is only a small correction

Allowing the section boundaries to move and imposing the usual centroid/midpoint conditions gives a Lloyd-Max staircase. At the current exponential benchmark:

```text
N=3 equal sections:      8.369 ps forward, 33.81% improvement
N=3 optimized sections:  8.269 ps forward, 34.61% improvement

N=4 equal sections:      7.991 ps forward, 36.81% improvement
N=4 optimized sections:  7.928 ps forward, 37.30% improvement
```

Thus the gain from longitudinal boundary optimization is only about `0.10 ps` for three sections and `0.06 ps` for four sections at the present floor.

**REFINEMENT:** precise nonuniform section placement is not the first-order challenge. Achieving the required transverse depth localization and low stochastic transport floors is more important.

---

## 9. Section-to-section systematic timing-error budget

Let the actual mean timing error of section `j`, after subtracting any common offset, be `h_j`. It can contain depth-placement error, optical-delay error, section-dependent mean avalanche delay, or any other deterministic section mean shift.

Because the ideal centroid quantization error has zero conditional mean inside every section,

```math
Cov(U-Q_N,h_j)=0.
```

Therefore

```math
\boxed{
\frac{\sigma_{f,N}^2}{T_0^2}
=F+D_N+Var_w(h_j/T_0),
}
```

where `Var_w` is weighted by detected-photon probability in each section.

For the 30% improvement gate, the maximum weighted section-to-section timing RMS is:

| N | allowed systematic section-mean RMS |
|---:|---:|
| 3 | **2.88 ps** |
| 4 | **3.81 ps** |
| 5 | 4.17 ps |
| 6 | 4.36 ps |
| 8 | 4.54 ps |
| 9 | 4.59 ps |

For pure depth-placement error at `v0=5e4 m/s`, these correspond to approximately

```text
N=3 -> 144 nm weighted RMS
N=4 -> 190 nm weighted RMS
```

of section mean-depth error.

For pure optical path error at `vg=7.5e7 m/s`, they correspond to approximately

```text
N=3 -> 216 um weighted RMS optical path
N=4 -> 286 um weighted RMS optical path.
```

These are **section mean** error budgets. They do not replace the already included `100 nm` unresolved local absorption-depth RMS within a section.

A combined depth/optical error budget should be applied to timing directly; independent contributions may be added in variance, while correlated contributions require their covariance.

---

## 10. Robustness of the direction-reversal control

Nominal discretization alone leaves a very large direction contrast:

```text
N=3: forward 8.37 ps, reverse 20.72 ps
N=4: forward 7.99 ps, reverse 21.17 ps.
```

For any reciprocal implementation in which the same sectionwise additive mean timing perturbation enters forward and reverse, the standard-deviation triangle inequality gives a conservative bound. Even if the entire 30%-gate error budget were arranged adversarially to reduce the reverse deterministic spread, the reverse total RMS remains roughly `18 ps` for the three- and four-section cases while the forward 30%-gate ceiling is `8.85 ps`.

Thus the direction-odd signature is not erased by the amount of section mismatch that still permits a 30% forward improvement.

Implementation-specific nonreciprocal or direction-dependent optical errors must be handled by a later Maxwell model rather than assumed away.

---

## 11. What has been established

**DERIVED / REDUCED-ORDER:**

1. A finite staircase has an exact centroid-quantization representation.
2. Equal longitudinal sections admit a closed-form residual variance for the 90%-absorption exponential benchmark.
3. Three equal sections already clear the current 30% total-RMS improvement gate.
4. Four equal sections retain about 90% of the continuous-map RMS improvement.
5. Equal-section depth levels are themselves equally spaced, giving simple geometric targets.
6. The exact relation `R_N=4A-3D_N` ties forward discretization improvement to stronger reverse anti-matching.
7. Several-picosecond weighted section-mean mismatch can be tolerated at the current residual floor.
8. Nonuniform Lloyd-Max boundary optimization produces only a small additional benefit for `N=3-4`.

**NOT ESTABLISHED:**

- that a real optical stack/waveguide can localize absorption near the required three or four transverse depths with `~100 nm` conditional RMS;
- that adjacent depth states can be switched with acceptably low scattering/reflection/loss;
- that the required section absorption probabilities remain close to the assumed exponential law once the mode is moved in depth;
- that heterointerface transport and avalanche mean delay are section independent;
- that a three- or four-section semiconductor structure is manufacturable with acceptable PDE, DCR, capacitance, and breakdown uniformity;
- novelty or priority.

---

## 12. Decision and next hard step

The discrete implementation test does **not** kill the experiment. It makes the next question more concrete.

A continuously migrated optical mode is no longer required as the first implementation target. The simplest meaningful Maxwell problem is now a **three- or four-state transverse mode staircase**.

The next hard step should construct the smallest physically credible coupled-waveguide or multilayer mode model that can produce approximately

```text
N=3 target depths: 0.29, 0.96, 1.62 um over 1-mm sections
```

or

```text
N=4 target depths: 0.23, 0.73, 1.23, 1.73 um over 0.75-mm sections,
```

while maintaining high absorption and `~100 nm` conditional depth localization.

Before full 3-D electromagnetic work, use a coupled-mode/eigenmode surrogate to test whether three/four localized transverse absorbing states and low-loss transitions are physically plausible. Kill the realization if mode localization necessarily becomes much broader than the timing budget or if transition loss/reflection destroys useful PDE.

Do not claim novelty or begin manuscript construction.