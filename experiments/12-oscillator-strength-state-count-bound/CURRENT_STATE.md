# Current State — Experiment 12

**Date:** 2026-08-15  
**Branch:** `experiment-12-oscillator-strength-state-count-bound`  
**Scope:** analytical/theoretical only

**Status:** **REV11 CENTRAL THEORY AND HgCdTe VALIDATION PASS FINAL ADVERSARIAL REGRESSION / ONE PRE-SUBMISSION LITERATURE-COMPLETENESS AMENDMENT IDENTIFIED / REV11 REMAINS LAST FULLY TYPESET-QA'D CANDIDATE**

## Read first

1. `REV11_FINAL_ADVERSARIAL_REGRESSION_AUDIT_2026-08-15.md`
2. `typeset/rev11_literature_completeness_candidate.patch`
3. `PRB_REV11_MINOR_REVISION_QA_2026-08-15.md`
4. `REV10_MINOR_REREVIEW_RESPONSE_2026-08-15.md`
5. `typeset/rev10_to_rev11_minor_revision.patch`
6. `numerics/parameter_sensitivity_audit.py`
7. `PRB_REV10_REFEREE_REPAIR_QA_2026-08-15.md`
8. `REV9_SUPREMUM_REREVIEW_RESOLUTION_2026-08-15.md`
9. `numerics/supremum_active_support_audit.py`
10. `typeset/rev9_exposition_to_rev10_referee_repaired.patch`
11. `MANUSCRIPT_REV9_EXPOSITION_REVISED_2026-08-15.md`
12. `numerics/kane_8band_tightness.py`

The exact Rev11 source is reconstructed from the archived Rev9 source by applying the Rev9→Rev10 patch followed by the Rev10→Rev11 patch. Rev11 remains the last package whose TeX and PDF hashes, compile state, and all-page visual QA are recorded.

The new literature-completeness patch is a **candidate delta only**. Do not call the amended source Rev12 or submission-ready until it is reconstructed, compiled, hashed, and visually QA'd.

---

# Controlling theorem — unchanged and independently rechecked

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

The final regression audit independently re-derived and passed:

```text
pointwise Fermi inequality;
Kubo-Greenwood normalization and thermal-kernel conversion;
exact-shell projected-block capacity;
singular-value/rank conversion to active population;
active-population <= total-population step;
fixed-window thermodynamic uniform-capacity condition;
moving-window low-energy quantifiers;
clean-bulk complete-shell -> k-block ordinary-supremum specialization.
```

Eq. (29) itself is unchanged.

The intrinsic one-species corollary remains restricted to the case where `mu` lies in a gap and the cross-`mu` partition coincides with the valence/conduction manifolds.

---

# Rev10/Rev11 repairs retained

## Ordinary supremum

The finite-system theorem uses an ordinary exact-shell supremum. Eq. (49) remains an ordinary `k` supremum in the clean bulk validation, not an essential supremum.

## Complete shell to momentum blocks

In a finite periodic clean system,

```math
P_\epsilon v_xQ_{\epsilon,B}
=\bigoplus_{\mathbf k}
P_{\epsilon,\mathbf k}v_x(\mathbf k)Q_{\epsilon,\mathbf k,B}.
```

Because the homogeneous velocity operator conserves crystal momentum, the complete-shell operator norm is the maximum finite-`k` block norm and becomes the ordinary bulk supremum.

## Gamma-point selection

The chemical potential lies `11.477 meV` above the nominal Gamma6 edge. Gamma6 and Gamma8 are all below `mu` at `k=0`, so there is no selected cross-`mu` Gamma8→Gamma6 block exactly at Gamma. The selected set begins near

```text
|k| ~= 0.05535 nm^-1.
```

## Active-support numerical criterion

The exact theorem uses exact mathematical rank. The Table-II diagnostic counts a singular value as numerically nonzero above

```text
1e-6 m/s.
```

A reduced broad-window sweep from `1e-9` through `1e4 m/s` leaves the active-support fraction unchanged to printed precision. The central lower bound does not depend on this threshold.

---

# Controlling HgCdTe result

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

Production quadrature:

```text
160 radial Gauss-Legendre x 10 cos(theta) Gauss-Legendre x 16 uniform phi
```

with `1e-7 eV` degeneracy clustering. `200 x 12 x 20` is an additional support check.

The final regression audit found the Hamiltonian derivative/velocity construction, integration measure, cross-`mu` counting, projected-block SVD logic, and reported interpretation internally consistent.

The ordinary capacity supremum is a reproducible numerical global-optimization result rather than an interval-certified mathematical maximum. This is consistent with the manuscript's claim of a numerical HgCdTe validation. If a referee demands stronger certification, multi-seed replication or deterministic/interval bracketing is the next numerical check.

---

# Parameter-sensitivity diagnostic

A one-at-a-time `+/-5%` perturbation of

```text
EP, Delta, F, gamma1, gamma2, gamma3
```

on a common reduced `24 x 4 x 6` diagnostic quadrature gives

```text
baseline ratio   = 0.1226
perturbed range  = 0.1098 ... 0.1293
relative range   ~= -10.5% ... +5.5%
```

This is not an uncertainty propagation and does not replace the production `0.1175` value. It only supports the statement that the representative multiband result remains order `10^-1` under modest independent parameter perturbations.

---

# Final literature audit

## Onishi-Fu

Rev11 already cites Y. Onishi and L. Fu, Phys. Rev. X 14, 011052 (2024), and correctly distinguishes their generalized optical-weight/topology/quantum-geometry gap bound from the Experiment-12 thermal quasiparticle population inequality.

## Newly identified neighboring work

The final regression audit identified a closer omitted reference:

```text
D. Mao, J. F. Mendez-Valderrama, and D. Chowdhury,
Low-energy optical absorption in correlated insulators:
Projected sum rules and the role of quantum geometry,
Phys. Rev. B 112, 075116 (2025),
DOI 10.1103/xmz7-jgl6.
```

This work develops a projected low-energy inverse-frequency optical sum and discusses a finite-temperature weighted form related to many-body quantum geometry/QFI.

It is **not a direct collision** with Eq. (29): Experiment 12 instead uses direct cross-`mu` one-body transitions, the distinct Fermi kernel

```math
\hbar\omega/[e^{\hbar\omega/(2k_BT)}-1],
```

and a per-exact-shell projected velocity-capacity/support-rank construction to lower-bound equilibrium thermal quasiparticle population.

The overlap is close enough in low-energy projected/windowed optical-sum methodology that the reference should be cited and distinguished before submission.

Candidate amendment:

`typeset/rev11_literature_completeness_candidate.patch`

No central equation or numerical result changes.

---

# Rev11 production / QA identity

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

These hashes apply to Rev11 **before** the new literature candidate patch.

---

# Scope / novelty

No universal dark-current, generation-rate, `D*`, or finite-bandwidth-noise claim. Excitons/collective states, indirect transitions, interacting spectral functions, and unconstrained photonic enhancement remain outside scope.

```text
DIRECT PRIOR-ART COLLISION: NOT FOUND IN TARGETED SEARCH
NOVELTY: PLAUSIBLE
HISTORICAL PRIORITY: NOT ESTABLISHED
PRIORITY LANGUAGE: NOT AUTHORIZED
```

The realistic HgCdTe bound remains an order-`10^-1` validation rather than a tight detector-design limit. Near-edge windows are looser than the broad validation window. This is an editorial/significance limitation, not a failed inequality.

# ACTIVE NEXT ACTION

Reconstruct exact Rev11 TeX, apply `typeset/rev11_literature_completeness_candidate.patch`, compile with the same PRB workflow, verify bibliography count/citations/boxes/floats, compute new TeX/PDF hashes, and visually inspect every page. If that passes, record the amended production package and stop defensive rewriting absent a new concrete mathematical defect, numerical inconsistency, direct literature collision, or journal-specific requirement.
