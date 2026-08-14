# Agent recovery entrypoint

Read `AGENTS.md` first.

## Global user constraint — THEORETICAL / ANALYTICAL RESEARCH ONLY

The user cannot perform real-life experiments. From 2026-08-14 onward, all active research must be analytical/theoretical.

Do not make laboratory execution, sample procurement, fabrication, measurement pilots, instrument selection, anneal schedules, or experimental sample counts the next research step.

Experimental arrangements may appear only as abstract thought experiments, prior-art comparators, or explanatory counterfactuals. They are not actionable research directions unless the user explicitly changes this constraint.

## Active Experiment 07 — isotope-tuned HgCdTe SRH theory

Branch: `experiment-07-isotope-srh`

Read first:

1. `experiments/07-isotope-srh/00_THEORETICAL_ONLY_SCOPE_2026-08-14.md`
2. `experiments/07-isotope-srh/00_ACTIVE_FRONTIER_INTERNAL_REFERENCE_2026-08-14.md`
3. `experiments/07-isotope-srh/NEGATIVE_U_INTERNAL_REFERENCE_SCREEN_2026-08-14.md`
4. `experiments/07-isotope-srh/ELECTRON_DETUNING_CLOSURE_2026-08-14.md`
5. `experiments/07-isotope-srh/ELECTRON_CAPTURE_BOTTLENECK_AND_REGISTRATION_2026-08-14.md`
6. `experiments/07-isotope-srh/TWO_STEP_SRH_KILL_TEST_2026-08-13.md`
7. `experiments/07-isotope-srh/ISOTOPE_AXIS_FINGERPRINT_2026-08-13.md`

The physical natural-Hg pilot, sister-coupon fabrication, isotope-exchange anneal, DLTS implementation, and enriched-Hg procurement work are archived feasibility analyses only. Do not optimize or advance them.

## Controlling physics retained from Experiment 07

The detector-relevant target is mercury-vacancy electron capture `C_n`; current narrow-gap theory places electron capture slower than hole capture and therefore rate-limiting for the SRH cycle.

For a one-optical-phonon electron transition, the relevant detuning is electron-side and isotope substitution changes both phonon and electronic terms. Schematically,

```math
\Delta_e=\hbar\omega_{op}-\Delta E_e,
```

so

```math
\delta\Delta_e=\hbar\,\delta\omega_{op}-\delta\Delta E_e.
```

A change in `C_n` cannot therefore be assigned to phonon mass scaling alone without accounting for isotope-induced electronic-level renormalization.

The negative-U transient algebra remains valid. For two sequential electron captures

```text
V0 --a=C1*n--> V- --b=C2*n--> V2-
```

```math
\bar N_e(t)=2-\frac{2b-a}{b-a}e^{-at}+\frac{a}{b-a}e^{-bt}.
```

The normalized unfilled signal is a two-exponential form. For `r=b/a<1/2` it is exactly identical to a positive mixture of two independent one-step capture populations; at `r=1/2` it becomes exactly single-exponential. This is a structural identifiability result, not an SNR issue.

Earlier filling-curve work also found an exact product degeneracy: a common carrier-density rescaling is indistinguishable from a capture-coefficient rescaling. Retain this only as an analytical inverse-problem result, not as motivation for new measurement hardware.

## New theoretical frontier

The former experimental gate is replaced by:

> For a negative-U Hg-vacancy SRH center with arbitrary parallel capture pathways and isotope-induced shifts of phonon energies, electronic defect energies, and possibly matrix elements, what can be inferred or bounded analytically about the total SRH rate from isotope mass alone?

Priority questions:

1. derive the full logarithmic isotope sensitivity of a sequential SRH cycle;
2. decompose it into phonon-frequency, electronic-level and matrix-element terms;
3. include arbitrary isotope-insensitive and isotope-sensitive bypass channels;
4. determine whether any isotope-axis ratio or temperature derivative remains invariant to those unknown channels;
5. prove upper/lower bounds or no-go conditions on the total isotope leverage;
6. compare the resulting theorem directly against established nonradiative-capture/isotope-effect theory before claiming novelty.

## Closed / archived paths

- Experiment 07 heavy-isotope dark-current engineering: STOP.
- Experiment 07 laboratory pilot / procurement / fabrication program: ARCHIVED, NOT ACTIVE.
- Experiment 06: SRH two-carrier provenance architecture closed by prior art.
- Experiment 05: active-volume/bandwidth theorem failed under arbitrary lossless matching.
- Experiment 04: passive nonreciprocal sensitivity path closed by trace bound.
- Experiment 02: migrating-depth APD dominated by fixed-depth waveguide comparator.
- Experiment 01: acquisition/information-spectrum paper path closed by prior art.

Preserve negative results. Do not draft a paper until a theoretical result survives a dedicated prior-art audit.
