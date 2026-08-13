# GR lifetime scaling classes

**Date:** 2026-08-13
**Status:** EXACT SCALING RESULT / CLASSICAL D*-BANDWIDTH CONNECTION / NOVELTY NOT CLAIMED

Use a short optical pulse and a first-order photoconductor whose low-frequency signal responsivity scales as `R0 proportional tau`. Model the measured noise PSD as

```math
S_n(omega)=\frac{G tau^m}{1+omega^2 tau^2}+W,
```

where `W` is an approximately lifetime-independent white floor and `G tau^m` is the low-frequency GR plateau.

Then

```math
I(omega)
=\frac{C tau^2}{W(1+C_G tau^m)}
\frac{1}{1+omega^2 tau_I^2},
```

with

```math
\boxed{tau_I=\frac{tau}{\sqrt{1+C_G tau^m}}}.
```

For GR-dominated operation,

```math
\boxed{tau_I proportional tau^(1-m/2)}.
```

For a sufficiently short optical pulse, the eventual matched-filter information scales the same way:

```math
rho_inf^2 proportional tau/[sqrt(1+C_G tau^m)]
          proportional tau^(1-m/2)
```

in the GR-dominated asymptote.

Interpretation:

- `m=0`: GR plateau independent of lifetime -> `tau_I proportional tau`.
- `m=1`: equilibrium carrier population roughly fixed while relaxation time changes -> GR plateau `proportional tau`, so `tau_I proportional sqrt(tau)`.
- `m=2`: background-generated carrier population itself grows `proportional tau` -> GR plateau `proportional tau^2`, so `tau_I` approaches a constant and the short-pulse eventual information also saturates.
- `m>2`: mathematically, the optimally whitened information time can decrease as raw lifetime increases; whether such a physical regime exists requires a specific carrier/noise model.

The `m≈2` background-limited behavior is closely related to classical photoconductor detectivity-bandwidth invariants. It must not be presented as new physics.

For a finite exponential optical pulse with time `tau_p`, replace the short-pulse information integral by

```math
rho_inf^2 = I0/[2(tau_p+tau_I)],
```

and the normalized timing covariance is

```math
R(Delta)=
[tau_p exp(-|Delta|/tau_p)-tau_I exp(-|Delta|/tau_I)]
/(tau_p-tau_I).
```

Its local curvature obeys

```math
\boxed{R''(0)=-1/(tau_p tau_I)},
```

so the local timing scale is `sqrt(tau_p tau_I)`.

The useful detector-facing distinction is therefore between raw lifetime, GR-noise scaling, and the noise-whitened timing scale. Novelty of this interpretation remains unestablished.