# AGENTS.md — Research Objective, Recovery, and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active branch:** `experiment-10-room-temperature-lwir-admissibility`

Before material writes, fetch live targets and exact blob SHAs. Preserve failed, corrected, conditional, and negative paths. Do not use novelty or priority language without a dedicated prior-art audit.

## Primary objective

Generate analytical/theoretical photodetector research from simple Gedanken experiments. The target is a defensible theorem, bound, invariant, counterexample, scaling law, or escape condition—not a materials list or a new scalar FOM.

## Hard global scope — ANALYTICAL / THEORETICAL ONLY

Allowed work: first-principles derivations, exact toy models, analytical bounds/no-go theorems, asymptotics, numerical thought experiments, analytical comparisons, and prior-art audits.

Do not make fabrication, measurement, instrumentation, sample procurement, or laboratory optimization the next step.

## Recovery order

1. `AGENTS.md`
2. `agent.md`
3. `experiments/10-room-temperature-lwir-admissibility/CURRENT_STATE.md`
4. `experiments/10-room-temperature-lwir-admissibility/RESONANT_PATH_ENHANCEMENT_RESPONSE_BOUND_STEP_2026-08-14.md`
5. `experiments/10-room-temperature-lwir-admissibility/THEOREM_CORE_2026-08-14.md`
6. `experiments/10-room-temperature-lwir-admissibility/JOINT_ADMISSIBILITY_NOVELTY_AUDIT_2026-08-14.md`
7. `experiments/10-room-temperature-lwir-admissibility/GENERAL_SPECTATOR_BAND_ADMISSIBILITY_THEOREM_STEP_2026-08-14.md`
8. `experiments/10-room-temperature-lwir-admissibility/HEAVY_HOLE_AUGER_RATE_AND_JOINT_BOUND_STEP_2026-08-14.md`
9. `experiments/10-room-temperature-lwir-admissibility/RADIATIVE_BOUNDARY_ADMISSIBILITY_STEP_2026-08-14.md`
10. earlier Experiment-10 derivations only as needed.

Do not infer chronology from `main`; later experiments live on divergent branches.

## Fixed target

```math
T=300\ \mathrm K,
\qquad
\lambda_c=10\ \mu\mathrm m,
\qquad
E_g=0.123984\ \mathrm{eV},
\qquad
E_g/(k_BT)\approx4.796.
```

Research question:

> What electronic structure must a passive LWIR absorber possess to approach HgCdTe-class room-temperature intrinsic detector quality without sacrificing useful temporal response?

---

# Controlling electronic result

For the finite-gap massive-Dirac active pair and the same required active-pair single-pass optical depth,

```math
\boxed{\Sigma_c\ge C/v^2.}
```

Spectator holes shift intrinsic `mu>0`, so they make this bound conservative rather than invalidating it.

A microscopic lattice resource gives

```math
\boxed{v\le V_{hop}.}
```

For each positive isotropic convex spectator-hole excitation `E_s(p)`, define

```math
\boxed{
 v_s^{crit}=\inf_{p>0}\frac{E_s(p)}{p}.
}
```

Exact finite-energy normal-momentum spectator-assisted CCCH closure is equivalent to

```math
\boxed{v\le v_s^{crit}.}
```

For multiple spectators,

```math
v_{spec}=\min_s v_s^{crit},
\qquad
v_{adm}=\min(V_{hop},v_{spec}).
```

Thus under the controlled **single-pass, active-pair-optically-dominant** hypotheses,

```math
\boxed{\Sigma_c\ge C/v_{adm}^2.}
```

The `min E/p` structure is Landau-like and the equal-group-velocity threshold condition is classical. Do not claim the kinematic ceiling as a new general principle.

Parabolic heavy-hole corollary:

```math
\boxed{M_{hh}v^2\le2(\Delta+\delta_{hh})}
```

and, when that spectator ceiling dominates,

```math
\boxed{\Sigma_c\ge C M_{hh}/[2(\Delta+\delta_{hh})].}
```

---

# Optical / radiative supporting results

Complete external mode-resolved optical boundary matching is required to fix irreversible radiative/background exchange. Internal radiative recombination is not invariant because of photon recycling.

At the ideal 10-um/300-K hemispherical step benchmark:

```text
Phi_0 = 4.89777e17 cm^-2 s^-1
q Phi_0 = 0.0784710 A/cm^2
```

Exact symmetric two-band direct Auger is closed; asymmetry and spectator bands reopen it. Threshold phase-space shells are quadratic in the controlled interior cases, with possible extra microscopic overlap powers.

---

# New resonant-response extension

One-port TCMT:

```math
A(\omega)
=\frac{4\gamma_e\gamma_i}
{(\omega-\omega_0)^2+(\gamma_e+\gamma_i)^2}.
```

Define field-envelope response time

```math
\boxed{\tau_{opt}=1/(\gamma_e+\gamma_i).}
```

For target peak absorptance `A_0`, define

```math
\boxed{g(A_0)=1-\sqrt{1-A_0}.}
```

On the over-coupled branch, which minimizes required internal material loss at fixed response time,

```math
\boxed{2\gamma_i\ge g(A_0)/\tau_{max}.}
```

Define the electromagnetic absorber sampling-rate resource

```math
\boxed{
\Lambda_a
=\frac{2\gamma_i}{\alpha_Dd}
=\frac{P_{abs}}{\alpha_Dd\,U}.
}
```

Then

```math
\boxed{
\alpha_Dd\ge g(A_0)/(\Lambda_a\tau_{max}).
}
```

Writing

```math
n_c/\alpha_D\ge B/v^2
```

and combining with `v<=v_adm` gives

```math
\boxed{
\Sigma_c
\ge
\frac{B}{v_{adm}^2}
\frac{g(A_0)}{\Lambda_a\tau_{max}}.
}
```

## Decisive no-go

TCMT itself does not upper-bound `Lambda_a`.

Therefore

```math
\boxed{
\text{finite temporal response alone does not restore a universal physical carrier-column lower bound.}
}
```

The missing ingredient is now explicitly photonic: an upper bound on field concentration / absorber participation / optical sampling rate, or an equivalent passive bandwidth/thickness/material-response resource.

For a simple ring/Fabry-type cavity, `Lambda_a~v_E/L`, so path enhancement is paid for by optical dwell time. But this is architecture-specific.

At 10 um, a simple one-optical-wavelength circulation has `L/v_E=lambda/c=33.36 fs`; with `A_0=0.90`, a 1-ps optical-response requirement still permits roughly a 100x lower column bound than the original 90%-absorbing single-pass slab.

---

# Hard theorem boundaries

```text
unbounded spectator optical strength destroys the active-pair physical-thickness bound;
finite response leaves an unbounded photonic participation resource Lambda_a;
exact Auger closure is sufficient, not necessary, for radiative-limited operation;
assisted/Umklapp/disorder channels are outside the exact normal-momentum theorem.
```

---

# Novelty discipline

Established and unavailable as novelty:

```text
alpha/G_th detector optimization;
small-gap band-structure Auger suppression;
HgCdTe heavy-hole CCCH;
equal-group-velocity impact-ionization thresholds;
Landau min E/p critical velocity;
Dirac/quasi-relativistic Auger suppression;
multiband IR detector design balancing absorption and Auger;
critical coupling and resonator linewidth/lifetime;
resonant-cavity-enhanced photodetectors;
Rozanov-type passive absorber thickness-bandwidth bounds;
radiative detailed balance and photon recycling.
```

Current disposition:

```text
CONDITIONAL THEOREM PACKAGE.
NOVELTY NOT ESTABLISHED.
NO MANUSCRIPT YET.
```

# DO NOT DO

Do not rank compounds. Do not add another electronic recombination mechanism. Do not add another example cavity. Do not draft a manuscript before the missing photonic resource is resolved or shown to be fully covered by prior art.

# NEXT ACTION

Audit known passive-electromagnetic bounds on `Lambda_a`:

```text
Rozanov-type absorption thickness-bandwidth sum rules;
Bode-Fano matching limits;
delay-bandwidth bounds;
material-susceptibility / field-concentration bounds;
resonance-density / sum-rule constraints;
complete external optical boundary.
```

Question:

> Do established passivity/causality/material-response bounds already supply the missing photonic ceiling strongly enough to close Experiment 10, or is there a detector-specific gap worth deriving?
