# Feasibility and diffusion discriminator

**Date:** 2026-08-13
**Status:** QUANTITATIVE SCREEN / DETECTOR-SPECIFIC NOVELTY STILL UNESTABLISHED

## Cross-spectrum precision

For `M` effectively independent Gaussian spectral averages, equal measured auto PSDs `S_T`, and small real coherence, the co-spectrum standard deviation is approximately

```math
\sigma_{12}\simeq\frac{S_T}{\sqrt{2M}}.
```

If intrinsic exchange gives cross/auto ratio `c` and intrinsic carrier noise is fraction

```math
d=S_{carrier}/S_T
```

of the measured auto PSD, then

```math
\boxed{Z\simeq c d\sqrt{2M}.}
```

Hence

```math
\boxed{M\simeq Z^2/(2c^2d^2).}
```

At `Z=5`:

```text
c=0.5%, d=1.0 -> M ~ 5.0e5
c=1.0%, d=1.0 -> M ~ 1.25e5
c=5.0%, d=1.0 -> M ~ 5.0e3
c=1.0%, d=0.5 -> M ~ 5.0e5
c=1.0%, d=0.3 -> M ~ 1.39e6
```

This is a conservative single-frequency estimate. Fitting the full predicted positive/zero/negative spectral shape can combine information from multiple bins.

The 2019 HgCdTe photon-recycling calculation reports sub-percent to percent-scale parasitic responses for small pixels, so a linear-array implementation would require precision simultaneous readout rather than ordinary frame covariance.

## Important bandwidth issue

Some HOT LWIR HgCdTe photodiodes have measured response times around or below 1 ns under reverse bias, with practical response limited by transit/RC effects. A carrier-exchange feature at such rates is not accessible through a normal imaging ROIC; a dedicated high-bandwidth two-pixel test structure would be required.

The current model should therefore be viewed as a measurement-method theory, not as something automatically extractable from standard FPA data.

## Direct versus indirect exchange at high frequency

For the symmetric array model

```math
S_x(\omega)=2mM(M^2+\omega^2I)^{-1},
```

expand at high frequency:

```math
\boxed{
S_x(\omega)
=\frac{2m}{\omega^2}M
-\frac{2m}{\omega^4}M^3
+O(\omega^{-6}).
}
```

For distinct pixels with a direct exchange edge `k_ij`,

```math
\boxed{
S_{ij}(\omega)
\sim-\frac{2m k_{ij}}{\omega^2}.}
```

If there is no direct edge (`k_ij=0`), the `1/omega^2` term vanishes and the leading cross-spectrum is at least `O(omega^-4)` in this finite-state local-exchange model.

Example: for a three-pixel nearest-neighbor chain, pixels 1 and 3 have no direct edge and

```math
S_{13}(\omega)
\sim
-\frac{2m k^2(3\gamma+4k)}{\omega^4}.
```

Thus the high-frequency power law contains information about whether a pair is directly coupled or connected only through intermediate reservoirs.

## Continuous local diffusion across a physical separation

For a 1-D reaction-diffusion model

```math
\partial_t n=D\partial_x^2n-\gamma n+\eta,
```

the frequency-domain Green function between points separated by `d>0` has the form

```math
G(d,\omega)
=\frac{1}{2D\kappa}
\exp(-\kappa d),
\qquad
\kappa=\sqrt{(\gamma+i\omega)/D}.
```

The equilibrium cross-spectrum is proportional to the real part of this Green function. At high frequency,

```math
|G|
\propto
\omega^{-1/2}
\exp[-d\sqrt{\omega/(2D)}].
```

Therefore genuinely local diffusion across a nonzero physical separation loses high-frequency cross-correlation much faster than an effectively instantaneous nonlocal jump.

## Candidate mechanism discriminator

Photon propagation can directly connect spatially separated pixels without passing through intervening carrier reservoirs. In the direct-jump limit it therefore permits a negative `1/omega^2` cross tail even between non-nearest pixels.

Local carrier diffusion cannot create such an instantaneous long-range carrier edge. For separated reservoirs it gives either higher-order graph-path tails or the diffusion Green-function suppression above.

This suggests the following candidate discriminator:

```text
long-range negative 1/f^2 cross tail
-> consistent with direct nonlocal exchange (e.g. photon transport)

short-range coupling with rapidly suppressed non-neighbor high-frequency correlation
-> consistent with local carrier diffusion
```

This is not unique to photons. Instantaneous electrical channel mixing or another nonlocal coupling can also produce long-range correlations and must be calibrated independently.

## Prior-art boundary

- Diffusion effects on semiconductor GR-noise spectra have been treated since at least the 1960s.
- HgCdTe crosstalk literature already separates optical and diffusive contributions using deterministic transport simulations and structures such as trenches/guard rings.
- SPAD arrays already use dark-event timing correlations to diagnose optical/electrical crosstalk.

A targeted search did not identify a linear HgCdTe/ordinary photodiode-array study using the **high-frequency analog cross-noise asymptotic** above to separate direct radiative exchange from local diffusion. This absence is not proof of novelty.