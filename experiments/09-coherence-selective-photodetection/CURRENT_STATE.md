# Current State — Experiment 09: Coherence-Selective Photodetection

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** **ACTIVE PAPER / PRA REV. 5 MAJOR REVISION / FIXED-d LOW-DENSITY OBJECTION REPAIRED / RENDERED AND QA'D / NOVELTY NOT ESTABLISHED**

## Read next

1. `PAPER_DRAFT_REV5_PRA_2026-08-14.md` — active scientific manuscript source
2. `PAPER_REV4_EXTERNAL_REFEREE_RESPONSE_2026-08-14.md` — external major-review objections and Rev. 5 disposition
3. `PAPER_REV5_PRA_RENDER_QA_2026-08-14.md` — current 9-page REVTeX render QA
4. `numerics/paper_rev5_figures.py` — current publication-figure generator
5. `SCALABLE_EFFICIENCY_CEILING_2026-08-14.md` — pre-Rev.5 headline theorem history
6. `RATE_SCALING_PHASE_DIAGRAM_2026-08-14.md` — full earlier asymptotic derivation history
7. `COLLECTIVE_EXTRACTION_RATE_BOUND_2026-08-14.md` — bounded-local-coupling proof
8. `GATED_REVERSE_INJECTION_PHASE_LAW_2026-08-14.md` — supporting thermodynamic result
9. `PAPER_REV4_REFERENCE_AUDIT_2026-08-14.md` — verified working bibliography
10. earlier Rev. 0–4 manuscripts/referee reports only as correction history.

Do **not** resume from Rev. 4's fixed-per-site-rate `d` asymptotic as the active theorem. It was superseded by the external hostile review.

---

# Active paper

> **Scalable internal false-count limits in a coherence-selective photodetector**

Current first target:

```text
Physical Review A — Regular Article
suggested section: A-3E Quantum Technologies
```

Rev. 5 has been rendered locally as a nine-page two-column REVTeX/PRA manuscript. The current render passes PDF preflight, citation/cross-reference checks, and page-level visual QA. Author/affiliation metadata remain placeholders.

---

# Why Rev. 5 exists

The external hostile referee review independently found no obvious algebraic defect in the core one-excitation dynamics, eigenvalues, asymptotic sectors, bounded-coupling proof, or reverse-count scaling. Its blocking objection was instead asymptotic self-consistency:

```text
fixed per-site generation d
+ slow gate/lifetime growing with N
-> the old model can leave a literal low-density regime as N->infinity.
```

That objection is accepted. Rev. 5 changes the primary observable rather than merely adding a caveat.

---

# Exact Lindblad model

Use the symmetric bright state

```math
|B\rangle=\frac1{\sqrt N}\sum_j|j\rangle
```

and counted sink `|c>`. With

```math
\mathcal D[L]\rho
=L\rho L^\dagger-\frac12\{L^\dagger L,\rho\},
```

the enlarged completely positive dynamics is

```math
\boxed{
\dot\varrho
=\kappa_N\mathcal D[|c\rangle\langle B|]\varrho
+\gamma_N\sum_j\mathcal D[|j\rangle\langle j|]\varrho.
}
```

Projecting onto the surviving excitation manifold gives

```math
\dot\rho
=-\frac{\kappa_N}{2}\{|B\rangle\langle B|,\rho\}
+\gamma_N\sum_j\mathcal D[|j\rangle\langle j|]\rho.
```

Define

```math
P=\operatorname{Tr}\rho,
\qquad
b=\langle B|\rho|B\rangle.
```

Exactly,

```math
\boxed{\dot P=-\kappa_Nb,}
```

```math
\boxed{
\dot b
=-(\kappa_N+\gamma_N)b
+\frac{\gamma_N}{N}P.
}
```

Hence

```math
\ddot P
+(\kappa_N+\gamma_N)\dot P
+\frac{\kappa_N\gamma_N}{N}P=0.
```

The exact rates are

```math
r_{\pm,N}
=\frac{a_N\pm\sqrt{a_N^2-4\kappa_N\gamma_N/N}}2,
\qquad
a_N=\kappa_N+\gamma_N,
```

and the emergent slow eigenvalue is

```math
\boxed{
r_{-,N}
=\frac1N
\frac{\kappa_N\gamma_N}{\kappa_N+\gamma_N}
[1+O(N^{-1})].
}
```

`r_-` is an effective collective eigenmode, **not** a primitive microscopic dark-to-bright jump.

For every nonzero `gamma_N`, both a bright excitation and a local excitation are eventually counted. The detector resource is therefore the temporal separation between the fast bright process and slow recycling.

---

# Primary Rev. 5 observable — dilute accepted-event susceptibility

Let

```math
C_{S,N}(t)
```

be the collection kernel for an initially bright photon-created excitation and

```math
C_{loc,N}(t)
```

for a uniformly local internally generated event.

For required conditional internal collection efficiency `0<eta<1`, choose

```math
\boxed{
T_N(\eta)
=\inf\{t:C_{S,N}(t)\ge\eta\}.
}
```

The primary internally generated false-event observable is

```math
\boxed{
\chi_N(\eta)
=N\int_0^{T_N(\eta)}C_{loc,N}(u)\,du
=\lim_{d\to0}\frac{\mu_{loc,N}(\eta;d)}d.
}
```

This order of limits is the central Rev. 5 repair.

A finite-rate unsaturable independent-particle Poisson model gives

```math
\mu_{loc,N}(\eta;d)=d\chi_N(\eta),
```

but this is now a **secondary conditional realization**. Do not call fixed `d` plus arbitrary `N->infinity` a uniformly valid low-density physical limit.

---

# General rate-scaling classification

Let

```math
\kappa_N=\kappa_0N^\alpha,
\qquad
\gamma_N=\gamma_0N^\beta.
```

Then the active asymptotic classification is

```math
\boxed{
\begin{array}{c|c|c|c}
\text{rate sector} & \text{efficiency} & T_N & \chi_N\\
\hline
\alpha>\beta & \eta<1 & N^{-\alpha} & N^{-\alpha}\\
\alpha=\beta=s & \eta<q_0 & N^{-s} & N^{-s}\\
\alpha=\beta=s & \eta=q_0 & N^{-s}\ln N & N^{-s}(\ln N)^2\\
\alpha=\beta=s & \eta>q_0 & N^{1-s} & N^{2-s}\\
\alpha<\beta & \eta>0 & N^{1-\alpha} & N^{2-\alpha}
\end{array}}
```

where

```math
q_0=\frac{\kappa_0}{\kappa_0+\gamma_0}.
```

Rev. 5 explicitly derives the leading collection kernels in each branch rather than only tabulating these powers.

## Extraction-dominated branch

With `v=kappa_N t` and `x_eta=-ln(1-eta)`,

```math
C_{S,N}\to1-e^{-v},
```

```math
NC_{loc,N}\to1-e^{-v},
```

so

```math
T_N\sim\frac{x_\eta}{\kappa_0}N^{-\alpha},
```

```math
\chi_N\sim\frac{x_\eta-\eta}{\kappa_0}N^{-\alpha}.
```

## Dephasing-dominated branch

With `z=kappa_N t/N`,

```math
C_{S,N}\to1-e^{-z},
\qquad
C_{loc,N}\to1-e^{-z},
```

so

```math
T_N\sim\frac{x_\eta}{\kappa_0}N^{1-\alpha},
```

```math
\chi_N\sim\frac{x_\eta-\eta}{\kappa_0}N^{2-\alpha}.
```

## Balanced branch

For `alpha=beta=s`, define

```math
A=\kappa_0+\gamma_0,
\qquad
q_0=\kappa_0/A,
\qquad
\lambda_0=\kappa_0\gamma_0/A.
```

Fast branch `eta<q0`:

```math
C_{S,N}\to q_0(1-e^{-v}),
```

```math
NC_{loc,N}
\to q_0^2(1-e^{-v})+q_0(1-q_0)v,
\qquad
v=AN^st.
```

Slow branch `eta>q0`, on `t=N^(1-s)y`:

```math
C_{S,N}\to1-(1-q_0)e^{-\lambda_0y},
```

```math
C_{loc,N}\to1-e^{-\lambda_0y}.
```

At `eta=q0`, the fast deficit balances the incipient slow contribution:

```math
v e^v\sim\frac{N}{(1-q_0)^2},
```

which produces

```math
T_N=\Theta(N^{-s}\ln N),
```

```math
\chi_N=\Theta[N^{-s}(\ln N)^2].
```

---

# Bounded microscopic counted-coupling resource

For arbitrary linear counted sink channels, define

```math
K=\sum_a|\ell_a\rangle\langle\ell_a|\ge0.
```

If each microscopic state has an `N`-independent counted-coupling budget

```math
K_{jj}\le\kappa_{loc},
```

then

```math
\boxed{
\kappa(\psi)
\le\lambda_{max}(K)
\le\operatorname{Tr}K
\le N\kappa_{loc}.
}
```

Hence

```math
\boxed{\alpha\le1}
```

**within the linear single-excitation resource class**.

This scope qualifier belongs to the theorem itself.

---

# Headline theorem — bounded-response efficiency supremum

Assume useful extraction does not weaken with size,

```math
0\le\alpha\le1.
```

Define

```math
\boxed{
\eta_{sc}
=\sup\{\eta\in(0,1):\chi_N(\eta)=O(1)\}.
}
```

Then

```math
\boxed{
\eta_{sc}
=\begin{cases}
1,&\alpha>\beta,\\[4pt]
\dfrac{\kappa_0}{\kappa_0+\gamma_0},&\alpha=\beta,\\[10pt]
0,&\alpha<\beta.
\end{cases}}
```

Interpretation:

```text
alpha > beta:
    every fixed eta<1 has bounded dilute response;

alpha = beta:
    the supremum equals the fast branching fraction q0;

alpha < beta:
    no fixed positive eta has bounded dilute response.
```

Important precision:

```text
s=0 and eta=q0:
    q0 is a supremum but is NOT attained,
    because chi_N(q0)=Theta[(ln N)^2].

s>0 and eta=q0:
    the boundary itself is bounded because
    N^(-s)(ln N)^2 -> 0.
```

`O(1)` means **nondivergent with system size**, not automatically an acceptably small false-count probability.

A budgeted interpretation may be written

```math
\eta_{bud}(d,\mu_*)
=\sup\left\{\eta:
\limsup_{N\to\infty}d\chi_N(\eta)\le\mu_*
\right\}
```

within the range where the linear-response mapping is physically appropriate. Rev. 5 defines but does not optimize this quantity.

---

# Robust slow-branch no-go

Within the **linear single-excitation resource class**,

```math
\boxed{
\text{strict slow-recycling operation}
\Longrightarrow
\chi_N=\Omega(N).
}
```

The detailed `N^(2-alpha)` susceptibility powers describe the dilute linear response. Their physical finite-rate translation need not survive saturation.

To stress the no-go, impose an extreme one-event-per-site-per-gate model:

```math
\mu_{1,N}(T)
=N\int_0^T d e^{-ds}C_{loc,N}(T-s)ds.
```

Then

```math
\mu_{1,N}(T_N)
\ge
N(1-e^{-dT_N/2})C_{loc,N}(T_N/2).
```

On every strict slow branch in the bounded-coupling class, the two factors multiplying `N` remain bounded away from zero asymptotically, so

```math
\boxed{
\mu_{1,N}(T_N)=\Theta(N).
}
```

Thus:

```text
N^(2-alpha) finite-rate powers: MODEL-DEPENDENT.
Strict slow-branch divergence: SURVIVES MAXIMAL PER-SITE SATURATION.
```

---

# Supporting thermodynamic result

The reversible counted-extraction result remains valid only under its assumed effective local-detailed-balance model and is now supporting material, not a coequal novelty claim.

At the same efficiency-selected gate, fixed effective affinity gives

```text
fast branch:          O(1)
balanced boundary:    O(log N)
strict slow branch:   O(N)
```

for the reverse contribution.

---

# Figure / terminology state

Rev. 5 reserves `dark manifold` for the state-space sector and calls noise-origin events `local internal events` or `false events`.

Current figures:

```text
Fig. 1 — mechanism and two clocks;
         gamma_N is microscopic dephasing;
         r_- is explicitly an effective slow eigenmode;
         local event shows bright weight 1/N and dark weight 1-1/N.

Fig. 2 — exact finite-N chi_N approaching asymptotic scaling classes;
         consistency illustration, not independent validation.

Fig. 3 — scaling classification diagram for eta_sc.
```

---

# Prior-art boundary

Mandatory comparators remain:

```text
Young/Sarovar/Léonard 2018 — coherence/backaction detector framework;
Young/Sarovar/Léonard 2020 — coherent collective detector architecture and dark-to-active isolation condition;
Shammah et al. 2017 — local-dephasing bright/dark mixing;
Pisani et al. 2023 — collective quantum IR detector extraction;
Bassler/Lyne/Cuerda 2026 — collective/decoherence large-N scaling;
Schwarzhans et al. 2026 — quantum-detector thermodynamic performance tradeoffs.
```

These eliminate broad novelty claims.

The current narrow claim is the efficiency-selected internally generated response theorem under imperfect dark-state isolation and bounded microscopic extraction resource.

Focused audits have not found a direct stronger match, but **novelty is not established**.

---

# Current rendered manuscript status

```text
PRA Rev. 5 source: ACTIVE
REVTeX two-column compile: PASS
PDF pages: 9
PDF SHA-256:
  bb41ad84b0904a9d126c9150a784effed0a9a77875f8358f4f03b7867df0bb7a
citations/cross-references: PASS
figures: PASS CURRENT VISUAL QA
PDF preflight: PASS
author metadata: OPEN
novelty: NOT ESTABLISHED
```

See `PAPER_REV5_PRA_RENDER_QA_2026-08-14.md`.

---

# Next gate

Do **not** open Experiment 10.

The fixed-`d`/low-density objection is now closed by reformulation.

The next useful action is one fresh **extreme hostile review of Rev. 5**, focused on the strongest remaining scientific risk:

> Is the bounded-response theorem too dependent on exact permutation symmetry, or can the main no-go survive a controlled class of bounded heterogeneity in optical coupling, local dephasing, local event rates, or a finite-rank bright subspace?

Only open more theory if that review identifies a concrete blocking defect. Otherwise proceed toward final author metadata, final citation-network audit, and PRA submission production.
