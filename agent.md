# Agent recovery entrypoint

Read `AGENTS.md` first, then this file. Do not infer research chronology from `main` alone.

## Hard global constraint — ANALYTICAL / THEORETICAL ONLY

The project goal is a defensible theoretical photodetector paper grown from a simple Gedanken experiment. Do not open a new experiment while the current paper path remains scientifically alive.

Active work may use first-principles derivation, exact toy models, analytical bounds/no-go results, numerical thought experiments, adversarial primary-literature audits, and theoretical manuscript development. Do not make laboratory work the next step.

Preserve failed/corrected paths and do not use novelty/priority language without a dedicated audit.

---

# ACTIVE FRONTIER — Experiment 09 rendered paper candidate

Branch:

```text
experiment-09-coherence-selective-photodetection
```

Active manuscript:

> **Scalable internal-dark-count limits in a coherence-selective photodetector**

Current first target:

```text
Physical Review A — Regular Article
suggested section: A-3E Quantum Technologies
```

Active journal-facing source text:

`experiments/09-coherence-selective-photodetection/PAPER_DRAFT_REV4_PRA_2026-08-14.md`

Rendered-production record:

`experiments/09-coherence-selective-photodetection/PAPER_REV4_PRA_RENDER_QA_2026-08-14.md`

Rev. 4 has been rendered locally as a seven-page two-column REVTeX/PRA PDF with resolved citations/references and three QA'd figures. Author metadata are intentionally still placeholders.

## Read in this order

1. `experiments/09-coherence-selective-photodetection/CURRENT_STATE.md`
2. `experiments/09-coherence-selective-photodetection/PAPER_DRAFT_REV4_PRA_2026-08-14.md`
3. `experiments/09-coherence-selective-photodetection/PAPER_REV4_PRA_RENDER_QA_2026-08-14.md`
4. `experiments/09-coherence-selective-photodetection/PAPER_REV4_REFERENCE_AUDIT_2026-08-14.md`
5. `experiments/09-coherence-selective-photodetection/PAPER_REV3_JOURNAL_STRATEGY_2026-08-14.md`
6. `experiments/09-coherence-selective-photodetection/PAPER_REV3_SIGNIFICANCE_REVIEW_2026-08-14.md`
7. `experiments/09-coherence-selective-photodetection/SCALABLE_EFFICIENCY_CEILING_2026-08-14.md`
8. `experiments/09-coherence-selective-photodetection/RATE_SCALING_PHASE_DIAGRAM_2026-08-14.md`
9. `experiments/09-coherence-selective-photodetection/COLLECTIVE_EXTRACTION_RATE_BOUND_2026-08-14.md`
10. `experiments/09-coherence-selective-photodetection/GATED_REVERSE_INJECTION_PHASE_LAW_2026-08-14.md`
11. figure and numerical scripts under `experiments/09-coherence-selective-photodetection/numerics/`.

Earlier Rev. 0–3 manuscripts/reviews are correction history, not the active starting point.

---

# Central model

Photon-created bright state:

```math
|B\rangle=N^{-1/2}\sum_j|j\rangle.
```

Internally generated events are local and incoherent. Static `1/N` bright projection is established geometry, not a novelty claim.

With bright extraction `kappa_N` and local pure dephasing `gamma_N`:

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

The slow recycling rate is

```math
r_{-,N}
=\frac1N\frac{\kappa_N\gamma_N}{\kappa_N+\gamma_N}
[1+O(N^{-1})].
```

---

# Counting-model scope — DO NOT REGRESS

Continuous local generation uses an explicit low-density independent-particle lift:

```text
N local sites;
Poisson generation rate d per site;
generated excitations distinguishable and noninteracting;
each follows an independent copy of the one-body kernel.
```

Then

```math
\mu_{loc,N}(T)=Nd\int_0^T C_{D,N}(u)du.
```

Signal efficiency is **conditional internal collection after bright-state preparation**, not end-to-end photon QE.

For fixed target `eta`:

```math
T_N(\eta)=\inf\{t:C_{S,N}(t)\ge\eta\},
```

```math
\mu_{loc,N}(\eta)=Nd\int_0^{T_N(\eta)}C_{D,N}(u)du.
```

Same-mode photon background is not rejected.

---

# Rate-scaling classification

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
\text{sector} & \text{efficiency} & T_N & \mu_{loc,N}\\
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
q_0=\kappa_0/(\kappa_0+\gamma_0).
```

This is detector-operational scaling, not a claim of a new generic decoherence phase transition.

---

# Bounded local coupling theorem

For positive extraction matrix

```math
K=\sum_a|\ell_a\rangle\langle\ell_a|,
```

and bounded local counted coupling `K_jj<=kappa_loc`,

```math
\boxed{
\kappa_B\le\lambda_{max}(K)\le\operatorname{Tr}K\le N\kappa_{loc}.
}
```

Hence `alpha<=1` in this resource class.

Any operating point strictly requiring slow dark-manifold recycling has

```math
\boxed{\mu_{loc,N}=\Omega(N).}
```

---

# ACTIVE HEADLINE THEOREM

Assume useful extraction does not weaken with size, `0<=alpha<=1`. Define

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

This is the Rev. 4 paper centerpiece.

---

# Corrected gated reverse floor

For a reversible counted transition

```math
\bar\kappa_N=\kappa_Ne^{-\Delta F_N/(kT)},
```

at the same efficiency-selected gate

```math
\mu_{rev,N}=\bar\kappa_N\int_0^{T_N}C_{S,N}(u)du.
```

At fixed affinity:

```text
fast branch:          O(1)
balanced boundary:    O(log N)
strict slow branch:   O(N)
```

The old blanket `kT ln C` gated interpretation is superseded.

---

# Closest prior-art boundary

Mandatory central comparators:

- Young/Sarovar/Léonard 2018 — quantum coherence/backaction detector framework;
- Young/Sarovar/Léonard 2020 — closest coherent detector architecture and dark-to-active isolation condition;
- Shammah et al. 2017 — local-dephasing bright/dark scattering;
- Pisani et al. 2023 — collective quantum infrared detector extraction;
- Bassler/Lyne/Cuerda 2026 — collective/decoherence large-N scaling regimes;
- Schwarzhans et al. 2026 — quantum-detector thermodynamic tradeoffs.

These eliminate broad novelty claims.

Focused audits have not found a direct statement of the complete Rev. 4 theorem, but **novelty remains unestablished**.

---

# Render state

`PAPER_REV4_PRA_RENDER_QA_2026-08-14.md` records:

```text
REVTeX/PRA compile: PASS
pages: 7
citations/cross-references: PASS
figures: PASS
visual QA: PASS
PDF preflight: PASS
author metadata: OPEN
novelty: NOT ESTABLISHED
```

The three final figure layouts are generated by `numerics/paper_rev3_figures.py` and have passed two visual correction cycles.

---

# NEXT ACTION

Do **not** open Experiment 10.

Perform one final extreme adversarial review of the **rendered Rev. 4 PDF**. If it finds no new scientific defect, freeze the theorem and move to author metadata plus actual PRA submission production. Further theory should be opened only to repair a concrete reviewer defect, not to expand the paper for its own sake.
