# Experiment 13 — channel-specific observability geometry

**Date:** 2026-08-15  
**Scope:** linear multichannel stochastic readout at fixed frequency; positive innovation covariance / Poisson-lineage specialization  
**Status:** **DERIVED / TIGHTENS EXPERIMENT-03 CONNECTION TO THE MASTER POSITIVE-OPERATOR FRAMEWORK**

## 1. Purpose

The complete-lineage theorem writes the terminal spectrum as an outer-product sum. That establishes when internal recycling produces measured cross-noise, but the connection to the positive-operator reciprocity can be made sharper.

At a fixed frequency, each terminal defines its own positive **observability effect** on the internal innovation/lineage space. An internal component can therefore be visible to one terminal, null to another, or jointly visible to both. Cross-spectrum requires joint visibility; a channel null forces the corresponding cross term to vanish.

Finite-transit Shockley–Ramo motion changes the channel-specific map and can lift a null that exists under endpoint counting.

---

# 2. Linear stochastic map

At one angular frequency `omega`, let the internal innovation vector be `xi` with positive spectral covariance

```math
\Sigma(\omega)\succeq0.
```

Let the terminal vector be

```math
\mathbf y=M(\omega)\boldsymbol\xi.
```

Then

```math
\boxed{
S_y=M\Sigma M^\dagger.
}
```

Let `|i>` denote terminal `i` in output space and define the scalar channel map

```math
M_i=\langle i|M.
```

The positive channel-specific observability operator on innovation space is

```math
\boxed{
G_i
=M^\dagger|i><i|M
=M_i^\dagger M_i
\succeq0.
}
```

Its response to the innovation activity is

```math
\boxed{
S_{ii}
=Tr(G_i\Sigma).
}
```

Thus each terminal is exactly another instance of a positive activity pairing.

---

# 3. Cross-channel operator

For terminals `i` and `j`, define

```math
C_{ij}
=M^\dagger|j><i|M
=M_j^\dagger M_i.
```

Then

```math
\boxed{
S_{ij}=Tr(C_{ij}\Sigma).
}
```

`C_ij` need not be Hermitian or positive. It is the off-diagonal overlap operator between the two channel maps.

Whiten the innovation covariance:

```math
W=M\Sigma^{1/2}.
```

Let `w_i` be row `i` of `W`. Then

```math
S_{ij}=\langle w_j,w_i\rangle,
```

so Cauchy–Schwarz gives

```math
\boxed{
|S_{ij}|^2
\le
S_{ii}S_{jj}.
}
```

This is the standard spectral-coherence inequality, now interpreted in the internal innovation space.

---

# 4. Channel-null theorem

If an internal activity sector `X>=0` satisfies

```math
Tr(G_iX)=0,
```

then positivity implies that the sector is null to channel `i`.

For any second channel `j`, the cross contribution of that same sector must vanish:

```math
\boxed{
S_{ij}^{(X)}=0.
}
```

This follows immediately either from Cauchy–Schwarz because `S_ii^(X)=0`, or from the fact that the whitened channel vector `w_i` vanishes on that sector.

Therefore:

> cross-noise requires an internal activity sector to be visible to **both** measured terminal channels at the same frequency.

Internal coupling without joint terminal visibility is insufficient.

---

# 5. Endpoint-counting conservative lineage

Consider one conservative photon-recycling lineage that starts in pixel A and ultimately terminates by extraction in pixel B.

Under ideal final-sink counting, the complete terminal waveform is

```math
\mathbf H_{A\to B}^{end}(\omega)
=g_B(\omega)\mathbf e_B.
```

For the lineage sector `X_{A->B}`,

```math
Tr(G_A^{end}X_{A->B})=0,
```

because the final-sink map has no A-terminal component.

Therefore

```math
\boxed{
S_{AB}^{A\to B,end}=0.
}
```

This is the channel-null form of the endpoint-counting result.

When every conservative lineage has support in exactly one final terminal, every per-lineage outer product is diagonal, and the complete endpoint spectrum has zero interterminal cross terms under independent Poisson generation.

---

# 6. Finite-transit Ramo map lifts the source-channel null

For the same A-to-B internal lineage, a finite-transit Shockley–Ramo readout retains carrier motion in A before the internal radiative recombination.

The complete waveform becomes schematically

```math
\mathbf H_{A\to B}^{Ramo}(\omega)
=
\begin{pmatrix}
H_A^{rec}(\omega)\\
e^{-i\omega T_{AB}}H_B^{col}(\omega)
\end{pmatrix}.
```

For the internally created/recombined A segment,

```math
H_A^{rec}(0)=0
```

but generically an individual trajectory has

```math
H_A^{rec}(\omega)\ne0
```

at finite frequency.

Thus

```math
Tr(G_A^{Ramo}(\omega)X_{A->B})
```

can change from exactly zero in the endpoint model to positive at finite frequency.

The A-channel null is lifted.

Once both

```math
S_{AA}^{(A->B)}>0
```

and

```math
S_{BB}^{(A->B)}>0,
```

a nonzero cross term is **allowed**:

```math
|S_{AB}^{(A->B)}|^2
\le
S_{AA}^{(A->B)}S_{BB}^{(A->B)}.
```

It is not guaranteed; phase averaging, trajectory symmetry, opposing lineage classes, or electronics can still make the overlap zero.

---

# 7. Direct relation to activity-weighted reciprocity

Each channel effect

```math
G_i(\omega)=M_i^\dagger M_i
```

has its own activity-weighted selectivity and inverse-certification tightness for any positive internal sector `X`:

```math
\mathcal S_{i,X}(\omega)
=\frac{\lambda_{max}[G_i(\omega)]TrX}
{Tr[G_i(\omega)X]},
```

```math
\tau_{i,X}(\omega)
=\frac{Tr[G_i(\omega)X]}
{\lambda_{max}[G_i(\omega)]TrX},
```

with

```math
\boxed{
\mathcal S_{i,X}(\omega)\tau_{i,X}(\omega)=1
}
```

whenever the channel response is nonzero.

If the channel is null to `X`, then

```math
\tau_{i,X}=0.
```

Thus the endpoint-versus-Ramo recycling result is not merely analogous to the master theorem. It is a **frequency-dependent change of the channel-specific positive observability operator**:

```text
endpoint model:
    G_A X_{A->B}=0;
    source-channel certification = 0;
    A-B cross contribution = 0;

finite-transit Ramo model:
    G_A(omega) X_{A->B} may become nonzero for omega != 0;
    source-channel observability is restored;
    A-B cross contribution becomes allowed.
```

This is the tightest current Experiment-03 connection to the unified positive-operator framework.

---

# 8. Capacity-domain warning

For every channel-specific use of the reciprocity, `lambda_max(G_i)` must be taken on a physically declared innovation/activity domain.

Padding the domain with inaccessible or irrelevant directions can change the nominal maximum capacity and weaken the inferred activity bound without changing the actual response.

The domain must therefore be fixed by the physical problem before evaluating the spectral edge.

This same rule applies to the Experiment-12 optical velocity capacity and should be elevated into the unified manuscript's master theorem.

---

# 9. Manuscript consequence

The recycling section can now be integrated into the same staged-map framework with no claim that the cross-spectrum itself is a positive quadratic form.

Use:

```text
positive channel effects G_i
    -> auto-response / channel observability / nulls;

off-diagonal overlap operators C_ij
    -> cross-spectrum once joint visibility exists.
```

This makes Experiment 03 a downstream realization of the same map geometry rather than a disconnected final example.
