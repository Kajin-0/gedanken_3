# Current State — Experiment 09: Coherence-Selective Photodetection

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** **ACTIVE PAPER / PRA REV. 8 / THEOREM INTACT / FIGURE AND REPRODUCIBILITY REPAIRS COMPLETE / NOVELTY NOT ESTABLISHED**

## Read next

1. `PAPER_REV8_PRODUCTION_AND_REVIEW_RESPONSE_2026-08-14.md` — current Rev. 8 production/reviewer disposition
2. `numerics/paper_rev8_fig1.py` — current clean Fig. 1 generator
3. `PAPER_DRAFT_REV5_PRA_2026-08-14.md` — last full repository manuscript text before Rev. 6–8 production corrections
4. `PAPER_REV4_EXTERNAL_REFEREE_RESPONSE_2026-08-14.md` — fixed-`d` asymptotic objection that forced the susceptibility reformulation
5. `PAPER_REV5_PRA_RENDER_QA_2026-08-14.md` — earlier Rev. 5 render record
6. `COLLECTIVE_EXTRACTION_RATE_BOUND_2026-08-14.md` — bounded-local-coupling theorem
7. `SATURATING_SITE_ROBUSTNESS_2026-08-14.md` — one-event-per-site robustness history
8. earlier manuscript/review files only as correction history.

Do **not** resume from Rev. 4's fixed-per-site-rate large-`N` low-density formulation.

---

# Active paper

> **Scaling of internal false-event susceptibility in a coherence-selective photodetector**

First target remains:

```text
Physical Review A — Regular Article
suggested section: A-3E Quantum Technologies
```

The current Rev. 8 rendered manuscript is nine pages. The literal author/affiliation placeholders have been removed from the working copy; actual submission metadata remain open.

---

# Primary observable and exact model

Bright state:

```math
|B\rangle=N^{-1/2}\sum_j|j\rangle.
```

Exact completely positive enlarged dynamics:

```math
\dot\varrho
=\kappa_N\mathcal D[|c\rangle\langle B|]\varrho
+\gamma_N\sum_j\mathcal D[|j\rangle\langle j|]\varrho.
```

With surviving probability `P` and bright population `b`, exactly

```math
\dot P=-\kappa_Nb,
```

```math
\dot b=-(\kappa_N+\gamma_N)b+\frac{\gamma_N}{N}P.
```

The emergent slow eigenvalue is

```math
r_{-,N}
=\frac1N\frac{\kappa_N\gamma_N}{\kappa_N+\gamma_N}
[1+O(N^{-1})].
```

`r_-` is an eigenmode, not a microscopic return jump.

For prescribed conditional internal signal efficiency `eta`, define

```math
T_N(\eta)=\inf\{t:C_{S,N}(t)\ge\eta\}.
```

The paper's primary false-event quantity is the dilute susceptibility

```math
\boxed{
\chi_N(\eta)
=N\int_0^{T_N(\eta)}C_{loc,N}(u)du
=\lim_{d\to0}\frac{\mu_{loc,N}(\eta;d)}d.
}
```

A finite-rate independent Poisson realization gives `mu=d chi` and, to first order,

```math
P_{FA}=d\chi_N+O(d^2),
```

but this finite-rate interpretation is conditional on the kinetic lift.

---

# Rate-scaling theorem

Let

```math
\kappa_N=\kappa_0N^\alpha,
\qquad
\gamma_N=\gamma_0N^\beta,
\qquad
\kappa_0,\gamma_0>0,
```

with fixed `N`-independent exponents.

The active asymptotic classification remains

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

where

```math
q_0=\kappa_0/(\kappa_0+\gamma_0).
```

A fresh independent exact-kernel recheck reported no algebraic collapse of this table.

---

# Bounded extraction resource and no-go

For

```math
K=\sum_a|\ell_a\rangle\langle\ell_a|\ge0
```

and bounded per-state counted coupling `K_jj<=kappa_loc`,

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

The bounded-response efficiency supremum remains

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

Reference model:

```math
\mu_{1,N}(T)=N\int_0^T d e^{-ds}C_{loc,N}(T-s)ds.
```

On fixed strict slow branches,

```math
\mu_{1,N}(T_N)\ge
N(1-e^{-dT_N/2})C_{loc,N}(T_N/2)=\Omega(N).
```

Rev. 8 now states the matching upper bound explicitly: at most `N` sites can contribute, each at most once, and `0<=C_loc,N<=1`, so `mu_1,N<=N`. Therefore

```math
\boxed{\mu_{1,N}(T_N)=\Theta(N).}
```

This tests local source saturation only; it is not a theorem for arbitrary many-body detector saturation, extractor dead time, blocking, or nonlinear collective dynamics.

---

# Rev. 8 figure and reproducibility corrections

## Figure 1

The figure was rebuilt again after Rev. 7 still showed line/text crowding at actual manuscript scale.

Current layout:

```text
(a) State flow
signal -> bright -> counted sink
local event -> 1/N bright + (1-1/N) dark
local dephasing gamma_N in a dedicated lane
slow clock r_-^{-1} isolated in its own note box

(b) Operating definition
eta -> T_N(eta) -> chi_N(eta)
```

No long equations are embedded in the artwork. Page-scale visual QA found no text/line or text/box overlaps.

## Figure 2

The generator uses

```text
kappa_0=10
gamma_0=1
q_0=10/11 ~= 0.909
```

so the plotted `eta=.50` balanced-fast case is strictly subcritical, not the `eta=q_0` logarithmic boundary. Rev. 8 states these values in the plot and caption.

Exact-kernel fitted slopes over `N=10^3..10^4` with the actual figure parameters:

```text
extraction wins:       -1.00017
balanced fast:         +0.000034
balanced slow:         +1.99994
balanced collective:   +0.99994
```

---

# Illustrative physical anchor

No measured exponents are assigned to an existing device.

Pisani et al. (Nat. Commun. 14, 3914 (2023)) provide a concrete collective intersubband-polarization plus electronic-extractor architecture, but not an `N`-series that determines `(alpha,beta)`.

Analytical benchmark only:

```text
coherent addition of N equivalent extraction amplitudes
-> matrix element ~ sqrt(N)
-> extraction rate ~ N
-> alpha ~ 1

N-independent microscopic scattering/dephasing
-> gamma_N ~ N^0
-> beta ~ 0
```

This idealized mapping lies in the favorable extraction-dominated sector. If dephasing itself scales as `N`, the mapping lies on the balanced line. These are scaling benchmarks, not claims about the Pisani device.

---

# Claim boundaries

Keep all of the following explicit:

- `eta` is conditional internal collection after bright-state preparation, not end-to-end QE;
- the theorem concerns independent **local internal generation**;
- same-mode optical background is not rejected;
- bright-aligned correlated internal noise can bypass local-state rejection;
- gate opening assumes no residual internal excitation;
- finite-rate `mu=d chi` requires the kinetic lift;
- exact permutation symmetry remains a model assumption;
- no material realization is claimed;
- novelty remains **NOT ESTABLISHED**.

---

# Rev. 8 render state

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

# Next action

Do **not** open Experiment 10.

Known mathematical/referee objections are now narrow. The next rational step is another hostile review of the actual Rev. 8 rendered paper, focused on **significance/generalizability**, not another unconstrained theory expansion. Open heterogeneity theory only if that review identifies exact symmetry as a real publication blocker.
