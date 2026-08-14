# Progress Log — Experiment 10: Room-Temperature LWIR Material Admissibility

## 2026-08-14 — branch initialization

Established target

```math
T=300\ \mathrm K,
\qquad
\lambda_c=10\ \mu\mathrm m,
\qquad
E_g\approx0.12398\ \mathrm{eV},
\qquad
E_g/(k_BT)\approx4.80.
```

Objective: derive a finite-gap band-structure admissibility theorem/bound rather than rank known materials.

---

## 2026-08-14 — matched massive-Dirac absorptance

Controlling file: `MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`.

Derived

```math
n_e\propto N_Dv^{-3},
\qquad
\alpha\propto N_Dv^{-1},
\qquad
d\propto v/N_D,
```

therefore

```math
\boxed{
\Sigma_e=n_ed\propto v^{-2},
\qquad
\Sigma_e\text{ independent of }N_D.
}
```

Ideal ballistic crossing time obeys

```math
\tau_{ball}\propto v^0.
```

At 10 um / 300 K the exact finite-gap Dirac carrier density is `1.8644x` the edge-parabolic estimate.

Disposition:

```text
MATCHED-ABSORPTANCE HIGH-v LEVER SURVIVES.
NOVELTY NOT ESTABLISHED.
```

---

## 2026-08-14 — Kane velocity freedom and microscopic resource bound

Controlling file: `KANE_VELOCITY_RESOURCE_BOUND_STEP_2026-08-14.md`.

Using

```math
E_P=2m_0P^2/\hbar^2,
\qquad
v^2=E_P/(3m_0),
```

```math
\Sigma_e\propto E_P^{-1}.
```

Generic upper-bound attempts based on the multiband effective-mass identity, global optical f-sum over a fixed detector energy window, and fixed remote-band energy failed to provide a material-independent upper bound on `v`.

For

```math
H(\mathbf k)=\sum_RH_Re^{i\mathbf k\cdot R},
```

```math
\boxed{
\|\hat v_i\|
\le\frac1\hbar\sum_R|R_i|\|H_R\|
\equiv V_i^{hop}.
}
```

Hence conditionally

```math
v\le V_{hop},
```

and

```math
\boxed{
\Sigma_e\ge C(T,E_g,A,r,n_b)/V_{hop}^2.
}
```

Disposition:

```text
FIRST MICROSCOPIC-RESOURCE-CONDITIONED DETECTOR INEQUALITY DERIVED.
NOVELTY NOT ESTABLISHED.
```

---

## 2026-08-14 — exact Auger kinematic closure

Controlling file:

`AUGER_KINEMATIC_CLOSURE_STEP_2026-08-14.md`

### Minimal process

Analyze ordinary phononless `eeh` Auger through inverse impact ionization

```text
e_0 -> e_1 + e_2 + h_3
```

in the exact particle-hole-symmetric massive-Dirac model

```math
\varepsilon(k)=\sqrt{\Delta^2+(\hbar vk)^2},
\qquad \Delta=E_g/2>0.
```

### Exact no-go

For arbitrary vectors `p,q`, derived strict subadditivity

```math
\boxed{
\varepsilon(\mathbf p+\mathbf q)
<\varepsilon(\mathbf p)+\varepsilon(\mathbf q).
}
```

Therefore, if normal crystal momentum is conserved,

```math
\mathbf k_0=\mathbf k_1+\mathbf k_2+\mathbf k_3,
```

then

```math
\varepsilon(k_0)
<\varepsilon(k_1)+\varepsilon(k_2)+\varepsilon(k_3),
```

so the simultaneous energy-conservation equality is impossible.

Result:

```math
\boxed{
\text{normal-momentum phononless }eeh\text{ Auger/impact ionization has empty kinematic support.}
}
```

By particle-hole symmetry, the mirror `hhe` channel is also closed.

### Exact mismatch

At fixed total momentum `K`, convexity makes equal momentum sharing the minimum-energy three-particle configuration. For hot energy

```math
E=\varepsilon(K),
```

obtained

```math
\boxed{
\Delta_A(E)
=3\varepsilon(K/3)-\varepsilon(K)
=\sqrt{E^2+2E_g^2}-E.
}
```

At fixed `E/E_g`, this contains **no `v`**.

This separates the two material-design resources:

```text
high v:
    Sigma_e ~ v^-2 at matched absorptance;

particle-hole-symmetric relativistic dispersion:
    exact ideal Auger closure.
```

Increasing `v` does not itself strengthen the dimensionless Auger kinematics.

### 10-um / 300-K mismatch witness

```text
E/Eg    Delta_A (meV)    Delta_A/kBT
1.5       69.62             2.69
2.0       55.73             2.16
3.0       39.26             1.52
5.0       24.32             0.94
10.0      12.34             0.48
```

These are off-shell mismatch scales, not ordinary thermal activation barriers.

### Massless limit

For `Delta -> 0`, closure becomes marginal and equality survives only for collinear co-directed momenta, consistent with established Dirac-material Auger theory.

### Prior-art disposition

Broad symmetry/Dirac Auger suppression is established by prior theory and HgCdTe-QW work. Mandatory comparators include:

```text
Alymov et al., Phys. Rev. B 97, 205411 (2018);
Alymov et al., ACS Photonics 7, 98–104 (2020);
But et al., Nature Photonics 13, 783–787 (2019);
Combescot & Combescot, Phys. Rev. B 37, 8781 (1988).
```

Therefore

```text
DIRAC/SYMMETRIC AUGER SUPPRESSION = NOT A NOVELTY CLAIM.
```

Possible surviving line is the detector-specific combination of high-`v` matched-absorptance thermodynamics with an explicit symmetry-breaking reopening criterion.

### Hard stop

Do not calculate an Auger rate yet.

Next question:

> Add the smallest particle-hole asymmetry, preferably `E_±(k)=Dk^2 ± sqrt(Delta^2+(hbar v k)^2)`, and derive the exact boundary at which the closed Auger phase space first reopens over the thermally relevant finite-energy window.
