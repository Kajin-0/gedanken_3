# AGENTS.md — Research Objective, Recovery, and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active branch:** `experiment-12-oscillator-strength-state-count-bound`

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

# Recovery order — Experiment 12

Read in this order:

1. `experiments/12-oscillator-strength-state-count-bound/CURRENT_STATE.md`
2. `experiments/12-oscillator-strength-state-count-bound/THERMAL_OPTICAL_SUM_INEQUALITY_STEP_2026-08-14.md`
3. `experiments/12-oscillator-strength-state-count-bound/DISPERSIVE_MULTIBAND_GENERALIZATION_STEP_2026-08-14.md`
4. `experiments/12-oscillator-strength-state-count-bound/OSCILLATOR_STRENGTH_STATE_COUNT_THEOREM_STEP_2026-08-14.md`
5. `experiments/12-oscillator-strength-state-count-bound/FOUNDING_GEDANKEN_2026-08-14.md`
6. `experiments/12-oscillator-strength-state-count-bound/PROGRESS_LOG.md`
7. candidate-audit files only as needed.

---

# Experiment 12 — controlling result

For exact independent-particle eigenstates below and above a chemical potential, define thermal upper-state electron density `n_e`, lower-state hole density `n_h`, and direct interband optical conductivity `sigma_1^inter`.

Assume a finite crossing-transition velocity-strength resource `v_*`:

```math
\sum_v|v_{cv}|^2\le v_*^2
\quad\forall c,
```

```math
\sum_c|v_{cv}|^2\le v_*^2
\quad\forall v.
```

Exact Fermi algebra gives the global thermal-optical spectral-weight inequality

```math
\boxed{
n_e+n_h
\ge
\frac{2}{\pi e^2v_*^2}
\int_0^\infty
\frac{\hbar\omega\,\sigma_1^{inter}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
d\omega.
}
```

For an intrinsic neutral absorber,

```math
\boxed{
n_{th}
\ge
\frac{1}{\pi e^2v_*^2}
\int_0^\infty
\frac{\hbar\omega\,\sigma_1^{inter}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
d\omega.
}
```

This is currently the strongest surviving theorem in the branch.

The thermal kernel tends to `2 kBT` at low transition energy, so fixed low-energy intrinsic interband spectral weight cannot coexist with vanishing thermal quasiparticle population unless the velocity-strength resource also changes.

## Nontrivial validations

```text
2-D neutral massless Dirac / graphene: bound/exact = 1/2
3-D massless Dirac:                    bound/exact = 2/3
3-D massive Dirac at 10 um / 300 K:    bound/exact = 0.794684
```

The finite-gap Dirac validation is important: the generalized theorem recovers about 79.5% of the exact thermal population without assuming the Dirac DOS in the derivation.

Reproduce with:

`experiments/12-oscillator-strength-state-count-bound/numerics/thermal_optical_sum_dirac_validation.py`

## Corollaries

Partial spectral weight below `E_Omega`:

```math
\boxed{
n_e+n_h
\ge
\frac{2E_\Omega}{\pi e^2v_*^2}
\frac{W(E_\Omega)}
{e^{E_\Omega/(2k_BT)}-1}.
}
```

The original two-flat-manifold theorem is the tight equality structure of this more general result.

---

# Scope boundary

Current valid class:

```text
independent-quasiparticle direct interband charge absorbers.
```

The theorem survives arbitrary dispersive multiband state reuse and static single-particle disorder when exact eigenstates are used.

It does **not** automatically cover:

```text
bound excitons;
collective/superradiant many-body optical states;
phonon-assisted transitions;
interaction-generated lifetime broadening;
arbitrary passive photonic path enhancement when translating intrinsic conductivity to external absorptance.
```

Bound excitons are a genuine free-carrier counterexample: strong neutral low-energy oscillator strength can lie below the free pair continuum and photocurrent then requires a separate dissociation process.

Also do not infer dark current directly from thermal population without an explicit electrical-activity/collection assumption. Localized-state detectors show why that distinction matters.

---

# Novelty status

Focused audits have checked Kubo-Greenwood, ordinary/generalized `f`-sums, restricted optical sums, quantum-geometric conductivity bounds, finite-temperature QFI response integrals, graphene finite-T optical sum rules, and the classic IR `alpha/G_th` material criterion.

No direct collision with the exact Experiment-12 thermal kernel and carrier-population inequality has yet been found.

```text
NOVELTY NOT ESTABLISHED.
NO MANUSCRIPT YET.
```

---

# Closed previous branches

## Experiment 10

`experiment-10-room-temperature-lwir-admissibility`

```text
CLOSED BY DEFAULT AS NOVELTY / MANUSCRIPT PATH.
```

Retained conditional single-pass theorem:

```math
\Sigma_c\ge C/[\min(V_{hop},v_{spec})]^2.
```

## Experiment 11

`experiment-11-weighting-capacitance-duality`

```text
CLOSED BY DEFAULT AS NOVELTY / MANUSCRIPT PATH.
```

Retained prompt-slew identity/bound reduces to Maxwell relaxation / reciprocal sensitivity theory.

Candidate-audit files on the Experiment-11 lineage record rejected premises and should be consulted before reopening old ideas.

---

# ACTIVE NEXT ACTION

Attack Experiment 12 rather than drafting it.

Priority order:

```text
1. localized-state / electrical-activity loophole;
2. carrier-number fluctuation/noise corollary without arbitrary lifetime assumptions;
3. dedicated novelty audit centered on the exact thermal kernel;
4. only if those survive, theorem compression and manuscript viability review.
```
