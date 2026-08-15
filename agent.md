# Agent recovery entrypoint

Read `AGENTS.md` first, then this file. Do not infer chronology from `main` alone.

## Hard scope

Experiment 10 is analytical/theoretical only. Preserve negative/corrected/conditional paths. Do not use novelty or priority language without a dedicated audit.

# ACTIVE FRONTIER — Experiment 10

Branch:

```text
experiment-10-room-temperature-lwir-admissibility
```

No manuscript is justified yet.

## Read in this order

1. `experiments/10-room-temperature-lwir-admissibility/CURRENT_STATE.md`
2. `experiments/10-room-temperature-lwir-admissibility/RESONANT_PATH_ENHANCEMENT_RESPONSE_BOUND_STEP_2026-08-14.md`
3. `experiments/10-room-temperature-lwir-admissibility/THEOREM_CORE_2026-08-14.md`
4. `experiments/10-room-temperature-lwir-admissibility/JOINT_ADMISSIBILITY_NOVELTY_AUDIT_2026-08-14.md`
5. `experiments/10-room-temperature-lwir-admissibility/GENERAL_SPECTATOR_BAND_ADMISSIBILITY_THEOREM_STEP_2026-08-14.md`
6. `experiments/10-room-temperature-lwir-admissibility/HEAVY_HOLE_AUGER_RATE_AND_JOINT_BOUND_STEP_2026-08-14.md`
7. `experiments/10-room-temperature-lwir-admissibility/RADIATIVE_BOUNDARY_ADMISSIBILITY_STEP_2026-08-14.md`
8. earlier derivations only as needed.

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

---

# Current theorem structure

## Electronic active-pair lower bound

For the finite-gap massive-Dirac active pair and the same required **active-pair single-pass optical depth**,

```math
\boxed{\Sigma_c\ge C/v^2.}
```

The equality is the two-band `mu=0` result. Spectator holes shift `mu>0`, increasing active electron density and weakening active-pair absorption, so the lower bound survives.

Standard witness:

```math
C=1.06668\times10^{29}\ \mathrm{m^{-2}(m/s)^2}.
```

## Electronic velocity ceilings

Microscopic lattice resource:

```math
\boxed{v\le V_{hop}.}
```

For spectator hole excitation `E_s(p)`:

```math
\boxed{v_s^{crit}=\inf_{p>0}E_s(p)/p.}
```

Exact finite-energy normal-momentum spectator-assisted CCCH closure is equivalent to

```math
\boxed{v\le v_s^{crit}.}
```

For multiple spectators:

```math
v_{spec}=\min_s v_s^{crit}.
```

This is mathematically Landau-like and based on classical impact-ionization threshold physics; do not claim the kinematic construction as novel.

Define

```math
\boxed{v_{adm}=\min(V_{hop},v_{spec}).}
```

Then the controlled single-pass active-pair-optically-dominant exact-closure theorem is

```math
\boxed{\Sigma_c\ge C/v_{adm}^2.}
```

Parabolic heavy-hole corollary:

```math
\boxed{M_{hh}v^2\le2(\Delta+\delta_{hh})}
```

and

```math
\boxed{\Sigma_c\ge C M_{hh}/[2(\Delta+\delta_{hh})]}
```

if the spectator ceiling is the active constraint.

---

# Optical-boundary / Auger support

The complete external mode-resolved optical boundary must be matched to fix irreversible radiative/background exchange. Internal radiative recombination is not invariant because of photon recycling.

Exact symmetric two-band direct Auger is closed; particle-hole asymmetry and spectator bands reopen it. Near interior thresholds the pure kinematic shell is quadratic, with possible extra overlap powers.

These ingredients are established broadly; only their detector-specific composition remains under evaluation.

---

# New resonant-response result

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

For target resonant absorptance `A_0`, define

```math
\boxed{g(A_0)=1-\sqrt{1-A_0}.}
```

The over-coupled branch minimizes required internal loss at fixed response time, giving

```math
\boxed{2\gamma_i\ge g(A_0)/\tau_{max}.}
```

Define the optical sampling-rate / absorber-participation resource

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
\alpha_Dd\ge\frac{g(A_0)}{\Lambda_a\tau_{max}}.
}
```

Let the active-pair density-to-absorption coefficient be

```math
n_c/\alpha_D\ge B/v^2,
```

where `C=zeta B` for the earlier single-pass target.

Combining with the electronic ceiling yields the resonant-response bound

```math
\boxed{
\Sigma_c
\ge
\frac{B}{v_{adm}^2}
\frac{g(A_0)}{\Lambda_a\tau_{max}}.
}
```

## New no-go

TCMT alone does not upper-bound `Lambda_a`.

Therefore

```math
\boxed{
\text{finite temporal response alone does not restore a universal physical carrier-column floor.}
}
```

A new electromagnetic resource is necessary.

For a simple cavity/ring,

```math
\Lambda_a\simeq v_E/L,
```

so path enhancement is paid for by dwell time. But this is architecture-specific, not universal.

At 10 um, a simple one-optical-wavelength circulation has `L/v_E = lambda/c = 33.36 fs`. For `A_0=0.90`, a `1 ps` response limit still permits about a `100x` smaller column floor than the original single-pass bound.

Reproducible helper:

`experiments/10-room-temperature-lwir-admissibility/numerics/resonant_path_response_bound.py`.

---

# Hard theorem boundaries

1. **Optically active spectators:** unbounded spectator useful absorption destroys the active-pair physical-thickness bound.
2. **Photonic path enhancement:** finite response introduces `Lambda_a` but does not bound it universally.
3. **Exact Auger closure:** sufficient, not necessary, for radiative/background-limited operation.
4. **Assisted channels:** not included in the exact normal-momentum theorem.

---

# Novelty boundary

Established prior art includes:

```text
critical coupling and TCMT linewidth/lifetime;
resonant-cavity-enhanced photodetectors used to improve efficiency-bandwidth tradeoffs;
Rozanov-type passive absorber thickness-bandwidth bounds;
alpha/G_th detector optimization;
Landau critical-velocity structure;
multiband Auger engineering;
radiative detailed balance and photon recycling.
```

Current disposition:

```text
CONDITIONAL THEOREM PACKAGE ONLY.
NOVELTY NOT ESTABLISHED.
NO MANUSCRIPT YET.
```

# NEXT ACTION

Do not add another electronic mechanism or another example resonator.

Audit established passive-electromagnetic bounds on `Lambda_a`:

```text
Rozanov thickness-bandwidth sum rules;
Bode-Fano matching limits;
delay-bandwidth bounds;
material-susceptibility / field-concentration bounds;
resonance-density sum rules;
complete external optical boundary.
```

Question:

> Do known passivity/causality/material-response bounds already provide the missing photonic ceiling strongly enough to close Experiment 10, or is there a detector-specific gap worth deriving?
