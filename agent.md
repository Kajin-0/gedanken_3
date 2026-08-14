# Agent recovery entrypoint

Read `AGENTS.md` first, then this file. Do not infer research chronology from `main` alone.

## Hard global constraint — ANALYTICAL / THEORETICAL ONLY

The user cannot perform real-life experiments. Active work is restricted to first-principles derivation, exact toy models, analytical bounds/invariants/no-go theorems, numerical thought experiments, adversarial primary-literature audits, and theoretical manuscript development.

Do not make fabrication, sample procurement, measurement pilots, instrumentation, annealing, device processing, or laboratory optimization the next step.

Preserve negative results. Do not use `novel`, `first`, `fundamental`, or priority language without a dedicated audit.

---

## Repository lineage

`main` contains the Experiment-01/Paper-A lineage and is not the current theory frontier.

Later branches include the closed Experiment-07 isotope-SRH line and the divergent closed Experiment-08 zero-gap Kane-statistics line. The QND information-without-absorption screen is also closed. Treat those branches as retained project knowledge; do not infer a single linear chronology from `main`.

---

# ACTIVE FRONTIER — Experiment 09: Coherence-Selective Photodetection

Branch:

```text
experiment-09-coherence-selective-photodetection
```

## CRITICAL STATUS CHANGE

Experiment 09 has passed the repository's threshold for **manuscript development**.

```text
premise generation: COMPLETE FOR NOW
paper-level combined prior-art audit: PROVISIONAL PASS
manuscript architecture: OPEN
Rev. 0 manuscript: OPEN
Experiment 10: DO NOT OPEN WHILE THIS PAPER CANDIDATE REMAINS ALIVE
```

The next action is a hostile referee-style review of the actual Rev. 0 paper, focused on significance/novelty and the possibility that the central result is only a repackaging of established state discrimination or optical/electrical area decoupling.

Do not resume the old instruction `paper drafting: DO NOT BEGIN`; it is superseded.

## Read in order

1. `experiments/09-coherence-selective-photodetection/CURRENT_STATE.md`
2. `experiments/09-coherence-selective-photodetection/PAPER_LEVEL_CLOSEST_PRIOR_ART_AUDIT_2026-08-14.md`
3. `experiments/09-coherence-selective-photodetection/PAPER_ARCHITECTURE_COHERENCE_DARK_SCALING_2026-08-14.md`
4. `experiments/09-coherence-selective-photodetection/PAPER_DRAFT_REV0_2026-08-14.md`
5. `experiments/09-coherence-selective-photodetection/GATED_DETECTOR_ROC_AND_SCALABILITY_THEOREM_2026-08-14.md`
6. `experiments/09-coherence-selective-photodetection/GENERAL_PASSIVE_EXTRACTION_AFFINITY_BOUND_2026-08-14.md`
7. `experiments/09-coherence-selective-photodetection/FIRST_PRINCIPLES_BRIGHT_STATE_DISCRIMINATION_2026-08-14.md`
8. `experiments/09-coherence-selective-photodetection/DEPHASING_EXTRACTION_AND_DETAILED_BALANCE_2026-08-14.md`
9. `experiments/09-coherence-selective-photodetection/CRITICAL_COUPLING_THERMAL_REVERSE_COST_2026-08-14.md`

---

# Central Gedanken premise

Use an `N`-dimensional single-excitation manifold. A photon prepares a coherent bright state

```math
|B\rangle=\sum_j\sqrt{w_j}e^{i\phi_j}|j\rangle,
```

while the adversarial internal dark event is chosen to have exactly the same microscopic populations but no coherence:

```math
\rho_D=\sum_jw_j|j\rangle\langle j|.
```

Thus energy, carrier number, and every local-basis diagonal observable are exactly unable to distinguish event provenance. Coherence is the only label.

For the symmetric gated theorem,

```math
|B\rangle=\frac1{\sqrt N}\sum_j|j\rangle.
```

---

# Result 1 — state-space dark projection

For

```math
\Pi_B=|B\rangle\langle B|,
```

ideal signal acceptance is unity and the population-matched incoherent dark state has acceptance

```math
\boxed{
\epsilon_D=\sum_jw_j^2=1/N_{eff}.
}
```

For general dark-generation covariance

```math
D=\sum_\alpha|l_\alpha\rangle\langle l_\alpha|,
```

and optical coupling vector `g`, the accepted internal dark-generation rate is

```math
\boxed{
\Gamma_D^B=\frac{g^\dagger Dg}{g^\dagger g}.
}
```

For independent identical local dark channels `D=dI`,

```math
\mathrm{Tr}D=Nd,
```

but

```math
\boxed{\Gamma_D^B=d.}
```

Generic state-verification mathematics is old; do not claim that part as new.

---

# Result 2 — exact finite-time extraction/dephasing dynamics

For bright extraction `kappa` and local dephasing `gamma`, surviving excitation probability `P` and bright population `b` obey

```math
\dot P=-\kappa b,
```

```math
\dot b=-(\kappa+\gamma)b+(\gamma/N)P.
```

Thus

```math
\ddot P+(\kappa+\gamma)\dot P+(\kappa\gamma/N)P=0.
```

With

```math
\Delta=\sqrt{(\kappa+\gamma)^2-4\kappa\gamma/N},
```

```math
r_\pm=(\kappa+\gamma\pm\Delta)/2,
```

the exact signal/dark collection-kernel separation is

```math
\boxed{
C_S(t)-C_D(t)
=\frac{\kappa(1-1/N)}{\Delta}
\left(e^{-r_-t}-e^{-r_+t}\right).
}
```

For every `gamma>0`,

```math
C_S(\infty)=C_D(\infty)=1.
```

Therefore coherence-based dark rejection is finite-time.

For large `N`,

```math
\boxed{
r_-\simeq\frac{\kappa\gamma}{N(\kappa+\gamma)},
\qquad
\tau_{leak}\simeq N(1/\kappa+1/\gamma).
}
```

High fast-window signal collection requires `kappa>>gamma`.

---

# Result 3 — exact gated internal-dark theorem

Assume independent local dark-generation Poisson processes with rate `d` per site. Raw internal dark generation is

```math
Nd.
```

For a gate of duration `T`, the exact accepted dark-count mean is

```math
\boxed{
\mu_{local}(T)
=Nd\int_0^T C_D(u)du.
}
```

and

```math
P_{FA,local}=1-e^{-\mu_{local}}.
```

A photon arriving at the gate opening is detected with probability

```math
\eta_S(T)=C_S(T).
```

In the coherence-preserving limit `gamma=0`,

```math
C_D(t)=\frac1N(1-e^{-\kappa t}),
```

so

```math
\boxed{
\mu_{local}(T)
=d\left[
T-\frac{1-e^{-\kappa T}}{\kappa}
\right].
}
```

**The factor `N` cancels exactly.**

This is the current manuscript's central result:

```text
raw internal dark generation: O(N)
accepted gated internal dark-count mean: O(1)
ideal photon detection after fast extraction: O(1)
```

All `N` dark-generating sites remain physically present; suppression occurs in excitation Hilbert space, not by shrinking electrical volume.

For nonzero dephasing, sufficiently long gates recover extensive counting. The useful regime is approximately

```math
\boxed{
1/\kappa\ll T\ll N/\gamma
}
```

when `kappa>>gamma` and `N` is large.

---

# Result 4 — generalized passive-extraction affinity theorem

For arbitrary stationary locally detailed-balanced counted channels `a`,

```math
\bar\kappa_a/\kappa_a=e^{-\beta\Delta F_a}.
```

Let

```math
K_\to=\sum_a\kappa_a,
\qquad
K_\leftarrow=\sum_a\bar\kappa_a.
```

With `p_a=\kappa_a/K_to`,

```math
\boxed{
\frac{K_\leftarrow}{K_\to}
=\sum_ap_ae^{-\beta\Delta F_a}
=e^{-\beta\Delta F_{eff}}.
}
```

Hence

```math
\boxed{
\Delta F_{eff}
=-kT\ln\left(\sum_ap_ae^{-\beta\Delta F_a}\right).
}
```

and

```math
\min\Delta F_a
\le\Delta F_{eff}
\le\sum_ap_a\Delta F_a
\le\max\Delta F_a.
```

Parallel passive pathways and affinity heterogeneity do not create a stronger effective reverse suppression.

If useful forward counted extraction is collectively enhanced by

```math
K_\to(N)=\mathcal C(N)K_\to(1),
```

then holding the reverse bright-injection coefficient fixed requires

```math
\boxed{
\Delta F_{eff}(N)-\Delta F_{eff}(1)
\ge kT\ln\mathcal C(N).
}
```

The previous `kT ln N` result is the special case `mathcal C=N`.

For a reverse-injection Poisson process, the gated contribution is

```math
\boxed{
\mu_{rev}(T)
=K_\leftarrow\int_0^T C_S(u)du.
}
```

so

```math
\boxed{
\mu_{dark}(T)=\mu_{local}(T)+\mu_{rev}(T).
}
```

The affinity theorem is therefore directly a detector false-count scaling law.

---

# Hidden-state passive-network result

For an equilibrium detailed-balanced finite Markov network, Gibbs symmetrization makes the generator symmetric. Eliminating hidden intermediate states by the quasistatic Schur complement preserves symmetry, hence effective boundary detailed balance:

```math
\boxed{
\pi_iK_{i\to j}^{eff}
=\pi_jK_{j\to i}^{eff}.
}
```

Passive equilibrium intermediate-state complexity therefore cannot produce an effective one-way counted transition in this reduction.

Do not extend this claim to every nonreciprocal or non-Markovian architecture.

---

# Closest-prior-art disposition

Read `PAPER_LEVEL_CLOSEST_PRIOR_ART_AUDIT_2026-08-14.md` before making significance claims.

Individual ingredients are established:

```text
quantum state discrimination / POVMs;
collective bright/dark states;
superradiance/subradiance;
dephasing-induced bright/dark transfer;
coherence-dependent photocurrent;
collective quantum infrared detector transport;
local detailed balance / KMS;
collective thermodynamic current/noise scaling;
nonreciprocal thermal transport.
```

The focused primary-literature audit found **no direct stronger match** to the combined detector-specific chain, especially the exact finite-gate `N` cancellation plus dephasing and reverse-affinity scaling.

This is not proof of novelty.

The strongest practical comparator is conventional resonant IR detector **optical-area/electrical-area decoupling**. The manuscript must distinguish that physical-space strategy from the present state-space strategy:

```text
conventional:
    reduce/isolate dark-generating electrical volume;

Experiment 09:
    retain all N dark-generating sites and raw rate Nd,
    reject local events because they occupy the wrong Hilbert-space direction.
```

---

# Manuscript state

Current working title:

> **Coherence-selective suppression of internal dark counts in a gated photodetector**

Read:

- `PAPER_ARCHITECTURE_COHERENCE_DARK_SCALING_2026-08-14.md`
- `PAPER_DRAFT_REV0_2026-08-14.md`

Rev. 0 contains Abstract, Introduction, complete central derivation, Discussion, Conclusion, and reference placeholders.

## NEXT ACTION — DO THIS BEFORE MORE THEORY

Perform an **extreme hostile referee review of Rev. 0** with these questions:

1. Is the exact gated `N` cancellation genuinely detector-specific, or does it reduce immediately to a known stronger theorem?
2. Is the distinction from optical/electrical area decoupling physically substantive?
3. Is the Poisson-thinning detector interpretation mathematically and operationally correct?
4. Does the dephasing model support the manuscript's claimed useful window without hidden assumptions?
5. Is the `kT ln mathcal C` section useful synthesis or too trivial to carry manuscript weight?
6. Does the paper need a stronger generalization to nonuniform `g`, nonuniform local dark rates, or correlated `D` before submission?
7. Are there any hidden violations of passivity, detailed balance, or detector reset semantics?
8. Is the contribution significant enough for a full theoretical research article, or should it be compressed into a shorter conceptual/theory paper?

If the referee identifies a fatal direct-prior-art or equivalence objection, close/narrow honestly. If not, revise Rev. 0 rather than opening a new experiment.

---

# Escape classes / claim boundaries

Not ruled out by the present theorem:

```text
same-mode thermal/background photons;
correlated dark baths aligned with the bright vector;
static nonreciprocity beyond simple pairwise LDB;
strong non-Markovian transients;
active/time-modulated extraction;
maintained nonequilibrium reservoirs;
many-excitation saturation;
real-material inability to prepare/preserve the required coherent state.
```

Do not silently broaden the theorem across these boundaries.

---

# Closed-path reminders

- Experiment 08: zero-gap Kane asymptotics retained; publication path closed.
- Experiment 07: isotope-SRH identities retained; novelty path closed.
- Experiment 06: two-carrier SRH provenance architecture closed by direct prior art.
- Experiment 05: active-volume/bandwidth theorem failed with arbitrary lossless matching.
- Experiment 04: passive nonreciprocal sensitivity path closed by trace bound.
- Experiment 03: photon-recycling cross-noise path closed as established linear exchange information.
- Experiment 02: migrating-depth APD dominated by fixed-depth waveguide comparator.
- Experiment 01: final full-research submission path closed by established acquisition/optimum-filter theory despite retained mathematics.
- QND information without absorption: closed by direct QND prior art.
