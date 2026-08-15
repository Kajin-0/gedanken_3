# Current State — Experiment 12

**Date:** 2026-08-15  
**Branch:** `experiment-12-oscillator-strength-state-count-bound`  
**Scope:** analytical/theoretical only

**Status:** **REV8 EXTREME REVIEW ADDRESSED / CENTRAL THEOREM SURVIVES / INTRINSIC-COROLLARY DOMAIN FIXED / PROJECTED-BLOCK SVD CAPACITY REPRODUCIBLE / HgCdTe MODEL BOUND-REFERENCE TEST RETAINED / PRB REV9 9-PAGE QA PASS / NOVELTY NOT ESTABLISHED**

## Read first

1. `REV8_EXTERNAL_REREVIEW_RESPONSE_2026-08-15.md`
2. `MANUSCRIPT_REV9_CHANGESET_2026-08-15.md`
3. `PRB_REV9_RENDER_QA_2026-08-15.md`
4. `numerics/kane_8band_tightness.py`
5. `HGCDTE_SECOND_ORDER_8BAND_TIGHTNESS_2026-08-15.md`
6. `REV7_EXTERNAL_REREVIEW_RESPONSE_2026-08-15.md`
7. `NOVELTY_AUDIT_2026-08-14.md`

Rev9 is the controlling local PRB manuscript/source state. Exact artifact hashes are in items 2–3.

---

# Controlling theorem — unchanged

For direct transitions crossing the chemical potential in selected positive-frequency window `B`,

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

The finite-system theorem is exact under the stated independent-quasiparticle/direct-transition assumptions.

For a fixed window, a macroscopic density statement requires

```math
\limsup_{V\to\infty}v_{B,V}^{cap}<\infty.
```

For a moving low-energy sequence `B_m`, the stronger double-uniformity condition is

```math
\boxed{
v_* = \sup_m\left[\limsup_{V\to\infty}v_{B_m,V}^{cap}\right]<\infty.
}
```

Then finite nonvanishing integrated selected spectral weight gives a nonzero low-energy active-population floor.

---

# Intrinsic-gap corollary — Rev9 domain correction

Do **not** state `n_e=n_h=n_th` from intrinsic neutrality alone when `n_e,n_h` are defined by the lower/upper-`mu` partition.

The one-species corollary is exact only when `mu` lies in a gap so the cross-`mu` partition coincides with valence/conduction manifolds:

```math
n_th
\ge
\frac{1}{\pi e^2(v_B^{cap})^2}
\int_B
\frac{\hbar\omega\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}\,d\omega.
```

When `mu` lies inside a nominal band, use the general two-sided hierarchy instead.

The realistic HgCdTe model is such a case: `mu-E_Gamma6 = +11.477 meV`.

---

# Realistic second-order HgCdTe test

Model: bulk constant-parameter second-order eight-band k.p Hamiltonian based on Novik et al., PRB 72, 035321 (2005), with representative linear interpolation of endpoint remote-band parameters.

Representative state:

```text
T = 300 K
Eg = 0.123984198 eV
x = 0.179727548
```

Conventional charge-neutral solution:

```text
conduction electron density = 5.050214e16 cm^-3
valence hole density        = 5.050214e16 cm^-3
```

Cross-mu theorem reference population:

```text
upper-mu electron population = 4.722888e16 cm^-3
lower-mu hole population     = 5.328518e16 cm^-3
reference total              = 1.005141e17 cm^-3
```

Conventional electron+hole total is `1.010043e17 cm^-3`; the difference is about 0.5%.

Window results:

```text
window       v_B^cap (m/s)   bound/reference   k_sel,max (nm^-1)
Eg..1.5Eg    1.016823e6      0.032046          0.149
Eg..2Eg      1.017273e6      0.074922          0.240
Eg..3Eg      1.015473e6      0.110977          0.415
Eg..0.5eV    1.015611e6      0.118010          0.583
```

For the broad window:

```text
population lower bound = 1.186163e16 cm^-3
bound/reference = 0.118010
```

The capacity is nearly window-independent; tightening is driven mainly by accumulated cross-mu spectral weight.

---

# Capacity implementation — now explicit and reproducible

The numerical calculation implements the theorem's **projected-block operator norm**, not a pairwise matrix-element maximum.

At each `k`:

```text
1. diagonalize H(k);
2. group exact model-degenerate eigenspaces;
3. assemble every opposite-side partner eigenspace satisfying the window;
4. construct P_lambda,k v_x(k) Q_lambda,k,B;
5. take its largest singular value;
6. maximize over shells and k, including lower-shell counterpart.
```

Bulk translational invariance makes the operator block diagonal in k.

Broad-window diagnostic:

```text
projected-block capacity = 1.015611e6 m/s
largest pairwise |v_cv|  = 0.868123e6 m/s
capacity/pairwise        = 1.169892
```

A pairwise-max substitute would overstate the population lower bound by `36.9%`.

Degeneracy clustering from `1e-10` through `1e-5 eV` leaves the capacity unchanged to reported precision at fixed quadrature.

Selected broad-window transitions involve Gamma8-derived -> Gamma6-derived branches; Gamma7-derived split-off branches do not enter the selected set. The selected optical window reaches only `|k|=0.583 nm^-1` even though the carrier reference integral is checked to `2.0 nm^-1`.

---

# First-order Kane resource retained

For the standard first-order 8x8 Kane Hamiltonian,

```math
\boxed{
\|v_x\|_{op}=\sqrt{3/2}\,v_K,
\qquad
v_B^{cap}\le\sqrt{3/2}\,v_K=P/\hbar.
}
```

This is a microscopic upper bound, not an assertion that each selected window attains the global operator norm.

---

# PRB Rev9 production

```text
experiment12_prb_rev9.tex
SHA-256 da4d929d77d817e48c6661d61ffcdcaac82a8503b9594a8dafcca27e838c0f7b

experiment12_prb_rev9.pdf
SHA-256 849e0653b6007c35a92967e812ab584ede70914714c2315bf849839701232e0b
```

QA:

```text
9 pages / US letter
3 pdflatex passes
no overfull boxes
no undefined refs/citations
no LaTeX/package warnings
PDF preflight pass
all 9 pages visually inspected
no clipping / overlap / broken glyphs / float regression
```

---

# Scope / novelty

Valid class: independent-quasiparticle direct cross-mu charge absorbers.

Do not infer universal dark current, thermal generation, D*, or finite-bandwidth noise. Excitons/collective states, indirect transitions, interacting many-body spectral functions, and unconstrained photonic enhancement remain outside scope.

```text
DIRECT PRIOR-ART COLLISION: NOT FOUND
PRIORITY: NOT ESTABLISHED
NOVELTY: NOT ESTABLISHED
NOVELTY RISK: HIGH
```

# ACTIVE NEXT ACTION

Perform another extreme hostile review of **Rev9**. Do not add more theory by default. The theorem itself has survived repeated independent attacks; further revision should be driven only by a concrete referee-level defect or by submission metadata/production needs.