# Experiment 09 — Collective extraction rate bound with bounded local coupling

**Date:** 2026-08-14  
**Status:** EXACT LINEAR-ALGEBRA BOUND / CLOSES SUPERLINEAR-RATE ESCAPE UNDER STATED RESOURCE ASSUMPTION / GENERIC MATRIX FACT IS NOT A NOVELTY CLAIM

## Question

The general rate-scaling phase diagram permits mathematical cases in which a slow-recycling detector avoids a growing accepted internal-dark burden by making the useful extraction rate scale as `N^2` or faster.

Is that escape available if each microscopic state has a fixed `N`-independent coupling budget to the counted extraction reservoirs?

For a linear Markovian single-excitation extractor, the answer is no.

---

# 1. General counted extraction matrix

Let the local single-excitation manifold be spanned by

```math
|j\rangle,
\qquad j=1,\ldots,N.
```

Allow an arbitrary number of counted sink channels `a`. Write the jump from the excitation manifold to sink channel `a` as

```math
J_a=|c_a\rangle\langle \ell_a|,
```

where `|ell_a>` is an arbitrary vector in the `N`-dimensional excitation manifold.

The total counted extraction operator on the excitation manifold is the positive semidefinite matrix

```math
\boxed{
K=\sum_aJ_a^\dagger J_a
=\sum_a|\ell_a\rangle\langle\ell_a|.
}
```

For a normalized excitation `|psi>`, the instantaneous counted extraction rate is

```math
\boxed{
\kappa(\psi)
=\langle\psi|K|\psi\rangle.
}
```

The largest possible extraction rate over all normalized superpositions is

```math
\kappa_{max}=\lambda_{max}(K).
```

---

# 2. Bounded per-site coupling resource

Define the total counted coupling strength available to local state `|j>` as

```math
K_{jj}
=\sum_a|\langle\ell_a|j\rangle|^2.
```

Assume a microscopic resource bound

```math
\boxed{
K_{jj}\le\kappa_{loc}
\qquad\text{for every }j,
}
```

where `kappa_loc` does not increase with `N`.

Then

```math
\operatorname{Tr}K
=\sum_jK_{jj}
\le N\kappa_{loc}.
```

Since `K` is positive semidefinite,

```math
\lambda_{max}(K)
\le\operatorname{Tr}K.
```

Therefore

```math
\boxed{
\kappa(\psi)
\le\kappa_{max}
\le N\kappa_{loc}
}
```

for every normalized excitation state.

This includes the optically bright state.

---

# 3. Linear collective scaling is the maximum within this resource class

If the bright extraction rate is parameterized as

```math
\kappa_N\sim\kappa_0N^\alpha,
```

then the bounded-local-coupling assumption implies

```math
\boxed{\alpha\le1.}
```

Linear scaling can be saturated. For example, one common counted sink with equal phase-aligned local amplitudes gives a rank-one matrix with diagonal entries `kappa_loc` and bright-state eigenvalue `N kappa_loc`.

Thus the bound does not forbid ordinary Dicke-like collective enhancement; it forbids superlinear extraction-rate scaling unless the microscopic coupling budget per local state itself grows with `N` or the model leaves this linear Markovian resource class.

---

# 4. Consequence for the internal-dark phase diagram

From `RATE_SCALING_PHASE_DIAGRAM_2026-08-14.md`, any strict slow-recycling sector has

```math
\mu_{local,N}\asymp N^{2-\alpha}.
```

Examples are:

```text
alpha<beta for every fixed eta>0;
alpha=beta=s with eta>q0.
```

Under the bounded-local-coupling result `alpha<=1`,

```math
2-\alpha\ge1.
```

Hence

```math
\boxed{
\text{strict slow-recycling operation}
\quad\Longrightarrow\quad
\mu_{local,N}=\Omega(N)
}
```

within the theorem class.

The mathematical `alpha>=2` escape required to keep the slow-branch local-dark burden bounded is unavailable unless the per-site counted coupling resource itself increases with system size.

---

# 5. Fast branch versus slow branch under the resource bound

The result sharpens the detector interpretation.

## Fast branch

When extraction asymptotically wins the branching competition, or on the balanced line when `eta<q0`,

```math
\mu_{local,N}\asymp N^{-\alpha}.
```

With the physically standard range

```math
0\le\alpha\le1,
```

the accepted local-dark burden is bounded or decreases with size.

At the maximal collective rate `alpha=1`,

```math
\mu_{local,N}\sim N^{-1}.
```

## Slow branch

If the required efficiency forces dark-manifold recycling, then under `alpha<=1`

```math
\mu_{local,N}\gtrsim N.
```

Thus bounded per-site coupling creates a sharp qualitative distinction:

```text
fast-branch operation can have nonextensive or decreasing local dark burden;
strict slow-recycling operation cannot have bounded local dark burden.
```

The exact critical balanced boundary `eta=q0` remains a separate logarithmic crossover and is not included in the strict slow-branch statement.

---

# 6. Combined consequence with thermally reversed extraction

For the maximally collective favorable example

```math
\kappa_N\propto N,
\qquad
\gamma_N=O(1),
```

the local internally generated burden scales as

```math
\mu_{local,N}\sim N^{-1}.
```

However, the gated reverse-injection result gives at fixed thermodynamic affinity

```math
\mu_{rev,N}=O(1)
```

on the fast branch.

Therefore the thermally reversed counted transition becomes the asymptotic floor even though it does not diverge with `N`:

```math
\boxed{
\mu_{local,N}\to0,
\qquad
\mu_{rev,N}\to\text{constant}
}
```

in this ideal collective limit.

This is a more detector-relevant resource statement than the earlier fixed-gate claim that reverse counts must scale directly with the collective extraction rate.

---

# 7. Scope

The bound assumes:

- a linear single-excitation Markovian counted extractor;
- positive extraction matrix `K`;
- an `N`-independent upper bound on each local diagonal coupling strength `K_jj`.

It can be evaded if:

- the microscopic coupling strength of each local constituent itself increases with `N`;
- active gain or time-dependent control supplies additional resources;
- many-excitation nonlinearities produce a different scaling object;
- the effective single-excitation Markov description fails.

The matrix inequality itself is elementary and is not a novelty claim. Its purpose is to remove an unphysical-looking superlinear escape from the detector phase diagram under an explicit resource assumption.

---

# 8. Manuscript implication

The strongest physically constrained statement now available is:

> Within a linear single-excitation extractor with bounded counted coupling per microscopic state, collective bright extraction can scale at most linearly with `N`. Consequently, any fixed-efficiency operating point that strictly requires slow dark-manifold recycling incurs at least an `O(N)` accepted local-dark burden, whereas fast-branch operation can remain bounded or improve with size. At maximally collective linear extraction and slower dephasing, the local-dark burden can fall as `1/N`, leaving thermally reversed bright injection as an `O(1)` gated floor at fixed affinity.

This should be used as a physical resource corollary of the general phase diagram, not as a new linear-algebra theorem.
