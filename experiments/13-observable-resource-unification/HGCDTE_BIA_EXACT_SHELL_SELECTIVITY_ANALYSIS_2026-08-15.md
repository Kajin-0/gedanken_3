# HgCdTe BIA stress test — exact-shell selectivity analysis

**Date:** 2026-08-15  
**Scope:** analytical/theoretical; spinful clean-bulk exact-shell decomposition  
**Status:** **NEW STRUCTURAL RESULT / BIA DOES NOT GENERICALLY CREATE A WITHIN-EXACT-SHELL SELECTIVITY PENALTY / NUMERICAL BIA TEST SHOULD TARGET CAPACITY AND WEIGHT REDISTRIBUTION**

## 1. Motivation

The Rev. 7 Physical Review Applied manuscript validates the shell-resolved population-bound decomposition in a second-order eight-band HgCdTe model that neglects explicit bulk inversion asymmetry (BIA). In that model, inversion plus spinful time reversal produces a fixed-k antiunitary `PT` with `(PT)^2=-1`. Each thermally relevant selected parent shell is a two-dimensional fixed-k doublet, and the PT-even velocity block has equal nonzero singular values. Consequently

```math
\mathcal S_a^{act}=1
```

to machine precision.

A hostile review correctly noted that real zincblende HgCdTe has BIA and asked how strongly the fourth, within-shell factor might change if BIA were included.

Before adding a detailed BIA Hamiltonian, however, the exact-shell definition itself must be followed. Breaking inversion generically removes the same-k spin degeneracy. This changes the dimension of the exact parent shell and therefore changes the correct singular-value question.

The key conclusion is:

> **Generic BIA spin splitting does not by itself create a within-exact-shell selectivity penalty. It usually makes the exact fixed-k parent shell one-dimensional, for which active selectivity is identically one. At a time-reversal-invariant momentum, a surviving Kramers doublet also has equal singular values for a T-odd velocity operator.**

Thus a realistic BIA calculation should primarily test how BIA redistributes shell capacities, occupations, support, and the Fermi factor—not assume that `1/S_a` must decrease below unity.

---

# 2. Exact-shell active selectivity

For one parent exact shell `a`, let the selected optical block be

```math
M_a,
```

with

```math
r_a=\operatorname{rank}M_a,
```

```math
\lambda_a=\|M_a\|_{op}^2,
```

```math
T_a=\operatorname{Tr}(M_aM_a^\dagger),
```

and

```math
r_{st,a}=T_a/\lambda_a.
```

The active-shell selectivity used in the exact dispersive decomposition is

```math
\boxed{
\mathcal S_a^{act}=\frac{r_a}{r_{st,a}}.
}
```

The corresponding capacity contribution is

```math
\frac{c_a}{\mathcal S_a^{act}},
\qquad
c_a=\lambda_a/u_{\mathcal B}^2.
```

---

# 3. Lemma 1 — one-dimensional active parent shells have S=1 identically

Suppose BIA removes the fixed-k degeneracy and the parent exact eigenspace is one-dimensional.

Then the selected block is either a row or a column,

```math
M_a\in\mathbb C^{1\times N}
```

or

```math
M_a\in\mathbb C^{N\times1}.
```

If the shell is optically active, `M_a != 0`, so

```math
r_a=1.
```

There is exactly one nonzero singular value `s_a`, hence

```math
T_a=s_a^2,
```

```math
\lambda_a=s_a^2,
```

and therefore

```math
r_{st,a}=1.
```

Thus

```math
\boxed{
\dim\mathcal H_a=1,\ M_a\ne0
\quad\Longrightarrow\quad
\mathcal S_a^{act}=1.
}
```

This conclusion is independent of the detailed BIA parameter values.

It follows purely from the exact-shell definition.

---

# 4. Generic BIA consequence in a zincblende bulk band

With time reversal but without inversion,

```math
E_n(\mathbf k)=E_{\bar n}(-\mathbf k),
```

but there is no generic requirement that

```math
E_n(\mathbf k)=E_{\bar n}(\mathbf k)
```

at a non-time-reversal-invariant momentum.

The purpose of bulk inversion asymmetry terms in eight-band zincblende models is precisely to reproduce this zero-field same-k spin splitting.

Therefore, away from symmetry-protected or accidental degeneracies, a BIA-inclusive fixed-k exact shell is generically one-dimensional.

For every such active shell, Lemma 1 gives

```math
\boxed{\mathcal S_a^{act}=1.}
```

So the removal of PT degeneracy does **not** generically drive the fourth factor below one. It trivializes the active singular spectrum to a single singular value.

---

# 5. Lemma 2 — a Kramers doublet at a TR-invariant momentum also has equal singular values for velocity

At a time-reversal-invariant momentum, spinful time reversal `\Theta` satisfies

```math
\Theta^2=-1,
```

so an exact shell can remain a Kramers doublet even without inversion.

Choose Kramers-adapted bases in parent and partner doublets such that

```math
\Theta=J K,
\qquad
J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
```

where `K` denotes complex conjugation.

For a matrix block `M` of an operator with time-reversal parity `eta`,

```math
J M^* J^{-1}=\eta M.
```

Velocity is T-odd,

```math
\Theta v_x\Theta^{-1}=-v_x,
```

so `eta=-1`. Solving the constraint gives

```math
M=\begin{pmatrix}
a&b\\
b^*&-a^*
\end{pmatrix}.
```

Hence

```math
MM^\dagger
=(|a|^2+|b|^2)I_2.
```

The two nonzero singular values are equal.

If the same parent Kramers doublet couples to several partner Kramers doublets, horizontal concatenation gives

```math
MM^\dagger
=\sum_j M_jM_j^\dagger
=\left(\sum_j s_j^2\right)I_2.
```

Therefore, provided the selected block is rank two,

```math
r_a=2,
\qquad
r_{st,a}=2,
```

and

```math
\boxed{
\mathcal S_a^{act}=1.
}
```

Thus the TRIM Kramers case also carries no within-shell penalty.

---

# 6. Combined result

For a spinful time-reversal-symmetric clean bulk with BIA, consider the fixed-k direct-sum blocks used to resolve the exact-shell optical theorem.

If every thermally relevant active parent block is either

```text
(a) nondegenerate at fixed k; or
(b) one Kramers doublet at a time-reversal-invariant k,
```

then

```math
\boxed{
\mathcal S_a^{act}=1
\quad\text{for every active shell }a.
}
```

This is a broader sufficient condition than the Rev. 7 PT-doublet argument.

The mechanism changes:

```text
BIA-neglecting model:
    fixed-k PT doublet -> two equal singular values -> S_a=1.

Generic BIA-split k:
    one-dimensional exact shell -> one singular value -> S_a=1.

TR-invariant k with BIA:
    T Kramers doublet + T-odd velocity -> two equal singular values -> S_a=1.
```

---

# 7. Where BIA can still produce S_a > 1

The result above is not universal for arbitrary crystal degeneracies.

A nontrivial within-shell penalty can still arise if a selected fixed-k parent exact shell contains a multidimensional degeneracy not reducible to one isolated Kramers pair, for example through

```text
crystalline little-group degeneracy;
accidental band degeneracy;
coincident multiple doublets at a high-symmetry point;
other symmetry-enforced multidimensional irreducible representations.
```

For such a block, neither one-dimensionality nor the single-doublet symplectic argument forces all nonzero singular values to be equal.

A BIA numerical audit should therefore search explicitly for these exceptional shell dimensions rather than assume that BIA generically produces `S_a>1`.

---

# 8. Consequence for the full population-tightness hierarchy

The Rev. 7 exact hierarchy is

```math
\frac{n_{bound}}{n_{ref}}
=
\frac{n_{\mathcal B}^{act}}{n_{ref}}
\eta_F
\sum_a w_a^{act}
\frac{c_a}{\mathcal S_a^{act}}.
```

If the sufficient condition above holds, then

```math
\mathcal S_a^{act}=1
```

throughout the thermally important active support and the spectral factor becomes

```math
\boxed{
\tau_{cap}^{act}
=\sum_a w_a^{act}c_a.
}
```

BIA can still change this quantity through

```text
1. spin-split endpoint energies -> different thermal weights w_a;
2. changed eigenvectors/velocity matrix elements -> different lambda_a;
3. changed global supremum u_B -> different c_a;
4. changed transition-window membership -> different active support;
5. changed endpoint Fermi asymmetry -> different eta_F;
6. changed selected-support fraction relative to n_ref.
```

These are the correct targets of a physical BIA stress test.

---

# 9. Implication for interpreting a future BIA calculation

A future numerical result such as

```text
within-shell factor = 0.999
```

would require careful scrutiny. In a truly exact-shell calculation with generic BIA-split nondegenerate parent states, the factor should be exactly one for each active rank-one shell.

A value below one could instead signal

```text
real multidimensional exact degeneracy;
numerical clustering of merely near-degenerate BIA-split states;
rank-threshold artifacts;
or a deliberate coarse-grained/quasi-degenerate shell definition rather than the theorem's exact-shell definition.
```

Therefore the BIA audit must record both exact/clustered shell dimension and energy splitting before interpreting singular-value selectivity.

---

# 10. Highest-value numerical test

The useful BIA calculation is now:

```text
1. add a physically sourced BIA Hamiltonian to the eight-band HgCdTe model;
2. recompute same-k spin splittings across the selected window;
3. classify exact/near-exact shell dimensions;
4. verify S_a=1 on generic rank-one shells and on isolated TRIM Kramers shells;
5. identify any exceptional multidimensional shells;
6. recompute global capacity u_B;
7. recompute c_a, thermal weights, eta_F, support coverage, and the full bound/reference ratio;
8. compare BIA-on against the Rev. 7 BIA-off baseline.
```

The main quantitative question is therefore

> **How much does BIA perturb the capacity/support/Fermi portions of the hierarchy?**

not

> **How far below one does the within-shell factor necessarily fall?**

---

# 11. Manuscript disposition

Do **not** create Rev. 8 from this analytical result alone.

Rev. 7 remains technically correct because it makes only the conservative statement that the exact PT-isotropy mechanism is a property of the BIA-neglecting validation and does not assert universal real-HgCdTe shell isotropy.

This new analysis suggests that the current caveat may actually be more conservative than necessary.

Only promote this result into the manuscript if a physically parameterized BIA calculation confirms the shell classification and produces a useful quantitative robustness statement.

---

# 12. Literature boundary

Primary eight-band BIA literature establishes that zincblende BIA produces zero-field spin splitting and provides the symmetry-allowed BIA terms. The exact-shell selectivity consequence above is derived here from the Experiment-13 decomposition and elementary time-reversal constraints; no novelty or priority language is authorized without a separate prior-art audit.
