# First-principles derivation

## 1. General variance identity

Let `X` denote the random absorption position. Let the detector timestamp be

```math
T=t_o(X)+t_c(X)+t_e(X)+A(X)+E,
```

where `A` is avalanche-build-up delay and `E` contains position-independent electronics timing noise.

Write

```math
\mu_a(X)=E[A|X]
```

and

```math
m(X)=t_o(X)+t_c(X)+t_e(X)+\mu_a(X).
```

The law of total variance gives

```math
\boxed{
Var(T)=Var[m(X)]+E[Var(T|X)].
}
```

The first term is the timing spread created by random absorption position through the position-dependent mean delay. It vanishes exactly if `m(X)` is constant on the detected-photon support.

Thus the exact isochronous condition is

```math
\boxed{t_o(X)+t_c(X)+t_e(X)+\mu_a(X)=constant.}
```

For a smooth scalar coordinate `x`, the local condition is

```math
\boxed{
\frac{d}{dx}[t_o+t_c+t_e+\mu_a]=0.
}
```

## 2. Direct vertical illumination

Let absorber depth be `z in [0,d]`, avalanche triggering region be at `z=d`, optical group velocity be `v_g`, and carrier drift velocity be `v_c`.

Ignoring position dependence of avalanche and readout delay,

```math
t(z)=\frac{z}{v_g}+\frac{d-z}{v_c}.
```

Therefore

```math
\frac{dt}{dz}=\frac1{v_g}-\frac1{v_c}.
```

Exact depth-jitter cancellation requires

```math
\boxed{v_g=v_c.}
```

Ordinary optical propagation is much faster than carrier drift, so direct incidence is far from this condition.

## 3. Optical path dilation

Let optical path coordinate `s` advance through physical depth at angle `theta`:

```math
z=s\sin\theta.
```

Then

```math
t(z)=\frac{z}{v_g\sin\theta}+\frac{d-z}{v_c}.
```

Define

```math
q=\frac{v_c}{v_g\sin\theta}.
```

Then

```math
\frac{dt}{dz}=\frac{q-1}{v_c}.
```

Hence

```math
\boxed{\sin\theta_*=v_c/v_g}
```

makes `q=1` and

```math
\boxed{t(z)=d/v_c}
```

for every absorption depth.

The design removes deterministic depth spread but does not reduce the common mean latency.

If the absorption-depth standard deviation is `sigma_z`, the residual position jitter in the constant-velocity model is

```math
\boxed{
\sigma_{pos}=|q-1|\frac{\sigma_z}{v_c}.
}
```

Thus a 10% mismatch in the compensation coefficient leaves 10% of the original carrier-depth jitter.

## 4. Arbitrary field profile

For field-dependent carrier speed,

```math
t_c(z)=\int_z^d\frac{dz'}{v_c(z')},
```

so

```math
\frac{dt_c}{dz}=-\frac1{v_c(z)}.
```

If the optical path is `s(z)` with local group velocity `v_g(z)`, then

```math
\frac{dt_o}{dz}=\frac1{v_g(z)}\frac{ds}{dz}.
```

The general first-order isochronous condition is therefore

```math
\boxed{
\frac1{v_g(z)}\frac{ds}{dz}
+\frac{dt_e}{dz}
+\frac{d\mu_a}{dz}
=\frac1{v_c(z)}.
}
```

If readout and avalanche mean delay are spatially uniform, this reduces to

```math
\boxed{\frac{ds}{dz}=\frac{v_g(z)}{v_c(z)}.}
```

## 5. Truncated exponential absorption

For effective absorption coefficient `alpha` over physical coordinate `0<z<d`, conditioned on detection within the region,

```math
p(z)=\frac{\alpha e^{-\alpha z}}{1-e^{-\alpha d}}.
```

The mean and variance are

```math
E[z]=\frac1\alpha-\frac{d}{e^{\alpha d}-1},
```

```math
\boxed{
Var(z)=\frac1{\alpha^2}
-\frac{d^2e^{\alpha d}}{(e^{\alpha d}-1)^2}.
}
```

Hence, in the simple linear mismatch model,

```math
\boxed{
Var_{pos}(T)=
\left(\frac{q-1}{v_c}\right)^2
\left[
\frac1{\alpha^2}-\frac{d^2e^{\alpha d}}{(e^{\alpha d}-1)^2}
\right].
}
```

At `q=1`, this contribution is exactly zero for any absorption distribution, not merely the exponential one.

## 6. Residual irreducible terms

Exact position compensation does not imply zero detector jitter. At the isochronous condition,

```math
Var(T)=E[Var(T|X)].
```

This retains, among other effects:

- stochastic avalanche-build-up time;
- carrier scattering and diffusion about the mean drift time;
- finite transverse extent of the optical absorption distribution;
- electronics and threshold noise;
- optical pulse-width and dispersion contributions;
- any spatial variation of trigger probability or avalanche statistics not included in the designed mean delay.

This experiment therefore proposes a way to remove one identifiable jitter term, not a zero-jitter photodetector.