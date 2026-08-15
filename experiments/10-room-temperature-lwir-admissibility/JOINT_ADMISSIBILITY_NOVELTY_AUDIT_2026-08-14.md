# Experiment 10 — Adversarial Prior-Art Audit of the Joint Admissibility Theorem

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Disposition:** **NO DIRECT COLLISION FOUND FOR THE EXACT COMPOSED BOUND / MOST CONSTITUENT IDEAS ARE ESTABLISHED / GENERAL SPECTATOR CEILING IS LANDAU-LIKE / CLOSEST IR-DETECTOR LITERATURE ALREADY JOINTLY OPTIMIZES ABSORPTION AND AUGER / MANUSCRIPT NOVELTY REMAINS UNPROVED AND CONDITIONAL**

## 1. Candidate being audited

The current conditional theorem chain is

```text
single-pass useful absorption dominated by a finite-gap massive-Dirac active pair
+ matched required active-pair optical depth
+ active carrier density / absorption scaling
+ microscopic lattice velocity ceiling
+ one or more convex spectator-hole bands that can participate in Auger
+ exact normal-momentum CCCH closure
-> lower bound on matched active-electron column.
```

For the active pair,

```math
\Sigma_c\ge C/v^2.
```

For each spectator branch,

```math
v_s^{crit}=\inf_{p>0}E_s(p)/p.
```

Exact spectator-assisted CCCH closure requires

```math
v\le v_{spec}=\min_s v_s^{crit}.
```

With the lattice resource `v<=V_hop`,

```math
v_{adm}=\min(V_{hop},v_{spec}),
```

so

```math
\boxed{\Sigma_c\ge C/v_{adm}^2.}
```

For the parabolic heavy-hole corollary,

```math
\boxed{\Sigma_c\ge C M_{hh}/[2(\Delta+\delta_{hh})].}
```

The audit asks whether this exact composed result, or a clearly equivalent theorem, is already established.

---

# 2. Prior-art collision map

## A. Infrared detector absorption/generation figures of merit — DIRECT CONCEPTUAL OVERLAP

Piotrowski and Gawron, *Ultimate performance of infrared photodetectors and figure of merit of detector material*, Infrared Physics & Technology **38**, 63–68 (1997), DOI `10.1016/S1350-4495(96)00030-8`, established the generic detector-material figure of merit

```math
\alpha/G_{th}
```

and explicitly treated absorber thickness and the thermal-generation penalty in near-room-temperature HgCdTe.

This means the following are **not novel**:

```text
requiring strong absorption at finite thickness;
penalizing thermal generation;
combining optical absorption and lifetime/generation into detector performance;
calling such a ratio a material figure of merit.
```

The Experiment-10 result must not be presented as a replacement scalar `alpha/G` FOM.

## B. Small-gap Auger suppression as a band-structure problem — DIRECT OVERLAP

A. M. White, *Generation-recombination processes and Auger suppression in small-bandgap detectors*, Journal of Crystal Growth **86**, 840–848 (1988), DOI `10.1016/0022-0248(90)90813-Z`, explicitly treats near-ambient small-gap detector Auger noise as a band-structure property and reviews ways to suppress it.

Pidgeon, Ciesla and Murdin, *Suppression of non-radiative processes in semiconductor mid-infrared emitters and detectors*, Progress in Quantum Electronics **21**, 361–419 (1997), DOI `10.1016/S0079-6727(97)00012-8`, reviews Auger suppression in MIR emitters and detectors across III-V and II-VI systems.

Thus

```text
"engineer the band structure to suppress Auger in an infrared detector"
```

is old.

## C. Heavy-hole CCCH / Auger-1 in HgCdTe — DIRECT OVERLAP

P. E. Petersen, *Auger Recombination in Mercury Cadmium Telluride*, Semiconductors and Semimetals **18**, 121–155 (1981), DOI `10.1016/S0080-8784(08)62764-7`, identifies the electron-electron process involving a heavy hole as the dominant fundamental band-to-band mechanism in n-type HgCdTe.

Therefore neither

```text
heavy-hole bands are dangerous;
CCCH is a fundamental HgCdTe mechanism;
heavy spectator bands lower Auger thresholds
```

is available as novelty.

## D. Arbitrary-band impact-ionization threshold condition — DIRECT OVERLAP

Classical impact-ionization/Auger threshold theory minimizes total final energy at fixed momentum. For differentiable bands, threshold stationarity gives equal group velocities of the final carriers.

This is explicitly treated in the established semiconductor threshold literature and in Landsberg's later syntheses of band-band Auger and impact-ionization theory.

Therefore the Experiment-10 use of

```math
v_{g,1}=v_{g,2}=v_{g,3}
```

at threshold is not new.

## E. General critical phase velocity — MATHEMATICAL COLLISION WITH LANDAU CRITERION

The generalized spectator ceiling

```math
v_s^{crit}=\inf_p E_s(p)/p
```

has exactly the mathematical structure of the Landau critical-velocity criterion for emission of an excitation. Primary superfluid literature routinely states the critical speed as the minimum excitation phase velocity, e.g. `min[omega(k)/k]`.

Therefore the general result

```math
E_s(p)\ge vp
```

should be described as a **Landau-like kinematic reduction** of the semiconductor Auger problem, not a new universal emission principle.

## F. Quasi-relativistic / symmetric Auger suppression — DIRECT OVERLAP

Alymov et al., ACS Photonics **7**, 98–104 (2020), DOI `10.1021/acsphotonics.9b01099`, develop a microscopic theory for recombination, absorption and gain in HgCdTe quantum wells and show strong Auger suppression from highly symmetric quasi-relativistic electron-hole dispersion.

Morozov et al., ACS Photonics **8**, 3526–3535 (2021), DOI `10.1021/acsphotonics.1c01111`, explicitly states that massive-Dirac Auger can be completely suppressed below a kinetic threshold determined by nonparabolicity and electron-hole symmetry and demonstrates a radiative-only regime.

Thus neither Dirac Auger suppression nor radiative-dominated operation by band engineering is new.

## G. Joint absorption + band structure + Auger + detector performance — CLOSEST COLLISION

Grein, Young, Flatte and Ehrenreich, *Long wavelength InAs/InGaSb infrared detectors: Optimization of carrier lifetimes*, Journal of Applied Physics **78**, 7143–7152 (1995), DOI `10.1063/1.360422`, uses accurate `k.p` band structures to calculate multiple Auger and radiative channels and derives theoretical high-temperature limits for ideal infrared photodiodes.

The same research program also treated absolute optical absorption and limiting detector performance in type-II superlattices. Later superlattice literature explicitly discusses the trade between valence-band engineering for Auger suppression and optical matrix-element / absorption strength.

For example, theoretical InAs/GaInSb LWIR work optimized both large valence-band splitting and large absorption coefficient, noting that valence-band splitting suppresses hole-hole Auger while thin periods are needed to preserve strong absorption.

This is the **closest conceptual prior art** to Experiment 10.

Therefore the broad claim

```text
"jointly optimize band structure for strong absorption, low carrier density / long lifetime, and suppressed Auger to improve HOT IR detection"
```

is established.

---

# 3. What the audit did NOT locate

The focused searches did not locate a prior source deriving the following exact chain for a three-dimensional finite-gap Dirac active pair:

```math
n_c\sim v^{-3},
\qquad
\alpha_D\sim v^{-1},
\qquad
d\sim v,
\qquad
\Sigma_c\gtrsim v^{-2},
```

combined with the arbitrary spectator-band closure ceiling

```math
v\le\min_s\inf_p E_s(p)/p
```

to produce

```math
\boxed{
\Sigma_c\ge
\frac{C}
{\left[\min(V_{hop},\min_s v_s^{crit})\right]^2}.
}
```

Nor did the audit locate the parabolic corollary

```math
\boxed{
\Sigma_c\ge C M_{hh}/[2(\Delta+\delta_{hh})]
}
```

as an explicit infrared-detector theorem.

No source found in this audit expresses a minimum required **thermal carrier sheet population at fixed active-pair optical depth** as the consequence of demanding exact spectator-band Auger closure.

This is evidence of separation, not proof of novelty.

---

# 4. Adversarial objections to manuscript novelty

Even if the exact equation has not appeared, a hostile reviewer can make several strong arguments.

## Objection 1 — elementary composition

The bound may be viewed as a straightforward substitution of

```math
v\le v_{crit}
```

into

```math
\Sigma\propto1/v^2.
```

If both component results are considered obvious within the chosen toy model, algebraic composition may not meet the novelty bar by itself.

## Objection 2 — active-pair optical dominance is restrictive

If spectator bands contribute useful absorption,

```math
\alpha_{tot}=\alpha_D+\alpha_s,
```

then the simple `C/v^2` lower bound does not follow without an upper bound on `alpha_s`.

This is not a small technical correction. Actual HgCdTe heavy-hole states participate strongly in interband optical transitions.

Thus the current theorem is **not** a universal bulk-HgCdTe material bound.

## Objection 3 — single-pass optical architecture is restrictive

The `d=zeta/alpha` step assumes the controlled single-pass homogeneous-absorber class. Resonant cavities, gratings, slow-light structures or other optical path enhancement can alter physical thickness at fixed external absorptance.

The broader external detailed-balance theorem remains valid, but the carrier-column bound needs an explicit optical-path resource if arbitrary photonic enhancement is allowed.

## Objection 4 — exact closure is stronger than detector relevance requires

A detector only requires all nonradiative traffic to fall below the external optical floor; exact kinematic closure is sufficient but not necessary.

The exact-closure bound can therefore be conservative and may not identify the true optimal material.

## Objection 5 — other channels can dominate

Even if normal-momentum spectator CCCH is closed, assisted or alternative channels remain:

```text
phonon-assisted Auger;
Umklapp;
disorder-assisted scattering;
plasmon-assisted processes;
other remote bands;
SRH/defect generation.
```

The theorem is an intrinsic direct-channel admissibility result, not a complete material guarantee.

---

# 5. Factors in favor of a publishable theorem note

Despite those objections, the surviving structure has several properties stronger than a generic FOM discussion:

```text
1. It starts from exact matched-absorptance scaling rather than empirical material tables.
2. It produces a hard kinematic incompatibility between two desirable electronic-structure trends.
3. It generalizes from a heavy-hole mass formula to an arbitrary spectator dispersion.
4. It remains a lower bound after repairing intrinsic charge neutrality for spectator holes, under the stated optical-dominance assumption.
5. It identifies precisely where universality fails: spectator optical strength and arbitrary photonic path enhancement.
6. It supplies exact closed/open/marginal classifications rather than only lifetime estimates.
```

This is enough to justify theorem compression and one more hostile literature pass, but not yet a manuscript novelty claim.

---

# 6. Novelty disposition by component

```text
Matched detector optical-depth / thermal-generation concept:
    RED — established by alpha/G_th detector theory.

Dirac DOS and optical-conductivity scalings separately:
    RED — established.

Symmetric-Dirac Auger suppression:
    RED — established.

Equal-group-velocity impact-ionization threshold:
    RED — classical.

v_crit = inf E(p)/p as a kinematic principle:
    RED — Landau-like established structure.

Heavy-hole CCCH in HgCdTe:
    RED — established.

Joint band-structure optimization of absorption and Auger in IR superlattices:
    RED/ORANGE — substantial prior art.

Exact active-pair column bound from spectator closure:
    YELLOW — not located directly, but potentially an elementary composition.

General multi-spectator conditional admissibility bound plus explicit universality no-go:
    YELLOW — possible theorem-level synthesis; novelty still unproved.
```

---

# 7. Decision

Do **not** close Experiment 10 yet, but do **not** draft a full manuscript yet either.

The strongest next move is to compress the surviving result into a short theorem/corollary/no-go package and then attack that package as if reviewing a theoretical note.

The paper-worthy core, if one exists, is no longer

```text
high v is good;
Dirac suppresses Auger;
heavy holes are bad.
```

All of that is established.

The candidate core is:

> For a single-pass absorber whose specified useful absorption is dominated by a finite-gap Dirac pair, exact normal-momentum Auger closure against a set of spectator hole bands imposes an upper bound on the active Dirac velocity. Because the matched thermal carrier column decreases as `v^-2`, the spectator spectrum therefore imposes a nonzero lower bound on the carrier sheet population required to obtain that optical depth. The bound is controlled by the smallest spectator excitation phase velocity and fails to be universal when spectator optical strength or unrestricted photonic path enhancement is allowed.

Current disposition:

```text
THEOREM-LEVEL SYNTHESIS SURVIVES FOCUSED AUDIT PROVISIONALLY.
NOVELTY NOT ESTABLISHED.
MANUSCRIPT DECISION DEFERRED UNTIL HOSTILE THEOREM REVIEW.
```
