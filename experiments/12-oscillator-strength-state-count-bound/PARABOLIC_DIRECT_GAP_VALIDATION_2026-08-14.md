# Experiment 12 — 3-D Parabolic Direct-Gap Validation

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Disposition:** **SECOND INDEPENDENT DISPERSIVE VALIDATION / EXACT EQUALITY FAMILY IDENTIFIED / MASS-ASYMMETRY TIGHTNESS FORMULA DERIVED**

## 1. Purpose

The Dirac validations show that the Experiment-12 theorem is nontrivial for relativistic/nonparabolic bands. A hostile reviewer could still argue that this is accidental to Dirac kinematics.

This step tests the theorem on the ordinary textbook 3-D direct-gap semiconductor with parabolic electron and hole bands.

---

## 2. Model

Take

```math
E_c(k)
=\frac{E_g}{2}+\frac{\hbar^2k^2}{2m_e},
```

```math
E_v(k)
=-\frac{E_g}{2}-\frac{\hbar^2k^2}{2m_h}.
```

Use vertical direct optical transitions `v,k -> c,k` for one polarization and assume the relevant interband velocity matrix element has constant magnitude

```math
|v_{cv}(k)|=v_0.
```

Each optically participating upper/lower state has only the corresponding vertical partner in this minimal model, so

```math
v_{*,B}^2=v_0^2
```

for a window containing the full direct transition continuum.

All spin/valley factors multiply the exact population and the bound equally and cancel from the tightness ratio.

---

## 3. Exact equality when `m_e=m_h`

If

```math
m_e=m_h=m,
```

then intrinsic neutrality puts

```math
\mu=0,
```

and the bands are mirror symmetric:

```math
E_c(k)-\mu
=\mu-E_v(k)
```

for **every** `k`.

Therefore every vertical transition saturates the pointwise Experiment-12 Fermi lemma,

```math
\frac{2[f_v(k)-f_c(k)]}
{e^{[E_c(k)-E_v(k)]/(2k_BT)}-1}
=f_c(k)+[1-f_v(k)].
```

The row/column velocity-strength bound also saturates because every state carries the same full selected strength `v_0^2`.

Hence

```math
\boxed{
(n_e+n_h)_{bound}
=(n_e+n_h)_{exact}
}
```

for equal parabolic masses at **all temperatures**, not only in the nondegenerate limit.

This is an exact dispersive equality family distinct from the original flat-manifold equality construction.

---

## 4. Nondegenerate unequal-mass limit

For

```math
E_g\gg k_BT,
```

the exact intrinsic carrier density is

```math
n_i
=\sqrt{N_cN_v}\,e^{-E_g/(2k_BT)}
```

with

```math
N_c\propto m_e^{3/2},
\qquad
N_v\propto m_h^{3/2}.
```

Thus

```math
n_e+n_h
\propto
2(m_em_h)^{3/4}e^{-E_g/(2k_BT)}.
```

The optical transition energy is

```math
E_{cv}(k)
=E_g+\frac{\hbar^2k^2}{2m_r},
```

where

```math
\frac1{m_r}=\frac1{m_e}+\frac1{m_h}.
```

Inserting the direct-transition spectrum into Experiment 12 gives a bound proportional to

```math
m_r^{3/2}e^{-E_g/(2k_BT)}.
```

Taking the ratio yields

```math
\boxed{
\frac{(n_e+n_h)_{bound}}
{(n_e+n_h)_{exact}}
=
\left[
\frac{4m_em_h}{(m_e+m_h)^2}
\right]^{3/4}
\le1.
}
```

AM-GM makes the maximum obvious:

```math
\boxed{m_e=m_h\quad\Rightarrow\quad\text{ratio}=1.}
```

Thus band-mass asymmetry is precisely the source of looseness in the classical parabolic model.

---

## 5. Connection to equality physics

The mass-ratio factor can be written

```math
\left[
\frac{2\sqrt{m_em_h}}{m_e+m_h}
\right]^{3/2}.
```

It measures how far the two dispersions are from being mirror images around the intrinsic chemical potential.

Experiment 12 therefore recovers, without inserting a detector-specific DOS figure of merit, the same qualitative design direction recognized in classic semiconductor-laser band-structure engineering:

```text
strong electron-hole asymmetry increases the carrier population required for an optical task;
mirror-symmetric low-energy bands are optimal.
```

That design intuition is established prior art. The new candidate contribution, if any, is the general inverse spectral-weight inequality rather than the statement that symmetric bands are favorable.

---

## 6. Finite-temperature 10-um / 300-K check

For

```math
E_g/(k_BT)=4.795922925,
```

exact Fermi-Dirac numerical integration gives:

```text
m_h/m_e    bound/exact    Boltzmann asymptote
0.1          0.437895        0.435969
0.2          0.645457        0.643496
0.5          0.916072        0.915452
1.0          1.000000        1.000000
2.0          0.916072        0.915452
5.0          0.645457        0.643496
10.0         0.437895        0.435969
20.0         0.278962        0.277964
```

Thus the simple nondegenerate formula is already accurate to roughly the percent level at the 10-um / 300-K target, while the exact theorem still saturates identically at equal masses.

Reproducible numerical check:

`numerics/parabolic_direct_gap_validation.py`

---

## 7. Scientific consequence

The validation substantially strengthens the interpretation of Experiment 12:

```text
flat resonant manifolds: exact equality construction;
parabolic mirror-symmetric bands: exact dispersive equality construction;
2-D massless Dirac: 50% of exact thermal population;
3-D massless Dirac: 66.7%;
3-D massive Dirac at 10 um / 300 K: 79.5%;
large-gap massive Dirac: approaches exactness.
```

The theorem is therefore neither tied to one DOS model nor generically extremely loose.

## Novelty status

This parabolic validation itself is **not** a novelty claim. The favorable role of light/symmetric electron-hole bands is old semiconductor-optics/laser physics.

Its role is to verify and physically interpret the more general thermal optical spectral-weight inequality.
