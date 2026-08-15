# Agent recovery entrypoint

Read `AGENTS.md` first, then this file. Do not infer chronology from `main` alone.

## Hard scope

All research in this repo is analytical/theoretical only. Preserve failed, corrected, conditional, and negative paths. Do not use novelty or priority language without a dedicated audit.

# ACTIVE — Experiment 12 / PRB Rev8

Branch:

```text
experiment-12-oscillator-strength-state-count-bound
```

## Recovery order

1. `experiments/12-oscillator-strength-state-count-bound/CURRENT_STATE.md`
2. `experiments/12-oscillator-strength-state-count-bound/REV7_EXTERNAL_REREVIEW_RESPONSE_2026-08-15.md`
3. `experiments/12-oscillator-strength-state-count-bound/HGCDTE_SECOND_ORDER_8BAND_TIGHTNESS_2026-08-15.md`
4. `experiments/12-oscillator-strength-state-count-bound/MANUSCRIPT_REV8_CHANGESET_2026-08-15.md`
5. `experiments/12-oscillator-strength-state-count-bound/PRB_REV8_RENDER_QA_2026-08-15.md`
6. `experiments/12-oscillator-strength-state-count-bound/numerics/kane_8band_tightness.py`
7. `experiments/12-oscillator-strength-state-count-bound/NOVELTY_AUDIT_2026-08-14.md`

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

The central finite-volume theorem is unchanged from Rev7.

## Rev8 low-energy quantifier fix

For a moving low-energy window sequence `B_m`, require

```math
E_m=\sup_{\omega\in B_m}\hbar\omega\to0,
```

```math
W_m=\int_{B_m}\sigma_1^{cross}d\omega\to W_0>0,
```

and

```math
\boxed{
v_*=\sup_m\left[\limsup_{V\to\infty}v_{B_m,V}^{cap}\right]<\infty.
}
```

Then

```math
\liminf_m(n_{e,B_m}^{act}+n_{h,B_m}^{act})
\ge4k_BT W_0/(\pi e^2v_*^2)>0.
```

## Full realistic multiband test added in Rev8

A bulk second-order 8-band HgCdTe-like `k.p` model based on Novik et al. was evaluated end-to-end at 300 K and a 10-um gap.

Representative charge-neutral state:

```text
mu - Ec = +11.477 meV
cross-mu exact population = 1.005141e17 cm^-3
```

Windowed results:

```text
Eg..1.5Eg  bound/exact = 0.0320
Eg..2Eg    bound/exact = 0.0749
Eg..3Eg    bound/exact = 0.1110
Eg..0.5eV  bound/exact = 0.1180
```

Broad-window selected capacity:

```text
v_B^cap ~= 1.016e6 m/s
```

Headline result:

```math
\boxed{
(n_e+n_h)_{bound}/(n_e+n_h)_{exact}\simeq0.118.
}
```

The model-validation window through 0.5 eV is not a proposed detector bandwidth.

The first-order Kane value near 1.31e6 m/s is an **upper bound**, not the actual selected-window capacity. Higher-order k.p capacity claims are restricted to a bounded momentum domain of model validity.

## Appendix correction

Internal absorptance illustration now uses

```text
[1.02 omega_g, 1.10 omega_g]
```

and the conservative column from the first-order Kane upper bound is

```text
Sigma_e >= 4.19e11 cm^-2.
```

## Rev8 production

```text
experiment12_prb_rev8.tex
SHA-256 18424af7052262b2974a94a5ed6f85495951674fdcc0333624f3426f635df3a9

experiment12_prb_rev8.pdf
SHA-256 36e3fa7c01053bd5ec20f235cbb3f4f99c5297c3d44f11845440f77dff1da402

8 pages / US letter / compile warning-free / all pages visually inspected.
```

## Scope / novelty

Valid only for independent-quasiparticle direct cross-`mu` charge absorbers. Do not promote to universal dark-current, `D*`, generation-rate, or finite-bandwidth-noise claims.

```text
DIRECT PRIOR-ART COLLISION: NOT FOUND
PRIORITY: NOT ESTABLISHED
NOVELTY: NOT ESTABLISHED
NOVELTY RISK: HIGH
```

## ACTIVE NEXT ACTION

Perform a new extreme hostile review of **Rev8**. Do not add more theory by default unless that review finds a genuine blocker.

## Closed previous branches

Experiment 10 and Experiment 11 remain closed by default as novelty/manuscript paths.