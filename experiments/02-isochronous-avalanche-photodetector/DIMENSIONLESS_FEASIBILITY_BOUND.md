# Dimensionless feasibility bound

**Date:** 2026-08-13
**Status:** EXACT BENCHMARK BOUND / GO-NO-GO TOOL

For the 90%-absorption benchmark, normalize time by

```math
T_0=d/v_c.
```

The removable between-slice depth variance is

```math
\boxed{\sigma_{depth}^2/T_0^2=0.0651549.}
```

The residual variance after perfect mean-delay compensation is approximated by

```math
\boxed{
\frac{\sigma_{floor}^2}{T_0^2}
=
\left(\frac{\sigma_\perp}{d}\right)^2
+rac{1.35363}{Pe}
+\left(\frac{\sigma_{other}}{T_0}\right)^2,
}
```

where:

- `sigma_perp` is unresolved local absorption-depth RMS;
- `Pe=v_c d/D` is the carrier Péclet number;
- `sigma_other` is the combined unrelated avalanche/electronics/optical timing floor.

The maximum ideal RMS improvement is

```math
\boxed{
I=1-
\sqrt{
\frac{\sigma_{floor}^2}
{\sigma_{floor}^2+\sigma_{depth}^2}
}.
}
```

For target improvement `I_target`, the maximum allowed total residual variance is

```math
\boxed{
\frac{\sigma_{floor}^2}{T_0^2}
\le
\frac{(1-I_{target})^2}
{1-(1-I_{target})^2}
\times0.0651549.
}
```

Numerically:

```text
20% RMS improvement -> residual variance/T0^2 <= 0.115831
30% RMS improvement -> <= 0.062600
50% RMS improvement -> <= 0.021718
```

Consequences:

1. `Pe=20` cannot reach 30% improvement even with zero local-depth width and zero unrelated jitter because diffusion alone contributes `1.35363/20=0.06768 > 0.06260`.
2. For `Pe=100` and `sigma_perp/d=0.05`, a 30% improvement remains possible provided

```math
\boxed{\sigma_{other}/T_0 \lesssim 0.216.}
```

3. For a `d=2 um`, `v_c=5e4 m/s` InGaAs scale, `T0=40 ps`, so the corresponding unrelated RMS floor is about `8.6 ps`.
4. The 20% criterion at the same `Pe=100`, `sigma_perp/d=0.05` permits `sigma_other/T0≈0.316`, or about `12.6 ps` RMS at `T0=40 ps`.

This bound should be evaluated before any detailed Maxwell/TCAD design. If a candidate operating point cannot satisfy the desired improvement threshold even under ideal mean-delay compensation, kill that device realization early.