# Experiment 13 — unified manuscript architecture

**Date:** 2026-08-15  
**Status:** CANDIDATE FLAGSHIP ARCHITECTURE / NOT YET A MANUSCRIPT / SUBJECT TO HOSTILE REVIEW

## Working title

**Spectral geometry of photodetection: task selectivity, thermal state-count bounds, and hidden internal dynamics**

Alternative, more compact:

**Spectral geometry of photodetector performance and observability**

Avoid titles claiming a first "unified theory of photodetectors." General photodetector frameworks already exist.

---

# 1. One-sentence scientific thesis

A photodetector's physically relevant coupling/readout map contains more information than any scalar performance metric, and its spectral geometry imposes linked constraints on **which optical tasks are favored, how strongly coherence can reject incoherent internal generation, how tightly optical response can certify equilibrium state population, and which internal stochastic dynamics remain visible at the terminals**.

The paper must support this with exact detector-specific relations, not with the generic statement that measurement operators matter.

---

# 2. Headline new results

The unified paper should stand or fall on the following results.

## Result A — trace-constrained spectral concentration closure

For a positive detector coupling/information operator `G` on a `d`-dimensional task subspace with fixed total strength

```math
T=TrG,
```

define stable rank

```math
r_{st}=T/\lambda_{max}.
```

Then

```math
\boxed{
\mathcal A_{max}
=\mathcal S_{coh}
=\frac{d}{r_{st}}
=\frac1{\tau_{count}}.
}
```

Here:

```text
A_max   = best-task advantage over equal-trace isotropic coupling;
S_coh   = top-bright-state response / uniform incoherent response;
tau_count = tightness of the corresponding total state-count capacity bound.
```

This gives the central bridge among Experiments 01, 09, and 12.

## Result B — quantitative no-free-selectivity task penalty

If the selectivity factor is `S`, then under the same fixed trace there exists an orthogonal task with

```math
\boxed{
\frac{q_{worst}}{q_{iso}}
\le
\frac{d-S}{d-1}.
}
```

Equivalently the guaranteed fractional task loss is at least

```math
\boxed{
\mathcal L\ge\frac{S-1}{d-1}.
}
```

Thus coherence selectivity quantitatively forces task anisotropy.

## Result C — thermal optical state-count theorem

Retain the Experiment-12 observable theorem in its exact scope:

```math
\boxed{
n_e+n_h
\ge
n_{e,\mathcal B}^{act}+n_{h,\mathcal B}^{act}
\ge
\frac{2}{\pi e^2(v_{\mathcal B}^{cap})^2}
\int_{\mathcal B}
\frac{\hbar\omega\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
d\omega.
}
```

This is not merely an example. It is the nontrivial physical inverse theorem that turns the abstract spectral-capacity geometry into a material constraint.

## Result D — dispersive decomposition of theorem tightness

For exact energy-shell blocks `a`,

```math
\boxed{
\tau_{cap}^{act}
=\sum_a w_a^{act}
\frac{c_a}{\mathcal S_a^{act}}.
}
```

With the Fermi/Kubo efficiency,

```math
\boxed{
\tau_{obs}^{act}
=\eta_F^{global}
\sum_a w_a^{act}
\frac{c_a}{\mathcal S_a^{act}}.
}
```

Thus the observable state-count bound slack separates into

```text
thermal/Fermi asymmetry;
shell-to-global capacity mismatch;
singular-spectrum/coherence selectivity.
```

## Result E — realistic HgCdTe closure

For the broad 300-K, 10-um-class eight-band HgCdTe validation:

```text
S_a^act                 = 1 to numerical precision;
weighted capacity factor ~= 0.571;
Fermi/Kubo factor         ~= 0.308;
product                    ~= 0.176.
```

This reconstructs the established ~17.6% bound/active-population ratio and shows that realistic HgCdTe lies in the locally isotropic, shell-capacity-limited regime rather than the coherence-selective regime.

The headline total-reference lower bound remains approximately 11.8%.

## Result F — conservative-recycling observability theorem

For independent Poisson primary lineages with multichannel waveform `H_a`,

```math
\boxed{
S_{ij}(\omega)
=\sum_a\lambda_a
E[H_{a,i}(\omega)H_{a,j}^*(\omega)].
}
```

An ideal final-sink counter can map each conservative lineage to one terminal only, giving zero cross-spectrum despite internal recycling.

For a finite-transit Shockley–Ramo stage that is created and recombines internally,

```math
\boxed{
H_k^{rec}(0)=0
}
```

but generically

```math
H_k^{rec}(\omega)\ne0
```

at finite frequency.

Thus the same conservative photon-recycling lineage can be invisible in endpoint/DC readout and observable at finite frequency through pre-recombination carrier motion.

This supplies the Experiment-03 observability branch.

---

# 3. Paper narrative

## I. Why scalar photodetector metrics fail as complete descriptors

Begin with the concrete Experiment-01 premise:

```text
two detectors can share the same conventional scalar D* yet differ in response time.
```

Do not spend many pages rederiving the entire Applied Optics manuscript.

Use one explicit finite-time/unknown-arrival witness to establish the empirical-theory motivation:

```text
same scalar normalization does not determine task ordering.
```

Then introduce the detector information/coupling map and explain that scalar metrics are projections/compressions of a higher-dimensional object.

This is motivation, not the novelty claim.

---

## II. Spectral concentration theorem

Introduce

```math
q_G(\rho)=Tr(G\rho),
\qquad G\succeq0.
```

Derive:

```text
isotropic scalar-complete limit G=(T/d)I;
stable rank;
maximum task advantage;
coherent selectivity;
reciprocal state-count capacity tightness;
quantitative forced task penalty;
rank-deficient/null limit.
```

This section should be short and theorem-driven.

The algebra is simple; significance must come from the detector consequences that follow.

---

## III. Coherence-selective photodetection as the maximally concentrated endpoint

Use the clean uniform Experiment-09 construction:

```math
|B\rangle=N^{-1/2}\sum_j e^{i\phi_j}|j\rangle,
```

```math
\rho_D=I_N/N,
```

```math
G=|B\rangle\langle B|.
```

Then

```math
\mathcal S=N,
\qquad
\tau_{count}=1/N.
```

Explain the general nonuniform `N_eff` result but do not overload this section with the entire PRA kinetic/scalability manuscript.

If the passive-extraction `kT ln C` affinity theorem is included at all, put it in an appendix or discussion. The unified paper's central connection is spectral geometry, not the full Experiment-09 thermodynamic extraction theory.

---

## IV. Optical response as an inverse thermal-state-count measurement

Now introduce the Experiment-12 physical theorem.

The derivation should retain the real nontrivial physics:

```text
cross-mu direct transitions;
exact Fermi inequality;
Kubo-Greenwood spectral representation;
energy-shell projected velocity blocks;
basis-invariant operator capacity;
trace-rank population step.
```

Then identify the capacity-step tightness with the reciprocal selectivity geometry from Sec. II.

This is the pivotal section: it converts the abstract operator concentration theorem into an equilibrium material constraint.

---

## V. Dispersive decomposition and realistic HgCdTe

Present the exact shell sum

```math
\tau_{obs}^{act}
=\eta_F
\sum_a w_a c_a/S_a.
```

Then apply it to the existing eight-band HgCdTe model.

The important scientific point is not merely to repeat the 11.8% lower bound. It is to explain **why** the active bound reaches only ~17.6%:

```text
coherence/singular anisotropy: essentially no loss;
shell capacity utilization:   ~0.57;
Fermi/Kubo asymmetry:          ~0.308.
```

This gives the unified theory a realistic-material diagnostic that the standalone Experiment-12 manuscript did not have.

---

## VI. Internal dynamics versus terminal observability

Shift from optical coupling to stochastic readout maps.

For independent Poisson lineages, derive the multichannel shot-noise outer-product spectrum.

Then show three readout limits:

```text
occupancy-sensitive photoconductor:
    internal recycling spectrum visible;

finite-transit Shockley–Ramo photodiode:
    internally recombining stages have zero DC area but finite AC support;

ideal endpoint counter:
    conservative lineage ends in one terminal only;
    cross-spectrum exactly zero.
```

This section demonstrates that null geometry applies not only to optical input states but also to internal-process observability.

Do not claim generic Shockley–Ramo or Poisson-output theory as new.

---

## VII. Synthesis: what a scalar can and cannot certify

End with a compact hierarchy.

A scalar detector metric can be complete only on a subspace where the relevant normalized coupling operator is effectively isotropic.

Once spectral structure is resolved:

```text
largest eigenvalue -> strongest selected task / per-state response capacity;
stable rank         -> concentration/selectivity and inverse count tightness;
full spectrum       -> task ordering;
null space          -> completely hidden directions/process components;
energy-shell weights -> thermal/material realization;
lineage waveform overlap -> terminal stochastic observability.
```

The conclusion should be about **what detector measurements certify**, not about replacing `D*` universally.

---

# 4. Suggested figures

## Figure 1 — spectral-geometry map

One horizontal sequence of eigenvalue spectra at fixed trace:

```text
isotropic -> anisotropic -> rank one.
```

Under each spectrum show the linked consequences:

```text
task selectivity;
coherence rejection;
state-count tightness;
null-space growth.
```

This must be mathematically exact, not decorative.

## Figure 2 — Experiment-01 task-order witness

A minimal plot showing equal scalar normalization but opposite ordering for two task regimes. Use the strongest already validated witness rather than reproducing the entire standalone paper.

## Figure 3 — selectivity/count reciprocity

Plot

```math
S=d/r_st
```

and

```math
tau=r_st/d=1/S
```

for representative spectra at fixed dimension. Include the guaranteed worst-task penalty.

## Figure 4 — Experiment-12 theorem chain

A clean schematic/equation flow:

```text
cross-mu optical spectral weight
-> Fermi/Kubo lower functional
-> shell velocity strength
-> capacity/state-count bound.
```

## Figure 5 — HgCdTe decomposition

Use a bar/product decomposition:

```text
shell capacity ~0.571
x Fermi factor ~0.308
= active-bound tightness ~0.176.
```

A second panel can show shell selectivity `S_a=1` versus shell capacity utilization distribution.

## Figure 6 — recycling readout observability

Same A->B recycling lineage under:

```text
occupancy readout;
finite-transit Ramo readout;
endpoint counting.
```

Show why the source-pixel internally recombining waveform integrates to zero but has finite AC content.

Six figures is already generous. Do not add separate figures merely to preserve content from source manuscripts.

---

# 5. What must be omitted from the unified paper

To avoid becoming an anthology, omit or heavily compress:

```text
Experiment-01 long rare-event/Palm technical history;
all obsolete hard-window numerical attempts;
Experiment-09 full passive-extraction rate-scaling phase diagram;
most Experiment-09 architecture-specific kinetics;
Experiment-12 every intermediate revision/audit detail;
closed Experiment-10 material-admissibility branches;
closed nonreciprocity/active-volume/weighting-capacitance experiments.
```

Put only proof details required for rigor into appendices.

---

# 6. Required appendices

## Appendix A — trace-constrained operator proofs

Short proofs of:

```text
equal-trace reversal;
selectivity/count reciprocity;
guaranteed task penalty;
rank/null consequences.
```

## Appendix B — Experiment-12 Fermi/Kubo proof

Retain complete theorem proof and exact hypotheses.

## Appendix C — shellwise dispersive decomposition

Derive the weighted sum and active/total variants.

## Appendix D — eight-band HgCdTe model

Parameter table, chemical potential, velocity derivative, quadrature, ordinary-supremum audit, stable-rank audit.

## Appendix E — Poisson-lineage and Shockley–Ramo derivations

Complete event-lineage spectral formula and zero-area recombination proof.

---

# 7. Central claims that are safe enough to test with reviewers

Candidate claim language:

> We identify a common spectral geometry behind four apparently different photodetector questions: task ordering, coherence-selective rejection of incoherent internal excitation, inverse bounds from optical response to equilibrium quasiparticle population, and terminal visibility of conservative internal recycling. At fixed total coupling strength, spectral concentration produces an exact trade: the maximum task/coherence advantage is the reciprocal of state-count capacity tightness. For dispersive bands the reciprocal factor enters as a thermally weighted shell contribution, separable from Fermi asymmetry and global-capacity mismatch. A second result shows that conservative photon recycling can be exactly invisible to endpoint-counting cross-noise while reappearing at finite frequency through Shockley–Ramo carrier motion.

Do not claim:

```text
first general photodetector theory;
new singular-value mathematics;
new task-based information theory;
new quantum coherence theory;
new Shockley–Ramo theorem;
new Poisson-output theorem.
```

---

# 8. Hard kill criteria before a manuscript is written

Kill or downgrade the unified manuscript if any of the following holds after hostile review:

1. the selectivity/state-count reciprocity is judged merely definitional and yields no independent physical prediction;
2. the Experiment-01 result cannot be integrated without looking like a separate unrelated case study;
3. the Experiment-03 Ramo/recycling result has a direct prior-art collision;
4. the HgCdTe decomposition cannot be reproduced at production numerical precision;
5. the paper requires repeatedly changing the physical meaning of `G` without a clear abstract measurement-map definition;
6. the combined paper becomes substantially longer or less intelligible than the three standalone manuscripts;
7. a referee can summarize the whole contribution as only "measurement operators matter."

---

# 9. Current strategic recommendation

The architecture is now scientifically coherent enough to justify a hostile editorial/referee simulation.

However:

```text
DO NOT withdraw Experiment 01;
DO NOT withdraw Experiment 09;
DO NOT withdraw Experiment 12;
DO NOT yet convert this architecture into the only submission path.
```

The next step is a severe review of this exact architecture as a single flagship paper. The review must judge whether Results B, D, E, and F create enough genuinely new cross-branch physics to overcome the obvious "elementary operator repackaging" objection.
