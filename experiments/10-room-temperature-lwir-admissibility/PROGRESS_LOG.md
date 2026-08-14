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

---

## 2026-08-14 — first hard derivation: matched massive-Dirac absorptance

Controlling derivation:

`MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`

### Exact finite-gap carrier statistics

For

```math
H=\hbar v\tau_x\boldsymbol\sigma\cdot\mathbf k+\Delta\tau_z,
\qquad
\Delta=E_g/2,
```

with `N_D` equivalent four-component Dirac species and intrinsic `mu=0`, derived

```math
n_e
=\frac{N_D}{\pi^2}
\left(\frac{k_BT}{\hbar v}\right)^3
F_2(\Delta/k_BT).
```

Therefore

```math
n_e\propto N_Dv^{-3}.
```

At the target `10 um / 300 K`,

```text
delta = 2.39796146
F_2 = 0.7887622040
```

and for `N_D=1`, `v=1e6 m/s`,

```math
n_e=4.8421\times10^{15}\ \mathrm{cm^{-3}}.
```

### Parabolic approximation stress

Using the edge mass

```math
m_D=\Delta/v^2
```

in the nondegenerate parabolic density gives

```math
n_e^{Dirac}/n_e^{par}=1.8644.
```

The exact finite-gap nonparabolicity is therefore already important at the nominal LWIR/room-temperature target. The error is not mainly due to Fermi versus Maxwell-Boltzmann occupancy: retaining the exact Dirac dispersion but using MB occupation changes the integral by only about `2.35%`.

### Exact clean-limit interband optical scaling

Derived

```math
\sigma_1(\omega)
=
\frac{N_De^2\omega}{12\pi\hbar v}
\left(1+\frac{2\Delta^2}{\hbar^2\omega^2}\right)
\sqrt{1-\frac{4\Delta^2}{\hbar^2\omega^2}}
\tanh\left(\frac{\hbar\omega}{4k_BT}\right),
```

so in the weak-loss bulk propagation limit

```math
\alpha\propto N_Dv^{-1}.
```

The underlying inverse-velocity 3-D Dirac optical-conductivity scaling is established prior art.

### New combined model result

For matched single-pass absorptance,

```math
A=1-e^{-\alpha d},
```

fixed optical depth requires

```math
d\propto v/N_D.
```

Therefore the equilibrium carrier column

```math
\Sigma_e=n_ed
```

obeys

```math
\boxed{
\Sigma_e\propto v^{-2},
\qquad
\Sigma_e\text{ independent of }N_D.
}
```

This answers the founding question **YES within the ideal massive-Dirac family**: the low-DOS advantage is not exactly canceled by the weaker absorption.

Equivalent species/valley degeneracy is not a thermal-column lever in this restricted model because its effects on density and absorption cancel after thickness matching.

### Temporal stress

At normalized photon energy `r=hbar omega/Eg`,

```math
u_\omega=v\sqrt{1-r^{-2}}.
```

Since `d~v`, the ideal ballistic crossing time satisfies

```math
\tau_{ball}=d/u_\omega\propto v^0.
```

Thus the simplest absorption-versus-transit-speed tradeoff does not cancel the `v^-2` column benefit.

### Numerical witness

For

```text
r = 1.2
n_b = 3.5
N_D = 1
A = 0.90
```

```text
v (m/s)       n_e (cm^-3)      alpha (cm^-1)    d_90 (um)    Sigma_e (cm^-2)    tau_ball (ps)
5.0e5         3.874e16          2090.5            11.015       4.267e13            39.85
1.0e6         4.842e15          1045.2            22.029       1.067e13            39.85
2.0e6         6.053e14           522.6            44.059       2.667e12            39.85
```

Factor-of-two increase in `v` gives

```text
8x lower bulk carrier density;
2x thicker absorber;
4x lower carrier column;
no ideal ballistic-time penalty.
```

### Important correction to the planned comparator

A generic parabolic model with independently adjustable masses and optical matrix elements is underconstrained. If it is made microscopically self-consistent through the same two-band `k.p` coupling, its band-edge parabolic form is simply the low-`k` limit of the massive-Dirac model.

Therefore the cross-class comparison is now labeled

```text
CONDITIONAL:
    full multiband k.p / oscillator-strength / sum-rule constraints are required
    before a parabolic-vs-Dirac material theorem is meaningful.
```

### Focused prior-art screen

Checked primary literature on 3-D Dirac/Kane optical conductivity and detector-material figures of merit. The optical pieces are clearly established. No direct match was found in the focused screen for the combined matched-absorptance statement

```math
\Sigma_e\propto v^{-2}
```

plus equivalent-species cancellation and ballistic-transit invariance.

Disposition remains

```text
POSSIBLE USEFUL SYNTHESIS / NOVELTY NOT ESTABLISHED.
```

### Hard stop after first consequence

Per protocol, Auger is **not** added yet.

Single next question:

> Once multiband `k.p` and oscillator-strength constraints are imposed at fixed finite `E_g`, is `v` genuinely a free design lever, or is there a microscopic upper bound/tradeoff that limits the `Sigma_e ~ v^-2` gain?
