# Optical depth-mapping implementation

**Date:** 2026-08-13
**Status:** CONCEPTUAL IMPLEMENTATION / NOT YET DEVICE-SIMULATED

## 1. Active concept

The distinct Experiment-02 implementation is no longer generic longitudinal traveling-wave matching.

Use an optically thick/depleted APD absorption region with avalanche-trigger region at one side. As light propagates along a waveguide coordinate `x`, deliberately shift the **conditional mean physical absorption depth** `z_bar(x)` toward the avalanche region.

For constant optical group velocity `v_g` and carrier drift speed `v_c`,

```math
t_mean(x)=x/v_g+[d-z_bar(x)]/v_c.
```

Exact depth isochrony requires

```math
\boxed{dz_bar/dx=v_c/v_g.}
```

Thus the optical mode moves through physical depth slowly enough that each increment of optical propagation delay is compensated by an equal decrement in carrier transit time.

## 2. General field-dependent form

Let the mean carrier transit from depth `z` be

```math
t_c(z)=\int_z^d dz'/v_c(z').
```

Then exact compensation is

```math
\frac{dt_o}{dx}
+\frac{dt_c}{dz}\frac{dz_bar}{dx}=0.
```

Since

```math
dt_o/dx=1/v_g(x),
```

and

```math
dt_c/dz=-1/v_c(z),
```

the required depth map obeys

```math
\boxed{
\frac{dz_bar}{dx}=\frac{v_c[z_bar(x)]}{v_g(x)}.
}
```

Equivalently, parameterized by optical propagation time,

```math
\boxed{
\frac{dz_bar}{dt_o}=v_c[z_bar].
}
```

This is a useful physical statement: the designed mean absorption depth must advance toward the avalanche region at the same speed that the triggering carrier would drift through that depth, when both are measured on the event clock.

## 3. Required optical length

For constant velocities and total compensated depth range `d`,

```math
\boxed{L=d v_g/v_c.}
```

With `v_g/v_c ~ 10^3`, each micrometer of compensated carrier-depth range costs roughly a millimeter of optical propagation.

This makes the concept most plausible for micrometer-scale depleted absorbers, not tens-of-micrometers bulk drift regions.

## 4. Candidate photonic implementations

The mathematics does not require a literal ray at a grazing angle. Possible implementations are:

1. **adiabatic vertical mode migration:** a slowly varying multi-layer waveguide moves the optical mode center through the absorber depth;
2. **coupled-waveguide supermode control:** longitudinally vary coupling/index so the absorbing supermode gradually shifts from one side of a thick active region toward the multiplication side;
3. **discrete depth ladder:** several thin absorbing sections at different carrier distances are visited sequentially with optical delays chosen to approximate the continuous isochronous map.

Published 3-D silicon-photonics systems have demonstrated adiabatic vertical optical-mode transfer over several micrometers on sub-millimeter scales, so the required slow mode motion is not obviously forbidden. Controlled absorption localization while the mode migrates remains the key unsolved implementation issue.

## 5. Finite optical-mode width

Write actual absorption depth

```math
Z=z_bar(x)+delta_z.
```

The component `delta_z` is not correlated with optical propagation delay. Its timing floor is approximately

```math
\boxed{sigma_perp/v_c.}
```

For `v_c=1e5 m/s`:

```text
50 nm RMS depth uncertainty  -> 0.5 ps
100 nm RMS                   -> 1 ps
250 nm RMS                   -> 2.5 ps
```

This is a central fabrication/optical-confinement requirement.

## 6. Latency-spread trade

Exact compensation does not make the slowest carrier arrive earlier. It delays the optically early/short-transit events so all conditional mean timestamps equal the maximum uncompensated carrier delay.

For the simple geometry,

```math
\boxed{t_iso=d/v_c.}
```

Thus the concept trades event-to-event latency spread for a fixed calibratable latency.

For time-of-flight or coincidence measurements, a fixed offset can be calibrated; random jitter cannot.

## 7. Go/no-go quantities for a real design

A credible implementation must provide:

- a computed `z_bar(x)` from Maxwell simulation;
- conditional absorption-depth variance `sigma_perp^2(x)`;
- carrier first-passage statistics from drift-diffusion/Monte Carlo transport;
- avalanche-build-up timing statistics;
- useful absorption/PDE over the full device;
- parasitic optical loss and dispersion;
- electrical readout propagation or a geometry that removes it.

No manuscript work is authorized before these are at least numerically stress-tested.