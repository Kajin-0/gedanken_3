# HgCdTe full homogeneous BIA robustness result

**Date:** 2026-08-15  
**Scope:** theoretical/numerical homogeneous eight-band BIA stress test  
**Status:** **HARD QA PASS / REFINED HIERARCHY PASS / MULTI-SEED + GRID + CLUSTER ROBUSTNESS PASS / REV. 8 SCIENTIFIC UPGRADE JUSTIFIED**

## 1. Question

The Rev. 7 production HgCdTe model omits explicit zincblende bulk inversion asymmetry (BIA). In that model every thermally important active exact parent shell is a fixed-k PT Kramers doublet and the within-shell selectivity factor is

```math
\mathcal S_a^{act}=1.
```

A hostile review identified the quantitative effect of real inversion breaking as the highest-value optional material-physics stress test.

The exact-shell analysis then showed that the naive expectation

```text
BIA -> unequal singular values -> S_a > 1
```

is not generally correct. Generic BIA removes the same-k doublet, making the exact parent shell one-dimensional, for which any nonzero active block has rank = stable rank = 1 and therefore `S_a=1` identically.

The purpose of the present calculation is to test this structure in a substantially more complete homogeneous zincblende eight-band model and quantify where the BIA correction actually enters the tightness hierarchy.

---

## 2. Homogeneous BIA model

The implementation adds the zero-field homogeneous-bulk terms of the standard 6c/8v/7v block formulation:

```text
B8v+ quadratic 6c-8v coupling;
B8v- quadratic 6c-8v coupling;
C_k linear 8v-8v coupling;
C_k linear 8v-7v coupling.
```

For a homogeneous scalar `B7v`, the antisymmetrized 6c-7v structure vanishes because the momenta commute with the constant material parameter.

Effective HgTe/CdTe endpoint parameters are linearly interpolated using the parametrization employed by Li et al., Phys. Rev. B 95, 035308 (2017):

```text
x_Cd   = 0.179727548444
B+     = -20.2588076698 eV A^2
B-     = +0.7061454583 eV A^2
C_k    = -0.06539794952 eV A
```

Important scope qualification: this is a homogeneous effective eight-band BIA model. It is not an atomistic/interface inversion-asymmetry calculation, and the effective B+ parametrization is inherited from the cited eight-band model class.

Implementation:

`numerics/hgcdte_bia_full_bulk.py`

---

## 3. Hard implementation QA

Before any hierarchy calculation was accepted, the BIA block was required to reproduce the phase/basis convention of the mature Experiment-12/13 Kane implementation and pass independent symmetry/derivative tests.

QA workflow:

`.github/workflows/hgcdte-bia-full-bulk-qa.yml`

Controlling QA:

```text
GitHub Actions run: 31915875544
source commit:      f065127d1b1fe9dab4600b8aea635aff8a96503c
artifact ID:        9254879019
artifact digest:    412fb869823c037dbedb13a798cfec3521a38ee56b80a72a20e7b3923aaedc32
```

Results:

```text
Theta^2 + I error                         = 0
parent Gamma6-Gamma8 P-block mismatch    = 6.21e-17
parent Gamma6-Gamma7 P-block mismatch    = 1.39e-17
Hermiticity error                         = 0
BIA time-reversal error                   = 0
full-H time-reversal error                = 0
full velocity T-odd error                 = 0
analytic vs finite-difference dH/dkx      = 3.58e-10 eV nm
BIA Hamiltonian at Gamma                  = 0
Gamma8 C reduction vs validated C stress  = 4.34e-19 eV
Gamma8 C derivative reduction             = 8.67e-19 eV nm
RESULT                                    = PASS
```

Thus the added BIA terms are in the same basis convention as the parent Hamiltonian and satisfy the intended exact symmetries to numerical representation.

---

## 4. Five-case decomposition

Refined workflow:

`.github/workflows/hgcdte-bia-full-bulk-refined.yml`

Controlling refined run:

```text
GitHub Actions run: 31915924737
source commit:      ce7c401d57d80912c90405659e665d1dbd9fda02
artifact ID:        9254902026
artifact digest:    a9b7b1ab85b3b8a36637fff87eaa3993c33a80842dd3f7f2e4b89711b85b96f0
```

The same `120 x 10 x 16` refined hierarchy pipeline and independent continuous ordinary-supremum capacity search were applied to:

```text
1. BIA off;
2. old Gamma8-diagonal C_k only;
3. complete eight-band C_k;
4. B+ + B- only;
5. full B+ + B- + C_k.
```

### BIA-off refined baseline

```text
mu                       = 0.1354615106 eV
n_ref                    = 1.005246445e17 cm^-3
n_active                 = 6.713386175e16 cm^-3
support fraction         = 0.667834859
eta_F                    = 0.307116485
continuous capacity      = 1.017639607e6 m/s
tau_cap                  = 0.572727662
tau_bound                = 0.175894107
full bound/reference     = 0.117468216
active exact blocks      = 20072 dimension-2
within-shell factor      = 1 exactly
```

The continuous baseline capacity independently reproduces the authoritative production value `1.01764e6 m/s`.

### Full homogeneous B+/B-/C_k result

```text
mu                       = 0.1355273416 eV
n_ref                    = 1.006941582e17 cm^-3
n_active                 = 6.805808982e16 cm^-3
support fraction         = 0.675889158
eta_F                    = 0.306255532
continuous capacity      = 1.022027377e6 m/s
tau_cap                  = 0.562863876
tau_bound                = 0.172380176
full bound/reference     = 0.116509892
active exact blocks      = 40452 dimension-1
within-shell factor      = 1 exactly
```

Selected-support same-k splitting reaches

```text
maximum  = 26.56 meV
weighted = 10.88 meV.
```

Thus the inversion-breaking perturbation is substantial on the selected support even though the within-shell factor does not move.

---

## 5. Relative full-BIA changes

Full B+/B-/C_k relative to BIA off:

```text
n_ref                    +0.169%
n_active                 +1.377%
support fraction         +1.206%
eta_F                    -0.280%
continuous capacity      +0.431%
tau_cap                  -1.722%
tau_bound                -1.998%
full bound/reference     -0.816%
mean inverse selectivity ~0 change
```

Therefore the realistic hierarchy-level BIA correction is not a new within-shell selectivity loss. It is redistributed among population support, Fermi weighting, and absolute capacity.

---

## 6. Which BIA terms matter

Relative to BIA off:

```text
Gamma8 C only:
full ratio -1.574%
capacity  +0.140%

complete eight-band C_k:
full ratio -1.613%
capacity  +0.154%

B+ + B- only:
full ratio -0.741%
capacity  +0.720%

full B+ + B- + C_k:
full ratio -0.816%
capacity  +0.431%
```

The missing Gamma8-Gamma7 `C_k` channel changes the older Gamma8-only C stress only weakly. The quadratic-B and C contributions are not simply additive in the final ratio; their changes partly cancel after the chemical potential, support, Fermi factor, and global capacity are recomputed self-consistently.

---

## 7. Exact-shell result survives the full homogeneous model

The most important structural observation is unchanged:

```text
BIA off:
20072 active dimension-2 PT-doublet parent blocks;
S_a = 1 for every block.

full homogeneous BIA:
40452 active dimension-1 parent blocks;
S_a = 1 for every block.
```

For the BIA-split case, no symmetry argument about equal doublet singular values is required. A nonzero active block with a one-dimensional parent has one nonzero singular value, so

```math
rank(M_a)=r_st,a=1
```

and therefore

```math
\boxed{\mathcal S_a^{act}=1.}
```

The BIA perturbation changes the mechanism for unity, not the value of the within-shell factor.

---

## 8. Robustness audit

Workflow:

`.github/workflows/hgcdte-bia-full-bulk-robustness.yml`

Final aligned run:

```text
GitHub Actions run: 31916168447
source commit:      f6cd79f05024acf79416000d9612f8a428eb7959
artifact ID:        9254954786
artifact digest:    2e80e62e7b8c61e68cc0e9cde04ffc0e5db035924f0d67e4c14beb6e92c5dc3a
```

### Continuous-capacity multi-seed stability

At the controlling `120 x 10 x 16` full-BIA chemical potential,

```text
seed 20260819: 1.02202737693e6 m/s
seed 20260829: 1.02202736245e6 m/s
seed 20260839: 1.02202737616e6 m/s
seed 20260849: 1.02202737592e6 m/s
```

fractional spread:

```text
1.42e-8.
```

### Independent grid behavior

The full-BIA change in the full bound/reference ratio remains approximately one percent or smaller across the independent audit grids:

```text
60 x 6 x 8:    about -0.8%
80 x 8 x 12:   about -0.9%
100 x 10 x 12: about -0.9%
120 x 10 x 16: -0.816%   [controlling refined result]
```

### Exact-shell cluster tolerance

For the full-BIA model, sweeping the degeneracy-clustering tolerance through

```text
1e-9, 1e-8, 1e-7, 1e-6, 1e-5 eV
```

gives in every case

```text
all active blocks dimension 1;
selectivity_min = 1;
selectivity_max = 1;
nonunit-selectivity population fraction = 0.
```

Thus the one-dimensional shell result is not a numerical clustering artifact.

---

## 9. Scientific conclusion

The BIA robustness question is now substantially closed within the homogeneous eight-band model class.

The original worry was that realistic zincblende inversion asymmetry could destroy the observed `S_a=1` shell result and therefore open an unquantified fourth source of theorem looseness.

The calculation shows the opposite mechanism:

```text
BIA removes the PT doublet at generic fixed k
-> active exact parent shells become nondegenerate
-> each active block has one singular value
-> S_a = 1 remains exact.
```

At the same time, physically non-negligible splitting up to ~26.6 meV changes the other hierarchy factors only enough to shift the final broad-window bound/reference ratio by about `0.82%` in the refined full model.

This is a stronger material-robustness result than the Rev. 7 BIA caveat.

---

## 10. Limitations

Do not overgeneralize the result.

Not included:

```text
interface-specific inversion asymmetry;
atomistic corrections beyond the homogeneous eight-band model;
strain-induced symmetry lowering beyond the stated bulk model;
exceptional multidimensional crystalline/accidental exact degeneracies;
uncertainty propagation over the published effective BIA parameters.
```

The effective `B+` parameterization is inherited from the cited HgTe/CdTe eight-band model and should not be presented as an ab-initio determination for the present alloy.

The exact population theorem itself remains independent of this material model.

---

## 11. Publication disposition

Unlike the earlier Gamma8-only C stress test, the full homogeneous result is sufficiently complete and robust to justify a **small Rev. 8 scientific manuscript upgrade**.

The appropriate use is narrow:

```text
replace the old open-ended BIA caveat;
report that full homogeneous BIA splits the active shells but leaves S_a=1;
report the ~0.43% capacity change and ~0.82% full-ratio change;
state the homogeneous-model limitations;
do not add a new figure unless layout requires it.
```

No central theorem, production baseline number, or readout result changes.
