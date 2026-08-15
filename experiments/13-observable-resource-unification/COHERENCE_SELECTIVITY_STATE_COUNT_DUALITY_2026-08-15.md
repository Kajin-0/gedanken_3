# Experiment 13 — coherence selectivity / state-count duality

**Date:** 2026-08-15  
**Scope:** exact finite-dimensional optical-shell theorem; analytical/theoretical only  
**Status:** **SECOND CROSS-BRANCH THEOREM DERIVED / EXACT AT THE CAPACITY STEP / FULL EXPERIMENT-12 EQUALITY REQUIRES FERMI-KERNEL SATURATION / NOVELTY NOT YET CERTIFIED**

## 1. Why this theorem matters

Experiment 09 uses concentration of optical response into a coherent bright superposition to reject an incoherent internal excitation.

Experiment 12 uses the largest singular value of an optical velocity block as a per-state capacity to infer a lower bound on how many thermally occupied states are required to carry a measured optical response.

These initially look like different uses of the same matrix algebra. They are in fact quantitatively dual.

For one selected optical coupling block, the same singular-value concentration that **improves coherent bright-state discrimination** makes a worst-case **state-count lower bound less tight**, by exactly the reciprocal factor.

The controlling invariant is the stable rank.

---

## 2. Optical coupling block

Let

```math
M:\mathcal H_-\to\mathcal H_+
```

be one selected optical coupling block, e.g.

```math
M=P_{\epsilon_+}\hat v_iQ^-_{\epsilon_+,\mathcal B}
```

or the corresponding lower-shell block used in Experiment 12.

Let its nonzero singular values be

```math
s_1\ge s_2\ge\cdots\ge s_r>0,
```

where

```math
r=rank(M).
```

Define

```math
G=M^\dagger M\succeq0,
```

so

```math
\lambda_{max}(G)=s_1^2=\|M\|_{op}^2,
```

```math
\operatorname{Tr}G
=\|M\|_F^2
=\sum_{a=1}^{r}s_a^2.
```

Define the stable rank

```math
\boxed{
r_{st}(M)
=\frac{\|M\|_F^2}{\|M\|_{op}^2}
=\frac{\operatorname{Tr}G}{\lambda_{max}(G)}.
}
```

Then

```math
1\le r_{st}\le r.
```

`r_st=r` iff all nonzero singular values are equal. `r_st=1` iff the coupling is rank one.

---

# 3. Coherent selectivity of the same coupling block

Let `|b_1>` be the top right-singular vector of `M`:

```math
G|b_1\rangle=s_1^2|b_1\rangle.
```

Use the natural coupling response functional

```math
q(\rho)=\operatorname{Tr}(G\rho).
```

For the maximally bright coherent signal

```math
\rho_B=|b_1\rangle\langle b_1|,
```

one has

```math
q_B=s_1^2.
```

Now let the incoherent dark excitation be maximally mixed over a `d`-dimensional microscopic parent subspace `H_D` that contains the support of `G`:

```math
\rho_D=\frac{P_D}{d}.
```

Then

```math
q_D
=\frac1d\operatorname{Tr}G.
```

Therefore the coherent-to-incoherent response ratio is

```math
\boxed{
\mathcal S_D
\equiv\frac{q_B}{q_D}
=\frac{d\lambda_{max}(G)}{\operatorname{Tr}G}
=\frac{d}{r_{st}(M)}.
}
```

This is the natural-coupling analogue of Experiment 09's bright-state rejection factor.

### Active-support version

If the incoherent comparison is restricted to the optically active support only, its dimension is `r`, so

```math
\boxed{
\mathcal S_{act}
=\frac{r}{r_{st}(M)}.
}
```

Thus singular-value concentration controls coherent selectivity:

```text
isotropic active coupling: r_st=r -> S_act=1;
rank-one coupling:          r_st=1 -> S_act=r.
```

---

# 4. State-count capacity step from Experiment 12

Now populate the same parent shell incoherently with a common equilibrium occupation weight `p`. Exact energy degeneracy makes this the natural Fermi occupation structure inside the shell.

The coupling-weighted optical strength carried by the shell is

```math
\mathcal R=p\operatorname{Tr}G.
```

The Experiment-12 spectral-capacity step uses

```math
\operatorname{Tr}G
\le
\lambda_{max}(G)\,d
```

for the total parent-space count, or the sharper

```math
\operatorname{Tr}G
\le
\lambda_{max}(G)\,r
```

for the optically active count.

## 4.1 Total parent-space population

The true shell population is

```math
N_{tot}=pd.
```

The population inferred from the spectral-capacity inequality alone is

```math
N_{cap}^{tot}
=\frac{\mathcal R}{\lambda_{max}(G)}
=p\frac{\operatorname{Tr}G}{\lambda_{max}(G)}
=pr_{st}(M).
```

Hence the capacity-step tightness is

```math
\boxed{
\tau_{tot}
\equiv\frac{N_{cap}^{tot}}{N_{tot}}
=\frac{r_{st}(M)}{d}.
}
```

## 4.2 Optically active population

The true optically active shell population is

```math
N_{act}=pr.
```

The same inferred population is `p r_st`, so

```math
\boxed{
\tau_{act}
\equiv\frac{N_{cap}^{act}}{N_{act}}
=\frac{r_{st}(M)}{r}.
}
```

This is exactly the singular-value slack in Experiment 12's trace-rank inequality.

---

# 5. Exact reciprocity theorem

Combining Secs. 3 and 4 gives

```math
\boxed{
\mathcal S_D\,\tau_{tot}=1,
}
```

and separately

```math
\boxed{
\mathcal S_{act}\,\tau_{act}=1.
}
```

Thus:

> For a fixed optical coupling block, coherent discrimination against a uniform incoherent ensemble and tightness of the corresponding spectral-capacity state-count bound are exact reciprocal quantities.

No fixed-trace assumption is required. Both quantities are functions of the same stable rank.

This is stronger and cleaner than the tentative fixed-oscillator-strength product considered before the exact Experiment-12 shell algebra was re-read.

---

# 6. Physical extremes

## 6.1 Isotropic full-rank coupling

If `d=r` and all singular values are equal,

```math
r_{st}=r=d.
```

Then

```math
\mathcal S_D=1,
\qquad
\tau_{tot}=1.
```

There is no coherent bright-state advantage: every microscopic direction couples equally strongly.

But the state-count inequality is exact because every active state uses the full allowed per-state capacity.

This is precisely the equality structure already identified in the equal-singular-value Experiment-12 models.

## 6.2 Rank-one bright coupling over `d` microscopic states

If the coupling has only one nonzero singular value,

```math
r_{st}=r=1.
```

Then against the full incoherent parent space,

```math
\boxed{\mathcal S_D=d,}
```

while

```math
\boxed{\tau_{tot}=1/d.}
```

The same concentration of oscillator strength that gives a factor-`d` coherence-selection advantage means the total-state-count theorem can certify only `1/d` of a uniformly occupied parent manifold from that optical response alone.

If one instead asks only for the optically active population, `r=1`, so

```math
\tau_{act}=1.
```

This explains why Experiment 12's active-subspace refinement removes slack associated with exactly dark microscopic combinations.

---

# 7. Direct connection to Experiment 09

Experiment 09's uniform bright-state construction has

```math
|B\rangle
=\frac1{\sqrt N}\sum_{j=1}^N e^{i\phi_j}|j\rangle,
```

with uniform incoherent dark state

```math
\rho_D=I_N/N.
```

For the ideal bright selector

```math
G=|B\rangle\langle B|,
```

```math
r_{st}=1,
\qquad
d=N.
```

Therefore the present theorem gives immediately

```math
\boxed{\mathcal S_D=N,}
```

which is the Experiment-09 conditional rejection factor.

The dual state-count statement is

```math
\boxed{\tau_{tot}=1/N.}
```

Thus the bright-state construction is the maximally selective / minimally total-state-identifying endpoint of the same coupling geometry.

Experiment 09's more general nonuniform result

```math
N_{eff}=1/\sum_jw_j^2
```

is a weighted extension of the uniform-parent theorem. The exact stable-rank reciprocity derived here should not be claimed for arbitrary nonuniform dark weights without redefining the population measure consistently.

---

# 8. Direct connection to Experiment 12

Experiment 12's active-subspace theorem uses, shell by shell,

```math
Tr(MM^\dagger)
\le
\|M\|_{op}^2 rank(M).
```

The fraction of the true active shell population captured by that capacity step is therefore exactly

```math
\boxed{\tau_{act}=r_{st}(M)/r.}
```

The previously derived equality condition — all nonzero singular values equal to the shell capacity — is exactly the condition

```math
r_{st}=r,
```

which gives

```math
\tau_{act}=1
```

and simultaneously

```math
\mathcal S_{act}=1.
```

Thus the equality family in Experiment 12 is the zero-coherence-selectivity endpoint of this duality.

Conversely, concentrating the same shell response into a smaller number of bright singular directions increases coherent selectivity but makes a capacity-only count of all participating microscopic directions less complete.

---

# 9. Include the Fermi/Kubo step: full Experiment-12 theorem

The Experiment-12 observable theorem contains an additional inequality before the capacity step. Define the exact thermally weighted velocity strength

```math
\mathcal R_B
```

and the observable thermal optical functional

```math
\mathcal L_B
=\frac{2}{\pi e^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
d\omega.
```

Experiment 12 proves

```math
0\le\mathcal L_B\le\mathcal R_B.
```

For one common shell block define

```math
\eta_F=\mathcal L_B/\mathcal R_B,
\qquad 0\le\eta_F\le1.
```

The **full observable** population-bound tightness is therefore

```math
\tau_{tot}^{obs}
=\eta_F\frac{r_{st}}d,
```

or on the active support

```math
\tau_{act}^{obs}
=\eta_F\frac{r_{st}}r.
```

Hence the exact reciprocity generalizes to

```math
\boxed{
\mathcal S_D\,\tau_{tot}^{obs}=\eta_F\le1,
}
```

and

```math
\boxed{
\mathcal S_{act}\,\tau_{act}^{obs}=\eta_F\le1.
}
```

When the Experiment-12 Fermi inequality saturates — e.g. the mirror-symmetric equal-occupation resonant-manifold family —

```math
\eta_F=1,
```

and the full observable theorem obeys exact reciprocal equality.

This cleanly separates two sources of slack:

```text
singular-spectrum anisotropy: r_st / dimension;
thermal/Fermi asymmetry:      eta_F.
```

---

# 10. Two-manifold electron + hole version

For two flat resonant manifolds linked by the same block `M`, let the conduction occupation be `p_e` and the valence-hole occupation be `p_h`.

Then

```math
\mathcal R
=(p_e+p_h)\operatorname{Tr}G,
```

while the total thermally excited endpoint count in equal-dimensional parent manifolds is

```math
N_{eh}^{tot}
=(p_e+p_h)d.
```

The common occupation prefactor cancels, so all reciprocity formulas above remain unchanged:

```math
\tau_{tot}=r_{st}/d.
```

Thus the duality is not an artifact of choosing electrons or holes alone.

---

# 11. New conceptual consequence

There are two fundamentally different meanings of "more selective optical coupling":

1. **measurement advantage** — concentrating coupling into a bright direction makes a coherent signal easier to distinguish from an incoherent parent ensemble;
2. **inverse-identification disadvantage** — the same concentration makes total microscopic state count harder to infer from optical strength because a small bright subspace can carry a large fraction of the response.

The stable rank quantifies both, reciprocally.

This is not the generic statement that `Tr(GX)` obeys eigenvalue bounds. It links two detector questions that were independently derived in Experiments 09 and 12:

```text
How well can coherence distinguish signal from internal dark generation?

versus

How much equilibrium state population is forced by a measured direct optical response?
```

---

# 12. Adversarial checks

## Check A — arbitrary rescaling of M

Under

```math
M\to cM,
```

both `Tr G` and `lambda_max` scale by `|c|^2`, so `r_st`, selectivity, and tightness are unchanged.

The theorem concerns **distribution** of coupling strength across singular channels, not its absolute scale.

## Check B — basis rotations

Singular values are invariant under unitary changes of basis within the parent manifolds. The theorem is therefore basis invariant.

## Check C — exact dark states

If `d>r`, exact kernel states increase full-parent coherent selectivity from `r/r_st` to `d/r_st` and reduce total-population tightness from `r_st/r` to `r_st/d`. The reciprocal product remains exactly one.

## Check D — nonuniform incoherent state

The simple `d/r_st` formula generally fails for nonuniform `rho_D`. Experiment 09's `N_eff` construction remains the correct weighted statement in its rank-one matched-population model. Do not overgeneralize the present uniform-shell theorem.

## Check E — dispersive nondegenerate states

The clean common occupation factor `p` belongs naturally to an exact energy shell / exactly degenerate manifold. Across different energies, Fermi weights differ and one must use an occupation-weighted effective rank. The current theorem should therefore be stated shellwise before any global aggregation.

---

# 13. Numerical stress check

Random complex coupling matrices of ranks `2,3,5,8` were generated and the algebraic identity

```math
(d/r_st)(r_st/d)=1
```

was checked to machine precision. This is only a regression check; the theorem is analytic.

---

# 14. Novelty boundary

The individual mathematical ingredients are established:

- singular values and stable/effective rank;
- bright/dark optical states and oscillator-strength concentration;
- coherent versus incoherent state discrimination;
- trace-rank and spectral-norm inequalities;
- oscillator-strength / state-count reasoning.

A focused literature search is required for the **combined reciprocal detector statement**. No novelty should be claimed merely for introducing `r_st`.

The candidate new result is specifically:

> the same optical coupling block gives a coherent-to-incoherent detector selectivity factor equal to the reciprocal of the singular-spectrum tightness of the corresponding optical state-count bound; after the Experiment-12 thermal/Fermi step, their product equals the independent Fermi-symmetry factor `eta_F`.

This cross-branch relation was not present in either Experiment 09 or Experiment 12 before Experiment 13.

---

# 15. Next action

Perform a focused primary-literature kill test for:

```text
stable/effective rank of optical coupling matrices;
coherent bright-state selectivity versus incoherent ensembles;
oscillator-strength participation ratios;
state-count bounds using spectral norm / Frobenius norm;
any published reciprocal relation between coherent selectivity and state-count/resource-bound tightness.
```

If no direct collision is found, test whether the theorem extends from exact shells to an occupation-weighted dispersive formulation without losing the clean physical interpretation.

This theorem is now strong enough that Experiment 13 should remain active even if the eventual manuscript preserves the three existing papers separately.
