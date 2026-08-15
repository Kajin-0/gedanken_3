# Experiment 13 — extreme novelty/significance review of unified Rev. 3

**Date:** 2026-08-15  
**Manuscript:** `PAPER_DRAFT_REV3_2026-08-15.md`  
**Review posture:** maximally skeptical editor/referee; generic mathematical novelty receives zero credit; every claim is compared against the strongest adjacent literature identified in the standalone audits and fresh primary-source searches.  
**Disposition:** **FLAGSHIP SURVIVES / NO DIRECT PRIOR-ART COLLISION FOUND FOR THE CROSS-BRANCH DETECTOR RESULTS / NOVELTY MUST BE CLAIMED NARROWLY / SIGNIFICANCE IS HIGHER THAN THE STANDALONE PAPERS IF THE PHYSICAL THEOREMS, NOT THE RECIPROCAL IDENTITY, LEAD THE PAPER**

---

# 1. Executive verdict

The unified manuscript survives the novelty kill test, but only under a disciplined statement of what is and is not new.

The following are **not** new and must receive no priority language:

```text
positive/Gram operators;
Rayleigh quotients and singular-value bounds;
stable rank / participation ratios;
task-dependent information matrices;
bright/dark states and concentration of oscillator strength;
quantum detector POVMs and coherence sensitivity;
Shockley–Ramo current induction;
generation–recombination noise in photoconductors or p-n junctions;
Poisson marking/thinning/output theorems;
photon recycling in direct-gap semiconductors;
mean optical crosstalk in photodiode arrays;
optical sum rules and geometric response bounds.
```

The manuscript remains publishably distinct because it derives **new detector-specific relations among independently physical quantities**, then validates one of them in a realistic multiband material model and extends the same staged geometry to terminal observability.

The strongest candidate-new content is:

```text
A. activity-weighted response-selectivity / inverse-certification reciprocity
   specialized to physically defined detector resource domains;

B. exact recovery of the Experiment-09 nonuniform N_eff from the same
   positive pairing whose inverse side becomes the Experiment-12 thermal
   capacity tightness;

C. endpoint-lifted formulation of the Experiment-12 thermal response as
   a positive activity pairing with lambda_max=(v_B^cap)^2;

D. exact dispersive shell decomposition
   tau_cap^act = sum_a w_a^act c_a/S_a^act;

E. production HgCdTe diagnosis
   0.5726 capacity utilization x 0.3068 Fermi/Kubo efficiency
   = 0.1757 active-bound tightness, with the absence of within-shell
   selectivity explained by PT symmetry of the BIA-neglecting model;

F. channel-null theorem for conservative recycling and its lifting by
   finite-transit Shockley–Ramo motion at finite frequency.
```

No searched source states this combination or an equivalent detector theorem.

Absence of a search hit is not proof of priority. The correct wording is therefore **“we derive”**, not “for the first time,” unless a formal literature review later establishes priority more strongly.

---

# 2. Claim matrix

## Claim 1 — one scalar does not rank every detector task

**Disposition: OLD.**

Task-based imaging/detection theory has long used Fisher-information matrices, Hotelling/ideal-observer task metrics, generalized NEQ, and related operators. Unknown-delay acquisition, search size, dwell time, false-alarm control, and correlated templates also have deep communications/radar/optical-ranging prior art.

Experiment 01 remains useful because it supplies a **specific detector time-scaling construction** in which one selected event-specific eventual matched-filter SNR is equalized while finite-time unknown-arrival ordering reverses. The flagship should use this as physical motivation/corollary, not as a broad novelty claim.

**Flagship role:** concise motivating witness only.

---

## Claim 2 — a positive coupling operator has a preferred direction and nulls

**Disposition: OLD / elementary.**

No novelty credit.

The equal-trace task penalty

```math
q_worst/q_iso <= (d-S)/(d-1)
```

is an exact useful corollary but follows from eigenvalue averaging. Do not sell it as new matrix theory.

**Flagship role:** establishes the task meaning of spectral concentration.

---

## Claim 3 — activity-weighted reciprocity

For a physically declared domain `D`, positive activity `X`, and positive effect/coupling operator `G_D`,

```math
S_{X|D}
=lambda_D TrX/Tr(G_DX),
```

```math
tau_{X|D}
=Tr(G_DX)/(lambda_D TrX),
```

so

```math
S_{X|D} tau_{X|D}=1.
```

**Mathematical novelty: NONE.** It is a normalized spectral-capacity identity.

**Detector novelty: PLAUSIBLE AS A CROSS-INTERPRETATION, NOT SUFFICIENT ALONE.**

The manuscript's defensible contribution is not the product identity. It is the demonstration that its two factors become independently meaningful detector quantities in different physics problems, with the same admissible-domain resource construction:

```text
forward selectivity of a physically allowed coupling map;
inverse activity/population certification from measured response.
```

Fresh searches around stable rank, participation ratio, oscillator strength, and bright-state concentration found substantial adjacent literature but no source connecting this response-selectivity ratio to a thermal optical state-count capacity theorem in photodetection.

**Flagship role:** connector theorem, not novelty headline.

---

## Claim 4 — nonuniform Experiment-09 N_eff specialization

For

```math
G=|B><B|,
X=rho_D=sum_j w_j |j><j|,
```

```math
S_X=1/sum_j w_j^2=N_eff.
```

**Generic ingredients: OLD.**

Quantum state discrimination, state verification, detector POVM coherence, bright/dark collective states, oscillator-strength concentration, and inverse participation measures are established.

Experiment 09 already correctly states that the generic measurement theorem is not new.

**Cross-branch result: PLAUSIBLY NEW.**

The new point is that the same activity-weighted response/capacity ratio that yields `N_eff` here becomes the exact global thermal velocity-capacity tightness in Experiment 12.

No searched source establishes that specific detector reciprocity.

**Flagship role:** clean rank-one endpoint demonstrating the meaning of the connector theorem.

---

## Claim 5 — direct cross-mu optical spectral weight bounds thermal endpoint population

**Disposition: DISTINCT / STRONGEST NOVELTY-BEARING RESULT.**

Experiment 12's theorem remains the physical center of gravity:

```math
n_e+n_h
>=n_B^act
>=
2/[pi e^2(v_B^cap)^2]
int_B
[hbar omega sigma_1^cross(omega)]/
[exp(hbar omega/(2kBT))-1] d omega.
```

The final Experiment-12 adversarial audit rederived the Fermi inequality, Kubo normalization, exact-shell direct-sum capacity, trace-rank step, and HgCdTe validation without finding a theorem defect.

Closest relevant modern literature includes:

```text
Onishi & Fu (2024): optical response / topology / quantum geometry / gap bounds;
Mao, Mendez-Valderrama & Chowdhury (2025): projected low-energy inverse-frequency optical sum rule and quantum geometry;
classical optical sum-rule literature.
```

Those works do not reproduce the Experiment-12 construction:

```text
direct cross-chemical-potential one-body transitions;
thermal Fermi endpoint kernel;
basis-invariant exact-energy shell velocity capacity;
inversion to equilibrium quasiparticle population.
```

The Mao et al. 2025 paper must be cited/discussed in the final unified reference network, as already identified in the Experiment-12 final audit.

**Flagship role:** principal physical theorem.

---

## Claim 6 — global endpoint-lifted activity operator

The unified manuscript writes the Experiment-12 exact thermal velocity strength as

```math
Tr(G_B X_B^act)/V=R_B
```

with

```math
lambda_max(G_B)=(v_B^cap)^2
```

on a declared endpoint-lifted direct-sum space.

**Disposition: NEW REFORMULATION / SCIENTIFICALLY USEFUL, BUT NOT A SEPARATE PRIORITY CLAIM.**

The direct-sum construction is consistent with the original theorem and contains no double counting defect: electron and hole endpoint sectors correspond to the two populations explicitly bounded.

Its value is that the activity-weighted reciprocity becomes exact globally even with nonuniform Fermi occupations and nonuniform shell capacities.

**Flagship role:** mathematical bridge between the central connector and the material theorem.

---

## Claim 7 — shellwise selectivity/capacity decomposition

```math
tau_cap^act
=sum_a w_a^act c_a/S_a^act.
```

**Disposition: CANDIDATE NEW DETECTOR RESULT.**

The algebra follows from standard singular-value identities, but no searched source was found that decomposes the tightness of a thermal optical population bound into exactly these physically interpretable factors:

```text
within-shell singular-spectrum concentration;
shell-to-global capacity mismatch;
thermal occupation weights;
with the independent Fermi/Kubo factor multiplying afterward.
```

The result is more than notation because it produces a quantitative material diagnosis that was not present in the standalone Experiment-12 manuscript.

**Flagship role:** strongest new cross-branch theorem after the base Experiment-12 population inequality.

---

## Claim 8 — production HgCdTe factorization

Production calculation:

```text
eta_F                       = 0.306836598
capacity tightness          = 0.572622972
observable active tightness = 0.175701685
```

and every contributing active shell has

```math
S_a^act=1
```

to about `4e-14`.

**Disposition: NEW NUMERICAL/STRUCTURAL RESULT WITHIN THE VALIDATION MODEL.**

The factorization reconstructs the independently known ~17.6% active-population bound and identifies the source of its looseness.

The machine-precision shell isotropy has an analytic explanation in the BIA-neglecting second-order Kane model:

```text
fixed-k antiunitary PT doublets;
PT-even velocity blocks;
quaternionic 2x2 structure;
equal nonzero singular values.
```

**Critical scope:** real zincblende HgCdTe has bulk inversion asymmetry. The exact `S_a^act=1` statement belongs to the BIA-neglecting validation model, not to HgCdTe universally.

The general population theorem is unaffected.

**Flagship role:** realistic validation and mechanism diagnosis.

---

## Claim 9 — GR noise depends on terminal coupling / Ramo weighting

**Disposition: OLD.**

Classical generation–recombination noise literature and Dąbrowski's corpuscular/Ramo treatments explicitly emphasize the coupling problem and proper Shockley–Ramo formulation for p-n junction noise.

The flagship must cite this literature and must not imply that it discovered the distinction between internal carrier fluctuations and terminal current.

**Flagship role:** prior-art foundation for the downstream extension.

---

## Claim 10 — photon recycling and mean photodiode crosstalk

**Disposition: OLD.**

HgCdTe and other direct-gap semiconductor literature treats photon recycling, radiative lifetime changes, reabsorption, and deterministic crosstalk between photodiode pixels.

**Flagship role:** physical process whose *noise observability* is being reconsidered.

---

## Claim 11 — ideal conservative final-sink counting can have zero interpixel cross-noise

Under:

```text
Poisson primary generation;
independent noninteracting lineages;
one final sink per lineage;
final-sink-only measurement;
no branching/gain;
no shared electronics,
```

final sink streams are independent Poisson thinnings/displacements.

**Underlying stochastic mathematics: OLD.**

Poisson output of infinite-server/routing networks is established.

**Detector specialization: PLAUSIBLY DISTINCT.**

Fresh searches did not locate a photodiode/photon-recycling paper stating the counterintuitive combination:

```text
nonzero conservative recycling / nonzero mean crosstalk
but
zero passive final-extraction interpixel cross-spectrum.
```

This should be claimed as a derived consequence under explicit hypotheses, not as new queueing theory.

**Flagship role:** first half of the observability boundary.

---

## Claim 12 — finite-transit Ramo lifting of the recycling channel null

For an internally created pair that recombines internally at a common point,

```math
Q_i^rec=0
```

for every electrode, while

```math
H_i^rec(omega)
=i omega e int Delta phi_i(t)e^{-i omega t}dt
```

can be nonzero at finite frequency.

Combined with channel effects

```math
G_i(omega)=M^dagger|i><i|M,
```

an A-to-B lineage that lies in the A-channel null under endpoint counting can acquire A-channel support under finite-transit Ramo readout.

**Shockley–Ramo ingredients: OLD.**

**Combined conservative-recycling channel-null theorem: CANDIDATE NEW DETECTOR RESULT.**

The searches found:

```text
classical Ramo GR-noise treatment;
photodiode impulse-response literature;
photon recycling in HgCdTe/GaAs devices;
photodiode-array optical/electrical crosstalk;
SPAD/SiPM correlated optical crosstalk;
```

but no direct source deriving the stated conservative one-final-sink null and its finite-frequency Ramo lifting.

This remains the highest prior-art-risk section because the historical semiconductor-noise literature is broad. The claim should remain narrow and conditional.

**Flagship role:** downstream extension showing that observability geometry is not merely an optical-input concept.

---

# 3. Significance assessment

## 3.1 What would make the paper insignificant

The manuscript should be rejected if framed as:

```text
"all detector problems can be written using positive operators"
```

or

```text
"selectivity times inverse tightness equals one."
```

Those statements are mathematically elementary and conceptually unsurprising.

## 3.2 What makes the current Rev. 3 potentially significant

The paper instead has a stronger causal chain:

```text
1. start from a real inverse semiconductor theorem;
2. identify its basis-invariant physical capacity resource;
3. discover that its capacity slack is exactly the inverse forward selectivity
   of the actual endpoint ensemble;
4. show the same relation reproduces an independently derived quantum
   coherence dimension;
5. resolve the global thermal slack shell by shell;
6. validate the decomposition at production resolution in eight-band HgCdTe;
7. explain a machine-precision numerical feature analytically through model symmetry;
8. extend the staged geometry to terminal observability and derive a
   conservative-recycling readout boundary.
```

That is a coherent theory paper, not an anthology.

The strongest significance comes from the combination of **general relation + nontrivial physical inverse theorem + realistic material diagnosis + downstream observability prediction**.

---

# 4. Editorial positioning

A broad/high-selectivity journal editor will likely ask whether the work changes how detector limits are thought about beyond HgCdTe.

The defensible answer is yes, but not because of a universal new metric.

The portable message is:

> A detector's maximum admissible coupling, its response to the actual activity ensemble, and the null geometry of the downstream readout answer different performance questions. Forward selectivity and inverse resource certification are reciprocal under a common declared capacity, while shell-resolved spectral structure and readout nulls determine where the bound becomes loose or internal dynamics disappear.

This can apply to other multiband semiconductors, coherence-selective detectors, and multichannel readouts after their physical maps and admissible domains are specified.

---

# 5. Reference-network requirements for the flagship

The final manuscript must explicitly include the following categories.

## Task / scalar incompleteness

Use the verified Experiment-01 task-based references and closest-prior-art audit. Avoid broad priority claims.

## Quantum/coherence detector theory

Use the Experiment-09 reference network, including state discrimination, detector POVM/coherence, collective bright/dark physics, and the relevant collective photocurrent/device comparator.

## Optical population theorem

Import the complete Experiment-12 bibliography, including:

```text
Kubo/optical conductivity foundations;
HgCdTe/Kane model parameters;
band-gap parameterization;
Onishi & Fu 2024;
Mao et al. 2025 literature-completeness amendment.
```

## Semiconductor noise / Ramo

At minimum cite classical p-n junction GR-noise/Ramo work such as Dąbrowski's corpuscular analysis and relevant predecessor literature. The manuscript must state that proper terminal coupling is established theory.

## Photon recycling / crosstalk

Cite direct HgCdTe photon recycling/reabsorption/crosstalk models and, if useful, other direct-gap photodiode recycling work.

## Poisson output

Cite the classical final-output theorem/network literature only to delimit the stochastic ingredient; do not overemphasize it.

---

# 6. Recommended claim language

### Safe central novelty language

> We derive detector-specific cross-relations between forward response selectivity and inverse resource certification, specialize them to coherence-selective and thermal multiband photodetection, and obtain a shell-resolved decomposition of the thermal population-bound tightness. We further derive a terminal-observability boundary for conservative photon-recycling lineages under endpoint and finite-transit readout.

### Safe Experiment-12 language

> The selected direct cross-chemical-potential conductivity gives a lower bound on the equilibrium population of the active one-body endpoint states under a finite basis-invariant shell velocity capacity.

### Safe HgCdTe language

> In the BIA-neglecting second-order eight-band Kane validation, the active exact-shell velocity blocks are singular-value isotropic by PT symmetry. The broad active-bound tightness is therefore controlled by shell-to-global capacity variation and Fermi/Kubo asymmetry rather than within-shell concentration.

### Safe recycling language

> Under independent conservative one-final-sink lineages, ideal final-sink counting yields zero interterminal cross-noise. Finite-transit Shockley–Ramo motion can lift a source-channel null at finite frequency, allowing—but not guaranteeing—interterminal recycling correlations.

### Avoid

```text
first unified theory of photodetection;
new general measurement principle;
new stable-rank theorem;
first proof that readout matters;
first use of Ramo theory for detector noise;
first theory of photon-recycling crosstalk.
```

---

# 7. Flagship decision after extreme review

```text
DIRECT PRIOR-ART COLLISION WITH MASTER CROSS-RELATION:      NOT FOUND
DIRECT COLLISION WITH EXPERIMENT-12 POPULATION THEOREM:    NOT FOUND
DIRECT COLLISION WITH SHELL DECOMPOSITION:                 NOT FOUND
DIRECT COLLISION WITH HgCdTe FACTOR DIAGNOSIS:             NOT FOUND
DIRECT COLLISION WITH RECYCLING CHANNEL-NULL/RAMO RESULT:  NOT FOUND
GENERIC INGREDIENT NOVELTY:                                NONE
NOVELTY CLAIM SCOPE:                                       NARROW / DETECTOR-SPECIFIC
SCIENTIFIC UNITY:                                          PASS
SIGNIFICANCE VERSUS STANDALONES:                           HIGHER IF FRAMED AROUND PHYSICAL THEOREMS
EDITORIAL BREADTH RISK:                                    MODERATE-HIGH
FLAGSHIP-FIRST STRATEGY:                                   RETAIN
SIMULTANEOUS OVERLAPPING SUBMISSION:                       AVOID
```

---

# 8. Next action

The novelty gate is sufficiently passed to proceed to a **claim/reference-clean Rev. 4**.

Rev. 4 should not add new theory by default. It should:

```text
1. reorder the narrative so the nontrivial physical population theorem carries
   more of the novelty burden than the elementary reciprocity;
2. import verified primary references from the three standalone networks;
3. insert the Mao 2025 neighboring-sum-rule citation;
4. cite classical Ramo/GR-noise and HgCdTe recycling/crosstalk literature explicitly;
5. remove any placeholder bibliographic language;
6. keep Experiment 01 concise;
7. preserve all admissible-domain, BIA, sigma_cross, and finite-frequency
   visibility caveats;
8. then perform another hostile review before typesetting.
```
