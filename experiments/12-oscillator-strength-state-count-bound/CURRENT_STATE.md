# Current State — Experiment 12

**Date:** 2026-08-15  
**Branch:** `experiment-12-oscillator-strength-state-count-bound`  
**Scope:** analytical/theoretical only

**Status:** **REV11 MINOR REFEREE CLEANUP COMPLETE / CENTRAL EQ. (29) UNCHANGED / PRB TYPESET QA PASS / NO MAJOR TECHNICAL DEFECT REMAINS IN LATEST ADVERSARIAL REVIEW / NOVELTY PLAUSIBLE BUT PRIORITY NOT ESTABLISHED**

## Read first

1. `PRB_REV11_MINOR_REVISION_QA_2026-08-15.md`
2. `REV10_MINOR_REREVIEW_RESPONSE_2026-08-15.md`
3. `typeset/rev10_to_rev11_minor_revision.patch`
4. `numerics/parameter_sensitivity_audit.py`
5. `PRB_REV10_REFEREE_REPAIR_QA_2026-08-15.md`
6. `REV9_SUPREMUM_REREVIEW_RESOLUTION_2026-08-15.md`
7. `numerics/supremum_active_support_audit.py`
8. `typeset/rev9_exposition_to_rev10_referee_repaired.patch`
9. `MANUSCRIPT_REV9_EXPOSITION_REVISED_2026-08-15.md`
10. `numerics/kane_8band_tightness.py`

The exact Rev11 source is reconstructed by first reconstructing Rev10 and then applying item 3. The final Rev11 TeX was verified byte-for-byte against that reconstruction.

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

Eq. (29), the pointwise Fermi inequality, the projected-shell rank/capacity proof, the fixed-window thermodynamic hypothesis, and the moving-window low-energy theorem are unchanged in Rev11.

The intrinsic one-species corollary remains restricted to the case in which `mu` lies in a gap and the cross-`mu` partition coincides with the valence/conduction manifolds.

---

# Rev11 minor referee cleanup

The latest adversarial rereview judged the Rev9 ordinary-supremum objection correctly repaired and found no major technical defect. Rev11 addresses the remaining cleanup requests without reopening the central theory.

## Eq. (49) now explicitly matches the complete energy-shell definition

For a finite periodic normalization volume, translational invariance makes the homogeneous velocity operator block diagonal in crystal momentum:

```math
P_\epsilon v_xQ_{\epsilon,B}
=\bigoplus_{\mathbf k}
P_{\epsilon,\mathbf k}v_x(\mathbf k)Q_{\epsilon,\mathbf k,B}.
```

Therefore the operator norm of a complete exact-energy shell is the maximum of its finite-`k` block norms, becoming the ordinary `k` supremum in the bulk limit. This directly links Eq. (49) to Eq. (21).

Do not revert Eq. (49) to `ess sup`.

## Support-rank numerical criterion is now explicit

The exact theorem uses exact rank. The Table-II numerical active-support diagnostic counts a singular value as nonzero when

```text
s > 1e-6 m/s.
```

This threshold affects only the diagnostic decomposition, not the central lower bound.

Reduced broad-window `40 x 6 x 8` audit:

```text
rank threshold (m/s)     n_B^act/n_ref
1e-9                     0.660512373
1e-6                     0.660512373
1e-3                     0.660512373
1                        0.660512373
1e2                      0.660512373
1e4                      0.660512373
```

Thus the numerical support diagnostic is stable over the tested threshold range. Production Table-II broad support fraction remains `~0.669`.

## Onishi–Fu neighboring literature added

Rev11 cites:

```text
Y. Onishi and L. Fu,
Phys. Rev. X 14, 011052 (2024),
DOI 10.1103/PhysRevX.14.011052.
```

Positioning:

```text
Onishi–Fu: generalized optical weight / topology / quantum geometry / topological-gap bound.
Experiment 12: finite-temperature cross-mu thermal population bound / thermal kernel / per-shell velocity capacity.
```

This is neighboring literature, not an identified collision with Eq. (29). No priority claim is introduced.

## Lightweight parameter-sensitivity diagnostic added

One-at-a-time `+/-5%` perturbations of

```text
EP, Delta, F, gamma1, gamma2, gamma3
```

are evaluated on a common reduced `24 x 4 x 6` diagnostic quadrature with charge neutrality re-solved and the projected-block capacity searched continuously.

```text
reduced-grid baseline ratio = 0.1226
perturbed range             = 0.1098 ... 0.1293
relative range              ~= -10.5% ... +5.5%
```

This is not an uncertainty propagation and does not replace the production value. It supports only the robustness statement that the realistic-model tightness remains of order `10^-1` under modest independent parameter perturbations.

Reproducibility: `numerics/parameter_sensitivity_audit.py`.

## Appendix B1

The secondary occupation-variance inequality now includes its one-line proof:

```math
[\sqrt a(1+b)-\sqrt b(1+a)]^2\ge0.
```

---

# Controlling HgCdTe production result

Representative second-order eight-band bounded-domain model at 300 K / 10 um:

```text
n_ref cross-mu                 = 1.005141e17 cm^-3
ordinary projected-block sup   ~= 1.01764e6 m/s
broad bound/reference precise  ~= 0.1175
headline rounded ratio         = 0.118 / 11.8%
broad lower bound              ~= 1.18e16 cm^-3
n_B^act/n_ref                  ~= 0.669
n_bound/n_B^act                ~= 0.176
pairwise ordinary sup          ~= 0.87165e6 m/s
pairwise substitution bias     ~= +36.3%
selected k onset               ~= 0.05535 nm^-1
selected k max                 ~= 0.583 nm^-1
```

The isolated Gamma point is not a selected cross-`mu` block because `mu` lies 11.477 meV above the nominal Gamma6 edge; Gamma6 and Gamma8 are both below `mu` at `k=0`.

Production quadrature remains

```text
160 radial Gauss-Legendre x 10 cos(theta) Gauss-Legendre x 16 uniform phi
```

with `1e-7 eV` degeneracy clustering. A `200 x 12 x 20` grid is an additional support-population check.

---

# Rev11 production / QA

```text
Rev11 TeX SHA-256 a75b75d6016d335746751b7c75a01d49deea7c4796c2eff30a7dd99c1f73cd68
Rev11 PDF SHA-256 ed5a558ac561cb67f0e918de96f4774c493cacd54fd6f3bea01e597890a7df5d
```

```text
REVTeX 4-2 / APS PRB reprint / US letter
13 pages
3 pdflatex passes
no overfull boxes
no undefined refs/citations
no critical package/class warnings
all 13 pages visually inspected
main equations (1)-(50)
appendix equations (A1), (B1)
Tables I-III
19 references
```

Source reconstruction path:

1. recover `typeset/experiment12_prb_rev9_exposition_revised.tex.gz.b64`;
2. apply `typeset/rev9_exposition_to_rev10_referee_repaired.patch`;
3. apply `typeset/rev10_to_rev11_minor_revision.patch`;
4. verify the Rev11 TeX SHA above.

---

# Scope / novelty

No universal dark-current, generation-rate, `D*`, or finite-bandwidth-noise claim. Excitons/collective states, indirect transitions, interacting spectral functions, and unconstrained photonic enhancement remain outside scope.

```text
DIRECT PRIOR-ART COLLISION: NOT FOUND IN TARGETED SEARCH
NOVELTY: PLAUSIBLE / HISTORICAL PRIORITY NOT ESTABLISHED
PRIORITY: NOT ESTABLISHED
```

# ACTIVE NEXT ACTION

Treat Rev11 as the controlling submission candidate. Another adversarial pass may be used as a final regression check, but do not continue defensive rewriting absent a concrete mathematical defect, numerical inconsistency, direct prior-art collision, or specific journal-facing requirement. The latest rereview has moved the risk from elementary technical correctness to ordinary publication significance/editorial judgment.
