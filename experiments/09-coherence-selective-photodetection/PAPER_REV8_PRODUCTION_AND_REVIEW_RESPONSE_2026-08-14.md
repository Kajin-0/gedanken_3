# Experiment 09 PRA Rev. 8 — production and review-response QA

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** active PRA paper; theorem intact; production/reproducibility corrections incorporated; novelty not established

## Why Rev. 8 exists

Rev. 8 responds to two concrete issues:

1. Figure 1 in Rev. 7 still contained crowded arrow/label geometry at actual REVTeX scale.
2. A fresh hostile review identified remaining scope/reproducibility issues: title/abstract overreach relative to the susceptibility theorem, undisclosed Fig. 2 prefactors, missing physical anchoring, an unstated `O(N)` half of the one-event-per-site `Theta(N)` proof, and overly compressed reverse-injection scaling.

## Figure 1 rebuild

Rev. 8 replaces the previous mechanism figure with a simpler two-panel construction.

Panel (a): state flow only.

- signal photon -> bright state -> counted sink;
- local event -> bright weight `1/N` and dark weight `1-1/N`;
- local dephasing `gamma_N` is drawn in its own lane;
- the slow clock `r_{-,N}^{-1}` is isolated in a separate note box and is explicitly an eigenmode, not a jump.

Panel (b): operating definition only.

- target efficiency `eta`;
- minimum gate `T_N(eta)`;
- susceptibility `chi_N(eta)`.

The false-alarm expansion is left to the caption, not crowded into the artwork.

Actual page-scale render inspection: **PASS.** No text/line or text/box overlaps found.

## Title and abstract scope

Old title:

`Scalable internal false-count limits in a coherence-selective photodetector`

Rev. 8 title:

`Scaling of internal false-event susceptibility in a coherence-selective photodetector`

This matches the proven primary object. The abstract now states explicitly that finite-rate false counts require a conditional kinetic lift and that same-mode optical background and bright-aligned correlated internal sources are outside the theorem.

## Figure 2 reproducibility repair

The exact-kernel figure generator uses

```text
kappa_0 = 10
gamma_0 = 1
q_0 = 10/11 ~= 0.909
```

Therefore the plotted balanced-fast `eta=0.50` case is strictly subcritical, not a boundary case. Rev. 8 prints these values in the figure and caption and labels `eta=0.50<q_0` and `eta=0.95>q_0`.

Independent exact-kernel slope check over `N=10^3..10^4` with these actual parameters:

```text
alpha=1, beta=0, eta=.90:      -1.00017
s=0, eta=.50<q0:               +0.000034
s=0, eta=.95>q0:               +1.99994
s=1, eta=.95>q0:               +0.99994
```

The earlier approximately `0.23` apparent slope arises only if one instead assumes `kappa_0=gamma_0`, making `q_0=.5` and `eta=.5` the logarithmic boundary.

## One-event-per-site `Theta(N)` completeness

Rev. 8 now states the matching upper bound explicitly:

```text
at most N sites can generate;
each site generates at most one event;
0 <= C_loc,N <= 1;
therefore mu_1,N <= N.
```

Combined with the existing `Omega(N)` lower bound, this proves `Theta(N)`.

## Illustrative physical mapping

Rev. 8 adds a bounded solid-state anchor without assigning unsupported exponents to a real device.

Pisani et al. (Nature Communications 14, 3914 (2023)) provide a concrete collective intersubband-polarization/electronic-extractor architecture, but not an `N`-series that identifies `alpha` or `beta`.

Analytical benchmark:

```text
N equivalent extraction amplitudes adding coherently
-> bright matrix element proportional to sqrt(N)
-> kappa_N proportional to N
-> alpha approximately 1

N-independent microscopic scattering/dephasing
-> gamma_N proportional to N^0
-> beta approximately 0

collective dephasing also proportional to N
-> balanced alpha=beta
```

These are scaling benchmarks, not parameter assignments to the Pisani device.

## Reverse-injection appendix

The `O(1)`, `O(log N)`, `O(N)` classification is retained but the scaling steps are now stated explicitly from `T_N` and `bar{kappa}_N` rather than quoted in one sentence.

## Author metadata

The literal `[Author name to be confirmed]` / `[Affiliation to be confirmed]` placeholders were removed from the review copy. Rev. 8 uses `Anonymous working copy` and states that identifying metadata are intentionally omitted pending the submission record. Actual author/affiliation metadata remain open and must be supplied before submission.

## Render QA

```text
REVTeX/PRA compile: PASS
Pages: 9
Citations/cross-references: PASS
Overfull boxes: NONE
Underfull boxes: NONE
Vector figures: PASS
Page-level visual QA: PASS
PDF preflight: PASS
```

PDF SHA-256:

`8fde6c8a2780d64178de6be7b500701d926b6c86aded79f7ff5c950c79ae47e4`

TeX SHA-256:

`149223d538321236781106a80ccf485dcc69d1ee61c9deffcd41a55886ef76d9`

## Active claim boundary

The central result is a large-`N` theorem for the dilute susceptibility to independent local internal generation under the stated symmetric one-excitation Lindblad model and bounded microscopic counted coupling. It is not a universal measured dark-count-rate bound, does not reject same-mode optical background, and does not assign a material realization.

**Novelty remains NOT ESTABLISHED.**
