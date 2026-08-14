# Candidate Screen — Hall/Transverse Readout for Photon-Pair Versus GR Noise

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Disposition:** CLOSED EARLY / PARAMETER IDENTIFIABILITY ONLY / NO FUNDAMENTAL SIGNAL-VERSUS-GR ADVANTAGE

## Premise

Could the opposite Hall signs of electrons and holes provide a readout coordinate that distinguishes photon-generated electron-hole pairs from thermally generated/recombined carrier fluctuations better than ordinary longitudinal conductivity?

## Minimal two-carrier model

At weak magnetic field,

```math
\sigma_{xx}=q(n\mu_e+p\mu_h),
```

and to first order in `B`,

```math
\frac{\sigma_{xy}}{B}
=q(p\mu_h^2-n\mu_e^2).
```

For a neutral pair perturbation,

```math
\delta n=\delta p=\delta N,
```

so

```math
\boxed{\delta\sigma_{xx}=q(\mu_e+\mu_h)\delta N}
```

and

```math
\boxed{
\delta(\sigma_{xy}/B)
=q(\mu_h^2-\mu_e^2)\delta N.
}
```

A photon-created pair and an intrinsic generation-recombination pair therefore move the carrier state along the same one-dimensional direction `(delta n,delta p) proportional to (1,1)`.

## Readout consequence

Let a scalar pair coordinate `x=delta N` have intrinsic GR noise PSD `S_x` and photon signal waveform `x_s`.

Any linear electrical readout of this mode has

```math
y_k=g_k x+n_k,
```

where `g_k` is the longitudinal or Hall gain and `n_k` is independent readout noise.

If intrinsic GR noise dominates (`n_k -> 0`), then

```math
S_{y_k}=|g_k|^2S_x
```

and the matched-filter signal/noise ratio is independent of `g_k`:

```math
\boxed{
\frac{|g_kx_s|^2}{|g_k|^2S_x}
=\frac{|x_s|^2}{S_x}.
}
```

Thus Hall weighting cannot distinguish the physical lineage of two perturbations that occupy the same carrier-state direction.

Using both longitudinal and Hall readouts jointly does not create a second physical state coordinate for pair generation. With independent electronics noise, combining them can improve readout SNR by ordinary sensor fusion, but this is not intrinsic rejection of GR dark fluctuations.

## When Hall information is genuinely additional

If electron and hole fluctuations are independent enough that `(delta n,delta p)` spans two dimensions, the two readouts have different sensitivity vectors and can identify carrier populations/mobilities separately. This is parameter identifiability, not pair-lineage discrimination.

Carrier-resolved photo-Hall methods already exploit exactly this richer two-carrier information to extract majority/minority densities, mobilities, lifetime and recombination coefficients.

## Strong prior art

Gunawan et al., Nature 575, 151-155 (2019), developed carrier-resolved photo-Hall analysis that simultaneously extracts majority/minority density and mobility, recombination lifetime, diffusion length and recombination coefficient from conductivity/Hall information under illumination.

Fundamental bipolar GR-noise theory likewise treats electron and hole density fluctuations jointly rather than as one majority-carrier noise source.

## Stop

```text
Hall readout as additional carrier-parameter observable: ESTABLISHED / USEFUL
Hall readout as intrinsic photon-vs-GR discriminator: NO
fundamental sensitivity gain for neutral pair signal: NO
Experiment branch: DO NOT OPEN
```

The correct abstract statement is that no linear readout can distinguish signal and dark events that create the same stochastic state perturbation solely by changing the observation basis.
