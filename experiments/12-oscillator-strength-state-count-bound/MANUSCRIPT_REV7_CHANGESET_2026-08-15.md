# Experiment 12 — MANUSCRIPT REV7 scientific changeset

**Date:** 2026-08-15  
**Base:** PRB Rev6  
**Disposition:** **MAJOR-REVISION RESPONSE / CENTRAL THEOREM UNCHANGED**

This file is the authoritative scientific changeset from Rev6 to the QA-passed PRB Rev7 production source whose SHA-256 is recorded in `PRB_REV7_RENDER_QA_2026-08-15.md`.

## Title

Rev7 title:

> Thermal quasiparticle population bound from direct interband spectral weight under finite optical-velocity capacity

The title now makes the optical-capacity conditioning visible rather than allowing the spectral-weight numerator to appear sufficient by itself.

## Abstract changes

Add explicitly:

```text
a nonzero macroscopic density floor requires uniform thermodynamic boundedness of v_B^cap;
the first-order 8x8 HgCdTe Kane Hamiltonian supplies v_B^cap <= sqrt(3/2) v_K;
measured HgCdTe Kane velocities place the capacity near 1.3e6 m/s;
the low-energy statement requires that the capacity remain uniformly bounded.
```

Retain all scope exclusions and existing Dirac/parabolic validation values.

## Introduction changes

Replace the overly broad implication that optical/thermal relations always require a chosen recombination model.

Add the two canonical equilibrium neighbors:

```text
van Roosbroeck-Shockley:
  optical absorption <-> radiative electron-hole recombination/emission via detailed balance;

Callen-Welton / fluctuation-dissipation:
  dissipative response <-> equilibrium fluctuations of the conjugate observable.
```

State the distinction:

```text
Experiment 12 does not infer a radiative event rate or fluctuation spectrum.
It bounds the one-body equilibrium quasiparticle population needed to support selected
cross-chemical-potential direct optical response under a finite per-shell optical capacity.
```

## Section II — exact-mu endpoint

After defining `E_v < mu < E_c`, add:

> For compact notation we assume that no selected positive-frequency transition has an endpoint exactly at `mu`; if such a state occurs, its contribution is defined by the continuous `mu -> mu +/- 0` limiting prescription.

This leaves all gapped applications unchanged and closes the formal gapless-spectrum endpoint issue.

## Section III — thermodynamic theorem hypothesis

After the finite-volume capacity definition, add a dedicated thermodynamic-limit subsection.

For a sequence `V_j -> infinity` at fixed useful window `B`, define

```math
\boxed{
\bar v_B^{cap}
=\limsup_{j\to\infty}v_{B,V_j}^{cap}<\infty.
}
```

State explicitly:

```text
the finite-volume inequality is exact without this assumption;
the nonzero macroscopic density-floor consequence requires it;
all thermodynamic-limit population-floor language therefore uses the uniform-capacity condition.
```

## Active support population interpretation

Retain the rank-based basis-invariant definition but add:

```text
n_B^act is an exact support-dimension construct;
rank is discontinuous when a singular value crosses zero;
it should not be described as a noise-robust experimentally inferred participation count;
the total-population corollary does not require that interpretation.
```

## Low-energy consequence

Replace any shorthand that can be read as `E_g -> 0 => n_th cannot decrease` with the precise conditional statement:

```text
low transition energy
+ finite nonvanishing integrated direct cross-mu spectral weight
+ uniformly bounded per-shell optical capacity
+ independent-quasiparticle direct-transition description
=> nonvanishing active thermal population floor.
```

## Parabolic equality model

Keep finite-window active-subspace saturation exactly as before.

For the full-spectrum total-population saturation, state explicitly that this is exact **within the stated ideal effective two-band optical model** with parabolic bands and constant one-to-one optical velocity matrix element. Do not imply that the unbounded model is a UV-complete real semiconductor Hamiltonian.

## New subsection — HgCdTe 8x8 Kane-model capacity

Add a realistic multiband narrow-gap validation using the first-order 8x8 Kane Hamiltonian used for bulk HgCdTe optical calculations.

Write

```math
H_K(\mathbf k)=\hbar v_K M(\mathbf k)+H_{edge}.
```

Then

```math
\hat v_x
=\frac{1}{\hbar}\frac{\partial H_K}{\partial k_x}
=v_K M_x.
```

In the published Kane basis, the two nontrivial weighted-star blocks of `M_x` have squared coupling sum

```math
\frac34+\frac14+\frac12=\frac32.
```

Therefore the nonzero eigenvalues are `+/-sqrt(3/2)` and

```math
\boxed{
\|\hat v_x\|_{op}=\sqrt{\frac32}\,v_K.
}
```

For every selected optical window, projector contraction gives

```math
\boxed{
v_B^{cap}\le\sqrt{\frac32}\,v_K.
}
```

This bound is independent of system size, `k`, `E_g`, and spin-orbit splitting in the first-order model, so it supplies the uniform thermodynamic hypothesis automatically.

With

```math
E_P=\frac{2m_0P^2}{\hbar^2},
\qquad
v_K^2=\frac{E_P}{3m_0},
```

also state

```math
\boxed{
v_B^{cap}\le\frac{P}{\hbar}
=\sqrt{\frac{E_P}{2m_0}}.}
```

Numerical scales:

```text
measured v_K = (1.07 +/- 0.05)e6 m/s
-> central v_B^cap <= 1.31e6 m/s;

E_P ~= 18.8 eV
-> v_K ~= 1.050e6 m/s
-> v_B^cap <= 1.286e6 m/s.
```

Caveat explicitly:

```text
the exact sqrt(3/2) coefficient belongs to the first-order 8x8 Kane Hamiltonian;
second-order 8x8 k.p models introduce finite k-dependent corrections;
for finite detector-relevant windows with finite coefficients the selected capacity remains finite,
but the exact first-order numerical ceiling is not claimed as a full-band material constant.
```

Cite Malcolm & Nicol (2015), Teppe et al. (2016), and Man & Pan (1991).

## Relation-to-established-theory section

Add a dedicated detailed-balance/FDT subsection explaining:

```text
van Roosbroeck-Shockley:
    target = radiative event-rate spectrum;

Experiment 12:
    target = equilibrium one-body thermal support population;

FDT:
    target = equilibrium fluctuations / dissipative response of conjugate observable;

Experiment 12:
    statewise Fermi optimization + finite optical-coupling capacity.
```

The theorem is not described as an FDT or detailed-balance identity.

## Scope section — measured conductivity

Add:

```text
Eq. (main theorem) cannot be applied indiscriminately to total measured sigma_1.
Direct experimental use requires either:
  sigma_1 ~= sigma_1^cross in the selected window,
or
  a microscopic/spectral decomposition isolating the direct cross-mu contribution.
```

List intraband, same-side interband, phonon-assisted, and excitonic response as possible contaminants.

## Appendix A — optical boundary

Change `90% single-pass absorptance` to

```text
90% internal single-pass absorptance of the optical power admitted into the absorber,
equivalently ideal antireflection or index-matched entrance coupling.
```

State explicitly that Fresnel entrance loss is not included.

Retain the original table values.

Add the realistic-capacity scale:

```text
v_B^cap <= 1.31e6 m/s
-> illustrative 10-um/300-K intrinsic electron-column bound ~= 5.33e11 cm^-2
```

under the same ideal internal-optical assumptions.

Do not claim that real bulk HgCdTe exactly realizes the ideal Appendix-A optical model.

## Bibliography additions

Add:

```text
W. van Roosbroeck and W. Shockley, Phys. Rev. 94, 1558 (1954).
H. B. Callen and T. A. Welton, Phys. Rev. 83, 34 (1951).
J. D. Malcolm and E. J. Nicol, Phys. Rev. B 92, 035118 (2015).
F. Teppe et al., Nat. Commun. 7, 12576 (2016).
P. Man and D. S. Pan, Phys. Rev. B 44, 8745 (1991).
```

Retain the existing 11 references.

## Claims explicitly NOT changed

```text
No universal dark-current bound.
No universal D* bound.
No universal thermal-generation-rate bound.
No universal finite-bandwidth-noise bound.
No extension to neutral excitons/collective states.
No extension to indirect phonon-assisted absorption.
No unconstrained external-absorptance theorem under arbitrary photonic enhancement.
No novelty or priority claim.
```

## Status after changes

Rev7 is a targeted response to a credible major-revision review. The central theorem remains mathematically unchanged. The major gain is that the optical-capacity resource is now demonstrated to be uniformly finite and numerically material-scale in a standard realistic multiband narrow-gap Hamiltonian rather than being left as a formal free parameter.