# Current State — Experiment 09: Coherence-Selective Photodetection

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** **ACTIVE CONCISE PAPER CANDIDATE / REV. 3 BUILT AROUND SCALABLE-EFFICIENCY LIMIT / THREE HOSTILE REVIEW ROUNDS COMPLETED / NOVELTY NOT ESTABLISHED**

## Read next

1. `PAPER_DRAFT_REV3_2026-08-14.md`
2. `PAPER_REV2_HOSTILE_REFEREE_REVIEW_2026-08-14.md`
3. `SCALABLE_EFFICIENCY_CEILING_2026-08-14.md`
4. `RATE_SCALING_PHASE_DIAGRAM_2026-08-14.md`
5. `COLLECTIVE_EXTRACTION_RATE_BOUND_2026-08-14.md`
6. `GATED_REVERSE_INJECTION_PHASE_LAW_2026-08-14.md`
7. `RATE_SCALING_PRIOR_ART_ADDENDUM_2026-08-14.md`
8. `PAPER_REV1_HOSTILE_REFEREE_REVIEW_2026-08-14.md`
9. `EFFICIENCY_SCALABILITY_TRANSITION_2026-08-14.md`
10. numerical checks in `numerics/`.

Do not resume from Rev. 0 or Rev. 1 as the active paper. Their failed/conditional results remain part of the correction history.

---

# 1. Established architecture / exact claim boundary

A photon prepares one collective bright excitation

```math
|B\rangle=\frac1{\sqrt N}\sum_j|j\rangle,
```

while independent internal dark events are created locally. Static `1/N` rejection of a uniform incoherent excitation by the bright projector is **standard coherent-mode/state-verification geometry** and is not claimed as new.

Young, Sarovar, and Leonard already establish coherently interacting nanoscale detector elements and high-efficiency/low-dark detector design. Their 2020 ideal-efficiency conditions explicitly require relaxation not to couple dark states back to the optically active manifold.

Experiment 09's narrow question is:

> What scalability penalty follows when that dark-to-bright isolation is violated by local dephasing, the detector gate is selected by a required internal collection efficiency, and the number of internal local dark-generation sites grows?

Same-mode optical background is not rejected and is outside the claim.

---

# 2. Exact one-body kernel

With bright extraction `kappa_N` and local pure dephasing `gamma_N`, define surviving excitation probability `P` and bright population `b`:

```math
\dot P=-\kappa_Nb,
```

```math
\dot b=-(\kappa_N+\gamma_N)b+\frac{\gamma_N}{N}P.
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
a_N=\kappa_N+\gamma_N.
```

The slow recycling rate is

```math
r_{-,N}
=\frac1N
\frac{\kappa_N\gamma_N}{\kappa_N+\gamma_N}
[1+O(N^{-1})].
```

For every nonzero dephasing rate, both bright and local excitations are eventually counted. The discrimination is finite-time.

---

# 3. Counting-model repair remains mandatory

Continuous local generation is not claimed to follow directly from a strict one-excitation Hilbert space.

Use the explicit independent-particle stochastic lift:

```text
N local sites;
independent Poisson generation rate d per site;
generated excitations distinguishable and noninteracting;
each excitation follows an independent copy of the exact one-body kernel.
```

Then

```math
\mu_{loc,N}(T)
=Nd\int_0^T C_{D,N}(u)du.
```

Signal performance is **conditional internal collection after bright-state preparation**, not end-to-end photon QE.

For fixed target `0<eta<1`:

```math
T_N(\eta)=\inf\{t:C_{S,N}(t)\ge\eta\},
```

```math
\mu_{loc,N}(\eta)
=Nd\int_0^{T_N(\eta)}C_{D,N}(u)du.
```

---

# 4. General rate-scaling theorem

Let

```math
\kappa_N=\kappa_0N^\alpha,
\qquad
\gamma_N=\gamma_0N^\beta.
```

The accepted local-dark burden has the asymptotic classification

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

where

```math
q_0=\frac{\kappa_0}{\kappa_0+\gamma_0}.
```

Explicit coefficients are in `RATE_SCALING_PHASE_DIAGRAM_2026-08-14.md`.

This is a **detector-operational scaling classification**, not a claim of a new generic collective/decoherence phase diagram. Bassler, Lyne, and Cuerda 2026 already establish large-`N` collective/decoherence scaling regimes in Dicke superradiance.

---

# 5. Bounded microscopic coupling removes the superlinear escape

For arbitrary linear counted sink channels define the positive extraction matrix

```math
K=\sum_a|\ell_a\rangle\langle\ell_a|.
```

If every local state has bounded counted coupling

```math
K_{jj}\le\kappa_{loc}
```

with `kappa_loc` independent of `N`, then

```math
\boxed{
\kappa_B
\le\lambda_{max}(K)
\le\operatorname{Tr}K
\le N\kappa_{loc}.
}
```

Thus

```math
\boxed{\alpha\le1.}
```

under this resource assumption.

Consequently every operating point strictly requiring slow dark-manifold recycling has

```math
\boxed{
\mu_{loc,N}=\Omega(N).
}
```

The formal `alpha>=2` slow-branch escape is unavailable unless microscopic per-site coupling itself grows with `N` or the model leaves this resource class.

---

# 6. ACTIVE HEADLINE THEOREM — scalable efficiency ceiling

Assume useful extraction does not weaken with size,

```math
0\le\alpha\le1.
```

Define

```math
\eta_{sc}
=\sup\{\eta\in(0,1):\mu_{loc,N}(\eta)=O(1)\}.
```

Then

```math
\boxed{
\eta_{sc}
=
\begin{cases}
1,&\alpha>\beta,\\[4pt]
\dfrac{\kappa_0}{\kappa_0+\gamma_0},&\alpha=\beta,\\[10pt]
0,&\alpha<\beta.
\end{cases}}
```

Interpretation:

```text
extraction scales faster than dephasing:
    any fixed eta<1 can remain locally scalable;

balanced extraction/dephasing scaling:
    scalable ceiling is the fast branching fraction q0;

dephasing scales faster than extraction:
    no nonzero fixed eta has bounded local-dark burden.
```

This is the active Rev. 3 centerpiece.

---

# 7. Corrected gated thermodynamic result

The old blanket interpretation

```text
collective forward enhancement C
-> kT ln C extra affinity required for bounded gated reverse dark counts
```

was too strong because it ignored gate shortening.

For a reversible counted transition

```math
\bar\kappa_N
=\kappa_Ne^{-\Delta F_N/(kT)},
```

the efficiency-selected reverse contribution is

```math
\mu_{rev,N}
=\bar\kappa_N\int_0^{T_N}C_{S,N}(u)du.
```

At fixed affinity:

```math
\boxed{
\mu_{rev,N}\sim
\begin{cases}
O(1), & \text{fast branch},\\
O(\ln N), & \text{balanced boundary},\\
O(N), & \text{strict slow branch}.
\end{cases}}
```

Thus bounded reverse burden requires additional affinity scaling of

```text
fast branch:             O(1)
balanced boundary:       kT ln ln N
strict slow branch:      kT ln N
```

up to additive constants.

For maximally collective favorable scaling `kappa_N~N`, `gamma_N=O(1)`:

```math
\mu_{loc,N}\sim N^{-1},
```

while

```math
\mu_{rev,N}=O(1)
```

at fixed affinity. The reversible extractor becomes the asymptotic floor.

---

# 8. Current manuscript and review history

Active paper:

> **Scalable internal-dark-count limits in a coherence-selective photodetector**

File:

`PAPER_DRAFT_REV3_2026-08-14.md`.

Review history:

```text
Rev. 0:
    FAIL — static 1/N centerpiece too close to standard mode filtering;
    Poisson exactness overstated;
    photon-efficiency wording wrong;
    thermodynamic claim overbroad.

Rev. 1:
    PASS fixed-rate algebra, but FAIL as universal scalability story;
    Young 2020 found as stronger architecture prior art;
    kappa_N scaling required.

Rev. 2:
    PASS general rate-scaling algebra;
    bounded-local-coupling theorem and gated reverse correction added;
    referee recommended compressing around scalable-efficiency ceiling.

Rev. 3:
    ACTIVE concise theory-paper candidate.
```

Do not erase failed drafts; they document the correction path.

---

# 9. Prior-art claim boundary

Mandatory central comparators:

- Young, Sarovar, Leonard 2018: quantum coherence/backaction and detector performance;
- Young, Sarovar, Leonard 2020: coherently interacting detector elements, high efficiency/low dark counts, and dark-to-optically-active isolation condition;
- Shammah et al. 2017: local-dephasing bright/dark transfer;
- Pisani et al. 2023: collective quantum infrared detector polarization feeding electronic extraction;
- Bassler, Lyne, Cuerda 2026: collective/decoherence large-`N` scaling regimes;
- Schwarzhans et al. 2026: thermodynamic efficiency/dark-count/jitter/dead-time tradeoffs.

These eliminate broad novelty claims.

Focused searches have not found a direct statement of the complete detector theorem

```text
prescribed conditional internal collection efficiency
+ extensive local internal generation
+ size-dependent extraction/dephasing
+ bounded microscopic extraction resource
-> scalable efficiency ceiling eta_sc and accepted-event scaling.
```

This is **not proof of novelty**.

---

# 10. Current next gate

Do **not** open Experiment 10.

The next useful work is now manuscript-level:

1. run one fresh significance/novelty review of Rev. 3 as a concise paper;
2. if it survives, generate 2–3 theory figures from exact finite-`N` kernels and asymptotic laws;
3. perform final citation-production audit;
4. choose a realistic journal/format and render the paper.

Current disposition:

```text
Gedanken premise: RETAIN
static 1/N result: SUPPORTING / ESTABLISHED GEOMETRY
one-body kernel: EXACT
count process: EXACT WITHIN EXPLICIT INDEPENDENT-PARTICLE LIFT
rate-scaling classification: RETAIN
bounded-local-coupling alpha<=1: RETAIN
scalable-efficiency ceiling: ACTIVE HEADLINE THEOREM
gated reverse-injection phase law: SUPPORTING RESULT
Rev. 3: ACTIVE
novelty: NOT ESTABLISHED
paper path: ACTIVE
```
