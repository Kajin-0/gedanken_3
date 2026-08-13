# Photoconductor information bandwidth

**Date:** 2026-08-13
**Status:** exact single-pole result; useful device interpretation; novelty not established.

## Model

Use a standard single-lifetime photoconductor response

```math
R(\omega)=\frac{R_0}{1+i\omega\tau}.
```

Model the measured output noise as a GR Lorentzian plus a white Johnson/readout floor,

```math
S_n(\omega)=\frac{S_{GR,0}}{1+\omega^2\tau^2}+S_W.
```

For optical event spectrum `P(omega)`, the optimum-filter information spectrum is

```math
\mathcal I(\omega)=\frac{|R(\omega)P(\omega)|^2}{S_n(\omega)}.
```

Define

```math
\gamma=S_{GR,0}/S_W.
```

Then exactly

```math
\boxed{\mathcal I(\omega)=
\frac{R_0^2}{S_{GR,0}+S_W}
\frac{|P(\omega)|^2}{1+\omega^2\tau_{info}^2}}
```

with

```math
\boxed{\tau_{info}=\frac{\tau}{\sqrt{1+\gamma}}
=\tau\sqrt{\frac{S_W}{S_{GR,0}+S_W}}.}
```

Thus the raw responsivity time constant and the detector/noise information time are generally different.

- White-output-noise dominated: `tau_info -> tau`.
- GR dominated: `tau_info << tau` because signal and GR noise share the same lifetime pole and whitening largely cancels it.
- Ideal GR-only limit: the lifetime pole cancels completely; other physical bandwidth limits must then regularize the high-frequency information.

## Finite optical pulse and timing information

For

```math
P(\omega)=1/(1+i\omega\tau_p),
```

```math
\mathcal I(\omega)=I_0/
[(1+\omega^2\tau_p^2)(1+\omega^2\tau_{info}^2)].
```

The normalized full-template covariance is

```math
R(\Delta)=
\frac{\tau_p e^{-|\Delta|/\tau_p}
-\tau_{info}e^{-|\Delta|/\tau_{info}}}
{\tau_p-\tau_{info}}.
```

Direct integration gives

```math
\boxed{J_\theta/\rho_\infty^2=1/(\tau_p\tau_{info})}
```

for arrival-time Fisher information `J_theta`. Hence

```math
\boxed{\tau_{tim}=\sqrt{\tau_p\tau_{info}}}
```

and

```math
\boxed{\sigma_\theta\ge\sqrt{\tau_p\tau_{info}}/\rho_\infty.}
```

This is the classical RMS/effective-bandwidth timing result written in detector/noise variables, not a new general timing theorem.

## HgCdTe scale check

Eppeldauer and Martin, J. Res. NIST 106, 577-587 (2001), DOI 10.6028/jres.106.024, report a PC HgCdTe detector with approximately `16 V/W` responsivity and `0.34 nW/sqrt(Hz)` measured NEP, dominated by GR noise, while detector Johnson and preamplifier floors were about `0.5` and `0.6 nV/sqrt(Hz)`.

Using those values only as a scale estimate:

```text
total detector-equivalent noise ~ 5.44 nV/sqrt(Hz)
combined white floor            ~ 0.781 nV/sqrt(Hz)
inferred GR/white power ratio   ~ 47.5
tau_info/tau                    ~ 0.144
```

This is not a timing fit to that detector; the paper does not provide the needed single-pole GR corner. It only shows that the noise-ratio factor can be large in a real HgCdTe photoconductor.

## Meaning for a device engineer

A `-3 dB` responsivity bandwidth answers how quickly signal amplitude rolls off. It does not necessarily answer how quickly **signal-to-noise information** rolls off after optimal whitening.

For transient tasks the detector-only spectral object is effectively

```math
|R(\omega)|^2/S_n(\omega)=1/NEP^2(\omega)
```

(up to the chosen input/output units). A scalar low-frequency `D*` plus a standalone `-3 dB` bandwidth does not specify this spectrum.

## Prior-art boundary

Do not claim novelty from the optimum-filter principle. Prior art already covers optimum timing with arbitrary stationary detector noise, finite sampled processing, RMS-bandwidth timing bounds, and photoconductor response/GR-noise/NEP tradeoffs. Older photoconductor literature also contains detectivity-bandwidth optimization.

Current disposition:

```text
physical interpretation: useful
closed-form mapping: useful
general optimum-filter principle: old
novelty: not established
```

## Next question

Use a measured HgCdTe spectrum containing GR + white + 1/f noise and ask whether three experimentally accessible bandwidths materially differ:

1. responsivity bandwidth;
2. frequency-dependent NEP bandwidth;
3. optimum timing RMS bandwidth.

If this reduces completely to conventional detector characterization with no new experimental consequence, close this branch as a pedagogical result rather than forcing another paper.