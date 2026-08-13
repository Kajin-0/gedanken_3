# Current State — Experiment 05: Active Volume versus Optical Bandwidth

**Date:** 2026-08-13  
**Status:** ACTIVE PROVISIONAL / FIRST RESONANT SURROGATE PASSED / GENERAL BOUND OPEN / NOVELTY NOT ESTABLISHED

## Device-engineer question

Optical structures can concentrate light into an electrically small absorber and thereby reduce bulk dark generation. Can the active semiconductor volume be made arbitrarily small while preserving both high optical absorptance and finite spectral acceptance?

## First nontrivial result

For one critically coupled resonance,

```math
A(\omega)=\frac{4\gamma_e\gamma_i}{(\omega-\omega_0)^2+(\gamma_e+\gamma_i)^2}
```

and at `gamma_e=gamma_i`,

```math
A(\omega_0)=1,
\qquad
\Delta\omega_{FWHM}=4\gamma_i.
```

Under the reduced-order assumptions

```math
\gamma_i=\kappa V,
\qquad
G_d=g_dV,
```

bulk-dark-current shot noise gives

```math
NEP_{pk}^2=2(\hbar\omega_0)^2g_dV,
```

hence

```math
\boxed{
NEP_{pk}^2/\Delta\omega_{FWHM}
=(\hbar\omega_0)^2g_d/(2\kappa).
}
```

Thus the toy model permits arbitrarily good **on-resonance** NEP as `V -> 0`, but only while the optical acceptance bandwidth collapses in direct proportion to `V`.

A many-resonance tiling does not evade the result in the same family because

```math
\sum_j\Delta\omega_j=4\kappa\sum_jV_j.
```

## Critical limitation

The step above is not a universal theorem. A large passive lossless lens, taper, antenna, or waveguide can alter the local optical field as the semiconductor volume changes, so the assumption of fixed `kappa` can fail.

The active question is therefore whether established electromagnetic absorption/sum-rule bounds can be converted into a lower bound on active semiconductor volume—or bulk dark-generation noise—for a prescribed set of accepted spatial/spectral optical modes **while arbitrary passive lossless collection optics are allowed**.

## Strong comparator

Any claimed bound must survive:

```text
large lossless collection optic
+ small electrically active absorber
+ waveguide or taper coupling
+ multiple resonances
```

If such an architecture can keep fixed finite-band absorption while driving active semiconductor volume to zero without spending another resource, the present hypothesis dies.

## Prior-art boundary

Already established:

- thin resonant-cavity photodiodes can reduce dark current while retaining high peak quantum efficiency;
- resonant-cavity detectors are spectrally selective/narrowband;
- antenna/meta-lens coupled infrared detectors reduce active electrical volume and improve NEP/detectivity;
- passive optical absorption has geometry-independent per-volume and power-bandwidth bounds.

Do not claim these ingredients as new.

## Next hard step

Formulate the strongest possible passive-optics problem:

> Given a required absorptance function over specified input modes and frequencies, what is the minimum lossy semiconductor volume when arbitrary lossless reciprocal structures are free resources?

Then translate any rigorous optical lower bound into dark-generation current/noise only after the optical theorem is secure.

If the optical bound necessarily depends on total collection-structure volume rather than active semiconductor volume, document that failure and close the detector claim rather than hiding the resource.