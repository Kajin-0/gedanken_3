# Current State — Experiment 10: Room-Temperature LWIR Material Admissibility

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** **MATCHED-ABSORPTANCE HIGH-v LEVER SURVIVES / CONDITIONAL MICROSCOPIC VELOCITY BOUND DERIVED / EXACT SYMMETRIC-DIRAC AUGER CLOSURE DERIVED / FINITE-ASYMMETRY REOPENING LAW DERIVED / BROAD AUGER-THRESHOLD NOVELTY EXCLUDED / NO MANUSCRIPT YET**

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

1. `AUGER_ASYMMETRY_REOPENING_STEP_2026-08-14.md`
2. `AUGER_KINEMATIC_CLOSURE_STEP_2026-08-14.md`
3. `KANE_VELOCITY_RESOURCE_BOUND_STEP_2026-08-14.md`
4. `MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`
5. `PROGRESS_LOG.md`

---

# Result A — matched-absorptance thermodynamic lever

For the intrinsic isotropic finite-gap massive-Dirac family,

```math
n_e\propto N_Dv^{-3},
\qquad
\alpha\propto N_Dv^{-1},
\qquad
d\propto v/N_D.
```

Therefore

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

At 10 um / 300 K the exact finite-gap carrier density is `1.8644x` the edge-parabolic estimate; retain exact nonparabolicity in quantitative work.

---

# Result B — microscopic velocity resource

Using the simplified Kane normalization

```math
E_P=2m_0P^2/\hbar^2,
\qquad
v^2=E_P/(3m_0),
```

```math
\Sigma_e\propto E_P^{-1}.
```

No useful material-independent upper bound on large `v` was obtained from the multiband effective-mass identity, global optical f-sum over a fixed detector energy window, or remote-band energy separation alone.

For a Wannier/tight-binding Hamiltonian,

```math
\boxed{
\|\hat v_i\|
\le\frac1\hbar\sum_R|R_i|\|H_R\|
\equiv V_i^{hop},
}
```

so conditionally

```math
\boxed{v\le V_{hop}}
```

and

```math
\boxed{\Sigma_e\ge C(T,E_g,A,r,n_b)/V_{hop}^2.}
```

This is a microscopic-resource-conditioned detector bound, not a universal numerical semiconductor limit.

---

# Result C — exact symmetric massive-Dirac Auger closure

For

```math
\varepsilon(k)=\sqrt{\Delta^2+(\hbar vk)^2},
\qquad\Delta=E_g/2>0,
```

strict subadditivity implies that normal-momentum phononless

```text
e_0 -> e_1 + e_2 + h_3
```

cannot satisfy exact energy and momentum conservation. The inverse `eeh` Auger channel and particle-hole mirror `hhe` channel therefore have empty exact kinematic support in the symmetric two-band model.

The exact minimum mismatch at hot energy `E` is

```math
\boxed{
\Delta_A(E)=\sqrt{E^2+2E_g^2}-E.
}
```

At fixed `E/E_g`, `v` cancels. Thus high `v` and particle-hole symmetry are distinct favorable resources.

Broad Dirac/symmetric-dispersion Auger suppression is established prior art and is not a novelty claim.

---

# Result D — particle-hole-asymmetry reopening boundary

Controlling file:

`AUGER_ASYMMETRY_REOPENING_STEP_2026-08-14.md`

Add the scalar asymmetry

```math
E_\pm(k)=Dk^2\pm\sqrt{\Delta^2+(\hbar vk)^2}.
```

Define

```math
q=\hbar vk/\Delta,
\qquad
s(q)=\sqrt{1+q^2},
```

```math
\boxed{
\beta=\frac{D\Delta}{\hbar^2v^2}.
}
```

The near-edge normalized inverse-mass asymmetry is

```math
\boxed{
\mathcal A_m
=\frac{|m_e^{-1}-m_h^{-1}|}
{m_e^{-1}+m_h^{-1}}
=2|\beta|.
}
```

For the favorable `eeh` sign, the exact fixed-total-momentum reopening boundary reduces to

```math
\boxed{
\beta_c(q_0)
=
\min_{0\le x\le q_0/2}
\frac{2s(x)+s(q_0-2x)-s(q_0)}
{2(q_0-x)^2}.
}
```

At an interior threshold the two final electrons have equal collinear momentum `x`, while the hole has `z=q_0-2x`.

The low-`q` boundary branch changes to the interior branch at

```math
q_*=\sqrt{2+2\sqrt2}\approx2.19737,
```

```math
\beta_*=(\sqrt2-1)/2\approx0.207107.
```

## Weak-asymmetry law

For `|beta| -> 0`, the threshold lies at large momentum. The optimal asymptotic partition is

```math
q_1=q_2\to q_0/4,
\qquad
q_3\to q_0/2,
```

and

```math
\boxed{
\beta_c(q_0)\sim4/q_0^3.
}
```

Hence

```math
\boxed{
q_{th}\sim(4/|\beta|)^{1/3}.
}
```

The hot-electron kinetic threshold above the conduction edge is

```math
K_{th}
=\Delta\left[s(q_{th})+|\beta|q_{th}^2-1\right],
```

so asymptotically

```math
\boxed{
K_{th}\sim E_g\,\mathcal A_m^{-1/3}.
}
```

At fixed temperature,

```math
\boxed{
K_{th}/k_BT
\sim(E_g/k_BT)\mathcal A_m^{-1/3}.
}
```

This is a derived reduced-model symmetry-tolerance law. Novelty is not established.

## Exact 10-um / 300-K witness

```text
A_m      beta       q_th      K_th/kBT
0.40     0.200      2.236       5.873
0.20     0.100      3.052       7.536
0.10     0.050      4.019       9.470
0.04     0.020      5.635      12.848
0.02     0.010      7.199      16.273
0.01     0.005      9.149      20.675
```

Inverting the exact relation:

```text
required K_th/kBT    max A_m     reduced-model m_h/m_e
8                     0.1671       1.401
10                    0.08476      1.185
12                    0.04900      1.103
15                    0.02536      1.052
```

Thus the chosen scalar-asymmetry model requires approximately

```math
\boxed{\mathcal A_m\lesssim0.0848}
```

to place the direct-channel threshold above `10 k_BT` at 10 um / 300 K.

Do not interpret the edge-mass ratio as universal. The true physical requirement is sufficiently small **finite-momentum dispersion asymmetry over the Auger-active momentum window**.

Reproducible calculation:

`numerics/auger_asymmetry_threshold.py`

---

# Prior-art boundary

Established territory includes:

```text
Dirac/symmetric-dispersion Auger suppression;
large Auger thresholds near Dirac-like HgCdTe-QW regimes;
threshold dependence on nonparabolicity and electron-hole symmetry;
full eight-band Kane calculations of HgCdTe-QW Auger thresholds.
```

Mandatory adjacent papers include Alymov et al. ACS Photonics 2020, Morozov et al. ACS Photonics 2021, Aleshkin et al. JPCM 2019, Alymov et al. PRB 2018, and classical Combescot threshold work.

The exact cube-root law above has not been established as new by the present focused audit.

```text
NOVELTY NOT ESTABLISHED.
```

---

# Important real-material boundary

Real bulk HgCdTe is not the exact symmetric two-band model. Heavy-hole and remote bands, disorder, phonons, finite linewidth, and many-body effects can reopen direct or assisted Auger channels.

The scalar `Dk^2` model is a controlled analytical probe of symmetry tolerance, not a complete bulk-HgCdTe model.

---

# NEXT ACTION

Do not rank candidate materials and do not jump directly to an empirical Auger coefficient.

The next question is now:

> Given the exact reopening threshold, what is the leading near-threshold thermal/phase-space scaling of the direct Auger rate, and can it be combined with `Sigma_e ~ v^-2` to produce a detector-level room-temperature admissibility inequality before model-dependent Coulomb prefactors dominate?

Introduce only the minimum screened-Coulomb structure required to determine universal threshold exponents. Keep matrix-element magnitude separate from the kinematic/thermal factor.
