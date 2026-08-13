# First realistic target scale: InGaAs/InP separate-absorption SPAD/APD

**Date:** 2026-08-13
**Status:** FIRST REALISTIC SCALE / NOT A FINAL DEVICE DESIGN

## Why InGaAs/InP is the first target

A modern InGaAs/InP SPAD architecture uses an approximately 2-um intrinsic InGaAs absorption layer, with the photogenerated hole injected into the InP multiplication layer. This is a useful scale because the absorption region is thick enough that carrier-depth transit can contribute several to ~10 ps RMS, unlike ultrathin few-hundred-nanometer Ge/Si waveguide APDs where the transverse depth term is intrinsically much smaller.

Relevant primary example:

- *Nature Communications* 14, 8044 (2023), DOI 10.1038/s41467-023-43341-9: intrinsic InGaAs absorption layer thickness 2 um; photogenerated hole triggers multiplication in InP.

Older high-speed InGaAs APD design models commonly use hole saturation velocity around

```text
v_h ~ 5e6 cm/s = 5e4 m/s
```

in the depleted absorber. Treat this only as a scale estimate; the actual field-dependent carrier first-passage distribution must come from the selected epistructure and operating field.

## Timing scale

For the 90%-absorption benchmark used in the analytic model,

```math
sigma_depth = 0.25525 d/v_c.
```

At

```text
d = 2 um
v_c = 5e4 m/s
```

this gives

```text
full carrier-depth delay range d/v_c = 40 ps
removable deterministic depth term  = 10.21 ps RMS
```

This is large enough to be interesting in a low-jitter detector if avalanche/electronics and diffusion are well controlled.

## Optical delay scale

Exact constant-velocity depth mapping requires

```math
L = d v_g/v_c.
```

For illustrative optical group velocity

```text
v_g = 7.5e7 m/s
```

```text
L = 3.0 mm
optical group-delay span = 40 ps
```

The required mean-depth slope is

```math
d z_bar/dx = v_c/v_g = 6.67e-4,
```

i.e. the mean absorption depth moves by 2 um over 3 mm of optical propagation.

## Why this is only a scale estimate

A credible InGaAs design must still determine:

1. actual field-dependent hole drift and diffusion/first-passage statistics;
2. heterointerface trapping/detrapping at the grading/charge transition;
3. avalanche-build-up jitter in the multiplication region;
4. a Maxwell structure capable of moving the conditional absorption-depth distribution through the absorber while retaining high PDE;
5. dark count and tunneling consequences of the required field profile;
6. electrical propagation/readout timing.

The next numerical stage should use the exact conditional-delay criterion

```math
d_opt(x)=C-E[t_c(Z)|X=x]
```

rather than assuming a linear depth centroid.