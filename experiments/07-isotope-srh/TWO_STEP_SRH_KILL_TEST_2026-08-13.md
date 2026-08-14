# Two-Step SRH Isotope Engineering Kill Test

**Date:** 2026-08-13  
**Status:** NATURAL-TO-HEAVY ENGINEERING LEVER FAILS ROBUSTNESS TEST / ISOTOPE DIAGNOSTIC REMAINS OPEN / NOVELTY NOT ESTABLISHED

## 1. Purpose

The first threshold calculation showed that a small isotope shift can be strongly amplified when a mercury-vacancy capture channel lies near a one-phonon threshold. That result was too optimistic because it treated the phonon/defect energy as sharp and did not require the full SRH cycle to survive competing capture paths.

This step asks whether natural HgCdTe -> heavy-isotope-enriched HgCdTe can still change the SRH cycle rate by at least a factor of two after three effects are included:

1. electron and hole capture are sequential parts of one SRH cycle;
2. an isotope-insensitive bypass channel is present;
3. the relative defect/phonon capture energy has a finite distribution.

Companion code: `numerics/two_step_srh_isotope.py`.

## 2. Sequential SRH cycle

Let the two required capture rates be `r_n` and `r_p`. The cycle rate is

```math
g=\frac{r_n r_p}{r_n+r_p}.
```

If isotope substitution changes them by factors `R_n` and `R_p`, then

```math
\boxed{
\frac{g'}{g}
=\frac{R_nR_p(r_n+r_p)}{R_n r_n+R_p r_p}.
}
```

Thus changing only a capture step that was already much faster than the other step has little effect on the complete SRH cycle. The largest possible isotope leverage occurs when the bottleneck step is isotope-sensitive, or when both steps change together.

## 3. One-phonon phase-space models

### Acoustic cutoff

For `Delta = hbar omega_max-E_b`, the 3-D Maxwell-Boltzmann fraction kinematically able to emit one acoustic phonon is

```math
\Phi_a(\Delta)=
\operatorname{erf}\sqrt{\Delta/kT}
-\frac{2}{\sqrt\pi}\sqrt{\Delta/kT}\,e^{-\Delta/kT},
```

for `Delta>0`, and zero otherwise.

### Optical phonon

For a nearly dispersionless optical phonon use the minimal phase-space proxy

```math
\Phi_o(\Delta)\propto
\sqrt{\Delta}\,e^{-\Delta/kT},
```

again for `Delta>0`.

These are intentionally not claimed to be microscopic capture coefficients. They isolate the strongest kinematic isotope leverage.

## 4. Fixed bypass model

A critical correction to the first stress test is that the bypass cannot be allowed to shrink automatically when the one-phonon channel approaches threshold.

Write one capture rate as

```math
r=B+A\Phi.
```

Define `f_ref` to be the fraction of the natural-material capture rate supplied by the isotope-sensitive term at a reference detuning `Delta_ref=1 meV`:

```math
f_{ref}=\frac{A\Phi_{ref}}{B+A\Phi_{ref}}.
```

This fixes the absolute bypass `B/A`. It is then held fixed while defect energy and isotope mass are varied.

This is much more conservative and physically meaningful than holding the sensitive fraction fixed arbitrarily close to threshold.

## 5. Natural-to-heavy isotope shift

Using the reduced-mass harmonic estimate for an HgTe-like mode:

```text
natural -> all-heavy frequency ratio = 0.991069
```

Therefore

```text
HgTe-like acoustic cutoff:
10.560 meV -> 10.466 meV
shift       = -0.094 meV

HgTe-like LO mode at 143 cm^-1:
17.730 meV -> 17.571 meV
shift       = -0.158 meV
```

The relevant practical isotope shift is therefore only a few tenths of a meV at most.

## 6. Energy-distribution convolution

Let the relative capture energy have a Gaussian spread `sigma_E`. This can represent, in reduced form, defect-level dispersion, phonon-energy dispersion, alloy disorder, or any combination that broadens the one-phonon resonance/cutoff.

The phase-space functions are convolved over that Gaussian before the natural/heavy capture-rate ratio is formed.

## 7. Acoustic-cutoff result

For the HgTe-like `10.56 meV` acoustic cutoff, the natural->heavy shift is only `0.094 meV`.

For the most favorable case in which **both** sequential capture steps have the same isotope-sensitive reduction, a twofold SRH-cycle suppression requires the one-phonon channel to dominate the natural capture rate very strongly.

Using `Delta_ref=1 meV`, the minimum required natural sensitive fraction is approximately:

```text
sigma_E = 0       -> f_ref >= 0.965
sigma_E = 0.05 meV -> f_ref >= 0.973
sigma_E = 0.10 meV -> f_ref >= 0.984
sigma_E = 0.20 meV -> f_ref >= 0.997
sigma_E = 0.25 meV -> f_ref >= 0.999
```

Therefore the acoustic-threshold engineering effect is not robust. Even a few-percent isotope-insensitive bypass kills the desired factor-of-two change.

## 8. Optical-phonon result

The 143-cm^-1 HgTe-like mode has a somewhat larger natural->heavy shift of about `0.158 meV`, so the single-optical-phonon case is more favorable.

Without broadening, the threshold can indeed create a large isotope effect. But the required sensitive fraction rises rapidly with energy spread.

For the same `Delta_ref=1 meV` definition:

```text
sigma_E = 0       -> f_ref >= 0.689 for >=2x suppression
sigma_E = 0.10 meV -> f_ref >= 0.841
sigma_E = 0.20 meV -> f_ref >= 0.936
sigma_E = 0.30 meV -> f_ref >= 0.966
```

An experimental HgCdTe Raman study reports an HgTe-like LO FWHM of `8.9 cm^-1` in its better MBE sample. If that width is used only as an **order-of-magnitude stress proxy** for the capture-energy broadening,

```text
FWHM = 8.9 cm^-1 ~= 1.10 meV
Gaussian sigma_E ~= 0.47 meV.
```

At this stress scale the model requires

```math
\boxed{f_{ref}\gtrsim0.995}
```

for a twofold natural->heavy SRH-rate reduction even when **both** capture steps are equally isotope-sensitive.

Illustrative best-tuned results at `sigma_E ~= 0.47 meV` are:

```text
f_ref = 0.90 -> g_heavy/g_natural ~= 0.745 -> lifetime gain ~1.34x
f_ref = 0.99 -> g_heavy/g_natural ~= 0.565 -> lifetime gain ~1.77x
f_ref = 1.00 -> much larger effects remain possible in the artificial zero-bypass limit
```

The measured Raman linewidth is not asserted to equal the microscopic capture spectral function. It is deliberately used as a robustness stress. A definitive result would require a first-principles capture spectral density or direct isotope experiment.

## 9. One-sensitive-step penalty

The result above is already an upper bound because it lets both capture steps receive the same favorable isotope reduction.

If only one step changes, the full SRH cycle responds less. Let

```math
b=r_{n,0}/r_{p,0}.
```

For only electron capture changing by `R`,

```math
\frac{g'}{g}=\frac{R(b+1)}{Rb+1}.
```

If the isotope-sensitive step is the fast non-bottleneck step (`b>>1`), even a large microscopic capture-coefficient change produces little lifetime improvement.

Thus any practical dark-current proposal must establish not merely a large isotope effect on one capture coefficient, but a large isotope effect on the **rate-limiting part of the complete SRH cycle**.

## 10. Full light-to-heavy contrast is different

The full stable-isotope endpoint span of an HgTe-like mode is about `3.3%`, corresponding to roughly `0.58 meV` for a 143-cm^-1 optical mode. This is several times larger than the natural->heavy shift.

At the same ~0.47-meV broadening stress, the reduced-order model can still produce multi-fold rate changes across the full light->heavy span when the one-phonon channel supplies most of the natural capture.

Therefore isotope substitution remains potentially powerful as a **causal spectroscopy experiment** even though natural->heavy enrichment is a weak engineering lever.

## 11. Physical interpretation

The first threshold result was real but incomplete:

```text
small phonon shift
+ exact one-phonon threshold
-> potentially huge local rate ratio.
```

The full detector problem adds two regularizers:

```text
alternative capture path + energy broadening.
```

Because the practical natural->heavy HgTe-like optical shift is only ~0.16 meV, the threshold enhancement survives as a factor-of-two dark-current engineering effect only if the dominant capture spectrum is exceptionally pure and sharp.

HgCdTe is a random alloy, and optical studies directly observe compositional disorder and broad phonon features. That does not prove the microscopic vacancy-capture spectral width, but it makes an ultra-sharp ensemble threshold a strong burden of proof rather than a safe design assumption.

## 12. Disposition

```text
Generic isotope suppression of SRH: REJECTED
Macroscopic phononic-crystal suppression: REJECTED
Natural->heavy isotope enrichment as a robust >2x dark-current engineering lever: DO NOT PURSUE BY DEFAULT
One-phonon threshold sensitivity: RETAIN
Full light-vs-heavy isotope contrast as a mechanism diagnostic: RETAIN / ACTIVE
Novelty: NOT ESTABLISHED
Paper drafting: NOT AUTHORIZED
```

The engineering path should be reopened only if microscopic calculations or measurements show all three:

1. a dominant Hg-vacancy capture channel within ~0.1-0.2 meV of an isotope-shifted one-phonon threshold;
2. an effective capture-energy width far below the ~meV optical-phonon broadening seen in ordinary HgCdTe Raman spectra;
3. isotope-insensitive bypass below roughly the percent level for the rate-limiting SRH step.

## 13. Next hard question

The natural next experiment is no longer "can heavy isotopes make a much better detector?"

It is:

> **Can light-vs-heavy isotope substitution be used as a causal perturbation that distinguishes single-phonon Hg-vacancy SRH from radiative, Auger, tunneling, and other lifetime mechanisms?**

That question needs an isotope-differential lifetime/dark-current signature that remains identifiable after isotope-induced bandgap shifts and ordinary sample-to-sample defect-density variation are included.
