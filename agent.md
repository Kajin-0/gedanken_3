# Agent recovery entrypoint

Read `AGENTS.md` first, then this file. Do not infer chronology from `main` alone.

## Hard scope

All active research is analytical/theoretical only. Preserve failed/corrected/conditional paths. Do not use novelty or priority language without dedicated prior-art audit.

# Experiment 10 — CLOSED BY DEFAULT

Branch:

```text
experiment-10-room-temperature-lwir-admissibility
```

Final disposition:

```text
CLOSED BY DEFAULT AS A NOVELTY / MANUSCRIPT PATH.
```

Do not draft a paper from the current Experiment-10 theorem package. Do not mechanically extend it by composing more established electronic or photonic resource bounds.

## Read in this order for recovery

1. `experiments/10-room-temperature-lwir-admissibility/CURRENT_STATE.md`
2. `experiments/10-room-temperature-lwir-admissibility/FINAL_PHOTONIC_AUDIT_AND_DISPOSITION_2026-08-14.md`
3. `experiments/10-room-temperature-lwir-admissibility/RESONANT_PATH_ENHANCEMENT_RESPONSE_BOUND_STEP_2026-08-14.md`
4. `experiments/10-room-temperature-lwir-admissibility/THEOREM_CORE_2026-08-14.md`
5. `experiments/10-room-temperature-lwir-admissibility/GENERAL_SPECTATOR_BAND_ADMISSIBILITY_THEOREM_STEP_2026-08-14.md`
6. earlier detailed derivations only if needed.

---

# Retained Experiment-10 results

## Active-pair optical-depth scaling

For the finite-gap massive-Dirac active pair and the same required active-pair single-pass optical depth,

```math
\boxed{\Sigma_c\ge C/v^2.}
```

The equality is exact in the two-band neutral model; spectator hole states shift `mu>0`, increase active electron density and reduce active-pair interband absorption, so the relation becomes a conservative lower bound.

Standard witness:

```math
C=1.06668\times10^{29}\ \mathrm{m^{-2}(m/s)^2}.
```

## Electronic velocity ceilings

Microscopic lattice resource:

```math
\boxed{v\le V_{hop}.}
```

For positive isotropic convex spectator hole excitation `E_s(p)`:

```math
\boxed{v_s^{crit}=\inf_{p>0}E_s(p)/p.}
```

Exact finite-energy normal-momentum spectator-assisted CCCH closure is equivalent to

```math
\boxed{v\le v_s^{crit}.}
```

For multiple spectators:

```math
v_{spec}=\min_s v_s^{crit},
\qquad
v_{adm}=\min(V_{hop},v_{spec}).
```

The conditional single-pass exact-closure theorem is

```math
\boxed{\Sigma_c\ge C/v_{adm}^2.}
```

Parabolic heavy-hole corollary:

```math
\boxed{M_{hh}v^2\le2(\Delta+\delta_{hh})}
```

and, when the spectator ceiling dominates,

```math
\boxed{\Sigma_c\ge C M_{hh}/[2(\Delta+\delta_{hh})].}
```

The `min E/p` construction is Landau-like and equal-group-velocity threshold physics is classical. Do not claim it as a new kinematic principle.

## Resonant-response extension

One-port TCMT with finite field-envelope response gives

```math
\boxed{
\Sigma_c\ge
\frac{B}{v_{adm}^2}
\frac{1-\sqrt{1-A_0}}
{\Lambda_a\tau_{max}},
}
```

where

```math
\Lambda_a=2\gamma_i/(\alpha_Dd)
```

is the electromagnetic absorber sampling-rate / participation resource.

TCMT does not upper-bound `Lambda_a`; finite response alone does not restore universality.

---

# Why Experiment 10 is closed

The final audit found established prior art covering the resource classes needed to close the remaining optical loophole:

```text
Bode-Fano passive broadband matching;
Rozanov passive thickness-bandwidth bounds;
Miller slow-light delay bounds;
Yu-Raman-Fan nanophotonic light-trapping limits;
Miller et al. susceptibility-based absorption-per-volume bounds;
resonant-cavity-enhanced photodetector efficiency/bandwidth engineering.
```

Nearly every electronic constituent is also established: `alpha/G_th`, heavy-hole CCCH, equal-group-velocity impact-ionization thresholds, Landau-like critical velocity, Dirac Auger suppression, multiband Auger engineering, radiative detailed balance, and photon recycling.

The exact composed carrier-column inequality was not located verbatim, but its novelty case is too weak and its hypotheses too restrictive for manuscript development without a new non-compositional result.

---

# Reopen Experiment 10 only if

A future line yields something genuinely outside the above constituent theories, e.g.:

```text
architecture-independent electronic-photonic invariant;
detector-specific no-go absent from known passivity theory;
non-factorizable performance bound;
new inverse theorem connecting detector observables directly to electronic structure.
```

# ACTIVE NEXT ACTION

Screen new purely theoretical photodetector Gedanken premises. Start a new experiment only after a premise survives an aggressive prior-art check.