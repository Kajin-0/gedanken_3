# Experiment 10 — Prior-Branch and Prior-Art Boundary

**Date:** 2026-08-14  
**Purpose:** prevent rediscovery before the new line is deepened.

## 1. Internal boundary — Experiment 08 must not be repeated

Branch:

```text
experiment-08-zero-gap-kane-statistics
```

Controlling stop file:

```text
experiments/08-zero-gap-kane-statistics/00_NOVELTY_STOP_2026-08-14.md
```

Experiment 08 already established, within its reduced Kane model:

- the failure of naive parabolic/nondegenerate intrinsic-density scaling as `E_g -> 0`;
- the finite zero-gap Kane carrier-density limit;
- a Lambert-W zero-gap asymptotic;
- a generic DOS-mismatch asymptotic theorem;
- the thermodynamic importance of finite heavy-hole curvature;
- the fact that the practical correction becomes large only at gaps far below ordinary MWIR/LWIR operation at 77 K.

Its publication path was closed because the underlying Kane charge-neutrality problem and nonparabolic carrier-statistics literature are mature.

**Experiment 10 is not a zero-gap-statistics project.** It fixes a finite LWIR gap near `0.1 eV` at room temperature and asks for a constrained detector-performance admissibility result.

## 2. Established detector-material figures of merit

A simple material metric is not sufficient novelty.

### Kopytko and Rogalski (2022)

M. Kopytko and A. Rogalski, "Figure of merit for infrared detector materials," *Infrared Physics & Technology* **122**, 104063 (2022).

DOI:

```text
10.1016/j.infrared.2022.104063
```

This work compares HgCdTe and T2SL material systems and explicitly discusses detector-material figures of merit including `alpha sqrt(tau)` and a detectivity form proportional to `sqrt(alpha/G_th)`.

### Rogalski (2025)

A. Rogalski, "alpha/G figure of merit for infrared photodetector materials," *Journal of Applied Physics* **137**, 170701 (2025).

DOI:

```text
10.1063/5.0260949
```

This is a direct novelty hazard for any proposal whose central result is merely that strong absorption and weak thermal generation are desirable.

Therefore Experiment 10 must not present

```math
\alpha/G_{th}
```

or a simple reparameterization of it as the new result.

## 3. Established high-operating-temperature HgCdTe theory

Detailed device-level theory already treats Auger, radiative, SRH, depletion, photon recycling, background limits, and HOT HgCdTe performance. A new branch cannot claim that combining those mechanisms is itself new.

The relevant literature must be audited before any manuscript claim. In particular, the branch must compare against work on ultimate/HOT HgCdTe photodiodes and background-limited operation.

## 4. Established Auger-engineering idea

Band-structure engineering to reduce Auger recombination is not new. It is central to substantial literature on narrow-gap quantum wells and type-II superlattices.

Therefore none of the following statements is a novelty claim:

```text
Auger recombination matters strongly in narrow-gap semiconductors;
Auger phase space can be changed by band engineering;
quantum wells or superlattices can suppress selected Auger channels;
HgCdTe/Kane-like structures can have unusual Auger kinematics.
```

A surviving contribution must be a more general theorem, bound, classification, or previously unrecognized constrained optimum.

## 5. Established radiative detailed balance

Kirchhoff reciprocity, generalized Planck relations, and semiconductor radiative detailed balance already connect absorption/emissivity with equilibrium photon exchange and radiative recombination.

Therefore the statement

> better absorption entails corresponding radiative emission in equilibrium

is not novel.

Potential novelty would require proving a detector-specific invariant or bound under the exact matched constraints used here and then showing a nontrivial implication for permissible electronic dispersions.

## 6. Strongest possible surviving question

The research line should be killed unless it can move beyond the established pieces above.

The strongest current formulation is:

> For a passive reciprocal interband LWIR detector at fixed `T`, cutoff, absorptance, optical environment, and response-time requirement, what constraints on electronic dispersion and matrix elements are necessary or sufficient for nonradiative internal generation to fall to the unavoidable radiative/background floor?

A useful result would be one of:

1. a no-go theorem for a broad dispersion class;
2. an exact tradeoff/invariant coupling thermodynamic DOS to useful absorptance;
3. a kinematic criterion that simultaneously preserves absorption and closes dominant Auger channels;
4. an admissibility region that is more primitive than `alpha/G` because `alpha` and `G` are both derived from the same electronic structure;
5. a proof that no such reduction is possible without violating the imposed bandwidth/resource constraint.

## 7. Mandatory novelty gate before manuscript work

Before manuscript architecture, explicitly audit at least:

```text
infrared detector material figures of merit;
Law 19 / HOT HgCdTe ultimate-performance theory;
van Roosbroeck-Shockley / generalized Planck detailed balance;
Auger threshold and phase-space theory in narrow-gap semiconductors;
HgCdTe Kane and quantum-well Auger literature;
T2SL Auger-suppression literature;
fundamental absorption / oscillator-strength sum rules;
DOS-optical-matrix-element tradeoffs in two-band k.p models.
```

If the proposed theorem reduces to any established result after change of notation, document the reduction and close the line.

## 8. Current novelty disposition

```text
simple material FoM: PRIOR ART
zero-gap Kane statistics: CLOSED IN EXPERIMENT 08
generic Auger suppression: PRIOR ART
generic detailed balance: PRIOR ART
finite-gap constrained band-structure admissibility theorem: OPEN / NOT YET DERIVED
novelty: NOT ESTABLISHED
paper drafting: PREMATURE
```
