# Reduced-order device surrogate — isochronous APD

**Date:** 2026-08-13  
**Status:** FIRST DEVICE-SURROGATE PASS / GO-GATE PASSED IN A RESTRICTED PARAMETER REGION / NOT MAXWELL OR TCAD / NOVELTY NOT ESTABLISHED

## 1. Purpose

The previous Experiment-02 steps established the exact conditional-mean delay criterion and analytic residual-jitter bounds. This step asks a harder question:

> Does the depth-compensation concept still produce a material total timing improvement after finite local absorption-depth width, drift-diffusion first-passage variance, avalanche buildup, optical pulse/dispersion, and electronics jitter are all present at once?

This is deliberately a **reduced-order Maxwell-to-transport surrogate**, not a full device simulation. The optical field is represented by a prescribed distributed-absorption coordinate and conditional depth map. Carrier transport is represented by constant-drift inverse-Gaussian first-passage statistics. The purpose is to test whether the concept survives a first realistic variance budget before investing in Maxwell/TCAD design.

The script is `numerics/isochronous_device_surrogate.py`.

## 2. Device scale and surrogate map

Use the existing first InGaAs/InP scale:

```text
absorber depth d              = 2.0 um
design carrier speed v0       = 5.0e4 m/s
optical group velocity vg     = 7.5e7 m/s
useful distributed absorption = 90%
```

Then

```math
T_0=d/v_0=40\ \mathrm{ps},
```

and exact full-depth delay matching requires

```math
L=dv_g/v_0=3.0\ \mathrm{mm}.
```

Let `U=X/L` be the detected-photon optical coordinate. For 90% exponentially distributed absorption,

```math
p(U)=\frac{b e^{-bU}}{1-e^{-b}},
\qquad
b=-\ln(0.1),
```

with

```math
E[U]=0.3231833708,
```

```math
\boxed{Var(U)=0.06515490689.}
```

The designed conditional mean absorption depth is

```math
\bar z(U)=dU.
```

Thus at the design velocity the forward deterministic mean timestamp is

```math
t_f(U)=UT_0+(1-U)T_0=T_0.
```

## 3. Residual stochastic terms

Use the first stress-test point

```text
unresolved local depth RMS sigma_perp = 100 nm = 0.05 d
carrier Peclet number Pe              = 100
avalanche buildup RMS                 = 5 ps
electronics/threshold RMS             = 2 ps
optical pulse/dispersion RMS          = 1 ps
```

The local-depth contribution is

```math
\sigma_\perp^2/T_0^2=(0.05)^2=0.0025.
```

With constant drift and first-passage diffusion,

```math
\frac{\sigma_{diff}^2}{T_0^2}
=\frac{2E[1-U]}{Pe}
=0.01353633258.
```

The remaining normalized contributions are

```text
avalanche   = 0.015625
electronics = 0.002500
optical     = 0.000625
```

so the complete post-compensation residual floor is

```math
\boxed{F\equiv\sigma_{floor}^2/T_0^2=0.03478633258.}
```

Therefore

```math
\boxed{\sigma_{floor}=7.4604\ \mathrm{ps\ RMS}.}
```

## 4. Four physically distinct controls

The earlier toy Monte Carlo mainly compared one mapped carrier-depth distribution with and without an imposed optical-delay term. This step makes the controls more explicit.

### A. Direct / unmapped depth-sensitive detector

There is no compensating longitudinal optical delay. The ordinary between-slice depth variance remains:

```math
\frac{\sigma_{direct}^2}{T_0^2}=F+Var(U).
```

Hence

```math
\boxed{\sigma_{direct}=12.6454\ \mathrm{ps\ RMS}.}
```

### B. Forward matched depth map

At the design point the between-slice conditional mean is exactly constant, so

```math
\frac{\sigma_f^2}{T_0^2}=F,
```

and

```math
\boxed{\sigma_f=7.4604\ \mathrm{ps\ RMS}.}
```

The total RMS reduction relative to the direct depth-sensitive detector is

```math
\boxed{1-\sigma_f/\sigma_{direct}=41.00\%.}
```

This clears the previously selected 20–30% practical go/no-go range.

### C. Decorrelated traveling-wave control

Keep the same optical-delay distribution and the same carrier-depth distribution, but destroy their correlation. The two between-slice variances then add:

```math
\frac{\sigma_{decorr}^2}{T_0^2}=F+2Var(U),
```

so

```math
\boxed{\sigma_{decorr}=16.2528\ \mathrm{ps\ RMS}.}
```

This control isolates the benefit of the **correlation itself**, rather than merely comparing a waveguide device against a direct-illumination device.

### D. Reverse illumination

For reverse propagation through the same fixed depth map,

```math
t_r(U)=2T_0(1-U),
```

so

```math
\frac{\sigma_r^2}{T_0^2}=F+4Var(U),
```

and

```math
\boxed{\sigma_r=21.7405\ \mathrm{ps\ RMS}.}
```

Thus the same structure predicts a large direction-odd timing signature:

```text
forward matched      7.46 ps RMS
direct depth control 12.65 ps RMS
decorrelated control 16.25 ps RMS
reverse anti-match   21.74 ps RMS
```

## 5. Monte Carlo verification

A `N=1,000,000` event simulation used inverse-Gaussian first-passage times with

```math
E[t|\ell]=\ell/v_0,
\qquad
Var(t|\ell)=2D\ell/v_0^3,
```

plus the local-depth, avalanche, electronics, and optical terms above.

Results:

```text
analytic direct       12.6454 ps
Monte Carlo direct    12.6502 ps

analytic forward       7.4604 ps
Monte Carlo forward    7.4644 ps

analytic decorrelated 16.2528 ps
Monte Carlo           16.2655 ps

analytic reverse      21.7405 ps
Monte Carlo reverse   21.7444 ps
```

The direct-to-forward Monte Carlo reduction is `40.994%`, so the simulation agrees with the variance decomposition to well below 0.1 ps at this sample count.

## 6. Avalanche budget versus transport quality

For a target 30% RMS improvement relative to the direct depth-sensitive control, at fixed

```text
sigma_perp = 100 nm
electronics RMS = 2 ps
optical RMS = 1 ps
```

the maximum allowed avalanche-build-up RMS is:

| `Pe` | maximum avalanche RMS for >=30% improvement |
|---:|---:|
| 20 | impossible even at zero avalanche jitter |
| 30 | 4.35 ps |
| 50 | 6.92 ps |
| 75 | 7.89 ps |
| 100 | 8.34 ps |
| 150 | 8.76 ps |
| 200 | 8.96 ps |
| 300 | 9.16 ps |

This sharpens the multiplication-region requirement. At the present `Pe=100` scale, avalanche buildup can be several picoseconds and the concept can still clear 30%, but an approximately 10-ps avalanche RMS already pushes the total improvement below 30%.

The concept is therefore not restricted to a zero-avalanche-jitter idealization, but it does require a multiplication/readout architecture substantially cleaner than the removable depth term.

## 7. Important refinement — exact mean-delay matching is not generally the minimum-total-jitter bias

The fixed photonic map is designed for `v=v0`. Let

```math
r=v/v_0.
```

Assume for this local bias sweep that the diffusion coefficient `D` is approximately fixed. Then the forward normalized variance is

```math
\boxed{
V_f(r)=
A\left(1-\frac1r\right)^2
+\frac{a}{r^2}
+\frac{\beta}{r^3}
+c,
}
```

where

```math
A=Var(U),
\qquad
a=(\sigma_\perp/d)^2,
\qquad
\beta=2E[1-U]/Pe_0,
```

and `c` contains the approximately bias-independent avalanche/electronics/optical floors.

The **deterministic conditional-mean cancellation** is exactly at `r=1`.

But minimizing the complete variance gives, with `s=1/r`,

```math
3\beta s^2+2(A+a)s-2A=0.
```

Hence

```math
\boxed{
s_*=
\frac{-(A+a)+\sqrt{(A+a)^2+6A\beta}}{3\beta},
\qquad
r_*=1/s_*.
}
```

For the present parameter point,

```math
\boxed{r_*=1.28154.}
```

Numerically,

```text
exact deterministic match r=1.000 -> 7.460 ps RMS
total-jitter minimum r=1.282       -> 6.911 ps RMS
```

The reason is physical: increasing drift velocity away from the exact geometric match introduces a small deterministic mismatch while simultaneously reducing local-depth transit spread and diffusion variance.

### Consequence for the proposed bias-tuning experiment

The earlier statement

```text
bias tuning should place the total timing minimum exactly at the geometric isochronous point
```

is too strong and is now **REJECTED**.

The correct prediction is:

```text
1. the conditional-mean depth slope is nulled at the geometric match;
2. the total RMS timing minimum can be shifted because residual stochastic transport terms are field dependent;
3. forward/reverse asymmetry remains the stronger causal discriminator.
```

A realistic TCAD/Monte Carlo model must therefore predict the field dependence of both the conditional mean and the conditional variance before assigning the minimum-jitter bias.

## 8. Mapping-mismatch tolerance

Let `q` multiply the designed optical-delay/depth-compensation coefficient. At the design carrier velocity,

```math
\frac{\sigma_f^2(q)}{T_0^2}=F+A(q-1)^2.
```

For the present parameter point, the maximum `|q-1|` consistent with the specified total improvement is

```text
>=20% RMS improvement -> |q-1| <= 0.669
>=30% RMS improvement -> |q-1| <= 0.467
>=40% RMS improvement -> |q-1| <= 0.135
```

Thus the 30% feasibility gate is not hypersensitive to modest slope error. Approaching the maximum approximately 41% improvement does require substantially tighter matching.

This is encouraging for a first fabricated demonstrator: the concept does not require sub-percent photonic-delay accuracy merely to produce a visible timing effect.

## 9. What has actually been established

**DERIVED / NUMERICALLY VALIDATED:**

1. A first combined device-level variance budget clears the 30% RMS-improvement gate at a plausible InGaAs/InP scale under `Pe=100`, 100-nm local-depth RMS, and 5-ps avalanche RMS.
2. The predicted forward/reverse contrast remains large after common stochastic floors are included.
3. A decorrelated same-marginal control is substantially broader than the correlated forward device, isolating the role of optical-depth timing correlation.
4. At `Pe=100`, the 30% gate survives avalanche buildup up to about `8.34 ps RMS` under the other stated assumptions.
5. The exact conditional-mean isochronous point need not coincide with the minimum-total-jitter operating point once field-dependent residual transport is retained.

**NOT ESTABLISHED:**

- that a real Maxwell structure can realize the required `p(x,z)` with 100-nm conditional depth RMS and acceptable optical loss;
- that a specific InGaAs/InP multiplication region provides <=8 ps avalanche buildup RMS at the required PDE and bias;
- that `D` is locally field independent;
- that heterointerface transport, trapping, tunneling, dark count, and electrical propagation remain negligible;
- novelty or priority.

## 10. Next hard step

The analytic surrogate is now strong enough that another generic timing derivation would add little.

The next useful step is to replace the prescribed depth map by a **constructive discrete optical-depth ladder** that approximates

```math
d_{opt}(x)=C-E[t_c(Z)|X=x]
```

with a finite number of absorbing sections and explicit delay increments.

That step should answer two practical questions before any full electromagnetic simulation:

1. how many independently localized depth sections are required to retain most of the continuous-map timing benefit;
2. how much section-to-section depth and optical-delay error can be tolerated before the forward/reverse signature falls below the 20–30% gate.

If a small discrete ladder cannot preserve the effect, a continuously migrated optical mode is likely to be fabrication-sensitive and the experiment should be reconsidered before full Maxwell/TCAD work.
