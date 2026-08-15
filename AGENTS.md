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
-> realistic model stress test where significance depends on a resource parameter
-> typeset and render QA
-> repeat hostile review before submission.
```

Do not add phenomenology merely to rescue a weak novelty case.

---

# Experiment 12 — PRB REV8 / POST-REV7-RE-REVIEW STATE

Branch:

```text
experiment-12-oscillator-strength-state-count-bound
```

Recovery order:

1. `experiments/12-oscillator-strength-state-count-bound/CURRENT_STATE.md`
2. `experiments/12-oscillator-strength-state-count-bound/REV7_EXTERNAL_REREVIEW_RESPONSE_2026-08-15.md`
3. `experiments/12-oscillator-strength-state-count-bound/HGCDTE_SECOND_ORDER_8BAND_TIGHTNESS_2026-08-15.md`
4. `experiments/12-oscillator-strength-state-count-bound/MANUSCRIPT_REV8_CHANGESET_2026-08-15.md`
5. `experiments/12-oscillator-strength-state-count-bound/PRB_REV8_RENDER_QA_2026-08-15.md`
6. `experiments/12-oscillator-strength-state-count-bound/numerics/kane_8band_tightness.py`
7. `experiments/12-oscillator-strength-state-count-bound/NOVELTY_AUDIT_2026-08-14.md`

Older revisions and review responses preserve the development/correction history. Rev8 is the current QA-passed manuscript state; exact source/PDF hashes are recorded in the changeset and render-QA files.

## Controlling theorem — unchanged

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

Do not modify the central theorem without a new mathematical counterexample.

## Thermodynamic and low-energy quantifiers — Rev8

For fixed `B`, macroscopic density statements require

```math
\limsup_{V\to\infty}v_{B,V}^{cap}<\infty.
```

For moving low-energy windows `B_m`, Rev8 requires the stronger joint condition

```math
\boxed{
\sup_m\left[\limsup_{V\to\infty}v_{B_m,V}^{cap}\right]<\infty.
}
```

With shrinking transition energies and nonzero limiting integrated spectral weight, this gives a strictly positive liminf active-population floor.

## First-order HgCdTe Kane resource

For the standard first-order 8x8 Kane Hamiltonian,

```math
\|\hat v_x\|_{op}=\sqrt{3/2}\,v_K,
```

so

```math
v_B^{cap}\le\sqrt{3/2}\,v_K=P/\hbar.
```

This is a global first-order **upper bound**, not the actual selected-window capacity.

HgCdTe scale:

```text
v_K=(1.07 +/- 0.05)e6 m/s -> upper bound ~=1.31e6 m/s.
```

For higher-order k.p Hamiltonians, make capacity statements only on finite spectral windows inside bounded momentum domains where the model is used.

## Full second-order realistic multiband test — Rev8

Using the bulk constant-parameter second-order 8-band Hamiltonian of Novik et al. with a representative 300-K, 10-um HgCdTe-like parameter interpolation:

```text
cross-mu exact theorem population = 1.005141e17 cm^-3
```

and

```text
window          v_B^cap (m/s)    bound/exact
Eg..1.5Eg       1.016823e6        0.032046
Eg..2Eg         1.017273e6        0.074922
Eg..3Eg         1.015473e6        0.110977
Eg..0.5eV       1.015611e6        0.118010
```

Headline broad-window result:

```math
\boxed{
(n_e+n_h)_{bound}/(n_e+n_h)_{exact}\simeq0.118.
}
```

This shows the bound remains quantitatively nontrivial in a heavy-hole/multiband narrow-gap model, although substantially looser than the ideal Dirac/parabolic examples.

The 0.5-eV upper limit is a model-validation window, not a detector bandwidth.

Reproducibility and convergence:

`HGCDTE_SECOND_ORDER_8BAND_TIGHTNESS_2026-08-15.md`

`numerics/kane_8band_tightness.py`

## Appendix-A correction

The illustrative internal-absorptance window is now

```text
[1.02 omega_g, 1.10 omega_g]
```

and the first-order Kane upper bound gives only a **conservative** lower column

```text
Sigma_e >= 4.19e11 cm^-2.
```

## Rev8 production state

```text
experiment12_prb_rev8.tex
SHA-256 18424af7052262b2974a94a5ed6f85495951674fdcc0333624f3426f635df3a9

experiment12_prb_rev8.pdf
SHA-256 36e3fa7c01053bd5ec20f235cbb3f4f99c5297c3d44f11845440f77dff1da402

8 pages / US letter / warning-free compile / PDF preflight pass / all 8 pages visually inspected.
```

## Scope boundary

Valid class:

```text
independent-quasiparticle direct cross-mu charge absorbers.
```

Do not automatically extend to bound excitons/collective states, indirect phonon-assisted absorption, interacting many-body spectral functions, or arbitrary passive photonic path enhancement.

Do not infer universal dark current, thermal generation rate, `D*`, or finite-bandwidth noise.

Applying the theorem to measured optical conductivity requires isolating `sigma_1^cross` or a window in which it dominates.

## Novelty status

```text
DIRECT PRIOR-ART COLLISION: NOT FOUND
PRIORITY: NOT ESTABLISHED
NOVELTY: NOT ESTABLISHED
NOVELTY RISK: HIGH
```

No `first`, `novel`, or priority wording is authorized.

## ACTIVE NEXT ACTION

Perform a new **extreme adversarial review of Rev8**.

Priority attacks:

```text
1. verify the second-order 8-band Hamiltonian implementation and theorem normalization independently;
2. test whether the 0.118 ratio is robust to reasonable parameter/interpolation choices and bounded-k-domain choices;
3. ask whether a semiconductor-optics prior result already implies this bound more directly;
4. attack the meaning of cross-mu population when the charge-neutral mu lies weakly inside the nominal conduction sector;
5. verify that the new realistic-material section materially strengthens significance rather than overfitting one model.
```

Do not add further theory unless that review identifies a genuine blocker.

---

# Closed previous branches

Experiment 10 and Experiment 11 remain closed by default as novelty/manuscript paths. Consult their retained results and candidate-audit files before reopening old directions.