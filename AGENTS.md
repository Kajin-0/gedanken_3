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
3. `experiments/10-room-temperature-lwir-admissibility/RESONANT_PATH_ENHANCEMENT_RESPONSE_BOUND_STEP_2026-08-14.md`
4. `experiments/10-room-temperature-lwir-admissibility/THEOREM_CORE_2026-08-14.md`
5. detailed files only as needed.

## Retained conditional electronic theorem

For a finite-gap massive-Dirac active pair, spectator-hole neutrality makes the matched active-pair single-pass sheet relation a lower bound:

```math
\boxed{\Sigma_c\ge C/v^2.}
```

Microscopic lattice resource:

```math
v\le V_{hop}.
```

For positive isotropic convex spectator-hole excitation `E_s(p)`, define

```math
v_s^{crit}=\inf_{p>0}E_s(p)/p.
```

Exact finite-energy normal-momentum spectator-assisted CCCH closure requires

```math
v\le v_s^{crit}.
```

For multiple spectators,

```math
v_{spec}=\min_s v_s^{crit},
\qquad
v_{adm}=\min(V_{hop},v_{spec}).
```

Under the **single-pass, active-pair-optically-dominant, exact-closure** hypotheses,

```math
\boxed{\Sigma_c\ge C/v_{adm}^2.}
```

For a parabolic heavy-hole spectator,

```math
M_{hh}v^2\le2(\Delta+\delta_{hh}),
```

and when this ceiling dominates,

```math
\Sigma_c\ge C M_{hh}/[2(\Delta+\delta_{hh})].
```

The `min E/p` kinematic structure is Landau-like and equal-group-velocity threshold theory is classical. Do not claim it as a new general principle.

## Retained resonant-response extension

For one-port TCMT, finite target absorptance and field-envelope response give

```math
\boxed{
\Sigma_c\ge
\frac{B}{v_{adm}^2}
\frac{1-\sqrt{1-A_0}}
{\Lambda_a\tau_{max}},
}
```

where

```math
\Lambda_a=2\gamma_i/(\alpha_Dd)
```

is an electromagnetic absorber sampling-rate / participation resource.

TCMT does not upper-bound `Lambda_a`. Therefore finite response alone does not restore a universal physical carrier-column floor.

## Why closed

The final novelty audit showed that the remaining photonic-resource space is already covered by mature theories under complementary hypotheses:

```text
Fano/Bode-Fano broadband matching;
Rozanov absorber thickness-bandwidth limits;
slow-light delay bounds;
nanophotonic light-trapping resonance/channel bounds;
susceptibility-based absorption-per-volume bounds;
resonant-cavity-enhanced photodetectors.
```

Electronic constituents are likewise established: `alpha/G_th`, heavy-hole CCCH, impact-ionization threshold conditions, Landau-like critical velocity, Dirac Auger suppression, multiband Auger engineering, detailed balance, and photon recycling.

The exact composed sheet-density inequality was not located verbatim, but the novelty case is not strong enough to justify manuscript development under the research protocol.

## Reopen Experiment 10 only for

```text
architecture-independent electronic-photonic invariant;
detector-specific no-go not reducible to known passivity bounds;
non-factorizable performance bound;
new inverse theorem from detector observables to electronic structure.
```

---

# ACTIVE NEXT ACTION

Screen **new** purely theoretical photodetector Gedanken premises.

Do not open Experiment 11 merely because Experiment 10 closed. First require a premise to survive a focused primary-literature screen.

Prefer premises that are not obvious restatements of:

```text
detailed balance / reciprocity;
FDT;
Landauer / reset thermodynamics;
standard information theory;
standard quantum measurement limits;
known critical-coupling / delay-bandwidth / Bode-Fano / Rozanov bounds;
known Auger suppression / band engineering;
ordinary shot-noise/Fano-factor arguments;
Experiment-08 zero-gap Kane statistics;
Experiment-09 collective/coherence line unless a genuinely new invariant appears.
```

If a candidate is established, document why and reject it before opening a new experiment.