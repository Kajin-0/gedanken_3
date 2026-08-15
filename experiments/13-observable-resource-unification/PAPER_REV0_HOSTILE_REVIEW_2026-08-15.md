# Experiment 13 — hostile review of unified manuscript Rev. 0

**Date:** 2026-08-15  
**Manuscript:** `PAPER_DRAFT_REV0_2026-08-15.md`  
**Review standard:** reject unless the unified paper is mathematically correct, physically scoped, and stronger than a thematic synthesis  
**Disposition:** **MAJOR REVISION, BUT FLAGSHIP PATH SURVIVES / ONE CONCRETE FORMULA REGRESSION / SEVERAL CLAIM-SCOPE REPAIRS / NO CENTRAL THEOREM FAILURE**

---

# 1. Executive assessment

Rev. 0 succeeds at the most important structural test: it reads as one scientific argument rather than four manuscript summaries. The order

```text
spectral concentration
-> coherent selectivity
-> inverse thermal state count
-> realistic HgCdTe decomposition
-> downstream stochastic observability
```

is coherent.

However, the first unified draft introduced one genuine technical presentation regression and several scope compressions that would be easy for a hostile referee to attack.

The central Experiment-13 relations survive. The manuscript should be revised, not abandoned.

---

# 2. BLOCKING: Kubo–Greenwood delta-function convention regressed

Rev. 0 writes

```math
\sigma_1^{cross}(\omega)
=\frac{\pi e^2}{V\omega}
\sum_{v,c}^{cross}
(f_v-f_c)|v^i_{cv}|^2
\delta(E_c-E_v-\hbar\omega).
```

The controlling Experiment-12 manuscript instead fixes the convention as

```math
\boxed{
\sigma_1^{cross}(\omega)
=
\frac{\pi e^2}{V}
\sum_{cv}^{cross}
\frac{D_{cv}|v_{cv}|^2}{E_{cv}}
\delta\!\left(\omega-\frac{E_{cv}}{\hbar}\right).
}
```

These representations can be transformed into related forms only if the delta-function Jacobian and the on-shell relation `E_cv=hbar omega` are handled consistently. A flagship manuscript should not invite a normalization dispute.

**Required fix:** use the exact controlling Experiment-12 convention everywhere and define

```math
K_T(E)=E/[e^{E/(2k_BT)}-1]
```

before writing

```math
\mathcal R_B
\ge
\frac{2}{\pi e^2}
\int_B K_T(\hbar\omega)\sigma_1^{cross}(\omega)d\omega.
```

**Severity:** blocking presentation error, not a failure of the theorem.

---

# 3. The simple stable-rank reciprocity needs its hypotheses attached to it every time

The elegant identity

```math
\mathcal A_{max}
=\mathcal S_{coh}
=1/\tau_{count}
=d/r_{st}
```

is exact under a specific comparison:

```text
one positive operator G on one d-dimensional parent subspace;
uniform incoherent comparison state I/d;
common population weight p across that parent shell for the state-count step;
equal-trace isotropic comparator for the task-advantage definition.
```

Rev. 0 states these assumptions in the derivation, but the abstract and conclusion compress them enough that a reader could misread the relation as universal for arbitrary nonuniform dark populations or dispersive equilibrium bands.

**Required fix:** label it the **uniform-shell spectral-concentration identity** or equivalent. State immediately that the dispersive theorem is the physical generalization and that nonuniform Experiment-09 dark populations retain the separate `N_eff` expression.

**Severity:** major scope repair.

---

# 4. Do not equate the natural Gram response with optimal quantum discrimination in general

For

```math
G=M^\dagger M,
```

the ratio

```math
\lambda_{max}/(TrG/d)
```

is a coherent-to-incoherent **response ratio of that coupling map**.

It is not, for a generic `G`, automatically the Helstrom-optimal discrimination advantage or the minimum false-positive rate at fixed signal efficiency.

Experiment 09 has a stronger, separately proven quantum-measurement statement for its rank-one bright projector. The unified manuscript should preserve this distinction.

**Required fix:** use `coherent response selectivity` for the generic `G` theorem. Reserve `dark rejection`, `optimal measurement`, and `accepted-dark fraction` for the Experiment-09 projector construction where those statements were actually proved.

**Severity:** major terminology repair.

---

# 5. Experiment 01 is a motivation/corollary, not a derivation from equal trace

The abstract operator theorem says

```math
TrG_A=TrG_B,
\quad G_A\ne G_B
```

forces opposite task orderings.

Experiment 01's physical construction instead equalizes **eventual event-specific matched-filter SNR** for a chosen transient and analyzes finite-time unknown-arrival search geometry. It does not establish that the corresponding full task-information operators have equal trace on some universal task space.

Rev. 0 mostly respects this, but the manuscript must not later imply that the Applied Optics theorem is a direct special case of the equal-trace theorem.

**Required fix:** say that Experiment 01 is a physical witness of scalar incompleteness and task ordering, while the equal-trace theorem gives a separate exact spectral statement under a stronger normalization.

**Severity:** important but local.

---

# 6. `sigma_1^{cross}` is not automatically the raw measured conductivity

The Experiment-12 theorem requires the conductivity contribution from direct transitions whose endpoints straddle `mu`.

A broadband experiment may measure a total conductivity containing same-side-of-`mu` transitions, phonon-assisted response, excitons, free-carrier response, or other channels. Obtaining `sigma_1^{cross}` can require microscopic decomposition, modeling, selection rules, or a regime in which the cross-`mu` contribution is isolated.

Rev. 0 occasionally says that the measured response certifies population without preserving this distinction.

**Required fix:** throughout the abstract, discussion, and conclusion use language such as

```text
selected/direct cross-mu contribution to the optical conductivity
```

and explicitly state that raw total conductivity cannot be inserted blindly.

**Severity:** major experimental-interpretation repair.

---

# 7. HgCdTe decomposition is validated, but not yet production-final

The stable-rank companion calculation independently closes

```math
\tau_{cap}^{act}
=\sum_aw_a^{act}c_a/\mathcal S_a^{act}
```

at moderate refined quadrature and finds

```text
S_a^act = 1
```

to numerical precision for the contributing active blocks.

Using the separately validated Experiment-12 continuous ordinary supremum gives approximately

```text
capacity factor ~0.571,
Fermi/Kubo factor ~0.308,
product ~0.176.
```

This is strong evidence, but the stable-rank audit itself has not yet been rerun at the complete production quadrature/convergence settings used for the submission-quality Experiment-12 validation.

**Required fix:** Rev. 1 should call these **audit-level decomposition values** and avoid excessive significant figures. A production companion run remains required before journal-facing numerical claims are frozen.

**Severity:** minor scientific / major production issue.

---

# 8. The Ramo result is exact at DC but only permissive at finite frequency

For an internally created electron-hole pair that later recombines internally at a common point,

```math
Q_k^{rec}=0
```

is exact for every electrode under ordinary Shockley–Ramo assumptions.

Likewise

```math
H_k^{rec}(0)=0.
```

The finite-frequency waveform is **generically permitted** to be nonzero for an individual trajectory:

```math
H_k^{rec}(\omega)
=i\omega e\int\Delta\phi_k(t)e^{-i\omega t}dt.
```

But a measured ensemble cross-spectrum can still vanish through symmetry, weighting-field geometry, cancellation among lineage classes, electronics, or insufficient overlap with the destination waveform.

Rev. 0 says finite-transit motion "can expose" the lineage in the body, which is correct, but the abstract says it may be invisible "while reappearing" at finite frequency, which reads more deterministically.

**Required fix:** consistently use

```text
can reappear / finite-frequency visibility becomes allowed
```

and distinguish trajectory-level waveform support from guaranteed ensemble-level cross-spectrum.

**Severity:** major claim-scope repair.

---

# 9. The Poisson endpoint cancellation also has explicit hypotheses

Exact independent output streams require the conservative independent-lineage model:

```text
Poisson primary generation;
independent noninteracting lineages;
one final sink per lineage;
measurement records only the final sink;
no common electronics or branching/gain.
```

Branching SPAD/e-APD crosstalk, nonlinear recombination, correlated generation, or pre-collection induced current leave this theorem class.

**Required fix:** list these hypotheses in the main text immediately before the exact zero-cross-spectrum statement rather than relying on the prior Experiment-03 documentation.

---

# 10. The staged-map abstraction should be made explicit with notation

The architecture review already identified the largest conceptual vulnerability: `G` plays different physical roles in different sections.

Rev. 0 explains this verbally, but the paper will be clearer if it introduces a staged chain such as

```math
\mathcal H_{task}
\xrightarrow{M_{opt}}
\mathcal H_{exc}
\xrightarrow{M_{dyn}}
\mathcal H_{int}
\xrightarrow{M_{ro}(\omega)}
\mathcal H_{term}.
```

The relevant Gram operator is then

```math
G_j=M_j^\dagger M_j
```

or that of an explicitly stated composite map.

This prevents a referee from accusing the paper of identifying unrelated matrices merely because they are positive.

**Required fix:** add this schematic in the introduction/discussion and use subscripts when ambiguity exists (`G_task`, `G_opt`, `G_ro`).

---

# 11. Novelty review after fresh targeted search

Focused searches continue to find established HgCdTe photon-recycling performance modeling and photon-transport calculations, including work treating photon recycling as important to HOT HgCdTe photodiode performance. They do not, in the searched material, state the specific conservative-lineage theorem that final-sink Poisson counting can have zero interpixel cross-spectrum while finite-transit pre-recombination Ramo motion gives finite-frequency multichannel lineage support.

This is not proof of novelty. It does mean the Experiment-03/13 result remains alive after another targeted screen.

Likewise no direct source was located for the detector-specific selectivity/state-count reciprocal interpretation. Stable rank, oscillator-strength participation, bright/dark states, and task operators remain individually established.

**Disposition:** novelty plausible only for the cross-relations and detector specializations, never for the underlying matrix machinery.

---

# 12. What survives unchanged

The following central results survive the Rev. 0 hostile audit:

```math
\mathcal A_{max}=d/r_{st}
```

under equal-trace isotropic comparison;

```math
\mathcal S_{resp}=d/r_{st}
```

for a top eigenstate versus a uniform incoherent state;

```math
\tau_{count}=r_{st}/d
```

for a uniformly populated parent shell using the same spectral capacity;

```math
\mathcal L_{task}\ge(\mathcal S_{resp}-1)/(d-1);
```

```math
\tau_{cap}^{act}
=\sum_aw_a^{act}c_a/\mathcal S_a^{act};
```

the Experiment-12 optical thermal-population theorem;

and the exact Shockley–Ramo zero-area result for internally created/recombined pair segments.

No counterexample to these derivations was found.

---

# 13. Referee disposition

```text
UNIFIED SCIENTIFIC SPINE:                PASS
CENTRAL SPECTRAL-CONCENTRATION ALGEBRA:  PASS
EXPERIMENT-12 THEOREM:                   PASS, restore authoritative Kubo form
DISPERSIVE DECOMPOSITION:                PASS
HgCdTe AUDIT CLOSURE:                    PASS, production rerun still needed
FINITE-TRANSIT RAMO DERIVATION:          PASS with ensemble-visibility qualification
POISSON ENDPOINT CANCELLATION:           PASS under explicit lineage hypotheses
NOVELTY:                                 PLAUSIBLE NARROWLY / NOT CERTIFIED
REV0 AS SUBMISSION DRAFT:                FAIL
REV1 SCIENTIFIC REVISION:                REQUIRED
FLAGSHIP RESEARCH PATH:                  CONTINUE
```

## Required Rev. 1 changes

1. Restore the authoritative Experiment-12 conductivity convention and thermal-kernel derivation.
2. Rename generic `S_coh` to a response-selectivity quantity unless the statement concerns the actual Experiment-09 projector.
3. Attach uniform-shell/common-occupation hypotheses to the simple stable-rank reciprocity.
4. Separate Experiment-01 physical witness from the equal-trace theorem.
5. Clarify that `sigma_cross` is a selected/decomposed conductivity contribution.
6. Mark HgCdTe decomposition numbers as audit-level pending a production stable-rank rerun.
7. Replace deterministic finite-frequency Ramo language with `can become visible` and add ensemble-cancellation caveats.
8. State endpoint-Poisson hypotheses explicitly.
9. Introduce staged physical maps and subscripted Gram operators.
10. Keep the overall architecture; no need to split the paper after this review.
