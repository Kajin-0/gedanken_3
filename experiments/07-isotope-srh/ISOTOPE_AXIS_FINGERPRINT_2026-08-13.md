# Isotope-Axis Fingerprint for HgCdTe SRH Capture

**Date:** 2026-08-13  
**Status:** DIAGNOSTIC HYPOTHESIS / REDUCED-MASS FINGERPRINT DERIVED / NOVELTY NOT ESTABLISHED

## 1. Revised purpose

The robust dark-current-engineering claim failed the two-step SRH stress test. Natural->heavy isotope shifts are too small to guarantee a large lifetime improvement once finite energy broadening and bypass capture are admitted.

A more defensible use of isotopes is as a **causal perturbation of the phonon spectrum**.

The question is:

> Can independent Hg, Cd, and Te isotope substitutions identify which lattice vibration controls a mercury-vacancy capture step by comparing the isotope derivatives of lifetime or dark current?

This does not require a large engineering improvement. It requires a reproducible isotope-dependent rate and a branch-specific mass fingerprint.

## 2. Diatomic reduced-mass result

For an idealized HgTe-like vibration,

```math
\omega\propto\mu^{-1/2},
\qquad
\mu=\frac{M_{Hg}M_{Te}}{M_{Hg}+M_{Te}}.
```

Therefore

```math
\frac{\partial\ln\omega}{\partial\ln M_{Hg}}
=-\frac12\frac{M_{Te}}{M_{Hg}+M_{Te}},
```

and

```math
\frac{\partial\ln\omega}{\partial\ln M_{Te}}
=-\frac12\frac{M_{Hg}}{M_{Hg}+M_{Te}}.
```

With natural atomic weights `M_Hg=200.59` and `M_Te=127.60`,

```text
d ln omega / d ln M_Hg = -0.1944
d ln omega / d ln M_Te = -0.3056
```

so

```math
\boxed{
\frac{\partial\ln\omega/\partial\ln M_{Hg}}
{\partial\ln\omega/\partial\ln M_{Te}}
=\frac{M_{Te}}{M_{Hg}}
\approx0.636.
}
```

For a CdTe-like mode,

```text
d ln omega / d ln M_Cd = -0.2658
d ln omega / d ln M_Te = -0.2342
```

and

```math
\boxed{
\frac{\partial\ln\omega/\partial\ln M_{Cd}}
{\partial\ln\omega/\partial\ln M_{Te}}
=\frac{M_{Te}}{M_{Cd}}
\approx1.135.
}
```

The two branch fingerprints are therefore qualitatively different.

## 3. Why the unknown capture nonlinearity cancels

Suppose a capture rate near a one-phonon feature can be written locally as

```math
r=r(\omega),
```

with an arbitrary and possibly very steep dependence on phonon frequency.

Then

```math
\frac{\partial\ln r}{\partial\ln M_a}
=\frac{\partial\ln r}{\partial\ln\omega}
\frac{\partial\ln\omega}{\partial\ln M_a}.
```

For two isotope axes acting on the same mode, the unknown first factor cancels:

```math
\boxed{
\frac{\partial\ln r/\partial\ln M_a}
{\partial\ln r/\partial\ln M_b}
=
\frac{\partial\ln\omega/\partial\ln M_a}
{\partial\ln\omega/\partial\ln M_b}.
}
```

If the measured lifetime is controlled by that capture rate (`tau ~ 1/r`), the same ratio holds for lifetime derivatives because the common minus sign cancels.

This is only exact for one dominant phonon coordinate and one rate-limiting capture step. Mixed modes or multiple parallel capture channels produce weighted combinations rather than a single ratio.

## 4. Finite enrichment predictions

Simple reduced-mass estimates give:

### HgTe-like mode

```text
Hg only: natural Hg -> 204Hg, Te natural
omega'/omega ~= 0.99675   (-0.325%)

Te only: natural Te -> 130Te, Hg natural
omega'/omega ~= 0.99434   (-0.566%)

both heavy:
omega'/omega ~= 0.99107   (-0.893%)
```

### CdTe-like mode

```text
Cd only: natural Cd -> 116Cd, Te natural
omega'/omega ~= 0.99175   (-0.825%)

Te only: natural Te -> 130Te, Cd natural
omega'/omega ~= 0.99567   (-0.433%)

both heavy:
omega'/omega ~= 0.98738   (-1.262%)
```

Thus separate cation and Te enrichment is more informative than only comparing fully natural and fully heavy material.

## 5. Strong experimental closure

The actual phonon modes in ternary HgCdTe are not pure diatomic oscillators. Therefore the preferred experiment should not rely only on reduced-mass predictions.

For every isotope sample measure:

1. Raman/infrared phonon frequencies and linewidths;
2. bandgap/cutoff energy;
3. carrier lifetime and/or dark generation current;
4. vacancy/trap density by the best available independent defect measurement.

Then test whether the lifetime change follows the **measured phonon shift** with the isotope-axis ratio expected for the mode character.

This makes the phonon measurement an internal calibration of the isotope perturbation.

## 6. Mechanism controls

A phonon-assisted SRH interpretation should satisfy more than `tau` changing with isotope mass.

Required controls:

```text
A. phonon tracking
   lifetime/dark-current change follows a measured lattice-mode shift.

B. electronic-energy control
   measure isotope-dependent bandgap/cutoff shifts and correct for the known
   sensitivity of radiative/Auger/tunneling rates to Eg.

C. defect-density control
   isotope samples must not simply contain different mercury-vacancy densities.

D. isotope-axis fingerprint
   Hg, Cd and Te enrichment should follow the mode-character sensitivity,
   not an arbitrary sample-to-sample pattern.

E. temperature dependence
   a one-phonon threshold should show a characteristic change as thermal carrier
   kinetic energy and phonon occupation change.
```

Radiative or Auger recombination can still have isotope dependence indirectly through bandgap/electron-phonon renormalization. Therefore an isotope effect alone does not identify SRH.

## 7. Prior-art status

Targeted searching found extensive prior art on:

- semiconductor isotope effects on phonons and electron-phonon properties;
- isotope purification for spin/coherence physics;
- hydrogen/deuterium isotope effects in defect passivation and bond breaking;
- multiphonon nonradiative defect capture;
- HgCdTe mercury-vacancy SRH capture.

The search did not identify a direct HgCdTe experiment using independent elemental isotope substitutions as a differential fingerprint of the phonon branch controlling SRH capture.

That absence is not proof of novelty. Do not use priority language.

## 8. Disposition

```text
heavy-isotope dark-current engineering: NOT ROBUST / DEFAULT STOP
isotope differential spectroscopy of Hg-vacancy SRH: RETAIN
branch-specific Hg/Cd/Te mass fingerprint: RETAIN AS TESTABLE PREDICTION
novelty: NOT ESTABLISHED
paper drafting: NOT AUTHORIZED
```

## 9. Next hard step

Build the smallest **identifiability model** that includes four lifetime channels,

```math
1/tau_total = 1/tau_SRH + 1/tau_rad + 1/tau_Auger + 1/tau_other,
```

and lets isotope substitution perturb:

1. the candidate SRH capture coefficient through the measured phonon shift;
2. the bandgap through an independently measured isotope shift;
3. the defect density as a nuisance parameter.

Determine how large and how precise the isotope-dependent lifetime signal must be before the phonon-branch fingerprint is distinguishable from ordinary bandgap and sample-to-sample changes.