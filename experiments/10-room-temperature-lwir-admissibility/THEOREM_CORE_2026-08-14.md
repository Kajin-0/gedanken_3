# Experiment 10 — Theorem Core After Adversarial Audit

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** **PROVISIONAL THEOREM PACKAGE / NOVELTY NOT ESTABLISHED / READY FOR HOSTILE THEOREM REVIEW, NOT MANUSCRIPT DRAFTING**

## 1. Controlled material class

Assume a homogeneous, reciprocal, single-pass absorber with one finite-gap 3-D massive-Dirac pair providing the specified useful optical transition:

```math
\varepsilon(p)=\sqrt{\Delta^2+v^2p^2},
\qquad
E_g=2\Delta.
```

Assume:

```text
1. fixed T, Eg, target photon energy and required active-pair optical depth;
2. active-pair useful absorption dominates, or spectator optical absorption is separately bounded;
3. normal crystal momentum (no Umklapp or momentum-assisting disorder/phonons in the theorem);
4. spectator hole dispersions are positive, isotropic, continuous, convex and nondecreasing over the model-valid momentum range;
5. exact-closure statements concern the continuum model unless a finite validity window is stated;
6. finite-gap Dirac statistics and Pauli factors are retained;
7. the complete external optical boundary is matched separately when comparing irreversible radiative/background traffic.
```

These hypotheses are part of the result. Removing them can invalidate the bound.

---

# Theorem 1 — spectator-band Auger closure ceiling

For spectator hole branch `s` with excitation energy `E_s(p)`, define

```math
\boxed{
 v_s^{crit}
=\inf_{p>0}\frac{E_s(p)}{p}.
}
```

For inverse spectator-assisted CCCH impact ionization

```text
e_0 -> e_1 + e_2 + h_s,
```

with the active conduction dispersion above, exact finite-energy normal-momentum kinematic closure holds iff

```math
\boxed{v\le v_s^{crit}.}
```

Equivalently,

```math
\boxed{E_s(p)\ge vp\quad\forall p\ge0.}
```

If the inequality is strict in the asymptotic infimum, the channel is strictly closed. Equality gives an asymptotically marginal channel. Violation gives one unique finite opening threshold under the convexity hypotheses.

### Proof sketch

Define

```math
F_s(P)
=\min_{\mathbf p_1+\mathbf p_2+\mathbf p_s=\mathbf P}
[\varepsilon(p_1)+\varepsilon(p_2)+E_s(p_s)]
```

and `D_s(P)=F_s(P)-epsilon(P)`.

Convexity makes the threshold minimizer collinear and the two final electrons equal. The final-state group velocities are equal at an interior minimum. Since the initial momentum exceeds either final-electron momentum and `epsilon'(p)` is strictly increasing,

```math
D_s'(P)<0.
```

Also

```math
D_s(0)=\Delta+E_s(0)>0.
```

Finally,

```math
\lim_{P\to\infty}D_s(P)
=\inf_p[E_s(p)-vp].
```

The classification follows.

### Prior-art status

The equal-group-velocity threshold condition is classical semiconductor impact-ionization/Auger theory. The form `inf E(p)/p` is mathematically the Landau critical-velocity construction. The theorem is therefore a specialization/repackaging for this detector model, not a claimed new kinematic principle.

---

# Corollary 1 — multiple spectator bands

For spectator branches `s=1,...,N`, define

```math
\boxed{
 v_{spec}=\min_s v_s^{crit}.
}
```

Exact finite-energy closure against all such normal-momentum spectator-assisted channels requires

```math
\boxed{v\le v_{spec}.}
```

The most dangerous band is the one with the smallest excitation phase velocity.

---

# Corollary 2 — parabolic heavy-hole branch

For

```math
E_{hh}(p)=\Delta+\delta_{hh}+\frac{p^2}{2M_{hh}},
```

```math
\boxed{
 v_{hh}^{crit}
=\sqrt{\frac{2(\Delta+\delta_{hh})}{M_{hh}}}.
}
```

Thus exact closure requires

```math
\boxed{
M_{hh}v^2\le2(\Delta+\delta_{hh}).
}
```

This reproduces `THIRD_BAND_HEAVY_HOLE_AUGER_ESCAPE_STEP_2026-08-14.md`.

---

# Theorem 2 — active-pair matched-column lower bound survives spectator-hole neutrality

At `mu=0`, the active massive-Dirac pair has

```math
n_0(v)
=\frac{N_D}{\pi^2}
\left(\frac{k_BT}{\hbar v}\right)^3F_2(\Delta/k_BT),
```

and active-pair absorption at fixed normalized photon energy has

```math
\alpha_0(v)=\frac{K_\alpha}{v},
```

where `K_alpha` contains the fixed gap/temperature/optical factors.

For required single-pass active-pair optical depth

```math
\zeta=-\ln(1-A),
```

```math
d_0=\zeta/\alpha_0\propto v.
```

Therefore

```math
\boxed{
\Sigma_0=n_0d_0=\frac{C}{v^2},
}
```

where exactly

```math
\boxed{
C
=\frac{3n_b\zeta F_2(\Delta/k_BT)}
{\pi^2\alpha_{fs}Q(r,\Delta/k_BT)}
\frac{(k_BT)^3}{\hbar^3\omega}.
}
```

Now add any number of thermally accessible **spectator hole** bands while retaining the active pair.

Intrinsic charge neutrality shifts the chemical potential positive:

```math
\boxed{\mu>0.}
```

Hence

```math
n_c(\mu)\ge n_c(0).
```

For the active symmetric transition at energies `+-E`, the occupation difference is

```math
\mathcal P(E,\mu)
=\frac{\sinh(E/k_BT)}
{\cosh(E/k_BT)+\cosh(\mu/k_BT)}
\le\mathcal P(E,0).
```

Thus

```math
\alpha_D(\mu)\le\alpha_D(0).
```

For the same required active-pair single-pass optical depth,

```math
d(\mu)\ge d_0.
```

Therefore

```math
\boxed{
\Sigma_c=n_c(\mu)d(\mu)
\ge\frac{C}{v^2}.
}
```

The earlier two-band equality becomes a rigorous lower bound after spectator-hole neutrality is restored.

---

# Theorem 3 — conditional electronic-structure admissibility bound

The microscopic lattice resource gives

```math
v\le V_{hop}.
```

Exact closure against the spectator set gives

```math
v\le v_{spec}.
```

Define

```math
\boxed{
 v_{adm}=\min(V_{hop},v_{spec}).
}
```

Then any member of the controlled absorber class satisfying the required active-pair optical depth and exact spectator-assisted CCCH closure obeys

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

For one parabolic heavy-hole spectator,

```math
\boxed{
\Sigma_c
\ge
\max\!\left[
\frac{C}{V_{hop}^2},
C\frac{M_{hh}}{2(\Delta+\delta_{hh})}
\right].
}
```

This is the strongest current Experiment-10 theorem candidate.

---

# No-go 1 — arbitrary spectator optical strength destroys universality

If the spectator also supplies useful absorption,

```math
\alpha_{tot}=\alpha_D+\alpha_s,
```

then required thickness is set by `alpha_tot`, not `alpha_D`.

Without a microscopic bound on `alpha_s/alpha_D`, no universal lower bound proportional to `C/v_adm^2` follows from the active-pair optical law.

Therefore

```math
\boxed{
\text{the theorem is conditional on active-pair optical dominance or bounded spectator optical strength.}
}
```

If

```math
\alpha_s\le\chi_{opt}\alpha_D,
```

then a weakened conditional bound is

```math
\boxed{
\Sigma_c\ge
\frac{C}{(1+\chi_{opt})v_{adm}^2}.
}
```

No universal `chi_opt` has been established.

---

# No-go 2 — unrestricted photonic path enhancement destroys the single-pass column bound

The step

```math
d=\zeta/\alpha
```

is a single-pass/homogeneous-absorber statement.

A resonant cavity, grating, slow-light structure or other field-enhancement mechanism can increase effective optical path length and reduce physical absorber thickness at fixed external absorptance.

Therefore arbitrary photonic enhancement is another escape from a universal physical carrier-column floor.

The natural way to close this loophole would be to impose the founding finite-temporal-response requirement and derive an optical path-enhancement / dwell-time / bandwidth bound.

That derivation has **not** yet been done.

---

# No-go 3 — exact Auger closure is sufficient, not necessary, for a radiative-limited detector

The detector only requires

```math
\Xi_{nr}^{ext}\lesssim1,
```

not exact kinematic closure of every nonradiative channel.

Therefore Theorem 3 gives a clean sufficient-condition bound, not the globally optimal room-temperature material boundary.

Finite but exponentially suppressed Auger rates can permit larger `v` than exact closure.

---

# Numerical witness

For the standard single-pass 10-um/300-K witness

```text
A = 0.90
r = 1.2
n_b = 3.5
```

```math
C=1.06668\times10^{29}\ \mathrm{m^{-2}(m/s)^2}.
```

For a touching parabolic spectator with `M_hh=0.5m0`, exact closure requires

```text
v <= 2.088e5 m/s
```

and the basic theorem gives

```math
\Sigma_c\ge2.446\times10^{14}\ \mathrm{cm^{-2}}.
```

Restoring spectator-hole charge neutrality at the exact closure boundary for one spin-degenerate spectator gives

```text
mu/kBT = 0.46384
n_c/n_c(mu=0) = 1.5695
active absorption occupation factor = 0.98907 of mu=0
matched active-electron column = 1.5869 x the basic lower bound
```

for the `r=1.2` witness.

Thus the theorem is conservative in this example.

---

# Novelty disposition

The constituent kinematic ideas are established, and the closest detector literature already combines accurate band structures, optical absorption, Auger suppression and ideal detector performance.

The focused audit has not located this exact conditional lower-bound composition, but a hostile reviewer could reasonably characterize it as an elementary synthesis of known results.

Therefore:

```text
THEOREM MATHEMATICALLY DEFENSIBLE UNDER STATED HYPOTHESES.
BROAD PHYSICS NOT NOVEL.
EXACT COMPOSED BOUND NOT FOUND IN FOCUSED SEARCH.
NOVELTY NOT ESTABLISHED.
```

# Next decisive question

The largest remaining escape from the theorem is now optical, not electronic:

> Can arbitrary optical path enhancement evade the matched carrier-column floor while preserving a specified detector temporal response/bandwidth, or does passivity impose a path-enhancement / dwell-time tradeoff that restores a generalized bound?

This question reconnects Experiment 10 to its original requirement of useful temporal response and should be attacked before any manuscript decision.