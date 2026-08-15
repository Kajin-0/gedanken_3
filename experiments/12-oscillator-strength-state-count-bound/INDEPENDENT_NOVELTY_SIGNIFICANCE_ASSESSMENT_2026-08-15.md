# Independent novelty/significance assessment — Rev9

**Date:** 2026-08-15  
**Branch:** `experiment-12-oscillator-strength-state-count-bound`  
**Disposition:** **FAVORABLE EXTERNAL ASSESSMENT / NO NEW THEOREM DEFECT IDENTIFIED / NO REV10 TRIGGERED BY DEFAULT**

## Summary of supplied external assessment

The supplied independent assessment judged the manuscript technically correct and suitable in principle for a Physical Review B regular article. It characterized the result as a genuinely new *assembly/inference direction* rather than a new elementary tool: surviving cross-chemical-potential optical spectral weight plus a finite per-shell optical-velocity resource implies a lower equilibrium thermal quasiparticle population.

The assessment independently rechecked:

```text
pointwise Fermi AM-GM lemma: pass;
parabolic mass-asymmetry formula: pass;
equal-mass saturation condition: pass;
reported HgCdTe Kane velocity scale: plausible/correctly cited;
no obvious literature collision found for the specific inverse state-count construction.
```

The reviewer regarded the paper as rigorous, honestly scoped, and publishable, but not a field-changing result.

## Independent targeted literature collision check performed after receiving the assessment

A separate targeted search was run against APS/arXiv literature for combinations of:

```text
optical conductivity + thermal population lower bound;
interband spectral weight + carrier density lower bound;
phase-space filling inverse bound;
finite-temperature optical spectral weight + particle-count inequality.
```

Searches again recovered established *forward* phase-space-filling work, where carrier density determines or bleaches oscillator strength/absorption, and standard optical-sum-rule literature. No direct source was found stating the Experiment-12 combination

```text
surviving direct cross-mu spectral weight
+ finite per-shell projected velocity/operator-norm resource
+ finite-T Fermi kernel
-> lower equilibrium thermal quasiparticle population.
```

This raises confidence that the result is not an obvious restatement, but it is **not** an exhaustive priority proof.

## Novelty status remains conservative

```text
DIRECT PRIOR-ART COLLISION: NOT FOUND
NOVELTY: PLAUSIBLE
PRIORITY: NOT ESTABLISHED
NO "FIRST" OR PRIORITY LANGUAGE AUTHORIZED
```

The external assessment used stronger language than the repository is willing to adopt. The manuscript should continue to claim the theorem directly and position it relative to phase-space filling, optical sum rules, van Roosbroeck-Shockley, FDT, and Kane-band engineering without asserting historical priority.

## Assessment of the remaining criticisms

### 1. Realistic-material tightness

The reviewer notes that the realistic HgCdTe bound/reference ratio is about `0.118` in the broad validation window and only `0.032-0.111` in narrower near-edge windows.

Disposition:

```text
VALID SIGNIFICANCE COMMENT, NOT A DEFECT.
```

For a theorem that does not assume a DOS, recombination law, one-to-one transition structure, or parabolic bands, an order-`10^-1` realistic multiband bound is nontrivial. The manuscript should not oversell this as a detector-design limit.

### 2. Uniform boundedness assumptions

The general thermodynamic and moving-window statements require uniform boundedness of the selected optical-velocity capacity.

Disposition:

```text
ALREADY EXPLICITLY STATED AS A HYPOTHESIS.
```

In addition, the first-order HgCdTe 8-band Kane example supplies a concrete system-size-independent microscopic upper bound. This does not convert the general hypothesis into a universal theorem for all Hamiltonians.

### 3. Name "capacity"

The reviewer notes possible confusion with channel capacity/capacitance.

Disposition:

```text
NO CHANGE BY DEFAULT.
```

`optical-velocity capacity` is defined unambiguously and has survived repeated reviews. Renaming it at this stage would introduce broad notation churn without a scientific benefit. Reconsider only if an actual journal referee objects.

### 4. Support-rank fragility

The support-rank active population is discontinuous under infinitesimal nonzero singular values.

Disposition:

```text
ALREADY ACKNOWLEDGED; TOTAL-POPULATION COROLLARY DOES NOT DEPEND ON EXPERIMENTAL ROBUSTNESS OF n_B^act.
```

No additional defensive caveat is needed.

## Overall disposition

The supplied assessment is the first external-style review in this sequence that is predominantly about *impact* rather than theorem correctness, scope, or reproducibility.

```text
CENTRAL THEOREM: survives
REALISTIC 8-band validation: survives
NUMERICAL reproducibility: survives
LITERATURE collision: none identified in targeted search
REMAINING disagreement: significance/tightness judgment
```

Therefore:

```text
DO NOT CREATE REV10 BY DEFAULT.
```

The correct next step is submission production or, if desired, one final independent novelty-focused literature audit. Further manuscript edits should require a concrete new defect or a genuine literature collision, not another stylistic preference.