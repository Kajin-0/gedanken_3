# Experiment 09 — Paper-level closest-prior-art audit

**Date:** 2026-08-14  
**Scope:** analytical/theoretical photodetector research  
**Status:** PROVISIONAL PASS TO MANUSCRIPT ARCHITECTURE / NO DIRECT STRONGER MATCH FOUND IN FOCUSED PRIMARY-LITERATURE AUDIT / NOVELTY STILL NOT ESTABLISHED

## Claim being audited

This audit does **not** ask whether bright/dark quantum states, state discrimination, superradiance, detailed balance, or dark-current suppression are individually new. They are not.

The candidate paper-level claim is the complete detector-specific chain:

```text
A photon prepares one coherent bright material excitation.
Internal local dark generation prepares the same microscopic populations incoherently.
A bright-selective counted extractor therefore accepts photon and dark events differently.

For independent local dark generation at rate d per site:
    raw dark generation = N d,

but in a coherence-preserving gate:
    accepted dark-count mean is independent of N exactly.

Local dephasing restores dark leakage on a slow timescale
    tau_leak ~ N(1/kappa + 1/gamma).

If useful counted extraction is collectively enhanced by mathcal C
and the extractor satisfies local detailed balance,
then keeping thermally reversed bright-injection dark counts fixed requires
    Delta F_extra >= kT ln mathcal C.
```

The strongest exact gated statement is

```math
\mu_{local}(T)
=d\left[T-\frac{1-e^{-\kappa T}}{\kappa}\right]
\qquad(\gamma=0),
```

which contains **no `N`**, despite raw local dark generation `Nd`.

For `gamma>0`, the exact signal and dark collection kernels are given in `GATED_DETECTOR_ROC_AND_SCALABILITY_THEOREM_2026-08-14.md`, and the discrimination is finite-time.

---

# 1. Threat class — generic quantum state discrimination / detector tomography

Quantum hypothesis testing, Helstrom discrimination, state verification, and POVM optimization already establish how coherences can distinguish density operators with identical diagonal populations.

Quantum detector tomography also directly reconstructs detector POVMs and their coherence sensitivity.

**Disposition:**

```text
GENERIC STATIC MEASUREMENT THEOREM: OLD
```

Therefore the paper must not claim novelty for

```math
\Pi_B=|B\rangle\langle B|
```

or for the fact that a coherent pure state and its dephased mixture are distinguishable.

What is not supplied by that literature alone is the detector-specific mapping from an **extensive internal dark-generation process** to the exact finite-gate count law and its scaling with `N`.

---

# 2. Threat class — collective bright/dark states, superradiance, and dephasing

Collective emitter systems with bright and dark states, superradiant/subradiant enhancement, and dephasing-induced scattering between collective sectors are mature quantum-optics subjects.

Recent primary work continues to develop collective absorption, superradiance, subradiance, and finite-temperature collective dynamics.

**Disposition:**

```text
BRIGHT/DARK MANIFOLD: OLD
COLLECTIVE RATE ENHANCEMENT: OLD
DEPHASING-INDUCED BRIGHT/DARK TRANSFER: OLD
```

The exact reduced rates

```math
r_\pm
=\frac{\kappa+\gamma
\pm\sqrt{(\kappa+\gamma)^2-4\kappa\gamma/N}}2
```

are therefore not to be sold as a new general open-system phenomenon.

Their role in the candidate paper is to quantify how long the detector's internal-dark rejection survives.

---

# 3. Threat class — coherence-dependent photocurrent and collective infrared detectors

A particularly important comparator is the 2023 quantum infrared detector work

> *Electronic transport driven by collective light-matter coupled states in a quantum device*, Nature Communications 14, 3914 (2023), DOI `10.1038/s41467-023-39594-z`.

That work develops microscopic fermionic transport theory for a semiconductor infrared detector in which collective electronic polarization and strongly coupled light-matter states drive single-particle current through an extractor level.

This is very close in **platform vocabulary**:

```text
collective optical excitation
+ quantum coherence/polarization
+ electronic extractor
+ photocurrent.
```

However, the audited source does not formulate the present provenance problem:

```text
photon-created coherent excitation
versus
population-identical incoherent internal dark excitation,
```

nor the exact `N` cancellation of accepted finite-gate internal dark counts, nor the `kT ln mathcal C` reverse-dark scaling theorem.

**Disposition:**

```text
CLOSEST DEVICE-PHYSICS NEIGHBOR FOUND
NOT A DIRECT MATCH TO THE COMBINED CLAIM
MUST BE CENTRAL PRIOR ART IN ANY PAPER
```

---

# 4. Threat class — ordinary infrared detector optical-area/electrical-area decoupling

A strong practical comparator is

> *Synchronously wired infrared antennas for resonant single-quantum-well photodetection up to room temperature*, Nature Communications (2020), DOI associated with `s41467-020-14426-6`.

That architecture emphasizes the standard detector design principle

```text
maximize optical collection area
while minimizing electrical dark-current area.
```

Related resonant QWIP/metamaterial detectors obtain strong optical coupling with small electrically active semiconductor volume, thereby reducing dark current.

This creates a serious significance challenge: a reviewer may argue that Experiment 09 is merely a quantum-coherence version of optical/electrical area decoupling.

The distinction is exact in the Gedanken model:

```text
conventional area decoupling:
    remove or electrically isolate dark-generating material;

Experiment 09:
    retain N dark-generating microscopic sites,
    raw dark generation remains Nd,
    reject local dark events because their excitation occupies the wrong Hilbert-space direction.
```

Thus the dark-generating physical volume need not be reduced in the theorem; the accepted dark count is reduced by coherence selection.

**Disposition:**

```text
STRONG PRACTICAL COMPARATOR
DOES NOT REPRODUCE THE STATE-SPACE REJECTION MECHANISM
PAPER MUST EXPLICITLY DISTINGUISH PHYSICAL-VOLUME FILTERING FROM HILBERT-SPACE FILTERING
```

---

# 5. Threat class — quantum-jump photon detectors with intrinsically low dark counts

The 2024 single-atom quantum jump photodetector demonstrates narrowband single-photon detection with very low signal-unprovoked dark-jump rates:

> *Quantum jump photodetector for narrowband photon counting with a single atom*, Phys. Rev. Research 6, 033338 (2024), DOI `10.1103/PhysRevResearch.6.033338`.

This establishes that quantum-state architecture can produce very low dark-count detectors.

But its discrimination mechanism is not the present one. It does not deliberately construct photon and dark events with identical material-state populations and discriminate only their coherence, and it does not derive the `N` cancellation / dephasing / reverse-affinity scaling chain.

**Disposition:**

```text
QUANTUM LOW-DARK DETECTOR: DIRECTLY RELEVANT CONTEXT
NO DIRECT MATCH TO CURRENT THEOREM
```

---

# 6. Threat class — quantum interference used to enhance detector signal

Quantum interference is already used to control photocurrent and enhance weak-signal detection in multiple contexts.

Examples include:

- collective coherence in coupled quantum-dot films measured through photocurrent;
- interference-controlled directional photocurrent in semiconductors;
- quantum-interference enhancement proposals for qubit-based dark-matter detection.

These establish that coherence/interference is a detector resource.

They do not, in the sources screened here, state the specific dark-generation projection theorem

```math
\Gamma_D^B
=\frac{g^\dagger Dg}{g^\dagger g}
```

as a method to convert extensive internal dark generation into a nonextensive accepted gated count while preserving unity ideal signal-state acceptance.

**Disposition:**

```text
COHERENCE AS DETECTOR RESOURCE: OLD
COHERENCE-SELECTIVE INTERNAL-DARK SCALING RESULT: NO DIRECT MATCH FOUND
```

---

# 7. Threat class — local detailed balance / stochastic thermodynamics

Local detailed balance directly gives

```math
\ln\frac{k_\to}{k_\leftarrow}
=\beta\Delta F
```

up to the sign/convention appropriate to the channel.

Falasco and Esposito, Phys. Rev. E 103, 042114 (2021), explicitly treat local detailed balance across scales and coarse graining.

Quantum detailed-balance/KMS theory is likewise mature.

Therefore

```math
\Delta F_{extra}=kT\ln\mathcal C
```

is **not** credible as an isolated new thermodynamics theorem. Once a forward rate is multiplied by `mathcal C`, the logarithmic affinity required to offset it follows immediately from local detailed balance.

**Disposition:**

```text
GENERIC kT ln(rate-ratio) MATHEMATICS: OLD
```

The candidate contribution is instead the fact that the detector's coherence mechanism creates an apparent scaling advantage in one dark sector, and the thermodynamic theorem identifies exactly where that advantage reappears when useful extraction is made collective.

---

# 8. Threat class — collective thermodynamic transport

Collective open quantum systems can exhibit enhanced currents together with enhanced fluctuations and entropy production.

A direct example is

> Kloc et al., *Superradiant Many-Qubit Absorption Refrigerator*, Phys. Rev. Applied 16, 044061 (2021), DOI `10.1103/PhysRevApplied.16.044061`.

That work reports collective scaling of cooling current together with noise and entropy production.

This is conceptually dangerous because it already teaches that collective transport enhancement is not thermodynamically free.

However it does not formulate the detector-specific sequence

```text
local incoherent dark generation rejected by bright-state projection
-> finite-gate N cancellation
-> collective counted extraction
-> reverse bright dark floor
-> kT ln mathcal C compensation.
```

**Disposition:**

```text
STRONG THERMODYNAMIC NEIGHBOR
NO DIRECT MATCH FOUND
```

---

# 9. Threat class — passive nonreciprocity

Nonreciprocal thermal systems can violate directional Kirchhoff equality and can support persistent equilibrium heat currents in many-body geometries.

Primary examples include:

- Zhu, Guo, and Fan, Phys. Rev. B 97, 094302 (2018);
- Guo and Fan, Phys. Rev. B 102, 085401 (2020).

Therefore the paper must **not** claim that every passive time-independent architecture satisfies pairwise local detailed balance in the simple scalar form used by the theorem.

Experiment 09's affinity result is conditional on the stated local-detailed-balance class.

Nonreciprocity is an escape class that may redirect thermal return channels while remaining globally constrained by equilibrium thermodynamics.

**Disposition:**

```text
NOT A CURRENT FATAL DEFECT
BUT A REQUIRED CLAIM-BOUNDARY LIMITATION
```

---

# 10. Search result for the complete combined claim

The focused primary-literature searches covered combinations of:

```text
photodetector + coherence + dark current;
collective excitation + electronic extraction;
bright/dark states + photocurrent;
quantum detector + dark count;
coherent excitation + incoherent dark generation;
collective rate enhancement + thermodynamic cost;
local detailed balance + logarithmic rate ratio;
collective transport + noise/entropy production.
```

No direct source was found that reproduces the complete Experiment-09 detector theorem.

This is not a legal priority opinion and does not prove novelty.

---

# 11. Hostile significance assessment

A skeptical referee has a plausible rejection argument:

> “The paper combines three known ideas: quantum state discrimination, bright/dark-state dephasing, and local detailed balance. The individual equations are straightforward. Why is the combination a new photodetector principle rather than a pedagogical synthesis?”

That objection must shape the manuscript.

The strongest answer is **not** to emphasize the generic ingredients. It is to center the detector-level result that does not appear explicitly in those ingredients:

```math
\boxed{
\mu_{local}(T)
=d\left[T-\frac{1-e^{-\kappa T}}{\kappa}\right]
\quad(\gamma=0),
}
```

despite raw internal dark generation `Nd`, and then show exactly how the cancellation fails under dephasing and reappears through thermally reversible extraction.

The conceptual claim would be:

> A detector can, in principle, retain a physically extensive dark-generating manifold while making the accepted internal dark-count process nonextensive, because the photon and dark bath populate different directions of the same excitation Hilbert space. This coherence advantage is finite-time and is not thermodynamically free when extraction itself is collectively enhanced.

That is materially more specific than “quantum coherence helps detection.”

---

# 12. Current novelty disposition

```text
Generic state discrimination: ESTABLISHED
Bright/dark collective physics: ESTABLISHED
Dephasing transfer: ESTABLISHED
Collective photocurrent: ESTABLISHED
Local detailed balance: ESTABLISHED
kT ln(rate enhancement): DIRECT CONSEQUENCE OF ESTABLISHED LDB

Exact gated N cancellation of accepted local internal dark counts
for population-identical coherent/incoherent detector excitations:
    NO DIRECT MATCH FOUND IN FOCUSED AUDIT

Combined gated cancellation + dephasing leakage + reverse-affinity scalability theorem:
    NO DIRECT MATCH FOUND IN FOCUSED AUDIT

Novelty: NOT PROVEN
Paper-level candidate: SURVIVES
```

---

# 13. Decision

**Proceed to manuscript architecture.**

This is not a declaration that the result is publishable. It means the line has now met the repository's threshold for using a manuscript as the next adversarial research tool:

```text
sharp question: YES
connected exact theory: YES
explicit detector ROC: YES
quantitative scaling law: YES
strong practical comparator identified: YES
closest primary prior art attacked: YES
fatal direct match found: NO
remaining significance risk: REAL BUT TESTABLE BY HOSTILE MANUSCRIPT REVIEW
```

Do not open Experiment 10.

The next work should be a compact theoretical-paper architecture centered on the gated `N` cancellation and its two failure/resource mechanisms, followed by a hostile referee-style review before substantial prose polishing.
