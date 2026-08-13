# Progress Log — Experiment 02: Isochronous Avalanche Photodetector

**Date:** 2026-08-13

This log preserves the scientific path, prior-art narrowing, failed interpretations, and current frontier. Detailed step files remain authoritative for individual derivations.

## Step 1 — first-principles timing decomposition

Defined the timestamp as the sum of optical propagation, carrier transport, electrical propagation, avalanche mean delay, and residual stochastic terms. The law of total variance gives

```math
Var(T)=Var[m(X)]+E[Var(T|X)],
```

with exact removal of absorption-position mean-delay jitter when

```math
m(X)=constant.
```

For direct vertical propagation with constant optical and carrier velocities, exact cancellation would require `v_g=v_c`, which is physically unrealistic.

## Step 2 — optical path dilation / depth mapping

Introduced an optical coordinate that advances slowly through physical absorption depth. For constant velocities,

```math
d\bar z/dx=v_c/v_g,
```

or equivalently

```math
L=dv_g/v_c.
```

This trades random depth-dependent latency for a common calibratable latency.

## Step 3 — prior-art narrowing

A targeted journal/patent audit found that generic longitudinal timing compensation is too close to established traveling-wave velocity matching. The active hypothesis was narrowed to **transverse absorption-depth compensation**: deliberately map physical absorption depth onto optical propagation time to cancel carrier-to-avalanche transit delay.

No priority claim is authorized. Novelty remains unestablished.

## Step 4 — exact optimal delay map

For a Maxwell-derived joint absorption distribution `p(x,z)`, the variance-minimizing deterministic optical delay is

```math
d_opt(x)=C-E[t_c(Z)|X=x].
```

The irreducible deterministic residual is

```math
E_X[Var(t_c(Z)|X)].
```

This replaced the weaker idea that only the optical-mode centroid matters. The correct design target is the conditional mean carrier delay.

## Step 5 — residual-jitter floor

Added unresolved local absorption-depth width and drift-diffusion first-passage variance. For the 90%-absorption benchmark,

```math
sigma_depth^2/T0^2=0.0651549,
```

and

```math
sigma_floor^2/T0^2
=(sigma_perp/d)^2+1.35363/Pe+(sigma_other/T0)^2.
```

A 30% RMS improvement requires total residual variance no larger than `0.062600 T0^2`. This immediately kills strongly diffusion-dominated candidates such as the idealized `Pe=20` case.

## Step 6 — first realistic InGaAs/InP scale

Adopted a first scale estimate

```text
d=2 um
v_c=5e4 m/s
v_g=7.5e7 m/s
T0=40 ps
L=3 mm
```

for which the removable 90%-absorption depth term is about `10.2 ps RMS`.

## Step 7 — forward/reverse causal discriminant

For a full-depth matched map, ideal forward illumination removes the between-slice depth variance while reverse illumination doubles the deterministic timing slope. At 90% absorption,

```text
forward between-slice RMS = 0
ordinary depth RMS         = 0.2553 T0
reverse between-slice RMS  = 0.5105 T0
```

This established direction reversal as a stronger causal control than a simple optimized-device/control-device comparison.

## Step 8 — multiplication-region requirement

Recognized that the experiment is only useful when avalanche buildup, electronics, and other residual floors do not dominate the removable depth term. Thin/dead-space/localized low-buildup-jitter multiplication approaches are enabling prior art, not proposed novelty.

## Step 9 — first combined device surrogate

Added `REDUCED_ORDER_DEVICE_SURROGATE_2026-08-13.md` and `numerics/isochronous_device_surrogate.py`.

Stress-test point:

```text
Pe=100
sigma_perp=100 nm
avalanche RMS=5 ps
electronics RMS=2 ps
optical RMS=1 ps
```

Analytic and `N=1,000,000` event Monte Carlo results agree:

```text
direct depth-sensitive control ~12.65 ps RMS
forward matched                ~ 7.46 ps RMS
decorrelated same-marginal     ~16.26 ps RMS
reverse anti-matched           ~21.74 ps RMS
```

The forward/direct improvement is approximately `41.0%`, clearing the chosen 20–30% go gate.

At `Pe=100` with the same local-depth/electronics/optical assumptions, the 30% gate survives avalanche buildup up to about `8.34 ps RMS`.

### Important correction from this step

The earlier intuitive prediction that the **minimum total jitter** should occur exactly at the geometric mean-delay matching bias is too strong.

If carrier drift speed changes with bias while the photonic map is fixed, the deterministic depth slope is nulled at the design speed, but diffusion and local transport variance also change. In the present reduced-order model with locally constant `D`, the total-jitter minimum moves to

```math
v/v_0\approx1.2815,
```

while exact conditional-mean cancellation remains at `v/v0=1`.

Therefore the correct experimental prediction is:

```text
conditional-mean depth slope null -> geometric isochronous point
total-jitter minimum              -> model-dependent, can be shifted
forward/reverse asymmetry         -> strongest causal signature
```

This correction must be preserved in all later experiment designs.

## Current frontier

The concept has passed the first combined variance-budget test, but only in a restricted reduced-order parameter region. No Maxwell structure or TCAD transport solution has yet been demonstrated.

The next hard step is a **finite discrete optical-depth ladder**: approximate the exact continuous delay map using a small number of absorbing depth sections and explicit optical delay increments. Determine how many sections are needed and how much section depth/delay error can be tolerated before the 20–30% timing-improvement gate is lost.

Do not begin manuscript construction or claim novelty before this constructive implementation test and a continued prior-art audit.
