# Forward/reverse timing contrast with distributed absorption

**Date:** 2026-08-13
**Status:** EXACT IDEALIZED CONTROL RESULT

Use the full-depth linear map

```math
z_bar(x)=d x/L,
\qquad
L=d v_g/v_c,
```

and total useful absorption `eta` distributed exponentially along optical path.

For forward illumination, the detected-photon coordinate has

```math
p_f(x)=a exp(-a x)/(1-exp(-aL)).
```

At the matched slope,

```math
t_f(x)=x/v_g+[d-z_bar(x)]/v_c=d/v_c=T0,
```

so the ideal between-slice timing variance is zero.

For reverse illumination from `x=L`,

```math
p_r(x)=a exp[-a(L-x)]/(1-exp(-aL)),
```

and

```math
t_r(x)=(L-x)/v_g+[d-z_bar(x)]/v_c
=2T0(1-x/L).
```

Because `1-x/L` under `p_r` has the same truncated-exponential statistics as `x/L` under `p_f`, the reverse deterministic RMS is

```math
\boxed{
sigma_reverse=2 sigma_u T0,
}
```

where `sigma_u` is the normalized coordinate RMS.

For `eta=0.90`,

```math
sigma_u=0.2552546,
```

so

```math
\boxed{
sigma_reverse=0.510509 T0.}
```

The ordinary uncompensated carrier-depth term is

```math
sigma_depth=0.255255 T0.
```

Thus, in this ideal distributed model:

```text
forward matched between-slice RMS = 0
ordinary unmapped depth RMS       = 0.2553 T0
reverse anti-matched RMS          = 0.5105 T0
```

For `T0=40 ps`, these are approximately

```text
0 ps, 10.2 ps, 20.4 ps RMS
```

before common within-slice, diffusion, avalanche, optical-dispersion, and electronics floors are added.

This shows that Beer-Lambert attenuation does not automatically erase the forward/reverse causal signature in the ideal full-depth mapping model. A realistic Maxwell model must still compute the two direction-dependent joint distributions `p_f(x,z)` and `p_r(x,z)`.