# Experiment 13 — dispersive selectivity / capacity decomposition

**Date:** 2026-08-15  
**Scope:** exact energy-shell family; dispersive one-body bands  
**Status:** **DERIVED / CLEAN SHELL RECIPROCITY SURVIVES AS AN OCCUPATION-WEIGHTED DECOMPOSITION / NO ARTIFICIAL FLAT-MANIFOLD ASSUMPTION REQUIRED**

## 1. Purpose

`COHERENCE_SELECTIVITY_STATE_COUNT_DUALITY_2026-08-15.md` proved an exact reciprocal relation for one optical coupling block:

```math
\mathcal S\tau=1.
```

A serious unified theory cannot rely only on one flat degenerate manifold. Experiment 12 is already formulated as a sum over exact energy shells. This note derives the corresponding dispersive result.

The simple reciprocal product becomes an exact weighted decomposition. Two additional sources of looseness appear naturally:

1. a shell may not reach the **global** velocity capacity `u_B`;
2. the observable Fermi/Kubo lower step may not saturate the exact thermally weighted velocity strength.

No new assumption is introduced.

---

# 2. Abstract shell family

Index every endpoint energy shell entering the Experiment-12 thermally weighted velocity-strength sum by `a`.

For each shell define a selected optical block

```math
M_a,
```

its positive Gram operator

```math
G_a=M_a^\dagger M_a,
```

its parent-shell dimension

```math
d_a=\dim\mathcal H_a,
```

and its active rank

```math
r_a=rank(M_a).
```

Let

```math
\lambda_a=\|M_a\|_{op}^2,
```

```math
T_a=Tr(G_a)=\|M_a\|_F^2,
```

```math
r_{st,a}=T_a/\lambda_a.
```

The equilibrium occupation/hole weight of that exact energy shell is `p_a>=0`.

For upper shells, `p_a=f(epsilon_a)`; for lower shells, `p_a=1-f(epsilon_a)`.

The Experiment-12 global capacity is

```math
\boxed{
u_B^2=\sup_a\lambda_a.}
```

Define the normalized shell-capacity utilization

```math
\boxed{
c_a=\lambda_a/u_B^2,
\qquad 0\le c_a\le1.
}
```

---

# 3. Exact thermally weighted optical strength

The exact velocity-strength quantity is

```math
\boxed{
\mathcal R_B
=\frac1V\sum_a p_aT_a.
}
```

For total parent population associated with the selected endpoint shells,

```math
\boxed{
N_{tot}
=\sum_a p_ad_a.
}
```

For the optically active population,

```math
\boxed{
N_{act}
=\sum_a p_ar_a.
}
```

The corresponding density versions divide by `V`; volume cancels in every tightness ratio below.

---

# 4. Local coherent selectivity

For each shell, compare its top singular vector against a uniform incoherent excitation of the full parent shell.

As in the one-block theorem,

```math
\boxed{
\mathcal S_a^{tot}
=\frac{d_a}{r_{st,a}}.
}
```

On the optically active support only,

```math
\boxed{
\mathcal S_a^{act}
=\frac{r_a}{r_{st,a}}.
}
```

These are local shell properties and are basis invariant.

---

# 5. Global Experiment-12 capacity bound

The capacity-only lower estimate of population is

```math
N_{cap}
=\frac{V\mathcal R_B}{u_B^2}
=\sum_a p_a\frac{T_a}{u_B^2}.
```

Since

```math
T_a=\lambda_ar_{st,a}=u_B^2c_ar_{st,a},
```

```math
\boxed{
N_{cap}
=\sum_a p_ac_ar_{st,a}.
}
```

This identity exposes the exact contribution of every shell.

---

# 6. Total-population tightness: exact weighted inverse-selectivity law

Define normalized thermal parent-population weights

```math
\boxed{
w_a^{tot}
=\frac{p_ad_a}{\sum_b p_bd_b},
\qquad
\sum_a w_a^{tot}=1.
}
```

Then

```math
\frac{N_{cap}}{N_{tot}}
=\frac{\sum_a p_ac_ar_{st,a}}
{\sum_a p_ad_a}.
```

Because

```math
\frac{r_{st,a}}{d_a}
=\frac1{\mathcal S_a^{tot}},
```

we obtain

```math
\boxed{
\tau_{cap}^{tot}
\equiv\frac{N_{cap}}{N_{tot}}
=\sum_a
w_a^{tot}
\frac{c_a}{\mathcal S_a^{tot}}.
}
```

This is the exact dispersive generalization of the one-shell reciprocal theorem.

Interpretation:

```text
1 / S_a: singular-spectrum/coherence-selectivity penalty;
c_a:     shell failure to reach the global per-state capacity;
w_a:     actual equilibrium population weight of the shell.
```

The capacity theorem's total-population tightness is their thermal weighted mean.

---

# 7. Active-population tightness

Define

```math
\boxed{
w_a^{act}
=\frac{p_ar_a}{\sum_b p_br_b}.
}
```

Since

```math
r_{st,a}/r_a
=1/\mathcal S_a^{act},
```

one obtains

```math
\boxed{
\tau_{cap}^{act}
\equiv\frac{N_{cap}}{N_{act}}
=\sum_a
w_a^{act}
\frac{c_a}{\mathcal S_a^{act}}.
}
```

This is exactly the active-subspace analogue.

Exact kernel states disappear from `r_a`, so the active formulation removes the slack associated purely with optically dark combinations while retaining slack from unequal nonzero singular values and submaximal shell capacities.

---

# 8. Recover the one-shell theorem

For a single shell,

```math
w_1=1,
\qquad
c_1=1
```

because that shell itself defines the capacity.

Hence

```math
\tau_{cap}^{tot}
=1/\mathcal S_1^{tot},
```

and

```math
\boxed{
\mathcal S_1^{tot}\tau_{cap}^{tot}=1.
}
```

Likewise on the active support.

Thus the previous exact reciprocity is not a special algebraic accident. It is the local building block of the fully dispersive theorem.

---

# 9. Add the observable Fermi/Kubo step

Experiment 12 proves an observable lower functional

```math
\mathcal L_B
=\frac{2}{\pi e^2}
\int_B
\frac{\hbar\omega\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
d\omega
```

with

```math
0\le\mathcal L_B\le\mathcal R_B.
```

Define the global Fermi/Kubo efficiency

```math
\boxed{
\eta_F^{global}
=\mathcal L_B/\mathcal R_B,
\qquad 0\le\eta_F^{global}\le1.
}
```

The final observable Experiment-12 population estimate is

```math
N_{obs}
=V\mathcal L_B/u_B^2
=\eta_F^{global}N_{cap}.
```

Therefore

```math
\boxed{
\tau_{obs}^{tot}
=\eta_F^{global}
\sum_a
w_a^{tot}
\frac{c_a}{\mathcal S_a^{tot}},
}
```

and

```math
\boxed{
\tau_{obs}^{act}
=\eta_F^{global}
\sum_a
w_a^{act}
\frac{c_a}{\mathcal S_a^{act}}.
}
```

This decomposes the full theorem slack into three physically different pieces:

```text
thermal/Fermi asymmetry;
nonuniform shell capacity;
coherent singular-spectrum concentration.
```

---

# 10. Bounds and diagnostic consequences

Because `0<=c_a<=1` and `S_a>=1`,

```math
0\le\tau_{cap}\le1.
```

More usefully,

```math
\tau_{cap}^{tot}
\le
\sum_aw_a^{tot}\frac1{\mathcal S_a^{tot}}.
```

If every thermally important shell has coherent selectivity at least `S_min`, then

```math
\boxed{
\tau_{cap}^{tot}\le1/S_{min}.
}
```

Thus a material whose useful optical response is highly coherence-selective on **every thermally populated shell** cannot simultaneously make the worst-case total-state-count bound tight.

Conversely, if the Experiment-12 capacity bound is observed numerically to be nearly tight, then most thermally weighted optical strength must come from shells that both:

```text
approach the global capacity, c_a≈1;
and have low coherent selectivity, S_a≈1,
```

apart from independent Fermi/Kubo slack.

This is a falsifiable structural diagnostic, not merely notation.

---

# 11. Relation to realistic HgCdTe Experiment-12 result

The realistic HgCdTe calculation already reports three distinct global tightness ratios:

```text
bound / reference total population;
active / reference population;
bound / active population.
```

The present decomposition identifies what a future shell-resolved singular-spectrum audit would explain:

```text
bound / active
```

is controlled by the thermally weighted combination of

```text
Fermi-kernel asymmetry,
shell capacity utilization,
and inverse coherent selectivity of the active singular spectrum.
```

The current HgCdTe numerics did not save the full singular spectrum of every shell as a manuscript observable, so no new numerical claim should be made until that audit is run explicitly.

---

# 12. Why this is more useful than a global stable rank

One could concatenate all shell matrices into one large block and compute a global stable rank. That would mix states of different energies and obscure the exact Fermi occupations, recreating the basis/resource ambiguity Experiment 12 deliberately removed.

The shell decomposition preserves the physically correct equilibrium energy resolution:

```math
p_a=p(\epsilon_a)
```

is constant inside each exact eigenspace but not across different energies.

Thus the dispersive extension remains compatible with Experiment 12's basis-invariant resource definition.

---

# 13. Novelty boundary

The weighted-average algebra itself follows from established singular-value identities. Do not claim novelty for weighted stable ranks.

The candidate detector result is the **cross-branch interpretation**:

> shellwise coherent selectivity against incoherent internal excitation is the reciprocal singular-spectrum factor that controls how completely direct optical response can identify thermal state count; in dispersive bands, the full Experiment-12 bound is a thermal weighted average of inverse selectivity, reduced independently by shell-capacity nonuniformity and Fermi asymmetry.

No direct prior-art collision for this detector-specific statement has yet been located.

---

# 14. Next numerical test

Modify the realistic HgCdTe shell audit to save, for every thermally relevant selected block:

```text
lambda_max;
Frobenius norm squared;
rank;
stable rank;
c_a=lambda_max/u_B^2;
S_a^act=rank/stable_rank;
thermal weight p_a rank;
```

Then reconstruct

```math
\sum_a w_a^{act}c_a/S_a^{act}
```

and compare it against the independently computed exact velocity-strength / active-population ratio.

After that, multiply by the independently known Fermi/Kubo efficiency and verify closure to the final Experiment-12 bound/active ratio.

If this closes numerically in the 8-band HgCdTe model, the unified theorem will have a realistic-material validation rather than only an abstract shell proof.
