# Electron-capture bottleneck and filling-curve registration

**Date:** 2026-08-14
**Status:** MAJOR CORRECTION / ELECTRON CAPTURE IS PRIMARY SRH TARGET / METROLOGY STILL PLAUSIBLE / NOVELTY NOT ESTABLISHED

## 1. Bottleneck correction

Recent mercury-vacancy theory states that, as in bulk narrow-gap HgCdTe, electron capture is substantially slower than hole capture and governs the SRH rate. Therefore the primary Experiment-07 observable must change from `C_p` to `C_n` if the goal is detector-relevant SRH physics.

Primary source: Kozlov et al., JETP 170, 131-138 (2026), article "Capture of Charge Carriers by Mercury Vacancy States in Narrow-Gap HgCdTe / HgCdTe Quantum Wells". The 2024 bulk narrow-gap calculation established that both electron and hole capture can proceed by single optical phonon emission near a ~40-meV gap (DOI 10.31857/S0044451024060117).

Hole capture remains a useful secondary comparison but cannot establish lifetime leverage if electron capture is the bottleneck.

## 2. Correct electron one-phonon detuning

For an electron captured from the conduction band into trap level `E_t`, define

`Delta_e = hbar*omega_op - (E_c-E_t)`.

The minimal 3-D one-optical-phonon phase-space proxy is

`C_n,sens proportional to sqrt(Delta_e) exp[-Delta_e/(kT)]`, for `Delta_e>0`.

Do not reuse the hole binding energy as the electron detuning.

Under isotope substitution,

`delta Delta_e = hbar delta omega_op - delta(E_c-E_t)`.

Therefore a measured isotope change in `C_n` is not by itself a phonon proof: the electronic trap separation can also shift. Raman and emission DLTS must measure the two terms independently.

## 3. Exact filling-curve time-rescaling test

For a nonuniform carrier profile `n(z)` and DLTS weighting `w(z)`, write the normalized filling curve

`F(t;C_n)=integral w(z)[1-exp(-C_n n(z)t)] dz / integral w(z) dz`.

If isotope substitution only multiplies the microscopic capture coefficient by `q` and the electrostatic filling profile is reproduced,

`boxed: F_B(t)=F_A(q t)`.

Thus the isotope ratio `q=C_n,B/C_n,A` can be obtained by horizontal registration of the entire normalized filling curve.

This removes the need for percent-level absolute carrier-density calibration. Trap density and the saturation transient amplitude cancel by normalization. Non-exponential filling due to a spatial carrier profile is allowed.

Failure of one horizontal scale factor to collapse A and B is itself a falsification: electrostatics changed, multiple traps/channels respond differently, or the one-coefficient model is incomplete.

Required controls:
- reversible A-B-A isotope sequence on one specimen;
- natural-Hg A-A-A anneal control;
- registration at several filling biases;
- Raman after every isotope state;
- emission DLTS and C-V/Hall to identify electronic/electrostatic shifts.

## 4. Statistical precision of curve registration

Using nine logarithmic filling times spanning `C n t = 0.1...10`, allowing each A/B/A state its own saturation amplitude and allowing linear drift in baseline log capture rate across the three states, a Fisher calculation gives

`boxed: sigma_ln(q) ~= 2.42 epsilon/sqrt(m)`

where `epsilon` is per-point normalized RMS noise relative to the full transient and `m` is repeats per filling time/state.

Approximate repeats for 5-sigma detection:

`epsilon=0.5%: 5% effect ~2; 2% ~10; 1% ~37`
`epsilon=1.0%: 5% effect ~6; 2% ~37; 1% ~147`
`epsilon=2.0%: 5% effect ~24; 2% ~147; 1% ~586`.

These are statistical floors only. State-to-state electrostatic changes are likely the stronger systematic.

## 5. Electron capture is experimentally addressable

HgCdTe DLTS already demonstrates electron filling in a p-type absorber using a negative fill pulse. A 2023 HgCdTe heterostructure study identified electron traps with apparent cross sections of about `5e-16` and `2.6e-15 cm^2`. These are enabling scales only, not asserted to be the target narrow-gap mercury-vacancy `C_n`.

The exact target `C_n` from the recent narrow-gap vacancy calculations has not yet been recovered numerically from an accessible primary full text. Do not infer it from the earlier hole-cross-section scale.

## 6. Hg-only isotope signal stress

For a 143-cm^-1 HgTe-like mode, natural Hg -> 204Hg changes the reduced-mass frequency by about `-0.325%`, or `-0.0577 meV` in phonon energy.

Reusing the existing reduced-order optical-threshold model only as a stress test, with the 8.9-cm^-1 Raman FWHM represented as a Gaussian energy spread and a fixed isotope-insensitive bypass, gives representative heavy/natural `C_n` ratios:

At `Delta_e=0.10 meV`: roughly `0.969, 0.947, 0.914, 0.893` for sensitive fractions `f_ref=0.5,0.7,0.9,0.99`.

At `Delta_e=0.50 meV`: roughly `0.968, 0.952, 0.933, 0.924`.

At `Delta_e=1.0 meV`: roughly `0.987, 0.982, 0.977, 0.975`.

At `Delta_e=2.0 meV`: roughly `0.996, 0.995, 0.994, 0.993`.

These are not predictions because the actual electron detuning, spectral density and bypass fraction are not established. They show only that a 1-5% Hg-only effect is compatible with the toy model for a sufficiently near-threshold electron transition and is not automatically below the statistical registration floor.

Companion: `numerics/electron_capture_registration.py`.

## 7. Stronger isotope consistency relation

At fixed temperature, direct filling gives `C_n`, while emission obeys schematically

`e_n = C_n N_c g exp[-(E_c-E_t)/(kT)]`.

Therefore isotope-differential measurements can infer the electronic trap-separation shift:

`delta(E_c-E_t) = -kT[delta ln e_n - delta ln C_n - delta ln N_c]`

(up to unchanged degeneracy/entropy assumptions).

Together with Raman,

`delta Delta_e = hbar delta omega_op - delta(E_c-E_t)`.

The strongest experiment therefore tests whether the measured `delta ln C_n(T)` follows the independently reconstructed `delta Delta_e(T)`, not merely whether `C_n` changes after isotope annealing.

## 8. Current go/no-go

Retain Experiment 07 only if:
1. the target electron trap can be filled reproducibly in the isotope-modified depletion region;
2. A/B curves collapse under a single horizontal scale factor at multiple fill biases;
3. the reversible `C_n` contrast exceeds the A-A-A control and electrostatic drift;
4. the contrast tracks the measured phonon/electronic detuning shift.

Do not start a manuscript. Novelty remains unestablished.
