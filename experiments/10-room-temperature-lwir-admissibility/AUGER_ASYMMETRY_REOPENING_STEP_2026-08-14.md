# Experiment 10 — Particle-Hole-Asymmetry Auger Reopening Boundary

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Disposition:** **FINITE-ASYMMETRY REOPENING BOUNDARY DERIVED IN CONTROLLED TOY MODEL / WEAK-ASYMMETRY CUBE-ROOT THRESHOLD LAW DERIVED / BROAD THRESHOLD PHYSICS IS PRIOR ART / NOVELTY NOT ESTABLISHED**

## 1. Question for this step

The previous step proved exact kinematic closure of the normal-momentum phononless `eeh` and `hhe` Auger channels in the particle-hole-symmetric finite-gap massive-Dirac model.

This step adds the smallest scalar particle-hole asymmetry,

```math
E_\pm(k)=Dk^2\pm\sqrt{\Delta^2+(\hbar vk)^2},
\qquad \Delta=E_g/2,
```

and asks:

> How large must the asymmetry be before the previously empty direct Auger phase space reopens, and how does the corresponding impact-ionization threshold scale as particle-hole symmetry is restored?

No Coulomb matrix element or empirical Auger coefficient is used here.

---

## 2. Dimensionless asymmetry

Define

```math
q=\frac{\hbar vk}{\Delta},
\qquad
s(q)=\sqrt{1+q^2},
```

and

```math
\boxed{
\beta=\frac{D\Delta}{\hbar^2v^2}.
}
```

For `D>0`, the positive electron and hole quasiparticle energies relative to the midgap reference are

```math
\frac{E_e(q)}{\Delta}=s(q)+\beta q^2,
```

```math
\frac{E_h(q)}{\Delta}=s(q)-\beta q^2.
```

For `D<0`, the `eeh` and `hhe` roles are interchanged. Therefore the kinematic tolerance can be stated in terms of `|beta|`.

Near the band edge,

```math
\frac{1}{m_e}
=\frac{v^2}{\Delta}(1+2\beta),
```

```math
\frac{1}{m_h}
=\frac{v^2}{\Delta}(1-2\beta).
```

Thus define the normalized inverse-mass asymmetry

```math
\boxed{
\mathcal A_m
=\frac{|m_e^{-1}-m_h^{-1}|}
{m_e^{-1}+m_h^{-1}}
=2|\beta|.
}
```

The condition `|beta|<1/2` keeps both edge curvatures positive in this reduced model.

Important: `A_m` is only a convenient observable representation of the `Dk^2` perturbation. In a real multiband material, matching edge masses alone does not guarantee symmetry at the finite momenta relevant to Auger scattering.

---

## 3. Impact-ionization formulation

Take `D>0` and the inverse `eeh` process

```text
e_0 -> e_1 + e_2 + h_3.
```

Dimensionless crystal momentum is conserved:

```math
\mathbf q_0
=\mathbf q_1+\mathbf q_2+\mathbf q_3.
```

Energy conservation requires

```math
s(q_0)+\beta q_0^2
=
s(q_1)+\beta q_1^2
+s(q_2)+\beta q_2^2
+s(q_3)-\beta q_3^2.
```

At `beta=0` this cannot be satisfied, as proved in the previous step.

---

## 4. Threshold reduction to a one-dimensional partition

At the first reopening threshold, minimize the final three-quasiparticle energy at fixed total momentum `q_0`.

For the controlled weak-asymmetry branch where the relevant electron and hole radial group velocities remain positive, stationarity under a vector momentum constraint requires all three final group velocities to point along the same Lagrange-multiplier direction. The two identical electron branches then carry equal momenta.

Write

```math
q_1=q_2=x,
\qquad
q_3=z,
\qquad
q_0=2x+z,
```

with all momenta collinear and co-directed.

The exact energy mismatch is

```math
\mathcal M
=
2s(x)+s(z)-s(q_0)
-2\beta(x+z)^2.
```

Therefore the asymmetry required to put this configuration on shell is

```math
\boxed{
\beta(x;q_0)
=
\frac{2s(x)+s(q_0-2x)-s(q_0)}
{2(q_0-x)^2},
\qquad
0\le x\le q_0/2.
}
```

The exact reopening boundary within this isotropic model is consequently

```math
\boxed{
\beta_c(q_0)
=
\min_{0\le x\le q_0/2}
\frac{2s(x)+s(q_0-2x)-s(q_0)}
{2(q_0-x)^2}.
}
```

Selected unconstrained two-dimensional vector optimizations were also performed numerically and returned the same collinear minima to numerical precision for `q_0=2.5,3,5,10`.

For an interior minimum, `z=q_0-2x` and the stationarity condition can be written

```math
\boxed{
\frac{x}{s(x)}
-\frac{z}{s(z)}
+\frac{2s(x)+s(z)-s(q_0)}{x+z}
=0.
}
```

Together with the boxed expression for `beta_c`, this gives the exact finite-energy threshold parametrically.

---

## 5. Boundary-to-interior transition

For sufficiently small total momentum, the minimizing partition sits at the boundary

```math
x=0,
\qquad
z=q_0,
```

which gives exactly

```math
\beta_c(q_0)=\frac{1}{q_0^2}.
```

The derivative of the variational ratio at `x=0` changes sign when

```math
q_0^2=2\sqrt{1+q_0^2}.
```

Hence the branch-change scale is

```math
\boxed{
q_*=\sqrt{2+2\sqrt2}\approx2.19737,
}
```

with

```math
\boxed{
\beta_*=\frac1{q_*^2}
=\frac{\sqrt2-1}{2}
\approx0.207107.
}
```

The weak-asymmetry regime `|beta| << 1`, which is the relevant controlled limit for an approximately Dirac material, lies on the interior high-threshold branch `q_0>q_*`.

---

## 6. Weak-asymmetry asymptotic — cube-root divergence

For `q_0 >> 1`, write

```math
x=a q_0,
\qquad
z=(1-2a)q_0,
\qquad
0<a<1/2.
```

Using

```math
s(q)=q+\frac{1}{2q}+O(q^{-3}),
```

the threshold becomes

```math
\beta_c(q_0)
=
\frac{1}{q_0^3}
\frac{1}{2a(1-2a)}
+O(q_0^{-5}).
```

The coefficient is minimized at

```math
a=1/4,
```

so asymptotically

```math
q_1=q_2\to q_0/4,
\qquad
q_3\to q_0/2,
```

and

```math
\boxed{
\beta_c(q_0)\sim\frac{4}{q_0^3}.
}
```

Therefore, for a small fixed asymmetry,

```math
\boxed{
q_{th}\sim\left(\frac{4}{|\beta|}\right)^{1/3}.
}
```

This is the first key result of this step: the impact-ionization threshold momentum diverges as `|beta|^{-1/3}` as particle-hole symmetry is restored.

---

## 7. Threshold kinetic-energy law

The hot-electron kinetic energy above the conduction edge is

```math
K_{th}
=
\Delta\left[
 s(q_{th})+|\beta|q_{th}^2-1
\right].
```

In the weak-asymmetry limit, the leading term is

```math
K_{th}
\sim
\Delta 4^{1/3}|\beta|^{-1/3}.
```

Using

```math
\mathcal A_m=2|\beta|,
\qquad
E_g=2\Delta,
```

gives the particularly simple form

```math
\boxed{
K_{th}
\sim
E_g\,\mathcal A_m^{-1/3},
\qquad
\mathcal A_m\to0.
}
```

Thus at fixed `E_g/k_BT`,

```math
\boxed{
\frac{K_{th}}{k_BT}
\sim
\frac{E_g}{k_BT}\,\mathcal A_m^{-1/3}.
}
```

Equivalently, a desired large threshold `K_th >= nu k_BT` requires asymptotically

```math
\boxed{
\mathcal A_m
\lesssim
\left(\frac{E_g}{\nu k_BT}\right)^3.
}
```

This is a symmetry-tolerance scaling law for the reduced model. It is not yet a finite Auger-rate theorem.

---

## 8. Exact 10-um / 300-K thresholds

For Experiment 10,

```math
\frac{E_g}{k_BT}=4.796,
\qquad
\frac{\Delta}{k_BT}=2.398.
```

Numerically minimizing the exact finite-`beta` threshold gives:

```text
A_m      beta       q_th      K_th/kBT     E_e,th/Eg
0.40     0.200      2.236       5.873         1.725
0.20     0.100      3.052       7.536         2.071
0.10     0.050      4.019       9.470         2.475
0.04     0.020      5.635      12.848         3.179
0.02     0.010      7.199      16.273         3.893
0.01     0.005      9.149      20.675         4.811
```

Here `E_e,th` is the total hot-electron quasiparticle energy measured from the midgap reference; `K_th=E_e,th-Delta`.

The factor `exp(-K_th/kBT)` may be used only as a qualitative measure of hot-state rarity. It is **not** the Auger rate, because the complete equilibrium/non-equilibrium phase-space occupations and Coulomb matrix element have not yet been integrated.

---

## 9. Inverted room-temperature symmetry requirement

Solving the exact threshold relation for a desired thermal barrier gives:

```text
required K_th/kBT    maximum A_m     implied m_h/m_e for D>0
8                     0.1671          1.401
10                    0.08476         1.185
12                    0.04900         1.103
15                    0.02536         1.052
```

The mass-ratio column follows from the reduced-model edge relation

```math
\frac{m_h}{m_e}
=\frac{1+\mathcal A_m}{1-\mathcal A_m}.
```

Therefore, in this particular `Dk^2` model, placing the direct-channel threshold above `10 k_BT` at the 10-um / 300-K target requires roughly

```math
\boxed{
\mathcal A_m\lesssim0.0848,
}
```

which corresponds to an edge-mass ratio no larger than about `1.185` for the favorable sign.

Again: this should not be interpreted as a universal rule that real electron and hole masses need only match within 18.5%. The actual requirement is that the **finite-momentum electron-hole dispersions remain sufficiently symmetric throughout the Auger-relevant momentum window**. The edge-mass criterion is exact only for the chosen scalar `Dk^2` asymmetry model.

---

## 10. Relation to the high-v lever

The asymmetry parameter is

```math
\beta=\frac{D\Delta}{\hbar^2v^2}.
```

At fixed dimensional `D` and fixed gap, increasing `v` reduces `|beta|`. However this should not be misread as a new independent `v`-driven Auger theorem: in a microscopic material, `D` and `v` arise from the same multiband Hamiltonian and generally co-vary.

The cleaner material-design statement remains two-dimensional:

```text
high v
    -> low matched-absorptance thermal carrier column;

small finite-momentum particle-hole asymmetry
    -> high direct Auger threshold.
```

A later multiband admissibility theorem must therefore constrain both resources simultaneously rather than treating `D` and `v` as independent knobs.

---

## 11. Prior-art boundary

The broad physics that quasi-relativistic electron-hole symmetry raises the Auger threshold is established.

Mandatory comparators include:

1. Alymov et al., *Fundamental Limits to Far-Infrared Lasing in Auger-Suppressed HgCdTe Quantum Wells*, ACS Photonics **7**, 98–104 (2020), DOI `10.1021/acsphotonics.9b01099`. Their full multiband HgCdTe-QW calculation shows that the Auger threshold normalized to the gap becomes very large near the Dirac-like critical regime and explicitly attributes the enhancement to quasi-relativistic electron-hole dispersion.

2. Morozov et al., *Coherent Emission in the Vicinity of 10 THz due to Auger-Suppressed Recombination of Dirac Fermions in HgCdTe Quantum Wells*, ACS Photonics **8**, 3526–3535 (2021), DOI `10.1021/acsphotonics.1c01111`. The paper states that for massive Dirac fermions Auger recombination can be suppressed below a carrier kinetic-energy threshold controlled by dispersion nonparabolicity and electron-hole symmetry.

3. Aleshkin et al., *Threshold energies of Auger recombination in HgTe/CdHgTe quantum well heterostructures with 30–70 meV bandgap*, J. Phys.: Condens. Matter **31**, 425301 (2019), DOI `10.1088/1361-648X/ab301a`, which calculates Auger threshold energies in an eight-band Kane model.

4. Classical threshold/anisotropy work, including Combescot and Combescot, establishes that Auger activation is controlled by detailed band dispersion rather than gap alone.

Therefore:

```text
"electron-hole symmetry raises/diverges the Auger threshold" = ESTABLISHED TERRITORY.
```

The present `K_th ~ E_g A_m^{-1/3}` law is a compact analytical consequence of the specific scalar-asymmetry massive-Dirac toy model. A focused search has not yet established whether this exact cube-root law has appeared previously. Do not claim novelty for it without a deeper analytical prior-art audit.

---

## 12. What has been established

```text
DERIVED:
    dimensionless scalar asymmetry beta=D Delta/(hbar^2 v^2);

DERIVED:
    exact reduced-model relation A_m=2|beta|;

DERIVED:
    exact variational reopening boundary beta_c(q0);

DERIVED:
    weak-asymmetry threshold beta_c ~ 4/q_th^3;

DERIVED:
    threshold momentum q_th ~ (4/|beta|)^(1/3);

DERIVED:
    threshold kinetic energy K_th ~ Eg A_m^(-1/3);

NUMERICAL VALIDATION:
    exact 10-um / 300-K finite-beta thresholds and inverted symmetry tolerances;

PRIOR-ART AUDIT:
    broad symmetry-enhanced Auger threshold is established.
```

## 13. What is not established

```text
finite Auger rate;
Coulomb matrix-element scaling;
phonon-assisted or disorder-assisted Auger;
heavy-hole/remote-band reopening;
that edge-mass asymmetry alone controls a real material;
that the cube-root law is novel;
full detector D* or noise;
that a real material can simultaneously attain high v and the required symmetry.
```

---

## 14. Next question

The direct two-band Auger problem is now kinematically characterized to first order in a controlled symmetry-breaking model.

The next minimal question should **not** yet be a materials search.

> If the direct Auger channel is given the exact threshold above, what is the leading thermal/phase-space scaling of its rate just above reopening, and does combining that rate with the already derived matched-absorptance `Sigma_e ~ v^-2` law produce a genuine room-temperature admissibility inequality?

The next step may introduce the simplest screened Coulomb matrix element, but must retain the exact threshold structure and clearly separate universal phase-space scaling from model-dependent interaction strength.
