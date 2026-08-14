# PRA Rev. 7 - Figure 1 production rebuild

**Date:** 2026-08-14  
**Branch:** `experiment-09-coherence-selective-photodetection`  
**Scope:** production/layout revision only; no theorem or scientific claim changed.

## Reason for revision

The Rev. 6 Figure 1 remained below submission quality. At actual REVTeX scale it contained crowded mathematical labels, weak visual hierarchy, and line/text collisions. It was therefore rebuilt rather than incrementally patched.

## Rev. 7 Figure 1 architecture

The figure is now a two-panel vector schematic.

### Panel (a): mechanism

- boxed `Signal photon` source;
- boxed `Local event` source;
- bright state `|B>` as the counted direction;
- dark subspace as the `N-1` orthogonal directions;
- extraction to the counted sink labeled only by `kappa_N`;
- local-event decomposition shown only by the weights `1/N` and `1-1/N`;
- local dephasing `gamma_N` shown separately between bright and dark populations;
- the slow scale is a detached callout: `r_-^{-1}` is an emergent eigenmode, **not** a microscopic jump.

### Panel (b): gate construction

A three-step stack now shows only:

1. target signal efficiency `eta`;
2. minimum collection gate `T_N(eta)`;
3. false-alarm susceptibility `chi_N(eta)`.

The only operational bridge retained inside the artwork is the dilute relation

```math
P_FA = d chi_N + O(d^2).
```

Long equations and explanatory prose were removed from the artwork and left to the manuscript/caption.

## Caption change

The caption now explicitly separates the state-space mechanism from the gate construction and states that the slow clock is an eigenmode rather than a jump.

## Render QA

Final Rev. 7 production checks:

```text
REVTeX/PRA compile: PASS
pages: 9
horizontal overfull boxes: NONE
underfull boxes: NONE
citations/cross-references: PASS
Figure 1 actual-page visual QA: PASS
PDF preflight: PASS
```

Final local artifact hashes:

```text
PDF SHA-256:
dbdfcfd8678df151a01fbbca5c29ea39d727708904c3598520937bf020f6c407

REVTeX SHA-256:
d22b45b9878753ce37a78340eabbd0847bc459cc943eb874f068fa2ae532aa63

Figure 1 PDF SHA-256:
3b8e9cc1ee5d867f1abe6632e8b06d981d800a831b7cb5c2e57fbae1fc083a6d
```

## Scientific state

Rev. 7 does **not** alter the Rev. 6 scientific disposition. The dilute-susceptibility theorem, fixed-target quantifier, reset assumption, bounded microscopic extraction resource, one-event-per-site source-saturation check, and prior-art positioning remain unchanged.

This revision should be treated as the current rendered production baseline because it supersedes Rev. 6 Figure 1.