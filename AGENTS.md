# AGENTS.md — Research Objective, Recovery, and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active branch:** `experiment-12-oscillator-strength-state-count-bound`

Before material writes, fetch live targets and exact blob SHAs. Preserve failed, corrected, conditional, and negative paths. Do not use novelty or priority language without a dedicated prior-art audit.

## Primary objective

Generate analytical/theoretical photodetector research from simple Gedanken experiments. Target defensible theorems, bounds, invariants, counterexamples, scaling laws, or escape conditions—not a materials list or a new scalar figure of merit.

## Hard scope

Analytical/theoretical only. Do not make fabrication, measurements, instrumentation, sample procurement, or laboratory optimization the next step.

---

# ACTIVE — Experiment 12 / Rev11 PRB submission candidate

Rev11 remains the controlling scientifically QA-passed manuscript. The final adversarial regression audit found **no central theorem defect and no HgCdTe numerical inconsistency**, but identified one concrete literature-completeness amendment before submission: cite and distinguish Mao, Mendez-Valderrama, and Chowdhury, Phys. Rev. B 112, 075116 (2025), on projected low-energy optical sum rules.

The literature amendment currently exists only as a candidate patch. Do **not** call it Rev12 or submission-ready until the exact Rev11 source is reconstructed, the patch is applied, and compile/hash/all-page QA is rerun.

## Recovery order

1. `experiments/12-oscillator-strength-state-count-bound/CURRENT_STATE.md`
2. `experiments/12-oscillator-strength-state-count-bound/REV11_FINAL_ADVERSARIAL_REGRESSION_AUDIT_2026-08-15.md`
3. `experiments/12-oscillator-strength-state-count-bound/typeset/rev11_literature_completeness_candidate.patch`
4. `experiments/12-oscillator-strength-state-count-bound/PRB_REV11_MINOR_REVISION_QA_2026-08-15.md`
5. `experiments/12-oscillator-strength-state-count-bound/REV10_MINOR_REREVIEW_RESPONSE_2026-08-15.md`
6. `experiments/12-oscillator-strength-state-count-bound/typeset/rev10_to_rev11_minor_revision.patch`
7. `experiments/12-oscillator-strength-state-count-bound/numerics/parameter_sensitivity_audit.py`
8. `experiments/12-oscillator-strength-state-count-bound/PRB_REV10_REFEREE_REPAIR_QA_2026-08-15.md`
9. `experiments/12-oscillator-strength-state-count-bound/REV9_SUPREMUM_REREVIEW_RESOLUTION_2026-08-15.md`
10. `experiments/12-oscillator-strength-state-count-bound/numerics/supremum_active_support_audit.py`
11. `experiments/12-oscillator-strength-state-count-bound/typeset/rev9_exposition_to_rev10_referee_repaired.patch`
12. `experiments/12-oscillator-strength-state-count-bound/MANUSCRIPT_REV9_EXPOSITION_REVISED_2026-08-15.md`

## Controlling theorem

For selected direct cross-mu optical window `B`,

```math
\boxed{
n_e+n_h
\ge n_{e,B}^{act}+n_{h,B}^{act}
\ge
\frac{2}{\pi e^2(v_B^{cap})^2}
\int_B
\frac{\hbar\omega\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}\,d\omega.
}
```

Eq. (29) and its proof remain unchanged through Rev11 and survive the final regression audit.

The low-energy moving-window corollary requires uniform capacity over both system size and the sequence of windows. The intrinsic one-species form is authorized only when the chemical potential lies in a gap so the cross-mu lower/upper partition coincides with valence/conduction manifolds.

## Rev10/Rev11 repairs that must not be lost

- Eqs. (21)–(22) use an ordinary finite-system shell supremum. Eq. (49) must remain an ordinary supremum, not an essential supremum.
- In the representative HgCdTe state, `mu` lies 11.477 meV above the nominal Gamma6 edge; Gamma6 and Gamma8 are all below `mu` at `k=0`, so the isolated-Gamma correction is inapplicable.
- In a finite periodic clean system, `v_x` conserves crystal momentum and the complete exact-energy-shell block decomposes as

```math
P_\epsilon v_xQ_{\epsilon,B}
=\bigoplus_{\mathbf k}
P_{\epsilon,\mathbf k}v_x(\mathbf k)Q_{\epsilon,\mathbf k,B}.
```

The full-shell norm is therefore the maximum finite-k block norm and becomes the ordinary k supremum in the bulk limit.

## Controlling HgCdTe result

```text
n_ref                      = 1.005141e17 cm^-3
v_B^cap ordinary sup       ~= 1.01764e6 m/s
precise bound/reference    ~= 0.1175
headline rounded value     = 0.118 / 11.8%
lower bound                ~= 1.18e16 cm^-3
n_B^act/n_ref              ~= 0.669
n_bound/n_B^act            ~= 0.176
pairwise ordinary sup      ~= 0.87165e6 m/s
pairwise substitution bias ~= +36.3%
selected k onset           ~= 0.05535 nm^-1
selected k max             ~= 0.583 nm^-1
```

Production quadrature: `160 x 10 x 16`; `200 x 12 x 20` is an additional support check.

The active-support diagnostic uses a numerical singular-value threshold of `1e-6 m/s` for Table II only. The central bound is threshold independent. A reduced-grid sweep from `1e-9` to `1e4 m/s` leaves the active-support fraction unchanged to printed precision.

A reduced one-at-a-time `+/-5%` sensitivity scan of `EP, Delta, F, gamma1, gamma2, gamma3` gives a broad diagnostic ratio range `0.1098 ... 0.1293`; this is not an experimental uncertainty interval.

## Literature positioning

Rev11 already cites Onishi and Fu, Phys. Rev. X 14, 011052 (2024), and distinguishes their topology/quantum-geometry gap bound from Eq. (29).

The final regression audit additionally identified:

```text
D. Mao, J. F. Mendez-Valderrama, D. Chowdhury,
Phys. Rev. B 112, 075116 (2025).
```

Their work treats projected low-energy optical sum rules and finite-temperature weighted forms tied to many-body geometry/QFI. It is neighboring literature, not a direct collision with the cross-mu Fermi-kernel + per-shell-capacity quasiparticle-population inequality. It should nevertheless be cited before submission.

## Rev11 production identity

Exact Rev11 source is reconstructed by applying, in order:

1. `typeset/rev9_exposition_to_rev10_referee_repaired.patch`
2. `typeset/rev10_to_rev11_minor_revision.patch`

to the archived Rev9 exposition source.

```text
Rev11 TeX SHA-256 a75b75d6016d335746751b7c75a01d49deea7c4796c2eff30a7dd99c1f73cd68
Rev11 PDF SHA-256 ed5a558ac561cb67f0e918de96f4774c493cacd54fd6f3bea01e597890a7df5d
13 pages / US letter / REVTeX PRB / compile clean / all-page visual QA pass
19 references
```

## Scope / novelty

No universal dark-current, `D*`, generation-rate, or finite-bandwidth-noise theorem. Excitons, indirect transitions, interacting many-body spectral functions, and unconstrained photonic enhancement remain outside scope.

```text
DIRECT PRIOR-ART COLLISION: NOT FOUND IN TARGETED SEARCH
NOVELTY: PLAUSIBLE
HISTORICAL PRIORITY: NOT ESTABLISHED
```

No `first`, `novel`, or priority language is authorized.

## Active next action

Reconstruct exact Rev11 TeX, apply `typeset/rev11_literature_completeness_candidate.patch`, update the bibliography count to 20, compile, verify citations/boxes/floats, compute new TeX/PDF hashes, and visually inspect every page. If that passes, record the amended production package and stop rewriting absent a new concrete defect or journal requirement.

Experiment 10 and Experiment 11 remain closed by default as novelty/manuscript paths.
