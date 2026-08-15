# Experiment 13 — Rev. 4 rendered hostile manuscript review

**Date:** 2026-08-15  
**Target:** Physical Review Applied — Regular Article  
**Object reviewed:** controlling seven-page production PDF from Actions run `31900965632`  
**Disposition:** **SCIENTIFICALLY FROZEN / RENDERED PRODUCTION QA PASS / FLAGSHIP-FIRST STRATEGY SURVIVES / HUMAN METADATA REQUIRED / NO THEORY REOPENING TRIGGERED**

## Executive judgment

The rendered Rev. 4 manuscript survives a final hostile review as a coherent single paper rather than a loose compilation of earlier Gedanken results.

The reason is structural. The manuscript does not ask the reader to accept generic positive-operator or singular-value mathematics as a discovery. It makes the thermal optical population theorem the principal physical result, uses the selectivity/certification reciprocity to expose the geometry behind the capacity step, diagnoses the realistic HgCdTe looseness quantitatively, and then demonstrates downstream readout nulls with the conservative-recycling/Ramo construction.

The paper remains broad, but the breadth is now causally organized rather than encyclopedic.

No rendered-page problem, theorem regression, numerical inconsistency, or direct prior-art collision was found that warrants reopening the scientific derivation.

---

## 1. Central-result hierarchy — PASS

The strongest editorial risk in earlier unified drafts was that the algebraic identity

```math
S_{X|D}\tau_{X|D}=1
```

could appear to be the principal theorem, inviting the referee response that the paper is merely repackaged linear algebra.

The rendered manuscript now avoids that failure.

The reader encounters first:

1. the exact Fermi endpoint inequality;
2. the selected cross-chemical-potential Kubo conductivity;
3. the basis-invariant exact-shell optical capacity;
4. the population lower bound.

The manuscript explicitly labels Eq. (16) as the principal physical theorem and later labels the reciprocity as a normalized spectral-capacity identity rather than a claim of new matrix theory.

That hierarchy is scientifically and editorially correct.

**Disposition:** no change required.

---

## 2. The semiconductor theorem remains defensible — PASS

The rendered theorem retains the necessary structure:

```text
selected direct cross-mu optical response
+ exact Fermi endpoint inequality
+ declared basis-invariant exact-shell capacity
+ active-support rank accounting
-> lower bound on equilibrium one-body endpoint population.
```

The paper continues to make the crucial negative statement that the theorem is not a universal recombination-rate, dark-current, noise, or D* theorem.

The selected `sigma_1^cross` requirement remains visible. A referee cannot reasonably read the manuscript as authorizing arbitrary total measured conductivity without spectral/channel decomposition.

The capacity domain is declared before the inversion and cannot be padded after the fact with irrelevant high-coupling states.

**Disposition:** PASS.

---

## 3. Forward-selectivity / inverse-certification section — PASS WITH KNOWN SIGNIFICANCE RISK

The reciprocity section is mathematically elementary once the positive operator and declared capacity are written down. That is not hidden.

Its value is the cross-identification:

```text
forward peak-to-ensemble selectivity
<->
inverse fraction of activity certified by maximum-capacity inversion.
```

The stable-rank and coherent-bright-state examples then become physical specializations, not independent novelty claims.

A hostile referee can still say:

> "This identity is obvious."

The manuscript's defense is appropriate: the identity itself is not sold as the novelty; its role is to connect the material state-count theorem to task/coherence selectivity and to resolve the source of bound looseness.

That defense is strongest because the paper immediately cashes the framework out in a nontrivial HgCdTe calculation.

**Disposition:** retain, but do not increase novelty rhetoric.

---

## 4. HgCdTe validation now carries substantial explanatory weight — PASS

The production section is the strongest answer to the objection that the paper is purely formal.

The broad-window calculation gives

```text
eta_F                  = 0.30684
capacity utilization   = 0.57262
observable tightness   = 0.17570
```

with

```math
0.30684\times0.57262=0.17570.
```

This transforms the earlier statement "the bound captures about 17.6% of the active population" into a diagnosis of *why* the bound is loose.

Within the BIA-neglecting eight-band model, the active shell selectivity satisfies

```math
S_a^{act}=1
```

to machine precision. The manuscript no longer leaves that as a suspicious numerical coincidence; it gives the fixed-k `PT`/quaternionic-block explanation and explicitly refuses to generalize exact isotropy to real zincblende HgCdTe with BIA restored.

That caveat is essential and is correctly rendered next to the result rather than buried later.

### Remaining significance vulnerability

The realistic lower bound is still approximately:

```text
11.8% of the full cross-mu reference population
17.6% of the selected active population.
```

A referee may call this quantitatively loose. The correct response is already implicit in the paper: the theorem is deliberately model-light and the decomposition identifies the independent losses rather than hiding them.

This is an impact question, not a correctness defect.

**Disposition:** PASS.

---

## 5. Photon-recycling / Ramo section is genuinely integrated — PASS

The recycling section no longer reads as an unrelated fourth case study.

The channel effects

```math
G_i(\omega)=M^\dagger(\omega)|i\rangle\langle i|M(\omega)
```

make the readout branch another instance of the same spectral/null-space logic.

Under the deliberately ideal final-sink assumptions, one conservative lineage may be null to the source terminal, giving zero endpoint-counting cross-spectrum even when internal exchange and mean crosstalk exist.

The finite-transit Shockley-Ramo step then changes the readout map:

```text
internally created + internally recombined pair
-> zero integrated induced charge
but
-> possible finite-frequency waveform support.
```

The manuscript correctly states that a nonzero ensemble cross-spectrum is **allowed, not guaranteed**. Symmetry, opposing lineages, weighting fields, and electronics can still cancel it.

This conditional language is critical and is present.

**Disposition:** PASS.

---

## 6. Rendered presentation — PASS

The seven-page APS two-column rendering is compact and readable.

The visual hierarchy is now appropriate:

- Fig. 1 gives the staged detector map;
- Fig. 2 summarizes the two-step population theorem;
- Fig. 3 illustrates selectivity versus inverse certification without dominating the paper;
- Fig. 4 exposes the HgCdTe quantitative decomposition;
- Fig. 5 contrasts endpoint counting with finite-transit Ramo observability.

Every equation is contained within its column. The central theorem is readable without a `widetext` grid interruption. The HgCdTe figure no longer intrudes into the adjacent column. No clipped text, broken glyph, missing figure, or overlapping annotation remains.

The production log contains float warnings, but direct inspection shows every float present and acceptably placed. They are not a rendered-manuscript defect in the controlling artifact.

**Disposition:** PASS.

---

## 7. The strongest remaining referee attacks

The paper is not invulnerable. The remaining attacks are mostly significance and applicability questions:

### A. "This is a synthesis of known mathematics."

Partly true at the ingredient level. Positive operators, singular values, stable rank, POVM selectivity, Shockley-Ramo coupling, and Poisson lineage theory are established.

The manuscript must continue to claim only the detector-specific cross-closure, not the mathematical ingredients.

### B. "How is `sigma_1^cross` obtained experimentally?"

This is a real applicability constraint. Total optical conductivity may mix intraband, same-side-of-mu, excitonic, phonon-assisted, and other channels. The theorem requires the selected microscopic contribution or a regime where it can be isolated.

This limits direct experimental deployment but does not invalidate the theorem.

### C. "How is `v_B^cap` known for an arbitrary material?"

The capacity is an additional microscopic resource input. In the HgCdTe example it is computed from a multiband Hamiltonian. For a new material it must be modeled, bounded, or otherwise established.

Again, applicability cost rather than theorem failure.

### D. "The realistic bound is loose."

True in the sense above: about 11.8% of the full cross-mu population and 17.6% of the active population. The decomposition now makes that looseness scientifically interpretable.

### E. "The one-body scope excludes important absorbers."

Also true. Excitonic, phonon-assisted, strongly interacting, and other many-body optical channels are outside the independent-quasiparticle theorem unless separately generalized.

The manuscript states this rather than implying universality.

### F. "The recycling cancellation uses ideal stochastic assumptions."

Yes. Endpoint Poisson cancellation requires independent, noninteracting, one-final-sink lineages without branching/gain or shared electronics. The point is an observability boundary, not a universal prediction for focal-plane arrays.

### G. "Why should all of this be in one paper?"

This remains the most credible editorial-level attack.

The answer is that the manuscript now has one causal question:

> How do the spectral edge, singular spectrum, and null space of the physically relevant detector map determine capacity, selectivity/inverse inference, and observability?

The semiconductor theorem supplies the nontrivial physical center; the task/coherence and Ramo branches show that the same accounting principle has forward and downstream consequences.

The current seven-page length is sufficiently compact that the breadth is defensible.

---

## 8. Flagship versus standalone strategy

The rendered manuscript is now strong enough to justify **flagship-first** development.

The standalone Experiment-01 Applied Optics, Experiment-09 PRA, and Experiment-12 PRB packages should remain frozen as fallback manuscripts. They should not be deleted or rewritten merely because the flagship exists.

Materially overlapping simultaneous submissions should be avoided.

If the flagship is rejected primarily for breadth rather than scientific correctness, the frozen standalone papers remain the natural fallback route.

---

## 9. Submission status

The manuscript is scientifically and technically frozen, but it is not yet administratively submission-ready.

Human metadata still required:

```text
author name
institutional affiliation
corresponding email
acknowledgments / funding statement
```

No scientific revision should be manufactured merely to keep editing.

---

## Final referee-style disposition

```text
CENTRAL THEOREM:                   PASS
MATHEMATICAL CONSISTENCY:          PASS
HgCdTe NUMERICAL CLOSURE:          PASS
BIA/PT CLAIM BOUNDARY:             PASS
RAMO/RECYCLING CLAIM BOUNDARY:     PASS
PRIOR-ART POSITIONING:             PASS AT CURRENT AUDIT LEVEL
RENDERED PRESENTATION:             PASS
FLAGSHIP UNITY:                    PASS
HUMAN METADATA:                    REQUIRED
NEW SCIENTIFIC REVISION:           NOT TRIGGERED
```

**Recommendation:** freeze Rev. 4 scientific content and production layout. Supply the human metadata, then perform only a metadata-aware final compile/hash/visual check before submission. Reopen theory only for a concrete mathematical defect, numerical inconsistency, direct prior-art collision, or explicit referee/editor requirement.
