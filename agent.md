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

## CRITICAL CURRENT STATUS

Experiment 09 is an **active paper candidate**.

Rev. 0 was deliberately subjected to a hostile review and **failed as written**. Do not restore its old centerpiece.

The hostile review found:

```text
static 1/N bright-state rejection:
    mathematically close to standard normalized coherent-mode filtering;

finite-rate Poisson counts under strict one-excitation model:
    exactness overstated;

C_S as "photon efficiency":
    wrong scope; it is conditional internal collection after bright-state preparation;

kT ln(mathcal C):
    valid LDB consequence but too generic for coequal novelty.
```

The review also exposed a much stronger theorem. Rev. 1 has been rebuilt around it.

```text
Experiment 10: DO NOT OPEN WHILE REV. 1 REMAINS ALIVE
```

---

## Read in this order

1. `experiments/09-coherence-selective-photodetection/CURRENT_STATE.md`
2. `experiments/09-coherence-selective-photodetection/PAPER_DRAFT_REV1_2026-08-14.md`
3. `experiments/09-coherence-selective-photodetection/EFFICIENCY_SCALABILITY_TRANSITION_2026-08-14.md`
4. `experiments/09-coherence-selective-photodetection/PAPER_REV0_HOSTILE_REFEREE_REVIEW_2026-08-14.md`
5. `experiments/09-coherence-selective-photodetection/PAPER_REV1_SCALING_PRIOR_ART_AUDIT_2026-08-14.md`
6. `experiments/09-coherence-selective-photodetection/numerics/efficiency_scaling_transition_check.py`
7. `experiments/09-coherence-selective-photodetection/PAPER_LEVEL_CLOSEST_PRIOR_ART_AUDIT_2026-08-14.md`
8. earlier Experiment-09 derivation files only for history / supporting results.

---

# Central Gedanken premise

A photon prepares a coherent bright state across `N` local excited states,

```math
|B\rangle=\sum_j\sqrt{w_j}e^{i\phi_j}|j\rangle,
```

while the adversarial internal dark event has the same local populations but no coherence,

```math
\rho_D=\sum_jw_j|j\rangle\langle j|.
```

Thus energy, excitation number, and all local-basis diagonal observables are deliberately blind to provenance.

The uniform theorem uses

```math
|B\rangle=\frac1{\sqrt N}\sum_j|j\rangle.
```

Static projection onto `|B>` gives `1/N` acceptance of a uniform incoherent local excitation, but treat this as **old mode-filtering/state-verification geometry**, not the paper claim.

---

# Exact one-body dynamics

Bright extraction rate `kappa`; independent local pure dephasing `gamma`.

```math
\dot P=-\kappa b,
```

```math
\dot b=-(\kappa+\gamma)b+\frac\gamma N P.
```

Hence

```math
\ddot P+(\kappa+\gamma)\dot P+\frac{\kappa\gamma}{N}P=0.
```

Let

```math
a=\kappa+\gamma,
```

```math
\Delta_N=\sqrt{a^2-4\kappa\gamma/N},
```

```math
r_{\pm,N}=(a\pm\Delta_N)/2.
```

Exact survival for initial bright population `b_0`:

```math
P_{b_0,N}(t)
=
\frac{r_{+,N}-\kappa b_0}{\Delta_N}e^{-r_{-,N}t}
+
\frac{\kappa b_0-r_{-,N}}{\Delta_N}e^{-r_{+,N}t}.
```

Collection `C=1-P`.

Signal bright state: `b_0=1`.
Uniform local dark event: `b_0=1/N`.

For every `gamma>0`, both are eventually collected, and

```math
r_{-,N}\simeq\frac{\kappa\gamma}{N(\kappa+\gamma)}.
```

---

# Required counting-model repair

The one-excitation quantum kernel is lifted to continuous dark generation through an explicit independent-particle stochastic model:

```text
N local sites generate independent Poisson events at rate d;
each event is distinguishable and noninteracting;
each carries its own independent copy of the exact one-body kernel.
```

Only under this lift is the accepted finite-rate count process claimed to be exactly Poisson:

```math
\mu_N(T)=Nd\int_0^T C_{D,N}(u)du.
```

Signal performance is **conditional internal collection after bright-state preparation**:

```math
\eta_{int,N}(T)=C_{S,N}(T).
```

Do not call it end-to-end photon QE.

---

# MAIN RESULT — fixed-efficiency scalability transition

Fix required conditional internal collection efficiency `0<eta<1`.

Define

```math
T_N(\eta)=\inf\{t:C_{S,N}(t)\ge\eta\},
```

and

```math
\mu_N(\eta)=Nd\int_0^{T_N(\eta)}C_{D,N}(u)du.
```

Define

```math
\boxed{
q=\eta_c=\frac{\kappa}{\kappa+\gamma}
}
```

and

```math
\lambda=\frac{\kappa\gamma}{\kappa+\gamma}.
```

Then

```math
\boxed{
\begin{array}{c|c|c}
\text{required internal efficiency} & T_N & \mu_N\\
\hline
0<\eta<q & O(1) & O(1)\\
\eta=q & \Theta(\ln N) & \Theta((\ln N)^2)\\
q<\eta<1 & O(N) & O(N^2).
\end{array}}
```

This is the active paper centerpiece.

## Subcritical explicit limit

For

```math
x_\eta=-\ln(1-\eta/q),
```

```math
\boxed{aT_N\to x_\eta}
```

and

```math
\boxed{
\mu_N
\to
\frac d a
\left[
\frac{q(1-q)}2x_\eta^2+q^2x_\eta-q\eta
\right].
}
```

## Supercritical explicit limit

```math
\boxed{
\frac{T_N}{N}
\to
\frac1\lambda\ln\frac{1-q}{1-\eta}
}
```

and

```math
\boxed{
\frac{\mu_N}{N^2}
\to
\frac d\lambda
\left[
\ln\frac{1-q}{1-\eta}
-
\frac{\eta-q}{1-q}
\right].
}
```

## Critical boundary

```math
\boxed{
aT_N(q)
\sim W\left(\frac{N}{(1-q)^2}\right)
}
```

so

```math
T_N=\Theta(\ln N),
\qquad
\mu_N=\Theta((\ln N)^2).
```

The Lambert-W coefficient is a boundary-layer asymptotic with slow finite-`N` convergence. Do not overstate its precision without a tighter remainder analysis.

---

# Operational criterion

The scalable bounded branch requires

```math
\boxed{
\eta<\frac{\kappa}{\kappa+\gamma}.
}
```

Equivalently

```math
\boxed{
\frac{\kappa}{\gamma}>
\frac{\eta}{1-\eta}.
}
```

A 99% **internal collection** target therefore requires `kappa/gamma>99` to remain strictly subcritical as `N->infinity`.

---

# gamma=0 result — COROLLARY ONLY

When `gamma=0`, `q=1`; every fixed `eta<1` is subcritical.

Exactly,

```math
\mu_N(\eta)
=\frac d\kappa[-\ln(1-\eta)-\eta],
```

independent of `N`.

Retain this as intuition/consistency check, not principal novelty.

---

# Prior-art disposition after Rev. 1 audit

Read `PAPER_REV1_SCALING_PRIOR_ART_AUDIT_2026-08-14.md`.

Broad neighboring results are established:

```text
coherence/backaction controls detector metrics;
bright/dark collective modes;
local-dephasing bright/dark scattering;
coherence/dark-state photocells;
collective electronic polarization + extractor current in IR detectors;
large-N decoherence scaling transitions in Dicke/superabsorption systems;
quantum-detector thermodynamic efficiency/dark-count tradeoffs.
```

Particularly important current sources:

- Bassler, Lyne, Cuerda, `arXiv:2607.28034` (2026): decoherence-controlled Dicke scaling regimes and transient critical behavior;
- Álvarez-Cuartas and Reina, Phys. Rev. Research 8, 033035 (2026): dynamical scaling in quantum superabsorption;
- Schwarzhans et al., PRX Quantum 7, 033001 (2026): nonequilibrium thermodynamic tradeoffs among detector efficiency, dark counts, jitter, and dead time;
- Pisani et al., Nature Communications 14, 3914 (2023): collective quantum IR detector polarization coupled to electronic extraction.

These kill broad novelty claims.

The focused audit did **not** find a direct match to the specific fixed-efficiency theorem

```text
eta_c=kappa/(kappa+gamma)
+
minimal gate chosen by eta
+
O(1) / logarithmic / O(N^2) local-dark burden.
```

Absence of a hit is not proof of novelty.

---

# Thermodynamic affinity result — supporting only

The locally detailed-balanced extraction result

```math
\Delta F_{extra}\ge kT\ln\mathcal C
```

remains correct under its stated assumptions, but it is now secondary. Do not sell it as a new thermodynamics theorem; current quantum-detector thermodynamics makes that untenable.

---

# Manuscript state

Current working paper:

> **Efficiency-controlled dark-count scaling transition in a coherence-selective photodetector**

File:

`experiments/09-coherence-selective-photodetection/PAPER_DRAFT_REV1_2026-08-14.md`.

Rev. 0 remains in history as a failed draft and should not be silently overwritten.

---

# NEXT ACTION

Do **not** open Experiment 10.

Next:

1. perform a fresh hostile referee review of **Rev. 1**, focused on whether the fixed-efficiency theorem is actually publishable and sufficiently distinct from current Dicke/decoherence scaling literature;
2. tighten the critical `eta=q` asymptotic if a referee would demand an error bound;
3. if it survives, generate manuscript figures from the exact finite-`N` equations and asymptotic laws;
4. complete citation-production audit and then consider journal-facing formatting.

Current state:

```text
Rev. 0: FAIL AS WRITTEN
Rev. 1: ACTIVE
main theorem: FIXED-EFFICIENCY THREE-REGIME SCALING
mathematical consistency: PASSES CURRENT CHECK
focused prior-art screen: PASSES WITHOUT DIRECT MATCH
novelty: NOT ESTABLISHED
paper path: ACTIVE
```

---

# Closed-path reminders

Experiments 01–08 and the QND screen contain retained results but closed publication paths. Do not reopen them merely because Rev. 1 becomes difficult. The project goal is a defensible paper, not a maximum number of branches.
