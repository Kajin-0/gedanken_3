# Experiment 12 — Novelty Audit Addendum: Low-Carrier Optical Band Engineering

**Date:** 2026-08-14  
**Purpose:** record older semiconductor-optics precedent closest to the Experiment-12 equality/design interpretation.

## 1. Why this addendum matters

The Experiment-12 carrier-population bound is tight when optically active upper/lower states are placed symmetrically about the chemical potential and the available optical velocity strength per thermally occupied state is maximized.

This suggests the design slogan

```text
light / symmetric electron-hole bands minimize the carrier population required for a given optical task.
```

That qualitative idea is **not new**.

---

## 2. Yablonovitch–Kane laser precedent

E. Yablonovitch and E. O. Kane, **“Reduction of Lasing Threshold Current Density by the Lowering of Valence Band Effective Mass,”** *Journal of Lightwave Technology* **4**, 504–506 (1986), DOI `10.1109/JLT.1986.1074751`.

The paper explicitly identifies the strong asymmetry between light conduction electrons and heavy valence holes as a penalty for laser threshold. Because holes remain comparatively classical while electrons become degenerate, the carrier injection required for threshold is increased. Strain and quantum confinement are proposed to lower the valence-band effective mass and reduce threshold requirements.

Related work by A. R. Adams and later Yablonovitch/Kane band-structure-engineering papers develops the same broad low-DOS / symmetric-band design direction for semiconductor lasers.

## 3. Relation to Experiment 12

The laser problem is not the Experiment-12 theorem.

The classic result asks how band dispersion/DOS affects the **nonequilibrium injected carrier density required to reach transparency or gain** under a Bernard-Duraffourg/quasi-Fermi-level condition.

Experiment 12 asks, at thermal equilibrium,

```text
how much thermally excited quasiparticle population is unavoidable
if a specified amount of direct cross-mu absorptive spectral weight survives,
subject to a finite per-state velocity-strength resource.
```

The current theorem:

```math
n_e+n_h
\ge
\frac{2}{\pi e^2v_{*,B}^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}d\omega
```

is DOS-model-independent and applies to arbitrary dispersive multiband state reuse inside the independent-quasiparticle class.

The old laser literature therefore supplies a strong conceptual precedent for the **design intuition** but not a direct mathematical collision with the equilibrium spectral-weight inequality.

## 4. Novelty consequence

Do not claim as novel:

```text
lighter valence bands are desirable;
electron-hole symmetry reduces optical-device carrier requirements;
low DOS can lower laser threshold carrier density;
band-structure engineering can reduce Auger penalties through lower carrier density.
```

If Experiment 12 becomes publishable, the contribution must be stated more narrowly:

```text
an inverse finite-temperature optical spectral-weight inequality that provides a necessary equilibrium thermal-population cost independent of an assumed DOS model.
```

## Disposition

```text
CONCEPTUAL PRIOR ART STRENGTHENED.
DIRECT THEOREM COLLISION STILL NOT IDENTIFIED.
NOVELTY CLAIM MUST REMAIN NARROW.
```
