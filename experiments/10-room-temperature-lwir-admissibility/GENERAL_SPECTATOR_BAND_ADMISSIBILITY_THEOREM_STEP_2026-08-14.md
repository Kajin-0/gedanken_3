# Experiment 10 — General Spectator-Band Closure Theorem and Robust Carrier-Column Bound

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Disposition:** **GENERAL SPECTATOR-BAND KINEMATIC CEILING DERIVED / MATHEMATICALLY LANDAU-LIKE AND NOT A NOVEL PRINCIPLE / THREE-BAND NEUTRALITY CONSISTENCY REPAIRED / CARRIER-COLUMN RESULT SURVIVES AS A LOWER BOUND / OPTICALLY ACTIVE SPECTATOR BANDS IDENTIFIED AS THE MAIN LIMITATION / NOVELTY NOT ESTABLISHED**

## 1. Why this step was necessary

The previous parabolic heavy-hole result

```math
M_{hh}v^2\le2(\Delta+\delta_{hh})
```

was useful but too model-specific to serve as the main theorem.

Two adversarial questions also had to be resolved before promoting the detector-level bound:

1. Does the kinematic closure condition have a general arbitrary-band form?
2. Does adding spectator hole states invalidate the earlier two-band thermal carrier-column relation by shifting the intrinsic chemical potential?

A third limitation also appears:

3. If the spectator band contributes substantially to useful optical absorption, the simple active-Dirac absorption law no longer controls the required absorber thickness.

This file resolves the first two and makes the third an explicit theorem boundary.

---

# Part I — general spectator-band kinematic theorem

## 2. Active sector

Use physical crystal momentum

```math
p=\hbar k.
```

The active conduction branch has positive excitation energy

```math
\boxed{
\varepsilon(p)=\sqrt{\Delta^2+v^2p^2},
\qquad \Delta>0.
}
```

Its group speed is

```math
\varepsilon'(p)=\frac{v^2p}{\sqrt{\Delta^2+v^2p^2}},
```

which is strictly increasing and tends to `v` as `p -> infinity`.

## 3. General spectator-hole branch

Let the extra hole excitation have isotropic energy

```math
\boxed{E_s(p)}
```

with the assumptions

```text
E_s(p) > 0;
E_s is continuous;
E_s is convex and nondecreasing for p >= 0;
the continuum model is taken to arbitrarily large p for the exact global theorem.
```

The finite-validity-window caveat is treated separately below.

Consider inverse CCCH-like impact ionization

```text
e_0 -> e_1 + e_2 + h_s
```

with normal momentum conservation

```math
\mathbf p_0=\mathbf p_1+\mathbf p_2+\mathbf p_s.
```

---

## 4. Minimum final-energy envelope

For total momentum magnitude `P`, define

```math
\boxed{
F(P)
=\min_{\mathbf p_1+\mathbf p_2+\mathbf p_s=\mathbf P}
\left[
\varepsilon(p_1)+\varepsilon(p_2)+E_s(p_s)
\right].
}
```

Convexity and isotropy imply that a minimizing configuration can be chosen collinear and co-directed. The two identical conduction electrons carry equal momentum `x`.

Thus

```math
P=2x+z,
```

and

```math
F(P)=\min_{0\le z\le P}
\left[
2\varepsilon\!\left(\frac{P-z}{2}\right)+E_s(z)
\right].
```

At an interior minimum the standard threshold stationarity condition is equality of final group velocities:

```math
\boxed{
\varepsilon'(x)=E_s'(z).
}
```

This equal-group-velocity condition is classical impact-ionization/Auger threshold theory and is **not** a novelty claim.

---

## 5. Strictly decreasing kinematic mismatch

Define

```math
\boxed{D(P)=F(P)-\varepsilon(P).}
```

At `P=0`,

```math
D(0)=\Delta+E_s(0)>0.
```

At an interior minimizing point, the envelope theorem gives

```math
F'(P)=\varepsilon'(x).
```

Since

```math
P=2x+z>x
```

for every nonzero final state, and `epsilon'(p)` is strictly increasing,

```math
\varepsilon'(x)<\varepsilon'(P).
```

Hence

```math
\boxed{D'(P)<0.}
```

Boundary minimizers obey the same strict inequality by the one-sided envelope derivative.

Therefore:

```text
the mismatch decreases monotonically;
there is at most one finite opening threshold.
```

---

## 6. Exact large-momentum limit

For fixed spectator momentum `z`,

```math
2\varepsilon\!\left(\frac{P-z}{2}\right)-\varepsilon(P)
\longrightarrow -vz
\qquad(P\to\infty).
```

Under the stated convexity/recession assumptions for the infimal convolution,

```math
\boxed{
D_\infty
\equiv\lim_{P\to\infty}D(P)
=
\inf_{p\ge0}\left[E_s(p)-vp\right].
}
```

In wave-vector notation,

```math
\boxed{
D_\infty
=\inf_{k\ge0}\left[E_s(k)-\hbar vk\right].
}
```

Equivalently this is the negative Legendre-Fenchel transform of the spectator dispersion evaluated at slope `v`:

```math
D_\infty=-E_s^*(v)
```

when physical momentum is the transform variable.

---

## 7. General exact closure/opening classification

Because `D(0)>0` and `D(P)` decreases strictly:

### Strictly closed

If

```math
\boxed{
\inf_{p\ge0}[E_s(p)-vp]>0,
}
```

then the spectator-assisted CCCH channel has no support at any finite energy.

### Asymptotically marginal

If

```math
\boxed{
\inf_{p\ge0}[E_s(p)-vp]=0,
}
```

then `D(P)>0` at every finite `P` and tends to zero only asymptotically.

### Open

If

```math
\boxed{
\inf_{p\ge0}[E_s(p)-vp]<0,
}
```

then there is exactly one finite threshold.

Therefore exact finite-energy closure is equivalent to the geometric condition

```math
\boxed{
E_s(p)\ge vp
\quad\text{for every }p\ge0.
}
```

or

```math
\boxed{
E_s(k)\ge\hbar vk
\quad\text{for every }k\ge0.
}
```

---

## 8. Spectator critical velocity

Define

```math
\boxed{
 v_s^{crit}
\equiv
\inf_{p>0}\frac{E_s(p)}{p}
=
\inf_{k>0}\frac{E_s(k)}{\hbar k}.
}
```

Then

```math
\boxed{
 v\le v_s^{crit}
\Longleftrightarrow
\text{no finite-energy spectator-assisted CCCH support.}
}
```

This is the general version of the heavy-hole theorem.

### Important novelty boundary

The mathematical structure

```math
v_c=\inf E(p)/p
```

is the same critical phase-velocity construction as the **Landau criterion** for emission of excitations by a moving object. Semiconductor impact-ionization threshold theory also long ago established equal final-state group velocities at threshold.

Therefore:

```text
THE SPECTATOR CRITICAL-VELOCITY FORMULA IS NOT CLAIMED AS A NEW GENERAL KINEMATIC PRINCIPLE.
```

Its role here is as a clean reduction of the multiband detector constraint.

---

## 9. Parabolic heavy-hole corollary

For

```math
E_s(p)=E_0+\frac{p^2}{2M_s},
\qquad
E_0=\Delta+\delta_s,
```

minimizing `E_s(p)/p` gives

```math
p_*=\sqrt{2M_sE_0},
```

and

```math
\boxed{
 v_s^{crit}=\sqrt{\frac{2E_0}{M_s}}.
}
```

Thus

```math
\boxed{
M_sv^2\le2E_0
=2(\Delta+\delta_s),
}
```

recovering the previous heavy-hole result exactly.

For a linear asymptotic spectator dispersion

```math
E_s(p)=E_0+u_s p,
```

one obtains

```math
v_s^{crit}=u_s.
```

A spectator branch whose asymptotic speed is below the active Dirac speed therefore opens the channel at sufficiently high momentum.

---

## 10. Multiple spectator bands

For spectator branches `s=1,...,N`, exact closure against every normal-momentum channel requires

```math
\boxed{
 v\le v_{spec}
\equiv\min_s v_s^{crit}.
}
```

The most dangerous spectator is the one with the smallest minimum excitation phase velocity.

This is a band-structure constraint, not a new scalar detector figure of merit.

---

# Part II — consistency repair: spectator holes shift intrinsic neutrality

## 11. The previous equality Sigma=C/v^2 is no longer exact

The original two-band matched-absorptance calculation assumed particle-hole symmetry and therefore

```math
\mu=0.
```

Adding any thermally accessible spectator **hole** band changes charge neutrality.

Let

```math
n_c(\mu)
```

be the active conduction-electron density,

```math
p_l(\mu)
```

the active light-hole density, and

```math
p_s(\mu)>0
```

the sum of spectator-hole densities.

Charge neutrality requires

```math
n_c(\mu)=p_l(\mu)+p_s(\mu).
```

At `mu=0`, active particle-hole symmetry gives

```math
n_c(0)=p_l(0),
```

so the extra spectator holes make the right-hand side larger.

Because `n_c(mu)` increases monotonically with `mu` while every hole density decreases,

```math
\boxed{\mu>0}
```

for the intrinsic multiband system.

Thus the exact two-band equality `Sigma=C/v^2` must not be reused unchanged.

---

## 12. The carrier-column result survives as a rigorous lower bound

For the active symmetric interband transition at energies `+-E`, the occupation difference is

```math
\boxed{
\mathcal P(E,\mu)
=f(-E;\mu)-f(E;\mu)
=
\frac{\sinh(E/k_BT)}
{\cosh(E/k_BT)+\cosh(\mu/k_BT)}.
}
```

At `mu=0`,

```math
\mathcal P(E,0)=\tanh(E/2k_BT).
```

Since `mu>0`,

```math
\boxed{
\mathcal P(E,\mu)\le\mathcal P(E,0).
}
```

Therefore the active-pair interband absorption coefficient at any fixed required photon energy obeys

```math
\boxed{\alpha_D(\mu)\le\alpha_D(0).}
```

At the same time,

```math
\boxed{n_c(\mu)\ge n_c(0).}
```

For the same required **single-pass active-pair optical depth** `zeta`,

```math
d(\mu)=\zeta/\alpha_D(\mu)
\ge
\zeta/\alpha_D(0)=d_0.
```

Hence

```math
\boxed{
\Sigma_c(\mu)=n_c(\mu)d(\mu)
\ge n_c(0)d_0
=\frac{C}{v^2}.
}
```

This repairs the three-band consistency problem:

```text
the old two-band expression becomes a lower bound rather than an equality.
```

Spectator holes make the active conduction-electron column worse, not better, **provided the useful optical-depth requirement is carried by the active Dirac transition**.

---

## 13. General exact-closure carrier-column bound

If exact spectator-assisted CCCH closure requires

```math
v\le v_{spec},
```

then the preceding lower bound immediately gives

```math
\boxed{
\Sigma_c
\ge
\frac{C}{v_{spec}^2}.
}
```

Including the independent lattice/Wannier resource

```math
v\le V_{hop},
```

define

```math
\boxed{
 v_{adm}=\min(V_{hop},v_{spec}).
}
```

Then

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

This is the general conditional Experiment-10 exact-closure carrier-column bound.

For the parabolic heavy-hole corollary,

```math
\boxed{
\Sigma_c
\ge
C\frac{M_{hh}}{2(\Delta+\delta_{hh})},
}
```

as derived previously.

---

## 14. Numerical neutrality witness at the parabolic closure boundary

Take the standard Experiment-10 target

```text
T = 300 K
lambda_c = 10 um
Delta/kBT = 2.39796
r = hbar omega / Eg = 1.2
```

and one spin-degenerate parabolic spectator hole band touching the active valence edge.

At the exact closure boundary

```math
\rho=M_{hh}v^2/\Delta=2,
```

solve the full Fermi-Dirac charge-neutrality equation rather than the Boltzmann approximation.

The solution is

```text
mu/kBT = 0.46384.
```

Relative to the two-band `mu=0` state,

```text
active conduction density increase = 1.5695x;
active interband occupation-factor ratio at r=1.2 = 0.98907;
matched active-electron column increase = 1.5869x.
```

Thus the old `C/v^2` value is conservative by about `59%` in this representative closure-boundary three-band case.

This numerical factor is not universal; degeneracies, offsets, and spectator dispersion change it.

---

# Part III — main limitation: optically active spectator bands

## 15. The general carrier-column bound is conditional on optical dominance of the active pair

The kinematic theorem itself does **not** require an optically dark spectator.

The detector-level composition does.

If the spectator band also contributes substantial useful absorption,

```math
\alpha_{tot}=\alpha_D+\alpha_s,
```

then the required thickness is

```math
d=\zeta/\alpha_{tot},
```

not `zeta/alpha_D`.

Without a microscopic upper bound on `alpha_s`, the active-electron column

```math
n_c d
```

can no longer be bounded from below by `C/v^2` using the active Dirac optical conductivity alone.

Therefore:

```math
\boxed{
\text{arbitrary optically active spectator strength prevents a universal }C/v_{spec}^2\text{ detector bound.}
}
```

This is a no-go on overgeneralizing the theorem.

A conditional extension is possible if one can bound

```math
\alpha_s\le\chi_{opt}\alpha_D.
```

Then

```math
d\ge\frac{\zeta}{(1+\chi_{opt})\alpha_D}
```

and

```math
\boxed{
\Sigma_c
\ge
\frac{C}{(1+\chi_{opt})v_{adm}^2}.
}
```

But `chi_opt` is a new microscopic optical resource and cannot be assumed universal.

---

## 16. Why this matters for HgCdTe

The heavy-hole band in actual Kane HgCdTe is not merely a silent Auger momentum reservoir. Magneto-optical work directly observes strong interband transitions involving the heavy-hole branch, and intrinsic absorption fits depend on heavy-hole mass and Kane parameters.

Therefore the simple conditional carrier-column theorem must **not** be presented as a quantitative bulk-HgCdTe bound.

Its correct scope is a hypothetical material class in which:

```text
a massive-Dirac active pair dominates the specified useful absorption;
nearby spectator bands can participate in Auger kinematics;
and their useful-band optical contribution is negligible or explicitly bounded.
```

---

# Part IV — novelty boundary

## 17. Established ingredients identified by the adversarial audit

The following are established and unavailable as novelty:

```text
impact-ionization/Auger thresholds obtained by minimizing final energy at fixed momentum;
equality of final-state group velocities at threshold for arbitrary differentiable bands;
Landau critical-velocity construction min[E(p)/p];
heavy-hole CCCH/Auger-1 in HgCdTe;
quasi-relativistic electron-hole symmetry as an Auger-suppression strategy;
multiband engineering of Auger thresholds in HgCdTe quantum wells;
infrared-detector alpha/G_th material figures of merit;
full radiative detailed balance and photon recycling.
```

The general spectator critical velocity is therefore best viewed as a **Landau-like reformulation of known threshold kinematics**, not a new principle.

## 18. Possible surviving contribution

A focused audit did not identify prior work that explicitly composes

```text
single-pass matched active-pair absorptance
+ exact finite-gap Dirac thermal statistics
+ active optical conductivity scaling
+ microscopic lattice velocity ceiling
+ spectator-band critical phase velocity
+ complete external optical-boundary comparison
```

into

```math
\boxed{
\Sigma_c\ge C/v_{adm}^2.
}
```

However, this may still be judged an elementary composition of known ingredients, and its detector-level generality is limited by spectator optical oscillator strength.

Therefore the correct disposition remains

```text
POSSIBLE CONDITIONAL JOINT ADMISSIBILITY THEOREM / NOVELTY NOT ESTABLISHED / UNIVERSAL VERSION FALSE WITHOUT OPTICAL-SPECTATOR CONSTRAINT.
```

---

## 19. What is established now

```text
DERIVED:
    arbitrary-convex-spectator CCCH closure criterion
    E_s(p) >= v p for all p;

DERIVED:
    v_s^crit = inf E_s(p)/p;

RECOGNIZED PRIOR ART STRUCTURE:
    this is Landau-like and equal-group-velocity threshold physics is classical;

DERIVED:
    multiple-spectator ceiling v_spec=min_s v_s^crit;

CORRECTED:
    spectator-hole neutrality shifts mu positive, so Sigma=C/v^2 is not an equality;

DERIVED:
    the shift increases carrier density and weakens active-pair absorption, therefore Sigma >= C/v^2 remains rigorous for the stated active-pair optical-depth requirement;

DERIVED:
    Sigma >= C/min(V_hop,v_spec)^2;

DERIVED NO-GO:
    unconstrained spectator optical absorption destroys the universal detector-level bound.
```

---

## 20. Next action

Do **not** add another recombination mechanism yet.

The next decision is whether the surviving **conditional** theorem is strong enough for a paper.

Perform a final theorem-level novelty audit focused on:

```text
1. infrared-detector alpha/G_th optimization versus matched optical depth;
2. arbitrary-band impact-ionization threshold theory beyond parabolic bands;
3. Landau/Cherenkov-like emission criteria in semiconductor carrier scattering;
4. multiband low-DOS / high-optical-matrix-element detector design;
5. whether any prior work derives an optical-column lower bound from an Auger-closure velocity ceiling.
```

If no direct collision appears, compress the result into theorem / corollary / limitation form and assess manuscript viability. If the surviving theorem is too conditional or too obviously compositional, close Experiment 10 rather than accumulating further physics.