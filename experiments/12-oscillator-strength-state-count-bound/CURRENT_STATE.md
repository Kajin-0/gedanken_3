# Current State — Experiment 12

**Date:** 2026-08-15  
**Branch:** `experiment-12-oscillator-strength-state-count-bound`  
**Scope:** analytical/theoretical only

**Status:** **REV7 EXTREME RE-REVIEW ADDRESSED / CENTRAL THEOREM SURVIVES / MOVING-WINDOW DOUBLE UNIFORMITY FORMALIZED / FULL SECOND-ORDER HgCdTe 8-BAND BOUND-EXACT TEST COMPLETE / PRB REV8 COMPILE + 8-PAGE VISUAL QA PASS / NOVELTY NOT ESTABLISHED**

## Read first

1. `REV7_EXTERNAL_REREVIEW_RESPONSE_2026-08-15.md`
2. `HGCDTE_SECOND_ORDER_8BAND_TIGHTNESS_2026-08-15.md`
3. `MANUSCRIPT_REV8_CHANGESET_2026-08-15.md`
4. `PRB_REV8_RENDER_QA_2026-08-15.md`
5. `numerics/kane_8band_tightness.py`
6. `REV6_EXTERNAL_REVIEW_RESPONSE_2026-08-15.md`
7. `MANUSCRIPT_REV7_CHANGESET_2026-08-15.md`
8. `NOVELTY_AUDIT_2026-08-14.md`

Rev6 remains the last full markdown manuscript stored directly in the branch. Rev8 is the controlling QA-passed local PRB source/PDF; exact hashes and a deterministic changeset are recorded in items 3–4 above.

---

# Controlling finite-volume theorem — unchanged

For exact independent-quasiparticle states with `E_v < mu < E_c`, define direct cross-chemical-potential conductivity

```math
\sigma_1^{cross}(\omega)
=\frac{\pi e^2}{V}
\sum_{cv}
\frac{[f(E_v)-f(E_c)]|v_{cv}|^2}{E_{cv}}
\delta\!\left(\omega-\frac{E_{cv}}{\hbar}\right).
```

For selected positive-frequency window `B`, exact energy-shell projectors define selected optical blocks and

```math
\boxed{
(v_B^{cap})^2
=\max\left[
\sup_{\epsilon_c>\mu}\|A_{\epsilon_c,B}\|_{op}^2,
\sup_{\epsilon_v<\mu}\|B_{\epsilon_v,B}\|_{op}^2
\right].
}
```

With support-rank thermal populations `n_{e,B}^{act}`, `n_{h,B}^{act}`,

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

The central finite-volume theorem was not modified in Rev8.

---

# Thermodynamic and low-energy limits — Rev8 formalization

For fixed `B`, a macroscopic density statement requires

```math
\bar v_B^{cap}
=\limsup_{V\to\infty}v_{B,V}^{cap}<\infty.
```

The Rev7 re-review correctly identified that a moving low-energy window introduces a second quantifier. Rev8 now defines a sequence `B_m` with

```math
E_m=\sup_{\omega\in B_m}\hbar\omega\to0,
```

```math
W_m=\int_{B_m}\sigma_1^{cross}(\omega)d\omega\to W_0>0,
```

and explicitly requires

```math
\boxed{
v_*
=\sup_m\left[\limsup_{V\to\infty}v_{B_m,V}^{cap}\right]<\infty.
}
```

Then

```math
\boxed{
\liminf_{m\to\infty}
(n_{e,B_m}^{act}+n_{h,B_m}^{act})
\ge
\frac{4k_BT}{\pi e^2v_*^2}W_0>0.
}
```

This closes the moving-window quantifier issue.

---

# First-order Kane capacity — interpretation fixed

For the standard first-order HgCdTe 8x8 Kane Hamiltonian,

```math
\|\hat v_x\|_{op}=\sqrt{3/2}\,v_K,
```

hence

```math
v_B^{cap}\le\sqrt{3/2}\,v_K=P/\hbar.
```

The `~1.31e6 m/s` HgCdTe value is now described only as a microscopic **upper bound**, not as the actual selected-window capacity.

Higher-order k.p terms are explicitly restricted to finite spectral windows inside a bounded `k` domain where the expansion is used. No global high-k velocity ceiling is claimed for a quadratic continuum model.

---

# Full second-order HgCdTe-like tightness validation — new in Rev8

Controlling note:

`HGCDTE_SECOND_ORDER_8BAND_TIGHTNESS_2026-08-15.md`

Script:

`numerics/kane_8band_tightness.py`

Model:

```text
bulk constant-parameter second-order 8-band k.p Hamiltonian of
Novik et al., Phys. Rev. B 72, 035321 (2005).
```

Representative state:

```text
T = 300 K
Eg = 0.123984198 eV (10 um)
x = 0.179727548 using the Laurenti Eg(x,T) convention
```

Remote parameters are linearly interpolated between the Novik HgTe/CdTe endpoints as an explicit modeling choice.

Charge-neutral calculation:

```text
mu - Ec = +11.477 meV
physical electron density = 5.050214e16 cm^-3
physical hole density     = 5.050214e16 cm^-3
cross-mu exact theorem population = 1.005141e17 cm^-3
```

The theorem population differs from the conventional electron-plus-hole total by only about `0.5%` in this state.

Windowed results:

```text
window          v_B^cap (m/s)    bound/exact
Eg..1.5Eg       1.016823e6        0.032046
Eg..2Eg         1.017273e6        0.074922
Eg..3Eg         1.015473e6        0.110977
Eg..0.5eV       1.015611e6        0.118010
```

Thus for the broad low-energy model-validation window,

```math
\boxed{
(n_e+n_h)_{bound}\simeq1.19\times10^{16}\ \mathrm{cm^{-3}},
\qquad
(n_e+n_h)_{bound}/(n_e+n_h)_{exact}\simeq0.118.
}
```

This is materially looser than the symmetric parabolic/Dirac validation families, as expected from heavy-hole and multiband asymmetry, but remains order `10^-1` rather than numerically negligible.

The `0.5 eV` window is a model-validation interval, not a detector bandwidth.

Convergence checks versus carrier/optical `k` cutoff and quadrature are documented in the controlling note.

---

# Appendix-A correction

The internal single-pass illustration now uses

```text
B = [1.02 omega_g, 1.10 omega_g]
```

rather than starting at the exact absorption edge.

Recalculated electron-column bounds:

```text
5.0e5 m/s  -> 2.88e12 cm^-2
1.0e6      -> 7.20e11
1.07e6     -> 6.29e11
2.0e6      -> 1.80e11
3.0e6      -> 8.00e10
```

Using the first-order HgCdTe capacity upper bound `v_B^cap <= 1.31e6 m/s` gives the conservative illustrative lower column

```text
Sigma_e >= 4.19e11 cm^-2.
```

---

# Independent validations retained

```text
2-D neutral massless Dirac: 0.5000
3-D massless Dirac:         0.6667
3-D massive Dirac, 10 um / 300 K: 0.794684
```

Ideal equal-mass parabolic active-subspace bound saturates within the stated optical model. Unequal-mass nondegenerate global ratio remains

```math
[4m_em_h/(m_e+m_h)^2]^{3/4}.
```

---

# Scope boundary

Valid class:

```text
independent-quasiparticle direct cross-mu charge absorbers.
```

Do not infer universal dark current, thermal generation rate, `D*`, or finite-bandwidth noise.

Do not automatically extend to bound excitons/collective states, indirect phonon-assisted absorption, interacting many-body spectral functions, or arbitrary passive photonic enhancement.

Apply the theorem to measured conductivity only when `sigma_1^cross` is isolated or dominates the chosen window.

---

# Novelty status

```text
DIRECT PRIOR-ART COLLISION: NOT FOUND
PRIORITY: NOT ESTABLISHED
NOVELTY: NOT ESTABLISHED
NOVELTY RISK: HIGH
```

No `first`, `novel`, or priority wording is authorized.

---

# PRB Rev8 production state

```text
experiment12_prb_rev8.tex
SHA-256 18424af7052262b2974a94a5ed6f85495951674fdcc0333624f3426f635df3a9

experiment12_prb_rev8.pdf
SHA-256 36e3fa7c01053bd5ec20f235cbb3f4f99c5297c3d44f11845440f77dff1da402
```

```text
REVTeX COMPILE: PASS
PAGES: 8
US LETTER: PASS
OVERFULL BOXES: NONE
UNDEFINED REFERENCES/CITATIONS: NONE
STUCK FLOATS: NONE
LATEX/PACKAGE WARNINGS: NONE
PDF PREFLIGHT: PASS
ALL 8 PAGES VISUALLY INSPECTED: PASS
CLIPPING/OVERLAP/BROKEN GLYPHS: NONE
```

Details: `PRB_REV8_RENDER_QA_2026-08-15.md`.

---

# ACTIVE NEXT ACTION

The correct next action is **another independent extreme adversarial review of Rev8**.

Do not add new theory by default. Rev8 now addresses the principal remaining Rev7 significance issue by testing the complete theorem in the same realistic second-order multiband narrow-gap model.