# AGENTS.md — Research Objective, Recovery, and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active branch:** `experiment-12-oscillator-strength-state-count-bound`

Before material writes, fetch live targets and exact blob SHAs. Preserve failed, corrected, conditional, and negative paths. Do not use novelty or priority language without a dedicated prior-art audit.

## Primary objective

Generate analytical/theoretical photodetector research from simple Gedanken experiments. Target defensible theorems, bounds, invariants, counterexamples, scaling laws, or escape conditions—not a materials list or new scalar FOM.

## Hard scope

Analytical/theoretical only. Do not make fabrication, measurements, instrumentation, sample procurement, or laboratory optimization the next step.

---

# Experiment 12 — PRB REV9 / HOSTILE-REVIEW STAGE

Recovery order:

1. `experiments/12-oscillator-strength-state-count-bound/CURRENT_STATE.md`
2. `experiments/12-oscillator-strength-state-count-bound/REV8_EXTERNAL_REREVIEW_RESPONSE_2026-08-15.md`
3. `experiments/12-oscillator-strength-state-count-bound/MANUSCRIPT_REV9_CHANGESET_2026-08-15.md`
4. `experiments/12-oscillator-strength-state-count-bound/PRB_REV9_RENDER_QA_2026-08-15.md`
5. `experiments/12-oscillator-strength-state-count-bound/numerics/kane_8band_tightness.py`
6. `experiments/12-oscillator-strength-state-count-bound/HGCDTE_SECOND_ORDER_8BAND_TIGHTNESS_2026-08-15.md`
7. `experiments/12-oscillator-strength-state-count-bound/NOVELTY_AUDIT_2026-08-14.md`

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

The low-energy moving-window corollary requires uniform capacity over both system size and the sequence of windows.

The intrinsic one-species form is authorized only when the chemical potential lies in a gap so the cross-mu lower/upper partition coincides with valence/conduction manifolds.

## HgCdTe second-order validation

```text
T = 300 K
Eg = 0.123984198 eV
mu - E_Gamma6 = +11.477 meV
cross-mu reference population = 1.005141e17 cm^-3
conventional e+h total        = 1.010043e17 cm^-3
```

Window results:

```text
Eg..1.5Eg : vcap 1.016823e6 m/s, bound/reference 0.032046, ksel,max 0.149 nm^-1
Eg..2Eg   : vcap 1.017273e6 m/s, bound/reference 0.074922, ksel,max 0.240 nm^-1
Eg..3Eg   : vcap 1.015473e6 m/s, bound/reference 0.110977, ksel,max 0.415 nm^-1
Eg..0.5eV : vcap 1.015611e6 m/s, bound/reference 0.118010, ksel,max 0.583 nm^-1
```

The capacity is computed from complete projected velocity blocks and their largest singular values, not from `max |v_cv|`. In the broad window the pairwise maximum is `0.868123e6 m/s`; using it would overstate the lower bound by 36.9%.

Selected broad-window transitions involve Gamma8-derived -> Gamma6-derived branches. Gamma7-derived split-off branches do not enter the selected set.

## Rev9 production

```text
TeX SHA-256 da4d929d77d817e48c6661d61ffcdcaac82a8503b9594a8dafcca27e838c0f7b
PDF SHA-256 849e0653b6007c35a92967e812ab584ede70914714c2315bf849839701232e0b
9 pages / US letter / compile clean / all pages visually inspected.
```

## Scope / novelty

Valid class: independent-quasiparticle direct cross-mu charge absorbers.

Do not infer universal dark current, generation rate, D*, or finite-bandwidth noise. Do not extend automatically to excitons/collective states, indirect absorption, many-body spectral functions, or arbitrary passive photonic enhancement.

```text
DIRECT PRIOR-ART COLLISION: NOT FOUND
PRIORITY: NOT ESTABLISHED
NOVELTY: NOT ESTABLISHED
NOVELTY RISK: HIGH
```

No `first`, `novel`, or priority language is authorized.

## Active next action

Perform an extreme hostile review of **Rev9**. Do not inflate the theory. Further scientific changes require a concrete referee-level defect. Otherwise move toward author metadata, reproducibility archive, and PRB submission production.

---

Experiment 10 and Experiment 11 remain closed by default as novelty/manuscript paths.