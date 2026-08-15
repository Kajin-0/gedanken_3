# Current State — Experiment 12

**Date:** 2026-08-15  
**Branch:** `experiment-12-oscillator-strength-state-count-bound`  
**Scope:** analytical/theoretical only

**Status:** **EXTERNAL REV6 MAJOR REVIEW ADDRESSED / CENTRAL THEOREM SURVIVES / THERMODYNAMIC CAPACITY HYPOTHESIS FORMALIZED / REALISTIC 8x8 HgCdTe KANE CAPACITY DERIVED / VRS+FDT POSITIONING ADDED / PRB REV7 COMPILE+7-PAGE VISUAL QA PASS / NOVELTY NOT ESTABLISHED**

## Read first

1. `REV6_EXTERNAL_REVIEW_RESPONSE_2026-08-15.md`
2. `MANUSCRIPT_REV7_CHANGESET_2026-08-15.md`
3. `PRB_REV7_RENDER_QA_2026-08-15.md`
4. `numerics/kane_8band_capacity.py`
5. `MANUSCRIPT_REV6_2026-08-14.md`
6. `MANUSCRIPT_REV6_FINAL_QA_2026-08-14.md`
7. `NOVELTY_AUDIT_2026-08-14.md`
8. `PROGRESS_LOG.md`

Rev6 remains the last full manuscript text stored directly in the branch. The QA-passed Rev7 PRB source/PDF were produced locally; their exact SHA-256 hashes and the complete scientific changeset are recorded in items 2–3 above.

---

# Controlling finite-volume theorem

For exact independent-quasiparticle states with `E_v < mu < E_c`, define the direct cross-chemical-potential conductivity

```math
\sigma_1^{cross}(\omega)
=\frac{\pi e^2}{V}
\sum_{cv}
\frac{[f(E_v)-f(E_c)]|v_{cv}|^2}{E_{cv}}
\delta\!\left(\omega-\frac{E_{cv}}{\hbar}\right).
```

The exact pointwise Fermi inequality is

```math
\boxed{
\frac{2[f(E_v)-f(E_c)]}
{e^{E_{cv}/(2k_BT)}-1}
\le
f(E_c)+1-f(E_v).
}
```

For a selected positive-frequency window `B`, exact energy-shell projectors define selected optical blocks and the basis-invariant capacity

```math
\boxed{
(v_B^{cap})^2
=\max\left[
\sup_{\epsilon_c>\mu}\|A_{\epsilon_c,B}\|_{op}^2,
\sup_{\epsilon_v<\mu}\|B_{\epsilon_v,B}\|_{op}^2
\right].
}
```

Define support-rank thermal populations

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

Finite-volume correctness is unchanged by Rev7.

---

# New formal thermodynamic hypothesis

A nonzero macroscopic density-floor interpretation requires uniform boundedness of the optical capacity along the thermodynamic sequence:

```math
\boxed{
\bar v_B^{cap}
\equiv
\limsup_{V\to\infty}v_{B,V}^{cap}<\infty.
}
```

The finite-system inequality does not require this assumption; the thermodynamic density consequence does.

The low-energy conclusion is therefore stated only as

```text
low transition energy
+ finite nonvanishing integrated direct cross-mu spectral weight
+ uniformly bounded per-shell optical capacity
+ independent-quasiparticle direct-transition description
-> nonvanishing active thermal population floor.
```

---

# Realistic narrow-gap capacity validation — HgCdTe 8x8 Kane model

For the standard first-order 8x8 Kane Hamiltonian used for bulk HgCdTe optical calculations,

```math
\hat v_x=(1/\hbar)\partial H_K/\partial k_x=v_KM_x.
```

The published matrix structure gives two nontrivial weighted-star blocks with squared coupling sum

```math
3/4+1/4+1/2=3/2.
```

Hence

```math
\boxed{\|\hat v_x\|_{op}=\sqrt{3/2}\,v_K}
```

and for every selected optical window

```math
\boxed{v_B^{cap}\le\sqrt{3/2}\,v_K.}
```

This ceiling is independent of system volume in the first-order model and therefore supplies the requested uniform thermodynamic bound automatically.

Equivalent Kane-energy form:

```math
\boxed{
v_B^{cap}
\le\frac{P}{\hbar}
=\sqrt{\frac{E_P}{2m_0}}.
}
```

Numerical scales retained in Rev7:

```text
measured HgCdTe v_K = (1.07 +/- 0.05)e6 m/s
-> central v_B^cap <= 1.31e6 m/s;

E_P ~= 18.8 eV
-> v_K ~= 1.050e6 m/s
-> v_B^cap <= 1.286e6 m/s.
```

The exact `sqrt(3/2)` coefficient is restricted to the first-order 8x8 Kane Hamiltonian. Second-order 8x8 k.p models introduce finite k-dependent corrections; Rev7 states this explicitly.

For the same ideal internal single-pass 10-um/300-K witness used previously, the measured-central capacity scale gives an illustrative total intrinsic electron-column lower bound of about

```text
5.33e11 cm^-2.
```

This is an ideal optical-model illustration, not a claim that real bulk HgCdTe realizes that absorptance model exactly.

---

# Other Rev7 corrections from the external review

Rev7 now also:

```text
adds a limiting prescription for selected endpoints exactly at E=mu;
qualifies n_B^act as an exact but rank-discontinuous support-dimension construct;
states that experimental use requires sigma_1 ~= sigma_1^cross in the chosen window or a decomposition;
qualifies global parabolic saturation as an ideal effective two-band optical-model result;
clarifies the Appendix-A 90% value as internal absorptance of admitted power / ideal AR or index matching;
adds van Roosbroeck-Shockley detailed-balance context;
adds fluctuation-dissipation context and distinguishes it from the theorem.
```

No dark-current, `D*`, generation-rate, or finite-bandwidth-noise theorem was added.

---

# Equality / independent checks retained

```text
Ideal equal-mass mirror-symmetric parabolic model:
    active-subspace theorem exact for any selected direct window;
    total-population theorem exact only within the stated ideal full-spectrum model.

2-D neutral massless Dirac: 0.5000
3-D massless Dirac:         0.6667
3-D massive Dirac,
10 um / 300 K:              0.794684
```

Unequal parabolic masses, nondegenerate global limit:

```math
n_{bound}/n_{exact}
=[4m_em_h/(m_e+m_h)^2]^{3/4}\le1.
```

---

# Scope boundary

Valid class:

```text
independent-quasiparticle direct cross-mu charge absorbers.
```

Do not automatically extend to bound excitons, neutral collective states, phonon-assisted transitions, interacting many-body spectral functions, or arbitrary passive photonic path enhancement.

Localized states do not break the state-count theorem but block automatic inference to DC dark current.

`n_B^act` is a support-dimension mathematical construct, not automatically an experimentally robust participation count.

Measured total optical conductivity may contain intraband, same-side interband, phonon-assisted, and excitonic contributions. Apply the theorem only to isolated `sigma_1^cross` or a window where it dominates.

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

# PRB Rev7 production state

Local QA-passed artifacts:

```text
experiment12_prb_rev7.tex
SHA-256 ec5f46f0256b320861fabdd3ad5e61832c1f20c03ea95216979207fe92dc488d

experiment12_prb_rev7.pdf
SHA-256 e481354dc25a0526dbe0b4eb636a0ca733aae8678f3a12b7a2d0a349d25c0740
```

Render state:

```text
REVTeX COMPILE: PASS
PAGES: 7
US LETTER: PASS
OVERFULL BOXES: NONE
UNDEFINED REFERENCES/CITATIONS: NONE
LATEX/PACKAGE WARNINGS: NONE
PDF PREFLIGHT: PASS
ALL 7 PAGES VISUALLY INSPECTED: PASS
CLIPPING/OVERLAP/BROKEN GLYPHS: NONE
```

Details: `PRB_REV7_RENDER_QA_2026-08-15.md`.

---

# ACTIVE NEXT ACTION

The correct next action is **another independent hostile review of Rev7 itself**.

Do not add new theory by default. The main Rev6 referee criticism about an unconstrained/formal `v_B^cap` has now been answered with a realistic, uniformly bounded multiband Kane example. Further additions should occur only if the Rev7 review exposes a genuine remaining blocker.