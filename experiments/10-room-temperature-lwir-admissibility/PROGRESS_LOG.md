# Progress Log — Experiment 10: Room-Temperature LWIR Material Admissibility

**Scope:** analytical/theoretical only.  
**Fixed target:** `T=300 K`, `lambda_c=10 um`, `Eg=0.123984 eV`, `Eg/kBT ~= 4.796`.

---

## 2026-08-14 — branch initialization

Created branch

```text
experiment-10-room-temperature-lwir-admissibility
```

with the objective of deriving a finite-gap band-structure admissibility theorem/bound rather than ranking known materials.

Novelty hazards excluded at founding: generic `alpha/G_th`, `alpha sqrt(tau)`, low-`n_i` arguments, radiative detailed balance, generic Auger suppression, and Experiment-08 zero-gap Kane statistics.

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
\boxed{\Sigma_e=n_ed\propto v^{-2}}
```

with equivalent-species cancellation. Ideal ballistic crossing time is `v^0`.

At 10 um / 300 K, exact finite-gap Dirac carrier density is `1.8644x` the edge-parabolic estimate.

Disposition: matched-absorptance high-`v` lever survives; novelty not established.

---

## 2026-08-14 — Kane velocity freedom and microscopic resource bound

Controlling file: `KANE_VELOCITY_RESOURCE_BOUND_STEP_2026-08-14.md`.

Using `E_P=2m_0P^2/hbar^2` and `v^2=E_P/(3m_0)`, obtained `Sigma_e ~ E_P^-1`.

Generic upper-bound attempts based on the multiband effective-mass identity, fixed-window optical f-sum, and fixed remote-band energy did not provide a material-independent upper `v`.

For a Wannier Hamiltonian,

```math
\boxed{
\|\hat v_i\|
\le\frac1\hbar\sum_R|R_i|\|H_R\|
\equiv V_i^{hop},
}
```

so conditionally

```math
v\le V_{hop}
```

and

```math
\boxed{\Sigma_e\ge C/V_{hop}^2.}
```

Disposition: microscopic-resource-conditioned detector inequality derived; novelty not established.

---

## 2026-08-14 — exact symmetric-Dirac Auger kinematic closure

Controlling file: `AUGER_KINEMATIC_CLOSURE_STEP_2026-08-14.md`.

For

```math
\varepsilon(k)=\sqrt{\Delta^2+(\hbar vk)^2},
```

strict subadditivity gives empty exact normal-momentum phononless `eeh` / `hhe` Auger support in the particle-hole-symmetric two-band model.

The exact off-shell mismatch is

```math
\boxed{\Delta_A(E)=\sqrt{E^2+2E_g^2}-E.}
```

At fixed `E/Eg`, `v` cancels. High `v` and particle-hole symmetry are distinct design resources.

Broad Dirac/symmetric-dispersion Auger suppression is established prior art.

---

## 2026-08-14 — scalar particle-hole-asymmetry reopening law

Controlling file: `AUGER_ASYMMETRY_REOPENING_STEP_2026-08-14.md`.

Reproducible calculation: `numerics/auger_asymmetry_threshold.py`.

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

At 10 um / 300 K, exact inversion gives approximately

```math
\boxed{\mathcal A_m\lesssim0.0848}
```

to put the direct threshold above `10 kBT` in the scalar model.

The edge-mass interpretation is model-specific; the physical requirement is finite-momentum electron-hole symmetry over the Auger-active window.

Broad threshold enhancement near quasi-relativistic HgCdTe-QW regimes is established prior art; novelty of the cube-root reduced-model law is not established.

---

## 2026-08-14 — near-threshold direct Auger phase space and thermal scaling

Controlling file: `AUGER_NEAR_THRESHOLD_RATE_STEP_2026-08-14.md`.

Reproducible check: `numerics/auger_near_threshold_phase_space.py`.

For a fixed hot electron on the interior threshold branch,

```math
\boxed{\Phi_{3body}\propto(K-K_{th})^2.}
```

If `|V_eff|^2 ~ (K-K_th)^nu`, then

```math
\boxed{\Gamma_{II}\propto(K-K_{th})^{2+\nu}.}
```

The phase-space exponent `2` is robust; the full-rate exponent is not universal because Kane/multiband overlap zeros can add powers.

Detailed balance gives

```math
\boxed{
G_A^{vol}
\propto
T^{3+\nu}
\exp[-(E_g/2+K_{th})/(k_BT)].
}
```

For the minimal static screened Coulomb model, matched absorptance gives

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

Weak screening and intrinsic-Debye large-`v` asymptotics approach `v^-4`; fixed physical screening length can strengthen the algebraic suppression toward `v^-8`.

Disposition: direct rate factorized as far as useful without a complete multiband wave-function model; novelty not established.

---

## 2026-08-14 — external radiative boundary floor and direct-Auger admissibility ratio

Controlling file:

`RADIATIVE_BOUNDARY_ADMISSIBILITY_STEP_2026-08-14.md`

Reproducible calculation:

`numerics/radiative_boundary_floor.py`

### Critical correction to optical matching

Matching useful front-side absorptance and accepted scene etendue alone does **not** fix total radiative exchange. Extra backside/substrate optical ports provide a counterexample.

The complete mode-resolved external optical boundary must be matched:

```math
\boxed{
\mathcal A_\mu^{(A)}=\mathcal A_\mu^{(B)}
\quad\text{for every external carrier-coupled optical channel.}
}
```

For reciprocal passive structures, modal Kirchhoff reciprocity then fixes the external thermal emission and external background absorption independently of absorber chemistry.

At thermal equilibrium,

```math
\boxed{\Phi_{abs}^{ext}=\Phi_{em}^{ext}=\Phi_0,}
```

so the two-way unavoidable optical event traffic is `2 Phi_0`.

### Photon-recycling correction

Internal bulk radiative recombination is not the invariant denominator. In the simple escape-probability picture,

```math
\Phi_{em}^{ext}=p_{esc}R_{rad}^{int},
```

so internal radiative event count can vary strongly at fixed external emission.

In the low-frequency/coarse-grained carrier-number limit, recombination followed by photon reabsorption removes and then restores a carrier pair. The irreversible optical traffic is external absorption plus final photon escape/loss.

### Derived event-traffic ratio

Define

```math
\boxed{
\Xi_A^{ext}
=\frac{G_A^{gen}+R_A^{rec}}
{\Phi_{abs}^{ext}+\Phi_{em}^{ext}}.
}
```

At thermal equilibrium,

```math
\boxed{\Xi_A^{ext}=G_A/\Phi_0.}
```

The natural direct-channel admissibility condition is

```math
\boxed{\Xi_A^{ext}\le1.}
```

This replaces the provisional `Xi_nr` bookkeeping idea with a defined nonradiative-to-unavoidable-optical event-traffic ratio.

### Ideal 10-um / 300-K radiative benchmark

For unit absorptance above the gap over one hemisphere,

```math
\Phi_0
=\frac{2\pi(k_BT)^3}{h^3c^2}I_2(E_g/k_BT).
```

Numerically:

```text
Phi_0 = 4.89777e17 cm^-2 s^-1
2 Phi_0 = 9.79555e17 cm^-2 s^-1
q Phi_0 = 0.0784710 A/cm^2
n_B(Eg) = 0.0083322
```

### Activation-parity result

The radiative boundary floor has Boltzmann factor `exp[-Eg/kBT]`, while direct Auger has `exp[-(Eg/2+K_th)/kBT]`.

Therefore

```math
\boxed{
\Xi_A^{ext}\propto_{exp}
\exp[-(K_{th}-E_g/2)/(k_BT)].
}
```

The direct-Auger/radiative activation-parity line is

```math
\boxed{K_{th}=E_g/2.}
```

At the previous `K_th=10 kBT` witness, the additional direct-Auger/radiative thermal factor is

```math
\boxed{4.99\times10^{-4}}
```

before favorable high-`v` algebraic suppression and before unresolved interaction prefactors.

Within the positive-curvature scalar-asymmetry family (`|beta|<1/2`),

```math
\boxed{K_{th}\ge\sqrt3\,E_g/2>E_g/2.}
```

Thus every member of that controlled family lies on the favorable side of activation parity, although prefactors can still prevent `Xi_A^ext <= 1`.

### Prior-art disposition

Radiative detailed balance, spectral/angular reciprocity, modal Kirchhoff laws, radiative dark-current formulas, photon recycling, and HgCdTe photon-transport/recycling effects are established prior art.

The only possible surviving contribution remains the detector-specific joint admissibility construction. Novelty is not established.

---

## Active frontier

The two-band direct-Auger side and the external radiative-boundary side are now closed at the controlled-model level.

The next intrinsic spoiler is a minimal **third-band/heavy-hole escape channel**:

> Add a heavy-hole-like reservoir to the high-`v` symmetric active pair and derive exact three-band Auger kinematics. Determine the minimum band offset/mass/velocity condition required to keep extra-band Auger event traffic below the fixed external optical floor.

Do not rank real materials yet. Do not insert empirical lifetimes before the three-band kinematic support is understood.
