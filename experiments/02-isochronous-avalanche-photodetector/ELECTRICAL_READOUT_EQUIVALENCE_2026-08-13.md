# Electrical-readout equivalence and traveling-wave escape route

**Date:** 2026-08-13  
**Status:** ARCHITECTURE FORK / SEGMENTED-READOUT REDUNDANCY DERIVED / NOVELTY NOT ESTABLISHED

## Exact segmented-readout equivalence

Let `J` be an observed detector section and `T` the raw timestamp.

```math
Var(T)=Var(E[T|J])+E[Var(T|J)].
```

If the fired section is known, define

```math
T_corr=T-E[T|J]+C.
```

Then

```math
\boxed{Var(T_corr)=E[Var(T|J)].}
```

This is exactly the variance floor obtained by adding an ideal deterministic physical delay

```math
d_opt(J)=C-E[T|J].
```

Therefore an independently read out three-section detector is **not** a clean demonstration of passive isochronous timing: the section label supplies the coordinate needed to calibrate away the same between-section mean delay electronically.

The optical localization may still reduce within-section depth spread, but the optical delay increments are redundant for mean-delay equalization if section identity is perfectly observed.

Any segmented implementation must therefore be compared against a segmented-and-calibrated control.

## Lumped capacitance warning

A simple scale estimate

```math
C_j ~= eps0 eps_r w L / W_d
```

with assumed `eps_r=13`, `W_d=2 um`, and `L=3 mm` gives:

| stripe width | Cj | 50-ohm RC |
|---:|---:|---:|
| 0.5 um | 86 fF | 4.32 ps |
| 1.0 um | 173 fF | 8.63 ps |
| 2.0 um | 345 fF | 17.3 ps |
| 5.0 um | 863 fF | 43.2 ps |

These are **not jitter predictions**. They show only that the earlier independent `2 ps electronics RMS` assumption cannot be retained for a millimeter-scale common junction without an explicit readout model.

Three electrical segments reduce each segment capacitance by about three, but expose `J` and trigger the calibration equivalence above.

## Electrical propagation changes the depth map

For forward optical propagation,

```math
m_f(x)=x/v_g+[d-z(x)]/v_c+t_e(x)+mu_a(x).
```

Ignoring an avalanche-mean gradient,

```math
\boxed{
dz/dx=v_c[1/v_g+dt_e/dx].
}
```

So deterministic electrical propagation is part of the isochronous design, not merely extra noise.

### Common output at the optical input end

If the electrical pulse propagates back to `x=0`,

```math
t_e=x/v_e,
```

then

```math
L_near
=
d/[v_c(1/v_g+1/v_e)]
=
L0/[1+v_g/v_e],
```

with `L0=3 mm`.

Examples:

```text
v_e -> infinity : 3.0 mm
v_e = 4 v_g     : 2.4 mm
v_e = 2 v_g     : 2.0 mm
v_e = 1.5 v_g   : 1.8 mm
v_e = v_g       : 1.5 mm
```

Thus electrical propagation toward the input end **assists** the optical delay gradient and can reduce active length.

### Common output at the far end

If

```math
t_e=(L-x)/v_e,
```

then

```math
L_far=L0/[1-v_g/v_e]
```

for `v_e>v_g`, so the device becomes longer:

```text
v_e = 4 v_g   : 4 mm
v_e = 2 v_g   : 6 mm
v_e = 1.5 v_g : 9 mm
```

The output direction is therefore a first-order design variable.

## Direction reversal survives electrical propagation exactly

Reverse only the optical direction while keeping the same depth map and electrical readout:

```math
m_r(x)=(L-x)/v_g+[d-z(x)]/v_c+t_e(x)+mu_a(x).
```

If the forward device is matched (`dm_f/dx=0`), then

```math
\boxed{dm_r/dx=-2/v_g.}
```

The deterministic electrical-delay gradient cancels from this result.

So the forward/reverse causal signature survives distributed electrical propagation exactly.

## Architecture fork

The device now has three branches:

```text
1. lumped common output
   + preserves passive-isocrony meaning
   - risks large lumped capacitance

2. segmented independent outputs
   + lower per-channel capacitance
   - section identity makes mean-delay optical compensation electronically redundant

3. traveling-wave common output
   + can distribute capacitance instead of lumping it
   + preserves a common timing output
   + electrical propagation can assist the depth map
   - Geiger-mode avalanche/quenching physics remains unresolved
```

Traveling-wave photodetectors are established enabling prior art, including periodic multi-diode devices on coplanar transmission lines and traveling-wave avalanche-photodetector designs. This is not a novelty claim.

## Current disposition

The strongest implementation path is now a **single-output distributed/traveling-wave APD/SPAD**, not electrically independent three-section SPADs.

The next surrogate must compare on equal footing:

1. lumped common-output isochronous detector;
2. segmented independently calibrated detector;
3. traveling-wave common-output isochronous detector.

If the segmented calibrated detector achieves the same timing with lower resource cost, the discrete optical-delay implementation loses its practical reason to exist. If the traveling-wave common-output version preserves the timing benefit without excessive avalanche/readout jitter, it becomes the leading device architecture.

Do not proceed to full Maxwell geometry until this comparison is made.
