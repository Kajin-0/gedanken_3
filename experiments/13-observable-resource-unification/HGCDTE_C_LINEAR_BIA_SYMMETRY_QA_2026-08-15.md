# HgCdTe C-linear BIA — symmetry and basis-convention QA

**Date:** 2026-08-15  
**Scope:** implementation QA for the C_k-linear Gamma8 BIA stress test  
**Status:** **PASS / HAMILTONIAN AND VELOCITY SYMMETRIES VERIFIED / MATRIX CONVENTION CROSS-CHECKED / C-LINEAR ROBUSTNESS RESULT VALIDATED**

## 1. Purpose

The refined C-linear BIA stress test found that substantial same-k spin splitting changes the HgCdTe population-bound hierarchy by moving weight among support, Fermi-statistical, and capacity factors while leaving

```math
\mathcal S_a^{act}=1
```

for every active exact shell.

Before accepting that result, the added BIA term must be checked independently against the symmetry and basis conventions of the parent eight-band Kane implementation.

The QA script is

`numerics/hgcdte_bia_c_linear_symmetry_qa.py`.

The workflow is

`.github/workflows/hgcdte-bia-c-linear-symmetry-qa.yml`.

---

# 2. Controlling run

```text
GitHub Actions run: 31915454606
source commit:      0f646cc58d980fef84a0ee4628038c94f3c4d6a5
artifact ID:        9254778059
artifact digest:    6a00b7563970834396135564224e494a6c8bd689c30553f8f26165bca374fe17
```

---

# 3. Checks performed

The script constructs the spinful time-reversal matrix in the exact basis used by the parent Hamiltonian,

```text
Gamma6: |1/2,+1/2>, |1/2,-1/2>
Gamma8: |3/2,+3/2>, |3/2,+1/2>, |3/2,-1/2>, |3/2,-3/2>
Gamma7: |1/2,+1/2>, |1/2,-1/2>
```

and verifies:

```text
1. Theta^2 = -I;
2. Hermiticity of the added C_k term and full C-BIA Hamiltonian;
3. H_0(k) -> H_0(-k) under spinful time reversal;
4. H_C(k) -> H_C(-k) under spinful time reversal;
5. v_x(k) -> -v_x(-k) for the parent velocity;
6. v_x^C(k) -> -v_x^C(-k) including the BIA derivative;
7. the C-linear BIA Hamiltonian vanishes at Gamma;
8. the angular-momentum invariant form agrees with the explicit Gamma8 C1/C2 matrix convention.
```

No tolerance was loosened to obtain a pass.

---

# 4. Numerical QA output

```text
theta_squared_plus_I_error=0
hermiticity_error_eV=0
base_TR_error_eV=0
C_BIA_TR_error_eV=0
base_velocity_TRodd_error_mps=0
C_BIA_velocity_TRodd_error_mps=0
Gamma_C_BIA_norm_eV=0
invariant_vs_C1C2_matrix_error_eV=4.84869951806e-19
RESULT=PASS
```

Thus all exact symmetry checks vanish to machine representation, and the independently written invariant and explicit-matrix forms agree to approximately `5e-19 eV` at the tested generic k points.

---

# 5. Consequence for the refined stress result

The controlling refined hierarchy result is recorded in

`HGCDTE_C_LINEAR_BIA_STRESS_RESULT_2026-08-15.md`.

The symmetry QA removes the main implementation-level alternatives to its interpretation:

```text
not a non-Hermitian perturbation;
not a wrong spinful time-reversal phase convention;
not a T-breaking Hamiltonian;
not a velocity-derivative sign error;
not an artificial Gamma splitting;
not a mismatch between invariant and explicit Gamma8 C-term conventions.
```

Therefore the observed transition from

```text
BIA off: 20072 active dimension-2 exact-shell blocks
C-BIA on: 40292 active dimension-1 exact-shell blocks
```

with

```math
\mathcal S_a^{act}=1
```

for every active block is accepted as a real consequence of the implemented C-linear zincblende BIA perturbation within this model.

---

# 6. Scientific disposition

The C-linear result is now a **validated side result** rather than a tentative numerical observation.

It establishes, within the stated C-linear model, that:

```text
substantial same-k inversion-asymmetry splitting does not imply a within-exact-shell singular-concentration penalty;
the BIA correction instead enters through shell energies, support, Fermi weighting, and velocity-capacity redistribution.
```

The quantitative C-linear hierarchy shift remains approximately

```text
continuous capacity:      +0.14%
full bound/reference:     -1.57%
within-shell factor:       unchanged at 1
selected-support splitting: up to ~10.9 meV
```

These values are **not** promoted to the Rev. 7 submission manuscript by default because the quadratic zincblende BIA terms are not included.

---

# 7. Full-BIA gate

A full `B+/B-/C` or equivalent bulk-`B/C` implementation is permitted only if the primary literature fixes the complete homogeneous-bulk Hamiltonian in the present basis without guessing matrix elements or parameter mappings.

Before any full-BIA numerical result is accepted it must reproduce at least:

```text
Hermiticity;
spinful time-reversal symmetry;
T-odd velocity transformation;
zero BIA energy correction at Gamma;
C-only reduction to the already validated implementation;
consistent HgTe/CdTe alloy interpolation;
a continuous-capacity BIA-off baseline matching 1.01764e6 m/s.
```

If the mapping from published `B+`, `B-` parameters to the homogeneous bulk invariant cannot be established unambiguously, stop and record that obstruction rather than manufacture a full-BIA model.

---

# 8. Manuscript status

**No Rev. 8 trigger.**

Experiment 13 Rev. 7 remains the sole active submission manuscript. This QA strengthens the side evidence that its BIA caveat is conservative but does not require a manuscript change.
