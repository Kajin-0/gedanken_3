# Experiment 12 — Microscopic Velocity-Strength Resource Corollary

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Disposition:** **ABSTRACT v_* RESOURCE GIVEN A DIRECT ONE-BODY SECOND-MOMENT DEFINITION / CONDITIONAL LATTICE-HOPPING VERSION DERIVED / NO UNIVERSAL NUMERICAL SPEED CLAIM**

## 1. Why `v_*` needs clarification

The global Experiment-12 theorem uses a row/column crossing-transition velocity-strength resource

```math
\sum_v|v_{cv}|^2\le v_*^2,
\qquad
\sum_c|v_{cv}|^2\le v_*^2.
```

It is sufficient, but unnecessarily strong, to assume a globally bounded velocity operator. In a continuum Hilbert space the full velocity operator need not possess a useful material-independent operator norm.

The theorem only needs a finite velocity **second moment for the states that participate in the optical/thermal window**.

---

## 2. Completeness gives a direct state-resolved resource

For any normalized upper single-particle eigenstate `|c>`, completeness gives

```math
\sum_n
|\langle c|\hat v_i|n\rangle|^2
=\langle c|\hat v_i^2|c\rangle.
```

The lower-state set `v` is only a subset of all states, hence

```math
\boxed{
\sum_v|v_{cv}|^2
\le
\langle c|\hat v_i^2|c\rangle.
}
```

Likewise, for any lower state `|v>`,

```math
\boxed{
\sum_c|v_{cv}|^2
\le
\langle v|\hat v_i^2|v\rangle.
}
```

Therefore one may define

```math
\boxed{
v_*^2
=
\max\left\{
\sup_{c\in\mathcal C_{rel}}\langle c|\hat v_i^2|c\rangle,
\sup_{v\in\mathcal V_{rel}}\langle v|\hat v_i^2|v\rangle
\right\},
}
```

where `C_rel,V_rel` contain the states whose optical transitions enter the chosen Experiment-12 spectral integral and whose thermal occupations are included in the counted excitation density.

This is a microscopic one-body resource, not a detector fit parameter.

---

## 3. Global theorem in second-moment form

With the above definition,

```math
\boxed{
n_e+n_h
\ge
\frac{2}{\pi e^2v_*^2}
\int_0^\infty
\frac{\hbar\omega\,\sigma_1^{inter}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
d\omega.
}
```

The physical content is now explicit:

```text
large low-energy direct-interband optical spectral weight
requires either
    a sufficiently large thermally excited quasiparticle population,
or
    sufficiently large microscopic velocity second moments in the participating states.
```

The theorem does not claim that `v_*` is chemistry-independent.

---

## 4. Conditional Wannier/tight-binding ultraviolet bound

For an orthonormal localized/Wannier Hamiltonian

```math
H(\mathbf k)=\sum_RH_Re^{i\mathbf k\cdot R},
```

Experiment 10 derived

```math
\|\hat v_i\|
\le
\frac1\hbar\sum_R|R_i|\|H_R\|
\equiv V_i^{hop}.
```

Therefore

```math
\langle n|\hat v_i^2|n\rangle
\le(V_i^{hop})^2
```

for every normalized state within that bounded lattice representation, so

```math
\boxed{v_*\le V_i^{hop}.}
```

Substituting the weaker hopping ceiling gives the conditional lattice-resource theorem

```math
\boxed{
n_e+n_h
\ge
\frac{2}{\pi e^2(V_i^{hop})^2}
\int_0^\infty
\frac{\hbar\omega\,\sigma_1^{inter}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
d\omega.
}
```

For an intrinsic neutral absorber, divide the right-hand side by two to bound `n_th`.

This version explicitly states the ultraviolet microscopic resource required to make the thermal population small at fixed optical spectral weight.

---

## 5. Why the ordinary TRK / effective-mass sum does not remove `v_*`

It is tempting to replace `v_*` by a universal bare-electron oscillator-strength sum.

That is not valid for a generic multiband solid. Effective-mass / oscillator-strength identities involve signed energy denominators and remote bands above and below the state of interest. Positive low-energy interband oscillator strength can be compensated by contributions of opposite sign elsewhere.

Experiment 10 already found this failure when attempting to derive a chemistry-independent upper Kane velocity from the multiband effective-mass identity.

Thus there is no justified positive universal numerical ceiling on the selected low-energy crossing-transition block from the ordinary TRK/effective-mass identity alone.

The Experiment-12 theorem is therefore correctly **resource-conditioned**.

---

## 6. Scientific role

This corollary addresses the hostile-review objection

```text
"v_* is arbitrary."
```

The answer is:

```text
v_* is the maximum relevant one-body velocity second moment;
it is directly computable from the microscopic Hamiltonian;
in a bounded Wannier model it is further constrained by hopping range/strength.
```

Do not claim a universal numerical `v_*` across all materials.

The novelty question remains the finite-temperature thermal-population versus low-energy interband spectral-weight inequality, not this standard microscopic resource bound by itself.
