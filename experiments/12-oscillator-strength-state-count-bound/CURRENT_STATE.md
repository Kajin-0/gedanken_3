# Current State — Experiment 12: Thermal Population Cost of Direct Interband Optical Spectral Weight

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** **WINDOWED THERMAL–OPTICAL POPULATION INEQUALITY SURVIVES HOSTILE REVIEW / BASIS-INVARIANT RESOURCE FIXED / PARABOLIC EQUALITY FAMILY + DIRAC VALIDATIONS COMPLETE / REV3 MANUSCRIPT EXISTS / REV3 NOTATION ERRATUM REQUIRED / NOVELTY NOT ESTABLISHED**

## Read first

1. `MANUSCRIPT_REV3_2026-08-14.md`
2. `MANUSCRIPT_REV3_NOTATION_ERRATUM_2026-08-14.md`
3. `THEOREM_CORE_2026-08-14.md`
4. `BASIS_INVARIANT_VELOCITY_RESOURCE_CORRECTION_2026-08-14.md`
5. `MANUSCRIPT_REV1_ADVERSARIAL_REVIEW_2026-08-14.md`
6. `NOVELTY_AUDIT_2026-08-14.md`
7. `NOVELTY_AUDIT_ADDENDUM_LOW_CARRIER_OPTICS_2026-08-14.md`
8. `PROGRESS_LOG.md`

Branch:

```text
experiment-12-oscillator-strength-state-count-bound
```

---

# Controlling theorem

Consider equilibrium independent-quasiparticle one-body eigenstates with

```math
E_v<\mu<E_c,
\qquad
E_{cv}=E_c-E_v>0.
```

Define

```math
p_c=f(E_c),
\qquad
h_v=1-f(E_v),
\qquad
D_{cv}=f(E_v)-f(E_c).
```

The direct positive-frequency conductivity used by the theorem is the **cross-chemical-potential** contribution only:

```math
\sigma_1^{cross}(\omega)
=\frac{\pi e^2}{V}
\sum_{cv}
\frac{D_{cv}|v_{cv}|^2}{E_{cv}}
\delta\!\left(\omega-\frac{E_{cv}}{\hbar}\right).
```

The exact pointwise Fermi lemma is

```math
\boxed{
\frac{2D_{cv}}
{e^{E_{cv}/(2k_BT)}-1}
\le p_c+h_v.
}
```

Equality holds iff the transition endpoints are mirror symmetric about `mu`.

For any measurable positive-frequency window `B`, define the thermally weighted optical-velocity strength `R_B(T)` and the basis-invariant shell resource `u_B` by projecting the physical velocity operator only between exact degenerate energy eigenspaces whose transition energies lie in `B`.

Then

```math
\boxed{
\frac{2}{\pi e^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
\,d\omega
\le
\mathcal R_B(T)
\le
u_B^2(n_e+n_h),
}
```

where the resource symbol is **Latin** `u_B`.

Therefore

```math
\boxed{
n_e+n_h
\ge
\frac{2}{\pi e^2u_B^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
\,d\omega.
}
```

For an intrinsic neutral absorber, `n_e=n_h=n_th`,

```math
\boxed{
n_{th}
\ge
\frac{1}{\pi e^2u_B^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
\,d\omega.
}
```

A global all-frequency statement is used only if a finite global velocity resource exists. The windowed theorem is controlling.

---

# Low-energy consequence

The thermal kernel

```math
K_T(E)=\frac{E}{e^{E/(2k_BT)}-1}
```

satisfies

```math
K_T(E)=2k_BT-E/2+O(E^2/k_BT).
```

Thus fixed **integrated** low-energy cross-`mu` optical spectral weight cannot coexist with vanishing equilibrium thermal quasiparticle population at fixed `u_B`.

A peak-only response in a bandwidth that shrinks to zero is not constrained to a finite population floor because its integrated spectral weight can vanish.

---

# Equality and validation

## Parabolic equality family

For three-dimensional direct parabolic bands with constant one-to-one optical matrix element,

```math
E_c(k)=E_g/2+\hbar^2k^2/(2m_e),
```

```math
E_v(k)=-E_g/2-\hbar^2k^2/(2m_h),
```

the theorem is **exactly saturated at all temperatures** when

```math
m_e=m_h
```

and the intrinsic chemical potential is at midgap.

For unequal masses in the nondegenerate limit,

```math
\boxed{
\frac{n_{bound}}{n_{exact}}
=\left[
\frac{4m_em_h}{(m_e+m_h)^2}
\right]^{3/4}
\le1.
}
```

## Dirac validations

```text
2-D neutral massless Dirac / graphene: bound/exact = 1/2
3-D massless Dirac:                    bound/exact = 2/3
3-D massive Dirac, 10 um / 300 K:      bound/exact = 0.794684
```

These validations are reproduced by the branch numerical scripts.

---

# Scope boundary

Current valid class:

```text
independent-quasiparticle direct cross-mu charge absorbers.
```

The theorem survives dispersive multiband state reuse, unequal degeneracy, and static single-particle disorder when exact eigenstates are used.

It does **not** automatically cover:

```text
bound excitons / neutral collective optical states;
phonon-assisted or indirect absorption;
interaction-generated many-body spectral functions;
unconstrained passive photonic path enhancement.
```

Localized one-particle states do not break the population theorem but prevent automatic inference from population to DC dark current.

Do **not** claim a universal dark-current, generation-rate, `D*`, or finite-bandwidth-noise bound. The attempted universal `G_th >= n_th/tau_response` conversion was explicitly rejected by the depleted-photodiode counterexample.

---

# Manuscript state

Current manuscript:

`MANUSCRIPT_REV3_2026-08-14.md`

Rev0 received major revision. Rev1 reached pass-with-minor-revision after the basis-invariance correction and bandwidth clarification. Rev3 is the current compressed archival manuscript.

### Mandatory Rev3 erratum

Rev3 still contains four stale rendered `\nu_B` / `\nu_{\mathcal B}` tokens caused by a LaTeX escape regression. They occur in the abstract hierarchy, Eq. (21), Eq. (22), and concluding Eq. (35).

The only valid resource symbol is Latin

```math
u_{\mathcal B}.
```

No physics changes. Treat

```text
MANUSCRIPT_REV3_2026-08-14.md
+
MANUSCRIPT_REV3_NOTATION_ERRATUM_2026-08-14.md
```

as the controlling archival manuscript state until the next typeset/journal-facing revision mechanically incorporates the substitution.

---

# Prior-art / novelty disposition

Focused audits include:

```text
Kubo-Greenwood conductivity;
semiconductor phase-space filling;
ordinary/generalized f-sum rules;
restricted optical sums;
quantum-geometric optical sums;
finite-T QFI response kernels;
graphene finite-T optical sums;
classic IR alpha/G_th criteria;
Yablonovitch-Kane low-carrier laser band engineering.
```

No direct source has yet been identified stating the same inverse windowed inequality from surviving cross-`mu` spectral weight plus finite per-shell optical velocity resource to minimum equilibrium thermal electron-hole population.

```text
NOVELTY NOT ESTABLISHED.
MANUSCRIPT DRAFT IS SCIENTIFICALLY DEFENSIBLE ENOUGH FOR FURTHER EXTERNAL-STYLE REVIEW.
```

---

# Next action

Do not add new physics to rescue or inflate the paper.

Next work should be one of:

```text
1. mechanically fold the Rev3 notation erratum into the next rendered revision;
2. run another independent hostile manuscript review;
3. verify every bibliography entry and journal-fit claim;
4. prepare LaTeX/PDF only after the claim scope remains unchanged.
```
