# Experiment 13 — Exact mixed-readout interpolation for recycling cross-noise

**Date:** 2026-08-15  
**Scope:** analytical/theoretical only  
**Status:** EXACT WITHIN TWO-PIXEL LINEAR POISSON MODEL / BRIDGES EXPERIMENT-03 ENDPOINTS

## 1. Purpose

Experiment 03 established two endpoint observables for the same internal conservative exchange process:

```text
occupancy-sensitive readout: internal sign-changing cross-spectrum visible;
ideal extraction counting:   cross-spectrum cancels exactly.
```

A useful unified paper should not leave these as disconnected device classes. This step derives an exact continuous interpolation between them.

---

## 2. Internal process

Use the Experiment-03 symmetric two-pixel state model

```math
\dot x=-Mx+\xi,
```

with

```math
M=\begin{pmatrix}
\gamma+k&-k\\
-k&\gamma+k
\end{pmatrix},
\qquad
\gamma=\Gamma_e+\Gamma_o.
```

For equal stationary mean population `m`, define

```math
R(\omega)=(M+i\omega I)^{-1}.
```

Then

```math
S_x(\omega)=m(R+R^\dagger).
```

The extraction shot-noise innovation `zeta_e` has

```math
D_e=\Gamma_e mI,
```

and because an extraction event is simultaneously a measured event and a state-loss event,

```math
S_{x\zeta_e}=-RD_e,
\qquad
S_{\zeta_e x}=-D_eR^\dagger.
```

The ideal extraction-counting record is

```math
j_e=\Gamma_e x+\zeta_e.
```

---

## 3. Mixed terminal observable

Define a real instantaneous linear combination

```math
\boxed{
y=a x+b j_e.
}
```

Here

```text
a = occupancy-sensitive transduction coefficient;
b = endpoint-extraction transduction coefficient.
```

Substituting `j_e`,

```math
y=(a+b\Gamma_e)x+b\zeta_e.
```

Let

```math
c=a+b\Gamma_e.
```

Then

```math
S_y
=c^2S_x+b^2D_e
+cb(S_{x\zeta_e}+S_{\zeta_e x}).
```

Using the exact correlated-noise identities,

```math
S_y
=m\left[
(c^2-cb\Gamma_e)(R+R^\dagger)
+b^2\Gamma_e I
\right].
```

Because

```math
c^2-cb\Gamma_e
=c(c-b\Gamma_e)
=a(a+b\Gamma_e),
```

we obtain

```math
\boxed{
S_y(\omega)
=a(a+b\Gamma_e)S_x(\omega)
+b^2\Gamma_e m I.
}
```

This is the exact interpolation formula.

---

## 4. Cross-spectrum

The added endpoint shot-noise term is diagonal. Therefore

```math
\boxed{
S_{y,12}(\omega)
=a(a+b\Gamma_e)S_{x,12}(\omega).
}
```

Using the known internal spectrum,

```math
\boxed{
S_{y,12}(\omega)
=a(a+b\Gamma_e)m
\left[
\frac{\gamma}{\gamma^2+\omega^2}
-
\frac{\gamma+2k}{(\gamma+2k)^2+\omega^2}
\right].
}
```

For positive `a,b`, the zero crossing remains

```math
\boxed{
\omega_x=\sqrt{\gamma(\gamma+2k)}.
}
```

Thus adding an endpoint-counting component does not move the intrinsic exchange-mode sign reversal in this instantaneous common-gain model. It rescales the correlated component and adds uncorrelated white terminal noise.

---

## 5. Autospectrum and normalized visibility

The internal auto-spectrum is

```math
S_{x,11}(\omega)
=m\left[
\frac{\gamma}{\gamma^2+\omega^2}
+
\frac{\gamma+2k}{(\gamma+2k)^2+\omega^2}
\right].
```

Hence

```math
\boxed{
S_{y,11}(\omega)
=a(a+b\Gamma_e)S_{x,11}(\omega)
+b^2\Gamma_e m.
}
```

The observable normalized cross-spectrum is therefore

```math
\boxed{
\frac{S_{y,12}}{S_{y,11}}
=
\frac{a(a+b\Gamma_e)S_{x,12}}
{a(a+b\Gamma_e)S_{x,11}+b^2\Gamma_e m}.
}
```

This gives a continuous visibility parameterization between the two ideal readouts.

---

## 6. Endpoint limits

### Pure occupancy readout

Set

```math
b=0.
```

Then

```math
S_y=a^2S_x,
```

so the full sign-changing internal exchange spectrum is preserved.

### Pure endpoint counting

Set

```math
a=0.
```

Then

```math
\boxed{
S_y=b^2\Gamma_e m I,
}
```

and therefore

```math
\boxed{S_{y,12}=0.}
```

The exact Experiment-03 cancellation is recovered.

### Algebraic cancellation point

There is also a formal second zero of the correlated coefficient when

```math
a=-b\Gamma_e.
```

This corresponds to an engineered subtraction of the state-mediated component and is not assumed to represent an ordinary passive photodetector readout. It is retained because it shows that readout phase/sign can create additional cancellation beyond pure endpoint counting.

---

## 7. Physical interpretation

The same internal exchange spectrum is multiplied by

```math
\boxed{a(a+b\Gamma_e)}
```

while endpoint counting contributes an independent diagonal floor

```math
b^2\Gamma_e m.
```

Therefore the visibility of photon-recycling cross-noise is not a property of recycling alone. It is controlled continuously by the mixture of:

```text
state/occupancy sensitivity
versus
final-event sensitivity.
```

This is the simplest explicit bridge between the two device classes identified in Experiment 03.

---

## 8. Relation to Shockley-Ramo readout

A real finite-transit photodiode generally cannot be represented by frequency-independent real constants `a,b`. Carrier motion produces a causal induced-current waveform, so the correct generalization is

```math
Y(\omega)=A(\omega)X(\omega)+B(\omega)J_e(\omega).
```

Complex `A(omega),B(omega)` can alter not only the magnitude but also the phase and therefore the detailed sign/crossover structure of the measured cross-spectrum.

The present constant-coefficient theorem should therefore be interpreted as the minimal exact interpolation and as a target that the full Shockley-Ramo model must reduce to in the appropriate limits.

---

## 9. Unification value

This interpolation strengthens the Experiment-13 program because it turns the Experiment-03 contribution from a binary anecdote into a continuous operator/readout statement:

```text
same internal state dynamics
+ continuously varying observation operator
-> continuously varying terminal visibility,
with an exact null at the endpoint-counting operator.
```

Together with the Experiment-13 spectral sandwich, this identifies the hidden-noise result as a concrete approach to a readout null direction rather than a separate stochastic curiosity.

## 10. Next step

Derive `A(omega)` and `B(omega)` from a minimal one-dimensional Shockley-Ramo transit model with a radiative recycling event between two pixels. Determine whether the finite-transit cross-spectrum has a closed form and whether the endpoint-counting cancellation is approached continuously as transit time tends to zero relative to the recycling/residence times.
