# Agent recovery entrypoint

Read `AGENTS.md` first.

## Global user constraint — ANALYTICAL / THEORETICAL RESEARCH ONLY

The user cannot perform real-life experiments. All active research must be analytical/theoretical.

Allowed active work:
- first-principles derivations;
- exact toy models;
- mathematical bounds/invariants/no-go theorems;
- numerical thought experiments;
- analytical comparison with published theory;
- adversarial prior-art/novelty audits.

Do not make fabrication, sample procurement, measurement pilots, instrument choice, anneal schedules, device processing, or physical experiments the next research step. Older experimental-feasibility files are archived history only.

## Experiment 07 — CLOSED BY DEFAULT AS NOVELTY PATH

Branch: `experiment-07-isotope-srh`

Read in this order:

1. `experiments/07-isotope-srh/00_THEORETICAL_ONLY_SCOPE_2026-08-14.md`
2. `experiments/07-isotope-srh/00_NOVELTY_STOP_2026-08-14.md`
3. `experiments/07-isotope-srh/THEORETICAL_ISOTOPE_CONTROL_SUM_RULE_2026-08-14.md`
4. `experiments/07-isotope-srh/ONE_PHONON_MASS_SENSITIVITY_AND_LAPLACE_CLOSURE_2026-08-14.md`
5. `experiments/07-isotope-srh/ISOTOPE_MODE_RANK_CLOSURE_2026-08-14.md`
6. `experiments/07-isotope-srh/BANDGAP_ISOTOPE_DIFFERENTIAL_EQUIVALENCE_2026-08-14.md`
7. `experiments/07-isotope-srh/PHONON_EDGE_EXPONENT_AND_ISOTOPE_SIGN_2026-08-14.md`
8. `experiments/07-isotope-srh/DEFECT_POPULATION_ISOTOPE_SECTOR_2026-08-14.md`

### Controlling HgCdTe physics

The 2024 Kozlov et al. narrow-gap HgCdTe calculation fixes the electron one-phonon energy-selection law for capture to the approximately 20-meV `A2^-1` mercury-vacancy level:

```math
K=\hbar\omega_{LO}-(E_g-E_2).
```

Both HgTe-like and CdTe-like optical phonon branches contribute. Electron capture is much slower than hole capture in the studied regime and controls SRH relaxation.

### Exact theoretical results retained

1. Sequential/parallel SRH isotope sensitivity is a convex combination of microscopic channel isotope sensitivities.
2. Total SRH isotope response separates capture kinetics, electronic thermodynamics and defect-population sectors; a total isotope dark-current change does not uniquely identify capture physics.
3. Finite spectral broadening regularizes sharp threshold sensitivity: for onset exponent `beta`, threshold sensitivity scales as `const(beta)/sigma` rather than diverging.
4. Correct one-phonon mass sensitivity must include quantized matrix-element and Bose-factor terms; the earlier `sqrt(Delta)` sign-crossing toy result was incomplete.
5. For a positive capture spectral kernel, Bose-corrected `ln C` is convex in inverse temperature and its derivatives are capture-energy cumulants.
6. If isotope dependence enters only through `m` phonon coordinates, the elemental isotope-response vector lies in the corresponding mass-participation column space. In an ideal HgTe-like + CdTe-like two-mode model:

```math
S_{Te}=\frac{M_{Hg}}{M_{Te}}S_{Hg}+\frac{M_{Cd}}{M_{Te}}S_{Cd}.
```

7. Single-branch isotope shifts are detuning-equivalent to bandgap shifts, but in the real two-branch HgCdTe problem the total `C_n(E_g)` slope cannot determine individual elemental isotope coefficients. Composition tuning moves both branch detunings; Hg/Cd isotope tuning moves different directions in parameter space.
8. A dispersive phonon edge changes the one-phonon threshold exponent. For coupling-weighted phonon edge `J_ph(u)~u^eta`, the joint electron/phonon phase space scales as `Delta^(eta+3/2)`. Conditional on `beta>=1`, the reduced 77-K model has no isotope sign reversal inside the 0–5 meV kinetic window emphasized by the 2024 HgCdTe calculation.
9. Equilibrium vacancy populations possess a separate quantum vibrational isotope sector. Quenched and annealed defect ensembles therefore have different total SRH isotope coefficients.

### Novelty stop

Generic components are already covered by stronger established theory:
- isotope-sensitive nonradiative defect capture;
- first-principles multimode capture and phonon renormalization;
- partial isotope coefficients/sum rules;
- reaction-network control identities;
- finite-temperature defect vibrational free energies;
- Kozlov et al.'s HgCdTe mercury-vacancy capture model itself.

A full HgCdTe isotope calculation could still be performed as a straightforward extension, but that alone is not a sufficiently strong theoretical frontier.

```text
Experiment 07 heavy-isotope detector engineering: CLOSED
Experiment 07 isotope-SRH major novelty path: CLOSED BY DEFAULT
derived analytical identities: RETAIN
paper drafting: DO NOT BEGIN
```

Reopen only if a genuinely new theoretical ingredient appears that is not reducible to the established capture model plus chain-rule/control/Laplace/isotope-effect machinery.

## Older closed paths

- Experiment 06: SRH two-carrier provenance architecture closed by direct prior art.
- Experiment 05: active-volume/bandwidth theorem failed under arbitrary lossless matching.
- Experiment 04: passive nonreciprocal sensitivity path closed by trace bound.
- Experiment 03: passive photon-recycling cross-noise contains the same linear exchange information as deterministic response.
- Experiment 02: migrating-depth APD dominated by fixed-depth waveguide comparator.
- Experiment 01: equal-D* acquisition/information-spectrum paper path closed by established optimum-filter theory.

## Next research rule

Return to premise generation. For each new photodetector thought experiment:

1. keep the initial physical model minimal and transparent;
2. identify the strongest existing theorem/architecture before extending it;
3. search primary literature early;
4. stop if the result reduces to established detailed balance, fluctuation-dissipation, optimum filtering, Shockley-Ramo theory, standard avalanche theory, or another stronger comparator;
5. only open a new experiment branch if the premise survives that screen.

Preserve all negative results. Do not manufacture novelty.
