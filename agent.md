# Agent recovery entrypoint

Read `AGENTS.md` first.

## Active Experiment 07 — isotope-tuned HgCdTe SRH

Branch: `experiment-07-isotope-srh`

Read in this order:

1. `experiments/07-isotope-srh/TWO_STEP_SRH_KILL_TEST_2026-08-13.md`
2. `experiments/07-isotope-srh/ISOTOPE_AXIS_FINGERPRINT_2026-08-13.md`
3. `experiments/07-isotope-srh/CURRENT_STATE.md`
4. `experiments/07-isotope-srh/numerics/two_step_srh_isotope.py`
5. `experiments/07-isotope-srh/numerics/isotope_threshold.py`

### Controlling result

A one-phonon mercury-vacancy capture channel can be strongly isotope-sensitive near a phonon threshold, but the practical natural->heavy isotope shift is small: about `0.094 meV` for the 10.56-meV HgTe-like acoustic cutoff and about `0.158 meV` for a 143-cm^-1 HgTe-like optical mode.

Once a fixed isotope-insensitive bypass and finite capture-energy broadening are included in the complete two-step SRH cycle, natural->heavy enrichment is not a robust >2x dark-current engineering lever. Using a published HgCdTe HgTe-like LO FWHM of `8.9 cm^-1` only as a broadening stress, the reduced-order model requires about `99.5%` of natural capture to come through the isotope-sensitive one-phonon path to reach 2x suppression even in the favorable both-captures-sensitive case.

Therefore:

```text
heavy-isotope dark-current engineering: STOP BY DEFAULT
single-phonon threshold physics: RETAIN
full light-vs-heavy isotope contrast as mechanism diagnostic: ACTIVE
novelty: NOT ESTABLISHED
paper drafting: DO NOT BEGIN
```

### Surviving diagnostic

Independent Hg, Cd and Te isotope substitutions can fingerprint phonon-mode character. In the ideal diatomic/one-mode limit:

```text
HgTe-like: (d ln tau/d ln M_Hg)/(d ln tau/d ln M_Te) ~= 0.636
CdTe-like: (d ln tau/d ln M_Cd)/(d ln tau/d ln M_Te) ~= 1.135
```

Measure actual isotope-dependent Raman/IR phonon shifts; the pure reduced-mass values are only first targets.

### Next hard step

Build an identifiability model for

`1/tau_total = 1/tau_SRH + 1/tau_rad + 1/tau_Auger + 1/tau_other`

including phonon shift, independently measured bandgap shift, and defect-density/sample variation. Determine the precision and sample matching required before the isotope-axis fingerprint can be distinguished from ordinary sample-to-sample changes.

## Closed paths

Experiment 06: SRH two-carrier provenance architecture closed by direct prior art.
Experiment 05: active-volume/bandwidth theorem failed under arbitrary lossless matching.
Experiment 04: passive nonreciprocal sensitivity path closed by trace bound.
Experiment 02: migrating-depth APD dominated by fixed-depth waveguide comparator.
Experiment 01: acquisition/information-spectrum paper path closed by prior art.

Preserve negative results. Do not rescue closed paths without a new physical constraint.