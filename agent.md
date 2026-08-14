# Agent recovery entrypoint

Read `AGENTS.md` first.

## Active Experiment 07 — isotope-tuned HgCdTe SRH capture

Branch: `experiment-07-isotope-srh`

### Read in this order

1. `experiments/07-isotope-srh/ELECTRON_CAPTURE_BOTTLENECK_AND_REGISTRATION_2026-08-14.md`
2. `experiments/07-isotope-srh/DLTS_OBSERVABILITY_AND_ISOTOPE_DECOMPOSITION_2026-08-14.md`
3. `experiments/07-isotope-srh/DLTS_PIVOT_2026-08-14.md`
4. `experiments/07-isotope-srh/REPEATED_CROSSOVER_AND_TEMPERATURE_SIGN_TEST_2026-08-14.md`
5. `experiments/07-isotope-srh/HG_ISOTOPE_CROSSOVER_2026-08-13.md`
6. `experiments/07-isotope-srh/TWO_STEP_SRH_KILL_TEST_2026-08-13.md`
7. `experiments/07-isotope-srh/ISOTOPE_AXIS_FINGERPRINT_2026-08-13.md`

Companion numerics include `numerics/electron_capture_registration.py`, `numerics/dlts_observability.py`, `numerics/two_step_srh_isotope.py`, and `numerics/isotope_identifiability_core.py`.

## Controlling correction

The primary detector-relevant capture observable is now **electron capture `C_n`**, not hole capture `C_p`. Recent mercury-vacancy theory states that electron capture is substantially slower than hole capture and governs the SRH rate in narrow-gap HgCdTe. Hole capture remains secondary.

For electron capture into trap level `E_t`, use

`Delta_e = hbar*omega_op - (E_c-E_t)`.

Do not reuse the hole binding energy as the electron detuning. Isotope substitution changes both the phonon and electronic terms:

`delta Delta_e = hbar delta omega_op - delta(E_c-E_t)`.

Therefore a reversible `C_n` change alone is not a phonon proof. Raman plus emission DLTS must reconstruct the actual detuning shift.

## Leading metrology result

For arbitrary reproducible spatial filling profile,

`F(t;C_n)=integral w(z)[1-exp(-C_n n(z)t)]dz / integral w(z)dz`.

If isotope substitution multiplies the microscopic capture coefficient by `q` while electrostatics are reproduced,

`F_B(t)=F_A(q t)`.

Thus extract `q=C_n,B/C_n,A` by horizontal registration of the complete normalized filling curves. Trap density and absolute carrier-density scale need not be known to percent precision. Failure of one horizontal scale factor to collapse A/B is itself a falsification.

A Fisher calculation for nine filling times from normalized `C n t=0.1...10`, separate saturation amplitudes in A/B/A, and linear cycle drift gives

`sigma_ln(q) ~= 2.42 epsilon/sqrt(m)`.

For per-point normalized RMS noise `epsilon=0.5%`, 5-sigma detection needs roughly 2 repeats for a 5% effect, 10 for 2%, and 37 for 1%. At `epsilon=1%`, the corresponding counts are about 6, 37, and 147. Statistical precision is therefore not obviously fatal; electrostatic state reproducibility is more important.

HgCdTe DLTS enabling prior art already demonstrates electron traps in a p-type absorber using negative fill pulses. Existing electron-trap cross sections are only enabling scales; do not claim they equal the narrow-gap mercury-vacancy `C_n`.

## Hg-only isotope stress

Natural Hg -> 204Hg shifts a 143-cm^-1 HgTe-like mode by about `-0.325%`, or `-0.0577 meV`.

Using the existing broadened/fixed-bypass optical-threshold surrogate only as a stress test, several-percent `C_n` changes remain possible for electron detuning `Delta_e` around `0.1-0.5 meV` when the one-phonon path is substantial. By `Delta_e~2 meV`, the Hg-only contrast is below about 1% in the tested parameter range.

This is not a prediction because the actual electron detuning and narrow-gap `C_n` have not yet been recovered quantitatively from the primary theory.

## Current experiment

Preferred first physical test remains a reversible/sister-piece Hg-isotope perturbation in a thin isotope-modified HgCdTe region, followed by shallow DLTS.

Measure:
- direct electron filling curves -> `C_n(T)` ratio by horizontal registration;
- Raman -> actual isotope phonon shift;
- emission DLTS -> electronic trap-separation shift;
- C-V/Hall -> electrostatic consistency;
- DLTS amplitude -> trap density;
- SIMS on sacrificial material -> isotope depth profile.

Require the A/B filling curves to collapse under one horizontal scale at several filling biases and require A-A-A natural-Hg controls to return `q~1`.

## Next hard step

Recover or bound the target narrow-gap mercury-vacancy `C_n` and its electron-side trap separation from the 2024-2026 theory. Determine whether the electron trap can be filled and emitted in a practical DLTS window. Then compare the measured/predicted `delta ln C_n` with the independently reconstructed

`delta Delta_e = hbar delta omega_op - delta(E_c-E_t)`.

If the target electron capture cannot be isolated or the Hg-only contrast is below the reversible registration/systematic floor, close Experiment 07.

## Closed paths

Experiments 01, 02, 04, 05 and 06 remain closed for the documented reasons. Preserve negative results. Do not draft a paper yet. Novelty is not established.
