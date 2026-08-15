# Experiment 13 — hostile review of the unified manuscript architecture

**Date:** 2026-08-15  
**Role:** skeptical high-level referee/editor  
**Object reviewed:** `UNIFIED_MANUSCRIPT_ARCHITECTURE_2026-08-15.md` plus the supporting Experiment-13 derivations  
**Disposition:** **SCIENTIFIC UNITY IS REAL / CURRENT ARCHITECTURE IS NOT A MERE ANTHOLOGY / FLAGSHIP DRAFT IS NOW JUSTIFIED / REPLACING THE THREE STANDALONE PAPERS IS NOT YET JUSTIFIED**

---

# 1. Executive verdict

The unified project has crossed an important threshold.

At the start of Experiment 13, the proposed unity was vulnerable to immediate rejection as

```text
"measurement operators matter" + elementary singular-value bounds.
```

That would not have been a publishable flagship contribution.

The present architecture is stronger because Experiment 13 has generated results that **did not exist in the source manuscripts**:

1. the exact coherence-selectivity / state-count-tightness reciprocity;
2. its dispersive shell decomposition with independent Fermi and capacity factors;
3. a realistic eight-band HgCdTe closure showing `~0.571 x ~0.308 ~= ~0.176` and no active-shell coherence anisotropy;
4. the conservative photon-recycling endpoint-counting versus finite-transit Shockley–Ramo observability boundary;
5. a quantitative fixed-trace task penalty tied directly to the coherence-selectivity factor.

These are genuine cross-branch deductions. The project is no longer merely putting common notation around Experiments 01, 09, and 12.

A unified manuscript draft is therefore scientifically justified.

However, the evidence is not yet strong enough to destroy the independent publication paths. The correct strategy is to draft and attack the flagship paper **in parallel**, then decide whether it supersedes the standalone manuscripts only after the full draft survives review.

---

# 2. Strongest aspect: there is now one quantitative spine

The strongest equation chain is

```math
\boxed{
\mathcal A_{max}
=\mathcal S_{coh}
=\frac{d}{r_{st}}
=\frac1{\tau_{count}}.
}
```

This is useful because each factor has a different detector meaning:

```text
A_max:
    maximum task advantage at fixed total coupling/information strength;

S_coh:
    coherent bright-state response relative to a uniform incoherent internal excitation;

tau_count:
    fraction of the parent state count certified by the same optical response under a spectral-capacity bound.
```

The paper then adds

```math
\boxed{
\frac{q_{worst}}{q_{iso}}
\le
\frac{d-\mathcal S_{coh}}{d-1},
}
```

so the coherence advantage carries a guaranteed task penalty elsewhere.

Finally the physical thermal theorem inserts an independent factor

```math
\eta_F\le1
```

and the dispersive material theorem becomes

```math
\boxed{
\tau_{obs}^{act}
=\eta_F
\sum_a w_a^{act}\frac{c_a}{\mathcal S_a^{act}}.
}
```

This is a coherent progression from abstract spectral concentration to a realistic semiconductor observable.

That is the manuscript's strongest intellectual spine.

---

# 3. Why the stable-rank reciprocity is not automatically enough

A hostile referee will immediately notice that

```math
\mathcal S=d/r_{st}
```

and

```math
\tau=r_{st}/d
```

were defined so their product is one.

If presented badly, the central result will look tautological.

The paper must therefore **not** sell `S*tau=1` as surprising algebra.

The scientific content is instead:

1. `S` arises independently from a detector discrimination problem;
2. `tau` arises independently from an inverse equilibrium state-count theorem;
3. both are physically realized by the **same microscopic optical coupling block**;
4. the realistic dispersive theorem shows exactly how the reciprocity survives energy resolution, global capacity, and thermal occupations;
5. the HgCdTe calculation produces a nontrivial decomposition not known when either source paper was derived.

If these five points are explicit, the tautology objection is manageable.

If the paper simply introduces `r_st` and then defines two reciprocal ratios, it should be rejected.

---

# 4. Experiment 12 must remain the physical center of gravity

The unified paper should not give equal page weight to all branches.

Experiment 12 contains the hardest physical theorem:

```math
n_e+n_h
\ge
n_{e,B}^{act}+n_{h,B}^{act}
\ge
\frac{2}{\pi e^2u_B^2}
\int_B
\frac{\hbar\omega\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}d\omega.
```

That result requires real semiconductor/statistical physics:

```text
Fermi occupations;
chemical-potential crossing;
Kubo-Greenwood response;
energy-shell projectors;
degenerate-subspace basis invariance;
velocity-block capacity;
active-support rank.
```

The other sections should orbit this result rather than compete with it.

Recommended hierarchy:

```text
core theorem/material result:            Experiment 12;
operator spectral interpretation:        Experiment 13;
coherence extreme:                       Experiment 09;
task-order consequence:                  Experiment 01;
terminal-observability extension:         Experiment 03.
```

This will make the paper look like a deep theorem with broad consequences rather than four papers taped together.

---

# 5. Experiment 01 connection: now real, but use sparingly

Originally Experiment 01 risked looking unrelated because its detailed problem is unknown arrival time, finite observation, and false-alarm/search geometry.

The fixed-trace theorem repairs that conceptual gap:

```math
TrG_A=TrG_B,
\quad G_A\ne G_B
\Longrightarrow
G_A-G_B\text{ indefinite},
```

so opposite task orderings necessarily exist.

The quantitative selectivity penalty strengthens this further.

However, the standalone Experiment-01 manuscript contains a specialized continuous-time search problem far more elaborate than the unified paper needs.

A unified paper should include exactly one strong physical witness and then stop.

If it imports Palm rare-event machinery, hard-window technical history, or multiple task-reversal constructions, the narrative will fracture.

**Referee disposition:** Experiment 01 belongs as a corollary/witness, not as a coequal subpaper.

---

# 6. Experiment 09 connection: mathematically clean, but distinguish idealization levels

The rank-one bright selector

```math
G=|B><B|
```

is the clean maximally concentrated endpoint:

```math
r_{st}=1,
\quad
S=N,
\quad
tau=1/N.
```

This is excellent pedagogically.

But the source Experiment-09 paper also contains kinetics, dephasing, extraction scaling, and thermodynamic reverse-rate arguments.

Most of that does not belong in the unified paper.

A referee will also note that the ideal coherent selector is a quantum-state-level construction, whereas the realistic HgCdTe example has locally isotropic active shell blocks. This is not a defect if stated properly.

Indeed the HgCdTe result is useful precisely because it shows the framework does not force a coherence-selective interpretation onto every detector.

**Referee disposition:** retain the bright-state result as the spectral-concentration extreme; move most Experiment-09 kinetics outside the flagship.

---

# 7. HgCdTe decomposition is unusually valuable

The new numerical finding

```text
S_a^act=1
```

for all thermally important selected exact-shell blocks is scientifically useful.

A weaker manuscript would have tried to claim that the realistic material demonstrates all pieces of the unification simultaneously.

It does not.

Instead the broad-window active-bound tightness is approximately

```text
capacity utilization  ~0.571
Fermi/Kubo factor      ~0.308
product                ~0.176.
```

This is a strong diagnostic result because it identifies **why the bound is not tight**.

The realistic example therefore validates the decomposition while falsifying the simplistic hypothesis that singular-spectrum coherence concentration explains the HgCdTe slack.

That improves credibility.

A production run should verify these factors with the exact same continuous-capacity and quadrature discipline used for Rev11 before numerical values enter a manuscript.

---

# 8. Experiment 03 / Ramo result: potentially high impact, but highest novelty risk

The conservative-recycling result is conceptually excellent:

```text
internal recycling can be real;
mean optical crosstalk can be real;
internal population correlations can be real;
endpoint count cross-noise can still be exactly zero.
```

The finite-transit derivation adds

```math
H_k^{rec}(0)=0
```

for an internally created/recombined pair but generically

```math
H_k^{rec}(\omega)\ne0
```

at finite frequency.

This yields a sharp detector prediction:

```text
endpoint/DC readout can hide a conservative recycling lineage;
finite-frequency Ramo motion can expose the same lineage.
```

The literature audit so far finds established photon recycling/crosstalk modeling and established Ramo treatment of semiconductor GR noise, but no direct collision with this combined conservative-lineage boundary.

Nevertheless this is the section I would attack most heavily as a referee because adjacent detector-noise literature is old and broad.

Before submission, it needs a dedicated literature search reaching beyond keyword-level HgCdTe papers into classical semiconductor noise theory, segmented-detector induced-charge theory, and queue/shot-noise descriptions.

**Referee disposition:** retain; potentially one of the most memorable results; novelty audit must be deeper.

---

# 9. Major conceptual vulnerability: the symbol G changes physical roles

The architecture uses positive operators in several spaces:

```text
Experiment 01:
    signal/task information operator;

Experiment 09:
    state-selective measurement/coupling effect;

Experiment 12:
    microscopic optical velocity Gram block;

Experiment 03:
    stochastic transfer/lineage Gram geometry.
```

These are not literally one identical operator acting on one universal Hilbert space.

A careless manuscript could therefore overstate the unity.

The correct abstraction is a **measurement/coupling map at a specified stage of the detector chain**, not one universal `G` shared by all physics.

I recommend explicitly introducing a staged detector map:

```text
optical/task input
    -> microscopic excitation
    -> internal dynamics
    -> terminal readout.
```

Each stage or composite stage has its own map `M_j` and Gram/effect `G_j=M_j^\dagger M_j` on the appropriate input space.

The unity is:

```text
performance/resource/observability questions reduce to the spectral geometry
of the relevant physical map at the stage being interrogated.
```

The paper should never imply that the HgCdTe velocity block and the arrival-time matched-filter operator are physically the same matrix.

This clarification is mandatory.

---

# 10. Major novelty vulnerability: broad frameworks already exist

General photodetector modeling frameworks already connect internal quantum dynamics, absorption, amplification, measurement, and performance metrics.

Task-based Fisher/information-operator approaches are established.

Quantum detector POVM coherence sensitivity is established.

Bright/dark and superradiant/subradiant optical states are established.

Stable rank and singular-value concentration are standard mathematics.

Shockley–Ramo detector response is established.

Therefore the paper must never claim conceptual priority for any of these broad ideas.

The novelty claim must be restricted to the **specific cross-relations and detector theorems** derived here.

A suitable novelty statement is approximately:

> We do not propose a new general formalism for measurements. We show that several detector-specific limits derived independently become quantitatively linked when expressed through the spectral geometry of their physical coupling maps, yielding new reciprocity, decomposition, and observability results.

That is defensible if the remaining prior-art audit survives.

---

# 11. Is this one paper or still four papers?

At this stage, it is **one possible paper**.

The reason is that there is now a causal logical order:

```text
scalar compression loses spectral geometry
-> fixed-strength spectral concentration creates task selectivity
-> the same concentration controls coherence rejection
-> the reciprocal factor controls inverse state-count identifiability
-> thermal physics turns that into an optical population theorem
-> realistic HgCdTe decomposes the resulting slack
-> downstream readout null geometry determines whether internal dynamics survive to terminals.
```

That sequence is substantially stronger than

```text
here are four examples where operators matter.
```

The architecture therefore passes the **unity test**.

---

# 12. Does it justify sacrificing the three standalone papers?

Not yet.

Reasons:

1. Experiment 12 alone already has a focused PRB-level identity and realistic material validation.
2. Experiment 09 has a coherent PRA-level story whose extraction/scaling results would be mostly omitted from the unified paper.
3. Experiment 01 contains a mathematically specialized task/search result that would be heavily compressed.
4. The unified paper still has a higher editorial-risk profile because its scope crosses detection theory, quantum coherence, semiconductor optical response, and stochastic readout.
5. The new cross-relations may be viewed as elegant synthesis rather than enough novelty to compensate for the breadth.

Therefore the standalone manuscripts are currently valuable scientific insurance.

---

# 13. What would justify replacing them with one flagship paper

I would authorize replacement only after a full draft satisfies all of the following:

```text
A. central theorem is stated before any case study and survives without jargon;
B. Experiment-12 theorem follows naturally from the central geometry rather than feeling inserted;
C. HgCdTe decomposition is production-quality and quantitatively closes;
D. Experiment-01 witness occupies no more than one main-text section;
E. Experiment-09 bright-state result occupies no more than one main-text section;
F. Experiment-03 Ramo/recycling novelty survives a deeper literature audit;
G. entire main text can be kept around a normal long-article scale rather than becoming a monograph;
H. an external hostile reader describes the work as one theorem with consequences, not several papers summarized together.
```

If those conditions are met, replacing the separate submissions becomes defensible.

---

# 14. Recommendation

```text
SCIENTIFIC UNITY:                     PASS
COMMON QUANTITATIVE SPINE:            PASS
NEW CROSS-BRANCH THEORY:              PASS
REALISTIC MATERIAL VALIDATION:        PASS, needs production rerun
OBSERVABILITY EXTENSION:              PASS mathematically / novelty still under audit
GENERIC-REPACKAGING OBJECTION:        MANAGEABLE, not eliminated
FLAGSHIP MANUSCRIPT DRAFT:            AUTHORIZE
WITHDRAW/STAND DOWN EXISTING PAPERS:   DO NOT YET AUTHORIZE
```

## Next action

Write **Rev0 of the unified manuscript**, but keep it deliberately lean.

The Rev0 objective is not polish. It is to test whether the complete derivation can be read as one uninterrupted scientific argument.

After Rev0:

1. perform a hostile referee review of the actual manuscript, not the architecture;
2. compare its scientific impact and clarity directly against the three standalone papers;
3. only then decide whether "ultimate unity" is strong enough to supersede them.
