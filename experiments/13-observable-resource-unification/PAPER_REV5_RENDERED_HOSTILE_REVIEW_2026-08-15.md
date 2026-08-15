# Extreme hostile review — Experiment 13 Rev. 5 rendered manuscript

**Date:** 2026-08-15  
**Target:** Physical Review Applied — Regular Article  
**Artifact reviewed:** GitHub Actions run `31903046137`, PDF SHA-256 `ce0fd199bb43652edf598ce7fa516e093e41fdc7a664d336092b8161ea7fa1c9`  
**Disposition:** **NO NEW CENTRAL MATHEMATICAL DEFECT / REV. 4 MANDATORY ISSUES REPAIRED / UNIFICATION SUBSTANTIALLY STRONGER / NO REV. 6 SCIENTIFIC REVISION TRIGGERED**

## Overall verdict

Rev. 5 is materially stronger than Rev. 4.

The previous hostile review's central objection was not that the semiconductor theorem failed; it was that a definitional reciprocal normalization could be mistaken for the unifying theorem, leaving the optical population theorem, task/coherence examples, and terminal recycling result looking stitched together.

Rev. 5 largely removes that attack. The manuscript now makes a more precise claim:

```text
optical excitation, internal dynamics, and terminal readout are distinct physical maps;
a capacity, singular-value distribution, or null space belongs to the stage on which it is defined;
inference across stages requires the intervening physical map.
```

That is a real conceptual statement rather than the observation that several matrices possess spectra.

The paper is still broad, and an editor could still judge the task/coherence and recycling sections as too expansive for one article. That is now an editorial-risk question rather than a technical incoherence in the manuscript's stated logic.

## 1. Central optical population theorem — PASS

The Rev. 5 correction pass does not alter the controlling theorem:

```math
n_e+n_h
\ge n_{e,\mathcal B}^{act}+n_{h,\mathcal B}^{act}
\ge
\frac{2}{\pi e^2(v_{\mathcal B}^{cap})^2}
\int_{\mathcal B}
\frac{\hbar\omega\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}\,d\omega.
```

The Fermi inequality, Kubo convention, exact-shell block construction, operator-norm/rank step, endpoint double counting, and dimensional structure remain unchanged from the previously audited theorem.

No regression was found.

## 2. Stable-rank terminology — FIXED

Rev. 5 now defines

```math
r_{eff}(G)=\frac{\operatorname{Tr}G}{\lambda_{max}(G)}
=\operatorname{srank}(\sqrt G).
```

It explicitly states that when `G=M^dagger M`, this is the conventional stable rank of `M`, not generally the stable rank of `G` itself.

The shell-resolved quantity

```math
r_{st,a}=\frac{\operatorname{Tr}(M_aM_a^\dagger)}{\|M_a\|_{op}^2}
```

remains the ordinary stable rank of `M_a`.

The terminology is now mathematically consistent.

## 3. Reciprocal normalization — FIXED EDITORIALLY

The identity

```math
\mathcal S_{X|D}\tau_{X|D}=1
```

remains in the paper, but Rev. 5 states plainly that it follows from the definitions and is not a new matrix theorem.

More importantly:

```text
it is absent from the abstract;
it is no longer the conclusion's displayed centerpiece;
it is described as fixed-map bookkeeping;
the full population-tightness hierarchy is promoted instead.
```

A referee can still call the identity definitional, but the paper now agrees with that criticism rather than depending on the identity for novelty.

## 4. Stage-specific unification — SUBSTANTIALLY IMPROVED

The title, abstract, introduction, Fig. 1, discussion, and conclusion now all state the same thesis: stage-specific non-transferability.

This is the strongest conceptual improvement in Rev. 5.

The manuscript does **not** claim that one master operator simultaneously describes:

```text
microscopic optical excitation;
task/coherence response;
internal stochastic dynamics;
terminal readout.
```

Instead it argues that invalid detector inference occurs when spectral properties of one physical map are silently transferred to another map.

That connects the three physical examples in a defensible way:

```text
optical response -> population:
    requires the microscopic capacity and Fermi/Kubo map;

peak/selective response -> arbitrary-task response:
    requires the task ensemble and the relevant fixed-stage response operator;

internal recycling -> terminal correlation:
    requires the terminal readout map.
```

This is not a universal dynamics theorem, but it is now a coherent detector-inference framework.

### Remaining editorial risk

The task/coherence section is still more generic than the semiconductor theorem, and the recycling section uses different stochastic physics. A severe editor could still prefer separate papers.

However, the objection is now:

> “Is this broad framework sufficiently significant for one paper?”

rather than:

> “The authors have mistaken reciprocal definitions for a unifying theorem.”

That is a meaningful improvement.

## 5. Full population-tightness hierarchy — PASS AND NOW CENTRAL

Rev. 5 introduces

```math
n_{bound}=\frac{\mathcal L_{\mathcal B}}{(v_{\mathcal B}^{cap})^2}
```

and the exact relation

```math
\boxed{
\frac{n_{bound}}{n_{ref}}
=
\frac{n_{\mathcal B}^{act}}{n_{ref}}
\eta_F
\sum_a w_a^{act}\frac{c_a}{\mathcal S_a^{act}}.
}
```

This is a substantially better organizing result than `S tau = 1`.

It identifies four physical mechanisms in the general hierarchy:

```text
1. selected-support coverage;
2. Fermi/Kubo asymmetry;
3. shell-to-global capacity mismatch;
4. within-shell singular-value concentration.
```

Important precision: the final two mechanisms occur inside the weighted sum in the general dispersive formula. They are not, in general, two independent global scalar factors. The manuscript's equation is correct and the prose describes them as mechanisms rather than falsely factorizing the weighted sum.

## 6. HgCdTe numerical closure — PASS

The broad-window values remain

```text
n_B^act / n_ref        = 0.66897
eta_F                  = 0.30684
tau_cap^act            = 0.57262
within-shell factor    = 1 in the present validation
```

and

```math
0.66897\times0.30684\times0.57262
=0.1175398\ldots,
```

consistent with the reported approximately `0.1175` / `11.8%` full bound/reference ratio.

The active-population tightness remains

```math
0.30684\times0.57262=0.17570.
```

No numerical inconsistency was found.

## 7. PT-isotropy claim — FIXED

Rev. 5 now makes the necessary distinction.

For each thermally relevant selected parent shell in the present BIA-neglecting validation, the parent is stated to be one fixed-k `PT` Kramers doublet. For a two-dimensional parent doublet, each partner-doublet block has quaternionic form and

```math
M_jM_j^\dagger=s_j I_2.
```

Horizontal concatenation over partner doublets therefore gives

```math
MM^\dagger=\sum_j s_j I_2,
```

so the two nonzero singular values are equal.

The manuscript now separately states that a general multidoublet quaternionic block is only guaranteed to have Kramers-paired singular values, not complete nonzero singular-value isotropy.

The real-zincblende BIA caveat remains explicit.

This closes the previous technical overstatement.

## 8. Occupancy cross-spectrum model — FIXED

Equation for `S_x,12(omega)` is now attached to an explicit continuous-time immigration--death--exchange process:

```text
A immigration: gamma m;
B immigration: gamma m;
A death:       gamma x_A;
B death:       gamma x_B;
A -> B:        k x_A;
B -> A:        k x_B;
stationary means: m;
PSD convention: two-sided angular-frequency.
```

For this process the symmetric and antisymmetric modes relax at `gamma` and `gamma+2k`, respectively, yielding the reported difference of Lorentzians and zero crossing

```math
\omega_x=\sqrt{\gamma(\gamma+2k)}.
```

The manuscript also states that drift rates plus stationary mean alone would not determine the noise spectrum. This directly answers the previous underdefinition criticism.

## 9. Channel-null theorem — PROOF NOW EXPLICIT

For a positive internal sector `X`, Rev. 5 defines

```math
Y_X=MXM^\dagger\succeq0.
```

If the sector is null to channel `i`, then `(Y_X)_ii=0`, and PSD Cauchy-Schwarz gives

```math
|(Y_X)_{ij}|^2\le (Y_X)_{ii}(Y_X)_{jj}=0.
```

The zero cross contribution is therefore demonstrated rather than merely asserted.

## 10. Final-sink Poisson cancellation — PROOF STRENGTHENED

Rev. 5 now explicitly uses exclusive independent marking of a parent Poisson process:

```text
parent rate: Lambda;
final-sink mark J in {A,B};
probabilities p_A, p_B;
marked sink processes: independent Poisson processes with rates Lambda p_A and Lambda p_B.
```

Independent random displacement/delay preserves the Poisson character and independence.

Therefore the ideal endpoint cross-spectrum is zero under the stated assumptions.

The assumptions remain restrictive and correctly visible:

```text
Poisson primaries;
independent noninteracting lineages;
exactly one final sink;
final-sink-only readout;
no branching/gain;
no shared electronics.
```

No overclaim was found.

## 11. Shockley--Ramo finite-frequency result — PASS

The manuscript retains the correct distinction

```math
Q_i^{rec}=0
```

while

```math
H_i^{rec}(\omega)
=i\omega e\int\Delta\phi_i(t)e^{-i\omega t}dt
```

can be nonzero for `omega != 0`.

Rev. 5 continues to say that the single-lineage source null can be lifted and that a nonzero ensemble cross-spectrum becomes **allowed, not guaranteed**.

That qualification is essential and remains intact.

## 12. “Certified” language — FIXED

Rev. 5 explicitly states that certification is conditional on:

```text
X lying in the declared admissible domain;
lambda_D actually bounding the relevant coupling over that domain;
the measured response being attributable to X.
```

The language no longer reads as an unconditional experimental inversion guarantee.

## 13. Uniform-task bound — FIXED

The manuscript now states `d>1` before

```math
\frac{q_{worst}}{q_{iso}}
\le
\frac{d-\mathcal S_{mix}}{d-1}.
```

No issue remains.

## 14. Abstract — IMPROVED, STILL DENSE

The abstract is now contribution-ranked and no longer promotes the reciprocal definition as a central discovery.

It remains approximately 200 words and still carries:

```text
principal theorem;
tightness hierarchy;
HgCdTe numbers;
PT/BIA qualification;
recycling readout result;
stage-specific thesis.
```

A hostile editor could still prefer a leaner abstract, particularly moving the detailed PT qualification into the body. This is an editorial refinement opportunity, not a correctness defect and not sufficient by itself to trigger Rev. 6.

## 15. Rendered presentation — PASS

The controlling 8-page artifact was inspected page by page.

A first Rev. 5 render exposed one Fig. 4 label collision. That was repaired and the manuscript rebuilt through CI.

The final artifact has:

```text
undefined references: none
undefined citations:  none
overfull boxes:        none
visible clipping:      none
figure overlap:        none
table clipping:        none
broken glyphs:         none
```

The remaining underfull paragraph and REVTeX stuck-float warning are visually harmless in the controlling render.

## 16. What a difficult referee can still attack

The strongest surviving attacks are now editorial rather than technical:

### A. Breadth

A referee may still argue that the task/coherence and readout sections are too far from the semiconductor theorem for a single article.

Defense: Rev. 5 no longer claims common microscopic dynamics. It claims a common restriction on inference across stage-specific maps, and demonstrates three different failure modes of cross-stage or cross-task inference.

### B. Applied significance of the general framework

A referee may say the stage-specific principle is conceptually sensible but not itself mathematically surprising.

Defense: the paper's novelty does not rest on the principle alone. The central semiconductor population theorem, shell-resolved tightness decomposition, quantitative HgCdTe closure, and conservative endpoint-versus-Ramo observability boundary provide the substantive physics.

### C. Generic selectivity section

The `r_eff`, task, and bright-projector material is mathematically simpler than the semiconductor theorem and could be viewed as explanatory scaffolding.

This is true. The manuscript now treats it as scaffolding rather than as the primary theorem. An editor could request compression without undermining the central results.

## 17. Referee-style verdict

If reviewing Rev. 5 after the previous major-revision report, the appropriate disposition is no longer “major revision required.”

A difficult but fair report would be approximately:

> The revised manuscript has addressed my principal technical concerns. The stable-rank terminology is corrected, the `PT`-isotropy statement is restricted to the single-parent-doublet situation actually used in the validation, and the stochastic process underlying the occupancy cross-spectrum is now explicit. The authors also substantially improved the organization by making stage-specific non-transferability, rather than the definitional reciprocal normalization, the conceptual thesis. The new full population-tightness hierarchy and its HgCdTe closure are particularly useful. I still regard the manuscript as unusually broad, and the task/coherence section could be compressed, but I no longer see a technical or conceptual defect that requires another major revision.

## 18. Current rating

```text
Mathematical correctness:               9.4 / 10
Semiconductor physics:                  9.5 / 10
HgCdTe validation:                      9.3 / 10
Readout/noise physics:                  9.2 / 10
Conceptual originality:                 8.7 / 10
Unification strength:                   8.4 / 10
Literature positioning:                 8.8 / 10
Physical Review Applied fit:            9.0 / 10
Resistance to hostile technical review: 9.2 / 10
Resistance to hostile editorial review: 8.2 / 10
```

The largest gain relative to Rev. 4 is editorial robustness, not a change in the central theorem.

## Final disposition

```text
CENTRAL OPTICAL THEOREM:             PASS
STABLE-RANK TERMINOLOGY:             FIXED
FULL TIGHTNESS HIERARCHY:            PASS
HgCdTe NUMERICAL CLOSURE:            PASS
PT SINGLE-PARENT QUALIFICATION:      FIXED
MARKOV NOISE MODEL:                  FIXED
CHANNEL-NULL PROOF:                  PASS
FINAL-SINK POISSON PROOF:            PASS
SHOCKLEY-RAMO RESULT:                PASS
STAGE-SPECIFIC UNIFICATION:          PASS WITH MODERATE EDITORIAL RISK
RENDERED PDF:                        PASS
NEW SCIENTIFIC REVISION REQUIRED:    NO
```

Rev. 5 should supersede Rev. 4 as the flagship submission manuscript. Do not reopen theory by default. Remaining work should be submission metadata/data-availability production unless an external referee or editor identifies a concrete scientific issue.
