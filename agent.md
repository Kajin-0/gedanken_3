# Agent recovery entrypoint

Read `AGENTS.md` first, then this file. Do not infer research chronology from `main` alone.

## Hard global constraint — ANALYTICAL / THEORETICAL ONLY

The project goal is a defensible theoretical photodetector paper grown from a simple Gedanken experiment.

Active work may use first-principles derivation, exact toy models, analytical bounds/no-go results, numerical thought experiments, adversarial primary-literature audits, and theoretical manuscript development. Do not make laboratory work the next step.

Preserve failed/corrected paths and do not use novelty/priority language without a dedicated audit.

---

# ACTIVE FRONTIER — Experiment 10

Branch:

```text
experiment-10-room-temperature-lwir-admissibility
```

Working title for the research line only:

> **Room-temperature LWIR band-structure admissibility**

This is not yet a manuscript title.

## Read in this order

1. `experiments/10-room-temperature-lwir-admissibility/CURRENT_STATE.md`
2. `experiments/10-room-temperature-lwir-admissibility/FOUNDING_GEDANKEN_2026-08-14.md`
3. `experiments/10-room-temperature-lwir-admissibility/PRIOR_BRANCH_BOUNDARY_2026-08-14.md`
4. `experiments/10-room-temperature-lwir-admissibility/PROGRESS_LOG.md`
5. Experiment-08 novelty stop on branch `experiment-08-zero-gap-kane-statistics` before invoking Kane zero/small-gap limits.

Parent research branch:

```text
experiment-09-coherence-selective-photodetection
```

Experiment 09 is a separate paper lineage. Do not mix its collective-coherence theorem into this branch unless a later derivation produces a genuine logical connection.

---

# Founding Gedanken experiment

Reference detector `H` is HgCdTe. Comparator `X` is an unknown passive interband semiconductor whose electronic dispersion may be designed subject to physical consistency.

Start at

```math
T=300\ \mathrm K,
\qquad
\lambda_c=10\ \mu\mathrm m.
```

Then

```math
E_g=\frac{hc}{\lambda_c}\approx0.12398\ \mathrm{eV},
```

```math
k_BT\approx25.85\ \mathrm{meV},
```

```math
\boxed{E_g/(k_BT)\approx4.80.}
```

This ratio is the basic thermal difficulty: a room-temperature LWIR interband gap is only a few thermal energies.

Initially match the two detectors in

```text
cutoff energy;
temperature;
area;
accepted optical etendue;
incident optical environment;
external absorptance spectrum over the task band;
response-time or bandwidth requirement.
```

Perfect contacts and no extrinsic SRH centers may be assumed initially to isolate intrinsic material limits.

---

# First heuristic only

For a conventional nondegenerate 3-D parabolic semiconductor,

```math
n_i=\sqrt{N_cN_v}\exp[-E_g/(2k_BT)],
```

with

```math
N_c\propto g_c(m_e^*T)^{3/2},
\qquad
N_v\propto g_v(m_h^*T)^{3/2}.
```

Hence

```math
n_i\propto
(g_cg_v)^{1/2}
(m_e^*m_h^*)^{3/4}
T^{3/2}
\exp[-E_g/(2k_BT)].
```

At fixed `E_g,T`, this makes low DOS masses and low degeneracy look attractive.

**Do not mistake this for the result.** The optical oscillator strength, thermal DOS, Auger phase space, and response time may not be independently tunable.

---

# Primary comparator — finite-gap massive Dirac/Kane

Use

```math
E_\pm(k)
=\pm\sqrt{\Delta^2+(\hbar vk)^2},
\qquad
\Delta=E_g/2.
```

Near the band edge,

```math
\boxed{m_D=E_g/(2v^2).}
```

The exact 3-D DOS shape is proportional to

```math
g(E)\propto
\frac{|E|\sqrt{E^2-\Delta^2}}
{\hbar^3v^3}.
```

Working hypothesis:

```text
large v
-> smaller thermodynamic DOS scale
while interband velocity matrix elements may remain strong
and Auger phase space may differ qualitatively.
```

This is a hypothesis only. Do not call the massive-Dirac/Kane class optimal unless a constrained proof establishes it.

---

# Experiment-08 boundary — mandatory

Experiment 08 already proved that the shortcut

```math
m^*=E_g/(2v^2)
```

inserted into a nondegenerate parabolic `n_i` formula and then extrapolated to `E_g -> 0` gives the wrong limit for the reduced Kane model.

Its zero-gap novelty path is closed.

Experiment 10 fixes a finite LWIR gap near `0.1 eV` at 300 K and asks a different detector-performance question. Use exact Fermi-Dirac statistics whenever the Maxwell-Boltzmann approximation becomes questionable.

---

# Novelty hazards already identified

The following are established territory and cannot be the paper:

```text
alpha/G_th detector-material merit;
alpha sqrt(tau) detector-material merit;
generic low intrinsic carrier density;
generic radiative detailed balance;
generic Auger suppression by band engineering;
T2SL/quantum-well Auger suppression in general;
zero-gap Kane charge-neutrality theory.
```

Mandatory early references include:

```text
M. Kopytko and A. Rogalski,
Infrared Phys. Technol. 122, 104063 (2022),
DOI 10.1016/j.infrared.2022.104063.

A. Rogalski,
J. Appl. Phys. 137, 170701 (2025),
DOI 10.1063/5.0260949.
```

The potential contribution must derive a more primitive joint constraint from the electronic structure itself.

---

# Detector-quality constraint

Do not optimize asymptotic scalar sensitivity while allowing the detector to become arbitrarily slow.

Carry a finite temporal requirement such as

```math
f_{3\mathrm{dB}}\ge f_0
```

or

```math
\tau_{det}\le\tau_0.
```

A provisional nonradiative-excess ratio is

```math
\Xi_{nr}
=\frac{\Gamma_{nonrad}}
{\Gamma_{rad}+\Gamma_{background}}.
```

Treat this as a bookkeeping idea only until the exact radiative/background fluctuation model is derived.

---

# First hard derivation

Do **not** add Auger yet.

Take two idealized 3-D two-band absorbers with the same finite `E_g`, `T`, optical environment, external absorptance target, and temporal target:

```text
A. parabolic dispersion;
B. massive-Dirac dispersion.
```

Derive enough exact carrier statistics and interband absorption to answer:

> At matched useful absorptance, can the massive-Dirac class have a lower equilibrium carrier population than the parabolic class, or is there an exact compensating DOS/oscillator-strength invariant?

Possible dispositions:

```text
YES:
    identify the surviving electronic-structure degree of freedom and its scaling;

NO:
    derive the invariant/no-go theorem;

CONDITIONAL:
    identify the exact extra microscopic assumption required.
```

Stop at the first nontrivial consequence and immediately compare it with the closest primary literature.

---

# Only after the first hard derivation

If a real degree of freedom survives the matched absorption problem, then add intrinsic Auger generation at the matrix-element/phase-space level rather than as an arbitrary lifetime coefficient.

The eventual target, if the line survives, is something like

```math
\mathcal A(T,\lambda_c,A_0,f_0)
```

—an admissible set of electronic structures satisfying the simultaneous optical, thermal-generation, nonradiative, and temporal constraints.

Possible paper-level outcomes:

```text
broad-class no-go theorem;
exact absorption/DOS invariant;
Auger kinematic escape criterion;
finite-gap admissibility region;
proof that HgCdTe lies unusually near an optimal dispersion class;
or proof that no passive interband material can substantially beat the reference under the matched constraints.
```

None of these is established yet.

---

# NEXT ACTION

Proceed from the two-band matched-absorptance problem only.

Do not search for candidate compounds yet. Do not build a material leaderboard. Do not reopen Experiment 08. Do not draft a paper yet.
