# Experiment 13 Rev. 7 — response to final adversarial re-review

**Date:** 2026-08-15  
**Branch:** `experiment-13-observable-resource-unification`  
**Target:** Physical Review Applied — Regular Article  
**Disposition:** **ALL ACTIONABLE REV6 REREVIEW ITEMS CLOSED / NO NEW SCIENTIFIC RESULT INTRODUCED**

## Why Rev. 7 exists

The external Rev. 6 re-review judged the technical loop essentially closed and found no new mathematical error affecting the central theorem, the full tightness factorization, the HgCdTe validation, or the recycling/Ramo result. It nevertheless identified three bounded manuscript corrections and two optional production-polish items.

Rev. 7 implements exactly those changes. It is not a new theory revision.

---

## 1. Thermodynamic convergence / liminf qualifier — CLOSED

Rev. 6 correctly restored the uniform-capacity hypothesis

```math
\bar v_{\mathcal B}^{\rm cap}
=\limsup_{j\to\infty}v_{\mathcal B,V_j}^{\rm cap}<\infty.
```

The re-review correctly noted that the sentence saying the density theorem simply “survives the thermodynamic limit” also presupposed convergence of the relevant intensive population and response quantities.

Rev. 7 now distinguishes the two cases explicitly.

If the finite-volume active population and response functional have ordinary thermodynamic limits, the usual density inequality follows with `v_B^cap` replaced by `bar v_B^cap`.

Without that convergence assumption, Rev. 7 states the fully general lower-limit form

```math
\boxed{
\liminf_{j\to\infty} n_{\mathcal B,V_j}^{\rm act}
\ge
\frac{\liminf_{j\to\infty}\mathcal L_{\mathcal B,V_j}}
{(\bar v_{\mathcal B}^{\rm cap})^2}
}
```

for positive finite `bar v_B^cap`.

This is a quantifier/formalism repair only. The finite-system theorem is unchanged.

---

## 2. Reference dependence of support coverage — CLOSED

The full hierarchy remains

```math
\frac{n_{\rm bound}}{n_{\rm ref}}
=
\frac{n_{\mathcal B}^{\rm act}}{n_{\rm ref}}
\eta_F
\sum_a w_a^{\rm act}\frac{c_a}{\mathcal S_a^{\rm act}}.
```

Rev. 7 now states immediately after defining `n_ref` that

```text
n_B^act / n_ref
```

is reference-domain dependent because `n_ref` is a declared broader reference population. Unlike `eta_F`, `c_a`, and `S_a^act`, the support-coverage factor is not fixed by the selected optical map alone.

This clarification reinforces the stage/domain thesis and does not alter the factorization.

---

## 3. Carrier-cutoff convergence for the reference population — CLOSED

Rev. 7 restores the previously audited carrier-domain convergence statement:

```text
Increasing the carrier cutoff from 1.5 to 2.0 nm^-1
changes the cross-mu reference population by less than 1%.
```

The production value continues to use `|k| <= 2.0 nm^-1`.

This check is relevant to the quoted support fraction

```text
n_B^act / n_ref = 0.66897
```

but does not enter the central population lower bound itself.

No production HgCdTe number changed.

---

## 4. “Production-resolution” wording — CLEANED UP

The abstract now says

```text
numerically converged second-order eight-band HgCdTe calculation
```

rather than `production-resolution`.

This cleanly separates numerical convergence from physical completeness, since the validation intentionally omits explicit zincblende BIA terms.

---

## 5. Dangling unknown-arrival sentence — REMOVED

The uniform-task subsection previously ended by referring to a separate unknown-arrival transient construction not developed in this manuscript.

That sentence is removed. No replacement claim is added.

The generic task subsection remains secondary and is still the first section to compress if an editor requests shortening.

---

## 6. Figure-label readability — IMPROVED WITHOUT RE-LAYOUT

Only the smallest annotations were enlarged:

```text
Fig. 1 map/arrow labels;
Fig. 3 top explanatory label;
Fig. 4 factor labels, values, and secondary annotation.
```

The main geometry, plotted values, captions, and scientific content are unchanged.

CI confirms no figure collision or page-count increase.

---

## 7. Publication overlap — ALREADY CLOSED BY REPOSITORY POLICY

The re-review correctly states that Experiment 12 / Experiment 13 overlap is potentially blocking only if both are intended as separate publications.

The repository policy is already explicit:

```text
Experiment 13 Rev. 7:     sole primary active submission manuscript
Experiment 12 manuscript: frozen fallback / development provenance
concurrent overlapping submission: prohibited
```

Therefore no manuscript restructuring is required on this ground.

If that policy ever changes, publication overlap must be re-audited before either manuscript is submitted.

---

## 8. Items deliberately not added

### BIA-inclusive stress test

The re-review identifies a BIA-inclusive numerical stress test as scientifically interesting but explicitly not necessary before submission because the manuscript already limits the exact shell-isotropy claim to the BIA-neglecting validation.

Do not open a new pre-submission calculation by default.

### Further theorem modification

None authorized. The re-review explicitly found no new counterexample, wrong inequality direction, normalization error, degeneracy problem, or invalid operator-norm step.

---

# Rev. 7 scientific delta

```text
central finite-system theorem:          unchanged
thermodynamic interpretation:           formally tightened
full tightness factorization:           unchanged
HgCdTe production values:               unchanged
support-rank audit:                      unchanged
PT single-parent-doublet result:         unchanged
recycling Markov spectrum:               unchanged
final-sink Poisson cancellation:         unchanged
Shockley-Ramo finite-frequency result:   unchanged
stage-specific thesis:                   unchanged
```

# Disposition

```text
REV6 TECHNICAL REREVIEW ITEMS: CLOSED
REV7 NEW SCIENCE:              NONE
REV7 SCIENTIFIC DEFECT FOUND:  NONE
FURTHER DEFENSIVE REVISION:    STOP
```

Proceed only with submission metadata / archival decisions unless a genuinely new counterexample, direct prior-art collision, or editor/referee request appears.
