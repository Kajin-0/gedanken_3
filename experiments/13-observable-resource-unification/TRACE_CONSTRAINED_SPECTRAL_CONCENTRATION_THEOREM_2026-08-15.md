# Experiment 13 — trace-constrained spectral concentration theorem

**Date:** 2026-08-15  
**Scope:** finite-dimensional positive detector coupling operator; exact  
**Status:** **DERIVED / CONNECTS EXPERIMENTS 01, 09, AND 12 IN ONE THEOREM / GENERIC MATRIX INGREDIENTS OLD / DETECTOR-SPECIFIC SYNTHESIS NOVELTY NOT YET CERTIFIED**

## 1. Purpose

The first Experiment-13 master pairing

```math
q_G(\rho)=Tr(G\rho),
\qquad G\succeq0
```

was too generic to be a publishable theorem by itself.

The later selectivity/state-count theorem connected Experiments 09 and 12 through stable rank.

This note adds Experiment 01 to the same exact structure by imposing a physically meaningful comparison: **fixed total coupling/information strength**

```math
T=Tr G.
```

At fixed `T`, spectral concentration cannot improve every task. It redistributes sensitivity from some directions into others. The same concentration simultaneously:

```text
creates task-dependent detector ordering;
increases bright-state/coherence selectivity;
reduces total-state-count identifiability;
and, at rank deficiency, creates exactly invisible internal directions.
```

The stable rank quantifies the trade.

---

# 2. Setup

Let `G` be a positive semidefinite detector information/coupling operator on a `d`-dimensional task subspace:

```math
G\succeq0.
```

Let its eigenvalues be

```math
\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_d\ge0.
```

Define

```math
T=TrG=\sum_{j=1}^d\lambda_j,
```

```math
\bar\lambda=T/d,
```

and, for `T>0`,

```math
r_{st}=T/\lambda_1.
```

The isotropic comparator with the same total strength is

```math
\boxed{
G_{iso}=\bar\lambda I_d
=\frac{T}{d}I_d.
}
```

For a normalized pure task/state `|s>`, define performance

```math
q_G(s)=\langle s|G|s\rangle.
```

---

# 3. Maximum task advantage equals the coherence-selectivity factor

The best-aligned task is the top eigenvector `|1>`:

```math
q_G^{max}=\lambda_1.
```

The isotropic comparator gives the same response to every normalized task:

```math
q_{iso}=T/d.
```

Therefore the maximum task advantage of `G` over the equal-trace isotropic comparator is

```math
\boxed{
\mathcal A_{max}
=\frac{\lambda_1}{T/d}
=\frac{d}{r_{st}}.
}
```

But `d/r_st` is exactly the uniform-incoherent coherent-selectivity factor derived in the selectivity/state-count theorem:

```math
\boxed{
\mathcal S_D=\frac{d}{r_{st}}.
}
```

Hence

```math
\boxed{
\mathcal A_{max}=\mathcal S_D.
}
```

The factor by which a detector can favor its brightest coherent direction over an incoherent uniform ensemble is exactly the factor by which it can outperform an equal-total-strength isotropic detector on its best task.

---

# 4. Exact reciprocal state-count relation

The same coupling operator used as a per-state capacity has total-parent state-count tightness

```math
\tau_{count}=r_{st}/d.
```

Therefore

```math
\boxed{
\mathcal A_{max}
=\mathcal S_D
=\frac1{\tau_{count}}.
}
```

Equivalently,

```math
\boxed{
\mathcal A_{max}\,\tau_{count}=1.
}
```

This is the three-way Experiment-01 / Experiment-09 / Experiment-12 closure at the capacity step:

```text
best-task enhancement
=
coherent bright-state selectivity
=
reciprocal total-state-count tightness.
```

The physical meanings are different, but the controlling spectral concentration is identical.

---

# 5. Any nontrivial concentration necessarily loses on another task

Define the difference from the equal-trace isotropic comparator:

```math
\Delta G=G-G_{iso}.
```

Then

```math
Tr(\Delta G)=0.
```

If `G != G_iso`, then `Delta G` is a nonzero Hermitian trace-zero operator.

A nonzero Hermitian trace-zero operator cannot be positive semidefinite or negative semidefinite. Therefore it has at least one positive and at least one negative eigenvalue.

Hence there exist normalized tasks `|s_+>` and `|s_->` such that

```math
\boxed{
\langle s_+|G|s_+\rangle
>
\langle s_+|G_{iso}|s_+\rangle,
}
```

while

```math
\boxed{
\langle s_-|G|s_-\rangle
<
\langle s_-|G_{iso}|s_-\rangle.
}
```

Thus:

> At fixed total quadratic sensitivity, every non-isotropic detector improvement is necessarily task selective.

There is no way to concentrate a fixed trace into a preferred signal direction without sacrificing another direction.

This is the clean operator form of the Experiment-01 ordering principle.

---

# 6. Stronger two-detector reversal theorem at equal trace

Let two detector operators `G_A` and `G_B` act on the same `d`-dimensional task space and satisfy

```math
TrG_A=TrG_B.
```

If

```math
G_A\ne G_B,
```

then

```math
\Delta=G_A-G_B
```

is nonzero, Hermitian, and trace zero.

Therefore `Delta` is indefinite and there exist normalized tasks `s_A,s_B` with

```math
\boxed{
q_A(s_A)>q_B(s_A),
}
```

and

```math
\boxed{
q_A(s_B)<q_B(s_B).
}
```

So equal total operator strength plus unequal spectral/task geometry **forces task-order reversal**.

This is stronger than merely saying a scalar can fail to predict a task. Under trace matching, reversal is unavoidable unless the two information operators are actually identical.

Experiment 01 uses a physically specific detector/time-search construction rather than `TrG` as its conventional scalar metric, so this theorem does not replace its hard-window result. It supplies the exact geometric skeleton underneath it.

---

# 7. Rank deficiency: the observability boundary

If

```math
rank(G)<d,
```

then there exists a nonzero `|z>` in the null space with

```math
\boxed{q_G(z)=0.}
```

Thus rank deficiency creates an exactly invisible direction.

At fixed nonzero trace, rank deficiency also implies

```math
r_{st}<d,
```

and hence

```math
\mathcal A_{max}=\mathcal S_D>1.
```

The same spectral concentration that creates a strong bright direction can therefore create dark/invisible directions.

This is the static analogue of the Experiment-03 lineage/readout result, where the endpoint-counting map has zero support for a source-terminal contribution of a lineage that ultimately exits through another terminal.

Finite-transit Shockley–Ramo readout changes the measurement map and can lift that zero at finite frequency without changing the internal recycling process.

---

# 8. Three regimes

The theorem organizes detector coupling geometry into three clean regimes.

## Regime I — isotropic complete

```math
G=(T/d)I.
```

Then

```text
r_st=d;
A_max=1;
S_D=1;
tau_count=1;
no null directions;
no task preference.
```

One scalar `T/d` is complete on the chosen task subspace.

## Regime II — anisotropic full rank

```math
rank(G)=d,
\qquad
G\ne(T/d)I.
```

Then

```text
1< A_max=S_D < d;
tau_count<1;
no exactly invisible direction;
task ordering is selective.
```

## Regime III — rank deficient

```math
rank(G)<d.
```

Then

```text
A_max=S_D>1;
tau_count<1;
exact null/invisible directions exist.
```

The rank-one limit gives

```math
A_max=S_D=d,
\qquad
tau_count=1/d.
```

---

# 9. Add Experiment-12 thermal asymmetry

The observable Experiment-12 theorem has an independent Fermi/Kubo efficiency

```math
0\le\eta_F\le1.
```

Therefore its full total-population tightness is

```math
\tau_{obs}
=\eta_F\tau_{count}.
```

The three-way relation becomes

```math
\boxed{
\mathcal A_{max}
=\mathcal S_D
=\frac{\eta_F}{\tau_{obs}}.
}
```

or

```math
\boxed{
\mathcal A_{max}\tau_{obs}
=\mathcal S_D\tau_{obs}
=\eta_F.
}
```

Thus thermal electron/hole asymmetry is a separate multiplicative source of inverse-bound slack, not part of the optical singular-spectrum trade itself.

---

# 10. Connection to the dispersive HgCdTe result

The exact-shell HgCdTe audit found

```text
S_a^act=1
```

for all thermally important selected active shell blocks in the current eight-band model.

Locally, those blocks sit in Regime I on their active supports: there is no coherence-selectivity / task-concentration penalty inside the shell.

The realistic global bound is nevertheless loose because:

```text
shell capacities vary relative to the global supremum;
and eta_F<1.
```

This is important: the theorem does not force every real material toward a coherence-selective regime. It identifies exactly which spectral resource is responsible when such selectivity exists.

---

# 11. Connection to Experiment 09

The uniform bright-state selector has

```math
G=|B\rangle\langle B|,
\qquad
T=1,
\qquad
r_{st}=1,
\qquad
d=N.
```

Thus it is the maximally concentrated Regime-III endpoint:

```math
\boxed{
\mathcal A_{max}=\mathcal S_D=N,
\qquad
\tau_{count}=1/N.
}
```

Its `N-1` orthogonal combinations are exactly dark to the ideal bright selector.

---

# 12. Connection to Experiment 01

For Gaussian linear detection, Experiment 01's task-information operator can be written

```math
G_D
=H_D^\dagger P^\dagger N_D^{-1}PH_D.
```

Known-waveform matched-filter SNR is

```math
SNR_D^2(s)=\langle s|G_D|s\rangle.
```

The theorem here says that, after matching a total-strength normalization such as `TrG`, any difference in `G_D` necessarily produces tasks with opposite orderings.

Experiment 01 goes further by constructing a specific physically meaningful pair of detectors and an unknown-arrival-time task where the reversal is driven by finite-time information/search geometry. That physical construction remains independently valuable.

---

# 13. Connection to Experiment 03

At any frequency, a linear stochastic readout has a transfer map

```math
M_y(\omega)
```

from elementary innovations/lineages to measured terminals, with spectral matrix

```math
S_y=M_y\Sigma M_y^\dagger.
```

After whitening the innovation covariance, the corresponding Gram geometry is again positive.

Endpoint counting can project a conservative lineage onto only its final terminal, producing exact zeros in other channel components.

Finite-transit Ramo motion changes the map `M_y(omega)` and can make those formerly null components nonzero at finite frequency.

Thus Experiment 03 is the dynamic/output-side realization of the same principle:

```text
what is invisible is determined by the null geometry of the measurement map,
not solely by whether the internal process exists.
```

---

# 14. What is and is not new

The mathematical statements used here are elementary or standard:

```text
trace-zero Hermitian matrices are indefinite unless zero;
Rayleigh quotient extrema are eigenvalues;
stable rank is TrG/lambda_max;
rank deficiency creates a null space.
```

No novelty claim should be attached to those facts.

The candidate scientific contribution is the detector-specific closure:

> under a common coupling/information operator, fixed total response can be concentrated only by becoming task selective; the exact concentration factor is simultaneously the coherent bright-state advantage and the reciprocal optical state-count identifiability, while nullity controls complete invisibility and thermal Fermi asymmetry enters as an independent multiplicative factor.

This unifies the physical conclusions of Experiments 01, 09, 12, and—through the dynamic measurement map—03 without asserting that generic matrix theory is new.

---

# 15. Manuscript consequence

Experiment 13 now has three layers of nontrivial content:

```text
A. trace-constrained detector spectral-concentration closure;
B. coherence-selectivity / Experiment-12 state-count reciprocity;
C. conservative-recycling endpoint cancellation versus finite-frequency Ramo reopening.
```

The first is mostly a synthesis theorem; B and C were not present in the source papers before Experiment 13.

This is enough to justify constructing a **manuscript architecture** for hostile review, but not enough to withdraw or merge the existing Experiment-01, -09, or -12 manuscripts.

The manuscript should be killed if its central scientific message reduces, after hostile review, to the generic phrase "measurement operators matter."
