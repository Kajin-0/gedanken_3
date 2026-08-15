# Progress Log — Experiment 10: Room-Temperature LWIR Material Admissibility

**Scope:** analytical/theoretical only.  
**Fixed target:** `T=300 K`, `lambda_c=10 um`, `Eg=0.123984 eV`, `Eg/kBT ~= 4.796`.

---

## 2026-08-14 — branch initialization

Created `experiment-10-room-temperature-lwir-admissibility` to derive a finite-gap band-structure admissibility theorem/bound rather than rank materials.

Immediate novelty exclusions: generic `alpha/G_th`, `alpha sqrt(tau)`, low-`n_i` arguments, radiative detailed balance, generic Auger suppression, and Experiment-08 zero-gap Kane statistics.

---

## 2026-08-14 — matched massive-Dirac absorptance

Derived

```math
n_e\propto N_Dv^{-3},
\qquad
\alpha_D\propto N_Dv^{-1},
\qquad
d\propto v/N_D,
```

hence

```math
\boxed{\Sigma_e=C/v^2}
```

for the controlled single-pass two-band active pair. Equivalent-species degeneracy cancels and ideal ballistic crossing time is `v^0`.

At 10 um / 300 K the exact finite-gap Dirac density is `1.8644x` the edge-parabolic estimate.

---

## 2026-08-14 — Kane velocity resource

Generic low-energy effective-mass sums, fixed-window optical f-sums, and remote-band energy separation did not give a universal upper `v`.

A Wannier Hamiltonian gives

```math
\boxed{v\le V_{hop}}
```

and therefore

```math
\boxed{\Sigma_e\ge C/V_{hop}^2.}
```

---

## 2026-08-14 — exact symmetric two-band Auger closure

For the symmetric finite-gap massive-Dirac pair, normal-momentum phononless `eeh/hhe` Auger is exactly closed.

```math
\boxed{\Delta_A(E)=\sqrt{E^2+2E_g^2}-E.}
```

At fixed `E/Eg`, `v` cancels. High `v` and dispersion symmetry are separate resources.

---

## 2026-08-14 — scalar particle-hole-asymmetry reopening

For

```math
E_\pm=Dk^2\pm\sqrt{\Delta^2+(\hbar vk)^2},
```

derived an exact reopening boundary and weak-asymmetry law

```math
\boxed{K_{th}\sim E_g\mathcal A_m^{-1/3}.}
```

At the fixed target, `A_m <= 0.0848` gives `K_th >= 10 kBT` in the scalar toy model.

---

## 2026-08-14 — near-threshold two-band Auger rate

For a fixed hot carrier on the interior branch,

```math
\boxed{\Phi_{3body}\propto(K-K_{th})^2.}
```

Microscopic overlap zeros may add powers.

Detailed balance gives threshold activation `exp[-(Eg/2+K_th)/kBT]`.

In the minimal weak-screening matched-area model, direct Auger retains approximately `v^-4` algebraic suppression.

---

## 2026-08-14 — external radiative boundary floor

Corrected the optical comparison: useful front-side absorptance alone does not fix total radiative exchange. Match the complete external mode-resolved optical boundary.

At equilibrium,

```math
\Phi_{abs}^{ext}=\Phi_{em}^{ext}=\Phi_0.
```

Internal radiative recombination is not invariant because photon recycling changes internal event count.

At the ideal hemispherical 10-um/300-K step-absorber benchmark:

```text
Phi_0 = 4.89777e17 cm^-2 s^-1
q Phi_0 = 0.0784710 A/cm^2
```

The direct-Auger/radiative activation-parity line is `K_th=Eg/2`.

---

## 2026-08-14 — minimal parabolic heavy-hole spectator

Added

```math
E_{hh}=\Delta+\delta_{hh}+p^2/(2M_{hh}).
```

With `rho=M_hh v^2/Delta` and `eta=delta_hh/Delta`, proved

```math
\boxed{
\rho\le2(1+\eta)
\Longleftrightarrow
\text{no finite-energy normal-momentum CCCH support}.
}
```

Equivalently

```math
\boxed{M_{hh}v^2\le2(\Delta+\delta_{hh}).}
```

This was the first direct conflict with the high-`v` thermodynamic lever.

---

## 2026-08-14 — open heavy-hole threshold phase space

Derived the exact six-dimensional constrained threshold Hessian. The pure threshold shell remains quadratic:

```math
\Phi_{hh}\propto
\frac{\gamma^2}{\sqrt{\det H}}(K-K_{th}^{hh})^2.
```

Negative result: as `M_hh -> infinity`, the normalized local threshold coefficient stays finite (`det H -> 1`, `gamma -> 1`). There is no universal independent `M_hh^(3/2)` threshold-rate catastrophe.

Near exact closure, with `delta rho=rho-rho_c`,

```math
K_{th}^{hh}/\Delta\sim3/(\delta\rho)
```

and

```math
\boxed{
\gamma^2/\sqrt{\det H}
\sim
(\sqrt3\rho_c^{3/2}/64)(\delta\rho)^{3/2}.
}
```

Thus approach to closure is suppressed both exponentially and algebraically.

---

## 2026-08-14 — first joint exact-closure carrier-column bound

Combining the two-band single-pass relation with parabolic spectator closure initially gave

```math
\boxed{
\Sigma_e\ge C M_{hh}/[2(\Delta+\delta_{hh})].
}
```

For a touching `0.5m0` spectator, this gives `v_c=2.088e5 m/s` and `Sigma_min=2.446e14 cm^-2` at the standard witness, about 23x the earlier `v=1e6 m/s` column.

This result triggered a dedicated prior-art and consistency audit rather than immediate manuscript drafting.

---

## 2026-08-14 — general spectator-band theorem

Controlling file:

`GENERAL_SPECTATOR_BAND_ADMISSIBILITY_THEOREM_STEP_2026-08-14.md`

For arbitrary positive isotropic convex spectator excitation `E_s(p)`, define

```math
\boxed{
 v_s^{crit}=\inf_{p>0}E_s(p)/p.
}
```

Using the minimum final-energy envelope and monotonic mismatch, exact finite-energy normal-momentum spectator-assisted CCCH closure is equivalent to

```math
\boxed{E_s(p)\ge vp\quad\forall p}
```

or

```math
\boxed{v\le v_s^{crit}.}
```

For multiple spectators,

```math
v_{spec}=\min_s v_s^{crit}.
```

The parabolic heavy-hole formula is recovered as a corollary.

### Novelty correction

The form `inf E(p)/p` is mathematically the Landau critical-velocity construction, and equality of final group velocities at impact-ionization threshold is classical semiconductor theory.

Therefore the kinematic ceiling itself is not a new universal principle.

---

## 2026-08-14 — three-band neutrality consistency repair

Adding spectator hole states invalidates the exact two-band assumption `mu=0`.

Charge neutrality shifts

```math
\boxed{\mu>0.}
```

which increases active conduction density and decreases the active interband occupation difference:

```math
\mathcal P(E,\mu)
=\frac{\sinh(E/k_BT)}{\cosh(E/k_BT)+\cosh(\mu/k_BT)}
\le\mathcal P(E,0).
```

Thus for the same required **active-pair single-pass optical depth**,

```math
\boxed{\Sigma_c\ge C/v^2}
```

survives as a lower bound rather than equality.

At the touching parabolic spectator closure boundary (`rho=2`), exact FD neutrality for one spin-degenerate spectator gives at `r=1.2`:

```text
mu/kBT = 0.46384
active density increase = 1.5695x
active absorption occupation factor = 0.98907x
active matched column increase = 1.5869x
```

relative to the two-band baseline.

---

## 2026-08-14 — strongest general conditional bound

Define

```math
v_{adm}=\min(V_{hop},v_{spec}).
```

Then under the controlled single-pass active-pair-optically-dominant hypotheses and exact spectator-assisted closure,

```math
\boxed{
\Sigma_c
\ge
\frac{C}{v_{adm}^2}
=
\max\!\left[
C/V_{hop}^2,
\max_s C/(v_s^{crit})^2
\right].
}
```

Parabolic heavy-hole corollary:

```math
\boxed{
\Sigma_c
\ge
\max\!\left[
C/V_{hop}^2,
C M_{hh}/(2(\Delta+\delta_{hh}))
\right].
}
```

Controlling compressed statement:

`THEOREM_CORE_2026-08-14.md`.

---

## 2026-08-14 — adversarial novelty audit

Controlling file:

`JOINT_ADMISSIBILITY_NOVELTY_AUDIT_2026-08-14.md`.

Direct collisions found for essentially every constituent idea:

```text
alpha/G_th detector optimization — established;
band-structure Auger suppression in small-gap detectors — established;
heavy-hole CCCH in HgCdTe — established;
equal-group-velocity impact-ionization thresholds — established;
Landau min[E(p)/p] critical-velocity structure — established;
Dirac/symmetric Auger suppression — established;
multiband superlattice optimization balancing absorption and Auger — established;
radiative detailed balance / photon recycling — established.
```

Closest detector literature includes Grein/Young/Flatte/Ehrenreich work using full `k.p` band structures to calculate absorption/recombination and theoretical detector limits, plus the Piotrowski/Gawron `alpha/G_th` framework.

The focused audit did **not** locate the exact carrier-sheet lower-bound composition above.

Disposition:

```text
THEOREM-LEVEL SYNTHESIS SURVIVES FOCUSED AUDIT PROVISIONALLY.
NOVELTY NOT ESTABLISHED.
```

### Major universality failures identified

1. **Optically active spectators:** if `alpha_s` is unconstrained, the active Dirac `alpha ~ 1/v` law no longer fixes physical thickness. Actual HgCdTe heavy-hole states are optically active.
2. **Arbitrary photonic path enhancement:** resonators/gratings/slow-light structures can reduce physical thickness at fixed absorptance, defeating a universal single-pass carrier-column floor.
3. Exact closure is sufficient but not necessary for radiative-limited operation.

---

## Active frontier

Do not add another electronic recombination mechanism.

The dominant remaining loophole is photonic:

> At specified external absorptance and finite detector response time/bandwidth, can a passive resonant/slow-light structure provide arbitrarily large optical path enhancement, or does photon dwell time impose a bound that restores a generalized carrier-column floor?

This is now the strongest continuation because it reconnects the theorem to the founding temporal-response requirement.