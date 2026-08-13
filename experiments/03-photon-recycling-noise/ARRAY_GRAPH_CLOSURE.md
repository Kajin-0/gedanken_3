# Array graph closure

**Date:** 2026-08-13
**Status:** EXACT LINEAR-EQUILIBRIUM RESULT / GENERAL NETWORK MATHEMATICS IS OLD / DETECTOR APPLICATION UNDER AUDIT

## 1. Symmetric N-pixel exchange model

Let `x_i` denote carrier-number fluctuations in pixel `i` about a common mean `m`.

Local non-transfer loss/birth relaxation is `gamma`. Let `k_ij=k_ji>=0` be the rate of successful carrier-equivalent exchange from pixel `i` to pixel `j` caused, for example, by radiative recombination in one pixel followed by photon reabsorption in the other.

Define the weighted graph Laplacian

```math
L_{ii}=\sum_{j\ne i}k_{ij},
\qquad
L_{ij}=-k_{ij}\;(i\ne j),
```

and

```math
\boxed{M=\gamma I+L.}
```

The fluctuation dynamics are

```math
\dot x=-Mx+\eta.
```

For equilibrium local birth/death plus conservative exchange jumps, the Langevin diffusion matrix is

```math
\boxed{Q_\eta=2mM.}
```

The stationary covariance is therefore

```math
\boxed{P=mI,}
```

because

```math
MP+PM=Q_\eta.
```

Hence all distinct pixels can have zero equal-time covariance even though they are dynamically coupled.

## 2. Exact cross-spectral matrix

With a two-sided angular-frequency PSD convention,

```math
\boxed{
S_x(\omega)
=(M+i\omega I)^{-1}Q_\eta(M-i\omega I)^{-1}
=2mM(M^2+\omega^2I)^{-1}.
}
```

This matrix shares eigenvectors with `M` and the graph Laplacian `L`.

If `L v_a=mu_a v_a`, then mode `a` relaxes at

```math
\boxed{\lambda_a=\gamma+\mu_a}
```

and has PSD

```math
\boxed{
S_a(\omega)=\frac{2m\lambda_a}{\lambda_a^2+\omega^2}.
}
```

The uniform mode has `mu_0=0`, so its corner is exactly `gamma`; exchange does not relax total population.

## 3. Low-frequency fluctuation/response closure

Apply a small steady generation perturbation `g` to the pixels. The mean steady response is

```math
\bar x=M^{-1}g.
```

But the zero-frequency equilibrium noise matrix is

```math
\boxed{S_x(0)=2mM^{-1}.}
```

Therefore the same matrix that determines deterministic DC crosstalk determines zero-frequency spontaneous carrier cross-noise.

For point excitation of pixel `j`,

```math
\boxed{
\frac{\bar x_i}{\bar x_j}
=
\frac{S_{ij}(0)}{S_{jj}(0)}
}
```

for the intrinsic carrier process.

This is a fluctuation-response identity of the minimal equilibrium exchange model, not a new general theorem.

## 4. High-frequency direct-edge limit

For large `omega`,

```math
S_x(\omega)
=\frac{2m}{\omega^2}M+O(\omega^{-4}).
```

Thus, for distinct pixels,

```math
\boxed{
S_{ij}(\omega)
\sim-\frac{2m k_{ij}}{\omega^2}.
}
```

The high-frequency cross-spectrum is therefore sensitive to **direct** exchange edges, while the low-frequency matrix `M^{-1}` includes all direct and indirect paths through the array.

This distinction may be experimentally useful.

## 5. Translationally invariant array

For a periodic uniform array with symmetric displacement-dependent coupling `k_r`, spatial Fourier modes diagonalize the problem. The relaxation rate at spatial wavevector `q` is

```math
\boxed{
\lambda(q)=
\gamma+\sum_r k_r[1-e^{i q\cdot r}].
}
```

For `k_r=k_{-r}`, this is real:

```math
\boxed{
\lambda(q)=
\gamma+\sum_r k_r[1-\cos(q\cdot r)].
}
```

The spontaneous noise of each spatial mode is

```math
\boxed{
S(q,\omega)
=\frac{2m\lambda(q)}{\lambda^2(q)+\omega^2}.
}
```

Hence the mode linewidth dispersion `lambda(q)` is the graph-Laplacian spectrum of pixel exchange.

For a square array with nearest-neighbor rate `k`,

```math
\lambda(q_x,q_y)
=\gamma+2k[2-\cos q_x-\cos q_y].
```

More generally, the nonzero-distance Fourier coefficients of `lambda(q)` recover the exchange kernel `k_r` up to the standard Laplacian sign convention.

Thus a time-resolved dark-noise movie could, in the ideal model, act as passive spatial crosstalk spectroscopy.

## 6. What can and cannot be identified

### Independent readout noise

If ROIC noise is independent pixel to pixel, it adds to auto-spectra but not the intrinsic off-diagonal cross-spectrum. Cross-spectral averaging is therefore naturally resistant to uncorrelated readout noise.

### Common-mode background fluctuations

A spatially uniform common optical or electronic fluctuation drives mainly the `q=0` spatial mode. Nonuniform exchange modes `q!=0` can therefore help separate exchange dynamics from ideal common-mode noise.

### Electrical readout mixing

A measurement matrix that mixes pixel outputs can itself create cross-spectra. It must be independently calibrated; the carrier-exchange interpretation is not unique without this control.

### Carrier diffusion

Carrier diffusion between pixels is also conservative exchange and generates a graph Laplacian. The passive cross-spectrum alone cannot distinguish diffusion from photon recycling if both produce the same coupling kernel.

Potential discriminants include trenches/barriers, optical absorbers, pixel spacing, bias and temperature dependence, and the spatial range of the inferred coupling.

### Photon propagation delay

The direct-jump approximation assumes photon flight/reabsorption is much faster than carrier relaxation. If not, photon states/delays must be retained and the cross-spectrum can acquire extra poles and phase.

## 7. Connection to ordinary HgCdTe crosstalk

Published HgCdTe calculations already predict radiative optical crosstalk between neighboring pixels and percent-level parasitic response for small LWIR pixels. They obtain crosstalk from carrier/photon transport under intentional illumination.

Experiment 03 asks whether the same coupling can be extracted from spontaneous cross-noise and checked against the deterministic response.

The general exchange-noise concept is not new: equilibrium spin-noise spectroscopy has experimentally observed positive low-frequency and negative high-frequency cross-correlation components from exchange coupling. General network inference from equilibrium fluctuations is also established.

Therefore any publication case must rest on a detector-specific capability such as:

1. quantitative agreement between passive cross-noise and independently measured optical crosstalk;
2. recovery of a spatial photon-recycling kernel inaccessible from ordinary single-pixel metrics;
3. a discriminating signature separating optical recycling from electrical/diffusive crosstalk.

Novelty remains unestablished.