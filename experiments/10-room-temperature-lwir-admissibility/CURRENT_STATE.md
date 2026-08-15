# Current State — Experiment 10: Room-Temperature LWIR Material Admissibility

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Final status:** **CLOSED BY DEFAULT AS A NOVELTY / MANUSCRIPT PATH**

## Why closed

Experiment 10 produced a technically coherent conditional theorem package, but the final passive-photonics audit showed that completing the result for arbitrary optical architectures would require composing the electronic inequalities with established photonic resource bounds: Bode-Fano broadband matching, Rozanov thickness-bandwidth limits, slow-light delay bounds, nanophotonic light-trapping bounds, susceptibility-based absorption-per-volume bounds, and mature resonant-cavity-enhanced photodetector theory.

The surviving electronic carrier-column inequality was not located verbatim in focused prior-art searches, but it is too conditional and too vulnerable to an “elementary composition of known ingredients” objection to justify a manuscript without a new non-compositional result.

Do not draft a paper from the current branch.

## Read first

1. `FINAL_PHOTONIC_AUDIT_AND_DISPOSITION_2026-08-14.md`
2. `RESONANT_PATH_ENHANCEMENT_RESPONSE_BOUND_STEP_2026-08-14.md`
3. `THEOREM_CORE_2026-08-14.md`
4. `JOINT_ADMISSIBILITY_NOVELTY_AUDIT_2026-08-14.md`
5. `GENERAL_SPECTATOR_BAND_ADMISSIBILITY_THEOREM_STEP_2026-08-14.md`
6. earlier detailed derivations only as needed.

---

# Retained result 1 — active-pair matched optical-depth scaling

For the finite-gap 3-D massive-Dirac active pair,

```math
n_c\propto v^{-3},
\qquad
\alpha_D\propto v^{-1}.
```

For the controlled single-pass two-band neutral model,

```math
\Sigma_c=C/v^2.
```

Adding spectator **hole** bands shifts intrinsic `mu>0`, increasing active electron density and reducing active-pair interband absorption. Therefore for the same required active-pair single-pass optical depth,

```math
\boxed{\Sigma_c\ge C/v^2.}
```

At the standard 90%-absorption witness (`T=300 K`, `lambda_c=10 um`, `r=1.2`, `n_b=3.5`),

```math
C=1.06668\times10^{29}\ \mathrm{m^{-2}(m/s)^2}.
```

---

# Retained result 2 — electronic velocity resources

Microscopic lattice/Wannier resource:

```math
\boxed{v\le V_{hop}.}
```

For a positive isotropic convex spectator-hole excitation `E_s(p)`, define

```math
\boxed{v_s^{crit}=\inf_{p>0}E_s(p)/p.}
```

Exact finite-energy normal-momentum spectator-assisted CCCH closure in the continuum model is equivalent to

```math
\boxed{v\le v_s^{crit}.}
```

For multiple spectators,

```math
v_{spec}=\min_s v_s^{crit}.
```

This construction is mathematically Landau-like and uses classical impact-ionization threshold physics. It is not a novelty claim.

For a parabolic heavy-hole branch,

```math
\boxed{M_{hh}v^2\le2(\Delta+\delta_{hh}).}
```

---

# Retained result 3 — strongest conditional single-pass theorem

Define

```math
v_{adm}=\min(V_{hop},v_{spec}).
```

Under the **single-pass, active-pair-optically-dominant, exact normal-momentum spectator-closure** hypotheses,

```math
\boxed{
\Sigma_c\ge
\frac{C}{v_{adm}^2}.
}
```

For a parabolic heavy-hole spectator,

```math
\boxed{
\Sigma_c\ge
\max\!\left[
C/V_{hop}^2,
C M_{hh}/(2(\Delta+\delta_{hh}))
\right].
}
```

This remains useful as a conditional analytical bound, but novelty is not established.

---

# Retained result 4 — Auger structure

Exact particle-hole-symmetric massive-Dirac `eeh/hhe` direct Auger is kinematically closed.

Scalar particle-hole asymmetry reopens it with weak-asymmetry threshold

```math
\boxed{K_{th}\sim E_g\mathcal A_m^{-1/3}.}
```

Near an interior threshold, the pure kinematic shell scales as

```math
\Phi\propto(K-K_{th})^2,
```

with possible additional microscopic overlap powers.

For a parabolic heavy-hole spectator, the open CCCH threshold shell is also quadratic; the flat-heavy-hole limit has a finite normalized local threshold coefficient. The heavy band primarily collapses the activation threshold rather than creating a universal `M_hh^(3/2)` threshold-DOS divergence.

---

# Retained result 5 — external radiative boundary

Matching useful front-side absorptance alone does not fix total radiative exchange. The complete external mode-resolved optical boundary must be matched.

At thermal equilibrium,

```math
\Phi_{abs}^{ext}=\Phi_{em}^{ext}=\Phi_0.
```

Internal radiative recombination is not the invariant denominator because photon recycling changes the internal event count.

Ideal 10-um/300-K hemispherical step benchmark:

```text
Phi_0 = 4.89777e17 cm^-2 s^-1
q Phi_0 = 0.0784710 A/cm^2
```

---

# Retained result 6 — resonant path enhancement versus response

One-port TCMT gives, for target peak absorptance `A_0`,

```math
A(\omega)
=\frac{4\gamma_e\gamma_i}
{(\omega-\omega_0)^2+(\gamma_e+\gamma_i)^2}.
```

Define field-envelope response time

```math
\tau_{opt}=1/(\gamma_e+\gamma_i)
```

and

```math
g(A_0)=1-\sqrt{1-A_0}.
```

The over-coupled branch gives the minimum internal loss at a fixed response time:

```math
2\gamma_i\ge g(A_0)/\tau_{max}.
```

Define the electromagnetic absorber sampling-rate resource

```math
\Lambda_a=2\gamma_i/(\alpha_Dd).
```

Then the resonant-response carrier-column bound is

```math
\boxed{
\Sigma_c\ge
\frac{B}{v_{adm}^2}
\frac{g(A_0)}{\Lambda_a\tau_{max}},
}
```

where `C=zeta B` for the earlier single-pass optical depth.

TCMT does not upper-bound `Lambda_a`; therefore finite temporal response alone does **not** restore a universal physical carrier-column floor.

---

# Final prior-art boundary

Established theory already occupies the missing photonic resource space:

```text
Fano/Bode-Fano passive broadband matching;
Rozanov passive absorber thickness-bandwidth limits;
Miller slow-light delay bounds;
Yu-Raman-Fan nanophotonic light-trapping limits;
Miller et al. susceptibility-based absorption-per-volume limits;
resonant-cavity-enhanced photodetector efficiency/bandwidth engineering.
```

Therefore continuing Experiment 10 by mechanically composing these bounds is not justified by the research novelty protocol.

---

# Reopen only if

Reopen Experiment 10 only if a future line yields a genuinely new result that is not reducible to known electronic and photonic resource bounds, for example:

```text
an architecture-independent electronic-photonic invariant;
a detector-specific no-go theorem absent from existing passivity theory;
a non-factorizable performance bound;
a new inverse theorem linking detector-level observables to electronic-structure constraints.
```

# NEXT ACTION

Screen new purely theoretical photodetector Gedanken premises. Do not continue adding established resource bounds to Experiment 10.
