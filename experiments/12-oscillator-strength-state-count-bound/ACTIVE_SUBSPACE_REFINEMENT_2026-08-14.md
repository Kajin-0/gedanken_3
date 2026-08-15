# Experiment 12 — Basis-invariant optically active thermal-population refinement

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** strengthens the existing windowed theorem; does not change its scope or add a dark-current/noise claim.

## 1. Reason for the refinement

`MANUSCRIPT_REV3_2026-08-14.md` bounds the **total** thermal excitation density by optical spectral weight in an arbitrary useful window `B`. That theorem is correct, but its parabolic equality statement is too broad: if `B` contains only part of the direct spectrum, thermally occupied states outside `B` remain in `n_e+n_h`, so the total-population inequality is generally strict.

The same operator formulation gives a sharper basis-invariant result: the optical window bounds the thermal population of the one-body subspaces that actually participate in transitions inside that window.

This both strengthens the theorem and makes finite-window equality statements precise.

---

## 2. Selected coupling blocks

Use the existing exact one-particle eigenspace projectors. For an upper energy shell `epsilon_c > mu`,

```math
A_{\epsilon_c,B}
=P_{\epsilon_c}\hat v_i Q^-_{\epsilon_c,B},
```

where `Q^-` projects onto all lower energy eigenspaces connected to `epsilon_c` by transition frequencies in `B`.

For a lower shell `epsilon_v < mu`,

```math
B_{\epsilon_v,B}
=Q^+_{\epsilon_v,B}\hat v_i P_{\epsilon_v}.
```

Define the basis-invariant shell ranks

```math
r^+_{\epsilon_c,B}
=\operatorname{rank}A_{\epsilon_c,B},
```

```math
r^-_{\epsilon_v,B}
=\operatorname{rank}B_{\epsilon_v,B}.
```

These ranks count the independent linear combinations inside each exactly degenerate energy eigenspace that carry nonzero selected optical coupling. They are invariant under unitary rotations within the eigenspace.

The existing shell velocity resource remains

```math
u_B^2
=\max\left[
\sup_{\epsilon_c>\mu}\|A_{\epsilon_c,B}\|_{op}^2,
\sup_{\epsilon_v<\mu}\|B_{\epsilon_v,B}\|_{op}^2
\right],
```

where the symbol is **Latin** `u_B`.

---

## 3. Optically active thermal population

Define

```math
\boxed{
n_{e,B}^{act}
=\frac1V\sum_{\epsilon_c>\mu}
f(\epsilon_c)\,r^+_{\epsilon_c,B}
}
```

and

```math
\boxed{
n_{h,B}^{act}
=\frac1V\sum_{\epsilon_v<\mu}
[1-f(\epsilon_v)]\,r^-_{\epsilon_v,B}.
}
```

Because each rank is at most the dimension of its parent eigenspace,

```math
n_{e,B}^{act}\le n_e,
\qquad
n_{h,B}^{act}\le n_h.
```

Thus these quantities count only thermally occupied one-body degrees of freedom that are optically connected through the chosen window.

---

## 4. Trace-rank inequality

The thermally weighted optical velocity strength can be regrouped shell by shell as

```math
\mathcal R_B(T)
=\frac1V\left[
\sum_{\epsilon_c>\mu} f(\epsilon_c)
\operatorname{Tr}(A_{\epsilon_c,B}A_{\epsilon_c,B}^{\dagger})
+
\sum_{\epsilon_v<\mu}[1-f(\epsilon_v)]
\operatorname{Tr}(B_{\epsilon_v,B}^{\dagger}B_{\epsilon_v,B})
\right].
```

For any finite-rank operator `X`,

```math
\operatorname{Tr}(XX^{\dagger})
=\sum_j s_j^2
\le
\|X\|_{op}^2\operatorname{rank}X,
```

where `s_j` are singular values.

Applying this to every selected shell gives

```math
\boxed{
\mathcal R_B(T)
\le
u_B^2
\left(n_{e,B}^{act}+n_{h,B}^{act}\right),
}
```

again with Latin `u_B`.

Combining with the existing exact Fermi/Kubo lower inequality,

```math
\mathcal R_B(T)
\ge
\frac{2}{\pi e^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
\,d\omega,
```

yields the sharpened theorem.

---

# THEOREM — windowed optically active thermal-population bound

```math
\boxed{
n_{e,B}^{act}+n_{h,B}^{act}
\ge
\frac{2}{\pi e^2u_B^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
\,d\omega.
}
```

Since

```math
n_e+n_h
\ge
n_{e,B}^{act}+n_{h,B}^{act},
```

the previous total-population theorem follows immediately as a corollary:

```math
\boxed{
n_e+n_h
\ge
n_{e,B}^{act}+n_{h,B}^{act}
\ge
\frac{2}{\pi e^2u_B^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
\,d\omega.
}
```

For an intrinsic neutral absorber `n_e=n_h=n_th`, the earlier bound on `n_th` remains valid by the leftmost inequality.

---

## 5. Finite-window equality structure

Consider the ideal mirror-symmetric parabolic direct-gap model with equal electron and hole masses and a constant one-to-one vertical optical velocity matrix element `v_0`.

For **any selected transition-energy window** `B`:

1. every selected transition is mirror symmetric about `mu`, so the pointwise Fermi lemma saturates;
2. every selected coupling block has all nonzero singular values equal to `v_0`, so

```math
\operatorname{Tr}(AA^{\dagger})
=v_0^2\operatorname{rank}A;
```

3. therefore the **active-subspace population theorem** saturates exactly at every temperature.

Hence

```math
\boxed{
(n_{e,B}^{act}+n_{h,B}^{act})_{bound}
=(n_{e,B}^{act}+n_{h,B}^{act})_{exact}
}
```

for arbitrary `B` in this ideal model.

The **total-population** theorem saturates only if `B` contains every thermally occupied direct-transition state in the ideal model; for the formal global direct spectrum this is true, whereas for a finite partial window it is generally strict.

This distinction corrects the overbroad equality wording in Rev3 without changing any underlying inequality.

---

## 6. Interpretation

The refined theorem is more specific than a generic carrier-density floor. It states that finite direct optical spectral weight in a chosen window requires a minimum equilibrium population of the **electronic degrees of freedom that actually carry that optical response**, subject to the finite per-shell optical-velocity resource.

It remains a one-body equilibrium statement. It does **not** imply a universal dark-current, generation-rate, terminal-noise, or `D*` floor.

Neutral excitons, phonon-assisted transitions, many-body spectral functions, and unconstrained photonic enhancement remain outside the theorem class exactly as before.

---

## 7. Manuscript consequence

The next manuscript revision should use the hierarchy

```math
\frac{2}{\pi e^2u_B^2}
\int_B K_T\sigma_1^{cross}d\omega
\le
n_{e,B}^{act}+n_{h,B}^{act}
\le
n_e+n_h.
```

The abstract and equality section should distinguish:

```text
finite-window active-population saturation: exact in the ideal equal-mass parabolic model;

total-population saturation: exact only when the selected window covers the full relevant direct-transition population.
```

No other Rev3 scientific claim needs to be expanded.