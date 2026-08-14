# Candidate Screen — Effective-Mass Asymmetry, Optical JDOS, and Thermal Carrier Density

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Disposition:** RETAIN EXACT INEQUALITY / DO NOT OPEN AS EXPERIMENT 08 / PRACTICAL BAND-STRUCTURE CO-OPTIMIZATION ALREADY ESTABLISHED

## 1. Premise

For a direct-gap semiconductor, near-edge optical absorption depends on the electron-hole **reduced mass**, while equilibrium intrinsic carrier density depends on the product of the separate electron and hole DOS masses.

Question:

> At fixed bandgap and fixed optical joint-density-of-states coordinate, can electron-hole mass asymmetry ever reduce thermal carrier population?

## 2. Isotropic theorem

For isotropic parabolic bands,

```math
\mu=\frac{m_e m_h}{m_e+m_h}.
```

Let

```math
r=m_e/m_h.
```

Then

```math
m_e m_h
=\mu^2\frac{(1+r)^2}{r}.
```

Since

```math
\frac{(1+r)^2}{r}=r+\frac1r+2\ge4,
```

```math
\boxed{m_e m_h\ge4\mu^2}
```

with equality only for

```math
\boxed{m_e=m_h=2\mu.}
```

For nondegenerate 3-D statistics,

```math
n_i
=2\left(\frac{kT}{2\pi\hbar^2}\right)^{3/2}
(m_e m_h)^{3/4}
\exp[-E_g/(2kT)].
```

Therefore, at fixed `E_g` and `mu`,

```math
\boxed{
n_i\ge
2^{5/2}\left(\frac{\mu kT}{2\pi\hbar^2}\right)^{3/2}
\exp[-E_g/(2kT)].
}
```

Mass symmetry uniquely minimizes the thermal carrier population.

Define the asymmetry penalty

```math
\boxed{
\Pi(r)
=\left[\frac{(1+r)^2}{4r}\right]^{3/4}\ge1.
}
```

Then

```math
n_i=\Pi n_{i,min}.
```

For the simple InSb effective-mass values `m_e=0.0145m0`, `m_h=0.39m0`, the reduced model gives `Pi~4.41`; a hypothetical mass-symmetric material with the same `mu` and gap would have about 4.4x lower `n_i`.

This is only an illustrative effective-mass comparison, not a claim that such a band structure is physically realizable with all other parameters fixed.

## 3. Anisotropic tensor theorem

Let `M_e` and `M_h` be positive-definite 3-D mass tensors. Define the reduced-mass tensor by

```math
R^{-1}=M_e^{-1}+M_h^{-1}.
```

Set

```math
X=R^{1/2}M_e^{-1}R^{1/2}.
```

Then

```math
0<X<I,
```

and

```math
R^{1/2}M_h^{-1}R^{1/2}=I-X.
```

Hence

```math
\det M_e\det M_h
=\frac{(\det R)^2}{\det X\det(I-X)}.
```

If the eigenvalues of `X` are `x_j`, each obeys

```math
x_j(1-x_j)\le1/4.
```

Therefore

```math
\boxed{
\det M_e\det M_h\ge4^3(\det R)^2
}
```

with equality only for

```math
\boxed{M_e=M_h=2R.}
```

This result does not require aligned principal axes.

Since

```math
n_i\propto[\det M_e\det M_h]^{1/4},
```

mass-tensor symmetry gives the unique thermal-DOS lower envelope at fixed optical reduced-mass tensor.

## 4. Joint-DOS-normalized bound

For spin-degenerate 3-D parabolic bands, the direct-transition joint DOS at excess photon energy `epsilon=hbar omega-E_g` is

```math
g_J(\epsilon)
=\frac{1}{2\pi^2}
\left(\frac{2}{\hbar^2}\right)^{3/2}
\sqrt{\det R}\sqrt{\epsilon}.
```

Eliminating `det R` gives

```math
\boxed{
\frac{n_i}{g_J(\epsilon)}
\ge
\sqrt{2\pi}\,
\frac{(kT)^{3/2}}{\sqrt{\epsilon}}
\exp[-E_g/(2kT)].
}
```

Equality occurs only for `M_e=M_h=2R`.

If the relevant interband dipole/momentum matrix element and refractive factors are held fixed so that near-edge absorption is proportional to `g_J`, the same inequality becomes an absorption-normalized lower bound on intrinsic carrier density.

## 5. Detector consequences inside the reduced model

If independent kinetic coefficients are artificially held fixed:

```text
SRH depletion generation ~ n_i      -> asymmetry penalty ~ Pi
minority diffusion dark current ~ n_i^2 -> penalty ~ Pi^2
```

At fixed reduced mass, the dominant direct BTBT exponential coordinate is also unchanged in simple two-band/WKB models; direct tunneling theory uses the reduced band mass.

However equilibrium radiative generation is different. van Roosbroeck-Shockley detailed balance fixes equilibrium radiative generation from the absorptance/absorption spectrum. If absorption is held fixed while `n_i` changes, the radiative recombination coefficient must compensate so that

```math
B n_i^2
```

remains consistent with the same equilibrium photon field. Thus mass symmetrization does **not** lower the radiative floor at fixed absorptance.

## 6. Kane-model stress

The optical matrix element and effective masses are not generally independent material parameters.

In a strict symmetric two-band `k.p` model, the same interband coupling produces equal-and-opposite band curvatures, so

```math
m_e=m_h.
```

The model automatically saturates the inequality.

Real mass asymmetry arises from multiband/remote-band structure, heavy-hole physics, strain, etc. General `k.p` theory derives effective masses and optical momentum matrix elements from the same set of interband couplings.

Therefore the theorem defines an abstract lower envelope; it is not proof that arbitrary mass symmetrization at fixed optical matrix element is physically realizable.

## 7. Strong comparator / prior art

Kane's original InSb band theory already connects effective mass and absolute fundamental absorption through the same `k.p` coupling.

More importantly for infrared detectors, Singh and Muralidharan, J. Appl. Phys. 136, 055703 (2024), use 8-band `k.p` to compare same-bandgap type-II and M-superlattice absorbers while jointly calculating:

- effective masses / band structure;
- intrinsic carrier concentration;
- oscillator strength and optical absorption;
- SRH/radiative lifetimes;
- diffusion dark current.

They explicitly find same-gap structures with different optical and dark-current performance and explain trends through band structure, carrier concentration, overlap and effective masses.

Thus the practical idea of co-optimizing DOS, absorption and dark current through band engineering is already established in a much more realistic multiband setting.

## 8. Disposition

```text
scalar/tensor determinant inequality: RETAIN
mass-asymmetry penalty Pi: RETAIN AS TEACHING/ANALYSIS TOOL
radiative detailed-balance cancellation: RETAIN
new fundamental detector architecture/principle: NOT ESTABLISHED
Experiment 08 branch: DO NOT OPEN
paper drafting: DO NOT BEGIN
```

An adversarial reviewer could reasonably call the core theorem an AM-GM/determinant inequality applied to textbook effective-mass formulas, while the real multiband detector optimization is already established.

## 9. Next rule

Return to theory-only premise generation. Seek a premise whose first nontrivial consequence is not merely a re-expression of standard band engineering, detailed balance, or an elementary inequality.
