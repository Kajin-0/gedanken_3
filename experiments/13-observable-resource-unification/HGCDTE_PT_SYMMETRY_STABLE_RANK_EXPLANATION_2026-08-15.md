# Experiment 13 — PT-symmetry explanation of HgCdTe active-shell stable rank

**Date:** 2026-08-15  
**Scope:** symmetry analysis of the second-order eight-band Kane validation model used in Experiments 12/13  
**Status:** **ANALYTIC EXPLANATION FOUND / `S_a^act=1` IS STRUCTURAL IN THE BIA-NEGLECTING MODEL / DO NOT GENERALIZE TO FULL ZINCBLENDE HgCdTe WITH BIA**

## 1. Numerical observation requiring explanation

The production stable-rank audit finds, for every thermally important selected active endpoint shell block,

```math
\mathcal S_a^{act}
=\frac{r_a}{r_{st,a}}
=1
```

to about `4e-14`.

Equivalently, every nonzero singular value of a selected active shell block is equal.

An exact result at this precision is unlikely to be accidental. It follows from the symmetry class of the Kane Hamiltonian used in the validation.

---

# 2. Symmetry of the validation Hamiltonian

The second-order eight-band bulk Kane Hamiltonian used in

```text
experiments/12-oscillator-strength-state-count-bound/numerics/
kane_8band_tightness.py
```

contains the standard `Gamma_6`, `Gamma_8`, and `Gamma_7` couplings through `P`, `F`, and the Luttinger parameters, but no explicit bulk-inversion-asymmetry/Dresselhaus term.

Within this model, there is an inversion operation `P` satisfying

```math
\mathcal P H(\mathbf k)\mathcal P^{-1}
=H(-\mathbf k),
```

and time reversal `T` satisfying

```math
\mathcal T H(\mathbf k)\mathcal T^{-1}
=H(-\mathbf k).
```

Therefore the antiunitary combined symmetry

```math
\Theta=\mathcal P\mathcal T
```

leaves each `k` fixed:

```math
\Theta H(\mathbf k)\Theta^{-1}
=H(\mathbf k).
```

For spinful states,

```math
\Theta^2=-1.
```

Hence every generic bulk eigenvalue of this BIA-neglecting model occurs as a twofold `Theta` doublet at the same `k`.

This is a symmetry of the **model**, not of the full zincblende crystal once bulk inversion asymmetry is retained.

---

# 3. Velocity is PT-even

The physical velocity operator is odd under inversion and odd under time reversal:

```math
\mathcal P\hat v_i\mathcal P^{-1}=-\hat v_i,
```

```math
\mathcal T\hat v_i\mathcal T^{-1}=-\hat v_i.
```

Therefore under the combined symmetry,

```math
\boxed{
\Theta\hat v_i\Theta^{-1}=+\hat v_i.
}
```

Thus the selected velocity block is an **even operator between `Theta` doublets**.

---

# 4. Matrix between two antiunitary doublets

Choose a `Theta`-adapted basis in one endpoint doublet,

```math
|u_2>=\Theta|u_1>,
```

and similarly for a partner doublet,

```math
|v_2>=\Theta|v_1>.
```

For an operator `O` satisfying

```math
\Theta O\Theta^{-1}=O,
```

the `2 x 2` matrix between the two doublets has quaternionic form

```math
\boxed{
M=
\begin{pmatrix}
a&b\\
-b^*&a^*
\end{pmatrix}
}
```

up to harmless basis/sign conventions inside the two doublets.

Then directly

```math
MM^\dagger
=
(|a|^2+|b|^2)I_2.
```

Therefore its two singular values are identical:

```math
s_1=s_2.
```

If the block is nonzero,

```math
rank(M)=2,
```

and

```math
r_{st}
=\frac{s_1^2+s_2^2}{s_1^2}
=2.
```

Thus

```math
\boxed{
\mathcal S^{act}
=rank/r_{st}
=1.
}
```

---

# 5. Multiple partner doublets

An endpoint shell can couple to more than one partner doublet inside the selected optical window.

Write the full selected block as a horizontal concatenation

```math
M=(M_1\;M_2\;\cdots\;M_q),
```

where every `M_j` is a `2 x 2` quaternionic block.

Then

```math
MM^\dagger
=\sum_jM_jM_j^\dagger
=\left[\sum_jc_j\right]I_2.
```

Hence the two nonzero singular values of the full endpoint block remain equal.

The same argument applies to the transpose/orientation used for a lower endpoint shell.

Therefore the shellwise result

```math
\boxed{\mathcal S_a^{act}=1}
```

is expected exactly for every generic twofold endpoint shell in this symmetry class, independent of the number of selected partner doublets.

---

# 6. Why the numerical audit sees machine-precision equality

The production audit groups exact model degeneracies before computing singular values. At generic quadrature `k` points the endpoint shells are twofold doublets.

The analytic symmetry above therefore predicts

```math
MM^\dagger=cI_2
```

before numerical diagonalization.

The observed range

```text
1 <= S_a^act <= 1 + 3.8e-14
```

is consistent with floating-point eigensolver/SVD noise around an exact model identity.

Thus the stable-rank result is not a coding coincidence.

---

# 7. Crucial physical caveat: zincblende HgCdTe has bulk inversion asymmetry

Real HgCdTe has the zincblende crystal structure and therefore does not possess true bulk inversion symmetry.

More complete multiband models can include bulk-inversion-asymmetry/Dresselhaus terms. Once such terms are retained,

```text
P is no longer a symmetry;
PT no longer provides the same fixed-k doublet structure;
the exact quaternionic block argument can fail;
S_a^act need not remain exactly one.
```

Therefore the unified manuscript must say

```text
"the active-shell blocks are isotropic within the BIA-neglecting second-order
 eight-band Kane validation model"
```

rather than

```text
"HgCdTe active-shell blocks are intrinsically isotropic."
```

This is a model-scope clarification, not a defect in the Experiment-12 theorem. The theorem itself does not assume inversion symmetry and would remain valid with a BIA-inclusive Hamiltonian after recomputing the selected shell capacity and ranks.

---

# 8. New physical interpretation of the HgCdTe decomposition

Within the current model, the `~0.573` capacity-step factor cannot come from unequal singular values **inside** a generic endpoint doublet because symmetry forbids that inequality.

It must come from variation of the common doublet singular value from shell to shell relative to the global maximum:

```math
c_a=\lambda_a/(v_B^{cap})^2<1.
```

This makes the production decomposition even sharper:

```text
within-shell anisotropy:
    symmetry-forbidden in the validation model;

between-shell capacity variation:
    ~0.573 thermal weighted factor;

Fermi/Kubo asymmetry:
    ~0.307;

final active tightness:
    ~0.1757.
```

---

# 9. Possible future robustness audit

A useful but nonessential future test is to add a physically reasonable BIA/Dresselhaus term to the bulk eight-band validation and ask:

```text
How far does S_a^act depart from 1?
How much does the shellwise selectivity contribution change the ~17.6% tightness?
Does the production ordinary supremum move materially?
```

This should be treated as a model-robustness audit, not as a requirement for the abstract population theorem.

Do not insert an ad hoc BIA parameter without a verified HgCdTe parameterization.

---

# 10. Manuscript consequence

Rev. 3 should replace generic wording such as

```text
"the HgCdTe active shell blocks are locally isotropic"
```

with the more precise statement:

> In the BIA-neglecting second-order eight-band Kane validation, the selected generic endpoint shells form fixed-k antiunitary doublets and the PT-even velocity blocks have equal nonzero singular values. The observed `S_a^act=1` is therefore symmetry enforced within this model. Bulk-inversion-asymmetry terms can lift this exact relation in real zincblende HgCdTe.

This both strengthens the numerical result and narrows its physical scope correctly.
