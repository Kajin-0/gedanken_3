# Current State — Experiment 09: Coherence-Selective Photodetection

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** **ACTIVE PAPER CANDIDATE / REV. 0 FAILED AS WRITTEN / REV. 1 REBUILT AROUND FIXED-EFFICIENCY SCALABILITY THEOREM / FOCUSED 2026 PRIOR-ART AUDIT SURVIVES / NOVELTY NOT ESTABLISHED**

## Read next

1. `PAPER_DRAFT_REV1_2026-08-14.md`
2. `EFFICIENCY_SCALABILITY_TRANSITION_2026-08-14.md`
3. `PAPER_REV0_HOSTILE_REFEREE_REVIEW_2026-08-14.md`
4. `PAPER_REV1_SCALING_PRIOR_ART_AUDIT_2026-08-14.md`
5. `numerics/efficiency_scaling_transition_check.py`
6. `PAPER_LEVEL_CLOSEST_PRIOR_ART_AUDIT_2026-08-14.md`
7. `GENERAL_PASSIVE_EXTRACTION_AFFINITY_BOUND_2026-08-14.md`
8. earlier first-principles/dephasing files only as derivation history.

Do not resume from the old instruction that the `gamma=0` `N` cancellation is the manuscript centerpiece. That was superseded by the hostile Rev. 0 review.

---

# 1. Minimal Gedanken premise

Use an `N`-dimensional degenerate single-excitation manifold. A photon prepares a coherent bright state

```math
|B\rangle
=\sum_j\sqrt{w_j}e^{i\phi_j}|j\rangle,
```

while the adversarial internal dark event has the same local populations but no coherence:

```math
\rho_D
=\sum_jw_j|j\rangle\langle j|.
```

Thus energy, excitation number, and every local-basis diagonal observable are intentionally blind to event provenance.

For the symmetric theorem,

```math
|B\rangle=\frac1{\sqrt N}\sum_j|j\rangle.
```

Static bright projection gives `1/N` dark acceptance for the uniform incoherent state, but this is now treated as **standard coherent-mode/state-verification geometry**, not the manuscript novelty claim.

---

# 2. Exact one-body extraction/dephasing kernel

Bright extraction rate `kappa`; independent local pure-dephasing rate `gamma`.

Define surviving excitation probability `P` and bright population `b`:

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

With

```math
a=\kappa+\gamma,
```

```math
\Delta_N=\sqrt{a^2-4\kappa\gamma/N},
```

```math
r_{\pm,N}=(a\pm\Delta_N)/2,
```

the exact survival probability for initial bright population `b_0` is

```math
P_{b_0,N}(t)
=
\frac{r_{+,N}-\kappa b_0}{\Delta_N}e^{-r_{-,N}t}
+
\frac{\kappa b_0-r_{-,N}}{\Delta_N}e^{-r_{+,N}t}.
```

Collection is `C=1-P`.

Photon-created bright excitation: `b_0=1`.
Uniformly local dark excitation: `b_0=1/N`.

For every `gamma>0`, both are eventually collected:

```math
C_{S,N}(\infty)=C_{D,N}(\infty)=1.
```

The slow leakage rate is

```math
r_{-,N}\simeq\frac{\kappa\gamma}{N(\kappa+\gamma)}.
```

---

# 3. Critical modeling repair — independent-particle stochastic lift

Rev. 0 incorrectly presented an exact finite-rate Poisson count process as if it followed directly from the strict single-excitation Hilbert space.

The repair is explicit:

```text
one-body Lindblad model -> exact collection kernel for one generated excitation;
continuous dark generation -> separate classical Poisson immigration process;
each generated excitation -> distinguishable, noninteracting independent copy of the one-body dynamics.
```

Under this independent-particle lift, `N` local sites each generate events at rate `d`, so raw generation is `Nd`, and accepted local dark counts in a gate `[0,T]` are exactly Poisson within the lifted model with mean

```math
\boxed{
\mu_N(T)=Nd\int_0^T C_{D,N}(u)du.
}
```

The signal quantity is **conditional internal collection efficiency after bright-state preparation**:

```math
\eta_{int,N}(T)=C_{S,N}(T).
```

It is not end-to-end optical quantum efficiency.

---

# 4. NEW MAIN THEOREM — efficiency-controlled scalability transition

Fix a required conditional internal collection efficiency

```math
0<\eta<1
```

and define the minimum gate

```math
T_N(\eta)
=\inf\{t:C_{S,N}(t)\ge\eta\}.
```

At that gate define

```math
\mu_N(\eta)
=Nd\int_0^{T_N(\eta)}C_{D,N}(u)du.
```

Now define the fast branching fraction

```math
\boxed{
q=\eta_c=\frac{\kappa}{\kappa+\gamma}
}
```

and

```math
\lambda=\frac{\kappa\gamma}{\kappa+\gamma}.
```

The large-`N` detector separates into three regimes:

```math
\boxed{
\begin{array}{c|c|c}
\text{efficiency regime} & T_N(\eta) & \mu_N(\eta)\\
\hline
0<\eta<q & O(1) & O(1)\\
\eta=q & \Theta(\ln N) & \Theta((\ln N)^2)\\
q<\eta<1 & O(N) & O(N^2).
\end{array}}
```

This is the active manuscript centerpiece.

## 4.1 Subcritical branch

For `eta<q`, define

```math
x_\eta=-\ln(1-\eta/q).
```

Then

```math
\boxed{aT_N(\eta)\to x_\eta}
```

and

```math
\boxed{
\mu_N(\eta)
\to
\frac{d}{a}
\left[
\frac{q(1-q)}2x_\eta^2+q^2x_\eta-q\eta
\right].
}
```

Thus raw local generation is `O(N)` but the fixed-efficiency accepted dark burden is bounded.

## 4.2 Supercritical branch

For `eta>q`, on slow time `t=Ny`,

```math
C_{S,N}(Ny)\to1-(1-q)e^{-\lambda y},
```

```math
C_{D,N}(Ny)\to1-e^{-\lambda y}.
```

Therefore

```math
\boxed{
\frac{T_N(\eta)}N
\to
\frac1\lambda
\ln\frac{1-q}{1-\eta}
}
```

and

```math
\boxed{
\frac{\mu_N(\eta)}{N^2}
\to
\frac{d}{\lambda}
\left[
\ln\frac{1-q}{1-\eta}
-
\frac{\eta-q}{1-q}
\right].
}
```

## 4.3 Critical branch

At `eta=q`, the fast tail balances incipient slow leakage:

```math
\boxed{
aT_N(q)
\sim W\left(\frac{N}{(1-q)^2}\right),}
```

so

```math
T_N(q)=\Theta(\ln N),
```

and

```math
\mu_N(q)=\Theta((\ln N)^2).
```

The Lambert-W coefficient is an asymptotic boundary-layer result; convergence is slower than in the two off-critical branches.

---

# 5. Operational scalability condition

The asymptotically bounded branch requires

```math
\boxed{
\eta<\frac{\kappa}{\kappa+\gamma}.
}
```

Equivalently,

```math
\boxed{
\frac{\kappa}{\gamma}>
\frac{\eta}{1-\eta}.
}
```

Example: a 99% **conditional internal** collection target requires `kappa/gamma>99` to remain strictly subcritical as `N->infinity`.

This is stronger and more task-specific than the old heuristic `kappa >> gamma`.

---

# 6. No-dephasing `N` cancellation — retained only as a corollary

For `gamma=0`, `q=1`; every fixed target `eta<1` is subcritical.

Exactly,

```math
C_{D,N}(t)=\frac1N(1-e^{-\kappa t}),
```

and

```math
\boxed{
\mu_N(\eta)
=\frac{d}{\kappa}
[-\ln(1-\eta)-\eta]
}
```

independent of `N`.

This result remains useful but is no longer sufficient as the paper's main novelty claim because it is mathematically close to ordinary normalized coherent-mode filtering of independent noise.

---

# 7. Numerical validation

Reproducible script:

`numerics/efficiency_scaling_transition_check.py`.

For the illustrative dimensionless choice

```text
kappa=10
gamma=1
d=1
```

so `q=10/11`, exact finite-`N` calculations converge to the analytical coefficients.

Examples:

```text
eta=0.95 (>q):
T_N/N -> 0.6576207008
mu_N/N^2 -> 0.1626207008

eta=0.99 (>q):
T_N/N -> 2.4280024045
mu_N/N^2 -> 1.4490024045
```

Subcritical `eta=.5` and `.9` converge to finite `T_N` and finite `mu_N` as predicted. Critical convergence is logarithmic and correspondingly slower.

These values are theory checks, not material parameters.

---

# 8. Hostile Rev. 0 disposition

`PAPER_REV0_HOSTILE_REFEREE_REVIEW_2026-08-14.md` records:

```text
REV. 0 AS WRITTEN: FAIL
reason 1: centerpiece too close to standard coherent-mode projection
reason 2: Poisson exactness overstated under strict single-excitation model
reason 3: C_S mislabeled as total photon detection efficiency
reason 4: thermodynamic kT ln C result too generic for coequal novelty

PAPER PATH AFTER NEW THEOREM: ACTIVE / MAJOR REVISION
```

Do not erase this correction history.

---

# 9. Current prior-art position

Read `PAPER_REV1_SCALING_PRIOR_ART_AUDIT_2026-08-14.md`.

Established neighboring structures include:

```text
quantum coherence/backaction in photodetector performance;
bright/dark collective states;
local-dephasing intermode transfer;
coherence/dark-state photocells;
collective electronic polarization + extractor current in quantum IR detectors;
large-N decoherence scaling transitions in Dicke/superabsorption systems;
quantum-detector efficiency/dark-count thermodynamic tradeoffs.
```

Important 2026 sources now include:

- Bassler, Lyne, Cuerda, `arXiv:2607.28034`, scaling theory of decoherence in Dicke superradiance;
- Álvarez-Cuartas and Reina, Phys. Rev. Research 8, 033035 (2026), dynamical scaling in quantum superabsorption;
- Schwarzhans et al., PRX Quantum 7, 033001 (2026), thermodynamic tradeoffs among quantum-detector efficiency, dark counts, jitter, and dead time.

These sources eliminate broad novelty claims about decoherence scaling or detector thermodynamic tradeoffs.

Focused searches have **not** found a direct stronger statement of the specific fixed-efficiency theorem

```text
eta_c=kappa/(kappa+gamma)
+
minimal-gate local-dark burden
+
O(1) / logarithmic / O(N^2) scaling partition.
```

This is not proof of novelty.

---

# 10. Thermodynamic affinity result — retained but demoted

For parallel locally detailed-balanced extraction channels,

```math
K_\leftarrow/K_\to=e^{-\beta\Delta F_{eff}}.
```

If useful forward extraction scales by `mathcal C`, a fixed reverse coefficient requires

```math
\Delta F_{extra}\ge kT\ln\mathcal C.
```

This remains correct under the stated assumptions but is now a **secondary resource constraint**, not a principal novelty claim. The 2026 autonomous quantum-detector thermodynamics literature makes this demotion especially important.

---

# 11. Manuscript state

Current manuscript:

> **Efficiency-controlled dark-count scaling transition in a coherence-selective photodetector**

File:

`PAPER_DRAFT_REV1_2026-08-14.md`.

Rev. 1 explicitly:

- admits the standard mode-filtering equivalence of the static result;
- repairs the count model with the independent-particle lift;
- renames `C_S` as conditional internal collection;
- makes the three-regime theorem the central result;
- retains the no-dephasing cancellation as a corollary;
- demotes thermodynamic affinity to a secondary constraint;
- incorporates current 2026 scaling and detector-thermodynamics prior art.

---

# 12. Current next gate

Do **not** open Experiment 10.

The next useful work is:

1. perform a fresh hostile review of **Rev. 1**, centered only on the fixed-efficiency theorem;
2. verify whether the critical Lambert-W asymptotic needs a tighter error bound or only scaling-level claim;
3. if Rev. 1 survives, generate theory figures exposing the three scaling regimes;
4. run a final citation-production audit, especially current 2025–2026 open-system scaling literature;
5. then decide whether the paper is strong enough for journal-facing formatting.

Current disposition:

```text
simple Gedanken premise: RETAIN
static 1/N projection: OLD GEOMETRY / SUPPORTING
exact one-body dephasing kernel: RETAIN
independent-particle count lift: EXPLICIT MODEL ASSUMPTION
fixed-efficiency three-regime theorem: ACTIVE CENTRAL RESULT
no-dephasing O(1) dark burden: COROLLARY
thermodynamic kT ln C: SUPPORTING CONSTRAINT
Rev. 0: FAILED AS WRITTEN
Rev. 1: ACTIVE
novelty: NOT ESTABLISHED
paper path: CONTINUE
```
