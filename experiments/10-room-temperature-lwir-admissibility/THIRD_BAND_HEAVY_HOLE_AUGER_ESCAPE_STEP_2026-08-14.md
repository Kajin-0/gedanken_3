# Experiment 10 — Third-Band Heavy-Hole Auger Escape Condition

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Disposition:** **EXACT THREE-BAND KINEMATIC OPENING CONDITION DERIVED / HIGH-v AND EXTRA-BAND PROTECTION SHOWN TO COMPETE / FLAT-HEAVY-HOLE LIMIT RECOVERS LOW AUGER-1 THRESHOLD / BROAD PHYSICS IS PRIOR ART / NOVELTY NOT ESTABLISHED**

## 1. Question for this step

The two-band Experiment-10 model established exact direct-Auger closure for a particle-hole-symmetric finite-gap massive-Dirac pair. That protection is fragile because real narrow-gap Kane systems can contain a heavy-hole or other spectator band that supplies momentum at low energetic cost.

This step therefore asks:

> Add one isotropic heavy-hole-like valence reservoir to the high-v symmetric active pair. Under exact energy and crystal-momentum conservation, when is the normal-momentum CCCH / Auger-1 channel closed, marginal, or open?

No empirical Auger lifetime and no Coulomb matrix element is inserted. This is a pure kinematic support problem.

---

## 2. Minimal three-band model

Retain the active conduction/light-hole massive-Dirac pair with positive quasiparticle energy

```math
\varepsilon(k)=\sqrt{\Delta^2+(\hbar vk)^2},
\qquad
\Delta=E_g/2>0.
```

Add a heavy-hole-like hole excitation branch

```math
E_{hh}(k)
=\Delta+\delta_{hh}
+\frac{\hbar^2k^2}{2M_{hh}}.
```

Here

```text
M_hh > 0
```

is the heavy-hole effective mass and

```text
delta_hh
```

is the heavy-hole hole-excitation offset relative to the active valence edge. For the cleanest active-gap comparison use `delta_hh >= 0`; then the extra valence band lies no higher than the active valence edge.

Define dimensionless variables

```math
q=\frac{\hbar vk}{\Delta},
```

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
\boxed{
\eta=\frac{\delta_{hh}}{\Delta}.
}
```

Then

```math
e(q)=\frac{\varepsilon}{\Delta}=\sqrt{1+q^2},
```

and

```math
h(q)=\frac{E_{hh}}{\Delta}
=1+\eta+\frac{q^2}{2\rho}.
```

The parameter `rho` measures how cheaply the spectator band can carry crystal momentum compared with the active Dirac sector.

---

## 3. CCCH / inverse-impact-ionization channel

Use the inverse process

```text
e_0 -> e_1 + e_2 + h_hh,
```

with normal crystal momentum

```math
\mathbf q_0
=\mathbf q_1+\mathbf q_2+\mathbf q_3.
```

At fixed total momentum magnitude `q`, define the minimum final excitation energy

```math
\mathcal F_{\rho,\eta}(q)
=
\min_{\mathbf q_1+\mathbf q_2+\mathbf q_3=\mathbf q}
\left[
e(q_1)+e(q_2)+h(q_3)
\right].
```

The channel is on shell if

```math
e(q)\ge \mathcal F_{\rho,\eta}(q).
```

The threshold is the first equality.

---

## 4. Exact minimizer structure

All three positive-energy dispersions are isotropic and strictly convex. At the constrained minimum, their group-velocity vectors are equal to the same Lagrange multiplier.

Thus the minimizing momenta are collinear and co-directed. The two identical conduction electrons carry equal momentum.

Write

```math
q_1=q_2=x,
\qquad
q_3=z,
\qquad
q=2x+z.
```

Introduce the common dimensionless velocity

```math
u
=\frac{x}{\sqrt{1+x^2}}
=\frac{z}{\rho},
\qquad 0\le u<1.
```

Then exactly

```math
\boxed{
x(u)=\frac{u}{\sqrt{1-u^2}},
\qquad
z(u)=\rho u,
}
```

and

```math
\boxed{
q(u)
=\frac{2u}{\sqrt{1-u^2}}+\rho u.
}
```

The minimized final energy is

```math
\boxed{
\mathcal F(u)
=\frac{2}{\sqrt{1-u^2}}
+1+\eta
+\frac{\rho u^2}{2}.
}
```

This parametrizes the exact fixed-total-momentum lower envelope.

---

## 5. Exact monotonic mismatch theorem

Define the kinematic mismatch

```math
D(q)
=\mathcal F_{\rho,\eta}(q)-e(q).
```

At `q=0`,

```math
\boxed{D(0)=2+\eta>0}
```

for the physical hole branch.

By the envelope theorem,

```math
\frac{d\mathcal F}{dq}=u.
```

But the initial Dirac-electron slope is

```math
\frac{de(q)}{dq}=\frac{q}{\sqrt{1+q^2}}.
```

At every nonzero constrained minimum,

```math
q=2x+z>x,
```

and `q/sqrt(1+q^2)` is strictly increasing. Since

```math
u=\frac{x}{\sqrt{1+x^2}},
```

it follows that

```math
\boxed{
D'(q)
=u-\frac{q}{\sqrt{1+q^2}}<0.
}
```

Therefore the mismatch decreases strictly with total momentum. There can be at most one finite opening threshold.

---

## 6. Large-momentum limit and exact closure/opening criterion

As `q -> infinity`, the common velocity tends to one:

```math
u\to1,
```

so

```math
x\to\infty,
\qquad
z\to\rho.
```

The heavy-hole branch asymptotically carries only the finite momentum `rho`, while the two Dirac electrons carry the remainder.

Evaluating the asymptotic energy difference gives

```math
\boxed{
\lim_{q\to\infty}D(q)
=1+\eta-\frac{\rho}{2}.
}
```

Because `D(q)` is strictly decreasing, the full kinematic disposition follows immediately.

### Closed

If

```math
\boxed{
\rho<2(1+\eta),
}
```

then

```math
D(q)>0
```

for every finite `q`, so the normal-momentum CCCH channel has empty support.

### Marginal

If

```math
\boxed{
\rho=2(1+\eta),
}
```

then `D(q)>0` at every finite momentum and tends to zero only as `q -> infinity`. The channel is asymptotically marginal but not on shell at finite energy.

### Open

If

```math
\boxed{
\rho>2(1+\eta),
}
```

then `D(q)` crosses zero exactly once. The CCCH channel opens at a unique finite threshold.

Therefore the exact three-band closure condition is

```math
\boxed{
\frac{M_{hh}v^2}{\Delta}
\le
2\left(1+\frac{\delta_{hh}}{\Delta}\right).
}
```

Equivalent forms are

```math
\boxed{
M_{hh}
\le
\frac{2(\Delta+\delta_{hh})}{v^2},
}
```

```math
\boxed{
v
\le
\sqrt{\frac{2(\Delta+\delta_{hh})}{M_{hh}}},
}
```

or, for a given `M_hh` and `v`,

```math
\boxed{
\delta_{hh}
\ge
\frac{M_{hh}v^2}{2}-\Delta.
}
```

The last form is a sufficient offset requirement when the right-hand side is positive.

---

## 7. Main conceptual consequence — high v and spectator-band protection compete

The two-band matched-absorptance result favored increasing `v` because

```math
\Sigma_e\propto v^{-2}.
```

But for a fixed heavy-hole band,

```math
\rho=\frac{M_{hh}v^2}{\Delta}\propto v^2.
```

Thus increasing `v` drives the third-band system **toward** the CCCH opening condition.

This is the first Experiment-10 mechanism that creates a direct conflict with the high-`v` thermodynamic lever:

```text
large v:
    lowers matched thermal carrier column;

large v at fixed spectator-band mass/offset:
    makes the spectator hole effectively heavier relative to the active Dirac sector and eventually reopens CCCH.
```

Therefore `v` cannot be optimized independently of the full nearby-band structure.

A convenient kinematic ratio is

```math
\chi_{hh}
=\frac{M_{hh}v^2}{2(\Delta+\delta_{hh})}.
```

Then

```text
chi_hh < 1  -> exact finite-energy closure;
chi_hh = 1  -> asymptotically marginal;
chi_hh > 1  -> unique finite threshold.
```

This ratio is bookkeeping for the theorem, not a claimed new detector figure of merit.

---

## 8. Exact threshold when the channel is open

For

```math
\rho>2(1+\eta),
```

the threshold is obtained from the unique `u_th in (0,1)` satisfying

```math
\boxed{
\sqrt{1+q(u)^2}
=
\frac{2}{\sqrt{1-u^2}}
+1+\eta
+\frac{\rho u^2}{2},
}
```

with

```math
q(u)=\frac{2u}{\sqrt{1-u^2}}+\rho u.
```

The hot-electron kinetic threshold above the active conduction edge is

```math
\boxed{
K_{th}^{hh}
=\Delta\left[
\sqrt{1+q_{th}^2}-1
\right].
}
```

This is reproduced by `numerics/third_band_heavy_hole_threshold.py`.

---

## 9. Rigorous threshold lower bound

Regardless of momentum sharing,

```math
e(q_1)\ge1,
\qquad
e(q_2)\ge1,
\qquad
h(q_3)\ge1+\eta.
```

Therefore every on-shell event satisfies

```math
\sqrt{1+q_{th}^2}
\ge3+\eta.
```

Hence

```math
\boxed{
\frac{K_{th}^{hh}}{\Delta}
\ge2+\eta,
}
```

or physically

```math
\boxed{
K_{th}^{hh}
\ge E_g+\delta_{hh}.
}
```

The lower bound is approached when the spectator hole becomes perfectly flat (`M_hh -> infinity`).

Thus a heavy spectator band destroys exact two-band Auger closure but does not make the direct threshold vanish in this model.

---

## 10. Flat-heavy-hole limit

For

```math
\rho\to\infty,
```

the heavy hole carries the required momentum at asymptotically zero kinetic-energy cost. The two final conduction electrons can sit at their band minima.

Therefore

```math
\boxed{
K_{th}^{hh}
\to E_g+\delta_{hh}.
}
```

For a heavy-hole band touching the active valence edge,

```math
\delta_{hh}=0,
```

so

```math
\boxed{K_{th}^{hh}\to E_g.}
```

This is the expected low-threshold CCCH / Auger-1 limit.

The simplified 6-band Kane description of bulk HgCdTe explicitly contains a nearly flat heavy-hole branch intersecting the electron/light-hole sector at the Gamma point, so the ideal two-band no-go cannot be transferred to bulk HgCdTe by simply invoking its Kane velocity.

---

## 11. Asymptotic threshold laws

### Just above the opening boundary

Let

```math
\rho_c=2(1+\eta)
```

and

```math
0<\rho-\rho_c\ll1.
```

The large-`q` mismatch has

```math
D(q)
=
-\frac{\rho-\rho_c}{2}
+\frac{3}{2q}
+O(q^{-2}).
```

Therefore

```math
\boxed{
q_{th}
\sim
\frac{3}{\rho-\rho_c},
}
```

and the threshold diverges as

```math
\boxed{
\frac{K_{th}^{hh}}{\Delta}
\sim
\frac{3}{\rho-\rho_c}.
}
```

So the extra-band channel turns on continuously from infinite threshold as the kinematic boundary is crossed.

### Very heavy spectator band

For `rho >> 1`,

```math
\boxed{
\frac{K_{th}^{hh}}{\Delta}
=
2+\eta
+\frac{(3+\eta)^2-1}{2\rho}
+O(\rho^{-2}).
}
```

For `eta=0`,

```math
\boxed{
\frac{K_{th}^{hh}}{E_g}
=1+\frac{2}{\rho}+O(\rho^{-2}).
}
```

The threshold rapidly approaches the conventional `~E_g` heavy-hole limit.

---

## 12. 10-um / 300-K witness for a touching spectator band

Set

```text
eta = 0
Eg/kBT = 4.795922925.
```

Then the exact dimensionless thresholds are

```text
rho=M_hh/m_D     q_th       K_th/Eg      K_th/kBT     exp[-(K_th-Eg/2)/kBT]
2.1               32.699      15.857        76.049       1.03e-32
2.5                8.814       3.935        18.874       6.99e-08
3                  5.909       2.496        11.972       6.95e-05
4                  4.474       1.792         8.596       2.03e-03
5                  3.980       1.552         7.442       6.45e-03
10                 3.306       1.227         5.884       3.06e-02
20                 3.052       1.106         5.303       5.47e-02
50                 2.915       1.041         4.992       7.47e-02
100                2.871       1.020         4.893       8.25e-02
infinity            2.828       1.000         4.796       9.09e-02
```

Thus once the spectator band becomes truly heavy relative to the tiny Dirac edge mass, the enormous two-band Auger threshold collapses toward `E_g`.

---

## 13. Interaction with the radiative activation-parity line

The external radiative boundary floor has activation `exp[-E_g/(k_BT)]`. The direct extra-band Auger event rate carries the hot-electron activation

```math
\exp[-(E_g/2+K_{th}^{hh})/(k_BT)].
```

Therefore the exponent-only ratio remains

```math
\exp[-(K_{th}^{hh}-E_g/2)/(k_BT)].
```

But the rigorous three-band lower bound gives

```math
K_{th}^{hh}\ge E_g+\delta_{hh}.
```

For `delta_hh >= 0`,

```math
\boxed{
K_{th}^{hh}-E_g/2
\ge E_g/2+\delta_{hh}>0.
}
```

So this minimal heavy-hole escape channel is still on the favorable side of the radiative **activation exponent** even when it is open.

In the worst flat touching-band limit (`delta_hh=0`), the extra thermal factor relative to the radiative floor is only

```math
\boxed{
\exp[-E_g/(2k_BT)].
}
```

At 10 um / 300 K this is

```math
\boxed{0.0909.}
```

This is far weaker than the `~5e-4` factor obtained for the deliberately symmetric two-band `K_th=10 kBT` witness. Therefore a heavy spectator band can erase most of the symmetry-derived exponential advantage even though it does not reverse activation parity.

Whether `Xi_A^ext <= 1` then holds depends on the extra-band density of states, Coulomb/spinor matrix element, screening, and degeneracy prefactors. Kinematics alone cannot settle the full event-rate inequality once the band is open.

---

## 14. High-v design conflict made explicit

For fixed `M_hh` and `delta_hh`, exact closure requires

```math
\boxed{
v\le v_c^{hh}
=\sqrt{\frac{2(\Delta+\delta_{hh})}{M_{hh}}}.
}
```

But matched thermal carrier column improves as

```math
\Sigma_e\propto v^{-2}.
```

Therefore a material cannot simultaneously take `v -> infinity` and retain exact heavy-hole-channel closure unless the spectator band itself changes:

```text
M_hh must decrease roughly as v^-2;

or delta_hh must increase roughly as M_hh v^2/2;

or symmetry/coupling must eliminate the matrix element by another mechanism.
```

This is a genuine multiband admissibility tradeoff absent from the two-band analysis.

At the fixed 10-um target with `delta_hh=0`, the exact closure mass ceiling is

```math
M_{hh}^{max}=\frac{E_g}{v^2}.
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

Thus a `v ~ 1e6 m/s` active pair can retain exact CCCH closure only if a touching spectator hole band is extremely light on the free-electron mass scale. A conventional heavy-hole branch lies on the open side of this toy-model condition.

---

## 15. Prior-art boundary

The broad physical conclusion is established territory and cannot be claimed as novelty:

1. Bulk narrow-gap HgCdTe Auger-1 / CCCH is a standard process in which a conduction electron recombines with a heavy hole and excites another conduction electron. Jiang, Teich, and Wang, *J. Appl. Phys.* **69**, 6869–6875 (1991), DOI `10.1063/1.347676`, explicitly formulate this channel for bulk HgCdTe.

2. Ciesla et al., *Phys. Status Solidi B* **204**, 121–124 (1997), report theory/experiment in highly excited HgCdTe with Auger-1 dominant over their studied temperature range and Auger-7 becoming significant in the intrinsic high-temperature regime.

3. Orlita et al. / Teppe and co-workers' simplified Kane description of HgCdTe contains an electron/light-hole quasi-relativistic sector crossed by a flat heavy-hole branch; see the bulk Kane-fermion magneto-optical literature, including *Nature Communications* **7**, 12576 (2016).

4. Modern HgCdTe-QW work deliberately engineers band dispersions to suppress Auger channels and demonstrates radiative-dominated operation when the threshold structure is favorable; see Alymov et al., *ACS Photonics* **7**, 98–104 (2020), and Morozov et al., *ACS Photonics* **8**, 3526–3535 (2021).

Therefore

```text
"heavy-hole bands reopen HgCdTe Auger" = ESTABLISHED PRIOR ART.
```

The retained result here is the exact reduced-model closure/opening theorem

```math
M_{hh}v^2\lessgtr2(\Delta+\delta_{hh})
```

and its role inside the broader Experiment-10 matched-optical-boundary admissibility construction. Novelty of that compact theorem or of the eventual combined framework is **not established**.

---

## 16. What has been established

```text
DERIVED:
    exact fixed-momentum minimum for a Dirac-electron + Dirac-electron + parabolic-heavy-hole final state;

DERIVED:
    mismatch is strictly decreasing with total momentum;

DERIVED:
    exact closure/marginality/opening criterion
    M_hh v^2 <=,=,> 2(Delta + delta_hh);

DERIVED:
    unique finite threshold on the open side;

DERIVED:
    near-boundary divergence K_th/Delta ~ 3/(rho-rho_c);

DERIVED:
    flat-heavy-hole limit K_th -> Eg + delta_hh;

DERIVED:
    extra band creates the first direct conflict with the high-v thermodynamic lever;

DERIVED:
    for delta_hh >= 0, the open heavy-hole channel remains on the favorable side of radiative activation parity, but can erase most of the stronger symmetry-derived exponential margin.
```

## 17. What is not established

```text
full extra-band Auger rate;
heavy-hole spinor/Coulomb overlap;
exchange contribution;
heavy-hole degeneracy and anisotropic/warped DOS;
multiple spectator bands;
phonon/Umklapp assistance;
real-material tightness of the isotropic parabolic spectator model;
that Xi_A^ext <= 1 once the heavy-hole channel is open;
novelty of the compact closure theorem or combined framework.
```

---

## 18. Hard stop and next question

The third-band kinematic support is now resolved for the minimal isotropic model.

The next question should not be another threshold calculation. It is:

> Once the heavy-hole channel is open, does its large spectator-band density of states and Coulomb/spinor coupling inevitably overwhelm the fixed external radiative floor at the 10-um / 300-K target, or is there still a calculable prefactor/offset regime with `Xi_hh^ext <= 1`?

The next step should derive the **near-threshold heavy-hole CCCH phase-space and v/M_hh scaling** while keeping the multiband overlap as an explicit remainder. This is necessary because the exponent alone is no longer decisive in the flat/heavy-band limit.
