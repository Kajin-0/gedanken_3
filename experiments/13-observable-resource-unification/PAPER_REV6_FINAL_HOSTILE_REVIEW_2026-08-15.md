# Extreme hostile review — Experiment 13 Rev. 6

**Date:** 2026-08-15  
**Target:** Physical Review Applied — Regular Article  
**Artifact:** Actions run `31905440563`, PDF SHA-256 `fa3c40b73ae8c75b8317e5522ebf50fb5fbf77c099aeeef52cf378a4febcf2e6`  
**Disposition:** **SECOND RE-REVIEW TECHNICAL ISSUES CLOSED / PUBLICATION OVERLAP RESOLVED BY SUPERSESSION POLICY / NO REV. 7 SCIENTIFIC REVISION TRIGGERED**

## Overall verdict

Rev. 6 addresses the remaining concrete technical criticisms from the Rev. 5 re-review without changing the central theorem.

The manuscript now has a defensible hierarchy:

```text
central finite-system semiconductor theorem;
explicit condition for macroscopic density inference;
full support/Fermi/capacity/selectivity tightness decomposition;
self-contained production HgCdTe realization;
forward task/coherence examples on their own stage map;
downstream recycling/readout counterexample on a distinct stage map.
```

The publication-overlap issue is not solved by wording inside the manuscript. It is solved by publication architecture: Experiment 13 is the sole active submission manuscript and Experiment 12 is held as a nonconcurrent fallback/development record. Under that policy, inherited theorem and HgCdTe material are not duplicate publication; they are the scientific core of the superseding manuscript.

If that project policy were later violated and Experiment 12 were submitted or published separately in substantially its present form, the overlap concern would immediately reopen.

## 1. Central optical population theorem — PASS

No mathematical term in the finite-system inequality changed:

```math
n_e+n_h
\ge n_{e,\mathcal B}^{act}+n_{h,\mathcal B}^{act}
\ge
\frac{2}{\pi e^2(v_{\mathcal B}^{cap})^2}
\int_{\mathcal B}
\frac{\hbar\omega\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}d\omega.
```

The pointwise Fermi inequality, Kubo-Greenwood normalization, exact-shell projected-block construction, operator-norm/rank step, and active-to-total population step remain as previously audited.

## 2. Thermodynamic-limit regression — FIXED

Rev. 6 explicitly distinguishes the finite-system result from the macroscopic density statement and restores

```math
\boxed{
\bar v_{\mathcal B}^{cap}
=\limsup_{j\to\infty}v_{\mathcal B,V_j}^{cap}<\infty.
}
```

The manuscript states that finite capacity at every finite volume is insufficient if the capacity itself diverges along the thermodynamic sequence.

This is the correct formal repair.

## 3. HgCdTe validation versus thermodynamic hypothesis — PASS

A further focused check asked whether the production HgCdTe model actually supplies the newly restored uniform bound rather than merely assuming it.

Rev. 6 now states the reason explicitly. On the stated compact momentum domain, the second-order eight-band velocity matrix is finite-dimensional and bounded. Any selected projected-block norm is bounded above by that microscopic operator norm. Consequently the continuous ordinary capacity supremum is finite and independent of normalization volume within the bounded-domain model.

Thus the model used for the macroscopic HgCdTe density example satisfies the required uniform-capacity hypothesis within its stated domain.

This does not assert validity of the k.p model at arbitrary momentum.

## 4. Standalone HgCdTe reproducibility — FIXED ENOUGH FOR MANUSCRIPT

Rev. 6 now includes the central production specification:

```text
Eg = 0.123984 eV
x = 0.17973
Delta = 1.04945 eV
F = -0.01618
gamma1 = 3.6273
gamma2 = 0.3598
gamma3 = 1.0717
EP = 18.8 eV
carrier cutoff = 2.0 nm^-1
mu from eight-band charge neutrality
production quadrature = 160 x 10 x 16
support check = 200 x 12 x 20
degeneracy clustering = 1e-7 eV
capacity search = continuous projected-block ordinary supremum
selected broad-window extent = 0.583 nm^-1
```

Together with the cited Hamiltonian/gap model and repository software, this removes the principal self-contained-method criticism.

A journal could still request an appendix containing more implementation detail, but the reported production numbers are no longer presented without the numerical settings needed to interpret them.

## 5. Numerical exact-rank realization — FIXED

Rev. 6 states that a numerical singular value is counted as nonzero for the support diagnostic when

```math
s>10^{-6}\ {\rm m/s}.
```

It also states the pre-existing audit on a reduced `40 x 6 x 8` grid: the broad-window active-support fraction is unchanged to printed precision when the threshold is swept from `1e-9` to `1e4 m/s`.

The manuscript correctly distinguishes this diagnostic threshold from the central population lower bound, which does not use numerical rank.

This is sufficient to support the reported `0.66897` active-support fraction as a stable numerical decomposition within the model.

## 6. Degeneracy clustering / capacity stability — PASS

The production clustering tolerance is `1e-7 eV`, and Rev. 6 reports that sweeping it from `1e-10` to `1e-5 eV` leaves the sampled capacity unchanged at reported precision.

The capacity itself is searched continuously in `(k,theta,phi)`, not taken as the maximum quadrature node.

No new numerical-capacity vulnerability is apparent.

## 7. `observability` terminology collision — FIXED

The optical bound-tightness variable is now

```math
\tau_{bound}^{act},
```

not `tau_obs`.

The word `observability` is therefore reserved for the downstream internal/readout null-space discussion, consistent with the manuscript's own stage-specific thesis.

Hard CI gates reject the obsolete optical `tau_obs^act` token.

## 8. Fermi/Kubo attribution — FIXED

The factor

```math
\eta_F=\mathcal L_{\mathcal B}/\mathcal R_{\mathcal B}
```

is now called the **Fermi-statistical factor**.

The manuscript explicitly states that its inequality/slack comes from the endpoint Fermi bound. Kubo-Greenwood supplies the exact spectral representation and introduces no additional inequality.

Figure 2 correspondingly says `Kubo map + Fermi bound`, and the tightness hierarchy labels `Fermi factor` rather than `Fermi/Kubo`.

This is physically cleaner.

## 9. Full tightness hierarchy — PASS

The central diagnostic relation remains

```math
\boxed{
\frac{n_{bound}}{n_{ref}}
=
\frac{n_{\mathcal B}^{act}}{n_{ref}}
\eta_F
\sum_a w_a^{act}\frac{c_a}{\mathcal S_a^{act}}.
}
```

It correctly separates:

```text
support coverage;
Fermi-statistical slack;
shell-to-global capacity utilization;
within-shell singular concentration.
```

The last two mechanisms remain inside the weighted sum in the general dispersive case; the manuscript does not falsely turn them into independent global scalar factors.

## 10. HgCdTe factorization — PASS

The unchanged broad-window values are

```text
support fraction         = 0.66897
Fermi factor eta_F       = 0.30684
capacity tightness       = 0.57262
active bound tightness   = 0.17570
full bound/reference     ~= 0.1175
```

with

```math
0.66897\times0.30684\times0.57262=0.1175398\ldots.
```

No numerical regression was introduced.

## 11. PT qualification — PASS

The Rev. 5 repair remains intact: complete singular-value isotropy is claimed only for thermally relevant selected parent shells that are single fixed-k `PT` Kramers doublets in the BIA-neglecting validation.

Generic multidoublet PT blocks are stated only to have Kramers-paired singular values, and real zincblende HgCdTe BIA remains an explicit caveat.

## 12. Recycling/readout section — PASS

No new revision was needed.

The immigration-death-exchange model remains explicit; the channel-null PSD argument is explicit; Poisson exclusive-final-sink splitting is explicit; and the Shockley-Ramo result remains restricted to

```text
zero integrated induced charge does not imply zero finite-frequency single-lineage support;
nonzero ensemble cross-spectrum becomes allowed, not guaranteed.
```

## 13. Publication overlap — RESOLVED CONDITIONALLY BY PROJECT POLICY

This was the potentially blocking item in the re-review.

The repository now contains an explicit Experiment-12 hold:

```text
Experiment 13 = sole primary active submission path;
Experiment 12 = frozen fallback/development provenance;
no concurrent or second overlapping submission in its current form.
```

This is the correct architecture if Experiment 13 is to inherit the central theorem and realistic material validation.

The condition is operational, not merely rhetorical: if the project later chooses to submit Experiment 12 separately, Experiment 13's overlap status must be re-audited before either manuscript proceeds.

## 14. Remaining editorial risk: generic task section

The strongest surviving hostile editorial criticism is still that the uniform-task material is mathematically simpler than the semiconductor theorem and not used by the HgCdTe or recycling calculations.

This is not a correctness issue.

For the present unified-paper goal it earns its place by representing the forward task-selectivity stage. If compression is requested, the generic uniform-task subsection should be shortened before sacrificing:

```text
the semiconductor theorem;
the full tightness hierarchy;
HgCdTe methods/validation;
the N_eff coherent photodetection specialization;
the endpoint-vs-Ramo observability boundary.
```

I would not trigger a new revision solely to preempt this possible editorial preference.

## 15. Rendered production — PASS

Controlling artifact:

```text
Actions run:     31905440563
artifact:        9252213152
pages:           8
undefined refs:  none
undefined cites: none
overfull boxes:  none
underfull boxes: none
visual QA:       all 8 pages pass
```

The added methods and thermodynamic material did not increase page count.

## Final referee-style disposition

A difficult but fair re-review after the supplied Rev. 5 criticism would now read approximately:

> The authors have addressed the remaining formal and reproducibility concerns. The finite-system theorem is now explicitly separated from its thermodynamic density interpretation through a uniform-capacity condition, and the HgCdTe validation states why that condition is satisfied within its bounded-domain model. The numerical quadrature, model parameters, rank threshold, and stability checks are given. Terminology has also been clarified so that observability is reserved for the terminal-map discussion and the statistical slack is correctly attributed to the Fermi inequality rather than Kubo-Greenwood. The earlier population-theorem manuscript is now explicitly held as a nonconcurrent fallback, resolving my publication-overlap concern provided that policy is maintained. I see no further technical revision that is necessary before submission, although the generic task subsection could be compressed at editorial request.

## Current assessment

```text
Mathematical correctness:                9.6 / 10
Semiconductor theorem:                   9.6 / 10
Tightness decomposition:                 9.6 / 10
HgCdTe interpretation:                   9.5 / 10
Standalone numerical reproducibility:    9.2 / 10
Readout/noise physics:                   9.4 / 10
Conceptual unification:                  8.7 / 10
Claim discipline:                        9.6 / 10
Physical Review Applied fit:             9.2 / 10
Hostile technical-review resistance:     9.5 / 10
Hostile editorial-review resistance:     8.5 / 10
```

## Final disposition

```text
CENTRAL THEOREM:                       PASS
THERMODYNAMIC CONDITION:              RESTORED / PASS
HgCdTe UNIFORM-CAPACITY LINK:         PASS
NUMERICAL METHOD DISCLOSURE:          PASS
SUPPORT-RANK THRESHOLD/STABILITY:     PASS
OBSERVABILITY TERMINOLOGY:            FIXED
FERMI/KUBO ATTRIBUTION:               FIXED
PUBLICATION OVERLAP:                  RESOLVED IF SUPERSESSION POLICY MAINTAINED
TASK/COHERENCE BREADTH:               MODERATE EDITORIAL RISK ONLY
PRODUCTION PDF:                       PASS
NEW SCIENTIFIC REVISION REQUIRED:     NO
```

Rev. 6 should supersede Rev. 5 as the flagship submission manuscript. Do not create Rev. 7 by default.
