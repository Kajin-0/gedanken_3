# Experiment 04 — passive nonreciprocal photodetector trace bound

**Date:** 2026-08-13  
**Status:** FIRST-PRINCIPLES CONDITIONAL NO-GO / PASSIVE LINEAR CASE / NOVELTY NOT ESTABLISHED

## Question

Can a nonreciprocal optical environment let a photodetector absorb strongly from a desired signal mode while radiatively recombining weakly, thereby lowering radiative dark current or noise without sacrificing signal absorption?

Nonreciprocal thermal emitters can have unequal directional absorptivity and emissivity. The detector question is whether that directional asymmetry lowers the **total radiative coupling relevant to carrier loss/noise**, or merely redirects emitted photons into other channels.

## 1. Channel formulation

At one angular frequency, describe all external propagating optical channels by a scattering matrix `S`.

For a passive system,

```math
S^\dagger S\preceq I.
```

The absorption operator for incoming channels is

```math
A_{in}=I-S^\dagger S.
```

Thus the absorptivity of incoming channel `j` is

```math
a_j=(A_{in})_{jj}.
```

Fluctuational electrodynamics gives the normalized emission operator into outgoing channels as

```math
E_{out}=I-SS^\dagger,
```

so

```math
e_i=(E_{out})_{ii}.
```

For reciprocal systems, the usual channel-paired Kirchhoff relation is recovered. For nonreciprocal systems, `a_j` and `e_j` need not be equal channel by channel.

## 2. Exact trace identity

Regardless of reciprocity,

```math
\sum_j a_j=Tr(I-S^\dagger S),
```

and

```math
\sum_i e_i=Tr(I-SS^\dagger).
```

Because

```math
Tr(S^\dagger S)=Tr(SS^\dagger),
```

we obtain

```math
\boxed{\sum_j a_j=\sum_i e_i.}
```

Therefore passive linear nonreciprocity may redistribute absorption and emission among channels, but it cannot change the angle/polarization/channel-integrated coupling at fixed frequency.

## 3. Strong detector comparator

Suppose the detector must accept a set `T` of orthogonal signal channels. Then

```math
\sum_j a_j\ge\sum_{j\in T}a_j.
```

The trace identity immediately gives

```math
\boxed{\sum_i e_i\ge\sum_{j\in T}a_j.}
```

If `K` orthogonal target channels must each be perfectly absorbed,

```math
a_j=1\quad(j\in T),
```

then

```math
\boxed{\sum_i e_i\ge K.}
```

An ideal reciprocal mode-selective absorber can attain the same lower bound by absorbing only those `K` channels and perfectly reflecting all others. Thus passive nonreciprocity does not beat the ideal reciprocal mode-selective comparator on total external radiative coupling.

## 4. Minimal two-channel example

Take

```math
S=\begin{pmatrix}0&1\\0&0\end{pmatrix}.
```

Then

```text
incoming absorptivity: (a1,a2)=(1,0)
outgoing emissivity:   (e1,e2)=(0,1)
```

The detector perfectly absorbs channel 1 and emits nothing back into channel 1, but it emits entirely into channel 2.

This is the cleanest possible demonstration that breaking directional Kirchhoff equality does not by itself reduce total emission:

```math
\sum a_j=\sum e_i=1.
```

A reciprocal comparator with one perfectly absorbed channel and one perfectly reflected channel also has total emissivity 1.

## 5. Radiative dark-current consequence

In the ideal radiative-limit photodiode picture, external radiative recombination/dark-current coupling is proportional to the thermally weighted total external emissive coupling. Schematically,

```math
J_{0,rad}\propto q\int d\omega\, n_T(\omega)\,Tr[A_{in}(\omega)].
```

For a required target-channel absorptivity `a_t(omega)`,

```math
Tr[A_{in}]\ge a_t,
```

so

```math
J_{0,rad}\ge Cq\int d\omega\,n_T(\omega)a_t(\omega)
```

for the appropriate channel normalization constant `C`.

An ideal reciprocal detector that absorbs only the target channel saturates the same bound. Nonreciprocity cannot lower this radiative floor further merely by redirecting the emitted photon.

This statement concerns **external radiative coupling**. Internal radiative recombination followed by photon recycling is not a net carrier loss until a photon escapes or is otherwise lost.

## 6. Background-photon consequence

Signal photons and thermal/background photons arriving in the same accepted optical channel see the same absorptivity `a_t`. Therefore directional nonreciprocity that leaves `a_t` unchanged does not reduce the photon-noise contribution already present in that accepted mode.

It can suppress emission back toward the scene, but that is a routing/system-feedback benefit, not an intrinsic improvement of the accepted-mode photon-noise floor.

## 7. What remains open

This is a no-go only for the passive linear comparison with a complete external channel basis.

Potentially different cases include:

1. active/time-modulated structures that exchange work with a pump;
2. frequency-converting systems where all Floquet sidebands must be included as channels;
3. detector objectives involving back-action or self-emission into the scene rather than total terminal dark noise;
4. fabrication/geometric constraints that prevent the reciprocal mode-selective comparator from reaching the same bound.

However, active time modulation is already established as a mechanism for photonic refrigeration, so it must be treated as an externally powered cooling resource rather than a free nonreciprocal detector improvement.

## 8. Prior-art boundary

Known before this experiment:

- generalized/adjoint Kirchhoff laws for nonreciprocal emitters;
- theoretical nonreciprocal thermal emitters and energy-conversion schemes;
- experimental observation of strong directional nonreciprocal thermal emission;
- active photonic refrigeration from time modulation;
- reciprocal angle/emission restriction and photon recycling in photovoltaic detailed-balance theory.

Relevant starting references:

- Guo, Zhao & Fan, *Phys. Rev. X* 12, 021023 (2022), DOI `10.1103/PhysRevX.12.021023`.
- Zhao et al., *Phys. Rev. Applied* 16, 064001 (2021), DOI `10.1103/PhysRevApplied.16.064001`.
- Zhang et al., *Phys. Rev. Lett.* 135, 016901 (2025), DOI `10.1103/PhysRevLett.135.016901`.
- Buddhiraju, Li & Fan, *Phys. Rev. Lett.* 124, 077402 (2020), DOI `10.1103/PhysRevLett.124.077402`.

Do not claim the trace identity or generalized Kirchhoff physics as new.

## 9. First disposition

```text
high absorption + low emission into the SAME direction: possible with nonreciprocity
high target absorption + lower TOTAL external radiative coupling than ideal reciprocal mode selection: NO in passive linear case
intrinsic radiative-dark-current advantage from directional rerouting alone: NOT ESTABLISHED; first model says NO
```

The next question is whether any realistic detector constraint makes the reciprocal mode-selective comparator unavailable while a nonreciprocal structure remains feasible. If no such constraint survives, close Experiment 04 early.