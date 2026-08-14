# Agent recovery entrypoint

Read `AGENTS.md` first, then this file. Do not infer research chronology from `main` alone.

## Hard global constraint — ANALYTICAL / THEORETICAL ONLY

The project goal is a defensible theoretical photodetector paper grown from a simple Gedanken experiment. Do not open a new experiment while the current paper path remains scientifically alive.

Active work may use first-principles derivation, exact toy models, analytical bounds/no-go results, numerical thought experiments, adversarial primary-literature audits, and theoretical manuscript development. Do not make laboratory work the next step.

Preserve failed/corrected paths and do not use novelty/priority language without a dedicated audit.

---

# ACTIVE FRONTIER — Experiment 09 PRA Rev. 5

Branch:

```text
experiment-09-coherence-selective-photodetection
```

Active manuscript:

> **Scalable internal false-count limits in a coherence-selective photodetector**

Current first target:

```text
Physical Review A — Regular Article
suggested section: A-3E Quantum Technologies
```

## Read in this order

1. `experiments/09-coherence-selective-photodetection/CURRENT_STATE.md`
2. `experiments/09-coherence-selective-photodetection/PAPER_DRAFT_REV5_PRA_2026-08-14.md`
3. `experiments/09-coherence-selective-photodetection/PAPER_REV4_EXTERNAL_REFEREE_RESPONSE_2026-08-14.md`
4. `experiments/09-coherence-selective-photodetection/PAPER_REV5_PRA_RENDER_QA_2026-08-14.md`
5. `experiments/09-coherence-selective-photodetection/numerics/paper_rev5_figures.py`
6. `experiments/09-coherence-selective-photodetection/COLLECTIVE_EXTRACTION_RATE_BOUND_2026-08-14.md`
7. earlier Rev. 0–4 files only as correction history.

**Do not resume from Rev. 4's finite-`d` low-density asymptotic.** The external hostile review identified that formulation as self-inconsistent on much of the strict slow branch, and Rev. 5 replaces it.

---

# Why Rev. 5 exists

The external hostile referee review independently checked and accepted the principal one-excitation algebra and scaling exponents, but raised a major modeling objection:

```text
fixed per-site rate d
+ T_N or slow lifetime growing as N^(1-alpha)
-> per-site occupancy need not remain dilute as N->infinity.
```

The correct response was not another caveat. The primary asymptotic observable is now the **dilute accepted-event susceptibility**.

---

# Exact Lindblad model

Bright state:

```math
|B\rangle=N^{-1/2}\sum_j|j\rangle.
```

Counted sink `|c>` and local projectors `P_j=|j><j|`.

With

```math
\mathcal D[L]\rho
=L\rho L^\dagger-\frac12\{L^\dagger L,\rho\},
```

the enlarged evolution is

```math
\boxed{
\dot\varrho
=\kappa_N\mathcal D[|c\rangle\langle B|]\varrho
+\gamma_N\sum_j\mathcal D[P_j]\varrho.
}
```

Projecting onto the surviving excitation manifold and defining

```math
P=\operatorname{Tr}\rho,
\qquad
b=\langle B|\rho|B\rangle,
```

gives exactly

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

The emergent slow eigenvalue is

```math
\boxed{
r_{-,N}
=\frac1N
\frac{\kappa_N\gamma_N}{\kappa_N+\gamma_N}
[1+O(N^{-1})].
}
```

Important: `r_-` is an **effective slow eigenmode**, not a primitive microscopic return jump.

For every `gamma_N>0`, both bright and local excitations are eventually counted. The useful discriminator is the coexistence of a fast bright clock and a slow recycling clock; the gate converts that temporal separation into detector selectivity.

---

# PRIMARY REV. 5 OBSERVABLE — dilute accepted-event susceptibility

Photon-created bright collection kernel:

```math
C_{S,N}(t).
```

Uniform local internally generated event kernel:

```math
C_{loc,N}(t).
```

For required conditional internal collection efficiency `eta`, choose

```math
\boxed{
T_N(\eta)
=\inf\{t:C_{S,N}(t)\ge\eta\}.
}
```

Then define

```math
\boxed{
\chi_N(\eta)
=N\int_0^{T_N(\eta)}C_{loc,N}(u)du
=\lim_{d\to0}\frac{\mu_{loc,N}(\eta;d)}d.
}
```

This is now the paper's primary asymptotic quantity.

A finite-rate unsaturable independent-particle Poisson model satisfies

```math
\mu_{loc,N}=d\chi_N,
```

but this is a secondary mapping only. Do not claim that a fixed finite `d` remains physically low-density on every `N->infinity` slow branch.

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

Rev. 5 explicitly derives the limiting signal/local kernels in each sector. Do not collapse this back to a bare exponent table.

---

# Bounded local extraction resource

For positive extraction matrix

```math
K=\sum_a|\ell_a\rangle\langle\ell_a|,
```

and bounded per-local-state counted coupling

```math
K_{jj}\le\kappa_{loc},
```

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

That qualifier must remain attached to the theorem.

---

# ACTIVE HEADLINE THEOREM — bounded-response efficiency supremum

Assume useful extraction does not weaken with size:

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

Call this the **bounded-response efficiency supremum**, not an operational efficiency ceiling.

`O(1)` means nondivergent with size. It does not imply a small practical false-count probability.

Balanced-boundary precision:

```text
s=0, eta=q0:
    q0 is a supremum but is NOT attained;
    chi_N = Theta[(ln N)^2].

s>0, eta=q0:
    the boundary itself is bounded because
    N^(-s)(ln N)^2 -> 0.
```

---

# ROBUST NO-GO — survives maximal per-site saturation

Within the **linear single-excitation resource class**,

```math
\boxed{
\text{strict slow-recycling operation}
\Longrightarrow
\chi_N=\Omega(N).
}
```

The detailed `N^(2-alpha)` powers are dilute-response properties. To test whether slow-branch divergence is merely an unlimited-particle artifact, impose at most one event per microscopic site during the gate:

```math
\mu_{1,N}(T)
=N\int_0^T d e^{-ds}C_{loc,N}(T-s)ds.
```

Then

```math
\mu_{1,N}(T_N)
\ge N(1-e^{-dT_N/2})C_{loc,N}(T_N/2).
```

On every strict slow branch in the bounded-coupling class the two factors multiplying `N` approach positive constants or one, hence

```math
\boxed{
\mu_{1,N}(T_N)=\Theta(N).
}
```

Therefore:

```text
N^(2-alpha) finite-rate powers: MODEL-SPECIFIC.
Strict slow-branch divergence: ROBUST TO MAXIMAL PER-SITE SATURATION.
```

---

# Supporting thermodynamic result

The effective local-detailed-balance reverse-extraction analysis is now supporting material only.

At the efficiency-selected gate, fixed effective affinity gives

```text
fast branch:          O(1)
balanced boundary:    O(log N)
strict slow branch:   O(N)
```

for reverse injection.

Do not make this a coequal novelty claim.

---

# Figures / terminology

Reserve `dark manifold` for the coherent state-space sector.

Generated noise-origin events are `local internal events` / `false events`.

Use:

```text
C_loc,N
chi_N
```

rather than overloading `D`/`dark`.

Current Fig. 1:

```text
local event -> bright weight 1/N + dark-subspace weight 1-1/N;
gamma_N -> primitive local dephasing;
r_- -> effective slow eigenmode;
T_N and chi_N -> separate decision strip.
```

Fig. 2 plots exact finite-N `chi_N` approaching the asymptotic classes. It is a consistency illustration, not independent validation.

Fig. 3 is a scaling-classification diagram.

---

# Render state

Current Rev. 5 render:

```text
REVTeX/PRA compile: PASS
pages: 9
PDF SHA-256:
  bb41ad84b0904a9d126c9150a784effed0a9a77875f8358f4f03b7867df0bb7a
citations/cross-references: PASS
vector figures: PASS
visual QA: PASS
PDF preflight: PASS
author metadata: OPEN
novelty: NOT ESTABLISHED
```

See `PAPER_REV5_PRA_RENDER_QA_2026-08-14.md`.

---

# Prior-art boundary

Mandatory comparators remain:

- Young/Sarovar/Léonard 2018 — coherence/backaction detector framework;
- Young/Sarovar/Léonard 2020 — coherent collective detector architecture and dark-to-active isolation condition;
- Shammah et al. 2017 — local-dephasing bright/dark mixing;
- Pisani et al. 2023 — collective quantum IR detector extraction;
- Bassler/Lyne/Cuerda 2026 — collective/decoherence large-N scaling;
- Schwarzhans et al. 2026 — quantum-detector thermodynamic tradeoffs.

These eliminate broad novelty claims.

Focused audits have not found a direct statement of the complete Rev. 5 detector theorem, but **novelty remains unestablished**.

---

# NEXT ACTION

Do **not** open Experiment 10.

The external Rev. 4 fixed-`d` objection is repaired.

The next useful stress test is one fresh hostile review of **Rev. 5**, centered on the strongest remaining significance risk:

> Is the main bounded-response/no-go result structurally stable to a controlled class of bounded heterogeneity, or is it too dependent on exact permutation symmetry for PRA significance?

Candidate stressors if needed:

```text
weakly heterogeneous optical weights g_j;
bounded nonuniform local event rates;
bounded disorder in local dephasing;
finite-rank bright subspace;
correlated generation covariance with controlled bright projection.
```

Do not expand all of these automatically. Open only the minimum theory needed if the next hostile review identifies exact symmetry as a blocking defect. Otherwise move to final author metadata, final citation-network audit, and submission production.
