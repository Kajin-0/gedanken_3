# Progress Log — Experiment 10: Room-Temperature LWIR Material Admissibility

**Scope:** analytical/theoretical only.  
**Fixed target:** `T=300 K`, `lambda_c=10 um`, `Eg=0.123984 eV`, `Eg/kBT ~= 4.796`.

---

## 2026-08-14 — branch initialization

Created `experiment-10-room-temperature-lwir-admissibility` to derive a finite-gap band-structure admissibility theorem/bound rather than rank materials.

Immediate novelty exclusions: generic `alpha/G_th`, `alpha sqrt(tau)`, low-`n_i` arguments, radiative detailed balance, generic Auger suppression, and Experiment-08 zero-gap Kane statistics.

---

## 2026-08-14 — matched massive-Dirac absorptance

For the controlled single-pass active pair,

```math
n_c\propto v^{-3},
\qquad
\alpha_D\propto v^{-1},
\qquad
\Sigma_c=C/v^2.
```

Adding spectator hole bands shifts `mu>0`, increases active electron density and weakens active-pair absorption, so the rigorous multiband statement becomes

```math
\boxed{\Sigma_c\ge C/v^2}
```

for the same required active-pair single-pass optical depth.

At the standard witness,

```math
C=1.06668\times10^{29}\ \mathrm{m^{-2}(m/s)^2}.
```

---

## 2026-08-14 — microscopic velocity resource

A Wannier Hamiltonian yields the conditional ceiling

```math
\boxed{v\le V_{hop}}
```

and therefore `Sigma >= C/V_hop^2` in the single-pass class.

Generic low-energy effective-mass, optical-sum and remote-band arguments did not yield a universal high-`v` ceiling.

---

## 2026-08-14 — two-band Auger sequence

Exact particle-hole-symmetric finite-gap massive-Dirac `eeh/hhe` direct Auger is kinematically closed.

Scalar particle-hole asymmetry reopens the direct channel with weak-asymmetry threshold

```math
\boxed{K_{th}\sim E_g\mathcal A_m^{-1/3}.}
```

At the fixed target, the scalar model needs about `A_m <= 0.0848` for `K_th >= 10 kBT`.

Interior threshold phase space scales as `(K-K_th)^2`; microscopic overlap zeros can add powers.

In the minimal weak-screening matched-area model, direct Auger retains approximately `v^-4` algebraic suppression times the threshold activation.

Broad Dirac/symmetric Auger suppression is prior art.

---

## 2026-08-14 — external radiative boundary

Corrected the optical comparison: useful front-side absorptance alone is insufficient. The complete external mode-resolved optical boundary must be matched.

At equilibrium,

```math
\Phi_{abs}^{ext}=\Phi_{em}^{ext}=\Phi_0.
```

Internal radiative recombination is not invariant because photon recycling changes internal event count.

Ideal 10-um/300-K hemispherical step benchmark:

```text
Phi_0 = 4.89777e17 cm^-2 s^-1
q Phi_0 = 0.0784710 A/cm^2
```

Direct-Auger/radiative activation parity occurs at `K_th=Eg/2`.

---

## 2026-08-14 — parabolic heavy-hole spectator

For

```math
E_{hh}=\Delta+\delta_{hh}+p^2/(2M_{hh}),
```

proved exact finite-energy CCCH closure iff

```math
\boxed{M_{hh}v^2\le2(\Delta+\delta_{hh}).}
```

This was the first direct conflict with the high-`v` carrier-column lever.

The open heavy-hole threshold phase space remains quadratic. The flat-heavy-hole limit has finite normalized local threshold phase space; the principal damage is threshold collapse rather than a universal `M_hh^(3/2)` threshold-DOS divergence.

Near exact closure, the threshold diverges as `3Delta/(rho-rho_c)` while the local phase-space coefficient vanishes as `(rho-rho_c)^(3/2)`.

---

## 2026-08-14 — general spectator-band theorem

For any positive isotropic convex spectator excitation `E_s(p)`, define

```math
\boxed{v_s^{crit}=\inf_{p>0}E_s(p)/p.}
```

Exact finite-energy normal-momentum spectator-assisted CCCH closure is equivalent to

```math
\boxed{v\le v_s^{crit}.}
```

For multiple spectators, `v_spec=min_s v_s^crit`.

This is mathematically Landau-like and equal-group-velocity threshold physics is classical. Do not claim the kinematic construction as novel.

The strongest conditional single-pass electronic theorem is

```math
\boxed{
\Sigma_c
\ge
\frac{C}{v_{adm}^2},
\qquad
v_{adm}=\min(V_{hop},v_{spec}).
}
```

Parabolic heavy-hole form:

```math
\boxed{
\Sigma_c\ge
\max[C/V_{hop}^2, C M_{hh}/(2(\Delta+\delta_{hh}))].
}
```

---

## 2026-08-14 — adversarial novelty audit

Prior art directly covers nearly every constituent idea:

```text
alpha/G_th detector optimization;
small-gap band-structure Auger suppression;
HgCdTe heavy-hole CCCH;
equal-group-velocity impact-ionization thresholds;
Landau min[E/p] critical velocity;
Dirac/quasi-relativistic Auger suppression;
multiband IR detector optimization balancing absorption and Auger;
radiative detailed balance and photon recycling.
```

Focused search did not locate the exact carrier-sheet lower-bound composition, but a hostile reviewer can characterize it as an elementary synthesis.

Two major universality failures were identified:

```text
1. unbounded useful optical absorption by spectator bands;
2. arbitrary photonic path enhancement reducing physical absorber thickness.
```

The theorem is therefore conditional, not a bulk-HgCdTe universal bound.

---

## 2026-08-14 — resonant path enhancement versus finite response

Controlling file:

`RESONANT_PATH_ENHANCEMENT_RESPONSE_BOUND_STEP_2026-08-14.md`.

Reproducible helper:

`numerics/resonant_path_response_bound.py`.

### One-port TCMT

Use

```math
\dot a=(i\omega_0-\gamma_e-\gamma_i)a+\sqrt{2\gamma_e}s_+.
```

The absorptance is

```math
A(\omega)
=\frac{4\gamma_e\gamma_i}
{(\omega-\omega_0)^2+(\gamma_e+\gamma_i)^2}.
```

Define the field-envelope response time

```math
\tau_{opt}=1/(\gamma_e+\gamma_i).
```

For target peak absorptance `A_0`, the over-coupled branch minimizes required internal loss at fixed response time. With

```math
\boxed{g(A_0)=1-\sqrt{1-A_0},}
```

```math
\boxed{
2\gamma_i\ge g(A_0)/\tau_{max}.
}
```

### New photonic resource

Define

```math
\boxed{
\Lambda_a
=\frac{2\gamma_i}{\alpha_Dd}
=\frac{P_{abs}}{\alpha_Dd\,U}.
}
```

This is the optical sampling-rate / absorber-participation resource.

Then

```math
\boxed{
\alpha_Dd
\ge
\frac{g(A_0)}{\Lambda_a\tau_{max}}.
}
```

Let `B=n_c v^2/alpha_D` be the active-pair bulk density-to-absorption coefficient (`C=zeta B` for the earlier single-pass target). Under spectator neutrality, `n_c/alpha_D >= B/v^2`.

Combining with the electronic ceiling gives

```math
\boxed{
\Sigma_c
\ge
\frac{B}{v_{adm}^2}
\frac{g(A_0)}{\Lambda_a\tau_{max}}.
}
```

### Decisive no-go

TCMT does **not** provide a universal upper bound on `Lambda_a`.

Therefore

```math
\boxed{
\text{finite temporal response alone does not restore a universal physical carrier-column lower bound.}
}
```

An additional electromagnetic resource is required: field-concentration / participation limit, material susceptibility, minimum resonator size, accepted optical bandwidth, resonance density, or a passivity/causality thickness-bandwidth constraint.

### Simple cavity corollary

For an absorber sampled once per optical circulation in a cavity of path length `L` and energy velocity `v_E`,

```math
\Lambda_a\simeq v_E/L,
```

so

```math
\boxed{
\Sigma_c
\gtrsim
\frac{B}{v_{adm}^2}
g(A_0)\frac{L}{v_E\tau_{max}}.
}
```

At `lambda=10 um`, a simple `L=lambda/n`, `v_E=c/n` resonator has circulation time `33.36 fs`. For `A_0=0.90`, a `1 ps` optical-response ceiling allows a column bound only `0.0099x` the original single-pass 90%-absorption bound, roughly a `100x` escape.

### Prior-art disposition

Critical coupling, resonator linewidth/lifetime, resonant-cavity-enhanced photodetectors, and passive absorber thickness-bandwidth limits are established. RCE photodetectors have long been used to improve the conventional quantum-efficiency / absorber-thickness bandwidth tradeoff.

Rozanov's 2000 absorber sum rule gives a passive thickness-bandwidth bound under its specific metal-backed multilayer assumptions; it is not automatically universal for arbitrary detector photonic architectures.

---

## Active frontier

Do not add another electronic mechanism or another example cavity.

Audit established passive-electromagnetic bounds on the new resource `Lambda_a`:

```text
Rozanov-type thickness-bandwidth sum rules;
Bode-Fano matching limits;
delay-bandwidth bounds;
material-susceptibility / field-concentration bounds;
finite resonance-density sum rules;
complete external optical boundary.
```

Question:

> Do established bounds already close the remaining photonic resource strongly enough that Experiment 10 should be formulated as a composition of known electronic and photonic bounds, or is there a detector-specific gap worth deriving?
