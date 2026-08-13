# Readout side-information no-go for section-level optical timing compensation

**Date:** 2026-08-13  
**Status:** EXACT CONDITIONAL-VARIANCE RESULT / NEGATIVE RESULT FOR ELECTRICALLY SEGMENTED IMPLEMENTATIONS / NOVELTY NOT ESTABLISHED

## Question

Does passive optical timing equalization retain a timing advantage if the detector readout reveals which spatial section produced the event?

Let the latent absorption coordinate be `X`, the observable electrical side information be `Y`, and the timestamp before any correction be

```math
T=m(X)+\epsilon,
```

with

```math
E[\epsilon|X]=0.
```

The coordinate-dependent conditional mean is `m(X)`.

## Optimal post-detection correction

For any correction `g(Y)`, the minimum mean-square residual is obtained with

```math
g_*(Y)=E[T|Y]-C.
```

Therefore

```math
\boxed{
\min_g Var[T-g(Y)] = E[Var(T|Y)].
}
```

If the stochastic residual is conditionally independent of the readout side information once `X` is fixed, then

```math
\boxed{
E[Var(T|Y)]
=E[Var(\epsilon|X)]
+E[Var(m(X)|Y)].
}
```

Exact physical precompensation

```math
d_{phys}(X)=C-m(X)
```

instead gives

```math
\boxed{Var[T+d_{phys}(X)]=E[Var(\epsilon|X)].}
```

Hence the maximum timing advantage available to physical precompensation over optimal readout correction is exactly

```math
\boxed{E[Var(m(X)|Y)].}
```

This vanishes whenever the readout side information is sufficient to determine the coordinate-dependent mean delay.

## Consequence for a segmented detector

Let `Y=J` be the identity of the electrical detector section. Then a calibrated correction

```math
T_{corr}=T-E[T|J]+C
```

removes every section-dependent mean delay.

The same operation can be performed *before* a single-output merger by inserting a fixed electrical branch delay

```math
\delta_J=C-E[T|J]
```

on each local section output and then combining the branches.

Therefore:

```text
multiple external outputs are not required for the equivalence.
```

A locally segmented SPAD/APD with section-specific pulse paths can implement the same section-level mean-delay equalization electrically and expose only one final output.

## Relation to the N-section optical ladder

For the finite ladder, `J` identifies the longitudinal/depth section. After per-section calibration, the remaining deterministic spread is the within-section quantization variance

```math
D_N=E[Var(U|J)].
```

This is exactly the same `D_N` that remains in the passive N-step optical ladder when each depth level is the conditional centroid.

Thus, on a timing-only objective,

```math
\boxed{
\text{N-section passive ladder}
\equiv
\text{N-section electrical timing calibration}
}
```

at the level of deterministic section means.

The optical ladder does not beat the calibrated segmented detector on this term.

## Stronger architecture requirement

The scientifically distinct regime is therefore narrower:

> the absorption coordinate to be equalized must remain hidden from any section-specific electrical timing path, or the passive section-level delay can be reproduced electronically.

A viable implementation should therefore favor a **continuous/common electrical detector degree of freedom** rather than three electrically isolated SPADs whose local pulses are separately available before merger.

A distributed/traveling-wave common-output APD remains a candidate because its propagation delay is part of the common physical timestamp rather than a set of independently programmable section offsets. However, if the common output waveform itself reveals position with useful precision, optimal waveform processing becomes another side-information comparator and must be allowed in a fair performance claim.

## Prior-art pressure

Existing SPAD-array readout patents already describe local quench/pulse-shaping circuits feeding distributed OR trees with substantially equal path lengths. Separate patents describe cell-position-dependent timing-skew correction. These do not establish the transverse optical-depth compensation concept, but they make section-level electrical timing equalization an obvious practical comparator.

## Disposition

**NEGATIVE RESULT:** do not use three independently read-out SPAD sections as the primary demonstration of optical isochrony.

**RETAINED:** continuous/common-output detector architectures in which the depth coordinate is not separately exposed electrically.

**NEXT:** compare common lumped and distributed/traveling-wave readout under the same residual timing budget, then decide whether the first physical demonstrator should be linear-mode APD rather than Geiger-mode SPAD.