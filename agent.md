# Agent recovery entrypoint

Read `AGENTS.md` first.

## Active Experiment 07 — isotope-tuned HgCdTe SRH capture

Branch: `experiment-07-isotope-srh`

### Read in this order

1. `experiments/07-isotope-srh/DLTS_OBSERVABILITY_AND_ISOTOPE_DECOMPOSITION_2026-08-14.md`
2. `experiments/07-isotope-srh/DLTS_PIVOT_2026-08-14.md`
3. `experiments/07-isotope-srh/REPEATED_CROSSOVER_AND_TEMPERATURE_SIGN_TEST_2026-08-14.md`
4. `experiments/07-isotope-srh/HG_ISOTOPE_CROSSOVER_2026-08-13.md`
5. `experiments/07-isotope-srh/TWO_STEP_SRH_KILL_TEST_2026-08-13.md`
6. `experiments/07-isotope-srh/ISOTOPE_AXIS_FINGERPRINT_2026-08-13.md`

Companion numerics:

- `experiments/07-isotope-srh/numerics/dlts_observability.py`
- `experiments/07-isotope-srh/numerics/isotope_identifiability_core.py`
- `experiments/07-isotope-srh/numerics/two_step_srh_isotope.py`
- `experiments/07-isotope-srh/numerics/isotope_threshold.py`

## Controlling scientific state

The broad engineering claim has failed:

```text
heavy-isotope enrichment as a robust HgCdTe dark-current reduction strategy: STOP
```

Natural->heavy phonon shifts are only ~0.1-0.2 meV and a >2x SRH change is washed out by modest bypass capture or spectral broadening unless the isotope-sensitive one-phonon path is almost perfectly dominant.

The surviving HgCdTe-specific hypothesis is narrower:

> Does the predicted single-optical-phonon mercury-vacancy capture channel show a reversible isotope dependence in its **direct carrier capture coefficient** that tracks the measured HgTe-like phonon shift?

General isotope-dependent nonradiative-defect dynamics are established prior art. Novelty is not established.

## Why total lifetime was rejected

Practical Hg isotope exchange favors a sub-micron modified layer. In such a thin HgCdTe film, surface/interface recombination can dominate total carrier lifetime. Therefore total-lifetime isotope spectroscopy is not the preferred experiment.

## Leading observable — direct DLTS capture kinetics

For a trap filling transient,

```math
A(t_p)=A_\infty[1-exp(-C_p p t_p)],
\qquad
\tau_c=(C_p p)^{-1}.
```

Measure `C_p(T,M)` or `C_n(T,M)` directly from filling-pulse dependence. Use emission DLTS separately:

```math
e_p=C_p N_v exp[-E_a/(kT)].
```

An isotope difference obeys

```math
Delta ln e_p = Delta ln C_p + Delta ln N_v - Delta E_a/(kT).
```

Therefore do **not** use an Arrhenius intercept alone as the isotope observable. Direct filling kinetics separates phonon-sensitive capture from isotope-induced electronic/trap-energy shifts.

Published HgCdTe trap cross-section scales imply capture times from tens of nanoseconds to hundreds of microseconds for controllable filling densities around `1e13-1e15 cm^-3`; the direct-capture route passes its first timing-feasibility gate.

The normalized filling-curve sensitivity is maximized at `C_p p t_p=1`:

```math
max d(A/A_inf)/d ln C_p = e^{-1}=0.368.
```

Thus a 2% capture-coefficient change gives ~0.74% of full transient amplitude near the optimal pulse duration. Multi-pulse fitting is required.

## Temperature-sign correction

For the minimal optical-phonon model

```math
C_p ~ sqrt(Delta) exp[-Delta/(kT)],
Delta=hbar omega-E_b,
```

```math
K_C=d ln C_p/d ln omega
=hbar omega[1/(2Delta)-1/(kT)].
```

The simple zero crossing is `kT_x=2Delta`, but thermal emission can make the trap unfillable at `T_x`.

For `hbar omega~17.73 meV`, the direct DLTS sign-crossing test is self-consistent mainly for a very near-threshold channel (`Delta` roughly <=1 meV at modest injection). For larger detuning, measure low-temperature `C_p(T)` rather than chasing the crossover to high temperature.

## Hg isotope exchange constraints

Hg lattice isotope exchange is much slower than Hg-vacancy diffusion, so vacancy populations can in principle re-equilibrate during a long Hg-rich anneal. However radiotracer work shows reduced surface tracer incorporation in epitaxial material, so actual isotope uptake must be measured by SIMS and Raman; do not assume the ideal constant-surface diffusion fraction.

A shallow depletion region (`~0.1-0.3 um`) can fit inside a `0.2-0.5 um` isotope-modified layer, making a thin DLTS test structure plausible.

## Preferred first experiment

1. Start from sister pieces of one narrow-gap HgCdTe wafer.
2. Precondition with matched Hg-rich thermal history.
3. Natural-Hg versus enriched-Hg anneal under matched chemical potential.
4. SIMS isotope profile on sacrificial sister material; Raman on the actual measured pieces.
5. Fabricate matched shallow MIS/diode structures after anneal.
6. Measure C-V/Hall carrier density, DLTS trap spectrum and trap concentration.
7. Measure direct filling kinetics over multiple pulse durations to extract `C_p(T)` and, if possible, `C_n(T)`.
8. Test whether isotope-dependent `C(T)` follows the measured phonon shift while `E_a` and trap density are separately controlled.

## Next hard step

Build an uncertainty floor for direct isotope-dependent `C_p` measurement: carrier-density uncertainty, pulse calibration, transient noise, trap nonuniformity and device-processing scatter. Compare that floor against the broadened/bypass one-phonon model's predicted natural-Hg -> 204Hg contrast.

If realistic `C_p` metrology cannot resolve the expected 1-5% range, close Experiment 07. If it can, proceed to a concrete shallow-junction structure and sample count.

## Closed paths

Experiment 06: SRH two-carrier provenance architecture closed by direct prior art.
Experiment 05: active-volume/bandwidth theorem failed under arbitrary lossless matching.
Experiment 04: passive nonreciprocal sensitivity path closed by trace bound.
Experiment 02: migrating-depth APD dominated by fixed-depth waveguide comparator.
Experiment 01: acquisition/information-spectrum paper path closed by prior art.

Preserve negative results. Do not rescue closed paths without a new physical constraint. Do not draft a paper yet.