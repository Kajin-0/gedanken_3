# Current State — Experiment 12

**Date:** 2026-08-15  
**Branch:** `experiment-12-oscillator-strength-state-count-bound`  
**Scope:** analytical/theoretical only

**Status:** **REV10 REFEREE REPAIR COMPLETE / CENTRAL EQ. (29) UNCHANGED / SUPREMUM FORMALISM REPAIRED / HGCDTE AUDIT UPDATED / PRB TYPESET QA PASS / NOVELTY PLAUSIBLE BUT PRIORITY NOT ESTABLISHED**

## Read first

1. `PRB_REV10_REFEREE_REPAIR_QA_2026-08-15.md`
2. `REV9_SUPREMUM_REREVIEW_RESOLUTION_2026-08-15.md`
3. `typeset/rev9_exposition_to_rev10_referee_repaired.patch`
4. `numerics/supremum_active_support_audit.py`
5. `MANUSCRIPT_REV9_EXPOSITION_REVISED_2026-08-15.md`
6. `REV9_EXPOSITION_REVISION_QA_2026-08-15.md`
7. `INDEPENDENT_NOVELTY_SIGNIFICANCE_ASSESSMENT_2026-08-15.md`
8. `numerics/kane_8band_tightness.py`
9. `HGCDTE_SECOND_ORDER_8BAND_TIGHTNESS_2026-08-15.md`

The Rev10 production source is the Rev9 exposition source plus the exact committed patch in item 3. The reconstruction was verified byte-for-byte against the final local TeX.

---

# Controlling theorem — unchanged

For selected positive-frequency direct transitions crossing the chemical potential,

```math
\boxed{
n_e+n_h
\ge n_{e,B}^{act}+n_{h,B}^{act}
\ge
\frac{2}{\pi e^2(v_B^{cap})^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}\,d\omega.
}
```

The finite-system theorem and its proof are unchanged by Rev10.

For fixed `B`, a macroscopic density statement requires

```math
\limsup_{V\to\infty}v_{B,V}^{cap}<\infty.
```

For a moving low-energy sequence `B_m`, retain

```math
v_* = \sup_m\left[\limsup_{V\to\infty}v_{B_m,V}^{cap}\right]<\infty.
```

The intrinsic one-species corollary remains restricted to the case in which `mu` lies in a gap and the cross-`mu` partition coincides with the valence/conduction manifolds.

---

# Rev10 referee repair — controlling change

An adversarial rereview found that Eqs. (21)–(22) define the capacity with an **ordinary supremum**, while the Rev9 bulk HgCdTe specialization had been written with `ess sup` in Eq. (49).

That formal mismatch was real and is now fixed conservatively. Rev10 uses

```math
v_B^{cap}
=\sup_{\mathbf k\in\mathcal K,\lambda}
 s_{\max}[P_{\lambda\mathbf k}v_x(\mathbf k)Q_{\lambda\mathbf k,B}],
```

with the corresponding lower-shell blocks also included. No new density/essential-supremum theorem was introduced.

## Why the proposed isolated-Gamma correction is rejected

The rereview proposed that the exact Gamma8 degeneracy at Gamma forces a selected capacity of order `v_K`, lowering the broad HgCdTe ratio to about 0.110.

That argument overlooks the theorem's cross-chemical-potential selection. In the numerical charge-neutral state,

```text
Eg = 0.123984198 eV
mu - Eg = +11.477 meV
```

so at `k=0` the Gamma6 pair and Gamma8 manifold are all **below mu**. There is therefore no selected Gamma8-to-Gamma6 cross-`mu` block at Gamma.

The selected set begins at finite momentum near

```text
|k| ~= 0.05535 nm^-1.
```

A continuous ordinary-supremum search gives

```text
v_B^cap ~= 1.01764e6 m/s
```

for all four Table-II windows at the reported numerical resolution.

---

# Revised HgCdTe validation

Reference cross-`mu` population remains

```text
n_ref = 1.005141e17 cm^-3.
```

The ordinary-supremum audit gives approximately:

```text
window       v_B^cap (m/s)   bound/reference   n_B^act/n_ref   bound/n_B^act   k_sel,max
Eg..1.5Eg    1.01764e6       0.0320            0.264           0.121           0.149
Eg..2Eg      1.01764e6       0.0749            0.450           0.166           0.240
Eg..3Eg      1.01764e6       0.1105            0.562           0.197           0.415
Eg..0.5eV    1.01764e6       0.1175            0.669           0.176           0.583
```

Broad-window lower bound:

```text
~1.18e16 cm^-3.
```

The manuscript headline remains `0.118` / `11.8%` because `0.1175` rounds to that precision.

The new active-support decomposition removes an overcompressed causal statement. In the broad window:

```text
selected-support fraction n_B^act/n_ref       ~= 0.669
Fermi/capacity tightness n_bound/n_B^act      ~= 0.176
product n_bound/n_ref                         ~= 0.1175
```

Thus incomplete selected support and Fermi/capacity slack are quantitatively distinct. Do not attribute the full loss solely to heavy-hole/multiband asymmetry.

Continuous broad-window pairwise audit:

```text
projected-block ordinary sup = 1.01764e6 m/s
pairwise ordinary sup        = 0.87165e6 m/s
pairwise substitution error  ~= +36.3% in the lower bound
```

---

# Numerical reproducibility — Rev10

Production integrals:

```text
Nk radial Gauss-Legendre       = 160
Ncos Gauss-Legendre            = 10
Nphi uniform azimuthal         = 16
degeneracy clustering          = 1e-7 eV
```

Additional support check:

```text
200 x 12 x 20
```

The ordinary capacity supremum is searched continuously in `(k,theta,phi)` rather than identified with the largest quadrature node.

Eq. (48) now distinguishes the angular-frequency window `B` from its energy image

```math
\mathcal E_B=\{\hbar\omega:\omega\in B\},
```

and applies the indicator to transition energy.

---

# Rev10 production / QA

Production TeX SHA-256:

```text
454a2ff8aba637d2e4c66ef5747899e85894996a020c633296cf950044c79b3d
```

Production PDF SHA-256:

```text
31ec4dd408552318f21de3e6bc7366e1b87badd7721a21575250c73adbb59a54
```

Format / QA:

```text
REVTeX 4-2 / APS PRB reprint / US letter
13 pages
3 pdflatex passes
no overfull boxes
no undefined refs/citations
no critical package/class warnings
all 13 pages visually inspected
```

Structural retention:

```text
main equations (1)-(50)
appendix equations (A1), (B1)
Tables I-III
18 references
Sections I-VIII + Appendices A/B
```

Exact source reconstruction path:

1. recover `typeset/experiment12_prb_rev9_exposition_revised.tex.gz.b64`;
2. apply `typeset/rev9_exposition_to_rev10_referee_repaired.patch`;
3. verify the TeX SHA above.

---

# Scope / novelty

No universal dark-current, generation-rate, `D*`, or finite-bandwidth-noise claim. Excitons/collective states, indirect transitions, interacting spectral functions, and unconstrained photonic enhancement remain outside scope.

```text
DIRECT PRIOR-ART COLLISION: NOT FOUND IN TARGETED SEARCH
NOVELTY: PLAUSIBLE / HISTORICAL PRIORITY NOT ESTABLISHED
PRIORITY: NOT ESTABLISHED
```

# ACTIVE NEXT ACTION

Treat Rev10 as the controlling submission candidate. The next useful action is another adversarial rereview directed specifically at the repaired ordinary-supremum implementation, active-support decomposition, Eq. (48) energy-window notation, and any accidental regressions from the surgical edits. Do not reopen unrelated theory unless that review exposes a concrete defect.