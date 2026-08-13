# Current State — Experiment 04: Nonreciprocal Photodetector

**Date:** 2026-08-13  
**Status:** EARLY CONDITIONAL NO-GO / PASSIVE LINEAR INTRINSIC-SENSITIVITY PATH CLOSED / NOVELTY NOT ESTABLISHED

## Question

Can a nonreciprocal optical environment give a photodetector high absorption from the desired signal mode but lower radiative dark current/noise by suppressing emission back into that mode?

## First result

Directional Kirchhoff equality can be broken, but total external radiative coupling cannot be reduced at fixed total absorption in a passive linear channel description.

For external scattering matrix `S`,

```math
A_{in}=I-S^\dagger S,
\qquad
E_{out}=I-SS^\dagger.
```

Hence

```math
\boxed{Tr(A_{in})=Tr(E_{out}).}
```

Equivalently,

```math
\boxed{\sum_j a_j=\sum_i e_i.}
```

This requires no reciprocity assumption.

## Strong reciprocal comparator

If `K` orthogonal signal channels must each have unit absorptivity,

```math
\sum_i e_i=\sum_j a_j\ge K.
```

An ideal reciprocal mode-selective detector that absorbs exactly those `K` channels and reflects all others attains the same lower bound.

Therefore passive nonreciprocity does **not** beat the ideal reciprocal comparator on the total external radiative coupling relevant to radiative carrier loss/dark-current detailed balance.

## Minimal one-way example

```math
S=\begin{pmatrix}0&1\\0&0\end{pmatrix}
```

gives

```text
absorptivity (1,0)
emissivity   (0,1).
```

The detector absorbs perfectly from one direction and emits nothing back there, but all emission is redirected into the other channel. Total emission is unchanged.

## Detector consequences

1. **Radiative dark current:** redirecting an emitted photon does not eliminate the carrier-pair loss associated with its escape. The thermally weighted total emissive coupling obeys the same minimum as an ideal reciprocal mode-selective detector.
2. **Background photon noise:** signal photons and thermal photons in the same accepted channel share the same absorptivity, so nonreciprocity does not reduce the photon noise already entering through the required signal mode.
3. **System routing:** nonreciprocity can still reduce self-emission back toward the scene, route heat, or alter optical feedback. Those are legitimate system-level uses, but they are not an intrinsic detector-sensitivity gain in this model.

## Active/time-varying escape route

Time-modulated structures exchange work with an external pump and can perform photonic refrigeration. That route is established prior art and must be treated as active cooling/energy conversion, including pump work and added channels, not as a free violation of the passive detector bound.

## Prior-art boundary

Do not claim as new:

- generalized or adjoint Kirchhoff laws;
- nonreciprocal directional absorption/emission;
- strong experimental violation of directional Kirchhoff equality;
- nonreciprocal thermal energy conversion;
- time-modulated photonic refrigeration.

Primary references include Guo, Zhao & Fan, *PRX* 12, 021023 (2022); Zhao et al., *PR Applied* 16, 064001 (2021); Zhang et al., *PRL* 135, 016901 (2025); Buddhiraju, Li & Fan, *PRL* 124, 077402 (2020).

## Disposition

```text
passive nonreciprocity as intrinsic radiative-dark-current advantage: CLOSE
trace/channel identity: RETAIN as useful reasoning
nonreciprocal routing/back-action applications: OUTSIDE current detector-sensitivity question
active modulation: established cooling resource, not default continuation
paper construction: DO NOT BEGIN
```

## Reopen condition

Only reopen if a physically unavoidable geometry/material constraint can be shown to prevent the reciprocal mode-selective comparator from reaching the same accepted-mode absorption while a nonreciprocal device can do so. The constraint must be part of the detector problem itself, not imposed merely to protect the hypothesis.

See `FIRST_PRINCIPLES_TRACE_BOUND.md` for the derivation.