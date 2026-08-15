# Current State — Experiment 13: Spectral Geometry / Observable-Resource Unification

**Date:** 2026-08-15  
**Scope:** analytical/theoretical only  
**Status:** **ACTIVE / SCIENTIFIC UNITY TEST PASSED / TWO NEW CROSS-BRANCH THEOREMS + REALISTIC HgCdTe CLOSURE + RAMO RECYCLING RESULT / UNIFIED MANUSCRIPT REV1 EXISTS / STANDALONE PAPERS REMAIN ACTIVE**

## Read first

1. `PAPER_DRAFT_REV1_2026-08-15.md`
2. `PAPER_REV0_HOSTILE_REVIEW_2026-08-15.md`
3. `UNIFIED_MANUSCRIPT_HOSTILE_REVIEW_2026-08-15.md`
4. `COHERENCE_SELECTIVITY_STATE_COUNT_DUALITY_2026-08-15.md`
5. `DISPERSIVE_SELECTIVITY_CAPACITY_DECOMPOSITION_2026-08-15.md`
6. `HGCDTE_STABLE_RANK_CLOSURE_2026-08-15.md`
7. `FINITE_TRANSIT_SHOCKLEY_RAMO_RECYCLING_2026-08-15.md`
8. `PRIOR_ART_KILL_TEST_2026-08-15.md`

Do **not** withdraw or replace the existing Experiment-01 Applied Optics, Experiment-09 PRA, or Experiment-12 PRB manuscripts yet. The flagship Rev1 must first survive direct manuscript-level hostile review, complete reference auditing, and production numerical QA.

---

# 1. Correct abstraction

There is no single universal matrix that is simultaneously the arrival-time information operator, the microscopic optical velocity block, and the terminal readout transfer matrix.

The correct staged detector picture is

```math
\mathcal H_{task}
\xrightarrow{M_{opt}}
\mathcal H_{exc}
\xrightarrow{M_{dyn}}
\mathcal H_{int}
\xrightarrow{M_{ro}(\omega)}
\mathcal H_{term}.
```

For the stage/composite map relevant to a particular question,

```math
G_j=M_j^\dagger M_j\succeq0.
```

The unity is that **task preference, coherent response selectivity, inverse resource inference, and observability are controlled by different spectral/geometric features of the physically relevant map**.

Generic positive-operator / singular-value mathematics is established and is not a novelty claim.

---

# 2. New cross-branch theorem A — uniform-shell spectral concentration

Let `G>=0` act on a `d`-dimensional comparison shell/subspace, with

```math
T=TrG,
\qquad
r_st=T/lambda_max.
```

Compare against the equal-trace isotropic operator

```math
G_iso=(T/d)I.
```

Then the maximum pure-task response advantage is

```math
\boxed{
\mathcal A_{max}=d/r_{st}.
}
```

For the brightest eigenstate versus the uniform incoherent state `I/d`, define the generic **response selectivity**

```math
\boxed{
\mathcal S_{resp}=d/r_{st}.
}
```

If the same exact shell is incoherently populated with a common occupation weight `p`, the spectral-capacity state-count tightness is

```math
\boxed{
\tau_{count}=r_{st}/d.
}
```

Therefore

```math
\boxed{
\mathcal A_{max}
=\mathcal S_{resp}
=1/\tau_{count}.
}
```

This simple reciprocal identity is **not** to be applied blindly to nonuniform dark populations or across different equilibrium energies. The dispersive theorem below is the general physical form.

### Guaranteed task penalty

If the selectivity factor is `S`, then fixed trace forces at least one orthogonal task to satisfy

```math
\boxed{
\frac{q_{worst}}{q_{iso}}
\le
\frac{d-S}{d-1}.
}
```

Equivalently,

```math
\boxed{
\mathcal L_{task}
\ge
\frac{S-1}{d-1}.
}
```

This is tight when the remaining `d-1` eigenvalues are equal.

Two unequal equal-trace positive operators necessarily have opposite task orderings somewhere because their difference is nonzero Hermitian trace-zero and therefore indefinite.

Experiment 01 remains a separate physical witness: it equalizes eventual event-specific matched-filter SNR for one transient and studies finite-time unknown-arrival search geometry. Do not claim its full task operators are equal-trace unless separately proved.

---

# 3. Experiment-09 endpoint

For the ideal bright projector

```math
G=|B><B|
```

with uniform `N`-state population-matched incoherent dark state,

```math
r_st=1,
\qquad
d=N.
```

Hence

```math
\mathcal S_{resp}=N,
\qquad
\tau_{count}=1/N.
```

In this rank-one construction the generic response ratio coincides with the **actual proven conditional quantum rejection factor**:

```math
eta_gamma=1,
\qquad
epsilon_D=1/N.
```

For nonuniform weights, retain the Experiment-09 result

```math
N_eff=1/\sum_jw_j^2,
```

rather than replacing it with `d/r_st`.

---

# 4. Experiment-12 physical theorem remains the center of gravity

Use the authoritative cross-chemical-potential conductivity convention

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

The exact Fermi inequality is

```math
\boxed{
\frac{2D_{cv}}
{e^{E_{cv}/(2k_BT)}-1}
\le p_c+h_v.
}
```

With

```math
K_T(E)=E/[e^{E/(2k_BT)}-1],
```

```math
\mathcal R_B
\ge
\frac{2}{\pi e^2}
\int_B K_T(\hbar\omega)\sigma_1^{cross}(\omega)d\omega.
```

Using the basis-invariant exact-shell capacity `v_B^cap` gives

```math
\boxed{
 n_e+n_h
 \ge
 n_{e,B}^{act}+n_{h,B}^{act}
 \ge
 \frac{2}{\pi e^2(v_B^{cap})^2}
 \int_B
 \frac{\hbar\omega\sigma_1^{cross}(\omega)}
 {e^{\hbar\omega/(2k_BT)}-1}
 d\omega.
}
```

This requires the selected/direct cross-`mu` conductivity contribution; raw total measured conductivity cannot in general be inserted without decomposition.

---

# 5. New cross-branch theorem B — dispersive selectivity/capacity decomposition

For each selected exact electron/hole endpoint shell `a`, define

```math
lambda_a=||M_a||_op^2,
r_a=rank(M_a),
r_st,a=Tr(M_aM_a^dagger)/lambda_a,
S_a^act=r_a/r_st,a,
c_a=lambda_a/(v_B^cap)^2.
```

With thermal active-population weights

```math
w_a^act=p_ar_a/\sum_bp_br_b,
```

the capacity-step tightness is exactly

```math
\boxed{
\tau_{cap}^{act}
=\sum_aw_a^{act}\frac{c_a}{S_a^{act}}.
}
```

Define

```math
eta_F=L_B/R_B<=1.
```

Then the full observable Experiment-12 active-population tightness is

```math
\boxed{
\tau_{obs}^{act}
=eta_F
\sum_aw_a^{act}\frac{c_a}{S_a^{act}}.
}
```

Thus the theorem slack separates into

```text
thermal/Fermi asymmetry;
shell-to-global capacity mismatch;
singular-spectrum response concentration.
```

This is the dispersive generalization of the one-shell reciprocal theorem and does not assume a common occupation across different energies.

---

# 6. Realistic eight-band HgCdTe closure

A companion audit script exists:

```text
numerics/hgcdte_selectivity_capacity_decomposition.py
```

It loads the authoritative Experiment-12 Kane implementation rather than duplicating the Hamiltonian.

For the broad `Eg..0.5 eV` window, the current audit gives approximately

```text
eta_F                         ~= 0.31
production-capacity factor    ~= 0.57
observable active tightness   ~= 0.176
```

with the independently established Experiment-12 headline values remaining

```text
reference cross-mu population ~= 1.005e17 cm^-3
v_B^cap                       ~= 1.018e6 m/s
lower bound                   ~= 1.18e16 cm^-3
bound/reference               ~= 0.118
bound/active                  ~= 0.176
```

Important result:

```math
\boxed{S_a^{act}=1}
```

to numerical precision for all thermally important contributing active exact-shell blocks in the present eight-band audit.

Therefore HgCdTe's ~17.6% active tightness is **not** weakened by local coherence concentration. It is explained primarily by shell-capacity variation (~0.57) and Fermi/Kubo asymmetry (~0.31).

These decomposition factors are audit-level until the stable-rank script is rerun with the complete production convergence protocol. Do not freeze extra significant figures yet.

---

# 7. New Experiment-03/13 result — conservative recycling readout boundary

For independent Poisson primary lineages with complete random multichannel waveform `H_a(omega)`,

```math
\boxed{
S_y(\omega)
=\sum_a\Lambda_aE[H_aH_a^\dagger].
}
```

Hence terminal cross-spectrum is complete-lineage waveform overlap.

Under the ideal final-sink assumptions

```text
Poisson primary generation;
independent noninteracting lineages;
one final sink per lineage;
final-sink-only measurement;
no branching/gain;
no common electronics,
```

conservative recycling can coexist with exactly zero interterminal endpoint-counting cross-spectrum.

For a finite-transit electron-hole pair, Shockley–Ramo gives

```math
\boxed{
i_k(t)
=e\frac{d}{dt}
[\phi_k(r_e)-\phi_k(r_h)].
}
```

If the pair is created internally at one point and later recombines internally at a common point,

```math
\boxed{Q_k^{rec}=0}
```

for every electrode, while

```math
\boxed{
H_k^{rec}(\omega)
=i\omega e\int\Delta\phi_k(t)e^{-i\omega t}dt
}
```

has

```math
H_k^{rec}(0)=0
```

but can have finite-frequency support.

Therefore finite-transit Ramo readout **permits** a conservative recycling lineage erased by endpoint counting to acquire multichannel AC support. A nonzero ensemble cross-spectrum is not guaranteed; symmetry, opposing lineage classes, weighting fields, or electronics can still cancel it.

Focused prior-art searches have found established Ramo GR-noise theory and established HgCdTe photon-recycling/crosstalk modeling, but no direct collision yet with this conservative-lineage endpoint-versus-finite-transit boundary. Novelty remains plausible, not certified.

---

# 8. Manuscript state

### Rev0

`PAPER_DRAFT_REV0_2026-08-15.md`

Hostile review found:

```text
one blocking Kubo convention regression;
stable-rank scope compression;
generic response selectivity over-described as quantum rejection;
sigma_cross experimental interpretation too broad;
Ramo finite-frequency visibility phrased too deterministically.
```

No central theorem failed.

### Rev1

`PAPER_DRAFT_REV1_2026-08-15.md`

Rev1 fixes those issues:

```text
authoritative Experiment-12 conductivity convention restored;
staged maps introduced;
uniform-shell hypotheses attached to the simple reciprocity;
generic S_resp separated from Experiment-09 quantum rejection;
Experiment-01 witness separated from equal-trace theorem;
sigma_cross explicitly described as selected/decomposed response;
HgCdTe factors marked audit-level;
endpoint Poisson hypotheses explicit;
finite-frequency Ramo result reduced from guaranteed visibility to permitted visibility.
```

---

# 9. Prior-art disposition

Generic ingredients are established and must not be claimed as new:

```text
Gram/positive operators;
stable rank and singular-value inequalities;
task/Fisher information operators;
POVM coherence sensitivity;
bright/dark optical states;
Shockley-Ramo detector response;
Poisson shot-noise / marking / thinning;
HgCdTe photon recycling and mean crosstalk;
optical sum-rule / geometric-bound neighborhoods.
```

Candidate new content is narrowly:

```text
1. detector-specific reciprocal relation between response selectivity and state-count capacity tightness;
2. its dispersive thermal decomposition and realistic HgCdTe diagnosis;
3. quantitative fixed-trace task penalty tied to the same selectivity;
4. conservative photon-recycling endpoint-counting invisibility versus finite-transit Ramo AC reopening;
5. the causal closure of these independently derived photodetector results into one staged spectral argument.
```

No direct prior-art collision has yet been found for the combined statements. Absence of a search hit is not proof of novelty.

---

# 10. Strategic disposition

```text
SCIENTIFIC UNITY:                     PASS
UNIFIED REV1:                         ACTIVE
CENTRAL EXPERIMENT-12 THEOREM:        PASS
NEW SELECTIVITY/COUNT DUALITY:        PASS
DISPERSIVE DECOMPOSITION:             PASS
HgCdTe AUDIT CLOSURE:                 PASS, production rerun pending
FINITE-TRANSIT RAMO RESULT:           PASS mathematically, novelty still under audit
STANDALONE PAPERS 01/09/12:           RETAIN
SUPERSEDING FLAGSHIP DECISION:        NOT YET
```

## Immediate next actions

1. Perform hostile referee review of **Rev1 itself**, not just the architecture or Rev0.
2. Run the stable-rank HgCdTe companion at production convergence settings and compare against the controlling Experiment-12 continuous ordinary supremum.
3. Deepen prior-art audit specifically around finite-transit GR/Ramo cross-noise and conservative photon-recycling lineages.
4. Import and verify the complete reference networks from Experiments 01, 09, and 12.
5. Only if Rev1 survives those gates should a journal target, typeset source, figures, or standalone-paper supersession be considered.
