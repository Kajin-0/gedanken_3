# Agent recovery entrypoint

Read `AGENTS.md` first, then this file. Do not infer chronology from `main` alone.

## Hard scope

All research is analytical/theoretical only. Preserve failed, corrected, conditional, and negative paths. Do not claim novelty or priority without a dedicated audit.

# ACTIVE — Experiment 12 / PRB Rev9

Branch:

```text
experiment-12-oscillator-strength-state-count-bound
```

## Recovery order

1. `experiments/12-oscillator-strength-state-count-bound/CURRENT_STATE.md`
2. `experiments/12-oscillator-strength-state-count-bound/REV8_EXTERNAL_REREVIEW_RESPONSE_2026-08-15.md`
3. `experiments/12-oscillator-strength-state-count-bound/MANUSCRIPT_REV9_CHANGESET_2026-08-15.md`
4. `experiments/12-oscillator-strength-state-count-bound/PRB_REV9_RENDER_QA_2026-08-15.md`
5. `experiments/12-oscillator-strength-state-count-bound/numerics/kane_8band_tightness.py`
6. `experiments/12-oscillator-strength-state-count-bound/HGCDTE_SECOND_ORDER_8BAND_TIGHTNESS_2026-08-15.md`
7. `experiments/12-oscillator-strength-state-count-bound/NOVELTY_AUDIT_2026-08-14.md`

## Controlling result

```math
n_e+n_h
\ge n_{e,B}^{act}+n_{h,B}^{act}
\ge
\frac{2}{\pi e^2(v_B^{cap})^2}
\int_B
\frac{\hbar\omega\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}\,d\omega.
```

The theorem is unchanged in Rev9.

The one-species intrinsic corollary `n_e=n_h=n_th` is valid only when `mu` lies in a gap and the cross-mu partition coincides with valence/conduction manifolds. The realistic HgCdTe test has `mu` 11.477 meV above the nominal Gamma6 edge, so it uses the general hierarchy.

## Realistic HgCdTe result

Second-order eight-band bounded-domain model at 300 K / 10 um:

```text
cross-mu reference population = 1.005141e17 cm^-3
broad-window v_B^cap          = 1.015611e6 m/s
population lower bound        = 1.186163e16 cm^-3
bound/reference               = 0.118010
selected k max                = 0.583 nm^-1
```

The numerical capacity is the full projected-block SVD norm required by the theorem. Largest pairwise matrix element is only `0.868123e6 m/s`; using it would overstate the bound by 36.9%.

## Production

```text
Rev9 TeX SHA-256 da4d929d77d817e48c6661d61ffcdcaac82a8503b9594a8dafcca27e838c0f7b
Rev9 PDF SHA-256 849e0653b6007c35a92967e812ab584ede70914714c2315bf849839701232e0b
9 pages / US letter / compile clean / visual QA pass.
```

## Scope / novelty

No universal dark-current, D*, generation-rate, or finite-bandwidth-noise claim. Excitons, indirect transitions, interacting many-body spectral functions, and unconstrained photonic enhancement remain outside scope.

```text
DIRECT PRIOR-ART COLLISION: NOT FOUND
NOVELTY: NOT ESTABLISHED
```

## Next action

Perform a fresh hostile review of Rev9. Do not add more theory unless that review finds a concrete defect.