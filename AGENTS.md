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
-> manuscript
-> hostile manuscript review
-> revise only against concrete scientific defects
-> typeset and render QA
-> repeat hostile review before submission.
```

Do not add phenomenology merely to rescue a weak novelty case.

---

# Experiment 12 — PRB REV7 / POST-MAJOR-REVIEW STATE

Branch:

```text
experiment-12-oscillator-strength-state-count-bound
```

Recovery order:

1. `experiments/12-oscillator-strength-state-count-bound/CURRENT_STATE.md`
2. `experiments/12-oscillator-strength-state-count-bound/REV6_EXTERNAL_REVIEW_RESPONSE_2026-08-15.md`
3. `experiments/12-oscillator-strength-state-count-bound/MANUSCRIPT_REV7_CHANGESET_2026-08-15.md`
4. `experiments/12-oscillator-strength-state-count-bound/PRB_REV7_RENDER_QA_2026-08-15.md`
5. `experiments/12-oscillator-strength-state-count-bound/numerics/kane_8band_capacity.py`
6. `experiments/12-oscillator-strength-state-count-bound/MANUSCRIPT_REV6_2026-08-14.md`
7. `experiments/12-oscillator-strength-state-count-bound/NOVELTY_AUDIT_2026-08-14.md`
8. `experiments/12-oscillator-strength-state-count-bound/PROGRESS_LOG.md`

Older revisions preserve development history. The QA-passed Rev7 PRB source/PDF are the active manuscript state; exact source/PDF hashes and the full deterministic changeset are recorded in items 3–4.

## Controlling theorem

For direct transitions crossing `mu` in selected positive-frequency window `B`, exact Fermi statistics plus Kubo-Greenwood and the per-shell singular-value/rank resource give

```math
\boxed{
n_e+n_h
\ge
n_{e,B}^{act}+n_{h,B}^{act}
\ge
\frac{2}{\pi e^2(v_B^{cap})^2}
\int_B
\frac{\hbar\omega\sigma_1^{cross}(\omega)}
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
\frac{\hbar\omega\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}\,d\omega.
}
```

## Thermodynamic-limit condition — now explicit

The finite-system theorem is exact as stated. A nonzero thermodynamic density floor requires

```math
\boxed{
\bar v_B^{cap}
=\limsup_{V\to\infty}v_{B,V}^{cap}<\infty.
}
```

Do not state a macroscopic low-energy population floor without this uniform-capacity hypothesis.

## Realistic multiband resource validation — added in Rev7

For the standard first-order HgCdTe 8x8 Kane Hamiltonian,

```math
\boxed{
\|\hat v_x\|_{op}=\sqrt{3/2}\,v_K
}
```

so, for every selected window,

```math
\boxed{
v_B^{cap}\le\sqrt{3/2}\,v_K.}
```

This is independent of system size in that Hamiltonian and directly satisfies the thermodynamic uniform-boundedness condition.

Equivalent form:

```math
v_B^{cap}\le P/\hbar=\sqrt{E_P/(2m_0)}.
```

HgCdTe scale:

```text
v_K=(1.07 +/- 0.05)e6 m/s -> central capacity <= 1.31e6 m/s
E_P ~=18.8 eV -> capacity <=1.286e6 m/s
```

The exact `sqrt(3/2)` coefficient is restricted to the first-order 8x8 Kane model. Second-order k.p corrections are a stated model boundary.

## Rev7 corrections beyond the Kane model

```text
van Roosbroeck-Shockley detailed-balance context added;
Callen-Welton fluctuation-dissipation context added;
E=mu transition-endpoint limiting prescription added;
rank-discontinuity / support-population interpretation clarified;
measured sigma_1 versus isolated sigma_1^cross limitation added;
full-spectrum parabolic saturation explicitly labeled an ideal effective-model result;
low-energy statement made conditional on integrated weight + uniform capacity;
10-um example clarified as internal admitted-power absorptance / ideal AR or index matching.
```

## Independent validations retained

```text
2-D neutral massless Dirac: 0.5000
3-D massless Dirac:         0.6667
3-D massive Dirac, 10 um / 300 K: 0.794684
```

Unequal parabolic nondegenerate global ratio:

```math
[4m_em_h/(m_e+m_h)^2]^{3/4}.
```

## Scope boundary

Valid class:

```text
independent-quasiparticle direct cross-mu charge absorbers.
```

Do not automatically extend to bound excitons/collective states, indirect phonon-assisted absorption, interacting many-body spectral functions, or arbitrary passive photonic path enhancement.

Do not infer universal dark current, thermal generation rate, `D*`, or finite-bandwidth noise.

Applying the theorem to measured optical conductivity requires isolating `sigma_1^cross` or a window in which it dominates.

`n_B^act` is an exact support-dimension construct and should not be described as a noise-robust experimental participation count.

## Novelty status

```text
DIRECT PRIOR-ART COLLISION: NOT FOUND
PRIORITY: NOT ESTABLISHED
NOVELTY: NOT ESTABLISHED
NOVELTY RISK: HIGH
```

No `first`, `novel`, or priority wording is authorized.

## Rev7 production state

```text
experiment12_prb_rev7.tex
SHA-256 ec5f46f0256b320861fabdd3ad5e61832c1f20c03ea95216979207fe92dc488d

experiment12_prb_rev7.pdf
SHA-256 e481354dc25a0526dbe0b4eb636a0ca733aae8678f3a12b7a2d0a349d25c0740

7 pages / US letter / compile clean / all pages visually inspected / no clipping or float regression.
```

## ACTIVE NEXT ACTION

Perform a new extreme hostile review of **Rev7 itself**.

Priority attacks:

```text
1. Is the Kane capacity derivation/interpretation correct and sufficiently realistic?
2. Does the new uniform thermodynamic hypothesis fully close the finite-size loophole?
3. Does VRS/FDT or another equilibrium theorem imply the result more directly than claimed?
4. Does second-order/multiband k.p expose a capacity-growth loophole in a finite useful window?
5. Does a stronger prior-art collision emerge now that the theorem is framed as response + capacity -> state count?
```

Do not add new theory unless that review finds a real blocker.

---

# Closed previous branches

Experiment 10 and Experiment 11 remain closed by default as novelty/manuscript paths. Consult their retained results and candidate-audit files before reopening old directions.