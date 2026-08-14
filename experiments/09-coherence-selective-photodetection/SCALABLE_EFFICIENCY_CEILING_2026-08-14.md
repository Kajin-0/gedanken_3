# Experiment 09 — Scalable efficiency ceiling under bounded local coupling

**Date:** 2026-08-14  
**Status:** COMPACT DETECTOR COROLLARY OF RATE PHASE DIAGRAM + EXTRACTION RATE BOUND / NOVELTY NOT ESTABLISHED

## Definition

Let `mu_N(eta)` be the accepted internally generated local-event burden at the minimum gate required to reach fixed conditional internal collection efficiency `eta`.

Call a fixed efficiency target **locally scalable** if

```math
\mu_N(\eta)=O(1)
\qquad(N\to\infty).
```

Assume:

1. `kappa_N=kappa_0 N^alpha`, `gamma_N=gamma_0 N^beta`;
2. the counted extractor is linear and single-excitation Markovian;
3. each microscopic state has an `N`-independent counted-coupling budget, so `alpha<=1`;
4. useful extraction does not weaken with size, `alpha>=0`;
5. per-site local dark-generation rate `d` remains fixed.

Define the **scalable efficiency ceiling** as the supremum of fixed efficiency targets with bounded local-dark burden:

```math
\boxed{
\eta_{sc}
=\sup\{\eta\in(0,1):\mu_N(\eta)=O(1)\}.
}
```

---

# Result

From the rate-scaling phase diagram and the extraction-rate bound,

```math
\boxed{
\eta_{sc}
=
\begin{cases}
1, & \alpha>\beta,\\[4pt]
\dfrac{\kappa_0}{\kappa_0+\gamma_0}, & \alpha=\beta,\\[10pt]
0, & \alpha<\beta.
\end{cases}}
```

This is a supremum statement. Exact attainability of the balanced boundary depends on the common rate exponent and on whether thermally reversed extraction is included.

---

# 1. Extraction outruns dephasing: alpha > beta

Here

```math
q_N\to1.
```

Every fixed target `eta<1` eventually lies on the fast branch. Since

```math
\mu_N(\eta)\asymp N^{-\alpha}
```

with `alpha>=0`, all fixed `eta<1` have bounded accepted local-dark burden.

Therefore

```math
\boxed{\eta_{sc}=1.}
```

The value `1` is a supremum: perfect collection generally requires an infinite gate in the ideal exponential model, but any fixed efficiency below unity remains scalable.

---

# 2. Extraction and dephasing scale together: alpha = beta = s

The fast branching fraction approaches

```math
q_0=\frac{\kappa_0}{\kappa_0+\gamma_0}.
```

For `eta<q_0`,

```math
\mu_N\asymp N^{-s},
```

which is bounded for `s>=0`.

For every fixed `eta>q_0`,

```math
\mu_N\asymp N^{2-s}.
```

The bounded-local-coupling result gives `s<=1`, hence

```math
2-s>=1
```

and every strict supercritical target has a divergent accepted local-dark burden.

Thus

```math
\boxed{\eta_{sc}=q_0.}
```

### Boundary attainability

At `eta=q_0`,

```math
\mu_N\asymp N^{-s}(\ln N)^2.
```

Therefore:

```text
s=0:
    local-dark burden diverges logarithmically squared;
    q0 is a supremum but is not attained by a bounded local burden.

0<s<=1:
    local-dark burden tends to zero;
    the local-dark criterion permits eta=q0 itself.
```

If a thermally reversed counted extractor with fixed affinity is included, its critical contribution grows as `ln N`, so a bounded **total** dark burden again requires operating strictly below `q0` unless an additional affinity of order `kT ln ln N` is supplied.

---

# 3. Dephasing outruns extraction: alpha < beta

Every fixed positive `eta` eventually requires slow recycling and

```math
\mu_N(\eta)\asymp N^{2-\alpha}.
```

Because `alpha<=1`,

```math
\mu_N(\eta)=\Omega(N)
```

for every fixed `eta>0`.

Therefore

```math
\boxed{\eta_{sc}=0.}
```

No nonzero fixed internal collection efficiency can retain a bounded accepted local-dark burden in this asymptotic resource class.

---

# 4. Interpretation

Under a bounded microscopic counted-coupling resource, the large-`N` detector has a simple scalable-efficiency classification:

```text
extraction scales faster than dephasing:
    any fixed efficiency below unity can remain scalable;

extraction and dephasing scale equally:
    the scalable ceiling is the fast branching fraction q0;

dephasing scales faster than extraction:
    no fixed positive efficiency can remain scalable.
```

The detailed power laws in `RATE_SCALING_PHASE_DIAGRAM_2026-08-14.md` refine this ceiling, but the ceiling is the simplest detector-facing summary.

---

# 5. Why this is stronger than kappa >> gamma

A finite-device heuristic such as

```math
\kappa\gg\gamma
```

does not determine scalability.

The asymptotic question depends on how the two rates change with `N`:

```math
\kappa_N/\gamma_N
=\frac{\kappa_0}{\gamma_0}N^{\alpha-\beta}.
```

A detector with mediocre finite-`N` ratio can become asymptotically extraction-dominated if `alpha>beta`, while a detector with favorable finite-`N` ratio eventually fails if `alpha<beta`.

The relevant scaling resource is therefore the exponent difference `alpha-beta` together with the bounded-local-coupling ceiling `alpha<=1`.

---

# 6. Scope

This ceiling concerns the independent internally generated local-event burden. Same-mode photon background is not rejected.

The result also depends on:

- fixed per-site local dark-generation rate;
- the independent-particle stochastic lift;
- bounded counted coupling per microscopic state;
- fixed efficiency targets independent of `N`;
- Markovian symmetric extraction/dephasing dynamics.

It is not a universal quantum-detector theorem.

---

# 7. Manuscript consequence

This ceiling may be a better headline result than the raw five-row phase table because it states an operational detector limit in one equation:

```math
\eta_{sc}
=
\begin{cases}
1,&\alpha>\beta,\\
\kappa_0/(\kappa_0+\gamma_0),&\alpha=\beta,\\
0,&\alpha<\beta.
\end{cases}
```

The full phase diagram then provides the approach to and failure beyond that ceiling.
