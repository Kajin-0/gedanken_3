# Agent recovery entrypoint

Read `AGENTS.md` first, then this file. Do not infer chronology from `main` alone.

## Hard scope

All research in this repo is analytical/theoretical only. Preserve failed, corrected, conditional, and negative paths. Do not use novelty or priority language without a dedicated audit.

# ACTIVE — Experiment 12 / PRB Rev7

Branch:

```text
experiment-12-oscillator-strength-state-count-bound
```

## Recovery order

1. `experiments/12-oscillator-strength-state-count-bound/CURRENT_STATE.md`
2. `experiments/12-oscillator-strength-state-count-bound/REV6_EXTERNAL_REVIEW_RESPONSE_2026-08-15.md`
3. `experiments/12-oscillator-strength-state-count-bound/MANUSCRIPT_REV7_CHANGESET_2026-08-15.md`
4. `experiments/12-oscillator-strength-state-count-bound/PRB_REV7_RENDER_QA_2026-08-15.md`
5. `experiments/12-oscillator-strength-state-count-bound/numerics/kane_8band_capacity.py`
6. `experiments/12-oscillator-strength-state-count-bound/MANUSCRIPT_REV6_2026-08-14.md`
7. `experiments/12-oscillator-strength-state-count-bound/NOVELTY_AUDIT_2026-08-14.md`
8. `experiments/12-oscillator-strength-state-count-bound/PROGRESS_LOG.md`

## What changed after Rev6

A supplied extreme adversarial review rated the theorem mathematically sound but recommended major revision, focusing on:

```text
uniform thermodynamic boundedness of v_B^cap;
physical significance of the capacity resource;
missing realistic narrow-gap multiband validation;
missing van Roosbroeck-Shockley / fluctuation-dissipation context;
several smaller interpretation qualifications.
```

Rev7 addresses all of these without changing the central theorem.

## Controlling theorem

For selected direct cross-`mu` conductivity in window `B`,

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

Intrinsic neutral form:

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

## Thermodynamic condition added in Rev7

For a nonzero macroscopic density floor, require

```math
\boxed{
\bar v_B^{cap}
=\limsup_{V\to\infty}v_{B,V}^{cap}<\infty.
}
```

The finite-volume inequality itself remains exact without this extra condition.

## New realistic HgCdTe Kane validation

For the standard first-order 8x8 Kane Hamiltonian,

```math
\boxed{
\|\hat v_x\|_{op}=\sqrt{3/2}\,v_K,
\qquad
v_B^{cap}\le\sqrt{3/2}\,v_K.
}
```

Thus the capacity is uniformly bounded in system size in this realistic multiband narrow-gap model.

Numerical scales:

```text
measured HgCdTe v_K = (1.07 +/- 0.05)e6 m/s
-> central capacity <= 1.31e6 m/s;

E_P ~= 18.8 eV
-> capacity <= 1.286e6 m/s.
```

The exact coefficient is first-order Kane only; second-order 8x8 k.p models add finite k-dependent corrections.

## Rev7 production state

```text
experiment12_prb_rev7.tex
SHA-256 ec5f46f0256b320861fabdd3ad5e61832c1f20c03ea95216979207fe92dc488d

experiment12_prb_rev7.pdf
SHA-256 e481354dc25a0526dbe0b4eb636a0ca733aae8678f3a12b7a2d0a349d25c0740

7 pages / US letter / compile pass / all pages visually inspected / no layout regression.
```

## Scope and novelty

Valid only for independent-quasiparticle direct cross-`mu` charge absorbers. Do not promote this into universal dark-current, `D*`, generation-rate, or finite-bandwidth-noise claims. Excitonic/collective, indirect, many-body, and arbitrary photonic-enhancement cases remain outside scope.

```text
DIRECT PRIOR-ART COLLISION: NOT FOUND
PRIORITY: NOT ESTABLISHED
NOVELTY: NOT ESTABLISHED
NOVELTY RISK: HIGH
```

## ACTIVE NEXT ACTION

Perform a fresh hostile review of **Rev7**, with special attention to whether the Kane-capacity subsection genuinely resolves the prior significance objection and whether any stronger prior-art collision emerges from the VRS/FDT/Kane additions.

Do not add more theory by default.

## Closed previous branches

- Experiment 10: closed by default as novelty/manuscript path.
- Experiment 11: closed by default; retained result reduces to Maxwell-relaxation / reciprocal-sensitivity theory.