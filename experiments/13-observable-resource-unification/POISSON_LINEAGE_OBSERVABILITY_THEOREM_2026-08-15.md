# Experiment 13 — Poisson-lineage terminal observability theorem

**Date:** 2026-08-15  
**Scope:** analytical/theoretical only  
**Status:** DERIVED / CONNECTS EXPERIMENT 03 TO MASTER GRAM GEOMETRY / NOVELTY NOT ESTABLISHED

## 1. Question

Experiment 03 found an apparently paradoxical boundary:

```text
internal photon-recycling population cross-spectrum: nonzero and sign-changing
ideal endpoint-counting terminal cross-spectrum: exactly zero
```

The desired general question is:

> What property of the terminal readout decides whether one internally recycled excitation is visible as inter-terminal noise correlation?

The cleanest answer is obtained at the level of complete stochastic event lineages.

---

## 2. Independent primary-event model

Let primary event class `a` occur as an independent stationary Poisson process of rate `lambda_a`.

A single primary event at time `t_n` generates an entire random internal lineage: carrier motion, recombination, photon recycling, reabsorption, final extraction, gain, etc. After all internal physics and readout are included, that lineage produces an `m`-terminal waveform

```math
\mathbf h_a(t;\zeta)
=\begin{pmatrix}
h_{a1}(t;\zeta)\\
\vdots\\
h_{am}(t;\zeta)
\end{pmatrix},
```

where `zeta` denotes all random marks/internal outcomes of the lineage.

The measured terminal record is

```math
\mathbf y(t)
=\sum_a\sum_n
\mathbf h_a(t-t_{an};\zeta_{an}).
```

Assume independent lineages and finite second waveform energy so the usual stationary shot-noise spectrum exists.

Let

```math
\mathbf H_a(\omega;\zeta)
```

be the Fourier transform of one complete lineage waveform.

---

## 3. Cross-spectral matrix

Campbell/Poisson shot-noise algebra gives the continuous fluctuation spectrum away from the DC mean line:

```math
\boxed{
S_y(\omega)
=\sum_a\lambda_a
\mathbb E_\zeta
\left[
\mathbf H_a(\omega;\zeta)
\mathbf H_a^\dagger(\omega;\zeta)
\right].
}
```

Therefore

```math
\boxed{
S_{y,ij}(\omega)
=\sum_a\lambda_a
\mathbb E_\zeta
\left[
H_{ai}(\omega;\zeta)
H_{aj}^*(\omega;\zeta)
\right].
}
```

This is exactly a Gram matrix of complete-lineage terminal response vectors.

The key object is **not** whether the internal state visited both pixels. The key object is whether the *same complete stochastic lineage contributes coherently/statistically to both measured terminal waveforms*.

---

## 4. Exact single-terminal-support theorem

Suppose every complete lineage, for every event class and every random mark, has support in at most one measured terminal:

```math
\mathbf H_a(\omega;\zeta)
=g_a(\omega;\zeta)\,\mathbf e_{J(a,\zeta)}.
```

That is, the lineage may wander internally through any number of locations, but the readout assigns the entire measured waveform to one terminal only.

Then each outer product is diagonal:

```math
\mathbf H_a\mathbf H_a^\dagger
=|g_a|^2
\mathbf e_J\mathbf e_J^\dagger.
```

Hence

```math
\boxed{
S_{y,ij}(\omega)=0
\qquad(i\ne j)
}
```

for every frequency.

This result is independent of the complexity of the internal conservative routing.

### Interpretation

```text
one lineage -> one measured terminal
```

is sufficient for exact absence of passive inter-terminal shot-noise correlation.

This is the waveform/spectral version of independent Poisson marking and thinning.

---

## 5. General observability criterion

For a specified pair of terminals `i,j`, define the lineage overlap

```math
\Gamma_{ij}(\omega)
=\sum_a\lambda_a
\mathbb E
[H_{ai}(\omega)H_{aj}^*(\omega)].
```

Then

```math
\boxed{
S_{y,ij}(\omega)=0
\iff
\Gamma_{ij}(\omega)=0.
}
```

This is the exact necessary-and-sufficient spectral criterion within the independent-lineage model.

A useful sufficient condition for **possible nonzero** correlation is that a set of lineages of nonzero measure has simultaneous multichannel support:

```math
H_{ai}(\omega)H_{aj}^*(\omega)\ne0.
```

However, simultaneous support is not by itself mathematically necessary for a nonzero *sum* if event classes are represented differently, nor does it guarantee nonzero total correlation because complex contributions from different lineage classes can cancel. The exact criterion is the weighted overlap `Gamma_ij`.

Thus the strongest general statement is:

> Terminal cross-noise measures overlap of complete-lineage readout waveforms, not internal coupling by itself.

---

## 6. Relation to the master Gram/effect operator

Introduce an abstract Hilbert space whose orthogonal basis labels independent primary-lineage innovations and marks. Let `M_y(omega)` map a unit lineage innovation into its multichannel terminal Fourier waveform.

Then

```math
S_y(\omega)
=M_y(\omega)\Sigma_{lineage}(\omega)M_y^\dagger(\omega),
```

and the channel pair cross-spectrum is the Gram inner product

```math
S_{ij}(\omega)
=\langle q_i(\omega)|q_j(\omega)\rangle,
```

where

```math
|q_i\rangle
=\Sigma_{lineage}^{1/2}M_y^\dagger|e_i\rangle.
```

Therefore Experiment 03 is the **off-diagonal Gram geometry** of the same operator structure used in the other unified branches.

---

## 7. Device-class specializations

### A. Ideal endpoint-counting photodiode

Each primary excitation eventually exits through exactly one counted sink. The entire measured lineage is a final extraction pulse in one terminal:

```math
\mathbf H(\omega)=g_J(\omega)e_J.
```

Therefore all inter-pixel cross-spectra vanish identically under independent Poisson generation, even if photon recycling changes the probability that the final sink is a neighboring pixel.

This reproduces Experiment 03's exact cancellation without needing to track the internal population covariance explicitly.

### B. Occupancy-sensitive photoconductor

A recycled excitation can alter the conductivity/current of pixel 1 during one residence interval and pixel 2 after radiative transfer/reabsorption. A single lineage can therefore produce

```math
H_1(\omega)\ne0,
\qquad
H_2(\omega)\ne0.
```

The lineage outer product has a nonzero off-diagonal term. Cross-noise is generically observable, with sign and frequency dependence set by the relative waveform phases and residence dynamics.

### C. Finite-transit Shockley-Ramo photodiode

A charge can induce current during motion before final collection. If the complete recycled lineage produces induced-current waveform segments associated with more than one pixel/electrode before its final sink is counted, then the single-terminal-support condition fails.

The exact terminal prediction requires the electrode weighting fields and the radiative-transfer lineage. The present theorem says precisely what must be computed: the complete multichannel lineage waveform, not merely the final sink probabilities.

### D. Branching gain / SPAD / e-APD

A primary event can create more than one recorded descendant output. Then one lineage naturally has multichannel/multiple-event support and the rank-one single-sink structure is broken. Cross-correlation is therefore generically allowed.

This explains why passive optical crosstalk in a branching avalanche array is qualitatively different from conservative photon recycling followed by one final extraction count.

---

## 8. Strong conceptual boundary

The hierarchy is now

```text
internal coupling
    does not imply
shared terminal waveform support
    does not by itself imply
nonzero total cross-spectrum
```

The exact terminal observable is

```math
S_{ij}(\omega)
=\sum_a\lambda_a E[H_{ai}H_{aj}^*].
```

Thus any inference from deterministic optical crosstalk or internal population correlation to terminal cross-noise must specify the complete lineage-to-terminal readout map.

---

## 9. Relation to Experiment 01 and Experiment 12

This theorem completes a striking spectral-geometric trio:

```text
Experiment 01:
    diagonal quadratic forms / full Gram kernel
    -> task performance and search geometry.

Experiment 12:
    largest singular value of coupling blocks
    -> minimum resource required for response.

Experiment 03:
    off-diagonal Gram products / null structure
    -> whether internal dynamics is visible as terminal correlation.
```

Experiment 09 additionally uses eigenvector alignment of a low-rank effect operator to distinguish coherent signal from incoherent internal generation.

---

## 10. Novelty warning

The generic ingredients are established mathematical objects:

- Poisson shot-noise/Campbell formulas;
- marking/thinning/displacement of Poisson processes;
- linear stochastic input-output theory;
- Gram matrices and observability/null-space ideas.

Do not claim those ingredients as new.

Potential paper-level value, if it survives prior-art search, would be the **photodetector-specific closure** showing that deterministic photon recycling, internal fluctuation correlation, terminal cross-noise, task information, and microscopic response/resource bounds occupy different geometric features of the same detector coupling operator.

## 11. Next step

Derive the exact finite-transit Shockley-Ramo lineage waveform for the minimal two-pixel recycling model and test whether it yields a nonzero cross-spectrum continuously interpolating between:

```text
occupancy-sensitive limit: visible recycling cross-noise
endpoint-counting limit: exact zero cross-noise.
```

This would provide a physically transparent interpolation rather than only two endpoint device classes.
