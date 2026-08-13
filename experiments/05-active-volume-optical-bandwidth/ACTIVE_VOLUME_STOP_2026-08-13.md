# Experiment 05 — active-volume / optical-bandwidth stop

**Date:** 2026-08-13  
**Status:** NEGATIVE RESULT / UNIVERSAL VOLUME-BANDWIDTH CLAIM CLOSED / RESOURCE ACCOUNTING RETAINED / NOVELTY NOT ESTABLISHED

## Original question

Can the dark-generating semiconductor volume approach zero while a passive detector retains high absorptance over a fixed nonzero optical bandwidth?

A fixed-mode, critically coupled resonance initially suggested a direct bandwidth cost. That implication does **not** survive the strongest allowed comparator.

## Decisive counterexample

For an extensive active load,

```math
Y_a(\omega;V)=sY_0(\omega),
\qquad s=V/V_0,
```

so

```math
Z_a(\omega;V)=Z_0(\omega)/s.
```

A lossless ideal transformer with

```math
n^2=s
```

gives

```math
Z_{in}=n^2Z_a=Z_0(\omega).
```

Thus the external reflection and absorptance spectrum can remain identical as active volume shrinks. This is true for an arbitrary dispersive reference impedance; volume rescales the whole impedance rather than changing its normalized frequency dependence.

For a parallel extensive `RC` model,

```math
R\propto1/V,
\qquad C\propto V,
\qquad RC=constant,
```

so the normalized Bode-Fano matching difficulty is volume independent. A lossless impedance transformer restores the absolute impedance level.

Therefore passivity/causality alone do not imply

```text
fixed finite optical bandwidth -> nonzero minimum active semiconductor volume
```

when arbitrary lossless optical matching is a free resource.

## Correction to the first resonance argument

The single-resonance result

```math
NEP_{pk}^2/\Delta\omega=constant
```

is valid only for the restricted family in which the normalized optical mode is held fixed and `gamma_i=kappa V`.

It is not a universal detector invariant.

Likewise, assigning separate absorber volume to each resonance was an invalid general argument against multi-resonance reuse of one active region.

## What resource actually grows

For local linear absorption,

```math
P_{abs}
=\frac{\omega\epsilon_0\chi''}{2}
V\langle |E|^2\rangle.
```

At fixed absorbed power,

```math
\boxed{\langle |E|^2\rangle\propto1/V.}
```

Thus shrinking the active volume requires increasing internal field and absorbed power density.

With a maximum linear field `E_lin`, the maximum incident power at fixed absorptance is proportional to `V`.

For bulk dark generation `G_d=g_dV`, dark-shot-noise-limited `NEP^2` is also proportional to `V`. Hence

```math
\boxed{P_{max}/NEP_d^2=constant}
```

within the simple extensive model, while amplitude dynamic range scales as `sqrt(V)`.

The microscopic equivalent is that the number of absorbing centers controls both dark-event rate and maximum cycling/throughput rate.

## Optical/radiative floor

Reducing bulk dark generation does not force the optical/background/radiative noise of the accepted modes to shrink. With fixed external absorptance,

```math
NEP_{tot}^2(V)=A V+B_{opt}+B_{read}+\cdots.
```

At sufficiently small `V`, further miniaturization yields little sensitivity gain while continuing to reduce saturation headroom.

## Relation to optical bounds

The 2026 Bode-Fano absorption work of Corsaro, Alu and Forestiere rigorously limits the absorption bandwidth of a finite homogeneous absorbing object. Its bound depends on the radiation geometry of the entire object (`C_{Omega,0}` / circumscribing geometry) and does not isolate a tiny dark-generating inclusion behind an arbitrary larger lossless collector.

Miller et al. provide geometry-independent per-volume bounds for a lossy body in a specified incident/background field, but those results likewise cannot be silently converted into a dark-generating-volume bound when separate lossless optics are permitted to enhance the local field.

The missing resource must be specified explicitly.

## Prior-art disposition

Already established:

- resonant-cavity, antenna, dielectric-resonator, and metalens infrared detectors use optical concentration to reduce active volume/dark current;
- optical Bode-Fano, sum-rule, and material-response bounds constrain passive optical response;
- detector saturation, nonlinear response, and dynamic range are standard performance limits.

The scaling organization here is useful but novelty is not established.

## Scientific disposition

```text
universal active-volume / optical-bandwidth theorem: REJECT
fixed-mode critical-coupling tradeoff: RETAIN AS CONDITIONAL
lossless-transformer counterexample: RETAIN
field / saturation / throughput resource shift: RETAIN
paper construction: DO NOT BEGIN
```

A future experiment may impose a real resource such as finite etendue, maximum field, saturation throughput, optical matching volume/order, or finite accepted spatial-mode count. That would be a different constrained problem and must be motivated physically rather than added to save the original hypothesis.