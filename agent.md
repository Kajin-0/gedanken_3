# Agent recovery entrypoint

Read `AGENTS.md` first, then this file. Do not infer research chronology from `main` alone.

## Hard global constraint — ANALYTICAL / THEORETICAL ONLY

The project goal is a defensible theoretical photodetector paper grown from a simple Gedanken experiment. Do not open a new experiment while the current paper path remains scientifically alive.

Active work may use first-principles derivation, exact toy models, analytical bounds/no-go results, numerical thought experiments, adversarial primary-literature audits, and theoretical manuscript development. Do not make laboratory work the next step.

Preserve failed/corrected paths and do not use novelty/priority language without a dedicated audit.

---

# ACTIVE FRONTIER — Experiment 09 PRA Rev. 8

Branch:

```text
experiment-09-coherence-selective-photodetection
```

Active title:

> **Scaling of internal false-event susceptibility in a coherence-selective photodetector**

First target:

```text
Physical Review A — Regular Article
suggested section: A-3E Quantum Technologies
```

## Read in this order

1. `experiments/09-coherence-selective-photodetection/CURRENT_STATE.md`
2. `experiments/09-coherence-selective-photodetection/PAPER_REV8_PRODUCTION_AND_REVIEW_RESPONSE_2026-08-14.md`
3. `experiments/09-coherence-selective-photodetection/numerics/paper_rev8_fig1.py`
4. `experiments/09-coherence-selective-photodetection/PAPER_DRAFT_REV5_PRA_2026-08-14.md` — last full repository manuscript before Rev. 6–8 production corrections
5. `experiments/09-coherence-selective-photodetection/PAPER_REV4_EXTERNAL_REFEREE_RESPONSE_2026-08-14.md`
6. `experiments/09-coherence-selective-photodetection/COLLECTIVE_EXTRACTION_RATE_BOUND_2026-08-14.md`
7. `experiments/09-coherence-selective-photodetection/SATURATING_SITE_ROBUSTNESS_2026-08-14.md`
8. older revisions only as correction history.

**Do not resume from Rev. 4's fixed finite-`d` low-density asymptotic.** The paper's primary asymptotic object is now the dilute susceptibility.

---

# Exact model

Bright state:

```math
|B\rangle=N^{-1/2}\sum_j|j\rangle.
```

Counted sink `|c>` and local projectors `P_j=|j><j|`.

```math
\dot\varrho
=\kappa_N\mathcal D[|c\rangle\langle B|]\varrho
+\gamma_N\sum_j\mathcal D[P_j]\varrho.
```

Projected exact closure:

```math
\dot P=-\kappa_Nb,
```

```math
\dot b=-(\kappa_N+\gamma_N)b+\frac{\gamma_N}{N}P.
```

Emergent slow eigenvalue:

```math
r_{-,N}
=\frac1N\frac{\kappa_N\gamma_N}{\kappa_N+\gamma_N}[1+O(N^{-1})].
```

`r_-` is an eigenmode, not a microscopic return jump.

---

# Primary observable

For target conditional internal efficiency `eta`:

```math
T_N(\eta)=\inf\{t:C_{S,N}(t)\ge\eta\}.
```

Primary dilute local-generation susceptibility:

```math
\boxed{
\chi_N(\eta)
=N\int_0^{T_N(\eta)}C_{loc,N}(u)du
=\lim_{d\to0}\frac{\mu_{loc,N}(\eta;d)}d.
}
```

For a dilute independent Poisson realization only:

```math
\mu=d\chi_N,
\qquad
P_{FA}=d\chi_N+O(d^2).
```

Do not turn this conditional finite-rate map into a universal dark-count-rate theorem.

---

# Rate-scaling theorem

```math
\kappa_N=\kappa_0N^\alpha,
\qquad
\gamma_N=\gamma_0N^\beta,
\qquad
\kappa_0,\gamma_0>0.
```

`alpha,beta` are fixed `N`-independent exponents.

```math
\boxed{
\begin{array}{c|c|c|c}
\text{sector} & \text{efficiency} & T_N & \chi_N\\
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

A fresh exact-kernel recheck did not find a mathematical failure in this table.

---

# Bounded extraction resource and headline result

For

```math
K=\sum_a|\ell_a\rangle\langle\ell_a|\ge0,
```

with bounded per-state counted coupling `K_jj<=kappa_loc`,

```math
\kappa(\psi)\le\lambda_{max}(K)\le\operatorname{Tr}K\le N\kappa_{loc},
```

hence

```math
\boxed{\alpha\le1}
```

within the **linear single-excitation resource class**.

For any **fixed** target efficiency strictly in a slow-recycling sector,

```math
\boxed{\chi_N=\Omega(N).}
```

Bounded-response efficiency supremum:

```math
\boxed{
\eta_{sc}=\begin{cases}
1,&\alpha>\beta,\\
\kappa_0/(\kappa_0+\gamma_0),&\alpha=\beta,\\
0,&\alpha<\beta.
\end{cases}}
```

This is a nondivergence criterion, not an operational false-count budget.

---

# One-event-per-site source saturation

```math
\mu_{1,N}(T)=N\int_0^T d e^{-ds}C_{loc,N}(T-s)ds.
```

On fixed strict slow branches, existing lower bound gives `Omega(N)`. Rev. 8 now states the matching upper bound explicitly: at most `N` sites, at most one event/site, and `0<=C_loc,N<=1`, therefore `mu_1,N<=N`.

Hence

```math
\boxed{\mu_{1,N}(T_N)=\Theta(N).}
```

This is robustness to **local source saturation**, not arbitrary many-body detector saturation.

---

# Rev. 8 production corrections — do not regress

## Title/abstract

Current title uses **false-event susceptibility**, not `false-count limits`.

The abstract explicitly states that:

- finite-rate `mu=d chi` is conditional;
- same-mode optical background is outside the theorem;
- bright-aligned correlated internal sources are outside the theorem.

## Figure 1

Rev. 8 Fig. 1 is the clean baseline. It has two sparse panels:

```text
(a) State flow
signal -> bright -> counted sink
local event -> 1/N bright + (1-1/N) dark
local dephasing gamma_N in a dedicated lane
slow r_-^{-1} in isolated note box

(b) Operating definition
eta -> T_N(eta) -> chi_N(eta)
```

No long equation is embedded in the figure. Do not reintroduce labels on top of arrows.

## Figure 2

The actual figure parameters are

```text
kappa_0=10
gamma_0=1
q_0=10/11 ~= 0.909
```

so `eta=.50` is genuinely subcritical and has slope 0. Rev. 8 discloses these parameters in the figure and caption.

Exact fitted slopes over `N=10^3..10^4`:

```text
-1.00017
+0.000034
+1.99994
+0.99994
```

for the four displayed cases respectively.

---

# Illustrative physical anchor

Pisani et al. 2023 supplies a concrete collective intersubband-polarization/electronic-extractor architecture, but not an `N`-series that determines the paper's exponents.

Analytical benchmark only:

```text
N equivalent extraction amplitudes add coherently
-> matrix element ~ sqrt(N)
-> kappa_N ~ N
-> alpha ~ 1

microscopic scattering remains N-independent
-> gamma_N ~ N^0
-> beta ~ 0
```

This idealized mapping lies in the extraction-dominated sector. If dephasing also scales like `N`, it lies on the balanced line. Do not assign these exponents to the Pisani device without a microscopic derivation.

---

# Claim boundaries

Must remain explicit:

- signal efficiency is conditional internal collection, not end-to-end QE;
- theorem concerns independent local internal generation;
- same-mode optical background is not rejected;
- bright-aligned correlated generation can bypass local rejection;
- gate starts with no residual internal excitation;
- finite-rate mapping requires a kinetic assumption;
- exact permutation symmetry is a model assumption;
- no material realization is claimed;
- novelty is **NOT ESTABLISHED**.

---

# Render state

Rev. 8:

```text
REVTeX/PRA compile: PASS
pages: 9
citations/cross-references: PASS
overfull boxes: NONE
underfull boxes: NONE
vector figures: PASS
page-level visual QA: PASS
PDF preflight: PASS
PDF SHA-256:
  8fde6c8a2780d64178de6be7b500701d926b6c86aded79f7ff5c950c79ae47e4
TeX SHA-256:
  149223d538321236781106a80ccf485dcc69d1ee61c9deffcd41a55886ef76d9
author/affiliation submission metadata: OPEN
novelty: NOT ESTABLISHED
```

---

# NEXT ACTION

Do **not** open Experiment 10.

Next: one fresh hostile review of the actual Rev. 8 rendered paper, focused on **PRA significance/generalizability**. Open heterogeneity theory only if exact symmetry is identified as a real publication blocker. Otherwise proceed to author metadata, final citation-network audit, and submission production.
