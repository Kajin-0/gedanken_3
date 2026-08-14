# Experiment 07 active frontier: isotope identifiability

**Date:** 2026-08-13

The diagnostic should fit measured Raman shifts, not only reduced-mass ratios:

`dln(tau)=A_H dln(omega_H)+A_C dln(omega_C)+B_E dEg+B_N dln(Nv)+noise`.

Competing radiative/Auger rates only dilute the SRH isotope amplitude by `f_SRH=R_SRH/R_total`; that common factor cancels from ideal isotope-axis ratios.

For natural->heavy Hg-only, Cd-only and Te-only design estimates:

`HgTe=(-0.003255,0,-0.005658)`
`CdTe=(0,-0.008252,-0.004333)`.

The two-mode design condition number is ~1.76, so branch collinearity is not the main problem.

With one natural reference, equal replication `n`, and per-sample scatter `s` in ln(lifetime), wrong-branch rejection scales as:

`Z_HgTe ~= 0.838 |dln(tau)_Te| sqrt(n)/s`
`Z_CdTe ~= 1.578 |dln(tau)_Te| sqrt(n)/s`.

For a 5% Te-isotope lifetime effect, the harder HgTe-like 5-sigma case requires group-mean reproducibility ~0.84%. If per-sample scatter is 5%, this is ~36 samples/group; at 2% scatter it is ~6/group.

Raw dark current is a poor primary observable because isotope-dependent band-gap shifts can create percent-level changes. At 77 K, any factor proportional to `n_i^2` has characteristic sensitivity `|d ln J/dEg|~1/kT~0.151/meV`; ~0.056 meV uncorrected Eg shift can consume the full 0.84% budget.

Preferred observable: carrier lifetime in an intentionally SRH-dominated regime. But then `tau_SRH ~ 1/(Nv C)`, so vacancy-density variation enters one-for-one. Material reproducibility / defect characterization is now the leading feasibility risk, not lifetime instrument noise.

Next: determine whether paired growth or a same-material isotope perturbation can suppress composition/vacancy nuisance enough to avoid tens of independent samples. If not, close Experiment 07 as impractical even though the isotope fingerprint is mathematically identifiable.

Companion calculation: `numerics/isotope_identifiability_core.py`.
