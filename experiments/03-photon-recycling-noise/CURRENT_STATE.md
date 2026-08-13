# Current State — Experiment 03: Can spontaneous pixel noise reveal photon recycling?

**Date:** 2026-08-13
**Status:** ACTIVE / POSSIBLE DETECTOR-APPLICATION NOVELTY / GENERAL EXCHANGE-NOISE MATHEMATICS IS PRIOR ART

## Device question

HgCdTe photon recycling can transfer a radiative recombination photon from one pixel to a neighboring pixel, where it is reabsorbed and creates a new electron-hole pair.

Question:

> Can the spontaneous electrical noise of two neighboring pixels reveal and quantify this photon exchange without deliberately illuminating one pixel?

This is a device-physics / characterization question. The general statistical fact that conservative exchange coupling produces cross-correlated equilibrium noise is not new.

## Prior-art gate already established

1. HgCdTe photon recycling and optical crosstalk are established. Jóźwikowska & Jóźwikowski, *Optical and Quantum Electronics* 51, 85 (2019), DOI 10.1007/s11082-019-1781-4, model radiative recombination photons emitted by one HgCdTe pixel and absorbed by a neighbor. Their calculated neighboring-pixel parasitic response is at roughly the percent level for small LWIR pixels.

2. Cross-correlation noise spectroscopy of exchange coupling is established in another physical system. Roy et al., *Scientific Reports* 5, 9573 (2015), DOI 10.1038/srep09573, show that equilibrium spin exchange gives a cross-spectrum with a narrow positive component and broader negative component, a difference of equal-area Lorentzians with zero integrated cross-correlation.

Therefore do **not** claim the sign-changing exchange spectrum as new statistical mechanics.

A targeted detector-array search has not yet located a linear HgCdTe/photodiode-array experiment that uses spontaneous pixel current cross-spectra to infer radiative photon-recycling coupling. Novelty remains unestablished.

## Minimal symmetric two-pixel model

Let `x1,x2` be excess carrier-number fluctuations about equal mean `m`.

Local birth/death relaxation occurs at rate `gamma`. Radiative exchange from either pixel to the other occurs at rate `k` per carrier. A transfer event removes one excitation from the emitting pixel and creates one in the neighbor.

The linear drift is

```math
\dot x=
-\left[
\gamma I+k
\begin{pmatrix}1&-1\\-1&1\end{pmatrix}
\right]x+\eta.
```

The common and difference modes have exact relaxation rates

```math
\boxed{\lambda_+=\gamma,\qquad \lambda_-=\gamma+2k.}
```

Exchange conserves the total carrier population, so it leaves the common mode unchanged but speeds relaxation of the difference mode.

For the chemical-Langevin birth/death/exchange process, the stationary equal-time covariance is

```math
\boxed{P=mI.}
```

Thus

```math
\boxed{\operatorname{Cov}(x_1,x_2)|_{t=0}=0}
```

even though the pixels dynamically exchange excitations.

## Exact intrinsic spectra

Using a two-sided angular-frequency PSD convention,

```math
S_+(\omega)=\frac{2m\gamma}{\gamma^2+\omega^2},
```

```math
S_-(\omega)=\frac{2m(\gamma+2k)}{(\gamma+2k)^2+\omega^2}.
```

Therefore

```math
\boxed{
S_{12}(\omega)=
m\left[
\frac{\gamma}{\gamma^2+\omega^2}
-\frac{\gamma+2k}{(\gamma+2k)^2+\omega^2}
\right].
}
```

Consequences:

```math
S_{12}(0)>0,
```

```math
S_{12}(\omega)<0\quad\text{at sufficiently high frequency},
```

and the exact zero is

```math
\boxed{\omega_\times=\sqrt{\gamma(\gamma+2k)}.}
```

The integrated cross-spectrum is zero, consistent with zero equal-time covariance.

Thus static frame-to-frame covariance can miss exchange that is visible in a frequency-resolved cross-spectrum.

## Asymmetric equilibrium result

Let local relaxation rates be `gamma1,gamma2`, transfer rates `k12,k21`, equilibrium means `m1,m2`, and impose detailed balance

```math
k_{12}m_1=k_{21}m_2\equiv J.
```

Let `lambda1,lambda2` be the two positive relaxation eigenrates. Their sum and product are

```math
\lambda_1+\lambda_2
=\gamma_1+\gamma_2+k_{12}+k_{21},
```

```math
\lambda_1\lambda_2
=\gamma_1\gamma_2+\gamma_1k_{21}+\gamma_2k_{12}.
```

The exact real cross-spectrum is

```math
\boxed{
S_{12}(\omega)=
\frac{2J(\lambda_1\lambda_2-\omega^2)}
{(\lambda_1\lambda_2-\omega^2)^2
+(\lambda_1+\lambda_2)^2\omega^2}.
}
```

Hence the sign reversal survives unequal pixels:

```math
\boxed{\omega_\times=\sqrt{\lambda_1\lambda_2}.}
```

This is the geometric mean of the two coupled relaxation rates.

## Deterministic/noise closure for identical pixels

Now deliberately illuminate pixel 1 with a small steady generation perturbation `g` and leave pixel 2 unilluminated. The steady linear equations give

```math
\frac{x_2}{x_1}
=\boxed{c_{dc}=\frac{k}{\gamma+k}}.
```

This is the ordinary small-signal neighboring/self crosstalk ratio of the two-state model.

For the intrinsic equilibrium noise spectra,

```math
\boxed{
\frac{S_{12}(0)}{S_{11}(0)}
= c_{dc},
}
```

while

```math
\boxed{
\lim_{\omega\to\infty}
\frac{S_{12}(\omega)}{S_{11}(\omega)}
=-c_{dc}.
}
```

Thus the same coupling parameter predicts both conventional illuminated crosstalk and passive cross-noise structure.

Equivalently,

```math
\frac{k}{\gamma}=\frac{c_{dc}}{1-c_{dc}},
```

```math
\frac{\lambda_-}{\lambda_+}
=\frac{1+c_{dc}}{1-c_{dc}},
```

and

```math
\frac{\omega_\times}{\gamma}
=\sqrt{\frac{1+c_{dc}}{1-c_{dc}}}.
```

This is a falsifiable fluctuation/response closure for the minimal exchange model.

## Important limitation

A sign-changing cross-spectrum establishes **exchange-like coupling**, not photon recycling uniquely.

Carrier diffusion or another conservative carrier-transfer mechanism can generate the same mathematics. Electrical readout mixing can also create correlations, although simple instantaneous readout mixing generally has a different spectral structure.

Photon recycling must therefore be identified by additional controls such as:

- optical isolation/trenches or absorbing barriers that change photon propagation while minimally changing carrier transport;
- pixel spacing and geometry;
- bias/temperature dependence of radiative efficiency;
- comparison with deterministic optical-crosstalk measurements;
- spatial range of the inferred coupling kernel.

Independent readout noise adds to individual auto-spectra but does not create the intrinsic cross-spectrum, so cross-correlation averaging can suppress uncorrelated readout noise.

## Next step

Extend to an `N`-pixel array. For symmetric photon exchange on a pixel graph, determine whether spatial Fourier/eigenmode noise spectra can reconstruct the coupling kernel and whether that provides a practical signature that differs from carrier diffusion and common-mode electronics.

Do not build a manuscript yet. The general exchange-noise theory is old; only a genuinely detector-specific, quantitatively useful consequence can justify publication.