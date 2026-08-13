# Residual jitter floor after mean-depth compensation

**Date:** 2026-08-13
**Status:** FIRST MICROSCOPIC FEASIBILITY TEST

## 1. What compensation can and cannot cancel

Let optical propagation coordinate be `X`. The optical structure is designed so the mean absorption depth `z_bar(X)` satisfies the isochronous condition. Write the actual absorption depth as

```math
Z=z_bar(X)+delta_z,
```

with

```math
E[delta_z|X]=0,
qquad
Var(delta_z|X)=sigma_perp^2(X).
```

Exact mean-depth compensation removes the timing variation associated with `z_bar(X)`. It does not remove the residual transverse absorption coordinate `delta_z`.

For constant carrier drift velocity `v_c`, this contributes

```math
\boxed{
Var_perp(T)=E[sigma_perp^2(X)]/v_c^2.
}
```

Thus 100 nm RMS unresolved absorption depth corresponds to 1 ps RMS timing at `v_c=1e5 m/s`.

## 2. Drift-diffusion first-passage floor

Model the triggering carrier over remaining path length `ell` by

```math
dY=v_c dt+sqrt(2D)dW,
```

with absorbing boundary at distance `ell`.

The first-passage time has

```math
E[t|ell]=ell/v_c,
```

```math
\boxed{
Var(t|ell)=2D ell/v_c^3.
}
```

Optical compensation can remove the position dependence of the conditional mean `ell/v_c`, but not this conditional stochastic variance.

Averaging over detected photons gives

```math
\boxed{
sigma_diff^2=2D E[ell]/v_c^3.
}
```

This is a lower-level transport floor that remains even for perfect deterministic isochrony.

## 3. Exponential distributed-absorption benchmark

Let optical absorption along the depth-mapping propagation length `L` be

```math
p(x)=a exp(-a x)/(1-exp(-a L)),
```

and map mean depth linearly:

```math
z_bar=d x/L.
```

Define

```math
b=aL=-ln(1-eta),
```

where `eta` is total useful absorption.

Then

```math
E[x/L]=1/b-1/(exp(b)-1),
```

```math
Var(x/L)=1/b^2-exp(b)/(exp(b)-1)^2.
```

The mean remaining carrier path is

```math
E[ell]/d
=1-1/b+1/(exp(b)-1).
```

Without compensation, the deterministic mapped-depth timing variance is

```math
sigma_depth^2
= d^2 Var(x/L)/v_c^2.
```

Define a carrier transport Péclet number

```math
Pe=v_c d/D.
```

Then

```math
\boxed{
\frac{sigma_diff^2}{sigma_depth^2}
=
\frac{2[E(ell)/d]}{Var(x/L)}\frac1{Pe}.
}
```

For `eta=0.90`:

```text
E[ell]/d       = 0.6768
Var(x/L)       = 0.0651
sigma_diff^2 / sigma_depth^2 ≈ 20.8/Pe
```

Hence:

```text
Pe = 20  -> diffusion variance ≈ 1.04 x removable depth variance
Pe = 50  -> diffusion RMS ≈ 0.645 x removable depth RMS
Pe = 100 -> diffusion RMS ≈ 0.456 x removable depth RMS
Pe = 200 -> diffusion RMS ≈ 0.322 x removable depth RMS
```

This is a hard feasibility criterion. The concept is unattractive in a strongly diffusion-dominated absorber even if the mean delay can be perfectly compensated.

## 4. Combined residual timing floor

To leading order, after exact mean-depth compensation,

```math
\boxed{
sigma_T^2
\simeq
\frac{E[sigma_perp^2]}{v_c^2}
+rac{2D E[ell]}{v_c^3}
+E[sigma_a^2|X]
+sigma_e^2
+sigma_opt^2
+\cdots
}
```

where the remaining terms include stochastic avalanche buildup, electronics/threshold jitter, optical pulse width and dispersion, and other conditional transport fluctuations.

The experiment is only useful if the removed mapped-depth variance is comparable to or larger than these surviving terms.

## 5. Immediate kill test

Before any detailed device proposal, estimate on a candidate material/field profile:

1. `v_c`;
2. longitudinal `D` or full first-passage distribution;
3. active depth `d`;
4. achievable unresolved transverse absorption width `sigma_perp`;
5. avalanche-build-up jitter.

If `Pe` is too small or `sigma_perp/v_c` already dominates, optical mean-depth compensation has little practical value.