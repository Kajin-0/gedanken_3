# Agent recovery entrypoint

Read `AGENTS.md` first, then this file. The repository now contains **divergent post-Experiment-07 research branches**; do not infer project chronology from `main` alone.

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

## Repository-lineage reconciliation — READ BEFORE CONTINUING

`main` is not the live research frontier. It contains the merged Experiment-01/Paper-A lineage and three merged Paper-A PRs.

The handoff branch is:

```text
experiment-07-isotope-srh
head = 49f0832c11452f1e869790de0075513a8ed11347
```

A parallel branch exists:

```text
experiment-08-zero-gap-kane-statistics
head = d8f5138146561d9907a1d1d8d43d7df999bb6ed4
```

The two branches diverged at

```text
b88dce33bc02805a91931eb61db354ef7d89df6f
```

The Experiment-08 branch is seven commits ahead of that merge base but does **not** contain the final three Experiment-07 commits. Conversely, the Experiment-07 branch contains those three final isotope/theoretical-screen commits but not the Experiment-08 work.

Future premise generation must treat both branches as project knowledge. Do not silently discard either lineage and do not describe one as a strict continuation of the other.

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
9. `experiments/07-isotope-srh/THEORETICAL_ISOTOPE_SENSITIVITY_BOUNDS_2026-08-14.md`
10. `experiments/07-isotope-srh/THRESHOLD_PROXIMITY_ISOTOPE_NO_GO_2026-08-14.md`
11. `candidate-audits/POST_EXP07_THEORETICAL_SCREEN_2026-08-14.md`

### Controlling HgCdTe physics

The 2024 Kozlov et al. narrow-gap HgCdTe calculation fixes the electron one-phonon energy-selection law for capture to the approximately 20-meV `A2^-1` mercury-vacancy level:

```math
K=\hbar\omega_{LO}-(E_g-E_2).
```

Both HgTe-like and CdTe-like optical phonon branches contribute. Electron capture is much slower than hole capture in the studied regime and controls SRH relaxation.

### Exact theoretical results retained

1. Sequential/parallel SRH isotope sensitivity is a convex combination of microscopic channel isotope sensitivities. Positive serial/parallel kinetics cannot amplify the total elasticity beyond the microscopic channel extrema.
2. Total SRH isotope response separates capture kinetics, electronic thermodynamics and defect-population sectors; a total isotope dark-current change does not uniquely identify capture physics.
3. Finite spectral broadening regularizes sharp threshold sensitivity: for onset exponent `beta`, threshold sensitivity scales as `const(beta)/sigma` rather than diverging.
4. Correct one-phonon mass sensitivity must include quantized matrix-element and Bose-factor terms; the earlier `sqrt(Delta)` sign-crossing toy result was incomplete.
5. For a positive capture spectral kernel, Bose-corrected `ln C` is convex in inverse temperature and its derivatives are capture-energy cumulants.
6. If isotope dependence enters only through `m` phonon coordinates, the elemental isotope-response vector lies in the corresponding mass-participation column space. In an ideal HgTe-like + CdTe-like two-mode model:

```math
S_{Te}=\frac{M_{Hg}}{M_{Te}}S_{Hg}+\frac{M_{Cd}}{M_{Te}}S_{Cd}.
```

7. Single-branch isotope shifts are detuning-equivalent to bandgap shifts, but in the real two-branch HgCdTe problem the total `C_n(E_g)` slope cannot determine individual elemental isotope coefficients.
8. A dispersive phonon edge changes the one-phonon threshold exponent. For coupling-weighted phonon edge `J_ph(u)~u^eta`, the joint electron/phonon phase space scales as `Delta^(eta+3/2)`.
9. Equilibrium vacancy populations possess a separate quantum vibrational isotope sector. Quenched and annealed defect ensembles therefore have different total SRH isotope coefficients.
10. **Threshold proximity does not imply isotope leverage.** For

```math
E_{ph}=PM^{-1/2},
\qquad
\varepsilon=\varepsilon_\infty+ZM^{-1/2},
```

```math
\Delta=-\varepsilon_\infty+(P-Z)M^{-1/2}.
```

If `Z=P`, the detuning is isotope-independent even arbitrarily close to the one-phonon threshold. Mass scaling alone cannot guarantee a nonzero isotope effect or even its sign.

### Novelty stop

Generic components are already covered by stronger established theory: isotope-sensitive nonradiative defect capture, first-principles multimode capture and phonon renormalization, partial isotope coefficients/sum rules, reaction-network control identities, finite-temperature defect vibrational free energies, and the HgCdTe mercury-vacancy capture model itself.

```text
Experiment 07 heavy-isotope detector engineering: CLOSED
Experiment 07 isotope-SRH major novelty path: CLOSED BY DEFAULT
derived analytical identities: RETAIN
paper drafting: DO NOT BEGIN
```

## Parallel Experiment 08 — ZERO-GAP KANE STATISTICS — CLOSED

Branch: `experiment-08-zero-gap-kane-statistics`.

Read on that branch:

1. `experiments/08-zero-gap-kane-statistics/00_NOVELTY_STOP_2026-08-14.md`
2. `experiments/08-zero-gap-kane-statistics/FIRST_PRINCIPLES_ZERO_GAP_2026-08-14.md`
3. `experiments/08-zero-gap-kane-statistics/DOS_MISMATCH_ASYMPTOTIC_2026-08-14.md`
4. `experiments/08-zero-gap-kane-statistics/ZERO_GAP_PAIR_FLUCTUATION_ASYMPTOTIC_2026-08-14.md`
5. `candidate-screens/MASS_ASYMMETRY_JDOS_BOUND_2026-08-14.md`
6. `candidate-screens/HALL_PAIR_READOUT_NO_GAIN_2026-08-14.md`
7. `experiments/08-zero-gap-kane-statistics/numerics/zero_gap_kane_statistics.py`

Retain:

```math
\lim_{E_g\to0+}n_i^{Kane}=n_0(T)>0
```

at fixed `T>0`, unlike the naive parabolic `E_g^{3/4}` extrapolation. At zero gap the reduced Kane/heavy-hole model gives

```math
n_0(T)\sim T^3[\ln(T_0/T)]^3
```

up to Lambert-W / `ln ln` corrections. For the neutral-pair equilibrium variance, the retained asymptotic is

```math
\operatorname{Var}N_{pair}/V\sim T^3[\ln(T_0/T)]^2.
```

The zero-gap carrier-statistics problem is mature Kane/HgCdTe physics; major detector novelty was not established. The Hall-readout candidate also closed because photon-created and intrinsic GR neutral pairs occupy the same `(delta n,delta p) proportional to (1,1)` state direction, so a linear change of observation basis cannot create intrinsic lineage discrimination.

## QND information-without-absorption screen — CLOSED EARLY

Current branch: `agent/qnd-information-screen`.

Read:

`candidate-audits/QND_INFORMATION_WITHOUT_ABSORPTION_SCREEN_2026-08-14.md`

The exact minimal QND model is

```math
U
=|0\rangle\langle0|\otimes V_0
+|1\rangle\langle1|\otimes V_1,
\qquad
[U,H_S]=0.
```

It transfers photon-number information to conditional meter states without changing the photon-number eigenstate or its energy. If the meter-state overlap is

```math
c=\langle m_0'|m_1'\rangle,
```

then for equal priors the Helstrom error is

```math
P_e=\frac12\left(1-\sqrt{1-|c|^2}\right),
```

while optical number-basis coherence is multiplied by `c`. Perfect number discrimination (`c=0`) therefore preserves photon energy but fully dephases incompatible number coherence.

Direct QND photon-detection prior art is overwhelming: nondestructive single trapped photons, repeated cavity photon counting, circuit-QED QND counting, and nondestructive detection of itinerant microwave and optical photons already exist.

```text
photon information without absorption: YES / ESTABLISHED
absorbed signal energy as universal information cost: NO
zero quantum backaction: NO
QND novelty path: CLOSED
Experiment 09 on this premise: DO NOT OPEN
```

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
4. stop if the result reduces to established detailed balance, fluctuation-dissipation, optimum filtering, Shockley-Ramo theory, standard avalanche theory, QND measurement/complementarity, Landauer/reset cost, or another stronger comparator;
5. only open a new numbered experiment branch if the premise survives that screen.

Preserve all negative results. Do not manufacture novelty.