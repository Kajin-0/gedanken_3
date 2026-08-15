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
-> manuscript only if novelty survives sufficiently to justify a draft
-> hostile manuscript review
-> typeset only after claim scope remains stable.
```

Do not add phenomenology merely to rescue a weak novelty case.

---

# Experiment 12 — ACTIVE MANUSCRIPT STAGE

Branch:

```text
experiment-12-oscillator-strength-state-count-bound
```

Recovery order:

1. `experiments/12-oscillator-strength-state-count-bound/CURRENT_STATE.md`
2. `experiments/12-oscillator-strength-state-count-bound/MANUSCRIPT_REV3_2026-08-14.md`
3. `experiments/12-oscillator-strength-state-count-bound/MANUSCRIPT_REV3_NOTATION_ERRATUM_2026-08-14.md`
4. `experiments/12-oscillator-strength-state-count-bound/THEOREM_CORE_2026-08-14.md`
5. `experiments/12-oscillator-strength-state-count-bound/BASIS_INVARIANT_VELOCITY_RESOURCE_CORRECTION_2026-08-14.md`
6. `experiments/12-oscillator-strength-state-count-bound/MANUSCRIPT_REV1_ADVERSARIAL_REVIEW_2026-08-14.md`
7. `experiments/12-oscillator-strength-state-count-bound/NOVELTY_AUDIT_2026-08-14.md`
8. `experiments/12-oscillator-strength-state-count-bound/NOVELTY_AUDIT_ADDENDUM_LOW_CARRIER_OPTICS_2026-08-14.md`
9. `experiments/12-oscillator-strength-state-count-bound/PROGRESS_LOG.md`

## Controlling theorem

For exact independent-quasiparticle states below and above a chemical potential, use only the direct cross-chemical-potential optical conductivity `sigma_1^cross`.

For every crossing transition,

```math
\boxed{
\frac{2[f(E_v)-f(E_c)]}
{e^{(E_c-E_v)/(2k_BT)}-1}
\le
f(E_c)+1-f(E_v).
}
```

For any measurable useful positive-frequency window `B`, define the basis-invariant optical-velocity shell resource `u_B` using projected physical velocity operators within exact degenerate energy eigenspaces.

Then

```math
\boxed{
n_e+n_h
\ge
\frac{2}{\pi e^2u_B^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
\,d\omega.
}
```

For an intrinsic neutral absorber,

```math
\boxed{
n_{th}
\ge
\frac{1}{\pi e^2u_B^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
\,d\omega.
}
```

The low-energy kernel tends to `2 kBT`, so a finite amount of **integrated** low-energy direct spectral weight has a finite thermal quasiparticle population cost at fixed optical-velocity resource.

## Tightness / validation

```text
3-D equal-mass parabolic direct bands:
    exact saturation at all temperatures in the ideal model

2-D neutral massless Dirac:
    bound/exact = 0.5000

3-D massless Dirac:
    bound/exact = 0.6667

3-D massive Dirac, 10 um / 300 K:
    bound/exact = 0.794684
```

For unequal parabolic masses in the nondegenerate limit,

```math
n_bound/n_exact
=
[4m_em_h/(m_e+m_h)^2]^{3/4}.
```

## Scope boundary

Valid class:

```text
independent-quasiparticle direct cross-mu charge absorbers.
```

Do not automatically extend to:

```text
bound excitons / neutral collective states;
phonon-assisted / indirect absorption;
interaction-generated many-body spectral functions;
unconstrained passive photonic path enhancement.
```

Localized states do not invalidate the population theorem but block any automatic conversion to DC dark current.

Do not claim a universal dark-current, thermal-generation-rate, D*, or finite-bandwidth-noise lower bound. The attempted `G_th >= n_th/tau_response` theorem was rejected by a depleted-photodiode counterexample.

## Manuscript state

Current manuscript:

`MANUSCRIPT_REV3_2026-08-14.md`

Rev3 is scientifically controlling but contains four stale **Greek-nu** renderings where the intended basis-invariant resource is Latin `u_B` / `u_{\mathcal B}`. Exact locations and correction are recorded in:

`MANUSCRIPT_REV3_NOTATION_ERRATUM_2026-08-14.md`

Treat Rev3 + erratum as the archival manuscript state. No scientific quantity changes.

```text
NOVELTY NOT ESTABLISHED.
REV3 IS READY FOR ANOTHER INDEPENDENT EXTERNAL-STYLE REVIEW.
```

## Next action

Do not add new physics by default.

Proceed with:

```text
1. fold the four-symbol erratum into the next rendered/journal-facing revision;
2. perform another independent hostile manuscript review;
3. verify every bibliography entry and journal-fit statement;
4. typeset only after claim scope remains unchanged.
```

---

# Closed previous branches

## Experiment 10

`experiment-10-room-temperature-lwir-admissibility`

```text
CLOSED BY DEFAULT AS NOVELTY / MANUSCRIPT PATH.
```

Retained conditional results remain useful but should not be mechanically extended.

## Experiment 11

`experiment-11-weighting-capacitance-duality`

```text
CLOSED BY DEFAULT AS NOVELTY / MANUSCRIPT PATH.
```

The prompt-slew/capacitance identity was retained as an established Maxwell-relaxation / reciprocal-sensitivity consequence.

Candidate-audit files from the Experiment-10/11 lineage document rejected premises; consult them before reopening old ideas.
