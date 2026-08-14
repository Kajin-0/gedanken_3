# Electron detuning closure and observability window

**Date:** 2026-08-14
**Status:** OVERDETERMINED SINGLE-PHONON TEST DERIVED / 20-40 K WINDOW PLAUSIBLE / TARGET C_n STILL NOT NUMERICALLY FIXED / NOVELTY NOT ESTABLISHED

## 1. Primary target remains electron capture

The 2026 JETP mercury-vacancy calculation states that electron capture is substantially slower than hole capture and governs the SRH recombination rate, as in bulk narrow-gap HgCdTe. Therefore detector relevance requires the isotope experiment to target `C_n`; `C_p` is secondary.

The 2024 JETP bulk calculation establishes the adjacent mechanism: for ~40-meV-gap HgCdTe, both carrier captures can occur by single optical phonon emission and Hg-vacancy SRH can determine total lifetime for sufficiently high recombination-center density.

Do not infer the target narrow-gap `C_n` from a hole cross section.

## 2. Broad observability bracket for C_n

An exact target `C_n` value has not been recovered from an accessible primary full text. A 2025 primary calculation for wider-gap HgCdTe gives a useful scale only: the low-temperature conduction-electron capture coefficient on the `A_2^-2` Hg-vacancy level falls from about `1e-8 cm^3/s` at `x=0.21` to about `1e-12 cm^3/s` at `x=0.25` as the vacancy level moves farther from the conduction band (Bekin & Kozlov, Semiconductors 59, 458-465, 2025, DOI 10.61011/FTP.2025.08.62187.8701).

Do **not** extrapolate that trend into the 40-meV single-phonon regime. For metrology only, use `C_n=1e-12...1e-8 cm^3/s` as a deliberately broad bracket.

HgCdTe DLTS enabling prior art independently shows that electron traps in a p-type absorber can be filled with negative pulses, with experimental electron cross sections around `5e-16` and `2.6e-15 cm^2` for two traps in a much wider-gap structure (Majkowycz et al., J. Electron. Mater. 52, 7074-7080, 2023, DOI 10.1007/s11664-023-10653-x). These are not assigned to the target narrow-gap vacancy transition.

## 3. Emission window

For order-of-magnitude timing only, use a parabolic-edge density of states with the standard narrow-gap detector-model scale

`m_e*/m0 ~= 0.071 Eg(eV)`.

At `Eg=40 meV`, `m_e*~0.00284m0`. Take a representative near-one-phonon electron separation `E_c-E_t=17.5 meV`.

Then

`e_n = C_n N_c exp[-(E_c-E_t)/(kT)]`.

Across the broad `C_n` bracket, representative emission rates are:

```text
T=20 K:  0.0025, 0.254, 2.54, 25.4 s^-1
T=25 K:  0.027,  2.71, 27.1, 271 s^-1
T=30 K:  0.138,  13.8, 138, 1379 s^-1
T=35 K:  0.457,  45.7, 457, 4572 s^-1
T=40 K:  1.15,   115,  1154, 1.15e4 s^-1
```

The columns correspond to `C_n=1e-12,1e-10,1e-9,1e-8 cm^3/s`.

Thus roughly 20-40 K spans conventional transient times over four decades of assumed `C_n`. At the slowest end, 20 K requires several-minute emission transients; at the fastest end, 40 K reaches tens of microseconds.

Direct filling is also tunable:

```text
n_fill=1e14 cm^-3:
C_n=1e-12 -> tau_c=10 ms
1e-10 -> 0.1 ms
1e-9  -> 10 us
1e-8  -> 1 us
```

The timing window is therefore not an obvious kill mechanism.

Companion: `numerics/electron_detuning_observability.py`.

## 4. Differential electronic-energy reconstruction

For isotope state `s`, write

`e_n,s = C_n,s N_c,s g_s exp[-E_e,s/(kT)]`,

where `E_e=E_c-E_t` and `g_s` collects the appropriate degeneracy/entropy factor.

Define an isotope log contrast using a reversible A-B-A sequence:

`D_I ln X = ln X_B - [ln X_A1 + ln X_A2]/2`.

Then

`Y(T) = D_I ln e_n - D_I ln C_n - D_I ln N_c`

obeys

`Y(T)=D_I ln g - D_I E_e/(kT)`.

If isotope substitution does not change the degeneracy factor, the physical null is a zero intercept:

`boxed: Y(T) = -D_I E_e/(kT)`.

This is preferable to comparing ordinary Arrhenius intercepts because the directly measured capture coefficient is divided out first.

A nonzero fitted intercept is itself a warning of entropy/degeneracy change or a systematic error.

## 5. Reconstruct the actual one-phonon detuning shift

For electron capture,

`Delta_e = hbar omega_op - E_e`.

Therefore

`boxed: D_I Delta_e = hbar D_I omega_op - D_I E_e`.

Raman measures the first term. Differential emission/capture DLTS measures the second. The experiment therefore does not have to assume that isotope mass perturbs only the phonon: an isotope-induced electronic trap/band-edge shift is measured and removed explicitly.

## 6. Energy precision

For independent per-state log uncertainties in emission, capture and DOS correction `s_e,s_c,s_N`, one A-B-A contrast has

`sigma(D_I E_e)=kT sqrt[1.5(s_e^2+s_c^2+s_N^2)]`.

Examples:

```text
per-state errors (e,C,Nc)=(0.5%,0.5%,0.2%):
20 K -> 0.0155 meV
30 K -> 0.0233 meV
40 K -> 0.0310 meV

(1%,1%,0.2%):
20 K -> 0.0301 meV
30 K -> 0.0452 meV
40 K -> 0.0603 meV
```

The ideal full Hg-only natural-Hg -> 204Hg shift of a 143-cm^-1 HgTe-like mode is about `-0.0577 meV`. Thus 20-30 K is the most favorable compromise between energy leverage and practical emission time.

Across five points from 20 to 40 K, enforcing the physically expected zero intercept gives approximately

```text
sigma(D_I E_e) ~= 0.0095 meV for 0.5%,0.5%,0.2% state errors
sigma(D_I E_e) ~= 0.0185 meV for 1%,1%,0.2% state errors.
```

If the intercept is allowed to float freely, the slope uncertainty is much larger; therefore the intercept must be reported as a model-consistency test, not silently absorbed.

## 7. Strong single-phonon closure

For the minimal pure one-optical-phonon phase-space model,

`C_n(T) = G sqrt(Delta_e) exp[-Delta_e/(kT)]`,

where `G` is a smooth matrix-element/prefactor term.

For two isotope states A and B,

`D_I ln C_n(T) = D_I ln G + 0.5 ln(Delta_B/Delta_A) - D_I Delta_e/(kT)`.

Therefore

`boxed: d[D_I ln C_n] / d[1/(kT)] = -D_I Delta_e`.

But `D_I Delta_e` is also measured independently from Raman plus differential emission DLTS.

Hence the single-phonon model is overdetermined:

```text
capture-contrast temperature slope
          must equal
Raman phonon shift - electronic trap-separation shift.
```

This is a stronger test than merely observing an isotope change in `C_n`.

## 8. Bypass interpretation

If an isotope-insensitive capture path runs in parallel,

`C_n = B + C_sens`,

the isotope response is diluted. For a small isotope perturbation and a limited temperature interval, the slope is approximately

`d[D_I ln C_n]/d[1/(kT)] ~= -f_sens D_I Delta_e`,

where `f_sens=C_sens/C_n` locally.

Thus the ratio

`f_iso ~= - slope_capture / (D_I Delta_e)`

provides a reduced-order estimate of the fraction of capture carried by the isotope-sensitive one-phonon channel. Exact interpretation requires the full spectral/bypass model because `f_sens` can itself vary with temperature.

The broadening/bypass model already showed that a large dark-current engineering effect requires nearly pure one-phonon capture. The isotope experiment can therefore remain useful even if it finds only a partial one-phonon fraction.

## 9. Smooth isotope prefactor

Do not assume all isotope dependence enters through `Delta_e`. Harmonic phonon normalization can also change the electron-phonon matrix-element prefactor smoothly with isotope mass. Such a contribution enters mainly the temperature-independent intercept `D_I ln G`, whereas the near-threshold detuning produces the characteristic `1/T` slope.

This is another reason to measure `D_I ln C_n(T)` over temperature rather than at one point.

## 10. Current go/no-go

Experiment 07 remains open because:

- electron capture is the physically relevant SRH bottleneck;
- electron filling is established in HgCdTe DLTS;
- a broad plausible `C_n` bracket gives practical filling/emission times;
- a few-percent Hg-isotope capture effect is compatible with the existing near-threshold stress model;
- the mechanism now has an overdetermined differential closure.

Next kill test: determine whether the same trap can be tracked reproducibly through isotope anneals and whether `D_I ln C_n(T)` can be measured with <=~0.5-1% state precision while keeping electrostatics fixed. If not, close the practical path.

Novelty remains unestablished. Do not draft a paper.
