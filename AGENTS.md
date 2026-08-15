# AGENTS.md — Research Objective, Recovery, and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Most recently active branch:** `experiment-10-room-temperature-lwir-admissibility`

Before material writes, fetch live targets and exact blob SHAs. Preserve failed, corrected, conditional, and negative paths. Do not use novelty or priority language without a dedicated prior-art audit.

## Primary objective

Generate analytical/theoretical photodetector research from simple Gedanken experiments. The target is a defensible theorem, bound, invariant, counterexample, scaling law, or escape condition—not a materials list or a new scalar FOM.

## Hard global scope — ANALYTICAL / THEORETICAL ONLY

Allowed work: first-principles derivations, exact toy models, analytical bounds/no-go theorems, asymptotics, numerical thought experiments, analytical comparisons, and prior-art audits.

Do not make fabrication, measurement, instrumentation, sample procurement, or laboratory optimization the next step.

## Research protocol

```text
premise
-> minimal model
-> first nontrivial result
-> immediate primary-literature audit
-> kill if established
-> deepen only if something survives
-> theorem/bound/invariant/counterexample
-> quantitative witness
-> adversarial audit
-> manuscript only if novelty survives.
```

Do not keep adding phenomenology to rescue a weak novelty case.

---

# Experiment 10 — FINAL DISPOSITION

Branch:

```text
experiment-10-room-temperature-lwir-admissibility
```

```text
CLOSED BY DEFAULT AS A NOVELTY / MANUSCRIPT PATH.
```

Read for recovery:

1. `experiments/10-room-temperature-lwir-admissibility/CURRENT_STATE.md`
2. `experiments/10-room-temperature-lwir-admissibility/FINAL_PHOTONIC_AUDIT_AND_DISPOSITION_2026-08-14.md`
3. `experiments/10-room-temperature-lwir-admissibility/THEOREM_CORE_2026-08-14.md`

Retained conditional single-pass theorem:

```math
\Sigma_c\ge C/[\min(V_{hop},v_{spec})]^2
```

under active-pair optical dominance and exact normal-momentum spectator-assisted Auger closure. This is technically useful but not established as novel.

Experiment 10 was closed because arbitrary photonic engineering introduces independent established resources (matching, delay, thickness-bandwidth, light trapping, susceptibility/volume, cavity participation), and composing those known optical bounds with the electronic inequality did not provide a strong novelty case.

Do not draft an Experiment-10 manuscript or mechanically extend the branch.

---

# Post-Experiment-10 screening status

Read:

`candidate-audits/POST_EXP10_THEORETICAL_SCREEN_2026-08-14.md`

Five candidate premises have been screened and rejected **before** opening Experiment 11:

```text
1. causal / nonminimum-phase detectivity — standard minimum-phase and finite-window detection theory;
2. spatially correlated noise / D* area scaling — standard covariance/FPA noise theory;
3. non-normal detector transient amplification — generic non-normal photonic/system dynamics;
4. wide-gap LWIR detection via intersubband transition — established QWIP/QCD architecture;
5. equal D* but different non-Gaussian false-alarm tails — standard likelihood/point-process detection theory.
```

Experiment 11 remains unopened.

---

# ACTIVE NEXT ACTION

Continue screening **new** purely theoretical photodetector Gedanken premises.

Do not create Experiment 11 until a premise survives an aggressive primary-literature screen.

Reject immediately if the first nontrivial result is merely an application of:

```text
detailed balance / reciprocity / FDT;
Landauer/reset thermodynamics;
standard information or detection theory;
minimum-phase / matched-filter / generic LTI theory;
standard quantum measurement limits;
critical coupling / delay-bandwidth / Bode-Fano / Rozanov;
generic non-normal dynamics;
known Auger suppression / band engineering;
ordinary shot-noise / Fano-factor arguments;
QWIP/QCD intersubband detection;
Experiment-08 zero-gap Kane statistics;
Experiment-09 collective/coherence line unless a genuinely new invariant appears.
```

Prefer premises whose first consequence arises from specifically photodetector physics and cannot be factored into a generic systems theorem plus a detector example.
