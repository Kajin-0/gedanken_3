# Current State — Experiment 10: Room-Temperature LWIR Material Admissibility

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** **MATCHED-ABSORPTANCE HIGH-v LEVER / MICROSCOPIC VELOCITY RESOURCE / TWO-BAND AUGER CLOSURE / ASYMMETRY REOPENING / THRESHOLDED DIRECT-AUGER RATE / EXTERNAL RADIATIVE FLOOR / MINIMAL THIRD-BAND HEAVY-HOLE ESCAPE ALL DERIVED IN CONTROLLED MODELS / FIRST DIRECT HIGH-v MULTIBAND TRADEOFF FOUND / NOVELTY NOT ESTABLISHED / NO MANUSCRIPT YET**

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

1. `THIRD_BAND_HEAVY_HOLE_AUGER_ESCAPE_STEP_2026-08-14.md`
2. `RADIATIVE_BOUNDARY_ADMISSIBILITY_STEP_2026-08-14.md`
3. `AUGER_NEAR_THRESHOLD_RATE_STEP_2026-08-14.md`
4. `AUGER_ASYMMETRY_REOPENING_STEP_2026-08-14.md`
5. `AUGER_KINEMATIC_CLOSURE_STEP_2026-08-14.md`
6. `KANE_VELOCITY_RESOURCE_BOUND_STEP_2026-08-14.md`
7. `MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`
8. `PROGRESS_LOG.md`

---

# Closed result A — matched-absorptance high-v lever

For the intrinsic isotropic finite-gap massive-Dirac family,

```math
n_e\propto N_Dv^{-3},
\qquad
\alpha\propto N_Dv^{-1},
\qquad
d\propto v/N_D,
```

so

```math
\boxed{\Sigma_e=n_ed\propto v^{-2}}
```

with equivalent-species cancellation. Ideal ballistic crossing time remains `v^0`.

At 10 um / 300 K, exact finite-gap carrier density is `1.8644x` the edge-parabolic estimate.

---

# Closed result B — microscopic velocity resource

For a lattice/Wannier Hamiltonian,

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
\boxed{\Sigma_e\ge C/V_{hop}^2.}
```

No chemistry-independent numerical upper `v` follows from the low-energy effective-mass sum, fixed-window optical f-sum, or remote-band energy separation alone.

---

# Closed result C — exact symmetric two-band direct-Auger closure

For

```math
\varepsilon(k)=\sqrt{\Delta^2+(\hbar vk)^2},
\qquad\Delta=E_g/2>0,
```

normal-momentum phononless `eeh` and `hhe` Auger channels have empty exact support in the symmetric two-band model.

The minimum mismatch is

```math
\boxed{\Delta_A(E)=\sqrt{E^2+2E_g^2}-E.}
```

At fixed `E/Eg`, `v` cancels. High `v` and electron-hole symmetry are distinct resources.

---

# Closed result D — scalar particle-hole-asymmetry reopening

For

```math
E_\pm=Dk^2\pm\sqrt{\Delta^2+(\hbar vk)^2},
```

with

```math
\mathcal A_m=2|D\Delta/(\hbar^2v^2)|,
```

the weak-asymmetry threshold obeys

```math
\boxed{K_{th}\sim E_g\mathcal A_m^{-1/3}.}
```

At 10 um / 300 K, the scalar model requires approximately

```math
\boxed{\mathcal A_m\lesssim0.0848}
```

to place the direct threshold above `10 kBT`.

This is not a universal edge-mass rule; the actual requirement is finite-momentum electron-hole symmetry over the Auger-active window.

---

# Closed result E — thresholded two-band direct-Auger rate

For the interior threshold branch,

```math
\boxed{\Phi_{3body}\propto(K-K_{th})^2.}
```

If `|V_eff|^2 ~ (K-K_th)^nu`, then

```math
\boxed{\Gamma_{II}\propto(K-K_{th})^{2+\nu}.}
```

Detailed balance gives

```math
\boxed{
G_A^{vol}\propto T^{3+\nu}e^{-(E_g/2+K_{th})/(k_BT)}.
}
```

For the minimal static screened-Coulomb model at matched absorptance,

```math
\boxed{
G_A^{area}
\propto
\frac{|S_{cv}|^2}{\epsilon_r^2}
\frac{v^{-4}}{(\mathcal Q_{th}^2+s_\kappa^2)^2}
\left(\frac{k_BT}{\Delta}\right)^{3+\nu}
\exp[-(\Delta+K_{th})/(k_BT)].
}
```

Weak-screening/intrinsic-Debye large-`v` behavior tends toward `v^-4`.

---

# Closed result F — complete external optical boundary fixes the unavoidable radiative exchange

Matching useful scene absorptance alone is insufficient. Match the complete external mode-resolved optical boundary:

```math
\boxed{
\mathcal A_\mu^{(A)}=\mathcal A_\mu^{(B)}
}
```

for every external optical channel relevant to active-carrier exchange.

For reciprocal passive structures this fixes external thermal emission and external background absorption. At equilibrium,

```math
\boxed{
\Phi_{abs}^{ext}=\Phi_{em}^{ext}=\Phi_0.
}
```

Internal radiative recombination is not invariant under photon recycling. Use irreversible external optical traffic in the low-frequency/coarse-grained carrier-number problem.

For the ideal hemispherical step absorber at 10 um / 300 K,

```text
Phi_0 = 4.89777e17 cm^-2 s^-1
q Phi_0 = 0.0784710 A/cm^2
```

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

The direct-channel admissibility target is `Xi_A^ext <= 1`.

The direct-Auger/radiative activation ratio is

```math
\boxed{
\Xi_A^{ext}\propto_{exp}
\exp[-(K_{th}-E_g/2)/(k_BT)].
}
```

The activation-parity line is

```math
\boxed{K_{th}=E_g/2.}
```

---

# NEW closed result G — minimal heavy-hole third-band escape

Controlling derivation:

`THIRD_BAND_HEAVY_HOLE_AUGER_ESCAPE_STEP_2026-08-14.md`

Reproducible calculation:

`numerics/third_band_heavy_hole_threshold.py`

Keep the active conduction/light-hole massive-Dirac pair and add a heavy-hole-like hole branch

```math
E_{hh}(k)
=\Delta+\delta_{hh}
+\frac{\hbar^2k^2}{2M_{hh}}.
```

Define

```math
\boxed{
\rho=\frac{M_{hh}v^2}{\Delta}
=\frac{M_{hh}}{m_D},
\qquad
m_D=\frac{\Delta}{v^2},
}
```

and

```math
\boxed{\eta=\delta_{hh}/\Delta.}
```

Analyze inverse CCCH impact ionization

```text
e_0 -> e_1 + e_2 + h_hh.
```

At fixed total dimensionless momentum `q`, convexity makes the minimum final state collinear with equal electron momenta. Using a common dimensionless group velocity `u`,

```math
x(u)=\frac{u}{\sqrt{1-u^2}},
\qquad
z(u)=\rho u,
```

```math
q(u)=\frac{2u}{\sqrt{1-u^2}}+\rho u,
```

and

```math
\mathcal F(u)
=\frac{2}{\sqrt{1-u^2}}
+1+\eta
+\frac{\rho u^2}{2}.
```

Define mismatch

```math
D(q)=\mathcal F(q)-\sqrt{1+q^2}.
```

The envelope theorem gives

```math
\boxed{D'(q)<0}
```

for all `q>0`. Also

```math
D(0)=2+\eta>0,
```

and

```math
\boxed{
\lim_{q\to\infty}D(q)
=1+\eta-\rho/2.
}
```

Therefore the exact three-band kinematic classification is

```math
\boxed{
\rho<2(1+\eta)
\Rightarrow
\text{CCCH closed at all finite energies},
}
```

```math
\boxed{
\rho=2(1+\eta)
\Rightarrow
\text{asymptotically marginal only},
}
```

```math
\boxed{
\rho>2(1+\eta)
\Rightarrow
\text{one unique finite CCCH threshold}.
}
```

Equivalently, exact finite-energy closure requires

```math
\boxed{
M_{hh}v^2
\le
2(\Delta+\delta_{hh}).
}
```

This is the first direct multiband conflict with the high-`v` thermodynamic lever.

---

# Result H — high-v and spectator-band protection compete

The matched thermal column wants

```math
\Sigma_e\propto v^{-2}.
```

But at fixed spectator-band mass and offset,

```math
\rho=M_{hh}v^2/\Delta\propto v^2.
```

Thus increasing `v` eventually reopens the heavy-hole CCCH channel unless the spectator band becomes lighter or moves farther away.

Exact closure can be written

```math
\boxed{
v\le v_c^{hh}
=\sqrt{\frac{2(\Delta+\delta_{hh})}{M_{hh}}}.}
```

For a touching spectator band (`delta_hh=0`) at 10 um,

```math
\boxed{M_{hh}^{max}=E_g/v^2.}
```

Numerically:

```text
v (m/s)       M_hh^max / m0
5.0e5           0.08723
1.0e6           0.02181
1.07e6          0.01905
2.0e6           0.005452
3.0e6           0.002423
```

A genuinely heavy touching band is therefore on the open side for a `v ~ 1e6 m/s` active pair.

---

# Result I — heavy-hole threshold asymptotics

On the open side, the threshold is the unique solution of

```math
\sqrt{1+q(u)^2}
=
\frac{2}{\sqrt{1-u^2}}
+1+\eta
+\frac{\rho u^2}{2}.
```

Near the opening boundary

```math
\rho_c=2(1+\eta),
```

```math
\boxed{
q_{th}\sim\frac{3}{\rho-\rho_c},
\qquad
K_{th}^{hh}/\Delta
\sim\frac{3}{\rho-\rho_c}.
}
```

Thus the threshold diverges continuously as the closed region is approached.

For a very heavy spectator band,

```math
\boxed{
K_{th}^{hh}
\to E_g+\delta_{hh}.
}
```

For `delta_hh=0`,

```math
\boxed{K_{th}^{hh}\to E_g.}
```

This is the conventional low-threshold CCCH/Auger-1 direction and explains why a flat heavy-hole branch destroys the exact two-band no-go.

For `eta=0`, exact thresholds include

```text
rho=M_hh/m_D     K_th/Eg      K_th/kBT
3                  2.496        11.972
4                  1.792         8.596
5                  1.552         7.442
10                 1.227         5.884
20                 1.106         5.303
50                 1.041         4.992
infinity            1.000         4.796
```

---

# Result J — extra-band opening erases much of the symmetry advantage but not activation parity

Every on-shell event satisfies

```math
\boxed{K_{th}^{hh}\ge E_g+\delta_{hh}.}
```

For `delta_hh >= 0`,

```math
K_{th}^{hh}>E_g/2,
```

so the open heavy-hole channel still lies on the favorable side of the external-radiative activation-parity line.

However, in the worst flat touching-band limit,

```math
K_{th}^{hh}=E_g,
```

and the exponent-only Auger/radiative ratio becomes merely

```math
\boxed{
\exp[-E_g/(2k_BT)].
}
```

At 10 um / 300 K,

```math
\boxed{0.0909.}
```

This is far weaker than the `~5e-4` factor of the earlier `K_th=10 kBT` two-band symmetry witness. A heavy spectator band can therefore erase most of the symmetry-derived exponential margin even though it does not reverse activation parity.

Once the heavy-hole channel is open, whether `Xi_hh^ext <= 1` depends on its large DOS and on Coulomb/spinor/exchange prefactors; kinematics alone cannot decide the full rate.

---

# Prior-art boundary

Established and unavailable as broad novelty:

```text
bulk HgCdTe CCCH / Auger-1 involving conduction electrons and a heavy hole;
flat/heavy-hole branch in simplified bulk HgCdTe Kane physics;
Auger-1 dominance in bulk n-type HgCdTe;
multiband/QW engineering of Auger thresholds and radiative-dominated operation.
```

Mandatory adjacent work includes Jiang, Teich & Wang, J. Appl. Phys. 69, 6869 (1991); Ciesla et al., Phys. Status Solidi B 204, 121 (1997); bulk Kane-fermion magneto-optical work including Nature Communications 7, 12576 (2016); Alymov et al., ACS Photonics 7, 98 (2020); and Morozov et al., ACS Photonics 8, 3526 (2021).

The compact reduced-model closure theorem

```math
M_{hh}v^2\lessgtr2(\Delta+\delta_{hh})
```

is retained as a derived analytical result only.

```text
NOVELTY NOT ESTABLISHED.
```

---

# What remains unresolved

```text
near-threshold phase-space scaling for the open heavy-hole channel;
heavy-hole DOS contribution to the matched-area event rate;
heavy-hole spinor/Coulomb/exchange matrix element;
anisotropic/warped heavy-hole dispersion;
multiple spectator bands;
phonon/Umklapp/plasmon-assisted channels;
SRH;
full Xi_hh^ext numerical inequality;
novelty of the combined framework.
```

# NEXT ACTION

The minimal third-band support problem is closed.

Next derive the **open heavy-hole CCCH near-threshold rate scaling**. The key question is:

> Once `M_hh v^2 > 2(Delta+delta_hh)`, how does the heavy-hole density of states modify the threshold phase-space exponent and the algebraic dependence on `v` and `M_hh`, and can any band-offset/mass regime still guarantee `Xi_hh^ext <= 1` up to an explicit multiband overlap remainder?

Keep the heavy-hole spinor/Coulomb overlap explicit. Do not insert an empirical Auger-1 lifetime and do not rank materials yet.
