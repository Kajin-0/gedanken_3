# Current State — Experiment 09: Coherence-Selective Photodetection

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** **ACTIVE PAPER / PRA-FACING REV. 4 RENDERED AND QA'D / NO FATAL INTERNAL DEFECT IDENTIFIED / NOVELTY NOT ESTABLISHED**

## Read next

1. `PAPER_DRAFT_REV4_PRA_2026-08-14.md` — active journal-facing scientific text
2. `PAPER_REV4_PRA_RENDER_QA_2026-08-14.md` — final 7-page REVTeX render QA
3. `PAPER_REV4_REFERENCE_AUDIT_2026-08-14.md` — verified working bibliography
4. `PAPER_REV3_JOURNAL_STRATEGY_2026-08-14.md` — PRA Regular Article rationale
5. `PAPER_REV3_SIGNIFICANCE_REVIEW_2026-08-14.md` — gate that authorized manuscript production
6. `SCALABLE_EFFICIENCY_CEILING_2026-08-14.md` — headline theorem
7. `RATE_SCALING_PHASE_DIAGRAM_2026-08-14.md` — full asymptotic classification
8. `COLLECTIVE_EXTRACTION_RATE_BOUND_2026-08-14.md` — bounded-local-coupling proof
9. `GATED_REVERSE_INJECTION_PHASE_LAW_2026-08-14.md` — corrected thermodynamic supporting result
10. `RATE_SCALING_PRIOR_ART_ADDENDUM_2026-08-14.md` — closest current prior-art boundary
11. numerical scripts under `numerics/`.

Earlier Rev. 0–3 manuscripts and referee reports are correction history. Do not resume from their superseded claims.

---

# Active paper

> **Scalable internal-dark-count limits in a coherence-selective photodetector**

Current first target:

```text
Physical Review A — Regular Article
suggested section: A-3E Quantum Technologies
```

The Rev. 4 manuscript has been rendered locally with `revtex4-2` into a seven-page, two-column PRA-style PDF. All citations/cross-references resolve; all three figures pass visual QA; PDF preflight passes. Author name/affiliation remain placeholders.

---

# Minimal model and exact kernel

A photon prepares the symmetric bright state

```math
|B\rangle=\frac1{\sqrt N}\sum_j|j\rangle,
```

while internally generated dark events are local. Static `1/N` rejection of a uniform local event is **established coherent-mode/state-verification geometry**, not the paper novelty claim.

With size-dependent bright extraction `kappa_N` and local pure dephasing `gamma_N`,

```math
\dot P=-\kappa_Nb,
```

```math
\dot b=-(\kappa_N+\gamma_N)b+\frac{\gamma_N}{N}P,
```

so

```math
\ddot P+(\kappa_N+\gamma_N)\dot P
+\frac{\kappa_N\gamma_N}{N}P=0.
```

The slow dark-manifold recycling rate is

```math
r_{-,N}
=\frac1N\frac{\kappa_N\gamma_N}{\kappa_N+\gamma_N}
[1+O(N^{-1})].
```

For nonzero dephasing, both bright and local excitations are eventually counted; the discrimination is finite-time.

---

# Counting model — exact scope

Continuous internal generation is represented by an explicit extensive low-density independent-particle lift:

```text
N local sites;
Poisson generation rate d per site;
generated excitations distinguishable and noninteracting;
each follows an independent copy of the exact one-body kernel.
```

Then

```math
\mu_{loc,N}(T)=Nd\int_0^T C_{D,N}(u)du.
```

Signal efficiency means **conditional internal collection after bright-state preparation**, not end-to-end photon QE.

For fixed target `eta`:

```math
T_N(\eta)=\inf\{t:C_{S,N}(t)\ge\eta\},
```

```math
\mu_{loc,N}(\eta)=Nd\int_0^{T_N(\eta)}C_{D,N}(u)du.
```

Same-mode optical background is not rejected.

---

# General rate-scaling classification

Let

```math
\kappa_N=\kappa_0N^\alpha,
\qquad
\gamma_N=\gamma_0N^\beta.
```

Then

```math
\boxed{
\begin{array}{c|c|c|c}
\text{rate sector} & \text{efficiency} & T_N & \mu_{loc,N}\\
\hline
\alpha>\beta & \eta<1 & N^{-\alpha} & N^{-\alpha}\\
\alpha=\beta=s & \eta<q_0 & N^{-s} & N^{-s}\\
\alpha=\beta=s & \eta=q_0 & N^{-s}\ln N & N^{-s}(\ln N)^2\\
\alpha=\beta=s & \eta>q_0 & N^{1-s} & N^{2-s}\\
\alpha<\beta & \eta>0 & N^{1-\alpha} & N^{2-\alpha}
\end{array}}
```

with

```math
q_0=\frac{\kappa_0}{\kappa_0+\gamma_0}.
```

This is a detector-operational accepted-event scaling classification, **not** a claim of a new generic decoherence phase transition.

---

# Bounded microscopic coupling

For linear counted extraction matrix

```math
K=\sum_a|\ell_a\rangle\langle\ell_a|\ge0,
```

with per-local-state coupling budget

```math
K_{jj}\le\kappa_{loc},
```

```math
\boxed{
\kappa_B\le\lambda_{max}(K)\le\operatorname{Tr}K\le N\kappa_{loc}.
}
```

Hence

```math
\boxed{\alpha\le1.}
```

within this resource class, and any operating point strictly requiring slow dark-manifold recycling has

```math
\boxed{\mu_{loc,N}=\Omega(N).}
```

---

# Headline theorem — scalable internal-efficiency ceiling

Assume useful extraction does not weaken with size,

```math
0\le\alpha\le1.
```

Define

```math
\eta_{sc}=\sup\{\eta\in(0,1):\mu_{loc,N}(\eta)=O(1)\}.
```

Then

```math
\boxed{
\eta_{sc}=
\begin{cases}
1,&\alpha>\beta,\\[4pt]
\dfrac{\kappa_0}{\kappa_0+\gamma_0},&\alpha=\beta,\\[10pt]
0,&\alpha<\beta.
\end{cases}}
```

This is the active paper centerpiece.

---

# Corrected gated reverse-injection floor

For a thermally reversible counted transition

```math
\bar\kappa_N=\kappa_Ne^{-\Delta F_N/(kT)},
```

at the same efficiency-selected gate

```math
\mu_{rev,N}=\bar\kappa_N\int_0^{T_N}C_{S,N}(u)du.
```

At fixed affinity:

```math
\mu_{rev,N}\sim
\begin{cases}
O(1),&\text{fast branch},\\
O(\ln N),&\text{balanced boundary},\\
O(N),&\text{strict slow branch}.
\end{cases}
```

Thus the older blanket `kT ln(C)` interpretation is not the gated detector law.

---

# Closest prior-art boundary

Mandatory comparators:

```text
Young/Sarovar/Leonard 2018 — coherence/backaction detector framework;
Young/Sarovar/Leonard 2020 — closest coherent collective detector architecture and dark-to-active isolation condition;
Shammah et al. 2017 — local-dephasing bright/dark scattering;
Pisani et al. 2023 — collective quantum infrared detector extraction;
Bassler/Lyne/Cuerda 2026 — collective/decoherence large-N scaling regimes;
Schwarzhans et al. 2026 — detector thermodynamic performance tradeoffs.
```

These eliminate broad novelty claims.

Focused searches have not found a direct statement of the complete Rev. 4 detector theorem, but **novelty remains unestablished**.

---

# Rendered manuscript status

Current production checks:

```text
PRA Rev. 4 scientific text: PASS current internal audit
REVTeX two-column compile: PASS
PDF pages: 7
citations/cross-references: PASS
three figures: PASS
page-level visual QA: PASS
PDF preflight: PASS
author metadata: OPEN
novelty: NOT ESTABLISHED
```

The rendered PDF SHA-256 is recorded in `PAPER_REV4_PRA_RENDER_QA_2026-08-14.md`.

---

# Next action

Do **not** open Experiment 10.

The next useful work is one final **adversarial review of the rendered Rev. 4 PDF itself**. If no new scientific defect appears, the remaining tasks are author metadata, final citation-network check immediately before submission, and the actual PRA submission package.
