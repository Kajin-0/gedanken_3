# Experiment 07 — DLTS Pivot

**Date:** 2026-08-14
**Status:** ACTIVE / TOTAL-LIFETIME ROUTE REJECTED / DIRECT CAPTURE-COEFFICIENT TEST RETAINED

## Why the lifetime route failed

Hg isotope exchange on practical anneal times favors a sub-micron modified layer. For a thin slab,

```math
1/tau_eff ~= 1/tau_bulk + 2S/d.
```

At `d=0.2 um`, even `S=200 cm/s` gives `tau_surface~50 ns`; `S=3000 cm/s` gives only ~3.3 ns. This is far shorter than the microsecond bulk-SRH regime targeted by Experiment 07. Therefore a thin isotope-exchanged film is a poor direct bulk-lifetime specimen unless extraordinary carrier confinement/passivation is added.

## Direct trap spectroscopy is the stronger observable

HgCdTe DLTS can separately determine trap concentration, activation energy and carrier capture cross section. For a filling transient,

```math
tau_c,p^{-1}=C_p p,
```

or similarly `tau_c,n^{-1}=C_n n`.

Thus

```math
C_p=1/(p tau_c,p).
```

The isotope experiment should target `C_p(M,T)` and/or `C_n(M,T)` directly rather than total lifetime.

Advantages:

1. Hg-vacancy density primarily changes DLTS amplitude/SNR rather than the ideal single-trap capture coefficient.
2. Competing radiative/Auger lifetimes do not dilute the measured capture coefficient.
3. Surface recombination does not need to be slower than bulk SRH lifetime.
4. Both capture steps predicted in the narrow-gap HgCdTe single-optical-phonon model can in principle be tested separately.

## Isotope depth and depletion width are compatible

For a one-sided depletion estimate

```math
W=sqrt[2 epsilon V/(qN)].
```

Using `epsilon_r~20` gives representative values:

```text
N=1e15 cm^-3, V=20 mV -> W~0.21 um
N=1e15 cm^-3, V=50 mV -> W~0.33 um
N=1e16 cm^-3, V=20 mV -> W~0.066 um
N=1e16 cm^-3, V=50 mV -> W~0.105 um
```

Therefore a `0.2-0.5 um` isotope-modified surface layer can fully contain a shallow DLTS depletion region.

## Preferred first experiment

1. Use sister pieces from one narrow-gap HgCdTe wafer, with a regime where V_Hg-related traps are measurable.
2. Precondition pieces with identical Hg-rich thermal histories.
3. Apply matched natural-Hg and enriched-Hg anneals.
4. Verify isotope uptake/profile by SIMS on sacrificial pieces and Raman on measured pieces.
5. Fabricate matched shallow MIS/diode structures after anneal.
6. Measure C-V/Hall carrier density and DLTS trap energy, concentration and capture kinetics.
7. Compare `C_p(T)` and, if accessible, `C_n(T)` against measured Raman shifts.
8. Use multiple devices per material piece to estimate device-processing scatter.

The relevant isotope response is

```math
K_C(T)=d ln C/d ln omega.
```

For the minimal one-optical-phonon phase-space model

```math
C propto sqrt(Delta) exp[-Delta/(kT)],
Delta=hbar omega-E_b,
```

```math
K_C(T)=hbar omega[1/(2Delta)-1/(kT)],
```

with the opposite sign to the lifetime derivative. The same predicted temperature zero crossing remains:

```math
kT_x=2Delta
```

in the spontaneous-emission approximation.

## Prior-art boundary

DLTS measurement of trap capture cross sections is established, including narrow-gap HgCdTe. General isotope-dependent nonradiative lifetimes and isotope-based defect identification are also established. The remaining question is specifically whether the predicted mercury-vacancy one-optical-phonon capture channel in narrow-gap HgCdTe shows a reversible isotope-dependent capture coefficient with the expected Raman and temperature dependence.

Novelty is not established. Do not begin manuscript construction.