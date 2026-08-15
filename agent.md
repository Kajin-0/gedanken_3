# Agent recovery entrypoint

Read `AGENTS.md` first, then this file. Do not infer chronology from `main` alone.

## Hard scope

All active research is analytical/theoretical only. Preserve failed/corrected/conditional paths. Do not use novelty or priority language without dedicated prior-art audit.

# ACTIVE — Experiment 12

Branch:

```text
experiment-12-oscillator-strength-state-count-bound
```

## Read in this order

1. `experiments/12-oscillator-strength-state-count-bound/CURRENT_STATE.md`
2. `experiments/12-oscillator-strength-state-count-bound/THERMAL_OPTICAL_SUM_INEQUALITY_STEP_2026-08-14.md`
3. `experiments/12-oscillator-strength-state-count-bound/DISPERSIVE_MULTIBAND_GENERALIZATION_STEP_2026-08-14.md`
4. `experiments/12-oscillator-strength-state-count-bound/OSCILLATOR_STRENGTH_STATE_COUNT_THEOREM_STEP_2026-08-14.md`
5. `experiments/12-oscillator-strength-state-count-bound/FOUNDING_GEDANKEN_2026-08-14.md`
6. `experiments/12-oscillator-strength-state-count-bound/PROGRESS_LOG.md`

## Controlling theorem

For independent single-particle eigenstates below and above `mu`, define

```math
n_e=V^{-1}\sum_cp_c,
\qquad
n_h=V^{-1}\sum_vh_v.
```

For direct interband optical conductivity and a finite crossing-transition velocity-strength resource `v_*`, exact Fermi algebra + Kubo give

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

Intrinsic neutral form:

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

Pointwise Fermi inequality underlying the result:

```math
\boxed{
\frac{2[f(E_v)-f(E_c)]}
{e^{(E_c-E_v)/(2k_BT)}-1}
\le
f(E_c)+[1-f(E_v)].
}
```

Velocity resource may be stated as

```math
\sum_v|v_{cv}|^2\le v_*^2
\quad\forall c,
```

and

```math
\sum_c|v_{cv}|^2\le v_*^2
\quad\forall v.
```

A finite relevant velocity-operator norm is sufficient.

## Validation

```text
2-D neutral massless Dirac / graphene: bound/exact = 1/2
3-D massless Dirac:                    bound/exact = 2/3
3-D finite-gap massive Dirac,
10 um / 300 K:                         bound/exact = 0.794684
```

The 3-D massive-Dirac bound approaches unity as `Delta/kBT` becomes large.

Reproduce with:

`experiments/12-oscillator-strength-state-count-bound/numerics/thermal_optical_sum_dirac_validation.py`

## Current theorem class

```text
independent-quasiparticle direct interband charge absorbers.
```

The theorem survives:

```text
arbitrary dispersive multiband state reuse;
unequal electron/hole degeneracies;
static single-particle disorder when exact eigenstates are used.
```

It does not automatically cover:

```text
bound excitons / neutral collective optical states;
phonon-assisted transitions;
interaction-generated lifetime broadening;
external absorptance enhanced by arbitrary passive photonics.
```

Do not infer dark current directly from the thermal population without an explicit electrical-activity/collection assumption. Localized-state detector architectures are the key counterexample to an unconditional current claim.

## Novelty status

Focused audits have not found the exact thermal kernel/carrier-population inequality in Kubo/f-sum, quantum-geometric, QFI, graphene, or IR-detector figure-of-merit literature.

```text
NOVELTY NOT ESTABLISHED.
NO MANUSCRIPT YET.
```

## ACTIVE NEXT ACTION

Hostile-test the detector significance:

```text
1. localized/electrical-activity loophole;
2. thermal occupation-fluctuation corollary and what it does/not imply for finite-bandwidth noise;
3. dedicated novelty audit around the exact kernel;
4. manuscript viability only after those survive.
```

---

# Experiment 10 — CLOSED BY DEFAULT

Branch:

`experiment-10-room-temperature-lwir-admissibility`

Retained conditional theorem and derivations remain useful but manuscript/novelty path closed.

# Experiment 11 — CLOSED BY DEFAULT

Branch:

`experiment-11-weighting-capacitance-duality`

Prompt-slew/capacitance identity retained as established Maxwell-relaxation / reciprocal-sensitivity consequence.

Post-Experiment-10/11 candidate-audit files document the large set of rejected premises. Consult them before reopening old directions.
