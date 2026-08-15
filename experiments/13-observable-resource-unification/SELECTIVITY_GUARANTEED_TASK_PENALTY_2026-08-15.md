# Experiment 13 — selectivity forces a quantitative task penalty

**Date:** 2026-08-15  
**Status:** EXACT COROLLARY / STRENGTHENS EXPERIMENT-01 CONNECTION

## 1. Setup

Use the trace-constrained detector operator

```math
G\succeq0,
\qquad
TrG=T,
```

on a `d`-dimensional task space. Let

```math
\lambda_1\ge\cdots\ge\lambda_d\ge0.
```

The equal-total-strength isotropic comparator is

```math
G_{iso}=(T/d)I.
```

Define the peak bright/task enhancement

```math
\boxed{
\mathcal S
=\frac{\lambda_1}{T/d}
=\frac{d\lambda_1}{T}.
}
```

This is the same uniform-incoherent coherence-selectivity factor derived in the stable-rank theorem.

Because `lambda_1<=T`,

```math
1\le\mathcal S\le d.
```

---

## 2. Remaining spectral budget

The total eigenvalue weight outside the brightest direction is

```math
\sum_{j=2}^d\lambda_j
=T-\lambda_1
=T\left(1-\frac{\mathcal S}{d}\right).
```

Therefore the average response of the remaining `d-1` eigen-directions is

```math
\bar\lambda_\perp
=\frac{T-\lambda_1}{d-1}
=\frac{T}{d}
\frac{d-\mathcal S}{d-1}.
```

At least one orthogonal eigen-direction must have response no larger than that average. Hence

```math
\boxed{
\lambda_d
\le
\frac{T}{d}
\frac{d-\mathcal S}{d-1}.
}
```

Relative to the isotropic comparator,

```math
\boxed{
\frac{q_{worst}}{q_{iso}}
\le
\frac{d-\mathcal S}{d-1}.
}
```

---

# 3. Guaranteed loss

Define the fractional degradation relative to the isotropic comparator on the guaranteed weak task as

```math
\mathcal L
=1-\frac{q_{worst}}{q_{iso}}.
```

Then

```math
\boxed{
\mathcal L
\ge
\frac{\mathcal S-1}{d-1}.
}
```

Thus any coherence/task selectivity above unity forces a minimum loss somewhere else in task space under fixed total strength.

Examples:

```text
S=1:
    no forced loss; isotropic limit.

S=d:
    loss >=1;
    at least one orthogonal direction is exactly invisible.

S=(d+1)/2:
    loss >=1/2;
    at least one task has at most half the isotropic response.
```

---

# 4. Express the task penalty in terms of state-count tightness

The selectivity/state-count reciprocity gives

```math
\mathcal S=1/\tau_{count}.
```

Therefore

```math
\boxed{
\frac{q_{worst}}{q_{iso}}
\le
\frac{d-1/\tau_{count}}{d-1},
}
```

and

```math
\boxed{
\mathcal L
\ge
\frac{1/\tau_{count}-1}{d-1}.
}
```

This turns the Experiment-12 inverse-identification slack into a guaranteed task-anisotropy statement when the same coupling operator and total-strength normalization apply.

Conversely, a detector whose state-count capacity bound is nearly tight (`tau_count≈1`) cannot possess a large bright-state/task advantage over the isotropic comparator on that same subspace.

---

# 5. Relation to Experiment 01

Experiment 01 established by explicit detector/time-search construction that equal conventional `D*` does not guarantee equal task performance and that detector ordering can reverse.

The present theorem addresses a different but complementary question:

> if a detector's total quadratic information strength is held fixed, how much task loss is mathematically forced by a specified bright/coherent selectivity advantage?

The answer is quantitative:

```math
\boxed{
S>1
\quad\Longrightarrow\quad
\exists\,s_\perp:
\frac{q_G(s_\perp)}{q_{iso}}
\le\frac{d-S}{d-1}.
}
```

Thus the Experiment-09 coherence advantage and Experiment-01 task reversal are not merely both consequences of "anisotropy." The magnitude of one constrains the unavoidable degradation of the other under a fixed total resource.

---

# 6. Tightness

The bound is tight.

Choose spectrum

```math
\lambda_1=\frac{ST}{d},
```

and distribute the remaining trace uniformly:

```math
\lambda_2=\cdots=\lambda_d
=\frac{T}{d}\frac{d-S}{d-1}.
```

Then every orthogonal eigen-direction attains the bound exactly.

Hence no stronger universal worst-task guarantee can be obtained from `d`, `T`, and `S` alone.

---

# 7. Novelty boundary

The eigenvalue averaging argument is elementary. Do not claim the inequality as new matrix theory.

Its value in Experiment 13 is the detector-specific chain

```text
coherence selectivity S
-> fixed-trace spectral concentration
-> guaranteed task penalty
-> reciprocal state-count tightness.
```

This makes the unified manuscript less vulnerable to the objection that the Experiment-01 connection is only rhetorical.
