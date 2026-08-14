# Current State — Experiment 10: Room-Temperature LWIR Material Admissibility

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** **MATCHED-ABSORPTANCE HIGH-v LEVER SURVIVES / CONDITIONAL MICROSCOPIC VELOCITY BOUND DERIVED / EXACT SYMMETRIC-DIRAC AUGER CLOSURE DERIVED / BROAD AUGER-SUPPRESSION NOVELTY EXCLUDED / NO MANUSCRIPT YET**

## Research objective

Derive from first principles the electronic-structure conditions a passive LWIR interband absorber must satisfy to approach HgCdTe-class intrinsic detector quality near 300 K without sacrificing useful temporal response.

Fixed target:

```math
T=300\ \mathrm K,
\qquad
\lambda_c=10\ \mu\mathrm m,
\qquad
E_g=0.1239841984\ \mathrm{eV},
\qquad
E_g/(k_BT)\approx4.796.
```

## Read first

1. `AUGER_KINEMATIC_CLOSURE_STEP_2026-08-14.md`
2. `KANE_VELOCITY_RESOURCE_BOUND_STEP_2026-08-14.md`
3. `MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`
4. `PROGRESS_LOG.md`

---

# Result A — matched-absorptance thermodynamic lever

For the intrinsic isotropic 3-D massive-Dirac model

```math
H=\hbar v\tau_x\boldsymbol\sigma\cdot\mathbf k+\Delta\tau_z,
\qquad \Delta=E_g/2,
```

with `N_D` equivalent species,

```math
n_e\propto N_Dv^{-3},
\qquad
\alpha\propto N_Dv^{-1}.
```

Matched ideal single-pass absorptance requires

```math
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

The ideal ballistic crossing time remains

```math
\boxed{\tau_{ball}\propto v^0.}
```

At 10 um / 300 K the exact finite-gap carrier density is `1.8644x` the edge-parabolic estimate; retain the exact dispersion in quantitative work.

---

# Result B — microscopic velocity resource

Using the simplified Kane normalization

```math
E_P=2m_0P^2/\hbar^2,
\qquad
v^2=E_P/(3m_0),
```

```math
\boxed{\Sigma_e\propto E_P^{-1}.}
```

No useful material-independent upper bound on large `v` was obtained from the multiband effective-mass identity, global optical f-sum over a fixed detector energy window, or remote-band energy separation alone.

For a Wannier/tight-binding Hamiltonian

```math
H(\mathbf k)=\sum_R H_Re^{i\mathbf k\cdot R},
```

the velocity operator obeys

```math
\boxed{
\|\hat v_i\|
\le\frac1\hbar\sum_R|R_i|\|H_R\|
\equiv V_i^{hop}.
}
```

Thus conditionally

```math
\boxed{v\le V_{hop},}
```

and the matched thermal carrier column satisfies

```math
\boxed{
\Sigma_e\ge C(T,E_g,A,r,n_b)/V_{hop}^2.
}
```

This is a microscopic-resource-conditioned detector bound, not a universal numerical semiconductor limit.

---

# Result C — exact symmetric massive-Dirac Auger closure

Controlling derivation:

`AUGER_KINEMATIC_CLOSURE_STEP_2026-08-14.md`

Use the positive quasiparticle dispersion

```math
\varepsilon(k)=\sqrt{\Delta^2+(\hbar vk)^2},
\qquad \Delta>0.
```

For arbitrary momenta `p,q`,

```math
\boxed{
\varepsilon(\mathbf p+\mathbf q)
<\varepsilon(\mathbf p)+\varepsilon(\mathbf q).
}
```

Therefore for normal-momentum impact ionization

```text
e_0 -> e_1 + e_2 + h_3
```

with

```math
\mathbf k_0=\mathbf k_1+\mathbf k_2+\mathbf k_3,
```

one necessarily has

```math
\varepsilon(k_0)
<\varepsilon(k_1)+\varepsilon(k_2)+\varepsilon(k_3),
```

so exact energy conservation cannot also hold.

Hence, within the exact symmetric two-band model,

```math
\boxed{
\text{normal-momentum phononless }eeh\text{ Auger/impact ionization has empty kinematic support.}
}
```

The particle-hole mirror `hhe` channel is closed as well.

## Exact closure margin

At fixed total momentum `K`, strict convexity gives the minimum three-particle energy at equal momentum sharing. For hot quasiparticle energy

```math
E=\varepsilon(K),
```

the minimum mismatch is

```math
\boxed{
\Delta_A(E)
=3\varepsilon(K/3)-\varepsilon(K)
=\sqrt{E^2+2E_g^2}-E>0.
}
```

At fixed `E/E_g`, **`v` cancels completely**.

Thus the two favorable resources are distinct:

```text
large v
    -> lower matched-absorptance thermal carrier column, Sigma_e ~ v^-2;

particle-hole-symmetric massive-Dirac shape
    -> exact ideal direct Auger kinematic closure.
```

Increasing `v` by itself does not cause the Auger closure; it only rescales momentum space.

For the 10-um / 300-K target:

```text
E/Eg    Delta_A (meV)    Delta_A/kBT
1.5       69.62             2.69
2.0       55.73             2.16
3.0       39.26             1.52
5.0       24.32             0.94
10.0      12.34             0.48
```

These are off-shell mismatch scales, not ordinary activation energies.

## Massless limit

For `Delta -> 0`, strict closure becomes marginal: equality is possible only for collinear, co-directed momenta. This agrees with established Dirac-material Auger theory.

---

# Prior-art boundary

Broad claims that symmetric/quasi-relativistic Dirac/Kane dispersion suppresses Auger recombination are established and unavailable as novelty.

Mandatory comparators:

```text
Alymov et al., Phys. Rev. B 97, 205411 (2018), DOI 10.1103/PhysRevB.97.205411;
Alymov et al., ACS Photonics 7, 98–104 (2020), DOI 10.1021/acsphotonics.9b01099;
But et al., Nature Photonics 13, 783–787 (2019), DOI 10.1038/s41566-019-0496-1;
Combescot & Combescot, Phys. Rev. B 37, 8781 (1988), DOI 10.1103/PhysRevB.37.8781.
```

Current possible contribution is only the narrower detector-specific synthesis:

```text
matched absorptance + exact finite-gap statistics + microscopic v resource
+ quantitative symmetry-breaking/Auger reopening condition.
```

```text
NOVELTY NOT ESTABLISHED.
```

---

# Important real-material boundary

Real bulk HgCdTe is not the exact symmetric two-band model. Heavy-hole and remote bands, disorder, phonons, finite linewidth, and many-body effects reopen Auger channels.

Do not state that bulk HgCdTe has zero Auger recombination.

---

# NEXT ACTION

Do not evaluate an empirical Auger coefficient yet.

Add the **smallest controlled particle-hole asymmetry** and derive the exact reopening boundary. Preferred first perturbation:

```math
E_\pm(k)
=Dk^2\pm\sqrt{\Delta^2+(\hbar vk)^2}.
```

Question:

> What dimensionless asymmetry parameter is required to close the mismatch `Delta_A(E)` and create nonempty Auger phase space over the thermally relevant energy window at `E_g/k_BT ~= 4.8`?

Only after the reopening condition is known should Coulomb matrix elements and finite Auger rates be introduced.
