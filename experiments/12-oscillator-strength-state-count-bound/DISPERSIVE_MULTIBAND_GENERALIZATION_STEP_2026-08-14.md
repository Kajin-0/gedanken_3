# Experiment 12 — Dispersive Multiband Thermal–Optical Spectral-Weight Inequality

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Disposition:** **FLAT-MANIFOLD THEOREM GENERALIZED TO ARBITRARY NONINTERACTING DISPERSIVE MULTIBAND INTERBAND TRANSITIONS / STATE-REUSE LOOPHOLE CLOSED / NOVELTY NOT ESTABLISHED**

## 1. Why this step was necessary

The first Experiment-12 theorem used two exactly resonant flat manifolds. The obvious escape was that a dispersive semiconductor can reuse one conduction or valence state in optical transitions at multiple energies, so frequency-bin state counts need not be additive.

This step removes the flat-manifold and rank-count assumptions entirely.

The result uses only:

```text
single-particle eigenstates;
Fermi-Dirac equilibrium;
interband transitions across a chemical potential lying in a gap;
Kubo-Greenwood linear optical response;
a finite per-state interband velocity-strength ceiling.
```

---

## 2. General gapped single-particle spectrum

Let `v` label all lower/valence states with

```math
E_v<\mu,
```

and `c` label all upper/conduction states with

```math
E_c>\mu.
```

Define

```math
E_{cv}=E_c-E_v>0.
```

The thermal conduction-electron occupation and valence-hole occupation are

```math
p_c=f(E_c),
```

```math
h_v=1-f(E_v),
```

where

```math
f(E)=\frac{1}{e^{\beta(E-\mu)}+1}.
```

The absorptive Fermi occupation difference is

```math
D_{cv}=f(E_v)-f(E_c)=1-h_v-p_c.
```

No equality of conduction/valence degeneracies is assumed.

---

## 3. Exact pointwise Fermi inequality

Define

```math
a=e^{-\beta(E_c-\mu)},
\qquad
b=e^{-\beta(\mu-E_v)}.
```

Then

```math
ab=e^{-\beta E_{cv}}\equiv z.
```

Also

```math
p_c=\frac{a}{1+a},
\qquad
h_v=\frac{b}{1+b},
```

and

```math
D_{cv}
=\frac{1-z}{(1+a)(1+b)}.
```

Meanwhile

```math
p_c+h_v
=\frac{a+b+2z}{(1+a)(1+b)}.
```

At fixed `z`, AM-GM gives

```math
a+b\ge2\sqrt z.
```

Therefore

```math
\frac{D_{cv}}{p_c+h_v}
\le
\frac{1-z}{2\sqrt z+2z}
=
\frac{e^{\beta E_{cv}/2}-1}{2}.
```

Thus for every interband transition crossing the chemical potential,

```math
\boxed{
D_{cv}
\le
\frac{e^{E_{cv}/(2k_BT)}-1}{2}
(p_c+h_v).
}
```

Equality occurs only when

```math
E_c-\mu=\mu-E_v=E_{cv}/2.
```

This pointwise inequality is the key step that makes global state reuse harmless.

---

## 4. Divide by transition energy

Kubo optical spectral weight contains `D_cv/E_cv`, so define

```math
g_T(E)
=\frac{e^{E/(2k_BT)}-1}{E}.
```

For `E>0`,

```math
\boxed{g_T'(E)\ge0.}
```

Indeed, with `x=E/(2k_BT)`, the derivative numerator is

```math
e^x(x-1)+1\ge0.
```

Therefore, for every transition with

```math
0<E_{cv}\le E_\Omega,
```

```math
\boxed{
\frac{D_{cv}}{E_{cv}}
\le
\frac{e^{E_\Omega/(2k_BT)}-1}{2E_\Omega}
(p_c+h_v).
}
```

---

## 5. Optical velocity-strength resource

For one polarization `i`, let

```math
v_{cv}=\langle c|\hat v_i|v\rangle.
```

Define a conservative microscopic interband velocity-strength ceiling `v_*` such that

```math
\boxed{
\sum_v|v_{cv}|^2\le v_*^2
\quad\text{for every }c,
}
```

and

```math
\boxed{
\sum_c|v_{cv}|^2\le v_*^2
\quad\text{for every }v.
}
```

A sufficient condition is a finite physical/projected velocity-operator norm

```math
\|\hat v_i\|\le v_*.
```

For lattice/Wannier models, Experiment 10 supplied a further conditional ultraviolet bound through hopping resources.

The row/column formulation is preferable here because selecting only transitions below an energy cutoff cannot increase any squared row or column sum.

---

## 6. Partial interband Kubo spectral weight

Define the clean single-particle interband optical spectral weight contributed by transitions with energy at most `E_Omega`:

```math
W(E_\Omega)
\equiv
\int_0^{E_\Omega/\hbar}
\sigma_1^{inter}(\omega)d\omega.
```

In transition form,

```math
\boxed{
W(E_\Omega)
=
\frac{\pi e^2}{V}
\sum_{\substack{c,v\\E_{cv}\le E_\Omega}}
\frac{D_{cv}|v_{cv}|^2}{E_{cv}}.
}
```

Insert the pointwise Fermi bound:

```math
W(E_\Omega)
\le
\frac{\pi e^2}{V}
\frac{e^{E_\Omega/(2k_BT)}-1}{2E_\Omega}
\sum_{cv}^{E_{cv}\le E_\Omega}
(p_c+h_v)|v_{cv}|^2.
```

Split electron and hole terms:

```math
\sum_{cv}p_c|v_{cv}|^2
\le
v_*^2\sum_cp_c,
```

```math
\sum_{cv}h_v|v_{cv}|^2
\le
v_*^2\sum_vh_v.
```

Define total thermally excited electron and hole densities

```math
n_e=\frac1V\sum_cp_c,
\qquad
n_h=\frac1V\sum_vh_v.
```

Then

```math
\boxed{
W(E_\Omega)
\le
\frac{\pi e^2v_*^2}{2}
\frac{e^{E_\Omega/(2k_BT)}-1}{E_\Omega}
(n_e+n_h).
}
```

Rearranging gives the **general thermal–optical spectral-weight inequality**

```math
\boxed{
n_e+n_h
\ge
\frac{2E_\Omega}{\pi e^2v_*^2}
\frac{W(E_\Omega)}
{e^{E_\Omega/(2k_BT)}-1}.
}
```

This result does not require `n_e=n_h`.

---

## 7. Intrinsic charge-neutral semiconductor

For an intrinsic absorber with

```math
n_e=n_h\equiv n_{th},
```

the bound becomes

```math
\boxed{
n_{th}
\ge
\frac{E_\Omega}{\pi e^2v_*^2}
\frac{W(E_\Omega)}
{e^{E_\Omega/(2k_BT)}-1}.
}
```

This is exactly the flat-manifold formula with

```math
E_\gamma\to E_\Omega
```

when all optical weight sits at the cutoff energy and the electron/hole states are symmetrically placed around `mu`.

Thus the first Experiment-12 theorem was not an artifact of equal degeneracy or flat dispersion; it is the equality structure of a more general inequality.

---

## 8. Low-energy limit

For

```math
E_\Omega\ll k_BT,
```

```math
\frac{E_\Omega}{e^{E_\Omega/(2k_BT)}-1}
\to2k_BT.
```

Hence the intrinsic result becomes

```math
\boxed{
n_{th}
\ge
\frac{2k_BT}{\pi e^2v_*^2}
W(E_\Omega)
+O(E_\Omega).
}
```

For total electron-plus-hole population,

```math
\boxed{
n_e+n_h
\ge
\frac{4k_BT}{\pi e^2v_*^2}
W(E_\Omega)
+O(E_\Omega).
}
```

At fixed low-energy interband spectral weight, the thermal-population lower bound therefore remains finite as the optical energy tends toward zero.

---

## 9. What closed the state-reuse loophole

A conduction state may indeed couple optically to many valence states at different energies. But it cannot contribute unlimited total squared velocity strength:

```math
\sum_v|v_{cv}|^2\le v_*^2.
```

Every such transition is also weighted by a Fermi factor bounded in terms of the thermal occupation `p_c+h_v`.

Thus reusing a state across many optical frequencies spends the same finite row/column oscillator-strength budget rather than creating independent free oscillator strength.

No frequency-bin additivity assumption is required.

---

## 10. Relation to ordinary f-sum rules

The conventional full optical f-sum relates total integrated optical conductivity to the density of **all electrons** (or to kinetic-energy/effective-mass quantities in restricted models).

The present inequality is structurally different:

```text
it uses only low-energy interband spectral weight below E_Omega;
it bounds thermally excited conduction electrons and valence holes;
it contains an explicit finite-temperature Fermi/Pauli factor;
it contains a microscopic interband velocity-strength ceiling v_*.
```

It should not be advertised as a replacement for the f-sum rule.

---

## 11. Boundaries and loopholes still open

The theorem currently assumes:

```text
independent single-particle quasiparticles;
a chemical potential in a true gap separating v and c state sets;
clean Kubo-Greenwood transition energies;
direct electric-dipole/current coupling through the single-particle velocity operator.
```

Not yet covered:

```text
excitons and other many-body optical states;
collective/superradiant oscillator-strength redistribution;
phonon-assisted/indirect absorption;
strong disorder where valence/conduction quasiparticle labels fail;
spectral broadening that mixes high-energy transition tails into a low measured-frequency window;
photonic field/path enhancement when translating intrinsic W to external absorptance;
whether thermally occupied states are mobile/collectable enough to create detector dark noise.
```

The last item is especially important: the theorem is first a **thermal population versus intrinsic optical spectral-weight** theorem, not yet a universal dark-current or D* theorem.

---

## 12. Focused novelty screen after generalization

Searches were performed for combinations of

```text
interband optical conductivity bound;
thermal carrier density;
partial optical spectral weight;
Fermi-Dirac occupation;
oscillator strength;
carrier-density inequality.
```

The closest established adjacent results found were:

```text
Kubo-Greenwood finite-temperature optical conductivity;
full/restricted optical sum rules;
quantum-geometric/topological optical-conductivity bounds;
Dirac/graphene finite-temperature interband Pauli blocking;
classic alpha/G_th infrared detector material criteria.
```

No direct source was identified with the inequality

```math
n_e+n_h
\ge
\frac{2E_\Omega W(E_\Omega)}
{\pi e^2v_*^2[e^{E_\Omega/(2k_BT)}-1]}
```

or an equivalent finite-temperature low-energy interband spectral-weight bound on thermally excited carrier population.

This is only a focused search, not a priority claim.

```text
NOVELTY NOT ESTABLISHED.
```

## Next action

Attack the many-body loophole first.

Question:

> Can an excitonic or collective optical state carry large low-energy current spectral weight while the density of thermally free charge carriers stays parametrically below the single-particle inequality?

If yes, Experiment 12 must either be explicitly restricted to quasiparticle interband detectors or generalized to a many-body excitation/noise quantity. Do not proceed to manuscript drafting before this is resolved.
