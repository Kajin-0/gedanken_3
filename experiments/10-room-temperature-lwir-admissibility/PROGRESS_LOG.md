# Progress Log — Experiment 10: Room-Temperature LWIR Material Admissibility

## 2026-08-14 — branch initialization

**Scope:** analytical/theoretical only.

### Founding question

Can a first-principles electronic-structure analysis determine what class of LWIR absorber could operate near 300 K with HgCdTe-class or near-HgCdTe-class detector quality while retaining useful temporal response?

### Branch created

```text
experiment-10-room-temperature-lwir-admissibility
```

Parent research branch:

```text
experiment-09-coherence-selective-photodetection
```

The parent was chosen to preserve the latest research-recovery lineage and theoretical-only protocol. Experiment 09 remains a separate paper line and is not modified conceptually by this branch.

### Initial numerical scales

For

```math
T=300\ \mathrm K,
\qquad
\lambda_c=10\ \mu\mathrm m,
```

record

```math
E_g\approx0.12398\ \mathrm{eV},
```

```math
k_BT\approx25.85\ \mathrm{meV},
```

```math
E_g/(k_BT)\approx4.80.
```

### First modeling decision

Do not begin by ranking real materials.

Use a constrained two-detector Gedanken comparison:

```text
H = HgCdTe reference;
X = unknown semiconductor with tunable electronic dispersion.
```

Initially match:

```text
cutoff;
temperature;
area;
optical etendue;
external absorptance spectrum;
optical environment;
response-time/bandwidth target.
```

### First candidate comparison

Compare a conventional parabolic two-band absorber with a finite-gap massive-Dirac/Kane absorber,

```math
E_\pm(k)=\pm\sqrt{(E_g/2)^2+(\hbar vk)^2}.
```

Near the edge,

```math
m_D=E_g/(2v^2).
```

This motivates, but does not establish, a possible low-DOS/high-optical-coupling direction.

### Novelty hazards recorded immediately

The branch explicitly excludes as novelty:

```text
alpha/G_th material figures of merit;
alpha sqrt(tau) material metrics;
generic low-ni arguments;
generic detailed-balance radiative limits;
generic band-engineered Auger suppression;
Experiment-08 zero-gap Kane carrier statistics.
```

Verified early bibliography hazards include:

```text
Kopytko & Rogalski, Infrared Phys. Technol. 122, 104063 (2022)
DOI 10.1016/j.infrared.2022.104063

Rogalski, J. Appl. Phys. 137, 170701 (2025)
DOI 10.1063/5.0260949
```

### Internal branch boundary

Experiment 08 already closed the zero-gap Kane-statistics novelty path. Its retained mathematical results must be respected, especially the noncommuting-limit failure of inserting `m*=E_g/(2v^2)` into a nondegenerate parabolic formula and then taking `E_g -> 0`.

Experiment 10 is finite-gap and detector-performance constrained.

### Immediate next research step

Before Auger and before material-specific complexity, derive the matched optical/statistical comparison:

> At fixed finite `E_g`, `T`, external absorptance, optical environment, and response-time target, can a massive-Dirac absorber have a smaller equilibrium carrier population than a parabolic absorber without paying an exact compensating optical cost?

Possible outcomes:

```text
YES -> identify the surviving free parameter and quantify its leverage;
NO  -> derive the invariant/no-go theorem;
CONDITIONAL -> state the exact missing microscopic assumption.
```

Stop after that first nontrivial consequence and audit it before expanding the model.
