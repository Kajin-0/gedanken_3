# Candidate Screen — Information about a Photon without Absorbing It

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Disposition:** CLOSED EARLY / QND PHOTODETECTION IS ESTABLISHED / RETAIN EXACT ENERGY–BACKACTION DISTINCTION

## 1. Premise

After Experiment 07, a candidate foundational question was:

> Can a detector acquire information about an optical quantum without consuming the optical excitation, and if so what physical resource replaces absorption when an irreversible classical record is produced?

The first half of this question has a decisive answer: **yes**. Quantum-nondemolition (QND) photon-number measurement is established both theoretically and experimentally.

The useful theoretical correction is narrower:

```text
information acquisition does not require photon-energy absorption;
perfect photon-number information instead requires distinguishability of meter states,
which produces backaction on optical coherences incompatible with photon number.
```

This candidate therefore does not support a new Experiment 09.

---

## 2. Minimal exact model

Restrict the optical system to the vacuum/one-photon subspace,

```math
\{|0\rangle,|1\rangle\},
```

with free Hamiltonian

```math
H_S=\hbar\omega |1\rangle\langle1|.
```

Let a meter start in `|m_0\rangle`. An ideal photon-number QND interaction has the controlled form

```math
U
=|0\rangle\langle0|\otimes V_0
+|1\rangle\langle1|\otimes V_1,
```

so

```math
[U,H_S]=0.
```

Choose

```math
V_0|m_0\rangle=|m_0'\rangle,
\qquad
V_1|m_0\rangle=|m_1'\rangle.
```

Then

```math
|0\rangle|m_0\rangle
\to
|0\rangle|m_0'\rangle,
```

```math
|1\rangle|m_0\rangle
\to
|1\rangle|m_1'\rangle.
```

The optical number eigenstate is unchanged. Therefore

```math
\boxed{
\Delta\langle H_S\rangle=0
}
```

for either number eigenstate, while the meter can acquire information about whether a photon is present.

If the pointer states are orthogonal,

```math
\langle m_0'|m_1'\rangle=0,
```

the two photon-number hypotheses are perfectly distinguishable even though the optical excitation survives.

Thus there is no theorem of the form

```text
one detected photon -> at least hbar*omega of signal energy must be absorbed by the detector.
```

Absorptive photodetection is one measurement architecture, not a fundamental requirement for acquiring photon-number information.

---

## 3. What replaces absorption: meter distinguishability

Let

```math
c=\langle m_0'|m_1'\rangle.
```

For equal prior probabilities and pure meter states, the Helstrom minimum binary decision error is

```math
\boxed{
P_e
=\frac12\left(1-\sqrt{1-|c|^2}\right).
}
```

Equivalently,

```math
\boxed{
|c|^2=4P_e(1-P_e).
}
```

The measurement resource in the abstract model is therefore the separation of conditional meter states, not removal of the photon's energy.

Perfect discrimination requires

```math
P_e=0
\quad\Longleftrightarrow\quad
c=0.
```

This does not say that a practical detector can generate orthogonal meter states at zero engineering cost. It says only that the cost is not universally tied to annihilating the signal photon.

---

## 4. Exact backaction on an optical superposition

Now let the input optical state be

```math
|\psi\rangle
=\alpha|0\rangle+\beta|1\rangle.
```

After the QND interaction,

```math
|\Psi\rangle
=\alpha|0\rangle|m_0'\rangle
+\beta|1\rangle|m_1'\rangle.
```

Tracing out the meter gives

```math
\rho_S'
=
|\alpha|^2|0\rangle\langle0|
+|\beta|^2|1\rangle\langle1|
+c\alpha\beta^*|0\rangle\langle1|
+c^*\alpha^*\beta|1\rangle\langle0|.
```

Therefore the photon-number probabilities, and hence the optical energy distribution, are unchanged, while the number-basis coherence is multiplied by `c`.

For a perfect photon-number measurement,

```math
c=0,
```

so the number-basis coherence vanishes completely.

Hence the correct first-principles distinction is

```math
\boxed{
\text{no energy absorption required}
\neq
\text{no quantum backaction}.
}
```

Perfect QND number information preserves number eigenstates but dephases superpositions of different photon numbers. This is the standard measurement/complementarity structure, not a new detector theorem.

---

## 5. Irreversible classical record is a separate resource layer

The unitary correlation above creates a quantum meter record but is not, by itself, an irreversible macroscopic record.

A practical detector must additionally perform some combination of:

- meter preparation;
- amplification;
- decoherence into stable pointer states;
- classical storage;
- reset for reuse.

Those operations can require work and produce entropy. However their thermodynamic cost is not universally `hbar*omega` per detected photon.

For example, under the usual Landauer assumptions, resetting one unbiased classical bit at temperature `T` has the quasistatic lower bound

```math
W_{erase}\ge k_B T\ln 2,
```

which depends on the memory environment rather than on the frequency of the detected photon.

Finite-time, finite-error, amplification, and measurement-implementation costs can be much larger and architecture-dependent. Quantum-measurement thermodynamics already treats these costs directly. Therefore attaching the classical record to a QND detector does not recover a universal photon-absorption requirement.

The important accounting rule is:

```text
signal energy,
meter/probe energy,
control work,
amplifier dissipation,
and reset/erasure cost
must be tracked as separate resources.
```

---

## 6. Direct experimental prior art

The basic premise is decisively occupied.

### Trapped/cavity photons

- G. Nogues et al., **Nature 400, 239–242 (1999)**, “Seeing a single photon without destroying it,” demonstrated nondestructive single-photon detection in cavity QED. DOI: `10.1038/22275`.
- S. Gleyzes et al., **Nature 446, 297–300 (2007)**, recorded the birth, life, and death of individual cavity photons using repeated nonabsorbing atomic probes. DOI: `10.1038/nature05589`.
- C. Guerlin et al., **Nature 448, 889–893 (2007)**, demonstrated progressive QND photon counting and measurement-induced collapse. DOI: `10.1038/nature06057`.
- J. Bernu et al., **Phys. Rev. Lett. 101, 180402 (2008)**, used absorption-free photon counting to demonstrate quantum-Zeno backaction on field phase. DOI: `10.1103/PhysRevLett.101.180402`.
- B. R. Johnson et al., **Nature Physics 6, 663–667 (2010)**, demonstrated single-shot cavity microwave photon-number detection and reported approximately 90% QND performance. DOI: `10.1038/nphys1710`.

### Itinerant photons

- S. Kono et al., **Nature Physics 14, 546–549 (2018)**, demonstrated QND detection of an itinerant microwave photon with reported quantum efficiency `0.84` and photon survival probability `0.87`. DOI: `10.1038/s41567-018-0066-3`.
- E. Distante et al., **Phys. Rev. Lett. 126, 253603 (2021)**, detected an itinerant optical photon twice without destroying it using cascaded cavity-QED detectors. DOI: `10.1103/PhysRevLett.126.253603`.

These results directly falsify any proposed universal principle that photodetection must consume the detected optical excitation.

---

## 7. Measurement-energy prior art

The second half of the premise — the energetic cost of producing information — is also occupied by broader quantum-measurement thermodynamics.

A particularly direct example is:

- X. Linpeng et al., **Phys. Rev. Lett. 128, 220506 (2022)**, “Energetic Cost of Measurements Using Quantum, Coherent, and Thermal Light,” which compares measurement signal-to-noise, backaction, and thermodynamic energy cost per information gain in dispersive circuit-QED measurement. DOI: `10.1103/PhysRevLett.128.220506`.

More general Landauer/reset and finite-time information-thermodynamics results were already screened after Experiment 07. The photodetector-specific version does not create a deeper fundamental bound.

---

## 8. Strongest conclusion

What is established by the minimal model is:

```math
\boxed{
\text{photon-number information can be transferred to a meter while}
\quad [U,H_S]=0.
}
```

For an ideal number eigenstate this permits

```math
\boxed{
\Delta E_{photon}=0
}
```

while the meter becomes perfectly distinguishable between the `n=0` and `n=1` hypotheses.

For an arbitrary superposition, the same information acquisition suppresses incompatible number-basis coherence according to the meter overlap.

Thus the fundamental exchange is not

```text
information <-> absorbed photon energy,
```

but, in the QND setting,

```text
information <-> entanglement / distinguishability / backaction on incompatible observables,
```

with separate physical resources required to prepare, control, amplify, store, and reset the meter.

All of these ingredients belong to established quantum measurement theory.

---

## 9. Disposition

```text
Can photon information be acquired without absorbing the photon? YES — established.
Is absorbed signal energy a universal information cost? NO.
Does perfect QND number measurement have zero backaction? NO — phase/coherence is disturbed.
Does irreversible record formation restore an hbar*omega lower bound? NO universal bound identified; costs are meter/memory dependent.
QND photodetection prior art: STRONG / DIRECT.
Foundational novelty: NOT ESTABLISHED.
Experiment 09 on this premise: DO NOT OPEN.
```

A narrower practical problem — such as survival probability versus information gain for a specified cavity, atom, qubit, or nonlinear medium — is legitimate device engineering, but it is not the sought new detector principle.

---

## 10. Repository-lineage note

This screen is branched from `experiment-07-isotope-srh` at head `49f0832c11452f1e869790de0075513a8ed11347`, which contains the final Experiment-07 isotope-sensitivity bounds and post-Experiment-07 candidate screen.

A parallel branch, `experiment-08-zero-gap-kane-statistics`, diverged earlier and reached head `d8f5138146561d9907a1d1d8d43d7df999bb6ed4`. That branch independently closed a zero-gap Kane-statistics path while retaining the finite zero-gap carrier floor, DOS-mismatch asymptotics, pair-fluctuation asymptotics, and Hall-readout no-go.

Future premise generation must treat **both** branches as prior project knowledge. Neither closed branch should be silently discarded merely because it is not ancestral to the other.

## 11. Next research rule

Return to analytical/theoretical premise generation. Reject any candidate whose claimed advantage reduces to:

- absorption being supposedly necessary for photon information;
- generic QND measurement;
- Landauer/reset cost;
- standard measurement-disturbance/complementarity;
- detailed balance/FDT;
- ordinary optimum filtering;
- readout-basis changes that do not create a new physical state coordinate;
- standard avalanche, Shockley-Ramo, or band-engineering effects.

Open a new numbered experiment only after the premise survives a direct theorem/architecture/prior-art kill test.