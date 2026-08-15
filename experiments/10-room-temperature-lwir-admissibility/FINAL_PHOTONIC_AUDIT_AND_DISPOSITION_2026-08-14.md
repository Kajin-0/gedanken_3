# Experiment 10 — Final Photonic Prior-Art Audit and Research Disposition

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Disposition:** **CLOSED BY DEFAULT AS A MANUSCRIPT/NOVELTY PATH / TECHNICALLY USEFUL CONDITIONAL RESULTS RETAINED / REOPEN ONLY WITH A NEW NON-COMPOSITIONAL THEOREM**

## 1. Why a final disposition is required

Experiment 10 began with the question:

> What electronic structure must a passive LWIR interband absorber possess to approach HgCdTe-class room-temperature intrinsic detector quality without sacrificing useful temporal response?

The branch produced several exact or controlled-model results, culminating in a conditional electronic carrier-column bound and then a resonant-response extension containing a new photonic resource `Lambda_a`.

The decisive question is now not whether more algebra can be done. It is whether closing `Lambda_a` produces genuinely new detector theory or merely composes the Experiment-10 electronic results with established passive-electromagnetic bounds.

This audit concludes that the latter is overwhelmingly more likely.

---

# 2. Strongest surviving electronic result

For a finite-gap massive-Dirac active pair whose specified useful absorption dominates the relevant optical depth,

```math
\Sigma_c\ge C/v^2.
```

Spectator hole bands shift intrinsic chemical potential positive, increasing active conduction density and reducing active-pair interband absorption, so the two-band equality becomes a conservative lower bound.

A microscopic lattice resource gives

```math
v\le V_{hop}.
```

For positive isotropic convex spectator-hole excitation `E_s(p)`, exact normal-momentum spectator-assisted CCCH closure requires

```math
v\le v_s^{crit},
\qquad
v_s^{crit}=\inf_{p>0}E_s(p)/p.
```

For multiple spectators,

```math
v_{spec}=\min_s v_s^{crit}.
```

Thus, within the single-pass, active-pair-optically-dominant, exact-closure class,

```math
\boxed{
\Sigma_c\ge
\frac{C}{[\min(V_{hop},v_{spec})]^2}.
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

This result remains technically valid under its hypotheses.

---

# 3. Why this is not enough for a strong novelty claim

Nearly every constituent ingredient has a direct prior-art lineage:

```text
alpha/G_th infrared-detector optimization;
absorption-versus-generation material figures of merit;
small-gap band-structure Auger suppression;
HgCdTe CCCH/Auger-1 heavy-hole channels;
equal-group-velocity impact-ionization threshold theory;
Landau-type minimum excitation phase velocity;
Dirac/quasi-relativistic Auger suppression;
multiband superlattice optimization of absorption and Auger;
radiative detailed balance and photon recycling.
```

A focused search did not locate the exact composed carrier-column equation above. However, a hostile reviewer can reasonably characterize it as the substitution of an established kinematic velocity ceiling into an analytically simple matched-optical-depth scaling law.

That is a serious novelty weakness even before photonic generalization.

---

# 4. Resonant optical enhancement exposes the decisive limitation

A one-port temporal coupled-mode model gives

```math
A(\omega)
=\frac{4\gamma_e\gamma_i}
{(\omega-\omega_0)^2+(\gamma_e+\gamma_i)^2}.
```

For target peak absorptance `A_0` and cavity-envelope response time `tau_opt`, the minimum internal absorption loss is

```math
2\gamma_i
=\frac{1-\sqrt{1-A_0}}{\tau_{opt}}
```

on the over-coupled branch.

Defining

```math
\Lambda_a
=\frac{2\gamma_i}{\alpha_Dd},
```

gives the conditional resonant carrier-column bound

```math
\boxed{
\Sigma_c
\ge
\frac{B}{v_{adm}^2}
\frac{1-\sqrt{1-A_0}}
{\Lambda_a\tau_{max}}.
}
```

Finite response therefore does not close the problem unless `Lambda_a` is independently bounded.

TCMT itself does not provide such a universal ceiling.

---

# 5. Existing photonic theory already occupies the missing resource space

## A. Broadband impedance matching — Fano/Bode-Fano

R. M. Fano, *Theoretical limitations on the broadband matching of arbitrary impedances*, Journal of the Franklin Institute **249**, 57–83 and 139–154 (1950), derived realizability and integral constraints on the logarithm of the reflection coefficient for passive matching networks.

Therefore tolerance-versus-bandwidth limitations of passive matching are classical.

## B. Passive absorber thickness-bandwidth — Rozanov

K. N. Rozanov, *Ultimate thickness to bandwidth ratio of radar absorbers*, IEEE Transactions on Antennas and Propagation **48**, 1230–1234 (2000), DOI `10.1109/8.884491`, derived a causality/sum-rule thickness-bandwidth limitation for passive metal-backed multilayer absorbers.

Its hypotheses are architecture-specific, but it directly occupies the passive absorption thickness-bandwidth direction.

## C. Linear slow-light delay — Miller

D. A. B. Miller, *Fundamental Limit to Linear One-Dimensional Slow Light Structures*, Physical Review Letters **99**, 203903 (2007), derived a general limit to delay in linear 1-D slow-light structures controlled by structure length in wavelengths and maximum dielectric-constant variation.

Thus delay enhancement cannot be discussed universally without footprint/material-contrast resources.

## D. Nanophotonic light-trapping limits — Yu, Raman & Fan

Z. Yu, A. Raman, and S. Fan, *Fundamental limit of nanophotonic light trapping in solar cells*, PNAS **107**, 17491–17496 (2010), uses electromagnetic mode counting and temporal coupled-mode theory to derive fundamental absorption-enhancement limits for nanophotonic thin absorbers.

This is extremely close to the Experiment-10 attempt to replace physical absorber thickness with resonant path enhancement while retaining broadband useful absorption.

The underlying message is already established:

```text
light-trapping enhancement depends on resonance density, coupling channels and optical bandwidth;
it is not an unlimited free resource.
```

## E. Absorption per lossy-material volume — Miller et al.

O. D. Miller et al., *Fundamental limits to optical response in absorptive systems*, Optics Express **24**, 3329–3364 (2016), DOI `10.1364/OE.24.003329`, derives geometry-independent per-volume absorption limits from energy conservation.

For isotropic electric susceptibility, the plane-wave absorption-cross-section bound is

```math
\boxed{
\frac{\sigma_{abs}}{V}
\le
k\frac{|\chi|^2}{\operatorname{Im}\chi}.
}
```

This directly establishes that extreme absorption from little lossy material is controlled by a material-response resource `|chi|^2/Im chi` rather than by electronic carrier density alone.

## F. Resonant-cavity-enhanced photodetectors

RCE photodetectors have long used optical cavities to achieve high quantum efficiency with thin absorption layers and high electrical bandwidth. Work from the late 1990s and early 2000s explicitly frames this as a route around the conventional absorber-thickness efficiency/transit-time tradeoff.

Therefore the detector-specific statement

```text
resonant path enhancement can reduce absorber thickness while retaining high quantum efficiency and high speed
```

is also established.

---

# 6. Consequence: there is no pure electronic-structure universal theorem under arbitrary photonics

Once arbitrary passive optical engineering is allowed, the achievable active absorber amount depends irreducibly on photonic resources such as

```text
material susceptibility;
lossless/lossy auxiliary materials;
structure footprint and thickness;
number and density of resonances;
external coupling-channel count;
accepted optical bandwidth;
delay / dwell time;
port topology.
```

Therefore a universal lower bound on physical active carrier column cannot depend only on

```text
Eg;
active Dirac velocity v;
spectator-band spectrum;
Auger closure;
T.
```

The correct generalized problem is a **joint electronic-photonic resource optimization**.

But the photonic resource bounds needed for that optimization already have substantial, mature prior art.

---

# 7. Why composing those photonic bounds is not a strong enough Experiment-10 continuation

One could continue by inserting, for example,

```text
a Rozanov thickness-bandwidth bound;
a Yu-Fan resonance/channel light-trapping bound;
a Miller susceptibility-volume absorption bound;
a slow-light delay bound;
a Bode-Fano matching constraint
```

into the Experiment-10 electronic inequalities.

Such formulas could be useful engineering syntheses.

They would not, however, resolve the central novelty problem:

```text
both sides of the composition would be established theory,
and the choice among optical bounds would depend on architecture-specific hypotheses.
```

The resulting paper would be vulnerable to the criticism that it is a restatement of known electronic and photonic design tradeoffs in a common notation.

The research protocol requires killing such lines rather than accumulating complexity.

---

# 8. Final novelty disposition

## Established and retained as technically useful

```text
matched finite-gap Dirac density/absorption scaling;
exact symmetric two-band Auger closure;
controlled scalar-asymmetry reopening law;
threshold phase-space factorization;
complete external optical-boundary correction;
parabolic heavy-hole CCCH opening theorem;
finite heavy-hole threshold phase-space coefficient;
general spectator critical-velocity representation;
three-band neutrality correction;
one-port resonant response/material-loss relation.
```

## Not available as broad novelty

```text
Dirac Auger suppression;
heavy-hole Auger physics;
impact-ionization threshold group-velocity conditions;
minimum excitation phase velocity as an emission criterion;
absorption/generation detector figures of merit;
resonant-cavity detector efficiency-bandwidth engineering;
passive optical matching / delay / thickness-bandwidth / light-trapping limits.
```

## Surviving exact composed carrier-column inequality

```math
\Sigma_c\ge C/[\min(V_{hop},v_{spec})]^2
```

was not located verbatim in the focused audit, but its novelty case is too weak and its detector universality too conditional to justify manuscript development without a new non-compositional insight.

---

# 9. Final branch disposition

```text
EXPERIMENT 10: CLOSED BY DEFAULT AS A NOVELTY / MANUSCRIPT PATH.
```

Do not draft a paper from the current theorem package.

Do not continue by mechanically composing additional known photonic bounds.

Reopen Experiment 10 only if a future line yields one of the following:

```text
1. an architecture-independent electronic-photonic invariant not reducible to known Bode-Fano/Rozanov/light-trapping/material-response bounds;
2. a new no-go theorem showing a detector-specific incompatibility not already implied by those theories;
3. an exact performance bound whose dependence on band structure and optical boundary cannot be factorized into known constituent bounds;
4. a clearly novel inverse result that can infer an electronic-structure constraint directly from detector-level observables.
```

---

# 10. Research value retained

Closing the manuscript path does not mean the branch failed scientifically.

Experiment 10 established a useful hierarchy:

```text
high v alone is not sufficient;
electron-hole symmetry alone is not sufficient;
spectator bands impose competing kinematic ceilings;
exact closure imposes a carrier-population cost in controlled optical classes;
complete external optical boundaries, not internal radiative rates, define the invariant radiative exchange;
photonic enhancement introduces independent resources that prevent a universal electronic-only material criterion.
```

That hierarchy is now documented for reuse, but novelty discipline requires moving on.

# NEXT ACTION

Screen new purely theoretical photodetector Gedanken premises rather than extending Experiment 10 by additional established resource bounds.
