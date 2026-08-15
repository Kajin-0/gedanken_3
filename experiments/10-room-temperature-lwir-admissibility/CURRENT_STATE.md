# Current State — Experiment 10: Room-Temperature LWIR Material Admissibility

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** **JOINT MATCHED-OPTICS / HIGH-v / MULTIBAND-AUGER ADMISSIBILITY STRUCTURE NOW DERIVED IN CONTROLLED MODELS / EXACT-CLOSURE CARRIER-COLUMN LOWER BOUND FOUND / DEDICATED NOVELTY AUDIT REQUIRED / NO MANUSCRIPT YET**

## Objective

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

1. `HEAVY_HOLE_AUGER_RATE_AND_JOINT_BOUND_STEP_2026-08-14.md`
2. `THIRD_BAND_HEAVY_HOLE_AUGER_ESCAPE_STEP_2026-08-14.md`
3. `RADIATIVE_BOUNDARY_ADMISSIBILITY_STEP_2026-08-14.md`
4. `AUGER_NEAR_THRESHOLD_RATE_STEP_2026-08-14.md`
5. `AUGER_ASYMMETRY_REOPENING_STEP_2026-08-14.md`
6. `AUGER_KINEMATIC_CLOSURE_STEP_2026-08-14.md`
7. `KANE_VELOCITY_RESOURCE_BOUND_STEP_2026-08-14.md`
8. `MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`
9. `PROGRESS_LOG.md`

---

# Result A — matched-absorptance high-v law

For the intrinsic finite-gap massive-Dirac family,

```math
n_e\propto N_Dv^{-3},
\qquad
\alpha\propto N_Dv^{-1},
\qquad
d\propto v/N_D,
```

therefore

```math
\boxed{\Sigma_e=n_ed=C/v^2.}
```

Equivalent-species degeneracy cancels from `Sigma_e`; ideal ballistic crossing time is `v^0`.

For the standard 10-um/300-K numerical witness (`A=0.90`, `r=1.2`, `n_b=3.5`),

```math
C=1.06668\times10^{29}\ \mathrm{m^{-2}(m/s)^2}.
```

---

# Result B — microscopic lattice velocity resource

For a Wannier/tight-binding Hamiltonian,

```math
\boxed{
\|\hat v_i\|
\le\frac1\hbar\sum_R|R_i|\|H_R\|
\equiv V_i^{hop}.
}
```

Hence conditionally

```math
\boxed{v\le V_{hop},}
```

and

```math
\boxed{\Sigma_e\ge C/V_{hop}^2.}
```

Generic effective-mass sums, fixed-window optical f-sums, and remote-band energy separation alone did not produce a chemistry-independent upper `v`.

---

# Result C — two-band Auger structure

For exact particle-hole-symmetric massive-Dirac dispersion,

```math
\varepsilon(k)=\sqrt{\Delta^2+(\hbar vk)^2},
\qquad\Delta=E_g/2,
```

normal-momentum phononless `eeh` and `hhe` Auger channels are exactly closed.

The minimum mismatch is

```math
\boxed{\Delta_A(E)=\sqrt{E^2+2E_g^2}-E.}
```

Adding scalar particle-hole asymmetry

```math
E_\pm=Dk^2\pm\sqrt{\Delta^2+(\hbar vk)^2}
```

gives the weak-asymmetry reopening law

```math
\boxed{K_{th}\sim E_g\mathcal A_m^{-1/3},}
```

where

```math
\mathcal A_m=2|D\Delta/(\hbar^2v^2)|.
```

At 10 um / 300 K, this toy model needs approximately `A_m <= 0.0848` for `K_th >= 10 kBT`.

The interior threshold phase-space shell obeys

```math
\boxed{\Phi_{3body}\propto(K-K_{th})^2,}
```

while a microscopic matrix-element zero can add powers.

---

# Result D — complete external optical boundary is the invariant radiative side

Matching useful front-side absorptance alone is insufficient. The theorem-grade comparison must match the complete external mode-resolved absorptance:

```math
\boxed{\mathcal A_\mu^{(A)}=\mathcal A_\mu^{(B)}}
```

for all external carrier-coupled optical channels.

At thermal equilibrium,

```math
\boxed{\Phi_{abs}^{ext}=\Phi_{em}^{ext}=\Phi_0.}
```

Internal radiative recombination is not invariant because photon recycling can change the internal event count at fixed external emission.

Define

```math
\boxed{
\Xi_A^{ext}
=\frac{G_A^{gen}+R_A^{rec}}
{\Phi_{abs}^{ext}+\Phi_{em}^{ext}}.
}
```

At equilibrium,

```math
\boxed{\Xi_A^{ext}=G_A/\Phi_0.}
```

For the ideal hemispherical step absorber at 10 um / 300 K,

```text
Phi_0 = 4.89777e17 cm^-2 s^-1
q Phi_0 = 0.0784710 A/cm^2
```

and the direct-Auger/radiative activation-parity line is

```math
\boxed{K_{th}=E_g/2.}
```

---

# Result E — exact heavy-hole third-band opening theorem

Add

```math
E_{hh}(k)
=\Delta+\delta_{hh}
+\frac{\hbar^2k^2}{2M_{hh}}.
```

Define

```math
\rho=\frac{M_{hh}v^2}{\Delta},
\qquad
\eta=\frac{\delta_{hh}}{\Delta}.
```

For normal-momentum CCCH / Auger-1,

```math
\boxed{
\rho\le2(1+\eta)
\Longleftrightarrow
\text{no finite-energy CCCH support}.
}
```

Equivalently,

```math
\boxed{
M_{hh}v^2\le2(\Delta+\delta_{hh}).
}
```

If the inequality is violated, there is one unique finite threshold. Near the opening boundary

```math
\rho_c=2(1+\eta),
```

```math
\boxed{
q_{th}\sim\frac{3}{\rho-\rho_c},
\qquad
K_{th}^{hh}/\Delta\sim\frac{3}{\rho-\rho_c}.
}
```

For `M_hh -> infinity`,

```math
\boxed{K_{th}^{hh}\to E_g+\delta_{hh}.}
```

Thus a flat touching heavy-hole band collapses the threshold to `E_g`, reproducing the conventional low-threshold Auger-1 direction.

---

# NEW Result F — heavy-hole threshold phase space does not diverge with spectator DOS

For a fixed hot electron, eliminate heavy-hole momentum and expand the six-dimensional final-state energy around the constrained threshold minimum.

With

```math
a_\parallel=(1-u^2)^{3/2},
\qquad
a_\perp=\sqrt{1-u^2},
```

the exact constrained Hessian determinant is

```math
\boxed{
\det H
=
a_\parallel\left(a_\parallel+\frac{2}{\rho}\right)
\left[
a_\perp\left(a_\perp+\frac{2}{\rho}\right)
\right]^2.
}
```

Define the threshold-envelope opening factor

```math
\boxed{
\gamma
=1-\frac{u_{th}}
{q_{th}/\sqrt{1+q_{th}^2}}.
}
```

Then

```math
\boxed{
\Phi_{hh}^{(q)}(K)
\propto
\frac{\gamma^2}{\sqrt{\det H}}
(K-K_{th}^{hh})^2.
}
```

In the flat-heavy-hole limit,

```math
\boxed{
\det H\to1,
\qquad
\gamma\to1.
}
```

Therefore the normalized local threshold phase-space coefficient remains finite. There is **no universal independent `M_hh^(3/2)` divergence** in the threshold event rate simply from the heavy-hole DOS.

The heavy band's principal kinematic damage is threshold collapse, not a mandatory divergent local phase-space coefficient.

---

# NEW Result G — near exact CCCH closure the rate is doubly suppressed

Let

```math
\delta\rho=\rho-\rho_c>0.
```

Then

```math
\gamma\sim(\delta\rho)^2/6,
```

```math
\det H
\sim
\frac{256}{243\rho_c^3}(\delta\rho)^5,
```

and hence

```math
\boxed{
\frac{\gamma^2}{\sqrt{\det H}}
\sim
\frac{\sqrt3\,\rho_c^{3/2}}{64}
(\delta\rho)^{3/2}.
}
```

Together with

```math
K_{th}^{hh}\sim3\Delta/\delta\rho,
```

the smooth-matrix weak-screening thermal rate near closure has the schematic structure

```math
\boxed{
G_{hh}^{area}
\propto
v^{-4}
(\delta\rho)^{3/2}
\exp[-(\Delta+3\Delta/\delta\rho)/(k_BT)].
}
```

Exact closure is therefore approached through both an essential thermal suppression and a vanishing phase-space prefactor.

---

# NEW Result H — open heavy-hole channel retains the high-v algebraic lever

At fixed dimensionless `rho`, `eta`, and normalized geometry,

```math
G_{hh}^{area}\propto |V_{th}^{hh}|^2v^{-8}
```

before Coulomb momentum dependence.

For a weakly screened Coulomb interaction with threshold transfer `Q_th ~ 1/v`,

```math
|V_{th}^{hh}|^2\propto v^4,
```

so

```math
\boxed{
G_{hh}^{area}
\propto
\mathcal P_{hh}(\rho,\eta)
v^{-4}
\exp[-(\Delta+K_{th}^{hh})/(k_BT)]
}
```

up to dielectric, spinor, exchange, screening, thermal-power, and optical-depth factors.

For fixed physical `M_hh`, increasing `v` increases `rho`, but `P_hh` tends to a finite constant in the flat-heavy-hole limit. Thus heavy-hole DOS does not automatically cancel the `v^-4` algebraic benefit.

---

# NEW Result I — exact CCCH closure imposes a matched-carrier-column floor

This is now the strongest clean Experiment-10 theorem candidate.

Matched absorptance gives

```math
\Sigma_e=C/v^2.
```

Exact CCCH closure gives

```math
v^2\le\frac{2(\Delta+\delta_{hh})}{M_{hh}}.
```

Therefore

```math
\boxed{
\Sigma_e
\ge
C\frac{M_{hh}}{2(\Delta+\delta_{hh})}
=
C\frac{M_{hh}}{E_g+2\delta_{hh}}.
}
```

This is an explicit thermodynamic/kinematic conflict: lowering the matched thermal carrier population through large `v` is limited by the mass and offset of a nearby spectator band if exact Auger-1 closure is demanded.

Including the lattice velocity resource gives

```math
\boxed{
\Sigma_e
\ge
\max\!\left[
\frac{C}{V_{hop}^2},
C\frac{M_{hh}}{2(\Delta+\delta_{hh})}
\right].
}
```

For a touching spectator band at the standard witness:

```text
M_hh/m0     v_c (m/s)      minimum Sigma_e for exact CCCH closure (cm^-2)
0.50        2.088e5         2.446e14
0.20        3.302e5         9.783e13
0.10        4.670e5         4.892e13
0.05        6.604e5         2.446e13
0.02        1.044e6         9.783e12
```

A touching `0.5 m0` spectator therefore forces a carrier-column floor about 23 times above the earlier `v=1e6 m/s` witness if exact CCCH closure is required.

Reproducible calculation:

`numerics/heavy_hole_rate_and_joint_bound.py`

---

# Prior-art boundary

Established and unavailable as broad novelty:

```text
classical thresholded direct-gap Auger theory;
CCCH/Auger-1 involving heavy holes in bulk HgCdTe;
heavy-hole mass dependence of conventional Auger formulas;
Kane overlap zeros and non-universal pre-exponential powers;
band-structure engineering of Auger thresholds in HgCdTe quantum wells;
alpha/G_th and alpha sqrt(tau) infrared-detector material figures of merit;
radiative detailed balance and photon recycling.
```

A focused search did not establish prior art for the specific composed exact-closure inequality

```math
\Sigma_e\ge C M_{hh}/[2(\Delta+\delta_{hh})],
```

but **novelty is not established** by that search.

---

# NEXT ACTION

Do not add another physical mechanism yet.

Perform a dedicated adversarial prior-art audit of the **joint theorem structure**:

```text
complete external optical boundary
+ matched-absorptance finite-gap carrier scaling
+ microscopic velocity resource
+ finite-k electron-hole symmetry
+ spectator-band CCCH closure
-> lower bound on matched thermal carrier column / admissible band-structure region.
```

If that synthesis survives, compress Experiment 10 into theorem/corollary form and then test the minimum additional channels required to break it. If it does not survive, close the branch rather than accumulating more phenomenology.