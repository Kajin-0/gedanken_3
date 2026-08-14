# Experiment 10 — Near-Threshold Direct Auger Rate and Thermal Scaling

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Disposition:** **KINEMATIC PHASE-SPACE EXPONENT DERIVED / THERMAL ACTIVATION FACTORIZED / COULOMB-v SCALING DERIVED CONDITIONALLY / FULL MATRIX-ELEMENT RATE NOT UNIVERSAL / NOVELTY NOT ESTABLISHED**

## 1. Question for this step

Previous steps established, for the controlled finite-gap massive-Dirac family,

```math
\Sigma_e=n_ed\propto v^{-2}
```

at matched absorptance, exact Auger closure at particle-hole symmetry, and the scalar-asymmetry reopening law

```math
K_{th}\sim E_g\mathcal A_m^{-1/3}.
```

This step asks:

> Once the direct Auger channel has reopened, what part of its near-threshold rate is fixed purely by kinematics and thermal occupation, and what part remains dependent on Coulomb/spinor matrix elements?

The objective is a factorization, not an empirical Auger coefficient.

---

## 2. Dimensionless asymmetric Dirac model

Use

```math
E_\pm(k)=Dk^2\pm\sqrt{\Delta^2+(\hbar vk)^2},
\qquad \Delta=E_g/2,
```

with

```math
q=\frac{\hbar vk}{\Delta},
\qquad
\beta=\frac{D\Delta}{\hbar^2v^2},
\qquad
s(q)=\sqrt{1+q^2}.
```

For the favorable-sign `eeh` channel,

```math
e(q)=s(q)+\beta q^2,
```

```math
h(q)=s(q)-\beta q^2
```

are the positive electron and hole quasiparticle energies in units of `Delta`.

The hot-electron kinetic energy above the conduction edge is

```math
K(q)=\Delta[e(q)-1].
```

At fixed `beta>0`, let `q_th` be the exact impact-ionization threshold from `AUGER_ASYMMETRY_REOPENING_STEP_2026-08-14.md`.

---

## 3. Golden-rule phase space for a fixed hot electron

For inverse `eeh` Auger / impact ionization,

```text
e_0 -> e_1 + e_2 + h_3,
```

normal crystal momentum gives

```math
\mathbf q_3=\mathbf q_0-\mathbf q_1-\mathbf q_2.
```

After eliminating `q_3`, define the constrained final energy

```math
F(\mathbf q_1,\mathbf q_2;\mathbf q_0)
=e(q_1)+e(q_2)+h(|\mathbf q_0-\mathbf q_1-\mathbf q_2|).
```

The exact threshold satisfies

```math
\min_{\mathbf q_1,\mathbf q_2}F
=e(q_{th}).
```

For the weak-asymmetry interior branch, the minimizing configuration is the collinear threshold partition already derived,

```math
\mathbf q_1=\mathbf q_2=x\hat{\mathbf z},
\qquad
\mathbf q_3=z\hat{\mathbf z},
\qquad
q_{th}=2x+z.
```

Let the six local relative coordinates around this minimum be collected into `y`, and let

```math
H=\nabla_y\nabla_y F|_{th}
```

be the `6 x 6` Hessian.

For the interior threshold branch checked numerically, `H` is positive definite. Define

```math
M_{min}(q_0)
=\min F-e(q_0),
```

and

```math
\boxed{
a=-\left.\frac{dM_{min}}{dq_0}\right|_{q_{th}}>0.
}
```

Then for

```math
q_0=q_{th}+\delta q,
```

the available dimensionless excess energy is

```math
\eta=a\,\delta q+O(\delta q^2).
```

Locally,

```math
F-e(q_0)
=-\eta+\frac12 y^THy+\cdots.
```

Therefore the purely kinematic energy-shell integral is

```math
\int d^6y\,
\delta\!\left(\eta-\frac12y^THy\right)
=
\frac{4\pi^3}{\sqrt{\det H}}\eta^2
\Theta(\eta).
```

The exponent is fixed by the six relative coordinates:

```math
6/2-1=2.
```

Hence, if the screened Coulomb/spinor matrix element is smooth and nonzero at threshold,

```math
\boxed{
\Gamma_{II}(K)\propto(K-K_{th})^2\Theta(K-K_{th}).
}
```

This is the **phase-space threshold law** for the isotropic interior branch.

---

## 4. Explicit fixed-hot-electron factorization

Let

```math
k_*\equiv\frac{\Delta}{\hbar v},
```

and let `V_th` denote the physical Fourier-space two-particle matrix element (units energy x volume), including whichever smooth threshold spinor factor is retained.

With the standard plane-wave continuum normalization, the leading fixed-hot-electron rate can be written schematically as

```math
\boxed{
\Gamma_{II}(K)
=
\mathcal S\,
\frac{|V_{th}|^2k_*^6}{8\pi^2\hbar\Delta}
\frac{a^2}{u_0^2\sqrt{\det H}}
\left(\frac{K-K_{th}}{\Delta}\right)^2
+o[(K-K_{th})^2],
}
```

where

```math
u_0\equiv\left.\frac{de}{dq}\right|_{q_{th}}
```

and `mathcal S` collects spin/exchange/species counting conventions.

The exact numerical prefactor is convention-dependent, but the quadratic phase-space power and the `k_*^6 ~ v^-6` measure are not.

---

## 5. Matrix-element zeros change the full rate exponent

The quadratic law above is **not universally the full Kane Auger rate law**.

If the threshold matrix element vanishes as

```math
|V_{eff}|^2\propto(K-K_{th})^\nu,
```

then

```math
\boxed{
\Gamma_{II}(K)
\propto
(K-K_{th})^{2+\nu}.
}
```

This distinction is required by prior art. Gelmont (Physics Letters A 66, 323-324, 1978; DOI `10.1016/0375-9601(78)90252-9`) explicitly showed that a Kane-model conduction/heavy-hole overlap integral can vanish at threshold and alter the pre-exponential temperature dependence. Later multiband impact-ionization work likewise obtains both quadratic and cubic threshold contributions depending on the overlap mechanism.

Therefore:

```text
UNIVERSAL WITHIN THE STATED KINEMATICS:
    phase-space exponent = 2;

NOT UNIVERSAL WITHOUT A MICROSCOPIC SPINOR MODEL:
    full rate exponent.
```

---

## 6. Thermal activation from the inverse process

At equilibrium, detailed balance equates Auger recombination and impact-ionization generation.

The threshold hot electron has absolute excitation energy relative to the intrinsic chemical potential

```math
E_{hot,th}=\Delta+K_{th}.
```

At the thresholds of interest here (`K_th >> kBT`), its Fermi factor is exponentially dilute, so

```math
f_{hot}\simeq
\exp[-(\Delta+K_{th})/(k_BT)].
```

For a smooth nonzero threshold matrix element (`nu=0`), integrating the fixed-hot-electron quadratic rate over the narrow thermal shell above threshold gives

```math
\int_0^\infty d\epsilon\,
\epsilon^2e^{-\epsilon/(k_BT)}
=2(k_BT)^3.
```

Hence the equilibrium direct Auger event rate per volume has the leading threshold form

```math
\boxed{
G_A^{vol}
\propto
T^3
\exp\!\left[-\frac{E_g/2+K_{th}}{k_BT}\right]
}
```

up to the band-curvature, Coulomb, spinor-overlap, and normalization prefactor.

More generally, if

```math
|V_{eff}|^2\propto(K-K_{th})^\nu,
```

then

```math
\boxed{
G_A^{vol}
\propto
T^{3+\nu}
\exp\!\left[-\frac{E_g/2+K_{th}}{k_BT}\right].
}
```

The **activation exponent is robust**; the polynomial temperature power is matrix-element dependent.

---

## 7. Cross-check against classical direct-gap Auger theory

In the low-temperature nondegenerate parabolic-edge limit,

```math
n_i\propto T^{3/2}e^{-E_g/(2k_BT)}.
```

Dividing the equilibrium event rate by `n_i` gives the Auger-limited inverse lifetime

```math
\boxed{
\tau_A^{-1}
\propto
T^{3/2+\nu}
\exp[-K_{th}/(k_BT)].
}
```

For `nu=0`, this reproduces the classical Beattie-Landsberg structure quoted by Combescot & Combescot, Phys. Rev. B 37, 8781 (1988):

```math
\tau^{-1}\sim
T^{3/2}\exp[-E_{th}/(k_BT)]
```

up to material-dependent powers introduced by anisotropy/warping.

This cross-check supports the thermal saddle derivation.

At the actual Experiment-10 target, do not use the parabolic `n_i` prefactor quantitatively; exact finite-gap Dirac statistics remain controlling. The threshold activation itself is unaffected by that warning.

---

## 8. 10-um / 300-K activation witness

At

```math
E_g/(k_BT)=4.79592,
\qquad
\Delta/(k_BT)=2.39796,
```

and at the previously derived symmetry tolerance

```math
\mathcal A_m\approx0.08476,
\qquad
K_{th}=10k_BT,
```

we obtain

```math
\boxed{
e^{-K_{th}/k_BT}=e^{-10}=4.54\times10^{-5}
}
```

for the lifetime activation factor, while the equilibrium event-rate occupation factor is

```math
\boxed{
\exp[-(\Delta+K_{th})/(k_BT)]
=\exp[-12.39796]
=4.13\times10^{-6}.
}
```

Selected values from the exact asymmetry thresholds are

```text
A_m       K_th/kBT    exp(-K_th/kBT)    exp[-(Delta+K_th)/kBT]
0.40        5.873       2.81e-3               2.56e-4
0.20        7.536       5.34e-4               4.85e-5
0.10        9.470       7.71e-5               7.01e-6
0.08476    10.000       4.54e-5               4.13e-6
0.04       12.848       2.63e-6               2.39e-7
0.02       16.273       8.56e-8               7.79e-9
0.01       20.675       1.05e-9               9.54e-11
```

Thus the symmetry coordinate enters the direct-channel rate primarily through a very strong exponential lever once `K_th/kBT` is large.

---

## 9. Explicit v scaling before screening details

For one Dirac species at fixed

```text
Delta,
beta,
Delta/(kBT),
normalized threshold geometry,
```

the four-particle golden-rule momentum measure gives

```math
\boxed{
G_A^{vol}
\propto
|V_{th}|^2v^{-9}
\left(\frac{k_BT}{\Delta}\right)^{3+\nu}
\exp[-(\Delta+K_{th})/(k_BT)]
}
```

up to fixed powers of `Delta` and `hbar` and a dimensionless threshold function.

Matched absorptance requires

```math
d\propto v
```

for the one-species family, so the event rate per detector area obeys

```math
\boxed{
G_A^{area}=dG_A^{vol}
\propto
|V_{th}|^2v^{-8}
\mathcal F_A(\beta,T/\Delta).
}
```

This `v^-8` is a **phase-space/density measure before the momentum dependence of Coulomb interaction is inserted**. It must not be advertised as a universal physical Auger scaling.

---

## 10. Minimum screened-Coulomb model

Use a static Yukawa form

```math
V(Q)
=\frac{e^2}
{\epsilon_0\epsilon_r(Q^2+\kappa^2)}
\times S_{cv},
```

where `S_cv` is the dimensionless spinor/overlap factor.

At fixed dimensionless threshold geometry,

```math
Q_{th}=k_*\mathcal Q_{th}
=\frac{\Delta}{\hbar v}\mathcal Q_{th}.
```

Define

```math
s_\kappa=\frac{\hbar v\kappa}{\Delta}.
```

Then

```math
|V_{th}|^2
=
\frac{e^4\hbar^4v^4}
{\epsilon_0^2\epsilon_r^2\Delta^4}
\frac{|S_{cv}|^2}
{(\mathcal Q_{th}^2+s_\kappa^2)^2}.
```

Combining with matched thickness gives the conditional direct-channel scaling

```math
\boxed{
G_A^{area}
\propto
\frac{|S_{cv}|^2}{\epsilon_r^2}
\frac{v^{-4}}
{(\mathcal Q_{th}^2+s_\kappa^2)^2}
\left(\frac{k_BT}{\Delta}\right)^{3+\nu}
\exp[-(\Delta+K_{th})/(k_BT)].
}
```

This is the first rate-level joint dependence in Experiment 10.

### Limiting screening cases

1. **Weak screening at the threshold transfer** (`s_kappa << Q_th`):

```math
\boxed{G_A^{area}\propto v^{-4}}
```

at fixed `beta, epsilon_r, S_cv`.

2. **Fixed physical screening length** (`kappa` independent of `v`) and sufficiently large `v`: `s_kappa ~ v`, so the denominator contributes another `v^4` and

```math
G_A^{area}\propto v^{-8}.
```

3. **Intrinsic Debye screening:** since

```math
\kappa_D^2\propto(n_e+n_h)/T\propto v^{-3}
```

at fixed finite `Eg,T,beta`,

```math
s_\kappa^2\propto v^{-1}.
```

Thus the large-`v` asymptote moves toward the weak-screening result

```math
\boxed{G_A^{area}\propto v^{-4}}
```

before dielectric/spinor covariance is considered.

Therefore the long-range Coulomb enhancement caused by the smaller physical momentum transfer weakens, but does not cancel, the high-`v` rate advantage in this minimal model.

---

## 11. Combined admissibility structure emerging

The direct-channel event rate now factorizes schematically as

```math
\boxed{
G_A^{area}
=
\mathcal I_A
\times
v^{-4}
\times
\exp[-K_{th}(\mathcal A_m)/(k_BT)]
\times
\text{known thermal/threshold factors},
}
```

in the weak-screening Coulomb limit, where `mathcal I_A` contains dielectric screening, spinor overlaps, exchange, species counting, and finite-width corrections.

Together with

```math
K_{th}\sim E_g\mathcal A_m^{-1/3}
```

for weak scalar asymmetry, the dominant reduced-model dependence is

```math
\boxed{
G_A^{area}
\sim
v^{-4}
\exp\!\left[-\frac{E_g}{k_BT}\mathcal A_m^{-1/3}\right]
\times\mathcal I_A
}
```

up to the additional universal intrinsic factor `exp[-E_g/(2kBT)]` for the equilibrium event rate.

This is **not yet a universal detector bound**, because `mathcal I_A` can vary strongly with multiband wave functions, dielectric response, screening, phonons, and heavy-hole/remote-band channels.

But it is the first point where the two electronic-structure coordinates identified earlier enter one direct rate formula:

```text
large v
    -> algebraic suppression of matched-area direct Auger events;

small finite-k particle-hole asymmetry
    -> exponential threshold suppression.
```

---

## 12. Prior-art boundary

Established prior art already contains:

- threshold-activated direct-gap Auger lifetimes;
- Beattie-Landsberg thermal activation;
- changes of the pre-exponential power from anisotropy/warping;
- Kane overlap zeros at threshold;
- quadratic/cubic impact-ionization threshold laws in multiband direct-gap semiconductors;
- HgCdTe-QW Auger suppression from quasi-relativistic symmetry.

Mandatory comparators include:

```text
Combescot & Combescot, Phys. Rev. B 37, 8781 (1988), DOI 10.1103/PhysRevB.37.8781;
Gelmont, Phys. Lett. A 66, 323-324 (1978), DOI 10.1016/0375-9601(78)90252-9;
Afanasiev, Greshnov & Zegrya, Semiconductors / arXiv:2112.05021;
Alymov et al., Phys. Rev. B 97, 205411 (2018);
Alymov et al., ACS Photonics 7, 98-104 (2020);
Morozov et al., ACS Photonics 8, 3526-3535 (2021).
```

Therefore neither the threshold activation nor the quadratic phase-space law alone is a novelty claim.

The possible contribution remains the **detector-specific joint admissibility synthesis** linking matched absorptance, finite-gap Dirac statistics, microscopic velocity resources, symmetry-controlled Auger threshold, and explicit interaction-factor separation.

```text
NOVELTY NOT ESTABLISHED.
```

---

## 13. What has actually been established

```text
DERIVED:
    fixed-hot-electron six-dimensional phase-space exponent 2;

DERIVED:
    generic full exponent 2+nu if the squared matrix element vanishes as excess-energy^nu;

DERIVED:
    equilibrium threshold activation exp[-(Eg/2+Kth)/kBT];

DERIVED:
    smooth-matrix thermal prefactor T^3;

CROSS-CHECKED:
    division by low-T ni recovers Beattie-Landsberg lifetime form T^(3/2) exp(-Kth/kBT);

DERIVED CONDITIONALLY:
    matched-area kinematic measure ~ |V_th|^2 v^-8;

DERIVED CONDITIONALLY WITH STATIC COULOMB:
    weak-screening matched-area direct Auger scaling ~ v^-4 times the symmetry-controlled activation factor.
```

## 14. What is not established

```text
microscopic Dirac/Kane spinor exponent nu for the exact proposed material class;
exchange cancellation at threshold;
dynamic rather than static screening;
heavy-hole and remote-band competing Auger channels;
phonon-assisted Auger;
Umklapp/disorder-assisted Auger;
full radiative-versus-Auger detector noise inequality;
novelty of the combined framework.
```

---

## 15. Next question

The direct channel is now factored as far as it can be without specifying multiband wave functions.

The next minimal detector-level question is:

> Under matched external absorptance and optical environment, compare the unavoidable radiative/background generation floor with the thresholded direct-Auger generation derived here. Can one express a band-structure admissibility condition `G_A <= G_rad+G_bg` in terms of `v`, finite-momentum asymmetry, dielectric/screening resources, and the fixed optical boundary?

This is the natural point to test the provisional `Xi_nr` idea from the founding notes. Do not yet rank real materials.
