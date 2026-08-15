# Experiment 13 — hostile review of unified manuscript Rev. 2

**Date:** 2026-08-15  
**Manuscript:** `PAPER_DRAFT_REV2_2026-08-15.md`  
**Disposition:** **CENTRAL GENERALIZATION PASSES / FLAGSHIP UNITY STRENGTHENED / TWO IMPORTANT DOMAIN-SCOPE REPAIRS + ONE HgCdTe MODEL-SYMMETRY REPAIR REQUIRED / REV3 AUTHORIZED**

---

# 1. Executive verdict

Rev. 2 is the first manuscript version whose central theorem naturally contains both the full nonuniform Experiment-09 coherence dimension and the global nonuniform Experiment-12 thermal ensemble.

The activity-weighted reciprocity

```math
\boxed{S_X tau_X=1}
```

is a materially better organizing theorem than the earlier stable-rank-only form.

Rev. 2 also retains the strongest physical content:

```text
fixed-trace task penalty;
nonuniform N_eff recovery;
full cross-mu Fermi/Kubo population theorem;
direct-sum thermal capacity reciprocity;
shellwise decomposition;
production eight-band HgCdTe closure;
endpoint-counting / finite-transit Ramo recycling boundary.
```

No counterexample to these results was found.

However, Rev. 2 still leaves one mathematically important choice implicit: **the domain over which `lambda_max` is taken**. This must be fixed physically before the reciprocity is interpreted as a resource bound.

A second repair is conceptual: the recycling section can now be embedded more directly into the same positive-operator framework through channel-specific observability effects.

A third repair is model scope: `S_a^act=1` in the current HgCdTe validation is symmetry enforced by the BIA-neglecting model and must not be stated as a universal property of real zincblende HgCdTe.

---

# 2. BLOCKING CONCEPTUAL ISSUE — the admissible capacity domain must be declared

Rev. 2 begins with a positive operator `G` and defines

```math
lambda_+=lambda_max(G).
```

But a resource theorem is meaningless until the space on which that maximum is taken is specified.

If one is free to enlarge the comparison space by adding an irrelevant but strongly coupled direction, `lambda_+` can increase while the actual response `Tr(GX)` remains unchanged. The inferred lower bound

```math
N_cap=Tr(GX)/lambda_+
```

would then become arbitrarily weaker for a purely bookkeeping reason.

The correct theorem must therefore begin with a **physically declared admissible domain** `D` and require

```math
supp(X) subset D.
```

Let `P_D` be the projector onto that domain and define

```math
G_D=P_D G P_D,
```

```math
lambda_D=lambda_max(G_D).
```

Then

```math
S_{X|D}
=lambda_D TrX / Tr(G_D X),
```

```math
tau_{X|D}
=Tr(G_D X)/(lambda_D TrX),
```

and

```math
\boxed{S_{X|D}tau_{X|D}=1.}
```

The domain must be fixed by the physical question before the spectrum is evaluated.

### Experiment-12 example

This is already handled correctly there. `D` is the selected endpoint shell space defined by

```text
cross-mu endpoint condition;
optical window B;
exact-energy shell decomposition;
chosen physical velocity polarization.
```

The ordinary supremum is then taken only over those allowed selected blocks.

### Experiment-09 example

`D` is the microscopic excited-state manifold over which the matched-population dark state and bright state are defined.

### Task example

`D` is the declared task subspace.

### Recycling example

`D` is the declared internal innovation/lineage sector for a chosen channel and frequency.

**Required Rev3 change:** make the admissible domain part of the theorem statement, not a later caveat.

---

# 3. Brightest direction need not be populated — explain why that is meaningful

For a nonuniform `X`, the eigenvector attaining `lambda_D` need not carry appreciable weight in the actual ensemble and may even lie outside `supp(X)` while remaining inside `D`.

This is not a defect. It is precisely why the inverse capacity estimate can be loose: the resource theorem is using the strongest **allowed** per-direction coupling, not the average coupling of the actual occupied ensemble.

In Experiment 12 this distinction is physically important. The production HgCdTe capacity is set by the strongest allowed selected shell, while the thermal population samples many shells with lower capacities.

**Required Rev3 clarification:** describe `S_{X|D}` as

```text
admissible peak response / actual ensemble-average response
```

rather than implying that the actual ensemble itself necessarily contains the peak direction with significant weight.

---

# 4. The direct-sum Experiment-12 construction passes

The endpoint operator

```math
G_B
= direct sum of upper A A^dagger blocks
  plus lower B^dagger B blocks
```

is legitimate.

It should be described explicitly as an **endpoint-lifted space** because each optical transition contributes once through its electron endpoint weighting and once through its hole endpoint weighting in `R_B`.

The thermal activity operator then gives

```math
Tr X_B^act / V=n_e,B^act+n_h,B^act
```

and

```math
Tr(G_B X_B^act)/V=R_B.
```

The resulting global capacity reciprocity is exact.

No double-counting defect is present: the two contributions correspond to the two endpoint populations that the theorem is bounding.

---

# 5. HgCdTe `S_a^act=1` is now analytically understood

The production calculation finds

```text
S_a^act=1
```

for every contributing active shell to machine precision.

This is not a numerical accident.

The second-order bulk eight-band Kane model used in the validation omits explicit bulk-inversion-asymmetry/Dresselhaus terms. In that model, the combined antiunitary `PT` symmetry leaves each `k` fixed and produces twofold endpoint doublets. Velocity is odd under both `P` and `T` and therefore even under `PT`.

A `PT`-even operator between two antiunitary doublets has quaternionic `2 x 2` form

```math
M=
\begin{pmatrix}
a&b\\
-b^*&a^*
\end{pmatrix},
```

so

```math
MM^dagger=(|a|^2+|b|^2)I_2.
```

Concatenating several partner doublets preserves this proportionality. Equal nonzero singular values and `S_a^act=1` therefore follow exactly within the model symmetry class.

### Required physical caveat

Real HgCdTe is zincblende and has bulk inversion asymmetry. More complete BIA-inclusive models can lift the exact fixed-k doublet/quaternionic structure.

Therefore Rev. 3 must say:

```text
"S_a^act=1 is symmetry enforced in the BIA-neglecting second-order Kane validation model"
```

and must not say or imply:

```text
"real HgCdTe generically has S_a^act=1."
```

The abstract Experiment-12 theorem is unaffected by this model limitation.

---

# 6. Recycling can now be integrated through channel-specific positive effects

At fixed frequency let

```math
y=M(omega) xi
```

with innovation covariance `Sigma>=0`.

For terminal `i`, define

```math
\boxed{
G_i(omega)
=M^dagger|i><i|M
\succeq0.
}
```

Then

```math
S_ii=Tr(G_i Sigma).
```

For terminals `i,j`, define the off-diagonal overlap operator

```math
C_ij=M^dagger|j><i|M,
```

so

```math
S_ij=Tr(C_ij Sigma).
```

If an internal sector `X` satisfies

```math
Tr(G_iX)=0,
```

then its auto-response in channel `i` is zero, and Cauchy-Schwarz forces its cross contribution with every other channel to vanish.

Thus a **channel null** is sufficient for zero cross-noise.

### Endpoint lineage

For an A-to-B conservative lineage under final-sink counting,

```math
H_end=g_B e_B,
```

so the A-channel effect is null on that lineage sector.

### Finite-transit Ramo lineage

The same sector can acquire

```math
H_A^rec(omega) != 0
```

at finite frequency, lifting the A-channel null. Joint A/B visibility becomes possible and therefore cross-noise becomes allowed.

This embeds the recycling result directly into the staged positive-operator language without pretending that the off-diagonal cross-spectrum itself is positive.

**Required Rev3 change:** use channel effects `G_i` and overlap operators `C_ij` explicitly.

---

# 7. The central reciprocity remains algebraically elementary

A skeptical referee can still write

```math
S_X=lambda/qbar,
```

```math
tau_X=qbar/lambda
```

and say that their product was defined to equal one.

This objection is valid at the algebra level.

The flagship manuscript must therefore continue to place its scientific weight on the independent realizations:

```text
Experiment-09 N_eff arises from an optimal quantum projector problem;
Experiment-12 tau arises from a nontrivial Fermi + Kubo + basis-invariant capacity theorem;
HgCdTe decomposition predicts which physical source causes the theorem slack;
Experiment-03 channel null is changed by a real finite-transit readout mechanism.
```

The central identity is a bridge, not the sole novelty.

This framing is currently adequate.

---

# 8. Fresh prior-art status

Targeted searches continue to support the existing boundary:

```text
Ramo/corpuscular p-n junction GR-noise coupling: established;
HgCdTe photon-recycling lifetime/performance: established;
HgCdTe photon-reabsorption mean crosstalk: established;
BIA terms in eight-band zincblende models: established;
generic stable-rank/positive-operator algebra: established.
```

No searched source directly states the combined detector-specific results

```text
activity-weighted selectivity ↔ optical thermal state-count capacity;
or
conservative one-final-sink recycling cross-noise null ↔ finite-transit Ramo channel-null lifting.
```

This is still not a certified novelty claim; it keeps the branch open.

---

# 9. Referee disposition

```text
ACTIVITY-WEIGHTED CENTRAL THEOREM:       PASS with domain declaration required
EXPERIMENT-09 NONUNIFORM N_eff:          PASS
EXPERIMENT-12 DIRECT-SUM MAPPING:        PASS
SHELL DECOMPOSITION:                     PASS
PRODUCTION HgCdTe NUMERICS:              PASS
HgCdTe S_a=1 INTERPRETATION:             REPAIR MODEL SCOPE
CHANNEL-SPECIFIC OBSERVABILITY:          ADOPT
RAMO ENDPOINT/AC BOUNDARY:               PASS
FLAGSHIP UNITY:                          PASS
REV2 AS FINAL SCIENTIFIC DRAFT:          NO
REV3:                                    AUTHORIZE
STANDALONE PAPER SUPERSESSION:           STILL HOLD
```

## Required Rev. 3 changes

1. Put the physically declared admissible capacity domain `D` in the master theorem.
2. Define `lambda_D` on that domain and require `supp(X) subset D`.
3. Clarify that the capacity-maximizing direction may be sparsely populated by the actual ensemble.
4. Describe the Experiment-12 direct sum as an endpoint-lifted activity space.
5. Explain `S_a^act=1` through the BIA-neglecting model's `PT` symmetry and add the real-zincblende caveat.
6. Rewrite the recycling section using channel effects `G_i` and cross-overlap operators `C_ij`.
7. Keep the central identity as organizing reciprocity; keep the physical theorems as the novelty-bearing content.
