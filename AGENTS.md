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

# Experiment 12 — SCIENTIFIC TEXT FROZEN AT REV6

Branch:

```text
experiment-12-oscillator-strength-state-count-bound
```

Recovery order:

1. `experiments/12-oscillator-strength-state-count-bound/CURRENT_STATE.md`
2. `experiments/12-oscillator-strength-state-count-bound/MANUSCRIPT_REV6_2026-08-14.md`
3. `experiments/12-oscillator-strength-state-count-bound/MANUSCRIPT_REV6_FINAL_QA_2026-08-14.md`
4. `experiments/12-oscillator-strength-state-count-bound/ACTIVE_SUBSPACE_REFINEMENT_2026-08-14.md`
5. `experiments/12-oscillator-strength-state-count-bound/MANUSCRIPT_REV4_EXTERNAL_STYLE_REVIEW_2026-08-14.md`
6. `experiments/12-oscillator-strength-state-count-bound/NOVELTY_AUDIT_ADDENDUM_TRK_CONDUCTIVITY_PARTICLE_COUNT_2026-08-14.md`
7. `experiments/12-oscillator-strength-state-count-bound/NOVELTY_AUDIT_2026-08-14.md`
8. `experiments/12-oscillator-strength-state-count-bound/PROGRESS_LOG.md`

Older Rev0–Rev5 manuscripts and corrections are development history. Rev6 is controlling.

## Controlling theorem

For exact independent-quasiparticle states with `E_v < mu < E_c`, the pointwise Fermi inequality is

```math
\boxed{
\frac{2[f(E_v)-f(E_c)]}
{e^{(E_c-E_v)/(2k_BT)}-1}
\le
f(E_c)+1-f(E_v).
}
```

For any measurable useful positive-frequency window `B`, use exact energy-shell projectors to define selected velocity blocks `A_{epsilon_c,B}` and `B_{epsilon_v,B}`.

The basis-invariant optical-velocity capacity is

```math
\boxed{
(v_B^{cap})^2
=\max\left[
\sup_{\epsilon_c>\mu}\|A_{\epsilon_c,B}\|_{op}^2,
\sup_{\epsilon_v<\mu}\|B_{\epsilon_v,B}\|_{op}^2
\right].
}
```

Define basis-invariant thermal optical-support populations

```math
n_{e,B}^{act}
=V^{-1}\sum_{\epsilon_c>\mu}f(\epsilon_c)
\operatorname{rank}A_{\epsilon_c,B},
```

```math
n_{h,B}^{act}
=V^{-1}\sum_{\epsilon_v<\mu}[1-f(\epsilon_v)]
\operatorname{rank}B_{\epsilon_v,B}.
```

Then

```math
\boxed{
n_e+n_h
\ge
n_{e,B}^{act}+n_{h,B}^{act}
\ge
\frac{2}{\pi e^2(v_B^{cap})^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}\,d\omega.
}
```

For intrinsic neutrality,

```math
\boxed{
n_{th}
\ge
\frac{1}{\pi e^2(v_B^{cap})^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}\,d\omega.
}
```

The low-energy kernel tends to `2 kBT`, so finite **integrated** low-energy direct spectral weight has a finite equilibrium thermal quasiparticle support-population cost at fixed `v_B^{cap}`.

`n_B^act` is a support-dimension count, not a continuously weighted optical participation ratio.

In 2-D, use sample area and sheet conductivity.

## Equality / validation

```text
equal-mass mirror-symmetric parabolic model:
    active theorem saturates for any selected direct window;
    total theorem saturates for full relevant direct spectrum.

2-D neutral massless Dirac: 0.5000
3-D massless Dirac:         0.6667
3-D massive Dirac,
10 um / 300 K:              0.794684
```

For unequal parabolic masses in the nondegenerate global limit,

```math
n_bound/n_exact
=[4m_em_h/(m_e+m_h)^2]^{3/4}.
```

## Scope boundary

Valid class:

```text
independent-quasiparticle direct cross-mu charge absorbers.
```

Do not automatically extend to:

```text
bound excitons / neutral collective optical states;
phonon-assisted / indirect absorption;
interaction-generated many-body spectral functions;
unconstrained passive photonic path enhancement.
```

Localized states do not invalidate the state-count theorem but block any automatic conversion to DC dark current.

Do not claim universal:

```text
dark-current lower bound;
thermal-generation-rate lower bound;
D* lower/upper limit;
finite-bandwidth-noise floor.
```

The attempted `G_th >= n_th/tau_response` theorem was rejected by a depleted-photodiode counterexample.

## Novelty status

Audited adjacency now includes:

```text
phase-space filling;
Kubo-Greenwood;
ordinary/generalized f-sums and TRK particle counts;
restricted optical sums;
quantum-geometric optical sums;
graphene optical sum rules;
classic IR alpha/G_th material criteria;
Yablonovitch-Kane low-carrier laser engineering;
Bethkenhagen et al. conductivity-to-ionization TRK counting.
```

No direct source was identified with the exact Experiment-12 thermal kernel plus per-shell optical-capacity/support-population inequality.

```text
DIRECT PRIOR-ART COLLISION: NOT FOUND
PRIORITY: NOT ESTABLISHED
NOVELTY: NOT ESTABLISHED
NOVELTY RISK: HIGH
```

No `first`, `novel`, or priority claim is authorized.

## Manuscript state

Current scientific submission candidate:

```text
experiments/12-oscillator-strength-state-count-bound/MANUSCRIPT_REV6_2026-08-14.md
```

Final internal hostile QA:

```text
FERMI ALGEBRA: PASS
KUBO NORMALIZATION: PASS
BASIS INVARIANCE: PASS
TRACE-RANK ACTIVE-SUBSPACE REFINEMENT: PASS
FINITE-WINDOW EQUALITY: PASS
2-D NORMALIZATION: PASS
PARABOLIC VALIDATION: PASS
DIRAC VALIDATION: PASS
LOW-ENERGY INTERPRETATION: PASS
CLAIM SCOPE: PASS
BIBLIOGRAPHY CORE: PASS
DIRECT PRIOR-ART COLLISION: NOT FOUND
NOVELTY: NOT ESTABLISHED
```

# ACTIVE NEXT ACTION — NO MORE THEORY BY DEFAULT

Do not extend Experiment 12 unless an external/referee-style review finds a blocking scientific gap.

Next phase:

```text
1. select journal;
2. perform journal-specific scope and bibliography/style audit;
3. typeset Rev6;
4. review rendered manuscript independently;
5. prepare submission materials if rendered QA passes.
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

The retained prompt-slew/capacitance identity reduces to established Maxwell-relaxation / reciprocal-sensitivity physics.

Candidate-audit files from the Experiment-10/11 lineage document rejected premises; consult them before reopening old ideas.
