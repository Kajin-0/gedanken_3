# Experiment 12 — Basis-Invariant Optical Velocity Resource Correction

**Date:** 2026-08-14  
**Disposition:** **BLOCKING REV0 RESOURCE AMBIGUITY RESOLVED / THEOREM CORE UNCHANGED IN STRUCTURE / PARABOLIC AND DIRAC TIGHTNESS RETAINED**

## 1. Problem

The pre-Rev1 theorem used

```math
v_{*,\mathcal B}^2
=\max\left[\sup_cR_c(\mathcal B),\sup_vC_v(\mathcal B)\right]
```

with

```math
R_c(\mathcal B)=\sum_{v:(c,v)\in\mathcal B}|v_{cv}|^2
```

and an analogous column strength.

For nondegenerate exact eigenstates this is unambiguous. Inside an exactly degenerate eigenspace, however, the individual eigenvectors may be unitarily rotated, redistributing row/column strengths. A theorem may be true in every chosen basis while the quoted resource is not uniquely basis invariant.

The correction should remove only this arbitrary degeneracy freedom; it should **not** allow coherent mixing between states of different energies, which are physically distinct equilibrium eigenstates with different Fermi occupations.

---

## 2. Spectral projectors

Work first in finite volume so the exact one-particle spectrum is discrete. Let

```math
P_\epsilon
```

be the projector onto the full eigenspace of energy `epsilon`.

For an upper energy `epsilon_c > mu`, define the lower-energy endpoint projector selected by optical window `B`:

```math
Q^-_{\epsilon_c,\mathcal B}
=\sum_{\substack{\epsilon_v<\mu\\(\epsilon_c-\epsilon_v)/\hbar\in\mathcal B}}
P_{\epsilon_v}.
```

Define the selected upper-shell optical block

```math
A_{\epsilon_c,\mathcal B}
=P_{\epsilon_c}\hat v_iQ^-_{\epsilon_c,\mathcal B}.
```

Similarly, for a lower energy `epsilon_v < mu`, define

```math
Q^+_{\epsilon_v,\mathcal B}
=\sum_{\substack{\epsilon_c>\mu\\(\epsilon_c-\epsilon_v)/\hbar\in\mathcal B}}
P_{\epsilon_c},
```

and

```math
B_{\epsilon_v,\mathcal B}
=Q^+_{\epsilon_v,\mathcal B}\hat v_iP_{\epsilon_v}.
```

---

## 3. Basis-invariant resource

Define

```math
\boxed{
u_{\mathcal B}^2
=\max\left[
\sup_{\epsilon_c>\mu}
\|A_{\epsilon_c,\mathcal B}\|_{op}^2,
\sup_{\epsilon_v<\mu}
\|B_{\epsilon_v,\mathcal B}\|_{op}^2
\right].
}
```

This quantity is invariant under arbitrary unitary rotations within every degenerate energy eigenspace.

For a normalized upper eigenstate `|c>` of energy `epsilon_c`, its selected row strength is

```math
R_c(\mathcal B)
=\langle c|
A_{\epsilon_c,\mathcal B}
A_{\epsilon_c,\mathcal B}^\dagger
|c\rangle
\le
u_{\mathcal B}^2.
```

Likewise every selected lower-state column strength obeys

```math
C_v(\mathcal B)\le u_{\mathcal B}^2.
```

Therefore the thermally weighted velocity-strength density still satisfies

```math
\boxed{
\mathcal R_{\mathcal B}
\le
u_{\mathcal B}^2(n_e+n_h).
}
```

Combining with the parameter-free Fermi/Kubo inequality yields the corrected invariant population theorem

```math
\boxed{
n_e+n_h
\ge
\frac{2}{\pi e^2u_{\mathcal B}^2}
\int_{\mathcal B}
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
d\omega.
}
```

For an intrinsic neutral absorber, divide the right side by two to bound `n_th`.

---

## 4. Why not use one spectral norm of the entire masked transition matrix?

One can define a frequency-masked matrix

```math
(M_\mathcal B)_{cv}
=1_\mathcal B(E_{cv}/\hbar)v_{cv}
```

and its spectral norm. That is also invariant under rotations within exact degeneracies.

However, a global spectral norm permits coherent superpositions of upper or lower states at **different energies**. Such superpositions are not basis ambiguities of the equilibrium Hamiltonian and can make the resource unnecessarily large.

The energy-shell definition `u_B` above maximizes only over physically arbitrary basis choices within truly degenerate eigenspaces, so it is the preferred sharp invariant resource.

---

## 5. Relation to the old row/column resource

If the relevant one-particle spectrum is nondegenerate, every energy projector is one-dimensional and

```math
\boxed{
u_{\mathcal B}^2
=
\max\left[
\sup_cR_c(\mathcal B),
\sup_vC_v(\mathcal B)
\right].
}
```

Thus all previous nondegenerate calculations are unchanged.

For exact degeneracies, the old basis-resolved maximum is bounded above by `u_B^2` in every basis and can equal it in the basis that diagonalizes the appropriate selected Gram operator.

---

## 6. Microscopic ceilings

Because spectral projectors are contractions,

```math
\|P_\epsilon\hat v_iQ\|_{op}
\le\|\hat v_i\|_{op}
```

whenever the full operator norm is finite. Therefore

```math
u_\mathcal B\le\|\hat v_i\|_{op}.
```

In a bounded orthonormal Wannier/tight-binding representation with

```math
\|\hat v_i\|_{op}
\le
\frac1\hbar\sum_R|R_i|\|H_R\|
\equiv V_i^{hop},
```

one has the conditional ultraviolet ceiling

```math
\boxed{u_\mathcal B\le V_i^{hop}.}
```

A continuum model with unbounded global velocity does not cause a problem: the theorem only requires the shell/window resource `u_B` to be finite over the selected optical/thermal energy region.

---

## 7. Equality examples survive

### Flat manifolds

For equal degenerate upper/lower manifolds whose interband block has every nonzero singular value equal to `v_0`,

```math
u_\mathcal B=v_0
```

and the original equality construction remains exact.

### Equal-mass parabolic direct bands

For the minimal one-to-one vertical-transition model with constant `|v_cv|=v_0`, each relevant energy-shell selected block has norm `v_0`. Thus

```math
u_\mathcal B=v_0,
```

and the all-temperature equal-mass saturation result is unchanged.

### Dirac validations

For the ideal Dirac models used in the numerical checks, the appropriate shell optical block is bounded by the Dirac velocity `v`; the reported ratios are unchanged.

---

## 8. Disposition

The Rev0 objection was legitimate but does not invalidate the theorem.

```text
OLD BASIS-RESOLVED RESOURCE:
    acceptable for nondegenerate numerical work;
    ambiguous as a general headline definition.

NEW u_B RESOURCE:
    basis invariant under exact degeneracies;
    sharp with respect to equilibrium energy shells;
    retains the existing equality/validation results.
```

All manuscript theorem statements should use `u_B` from this point onward.
