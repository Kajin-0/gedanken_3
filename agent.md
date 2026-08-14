# Agent recovery entrypoint

Read `AGENTS.md` first, then this file. Do not infer research chronology from `main` alone.

## Hard global constraint — ANALYTICAL / THEORETICAL ONLY

The user cannot perform real-life experiments. Active work is restricted to first-principles derivation, exact toy models, analytical bounds/invariants/no-go theorems, numerical thought experiments, adversarial primary-literature audits, and theoretical manuscript development.

Do not make fabrication, sample procurement, measurement pilots, instrumentation, annealing, device processing, or laboratory optimization the next step.

Preserve negative results. Do not use `novel`, `first`, `fundamental`, or priority language without a dedicated audit.

---

# ACTIVE FRONTIER — Experiment 09: Coherence-Selective Photodetection

Branch:

```text
experiment-09-coherence-selective-photodetection
```

Experiment 09 is now an **active concise theory-paper candidate**. Do not open Experiment 10 while Rev. 3 remains scientifically alive.

## Active manuscript

> **Scalable internal-dark-count limits in a coherence-selective photodetector**

File:

`experiments/09-coherence-selective-photodetection/PAPER_DRAFT_REV3_2026-08-14.md`

## Read in this order

1. `experiments/09-coherence-selective-photodetection/CURRENT_STATE.md`
2. `experiments/09-coherence-selective-photodetection/PAPER_DRAFT_REV3_2026-08-14.md`
3. `experiments/09-coherence-selective-photodetection/PAPER_REV2_HOSTILE_REFEREE_REVIEW_2026-08-14.md`
4. `experiments/09-coherence-selective-photodetection/SCALABLE_EFFICIENCY_CEILING_2026-08-14.md`
5. `experiments/09-coherence-selective-photodetection/RATE_SCALING_PHASE_DIAGRAM_2026-08-14.md`
6. `experiments/09-coherence-selective-photodetection/COLLECTIVE_EXTRACTION_RATE_BOUND_2026-08-14.md`
7. `experiments/09-coherence-selective-photodetection/GATED_REVERSE_INJECTION_PHASE_LAW_2026-08-14.md`
8. `experiments/09-coherence-selective-photodetection/RATE_SCALING_PRIOR_ART_ADDENDUM_2026-08-14.md`
9. numerical scripts under `experiments/09-coherence-selective-photodetection/numerics/`.

Earlier Rev. 0–2 manuscripts and referee reports are correction history, not the active starting point.

---

# Minimal Gedanken premise

A photon prepares one collective bright excitation across `N` local states,

```math
|B\rangle=\frac1{\sqrt N}\sum_j|j\rangle,
```

while internal dark events are generated locally and incoherently.

Static bright projection gives `1/N` acceptance of a uniform local event. **This is established coherent-mode/state-verification geometry and is not the paper novelty claim.**

The closest coherent detector precedent is Young, Sarovar, and Leonard, ACS Photonics 7, 821–830 (2020). Their ideal-efficiency conditions explicitly require relaxation not to couple dark states back to the optically active manifold.

Experiment 09 asks what scalability penalty follows when this isolation is violated by local dephasing while the number of internally dark-generating sites grows.

Same-mode optical background is not rejected.

---

# Exact one-body kernel

With size-dependent bright extraction `kappa_N` and local pure dephasing `gamma_N`:

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

For nonzero dephasing, local and bright excitations are eventually counted; rejection is finite-time.

---

# Counting model — DO NOT REGRESS

The one-body kernel does not by itself imply an exact finite-rate many-event Poisson process.

Use the explicit independent-particle stochastic lift:

```text
N local sites;
Poisson generation rate d per site;
generated excitations distinguishable and noninteracting;
each follows an independent copy of the one-body quantum kernel.
```

Then

```math
\mu_{loc,N}(T)
=Nd\int_0^T C_{D,N}(u)du.
```

Signal efficiency means **conditional internal collection after bright-state preparation**:

```math
\eta_{int,N}(T)=C_{S,N}(T).
```

Do not call it end-to-end photon QE.

For fixed target `eta`:

```math
T_N(\eta)=\inf\{t:C_{S,N}(t)\ge\eta\},
```

```math
\mu_{loc,N}(\eta)
=Nd\int_0^{T_N(\eta)}C_{D,N}(u)du.
```

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

Explicit coefficients are in `RATE_SCALING_PHASE_DIAGRAM_2026-08-14.md`.

Do not call this a new generic decoherence phase diagram. Bassler, Lyne, and Cuerda 2026 already develop collective/decoherence large-`N` scaling regimes in Dicke superradiance.

---

# Bounded local extraction resource

For arbitrary linear counted sinks define

```math
K=\sum_a|\ell_a\rangle\langle\ell_a|\ge0.
```

If each local state has bounded counted coupling

```math
K_{jj}\le\kappa_{loc},
```

then

```math
\boxed{
\kappa_B
\le\lambda_{max}(K)
\le\operatorname{Tr}K
\le N\kappa_{loc}.
}
```

Therefore

```math
\boxed{\alpha\le1.}
```

within this linear single-excitation resource class.

Any operating point strictly requiring slow dark-manifold recycling then incurs

```math
\boxed{\mu_{loc,N}=\Omega(N).}
```

The formal `alpha>=2` slow-branch escape is unavailable unless per-site coupling itself grows with `N` or the model changes.

---

# ACTIVE HEADLINE THEOREM — scalable efficiency ceiling

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

This is the Rev. 3 paper centerpiece.

Interpretation:

```text
extraction scaling wins:
    any fixed efficiency below unity can retain bounded local-dark burden;

balanced extraction/dephasing scaling:
    ceiling equals fast branching fraction q0;

dephasing scaling wins:
    no nonzero fixed efficiency retains bounded local-dark burden.
```

---

# Corrected gated reverse-injection result

For a thermally reversible counted transition

```math
\bar\kappa_N
=\kappa_Ne^{-\Delta F_N/(kT)},
```

the accepted reverse contribution at the same efficiency-selected gate is

```math
\mu_{rev,N}
=\bar\kappa_N\int_0^{T_N}C_{S,N}(u)du.
```

At fixed affinity:

```math
\boxed{
\mu_{rev,N}\sim
\begin{cases}
O(1),&\text{fast branch},\\
O(\ln N),&\text{balanced boundary},\\
O(N),&\text{strict slow branch}.
\end{cases}}
```

Thus extra affinity required for bounded gated reverse burden is:

```text
fast branch:          O(1)
balanced boundary:    kT ln ln N
strict slow branch:   kT ln N
```

The older blanket `kT ln mathcal C` interpretation was a fixed-rate-coefficient statement and must not be presented as the detector's gated dark-count law.

At favorable maximal collective scaling `kappa_N~N`, `gamma_N=O(1)`:

```math
\mu_{loc,N}\sim N^{-1},
\qquad
\mu_{rev,N}=O(1)
```

at fixed affinity. The reversible extractor becomes the asymptotic floor.

---

# Prior-art claim boundary

Mandatory central comparators:

- Young, Sarovar, Leonard 2018 — quantum coherence/backaction detector metrics;
- Young, Sarovar, Leonard 2020 — coherently interacting nanoscale detector elements and dark-to-optically-active isolation condition;
- Shammah et al. 2017 — local-dephasing bright/dark scattering;
- Pisani et al. 2023 — collective quantum infrared detector polarization feeding electronic extraction;
- Bassler, Lyne, Cuerda 2026 — collective/decoherence large-`N` scaling regimes;
- Schwarzhans et al. 2026 — thermodynamic detector performance tradeoffs.

These kill broad novelty claims.

The focused audit has not found a direct statement of the complete detector theorem

```text
prescribed conditional internal efficiency
+ extensive local internal generation
+ size-dependent extraction/dephasing
+ bounded per-site extraction resource
-> scalable efficiency ceiling and accepted-event scaling.
```

This remains **novelty not established**.

---

# Review history

```text
Rev. 0:
    FAILED — static mode-projection centerpiece, counting-model exactness, and scope errors.

Rev. 1:
    fixed-rate three-regime theorem survived;
    failed as universal scalability story;
    Young 2020 identified as closer prior art;
    rate scaling required.

Rev. 2:
    general alpha/beta rate classification survived;
    bounded-local-coupling theorem and gated thermodynamic correction added;
    referee requested compression around detector-facing efficiency ceiling.

Rev. 3:
    ACTIVE concise theory-paper candidate.
```

Preserve all failures.

---

# Next action

Do **not** open Experiment 10.

1. run one final significance/novelty review of Rev. 3 as a concise theory paper;
2. if it survives, generate 2–3 theory figures from exact finite-`N` kernels and asymptotic laws;
3. perform citation-production audit;
4. select a realistic journal/format and render a submission-quality manuscript.

The project goal is now the paper, not more numbered Gedanken experiments.
