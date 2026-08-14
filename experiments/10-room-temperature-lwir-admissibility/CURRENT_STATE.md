# Current State — Experiment 10: Room-Temperature LWIR Material Admissibility

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** **MATCHED-ABSORPTANCE HIGH-v LEVER / MICROSCOPIC VELOCITY RESOURCE BOUND / SYMMETRIC-DIRAC AUGER CLOSURE / FINITE-ASYMMETRY THRESHOLD / THRESHOLDED DIRECT-AUGER RATE / EXTERNAL RADIATIVE-BOUNDARY FLOOR ALL DERIVED IN CONTROLLED MODELS / JOINT ADMISSIBILITY RATIO DEFINED / NOVELTY NOT ESTABLISHED / NO MANUSCRIPT YET**

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

1. `RADIATIVE_BOUNDARY_ADMISSIBILITY_STEP_2026-08-14.md`
2. `AUGER_NEAR_THRESHOLD_RATE_STEP_2026-08-14.md`
3. `AUGER_ASYMMETRY_REOPENING_STEP_2026-08-14.md`
4. `AUGER_KINEMATIC_CLOSURE_STEP_2026-08-14.md`
5. `KANE_VELOCITY_RESOURCE_BOUND_STEP_2026-08-14.md`
6. `MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`
7. `PROGRESS_LOG.md`

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

Thus

```math
\boxed{\Sigma_e=n_ed\propto v^{-2}}
```

with equivalent-species cancellation, while ideal ballistic crossing time is `v^0`.

At 10 um / 300 K the exact finite-gap carrier density is `1.8644x` the edge-parabolic estimate.

---

# Result B — microscopic velocity resource

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

# Result C — exact symmetric-Dirac direct-Auger closure

For

```math
\varepsilon(k)=\sqrt{\Delta^2+(\hbar vk)^2},
\qquad\Delta=E_g/2>0,
```

normal-momentum phononless `eeh` and `hhe` Auger channels have empty exact support in the symmetric two-band model.

The minimum off-shell mismatch is

```math
\boxed{\Delta_A(E)=\sqrt{E^2+2E_g^2}-E.}
```

At fixed `E/Eg`, `v` cancels. High `v` and electron-hole symmetry are distinct favorable resources.

---

# Result D — scalar asymmetry reopening

For

```math
E_\pm=Dk^2\pm\sqrt{\Delta^2+(\hbar vk)^2},
```

use

```math
\beta=D\Delta/(\hbar^2v^2),
```

and

```math
\boxed{
\mathcal A_m
=\frac{|m_e^{-1}-m_h^{-1}|}
{m_e^{-1}+m_h^{-1}}
=2|\beta|.
}
```

The exact reduced-model reopening boundary is in `AUGER_ASYMMETRY_REOPENING_STEP_2026-08-14.md`.

For weak asymmetry,

```math
\boxed{K_{th}\sim E_g\mathcal A_m^{-1/3}.}
```

At 10 um / 300 K, the scalar model requires approximately

```math
\boxed{\mathcal A_m\lesssim0.0848}
```

to put the direct threshold above `10 k_BT`.

This is not a universal edge-mass rule. The physical requirement is finite-momentum electron-hole symmetry over the Auger-active window.

---

# Result E — near-threshold direct-Auger phase space and rate factorization

On the interior threshold branch, the fixed-hot-electron three-body energy-shell measure is

```math
\boxed{\Phi_{3body}\propto(K-K_{th})^2.}
```

If the squared threshold matrix element behaves as

```math
|V_{eff}|^2\propto(K-K_{th})^\nu,
```

then

```math
\boxed{\Gamma_{II}\propto(K-K_{th})^{2+\nu}.}
```

The exponent `2` is a kinematic phase-space exponent, not a universal full-rate exponent.

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

Weak screening and intrinsic-Debye large-`v` asymptotics tend toward `v^-4`; fixed physical screening length can strengthen the algebraic suppression toward `v^-8`.

---

# Result F — complete external optical boundary fixes the unavoidable radiative/background exchange

Controlling derivation:

`RADIATIVE_BOUNDARY_ADMISSIBILITY_STEP_2026-08-14.md`

## Critical correction

Matching useful front-side absorptance and accepted scene etendue is **not sufficient** to fix total thermal emission. A detector with an extra backside/substrate optical port can have the same task absorptance and a different radiative exchange.

The theorem-grade comparison must match the **complete external mode-resolved optical boundary**:

```math
\boxed{
\mathcal A_\mu^{(A)}=\mathcal A_\mu^{(B)}
\quad\text{for every external optical channel/reservoir relevant to active-carrier exchange.}
}
```

For reciprocal passive structures, modal Kirchhoff reciprocity then fixes the escaping thermal emission:

```math
\boxed{
\Phi_{em}^{ext}(T_d)
=\int d\mu\,\mathcal A_\mu n_B(\omega_\mu,T_d)\Gamma_\mu.
}
```

The absorbed external-background rate is

```math
\boxed{
\Phi_{abs}^{ext}
=\int d\mu\,\mathcal A_\mu n_\mu^{env}\Gamma_\mu.
}
```

Thus at fixed complete optical boundary, detector temperature, and environment, these external rates are chemistry-independent.

At full thermal equilibrium,

```math
\boxed{\Phi_{abs}^{ext}=\Phi_{em}^{ext}=\Phi_0.}
```

The mean net photon flux is zero but the two-way event traffic is

```math
\boxed{\mathcal T_{opt}^{eq}=2\Phi_0.}
```

---

# Result G — internal radiative recombination is NOT the invariant denominator

Photon recycling separates internal recombination count from irreversible external optical exchange.

In a simple escape-probability model,

```math
\Phi_{em}^{ext}=p_{esc}R_{rad}^{int}.
```

Therefore `R_rad^int` can vary strongly while the external thermal emission remains fixed.

In the low-frequency/coarse-grained carrier-number limit, an internal radiative recombination followed by photon reabsorption removes and then recreates a pair, so the irreversible optical events are external absorption and final photon escape/loss.

At bandwidths comparable to photon dwell/recycling rates, internal cycling can add dynamical fluctuations; that is not fixed by external absorptance alone.

Therefore do **not** use bulk `B n_i^2 d` as the universal radiative denominator in Experiment 10.

---

# Result H — derived direct-Auger-to-external-optical admissibility ratio

Define direct-Auger event traffic

```math
\mathcal T_A=G_A^{gen}+R_A^{rec},
```

and irreversible external optical traffic

```math
\mathcal T_{opt}=\Phi_{abs}^{ext}+\Phi_{em}^{ext}.
```

Then

```math
\boxed{
\Xi_A^{ext}=\frac{\mathcal T_A}{\mathcal T_{opt}}.
}
```

At thermal equilibrium,

```math
G_A^{gen}=R_A^{rec}=G_A,
```

and

```math
\Phi_{abs}^{ext}=\Phi_{em}^{ext}=\Phi_0,
```

so

```math
\boxed{\Xi_A^{ext}=G_A/\Phi_0.}
```

The natural direct-channel admissibility condition is

```math
\boxed{\Xi_A^{ext}\le1.}
```

This is a derived event-traffic comparison, replacing the earlier provisional `Xi_nr` bookkeeping quantity.

---

# Result I — ideal 10-um / 300-K radiative benchmark

For unit absorptance above `E_g` over one hemisphere,

```math
\boxed{
\Phi_0
=\frac{2\pi(k_BT)^3}{h^3c^2}I_2(x_g),
\qquad
I_2(x_g)=\int_{x_g}^{\infty}\frac{x^2dx}{e^x-1}.
}
```

At the fixed target,

```text
x_g = 4.795922925
I_2 = 0.286823524
Phi_0 = 4.89777e17 cm^-2 s^-1
2 Phi_0 = 9.79555e17 cm^-2 s^-1
q Phi_0 = 0.0784710 A/cm^2
n_B(Eg) = 0.0083322
```

The Bose bunching correction for any fully accepted interband mode is therefore below about `0.84%` relative to a Poisson variance-to-mean factor at this target.

Reproducible calculation:

`numerics/radiative_boundary_floor.py`

---

# Result J — direct-Auger/radiative activation parity

For `x_g >> 1`,

```math
I_2(x_g)\simeq(x_g^2+2x_g+2)e^{-x_g}.
```

At `x_g=4.7959` this approximation is already within about `0.34%` of the exact integral.

Since the external radiative floor has the Boltzmann exponent

```math
e^{-E_g/(k_BT)}=e^{-2\Delta/(k_BT)},
```

while direct Auger has

```math
e^{-(\Delta+K_{th})/(k_BT)},
```

their exponential ratio is

```math
\boxed{
\Xi_A^{ext}\propto_{exp}
\exp[-(K_{th}-\Delta)/(k_BT)].
}
```

Thus the **activation-parity line** is

```math
\boxed{K_{th}=\Delta=E_g/2.}
```

If `K_th > E_g/2`, direct Auger is thermally steeper than the unavoidable radiative boundary floor. Prefactors still determine whether `Xi_A^ext <= 1` numerically.

For the earlier `K_th=10 k_BT` witness,

```math
\boxed{
\exp[-(K_{th}-E_g/2)/(k_BT)]
=4.99\times10^{-4}.
}
```

This is before the additional favorable `v^-4` direct-Auger scaling in the weak-screening model.

---

# Result K — the positive-curvature scalar-asymmetry family is automatically on the favorable side of activation parity

Positive electron and hole edge curvatures require

```math
|\beta|<1/2.
```

The minimum direct threshold over that controlled family is

```math
\boxed{
K_{th}\ge\sqrt3\,\Delta
=0.866025\,E_g.
}
```

Hence

```math
\boxed{
K_{th}-\Delta
\ge(\sqrt3-1)\Delta>0.
}
```

At 10 um / 300 K the weakest possible direct-Auger/radiative exponential factor in this reduced positive-curvature family is

```math
\boxed{e^{-1.7555}=0.173.}
```

This is an exponent-only statement, not a full-rate guarantee.

---

# Prior-art boundary

Established and unavailable as novelty:

```text
van Roosbroeck-Shockley radiative detailed balance;
spectral/angular photovoltaic-luminescence reciprocity;
modal Kirchhoff laws for reciprocal emitters;
blackbody/background current formulas;
photon recycling and escape-probability effects;
HgCdTe photon-transport/recycling calculations;
direct-gap Auger activation thresholds and threshold-power laws.
```

The possible surviving contribution is only the detector-specific joint construction

```text
complete external optical boundary
+ matched-absorptance finite-gap carrier scaling
+ microscopic velocity resource
+ symmetry-controlled direct-Auger threshold
+ thresholded direct-Auger rate
-> Xi_A^ext.
```

```text
NOVELTY NOT ESTABLISHED.
```

---

# Important boundaries

Real bulk HgCdTe is not the exact two-band model. Heavy-hole/remote bands, phonons, disorder, finite linewidth, Umklapp, plasmon assistance, and SRH can add intrinsic or extrinsic carrier-generation channels.

The external-boundary theorem is a low-frequency/coarse-grained carrier-number statement when photon recycling is fast relative to the measurement timescale.

---

# NEXT ACTION

The two-band direct-Auger and radiative-boundary sides are now closed at the controlled-model level.

The next intrinsic spoiler is the first **extra-band escape from the two-band Auger protection**:

> Add a minimal third band, especially a heavy-hole-like reservoir, and derive whether a direct Auger channel can remain kinematically open even when the active conduction/valence pair has large `v` and excellent particle-hole symmetry. Identify the minimum energy/mass/velocity separation condition required to preserve a radiative-floor-limited regime.

Start with exact three-band kinematics. Do not insert empirical lifetimes and do not rank candidate materials yet.
