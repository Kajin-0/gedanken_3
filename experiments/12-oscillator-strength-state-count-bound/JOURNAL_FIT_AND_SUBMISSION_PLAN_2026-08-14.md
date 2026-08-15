# Experiment 12 — Journal fit and submission plan

**Date:** 2026-08-14  
**Scientific text:** `MANUSCRIPT_REV6_2026-08-14.md`

## Recommendation

```text
FIRST TARGET: Physical Review B — Regular Article
FALLBACK: Journal of Applied Physics — Article
SECONDARY / LESS CLEAN FIT: Physical Review Applied — Regular Article
NOT PREFERRED: Applied Physics Letters / short-letter route
```

## 1. Physical Review B — recommended first target

Current PRB scope explicitly covers:

```text
electronic structure;
thermal and optical properties;
semiconductors;
photonics / metamaterials;
mathematical and materials physics related to condensed matter.
```

PRB also publishes detailed full research articles and does not require the result to be framed as a device-performance optimization.

That matches Rev6 well because its central contribution is a general finite-temperature response/state-count inequality for independent-quasiparticle electronic systems. Photodetection motivates the problem, but the theorem itself is condensed-matter / semiconductor optical physics.

### PRB strengths for this manuscript

```text
theorem-first presentation is natural;
parabolic and Dirac validation families are directly relevant;
Kubo, Fermi statistics, optical sum rules, and semiconductor physics are native PRB language;
the manuscript can remain honest that it is not a universal detector-performance bound.
```

### PRB risk

The dominant risk is editorial significance/novelty. The proof is compact and composed from elementary ingredients. A PRB editor or referee may view the result as an obvious inversion of phase-space filling unless the arbitrary-window, multiband, basis-invariant, active-subspace structure is made immediately clear.

Therefore do not weaken the manuscript into an HgCdTe-only or detector-engineering paper for PRB. The general theorem is the strongest reason to submit there.

## 2. Journal of Applied Physics — strongest fallback

Journal of Applied Physics explicitly publishes significant new experimental **and theoretical** applied-physics results, including materials physics, condensed matter, photonics, devices and sensors.

This is an excellent fallback if PRB rejects primarily on perceived general condensed-matter significance rather than correctness.

For JAP, the manuscript can retain the theorem but place slightly more emphasis on:

```text
infrared absorber design;
optical spectral-weight versus thermal-population tradeoff;
10-um / 300-K single-pass illustration;
connection to alpha/G_th detector-material criteria.
```

Do not add a dark-current claim to improve applied framing.

## 3. Physical Review Applied — possible but less clean

Physical Review Applied includes device physics, optics, optoelectronics, photonics, and electronics, but its current acceptance criteria emphasize fresh insight into **applications-based physical phenomena**.

Rev6 deliberately stops at an equilibrium state-count theorem and refuses an unconditional conversion to dark current, D*, or response time. That scientific discipline makes the paper stronger but weakens its PRApplied fit.

PRApplied would become more attractive only if a defensible application-level consequence were later established. Do not invent one merely for journal fit.

## 4. Why not a Letter first

The derivation is compact, but the credibility of the result depends on:

```text
basis-invariant shell construction;
active-subspace trace-rank refinement;
parabolic equality family;
Dirac validations;
explicit counterexamples and scope boundaries;
prior-art positioning.
```

Compressing these into a short Letter would increase the probability that the theorem looks either trivial or overclaimed.

A full PRB Regular Article is preferred.

## 5. PRB-facing framing

Recommended working title:

```text
Thermal quasiparticle population bound from direct interband optical spectral weight
```

Alternative conservative title:

```text
Thermal population cost of direct interband optical spectral weight
```

The first is sharper and theorem-forward; the second is slightly less claim-heavy. Either is defensible.

Recommended one-sentence significance statement for cover-letter use:

```text
The work derives a density-of-states-independent finite-temperature inequality that converts surviving direct cross-chemical-potential optical spectral weight into a lower bound on the thermal population of the one-body optical-support subspaces, with exact equality constructions and nontrivial Dirac validations.
```

Do not state that this is the first such bound.

## 6. Submission sequence

```text
1. Freeze Rev6 scientific content.
2. Prepare PRB-style LaTeX/typesetting without changing theorem scope.
3. Perform journal-specific reference audit and rendered-PDF QA.
4. Run one independent review of the rendered manuscript.
5. Submit to PRB if rendered QA passes.
6. If rejected for scope/significance rather than a scientific defect, adapt framing—not physics—for Journal of Applied Physics.
```

## 7. Hard stop

```text
NO MORE THEORY BY DEFAULT.
```

A journal-fit problem is not a reason to add a mechanism, fabricate a detector consequence, or resurrect a previously rejected dark-current/noise theorem.