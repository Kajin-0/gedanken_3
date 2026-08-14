# Experiment 10 — Matched-Absorptance Massive-Dirac DOS Scaling

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Disposition:** **DERIVED WITHIN IDEALIZED MASSIVE-DIRAC MODEL / CROSS-CLASS COMPARISON STILL CONDITIONAL / NOVELTY NOT ESTABLISHED**

## 1. Question answered in this step

The founding question was deliberately narrower than a material survey:

> At fixed finite LWIR gap, temperature, useful absorptance, and temporal target, can a low-DOS massive-Dirac/Kane absorber reduce its equilibrium carrier population without paying an exact compensating optical cost?

This file answers that question **inside the clean isotropic 3-D massive-Dirac family**. It also identifies why the originally proposed generic parabolic comparator is underconstrained unless its masses and optical matrix elements are tied to a common microscopic Hamiltonian.

No Auger process is added in this step.

---

## 2. Minimal massive-Dirac model

Take one four-component isotropic massive-Dirac species

```math
H(\mathbf k)
=\hbar v\,\tau_x\,\boldsymbol\sigma\cdot\mathbf k
+\Delta\tau_z,
\qquad
\Delta=E_g/2,
```

with spectrum

```math
E_\pm(k)=\pm E_k,
\qquad
E_k=\sqrt{\Delta^2+(\hbar vk)^2}.
```

Allow `N_D` identical Dirac species/valleys. Each four-component species contains the usual twofold degeneracy of each `+/-` branch.

Assume for this step:

```text
intrinsic particle-hole symmetry, so mu=0;
clean independent quasiparticles;
no SRH and no Auger yet;
fixed Eg and T;
ideal antireflection / no parasitic interface loss;
weak-loss propagation through a background refractive index n_b;
all N_D species couple equivalently to the accepted optical field.
```

These assumptions define the theorem scope. They are not claims about a complete HgCdTe band structure.

At the target

```math
\lambda_c=10\ \mu\mathrm m,
\qquad
T=300\ \mathrm K,
```

```math
E_g=0.1239841984\ \mathrm{eV},
```

```math
k_BT=0.0258519998\ \mathrm{eV},
```

and

```math
\delta\equiv\frac{\Delta}{k_BT}
=\frac{E_g}{2k_BT}
\approx2.39796146.
```

---

## 3. Exact equilibrium carrier density

For `mu=0`, the conduction-electron density is

```math
n_e
=2N_D\int\frac{d^3k}{(2\pi)^3}
\frac{1}{e^{E_k/(k_BT)}+1}.
```

Set

```math
x=\frac{\hbar vk}{k_BT}.
```

Then exactly

```math
\boxed{
n_e
=\frac{N_D}{\pi^2}
\left(\frac{k_BT}{\hbar v}\right)^3
F_2(\delta),
}
```

where

```math
F_2(\delta)
=\int_0^\infty
\frac{x^2\,dx}
{\exp\!\left(\sqrt{x^2+\delta^2}\right)+1}.
```

Particle-hole symmetry gives

```math
n_h=n_e.
```

Therefore, at fixed `E_g,T`,

```math
\boxed{n_e\propto N_D v^{-3}.}
```

For the 10-um / 300-K target,

```math
F_2(2.39796146)=0.7887622040.
```

For one Dirac species and

```math
v=1.00\times10^6\ \mathrm{m/s},
```

```math
\boxed{
n_e=4.8421\times10^{15}\ \mathrm{cm^{-3}}.
}
```

### Finite-gap parabolic check

The band-edge expansion is

```math
E_+(k)
=\Delta+\frac{\hbar^2k^2}{2m_D}+\cdots,
```

with

```math
m_D=\frac{\Delta}{v^2}=\frac{E_g}{2v^2}.
```

The corresponding nondegenerate edge-parabolic estimate is

```math
n_e^{par}
=2\left(\frac{m_Dk_BT}{2\pi\hbar^2}\right)^{3/2}
e^{-\delta}.
```

The exact ratio is

```math
\boxed{
\frac{n_e^{Dirac}}{n_e^{par}}
=\sqrt{\frac{2}{\pi}}
\frac{e^\delta F_2(\delta)}{\delta^{3/2}}.
}
```

At the present target,

```math
\boxed{
\frac{n_e^{Dirac}}{n_e^{par}}
\approx1.8644.
}
```

Thus the edge-parabolic approximation underestimates the carrier density by about `46%` relative to the exact result when expressed as `(parabolic-exact)/exact`, or equivalently the exact density is about `86%` larger than the edge-parabolic estimate.

This discrepancy is primarily a **nonparabolic-dispersion correction**, not a large Fermi-versus-Boltzmann correction. If the exact Dirac dispersion is retained but the Fermi factor is replaced by Maxwell-Boltzmann statistics, the dimensionless integral becomes

```math
F_2^{MB}(\delta)=\delta^2K_2(\delta)
\approx0.807315,
```

only about `2.35%` above the exact Fermi-Dirac integral.

So at 10 um and 300 K, exact finite-gap dispersion matters materially even though `E_g/k_BT ~= 4.8`.

---

## 4. Interband optical conductivity

The velocity operator is

```math
\hat v_x=v\tau_x\sigma_x.
```

For the two doubly-degenerate Dirac branches, the angular-averaged interband velocity-matrix-element sum is

```math
\overline{\sum_{cv}|\langle c|\hat v_x|v\rangle|^2}
=
\frac{2v^2}{3}
\left(2+\frac{\Delta^2}{E_k^2}\right).
```

Insert this into the clean-limit Kubo / Fermi-golden-rule expression

```math
\sigma_1(\omega)
=
\frac{\pi e^2}{\omega}
N_D\int\frac{d^3k}{(2\pi)^3}
[f(-E_k)-f(E_k)]
\sum_{cv}|v_x^{cv}|^2
\delta(2E_k-\hbar\omega).
```

At intrinsic `mu=0`,

```math
f(-E)-f(E)=\tanh\left(\frac{E}{2k_BT}\right).
```

The radial integral gives

```math
\boxed{
\sigma_1(\omega)
=
\frac{N_De^2\omega}{12\pi\hbar v}
\left(1+\frac{2\Delta^2}{\hbar^2\omega^2}\right)
\sqrt{1-\frac{4\Delta^2}{\hbar^2\omega^2}}
\tanh\left(\frac{\hbar\omega}{4k_BT}\right)
\Theta(\hbar\omega-2\Delta).
}
```

The important scaling at fixed normalized photon energy and fixed `E_g,T` is

```math
\boxed{\sigma_1\propto N_Dv^{-1}.}
```

This agrees with the established 3-D Dirac result that the interband optical conductivity is linear in photon frequency and inversely proportional to the Dirac/Fermi velocity. That underlying optical-conductivity fact is not new.

In the weak-loss propagation approximation,

```math
\alpha(\omega)
\simeq\frac{\sigma_1(\omega)}{n_b\epsilon_0c}.
```

Define

```math
r\equiv\frac{\hbar\omega}{E_g}>1
```

and

```math
Q(r,\delta)
=\left(1+\frac{1}{2r^2}\right)
\sqrt{1-r^{-2}}
\tanh\left(\frac{r\delta}{2}\right).
```

Then

```math
\boxed{
\alpha(\omega)
=
\frac{N_D\alpha_{fs}}{3n_b}
\frac{\omega}{v}
Q(r,\delta).
}
```

Thus

```math
\boxed{\alpha\propto N_Dv^{-1}.}
```

---

## 5. Matched-absorptance result

For an ideal single-pass absorber with no reflection,

```math
A(\omega)=1-e^{-\alpha(\omega)d}.
```

Let the required optical depth at a chosen frequency be

```math
\zeta=-\ln[1-A_0].
```

The thickness required to reach that absorptance is

```math
\boxed{
d
=
\frac{3n_b\zeta}{N_D\alpha_{fs}Q(r,\delta)}
\frac{v}{\omega}.
}
```

Therefore

```math
\boxed{d\propto\frac{v}{N_D}.}
```

Now define the equilibrium conduction-electron column per detector area

```math
\Sigma_e\equiv n_ed.
```

Combining the exact carrier density and optical thickness gives

```math
\boxed{
\Sigma_e
=
\frac{3n_b\zeta F_2(\delta)}
{\pi^2\alpha_{fs}Q(r,\delta)}
\frac{(k_BT)^3}
{\hbar^3\omega}
\frac{1}{v^2}.
}
```

The Dirac-species degeneracy cancels exactly:

```math
\boxed{
\Sigma_e\propto v^{-2},
\qquad
\Sigma_e\text{ is independent of }N_D.
}
```

The total equilibrium electron-plus-hole column is simply

```math
\Sigma_{eh}=2\Sigma_e.
```

### First nontrivial consequence

This is the first important result of Experiment 10:

> **Inside the ideal 3-D massive-Dirac family, matching useful optical depth does not cancel the low-DOS advantage. Volume carrier density falls as `v^-3`, optical absorption only falls as `v^-1`, and the absorptance-matched thermal carrier column therefore falls as `v^-2`.**

A second consequence corrects the founding heuristic about valley degeneracy:

> **Equivalent Dirac-species/valley degeneracy is not a lever for reducing thermal carrier inventory per absorbed area in this model. It raises thermal density and optical absorption in the same linear proportion, so it cancels after thickness is adjusted to match absorptance.**

This cancellation is a model result, not a general theorem for arbitrary multivalley semiconductors with inequivalent optical selection rules.

---

## 6. Spectral rather than single-frequency matching

At fixed `E_g,T,n_b`, the entire absorption spectrum factorizes as

```math
\alpha(\omega)
=\frac{N_D}{v}\,\mathcal F(\omega;E_g,T,n_b).
```

Therefore choosing

```math
d\propto\frac{v}{N_D}
```

keeps

```math
\alpha(\omega)d
```

unchanged at **every frequency** within the validity of the same Dirac model, not merely at one selected photon energy.

Thus the `v^-2` carrier-column result can be imposed while matching the full single-pass absorptance spectral shape in this idealized model.

Important caveat: this factorization assumes the background refractive index and interface optics do not acquire a compensating `v` dependence through remote bands or Kramers-Kronig constraints. That is one of the next microscopic consistency questions.

---

## 7. Does the thicker high-v absorber become slower?

For a photon with

```math
\hbar\omega=rE_g,
```

the excited Dirac quasiparticle has energy

```math
E=\hbar\omega/2=r\Delta.
```

Its group speed is

```math
u_\omega
=\frac{1}{\hbar}\frac{\partial E}{\partial k}
=v\sqrt{1-r^{-2}}.
```

Because

```math
d\propto v,
\qquad
u_\omega\propto v,
```

the ideal ballistic crossing time satisfies

```math
\boxed{
\tau_{ball}=\frac{d}{u_\omega}
\propto v^0
}
```

for fixed `N_D`.

More explicitly,

```math
\boxed{
\tau_{ball}
=
\frac{3n_b\zeta}
{N_D\alpha_{fs}\omega Q(r,\delta)\sqrt{1-r^{-2}}}.
}
```

So **the same increase in `v` that forces a proportionally thicker absorber also increases the ideal group velocity by the same factor.** There is no ballistic-transit-time penalty in this minimal model.

This does not prove that a real detector's `f_3dB` is invariant: scattering, diffusion, contacts, capacitance, recombination, depletion field, and saturation velocity are absent. It establishes only that the simplest absorptance-versus-ballistic-speed tradeoff does not erase the `v^-2` carrier-column advantage.

---

## 8. Numerical witness at the 10-um / 300-K target

Choose a comparison point inside the absorption band,

```math
r=1.2,
```

so

```math
\hbar\omega=1.2E_g
```

and the corresponding free-space wavelength is about `8.33 um`.

Take

```text
n_b = 3.5,
N_D = 1,
A_0 = 0.90,
zeta = ln(10) = 2.302585.
```

At this point,

```math
Q(r,\delta)=0.665358.
```

The exact model gives:

```text
v (m/s)       n_e (cm^-3)      alpha (cm^-1)    d_90 (um)    Sigma_e (cm^-2)    tau_ball (ps)
5.0e5         3.874e16          2090.5            11.015       4.267e13            39.85
1.0e6         4.842e15          1045.2            22.029       1.067e13            39.85
2.0e6         6.053e14           522.6            44.059       2.667e12            39.85
```

Thus doubling `v` from `1e6` to `2e6 m/s` at fixed gap and 90% absorptance:

```text
reduces volume thermal carrier density by 8x;
requires 2x absorber thickness;
reduces thermal carrier column by 4x;
leaves the ideal ballistic crossing time unchanged.
```

This is exactly the scaling predicted analytically.

---

## 9. What this does and does not establish

### Established within the stated ideal model

```text
DERIVED:
    n_e ~ N_D v^-3.

DERIVED:
    alpha ~ N_D v^-1 at fixed normalized photon energy.

DERIVED:
    matched absorptance requires d ~ v/N_D.

DERIVED:
    thermal carrier column Sigma_e = n_e d ~ v^-2.

DERIVED:
    equivalent species degeneracy N_D cancels from Sigma_e.

DERIVED:
    ideal ballistic crossing time is independent of v.

NUMERICAL VALIDATION:
    the 10-um / 300-K example follows the exact 8x / 2x / 4x / invariant scaling under a factor-2 change in v.
```

### Not established

```text
NOT ESTABLISHED:
    that massive Dirac is globally optimal;

NOT ESTABLISHED:
    that any real material can tune v arbitrarily at fixed Eg;

NOT ESTABLISHED:
    that HgCdTe is worse or better than the hypothetical family;

NOT ESTABLISHED:
    that lower equilibrium carrier column directly implies a proportional detector-noise reduction;

NOT ESTABLISHED:
    Auger generation scaling or kinematic closure;

NOT ESTABLISHED:
    SRH-limited behavior;

NOT ESTABLISHED:
    full electrical detector bandwidth;

NOT ESTABLISHED:
    novelty of the matched-optical-depth v^-2 carrier-column statement.
```

---

## 10. Why the generic parabolic comparator is not yet well posed

The original plan proposed comparing

```text
independent parabolic two-band absorber
vs
massive-Dirac absorber.
```

A generic parabolic model usually introduces

```text
m_e,
m_h,
and p_cv or v_cv
```

as separate parameters. If they are allowed to vary independently, one can lower DOS masses while increasing the optical matrix element by hand. The optimization is then underconstrained and cannot support a fundamental theorem.

Conversely, if the parabolic model is required to be the low-`k` limit of a self-consistent two-band `k.p` Hamiltonian, then

```math
m_D=\Delta/v^2
```

and the optical matrix element is controlled by the same `v`. That edge-parabolic model is not an independent electronic-structure class; it is the small-`k` approximation to the same massive-Dirac physics.

Therefore the cross-class comparison is currently

```text
CONDITIONAL:
    a fair parabolic comparator requires a multiband / oscillator-strength / sum-rule constraint
    that links its effective masses and interband matrix elements.
```

This is the exact missing microscopic assumption identified by the first hard derivation.

---

## 11. Focused prior-art screen

The optical ingredients are established:

- C. J. Tabert and J. P. Carbotte, **Phys. Rev. B 93, 085442 (2016)**, DOI `10.1103/PhysRevB.93.085442`: 3-D Dirac/Weyl interband optical response and its inverse-velocity scaling.
- J. D. Malcolm and E. J. Nicol, **Phys. Rev. B 92, 035118 (2015)**, DOI `10.1103/PhysRevB.92.035118`: Kane-model zero-field and magneto-optical conductivity relevant to HgCdTe-like Kane fermions.
- M. Ezawa, **Phys. Rev. B 110, 195437 (2024)**, DOI `10.1103/PhysRevB.110.195437`: analytical optical-conductivity treatment for Dirac models in arbitrary dimensions with momentum-dependent mass.

Established detector-material figures of merit based on absorption versus thermal generation remain mandatory novelty hazards and are recorded elsewhere in this branch.

A focused search performed on 2026-08-14 did **not** locate a direct statement of the specific combined result

```math
\Sigma_e=n_ed\propto v^{-2}
```

at matched 3-D massive-Dirac absorptance together with exact cancellation of equivalent Dirac-species degeneracy and the ballistic-transit invariance. That is **not enough to establish novelty**. A broader semiconductor `k.p`, oscillator-strength, infrared-detector, and Dirac-material literature audit is required before any priority language.

---

## 12. First hard-stop disposition

The founding yes/no question now has a restricted answer:

```text
YES, WITHIN THE IDEAL MASSIVE-DIRAC FAMILY:
    lower thermodynamic DOS can coexist with matched absorptance
    without an exact optical-depth or ballistic-transit compensation.

SURVIVING LEVER:
    Dirac velocity v, giving Sigma_e ~ v^-2.

NON-LEVER IN THIS MODEL:
    equivalent Dirac-species/valley degeneracy N_D after absorptance matching.

CROSS-CLASS PARABOLIC COMPARISON:
    not yet closed because generic parabolic masses and optical matrix elements
    cannot be treated as independent if the goal is a first-principles bound.
```

This is the first nontrivial consequence. Per the experiment protocol, **do not add Auger yet**.

## 13. Single next question

> Once the full multiband `k.p` / oscillator-strength constraints are imposed at fixed finite `E_g`, is the Dirac velocity `v` genuinely a free material-design lever, or is there a microscopic upper bound/tradeoff that limits the `Sigma_e ~ v^-2` gain?

That question must be answered before promoting the present scaling into a material-admissibility theorem.
