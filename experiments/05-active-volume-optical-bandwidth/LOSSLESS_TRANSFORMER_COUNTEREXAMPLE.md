# Experiment 05 — lossless-transformer counterexample to a volume-only bandwidth bound

**Date:** 2026-08-13  
**Status:** STRONG COUNTEREXAMPLE / FIRST RESONANCE-VOLUME INVARIANT INVALIDATED AS GENERAL LAW / NOVELTY NOT ESTABLISHED

## 1. What is being tested

The first critical-coupling surrogate suggested

```math
NEP_{pk}^2/\Delta\omega=constant
```

when the active absorber volume `V` is reduced while the normalized optical mode is held fixed.

That conclusion is **not** universal because it fixes the optical impedance transformation implicitly.

The correct strong-comparator question is:

> If arbitrary passive lossless matching optics are allowed, does passivity/causality alone force optical bandwidth to collapse when the dark-generating semiconductor volume shrinks?

The answer is no in the following network model.

## 2. Extensive active-load model

Let a reference active semiconductor volume `V0` present an arbitrary causal passive optical-port admittance

```math
Y_0(\omega).
```

For a geometrically similar electrically/optically small active region in which the microscopic material response is unchanged and the port admittance is extensive, define

```math
s=V/V_0
```

and

```math
\boxed{Y_a(\omega;V)=sY_0(\omega).}
```

Then

```math
\boxed{Z_a(\omega;V)=Z_0(\omega)/s.}
```

This scales the entire impedance function, including resistance and reactance, by the same frequency-independent factor.

## 3. Lossless transformer

Insert a frequency-independent ideal lossless transformer between the external optical port and the active load. With the convention

```math
Z_{in}=n^2 Z_a,
```

choose

```math
\boxed{n^2=s.}
```

Then

```math
\boxed{
Z_{in}(\omega;V)
=s\,\frac{Z_0(\omega)}{s}
=Z_0(\omega).
}
```

Thus the external source sees exactly the same complex impedance at every frequency for every active volume `V`.

Consequences:

```text
reflection spectrum: unchanged
absorptance spectrum: unchanged
Bode-Fano matching difficulty: unchanged
active semiconductor volume: can decrease independently in this idealized family
```

Any passive matching network designed for the reference load can be retained after the transformer because the transformed load is identical to the reference load.

This counterexample works for an arbitrary dispersive `Z0(omega)`; it is not restricted to a pure resistor.

## 4. Parallel-RC example

For a simple extensive material admittance

```math
Y_a=V(g+j\omega c),
```

the equivalent parallel parameters are

```math
G=gV,
\qquad
C=cV,
\qquad
R=1/(gV).
```

Therefore

```math
\boxed{RC=c/g}
```

is independent of `V`.

The usual Bode-Fano difficulty of matching a parallel-RC load depends on this relaxation/reactance-to-loss scale, not on the absolute impedance magnitude. Shrinking `V` changes `R` and `C` inversely so the normalized matching problem is unchanged; a lossless impedance transformer restores the absolute level.

## 5. Physical resource that actually diverges

For a local linear dielectric absorber,

```math
P_{abs}
=\frac{\omega\epsilon_0}{2}
\int_V \operatorname{Im}\chi(\omega)|E|^2\,dV.
```

If the material is uniform and a fixed incident power is absorbed with fraction `eta`, then

```math
P_{abs}=\eta P_{in}.
```

Hence the volume-averaged internal field obeys

```math
\boxed{
\langle |E|^2\rangle_V
=\frac{2\eta P_{in}}
{\omega\epsilon_0\operatorname{Im}\chi\,V}
}
```

when `Im chi` is approximately uniform over the active region.

Therefore

```math
\boxed{E_{rms}\propto V^{-1/2}.}
```

The price of shrinking the active absorber at fixed optical absorption is diverging local field / dissipated power density, not necessarily vanishing spectral bandwidth.

A physical lower-volume bound appears only after another resource is constrained, e.g. maximum tolerable internal field, saturation carrier density, heating, nonlinear absorption, breakdown, finite transformer ratio, aperture/etendue, matching-network size/order, or fabrication limits.

For example, if `|E|<=E_max` everywhere, then

```math
\boxed{
V\ge
\frac{2\eta P_{in}}
{\omega\epsilon_0\operatorname{Im}\chi E_{max}^2}.
}
```

This is a dynamic-range/power-density bound, not a bandwidth-only bound.

## 6. Why the recent optical Bode-Fano result does not contradict this

Corsaro, Alu and Forestiere (arXiv:2606.24658, 2026) derive a rigorous Bode-Fano absorption-bandwidth limit for a **finite homogeneous absorbing object**. Their bound contains the radiation geometry parameter `C_{Omega,0}` of the entire object and assumes the material occupies the bounded domain `Omega`.

It therefore does not by itself bound a separately identified tiny dark-generating inclusion embedded behind an arbitrary larger lossless matching/collection structure.

The paper strengthens the conclusion that a resource must be specified: its right-hand side depends on the radiation geometry of the whole scatterer. It does not provide a lower bound on active semiconductor volume alone when the lossless optical transformer is treated as free.

## 7. Correction to the many-resonance argument

The earlier statement

```math
\sum_j\Delta\omega_j=4\kappa\sum_jV_j
```

was valid only when distinct resonances were assigned distinct absorber-volume resources.

It does **not** rule out multiple resonances that all reuse the same physical active region.

That shortcut is therefore rejected as a general volume-bandwidth proof.

## 8. Detector-noise consequence

If a bulk nonradiative dark-generation rate density `g_nr` gives

```math
G_{nr}=g_{nr}V,
```

then this component of dark-current shot noise can indeed shrink as `V` while the ideal matched optical absorptance remains fixed in the counterexample.

This does not imply unbounded total sensitivity. With fixed accepted optical modes, background-photon noise and external radiative detailed-balance contributions are controlled primarily by the absorptance of those modes rather than by active semiconductor volume. As `V -> 0`, the detector therefore approaches a volume-independent optical/radiative noise floor rather than zero total noise.

That crossover is established detector physics (background/radiative-limited operation), not a novelty claim.

## 9. Disposition

```text
universal passive bound: finite optical bandwidth -> minimum active semiconductor volume
    REJECTED without an additional matching/field/resource constraint

first critical-coupling NEP^2/bandwidth invariant
    RETAIN only for the fixed-mode single-resonance family

actual unavoidable resource in the ideal scaling counterexample
    local field / power density (and practical matching complexity)

next question
    formulate the detector tradeoff after explicitly constraining one real optical resource rather than treating lossless matching as free
```

Do not convert whole-object optical Bode-Fano bounds into active-volume dark-current bounds without explicit resource accounting.