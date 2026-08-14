# Experiment 10 — Exact Auger Kinematic Closure in the Symmetric Massive-Dirac Model

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Disposition:** **EXACT TOY-MODEL NO-GO DERIVED / HIGH-v AND AUGER-SYMMETRY LEVERS SEPARATED / BROAD NOVELTY NOT ESTABLISHED**

## 1. Question for this step

The preceding Experiment-10 results established that, for an ideal finite-gap 3-D massive-Dirac absorber with matched useful absorptance,

```math
\Sigma_e=n_ed\propto v^{-2},
```

while ideal ballistic crossing time is independent of `v` and generic low-energy sum rules do not provide a material-independent upper bound on `v`.

The next unavoidable intrinsic mechanism is Auger recombination/generation.

This step asks only:

> In the same exact particle-hole-symmetric massive-Dirac two-band model, is the ordinary phononless Coulomb Auger process kinematically allowed at all under exact energy and crystal-momentum conservation?

Do not insert an empirical Auger coefficient. Do not calculate a Coulomb rate before establishing whether the delta-function support exists.

---

## 2. Model

Use the same isotropic dispersion

```math
\varepsilon(k)
=\sqrt{\Delta^2+(\hbar vk)^2},
\qquad
\Delta=E_g/2>0.
```

Conduction quasiparticles and holes have the same positive excitation energy `varepsilon(k)`.

Assumptions for this exact closure step:

```text
one symmetric electron-hole Dirac pair;
normal crystal-momentum conservation (no Umklapp);
exact quasiparticle energies (zero spectral linewidth);
no phonon or impurity momentum assistance;
no additional heavy-hole or remote band participating in the event;
no particle-hole asymmetric scalar term;
no many-body spectral broadening/renormalization.
```

These assumptions are deliberately stronger than real bulk HgCdTe. The result is a clean kinematic reference point, not a claim that bulk HgCdTe has zero Auger recombination.

---

## 3. Write Auger as the inverse impact-ionization problem

The ordinary electron-electron-hole Auger channel is most cleanly written through its time reverse.

Impact ionization would require one conduction quasiparticle to produce two conduction quasiparticles plus one hole:

```text
e_0 -> e_1 + e_2 + h_3.
```

Define the hole quasiparticle momentum so that normal crystal-momentum conservation can be written

```math
\mathbf k_0
=\mathbf k_1+\mathbf k_2+\mathbf k_3.
```

If another hole-momentum convention is used, replace `k_3` by `-k_h`; because `varepsilon(k)` is even, the proof is unchanged.

Energy conservation would require

```math
\varepsilon(k_0)
=\varepsilon(k_1)+\varepsilon(k_2)+\varepsilon(k_3).
```

If this inverse process has no support, the corresponding phononless Auger recombination channel has no support either.

---

## 4. Strict subadditivity of the massive-Dirac energy

For arbitrary vectors `p,q`, define

```math
\varepsilon(\mathbf p)
=\sqrt{\Delta^2+(\hbar v)^2|\mathbf p|^2}.
```

Then

```math
[\varepsilon(\mathbf p)+\varepsilon(\mathbf q)]^2
-\varepsilon(\mathbf p+\mathbf q)^2
```

is

```math
\Delta^2
+2\left[
\varepsilon(\mathbf p)\varepsilon(\mathbf q)
-(\hbar v)^2\mathbf p\cdot\mathbf q
\right].
```

Since

```math
\varepsilon(\mathbf p)\varepsilon(\mathbf q)
>(\hbar v)^2|\mathbf p||\mathbf q|
\ge(\hbar v)^2\mathbf p\cdot\mathbf q
```

for every finite `Delta>0`,

```math
\boxed{
\varepsilon(\mathbf p+\mathbf q)
<\varepsilon(\mathbf p)+\varepsilon(\mathbf q).
}
```

The inequality is strict for every finite-gap massive-Dirac dispersion.

Apply it twice:

```math
\varepsilon(\mathbf k_1+\mathbf k_2+\mathbf k_3)
<
\varepsilon(\mathbf k_1)+
\varepsilon(\mathbf k_2)+
\varepsilon(\mathbf k_3).
```

Using momentum conservation gives

```math
\boxed{
\varepsilon(k_0)
<\varepsilon(k_1)+\varepsilon(k_2)+\varepsilon(k_3).
}
```

This contradicts the required Auger/impact-ionization energy equality.

Therefore

```math
\boxed{
\text{ordinary normal-momentum phononless }e\!e\!h
\text{ Auger/impact ionization has empty kinematic support.}
}
```

By particle-hole symmetry, the mirror hole-hole-electron channel is closed as well.

The result does not depend on the Coulomb matrix element because the energy-momentum delta functions already have no simultaneous support.

---

## 5. Equivalent convex minimization proof and exact mismatch

For fixed total momentum

```math
\mathbf K=\mathbf k_1+\mathbf k_2+\mathbf k_3,
```

the final three-quasiparticle energy is

```math
E_3
=\sum_{j=1}^3\varepsilon(k_j).
```

The function `varepsilon(k)` is strictly convex as a function of vector momentum for `Delta>0`. Jensen's inequality therefore gives

```math
E_3
\ge
3\varepsilon(K/3),
```

with equality only when

```math
\mathbf k_1=\mathbf k_2=\mathbf k_3=\mathbf K/3.
```

The smallest possible energy deficit for a nominal one-to-three process at total momentum `K` is therefore

```math
\boxed{
\Delta_A(K)
=3\varepsilon(K/3)-\varepsilon(K)>0.
}
```

Let the initial hot-quasiparticle energy be

```math
E=\varepsilon(K).
```

Since

```math
(\hbar vK)^2=E^2-\Delta^2,
```

we get exactly

```math
3\varepsilon(K/3)
=\sqrt{E^2+8\Delta^2}.
```

Thus

```math
\boxed{
\Delta_A(E)
=\sqrt{E^2+8\Delta^2}-E
=\sqrt{E^2+2E_g^2}-E.
}
```

This quantity is not an ordinary thermal activation barrier. It is the minimum energy mismatch that a symmetry-breaking band correction, finite spectral width, phonon/impurity assistance, extra band, or other physics must overcome to put the nominal channel on shell at that hot-carrier energy.

---

## 6. The key scaling result: v cancels

At fixed `E/E_g`,

```math
\boxed{
\Delta_A(E)/E_g
=\sqrt{(E/E_g)^2+2}-E/E_g,
}
```

which contains **no `v`**.

Equivalently, after rescaling

```math
\mathbf q=\hbar v\mathbf k/\Delta,
```

the entire ideal kinematic problem becomes dimensionless:

```math
\varepsilon/\Delta=\sqrt{1+q^2}.
```

Therefore

```text
high v does not create the Auger closure;
finite-gap particle-hole-symmetric relativistic dispersion creates the closure;
within that ideal shape, changing v only rescales momentum space.
```

This corrects the earlier qualitative hypothesis that simply increasing the Kane velocity might itself make Auger kinematically harder.

The two favorable resources identified so far are distinct:

```text
large v:
    lowers matched-absorptance thermal carrier column as v^-2;

particle-hole-symmetric massive-Dirac shape:
    closes the ideal direct phononless Auger channel.
```

---

## 7. Numerical mismatch scale for the 10-um / 300-K target

Use

```math
E_g=0.1239842\ \mathrm{eV},
\qquad
k_BT=25.852\ \mathrm{meV}.
```

Then

```text
hot energy E/Eg    Delta_A/Eg    Delta_A (meV)    Delta_A/kBT
1.5                 0.56155       69.62            2.69
2.0                 0.44949       55.73            2.16
3.0                 0.31662       39.26            1.52
5.0                 0.19615       24.32            0.94
10.0                0.09950       12.34            0.48
```

The mismatch approaches zero only at very high quasiparticle energy:

```math
\Delta_A(E)
=\frac{2E_g^2}{\sqrt{E^2+2E_g^2}+E}
\sim\frac{E_g^2}{E}
\qquad(E\gg E_g).
```

Thus the continuum symmetric model is exactly closed at every finite energy, but it becomes increasingly vulnerable to remote-band asymmetry or broadening at high energy. This is important because the low-energy two-band model itself will eventually fail before arbitrarily high `E` is reached.

---

## 8. Massless limit

If

```math
\Delta\to0,
```

then

```math
\varepsilon(k)=\hbar v|k|.
```

The strict inequality becomes the ordinary triangle inequality

```math
|\mathbf k_1+\mathbf k_2+\mathbf k_3|
\le|\mathbf k_1|+|\mathbf k_2|+|\mathbf k_3|,
```

with equality only for collinear, co-directed momenta.

Therefore the massless cone is only **marginally** closed: lowest-order Auger support collapses onto a collinear set rather than being strictly empty.

This is consistent with established Dirac-material theory showing that ideal linear dispersion makes lowest-order Auger processes prohibited or marginally prohibited and highly sensitive to many-body broadening, screening, and dispersion corrections.

---

## 9. Prior-art boundary

Broad Auger suppression by relativistic/symmetric dispersion is established and cannot be a novelty claim.

Mandatory comparators include:

1. G. Alymov, V. Vyurkov, V. Ryzhii, A. Satou, and D. Svintsov, *Auger recombination in Dirac materials: A tangle of many-body effects*, Phys. Rev. B **97**, 205411 (2018), DOI `10.1103/PhysRevB.97.205411`. The paper explicitly states that peculiar Dirac dispersion makes lowest-order Auger processes prohibited or marginally prohibited and studies how many-body effects restore finite rates.

2. G. Alymov et al., *Fundamental Limits to Far-Infrared Lasing in Auger-Suppressed HgCdTe Quantum Wells*, ACS Photonics **7**, 98–104 (2020), DOI `10.1021/acsphotonics.9b01099`. This work explicitly attributes suppressed HgCdTe-QW Auger recombination to highly symmetric quasi-relativistic electron-hole dispersion and energy-momentum restrictions.

3. D. B. But et al., *Suppressed Auger scattering and tunable light emission of Landau-quantized massless Kane electrons*, Nature Photonics **13**, 783–787 (2019), DOI `10.1038/s41566-019-0496-1`.

4. M. Combescot and R. Combescot, *Auger recombination in direct-gap semiconductors: Effect of anisotropy and warping*, Phys. Rev. B **37**, 8781 (1988), DOI `10.1103/PhysRevB.37.8781`. This establishes that deviations from ideal symmetric dispersions materially alter Auger thresholds and temperature scaling.

Therefore:

```text
"Dirac/symmetric dispersion suppresses Auger" = ESTABLISHED PRIOR ART.
```

The possible Experiment-10 contribution, if it survives later audit, is narrower: combining the already derived matched-absorptance high-`v` thermodynamic lever with a separate quantitative symmetry/kinematic admissibility condition, rather than claiming Auger suppression itself as new.

---

## 10. Why this is not bulk-HgCdTe closure

Real bulk HgCdTe is not the exact two-band symmetric model used above. Its Kane electronic structure includes a heavy-hole branch and remote bands; composition disorder, finite lifetime, phonons, and Coulomb many-body effects also break the ideal assumptions.

The standard bulk-HgCdTe Auger-1 process specifically exploits the real multiband structure. Therefore the theorem above says:

```text
IF the active electron-hole sector were an exact finite-gap symmetric massive-Dirac pair,
THEN the direct normal-momentum phononless 3<->1 Auger channel would be kinematically closed.
```

It does **not** say:

```text
bulk HgCdTe has zero Auger recombination.
```

This distinction must remain explicit.

---

## 11. What has been established

```text
DERIVED:
    strict subadditivity of finite-gap massive-Dirac excitation energy;

DERIVED:
    empty exact kinematic support for normal-momentum phononless eeh Auger / impact ionization;

DERIVED:
    mirror hhe closure under particle-hole symmetry;

DERIVED:
    exact minimum mismatch
    Delta_A(E)=sqrt(E^2+2 Eg^2)-E;

DERIVED:
    mismatch at fixed E/Eg is independent of v;

DERIVED:
    high-v thermodynamic lever and Auger-symmetry lever are distinct resources;

PRIOR-ART AUDIT:
    broad symmetry/Dirac Auger suppression is established.
```

## 12. What is not established

```text
Auger suppression in real bulk HgCdTe;
finite rate under particle-hole asymmetry;
critical asymmetry needed to open a channel;
role of heavy-hole curvature;
phonon-assisted Auger rate;
Umklapp Auger rate;
many-body broadening/plasmon-assisted rate;
Coulomb matrix-element scaling with v;
full room-temperature detector D*;
novelty of the eventual combined admissibility framework.
```

---

## 13. Hard stop and next question

Stop before evaluating a rate.

The next minimal question is now sharper than "does high v suppress Auger?":

> Add the smallest controlled departure from particle-hole-symmetric massive-Dirac dispersion and determine the exact condition under which Auger kinematic support first reopens. What dimensionless asymmetry parameter must remain below what bound over the thermally relevant energy window at `E_g/k_BT ~= 4.8`?

Candidate first perturbation:

```math
E_\pm(k)
=Dk^2
\pm\sqrt{\Delta^2+(\hbar vk)^2},
```

or an equivalent electron/hole curvature asymmetry.

Only after the reopening boundary is derived should Coulomb matrix elements and a finite Auger rate be introduced.
