# Post-Experiment-11 Theoretical Premise Screen — 2026-08-14

**Scope:** analytical/theoretical only  
**Purpose:** reject known/reducible premises before opening Experiment 12.  
**Disposition:** **TWO ADDITIONAL CANDIDATES REJECTED / EXPERIMENT 12 NOT OPENED**

Experiment 11 is closed by default as a novelty/manuscript path. This screen continues the repository protocol: derive the first nontrivial consequence, audit primary literature immediately, and kill the premise if the result is established or reducible to a generic theorem plus a detector example.

---

## Candidate 6 — irreducible random-alloy bandgap granularity

### Gedanken premise

In a substitutional alloy such as Hg_{1-x}Cd_xTe, a finite coarse-graining region containing `N` cation sites has binomial composition fluctuations even when the macroscopic mean composition is perfectly controlled:

```math
\operatorname{Var}(x_N)=\frac{x(1-x)}{N}.
```

Linearizing the local gap gives

```math
\delta E_g
\sim
\left|\frac{dE_g}{dx}\right|
\sqrt{\frac{x(1-x)}{N}}.
```

Question:

> As the target gap becomes very small, does unavoidable microscopic alloy granularity create a random-gap/sign-changing-gap floor even in a perfectly uniform macroscopic crystal?

### First consequence

Yes in principle: the relative disorder scale `delta Eg / |Eg|` grows as the mean gap approaches zero for a fixed coarse-graining volume. A sufficiently narrow nominal gap can therefore become dominated by local alloy fluctuations.

### Prior-art collision

This direction is already explicit in HgCdTe literature:

- Bazhenov et al., *Study of alloy disorder in (Hg,Cd)Te with the use of infrared photoluminescence*, Physica B 404, 5035–5037 (2009), attributes red-shifted photoluminescence to excitons localized by compositional fluctuations and extracts a fluctuation measure.
- Teppe et al., *Temperature-driven massless Kane fermions in HgCdTe crystals*, Nature Communications 7, 12576 (2016), states that composition tuning cannot finely tune the bandgap near the phase transition because of inherent Cd-concentration fluctuations.
- Krishtopenko, Antezza & Teppe, *Disorder-induced topological phase transition in HgCdTe crystals*, Physical Review B 106, 115203 (2022), explicitly models uncorrelated disorder from impurities and Cd-composition fluctuations and follows disorder-renormalized Kane mass / density of states.

The binomial coarse-graining formula is elementary alloy statistics, and its narrow-gap amplification is already qualitatively and quantitatively represented in the HgCdTe disorder literature.

### Disposition

```text
REJECT.
```

Useful as a materials-design warning, not a sufficiently new theoretical premise.

---

## Candidate 7 — finite-volume intrinsic carriers under exact neutrality

### Gedanken premise

Conventional intrinsic semiconductor statistics give

```math
n_i=\sqrt{N_cN_v}\exp[-E_g/(2k_BT)].
```

For a finite electrically isolated absorber with **exact** net charge neutrality, however, thermal electronic excitations must occur with

```math
N_e=N_h=n.
```

Question:

> When the expected bulk intrinsic carrier number is below unity, does exact neutrality change the finite-volume carrier law from the thermodynamic-limit `exp(-Eg/2kT)` behavior to a rare-pair `exp(-Eg/kT)` behavior?

### Exact classical canonical derivation

Let the conduction-electron and hole one-particle partition sums, measured from their respective band edges, be

```math
z_e=\sum_c e^{-\beta\epsilon_c},
\qquad
z_h=\sum_h e^{-\beta\epsilon_h}.
```

For `n` nondegenerate electron-hole pairs with no interactions,

```math
Z_n
=\frac{1}{(n!)^2}
\left[z_ez_h e^{-\beta E_g}\right]^n.
```

Define

```math
a=z_ez_h e^{-\beta E_g}.
```

Strict neutrality gives the full partition function

```math
\boxed{
Z=\sum_{n=0}^{\infty}\frac{a^n}{(n!)^2}
=I_0(2\sqrt a).
}
```

The exact mean pair number is

```math
\boxed{
\langle n\rangle
=a\frac{\partial\ln Z}{\partial a}
=\sqrt a\,
\frac{I_1(2\sqrt a)}{I_0(2\sqrt a)}.
}
```

Let

```math
N_i^{bulk}=\sqrt a.
```

In the continuum thermodynamic approximation,

```math
N_i^{bulk}
=V\sqrt{N_cN_v}\,e^{-E_g/(2k_BT)}
=n_iV.
```

Therefore

```math
\boxed{
\langle n\rangle
=N_i^{bulk}
\frac{I_1(2N_i^{bulk})}{I_0(2N_i^{bulk})}.
}
```

#### Rare-pair limit

For `N_i^{bulk} << 1`,

```math
\boxed{
\langle n\rangle
=(N_i^{bulk})^2+O[(N_i^{bulk})^4]
}
```

so

```math
\langle n\rangle
\propto
V^2 e^{-E_g/(k_BT)}.
```

#### Thermodynamic limit

For `N_i^{bulk} >> 1`,

```math
\frac{I_1(2N)}{I_0(2N)}
=1-\frac{1}{4N}+O(N^{-2}),
```

hence

```math
\boxed{
\langle n\rangle
=N_i^{bulk}-\frac14+O[(N_i^{bulk})^{-1}],
}
```

recovering the ordinary intrinsic bulk law.

The crossover occurs at order

```math
n_iV\sim1.
```

### Numerical witness

For the Experiment-10 10-um / 300-K massive-Dirac witness with

```text
n_i ~= 4.8421e15 cm^-3,
```

the volume containing one bulk-expected electron is approximately

```text
V ~= 2.065e-16 cm^3,
```

corresponding to a cube about

```text
59.1 nm
```

on a side.

At `N_i^bulk=0.1`, exact neutrality gives

```text
<n> = 0.0099503,
```

roughly ten times below the grand-canonical bulk expectation `0.1`.

At `N_i^bulk=1`,

```text
<n> = 0.697775.
```

At `N_i^bulk=10`,

```text
<n> = 9.74671,
```

already close to the thermodynamic limit.

### Prior-art collision

The mathematics is the standard canonical suppression of oppositely charged particles under exact charge conservation.

Ko, Koch, Lin, Redlich, Stephanov & Wang, *Kinetic Equation with Exact Charge Conservation*, Physical Review Letters 86, 5438 (2001), formulate a master equation for particles created or destroyed only in oppositely charged pairs. Their canonical rare-particle equilibrium and grand-canonical abundant-particle limit are precisely the structure above.

The canonical exact-charge literature gives the same modified-Bessel suppression factor

```math
I_1(2z)/I_0(2z).
```

Thus the semiconductor Bessel law is not a new statistical-mechanical theorem; it is a direct specialization of generic exact-charge canonical suppression.

### Detector-specific physical boundary

The strongest semiconductor interpretation also requires unusually strict isolation:

```text
ordinary electrical contacts provide charge reservoirs and move the carrier statistics toward an open/grand-canonical system;
charging energy becomes relevant in sufficiently small isolated structures;
quantum confinement alters z_e and z_h at tens-of-nanometers scales;
electron-hole Coulomb attraction/excitons modify the one-pair energy;
equilibrium carrier suppression alone does not determine dark-generation kinetics or detector noise.
```

The exact Bessel structure remains valid for the stated classical noninteracting model, but exploiting it as a photodetector would require additional device physics that is itself standard mesoscopic/quantum-dot territory.

### Disposition

```text
REJECT.
```

The finite-volume crossover is real and worth retaining as a technical note, but under the repository novelty rule it is a generic exact-conservation theorem plus a semiconductor specialization.

---

# Overall screen after Experiment 11

```text
Candidate 6 — random-alloy narrow-gap granularity: REJECT
Candidate 7 — exact-neutral finite-volume intrinsic carriers: REJECT
```

Experiment 12 should remain unopened.

## Updated screening lesson

Also reject premises whose apparent detector novelty is entirely generated by imposing a generic exact conservation law on a small absorber. A surviving next premise must derive its nontrivial constraint from the microscopic optical-to-electrical transduction itself, rather than from ensemble choice alone.
