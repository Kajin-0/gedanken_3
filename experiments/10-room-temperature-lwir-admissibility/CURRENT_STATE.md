# Current State — Experiment 10: Room-Temperature LWIR Material Admissibility

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** **PROVISIONAL CONDITIONAL THEOREM PACKAGE SURVIVES FOCUSED PRIOR-ART AUDIT / GENERAL SPECTATOR CEILING DERIVED / THREE-BAND NEUTRALITY REPAIRED / UNIVERSALITY FAILS FOR UNBOUNDED SPECTATOR OPTICAL STRENGTH OR PHOTONIC PATH ENHANCEMENT / NOVELTY NOT ESTABLISHED / NO MANUSCRIPT YET**

## Fixed target

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

1. `THEOREM_CORE_2026-08-14.md`
2. `JOINT_ADMISSIBILITY_NOVELTY_AUDIT_2026-08-14.md`
3. `GENERAL_SPECTATOR_BAND_ADMISSIBILITY_THEOREM_STEP_2026-08-14.md`
4. `HEAVY_HOLE_AUGER_RATE_AND_JOINT_BOUND_STEP_2026-08-14.md`
5. `THIRD_BAND_HEAVY_HOLE_AUGER_ESCAPE_STEP_2026-08-14.md`
6. `RADIATIVE_BOUNDARY_ADMISSIBILITY_STEP_2026-08-14.md`
7. earlier Experiment-10 derivations as needed.

---

# 1. Matched active-pair optical depth

For the finite-gap 3-D massive-Dirac active pair,

```math
n_0\propto v^{-3},
\qquad
\alpha_D\propto v^{-1},
\qquad
d_0\propto v,
```

so under the controlled single-pass active-pair optical-depth requirement

```math
\boxed{\Sigma_0=C/v^2.}
```

For the standard numerical witness (`A=0.90`, `r=1.2`, `n_b=3.5`),

```math
C=1.06668\times10^{29}\ \mathrm{m^{-2}(m/s)^2}.
```

The ideal ballistic crossing time remains `v^0`.

---

# 2. Microscopic lattice velocity resource

For a Wannier/tight-binding Hamiltonian,

```math
\boxed{
\|\hat v_i\|
\le\frac1\hbar\sum_R|R_i|\|H_R\|
\equiv V_i^{hop}.
}
```

Therefore conditionally

```math
\boxed{v\le V_{hop}.}
```

---

# 3. Two-band Auger results

Exact particle-hole-symmetric massive-Dirac `eeh/hhe` direct Auger is kinematically closed.

The exact mismatch is

```math
\boxed{\Delta_A(E)=\sqrt{E^2+2E_g^2}-E.}
```

Scalar particle-hole asymmetry reopens the channel with weak-asymmetry threshold

```math
\boxed{K_{th}\sim E_g\mathcal A_m^{-1/3}.}
```

The interior threshold phase-space shell obeys

```math
\boxed{\Phi_{3body}\propto(K-K_{th})^2,}
```

with extra microscopic powers possible from overlap zeros.

In the minimal weak-screening model at matched absorptance, direct-area Auger retains an approximate `v^-4` algebraic dependence times the threshold activation.

Broad Dirac/symmetric Auger suppression and threshold physics are established prior art.

---

# 4. Complete external optical boundary

Matching useful front-side absorptance alone does not fix radiative exchange. Match the complete external mode-resolved optical boundary when comparing irreversible optical traffic.

At equilibrium,

```math
\Phi_{abs}^{ext}=\Phi_{em}^{ext}=\Phi_0.
```

Internal radiative recombination is not invariant because photon recycling changes internal event count.

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

# 5. General spectator-band kinematic ceiling

Let a spectator hole branch have positive isotropic convex excitation energy `E_s(p)`.

Define

```math
\boxed{
 v_s^{crit}=\inf_{p>0}\frac{E_s(p)}{p}.
}
```

For normal-momentum spectator-assisted CCCH with the active massive-Dirac conduction band,

```math
\boxed{
 v\le v_s^{crit}
\Longleftrightarrow
\text{no finite-energy support}
}
```

within the continuum model.

Equivalently,

```math
\boxed{E_s(p)\ge vp\quad\forall p.}
```

For multiple spectators,

```math
\boxed{v_{spec}=\min_s v_s^{crit}.}
```

This has the mathematical structure of the Landau critical-velocity criterion and uses the classical equal-group-velocity impact-ionization threshold condition. It is not claimed as a new general kinematic principle.

For a parabolic heavy-hole spectator,

```math
E_{hh}(p)=\Delta+\delta_{hh}+p^2/(2M_{hh}),
```

```math
\boxed{
 v_{hh}^{crit}=\sqrt{2(\Delta+\delta_{hh})/M_{hh}}
}
```

and exact closure is

```math
\boxed{M_{hh}v^2\le2(\Delta+\delta_{hh}).}
```

---

# 6. Spectator-hole charge neutrality correction

Adding spectator hole states shifts the intrinsic chemical potential positive. Therefore the old two-band relation is no longer an equality.

However,

```math
n_c(\mu)\ge n_c(0)
```

and the active symmetric interband occupation difference satisfies

```math
\mathcal P(E,\mu)
=\frac{\sinh(E/k_BT)}{\cosh(E/k_BT)+\cosh(\mu/k_BT)}
\le\mathcal P(E,0).
```

Thus active-pair absorption weakens and the required active-pair single-pass thickness increases.

Therefore the two-band result survives as the rigorous lower bound

```math
\boxed{\Sigma_c\ge C/v^2.}
```

At the touching parabolic-spectator exact-closure boundary (`rho=2`), one spin-degenerate spectator gives, for the standard `r=1.2` witness,

```text
mu/kBT = 0.46384
active density = 1.5695 x two-band value
active absorption Pauli factor = 0.98907 x two-band value
matched active-electron column = 1.5869 x C/v^2
```

so the basic bound is conservative in that case.

---

# 7. Strongest current conditional theorem

Define

```math
\boxed{v_{adm}=\min(V_{hop},v_{spec}).}
```

Then any member of the controlled single-pass, active-pair-optically-dominant class satisfying exact normal-momentum spectator-assisted Auger closure obeys

```math
\boxed{
\Sigma_c
\ge
\frac{C}{v_{adm}^2}
=
\max\!\left[
\frac{C}{V_{hop}^2},
\max_s\frac{C}{(v_s^{crit})^2}
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

This is the strongest surviving Experiment-10 theorem candidate.

---

# 8. Heavy-hole open-channel rate result

For the open parabolic CCCH channel, the constrained six-dimensional threshold Hessian gives a `(K-K_th)^2` kinematic shell.

The flat-heavy-hole limit has finite normalized local threshold phase space:

```math
\det H\to1,
\qquad
\gamma\to1.
```

There is no universal independent `M_hh^(3/2)` divergence in the local threshold event rate.

Near exact closure, with `delta rho=rho-rho_c`,

```math
K_{th}^{hh}/\Delta\sim3/(\delta\rho),
```

and

```math
\boxed{
\gamma^2/\sqrt{\det H}
\sim
(\sqrt3\rho_c^{3/2}/64)(\delta\rho)^{3/2}.
}
```

So the rate is suppressed both exponentially and algebraically near closure.

---

# 9. Adversarial prior-art disposition

Established:

```text
alpha/G_th detector-material optimization;
band-structure Auger suppression in small-gap detectors;
HgCdTe heavy-hole CCCH/Auger-1;
equal-group-velocity impact-ionization thresholds;
Landau min[E(p)/p] critical-velocity structure;
Dirac/quasi-relativistic Auger suppression;
multiband superlattice design jointly balancing absorption and Auger;
radiative detailed balance and photon recycling.
```

The focused audit did not locate the exact composed carrier-column inequality above, but a hostile reviewer can plausibly call it an elementary synthesis of known ingredients.

Current novelty status:

```text
PROVISIONAL THEOREM-LEVEL SYNTHESIS.
NO DIRECT COLLISION FOUND IN FOCUSED AUDIT.
NOVELTY NOT ESTABLISHED.
```

---

# 10. Two hard universality failures

## Optically active spectator bands

If spectators also provide unconstrained useful absorption,

```math
\alpha_{tot}=\alpha_D+\alpha_s,
```

then the simple active-pair `C/v^2` physical-thickness bound is not universal.

If `alpha_s <= chi_opt alpha_D`, only the weakened conditional result

```math
\Sigma_c\ge C/[(1+\chi_{opt})v_{adm}^2]
```

follows.

Actual HgCdTe heavy-hole states are optically active, so the current theorem is **not** a quantitative bulk-HgCdTe bound.

## Arbitrary photonic path enhancement

The step `d=zeta/alpha` is single-pass. Resonators, gratings and slow-light structures can reduce physical absorber thickness at fixed external absorptance.

Without an optical-path resource, arbitrary photonic enhancement escapes a universal physical carrier-column floor.

---

# NEXT ACTION

Do not add another electronic recombination mechanism.

Attack the dominant remaining loophole:

> For a passive absorber with specified external absorptance and finite detector temporal response/bandwidth, what is the maximum optical path enhancement or photon dwell time, and does that restore a generalized carrier-column lower bound against resonant/slow-light escape?

This reconnects the theorem to the founding finite-response requirement.
