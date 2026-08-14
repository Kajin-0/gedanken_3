# Agent recovery entrypoint

Read `AGENTS.md` first, then this file. Do not infer research chronology from `main` alone.

## Hard global constraint — ANALYTICAL / THEORETICAL ONLY

The project goal is a defensible theoretical photodetector result grown from a simple Gedanken experiment. Preserve failed/corrected paths and do not use novelty/priority language without a dedicated audit.

---

# ACTIVE FRONTIER — Experiment 10

Branch:

```text
experiment-10-room-temperature-lwir-admissibility
```

Working research-line title only:

> **Room-temperature LWIR band-structure admissibility**

No manuscript is justified yet.

## Read in this order

1. `experiments/10-room-temperature-lwir-admissibility/CURRENT_STATE.md`
2. `experiments/10-room-temperature-lwir-admissibility/MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`
3. `experiments/10-room-temperature-lwir-admissibility/PROGRESS_LOG.md`
4. `experiments/10-room-temperature-lwir-admissibility/FOUNDING_GEDANKEN_2026-08-14.md`
5. `experiments/10-room-temperature-lwir-admissibility/PRIOR_BRANCH_BOUNDARY_2026-08-14.md`
6. Experiment-08 novelty stop before invoking zero/small-gap Kane limits.

Parent branch `experiment-09-coherence-selective-photodetection` is a separate paper lineage. Do not mix its collective-coherence theorem into Experiment 10 without a genuine later derivation.

---

# Fixed target

```math
T=300\ \mathrm K,
\qquad
\lambda_c=10\ \mu\mathrm m,
```

```math
E_g=0.1239841984\ \mathrm{eV},
\qquad
k_BT=0.0258519998\ \mathrm{eV},
```

```math
\boxed{E_g/(k_BT)\approx4.796.}
```

Research objective:

> Determine which electronic-structure constraints a passive LWIR interband absorber must satisfy to approach HgCdTe-class intrinsic detector quality near 300 K while retaining finite useful temporal response.

The target is a band-structure theorem/bound/invariant/escape condition, not a materials list and not a scalar FOM.

---

# FIRST HARD DERIVATION — CLOSED

Use the intrinsic isotropic massive-Dirac Hamiltonian

```math
H
=\hbar v\tau_x\boldsymbol\sigma\cdot\mathbf k
+\Delta\tau_z,
\qquad
\Delta=E_g/2.
```

Allow `N_D` equivalent Dirac species.

## Exact carrier density

At `mu=0`,

```math
\boxed{
n_e
=\frac{N_D}{\pi^2}
\left(\frac{k_BT}{\hbar v}\right)^3
F_2(\delta),
\qquad
\delta=\Delta/(k_BT),
}
```

with

```math
F_2(\delta)
=\int_0^\infty
\frac{x^2dx}{e^{\sqrt{x^2+\delta^2}}+1}.
```

Thus

```math
\boxed{n_e\propto N_Dv^{-3}.}
```

At the fixed target,

```text
delta = 2.39796146
F_2 = 0.7887622040
```

and for `N_D=1`, `v=1e6 m/s`,

```math
n_e=4.8421\times10^{15}\ \mathrm{cm^{-3}}.
```

## Important finite-gap correction

The edge-parabolic mass is

```math
m_D=\Delta/v^2.
```

At 10 um / 300 K,

```math
\boxed{
n_e^{Dirac}/n_e^{edge-parabolic}\approx1.8644.
}
```

The exact finite-gap nonparabolicity is therefore material at the target. Do not revert to the ordinary edge-parabolic density formula for quantitative work.

---

# Exact interband absorption scaling

The clean-limit conductivity derived in the controlling file is

```math
\boxed{
\sigma_1(\omega)
=
\frac{N_De^2\omega}{12\pi\hbar v}
\left(1+\frac{2\Delta^2}{\hbar^2\omega^2}\right)
\sqrt{1-\frac{4\Delta^2}{\hbar^2\omega^2}}
\tanh\left(\frac{\hbar\omega}{4k_BT}\right).
}
```

At fixed normalized photon energy,

```math
\boxed{\alpha\propto N_Dv^{-1}.}
```

This inverse-velocity 3-D Dirac optical-conductivity scaling is established prior art.

For ideal single-pass absorptance

```math
A=1-e^{-\alpha d},
```

matched optical depth requires

```math
\boxed{d\propto v/N_D.}
```

---

# HEADLINE FIRST RESULT

Define the equilibrium electron column per detector area

```math
\Sigma_e=n_ed.
```

Then

```math
\boxed{
\Sigma_e\propto v^{-2},
\qquad
\Sigma_e\text{ is independent of }N_D.
}
```

Interpretation within the exact stated toy model:

```text
larger v lowers the thermodynamic DOS much faster than it lowers optical absorption;
there is no exact DOS-versus-absorption cancellation;
equivalent valley/species degeneracy is not a lever for the matched-absorptance carrier column.
```

Because the absorption spectrum factorizes as

```math
\alpha(\omega)=\frac{N_D}{v}\mathcal F(\omega;E_g,T,n_b),
```

choosing `d~v/N_D` matches the entire ideal single-pass absorptance spectral shape, not just one frequency, as long as the background optical constants remain fixed.

---

# Temporal stress test

At

```math
r=\hbar\omega/E_g>1,
```

the photoexcited group speed is

```math
u_\omega=v\sqrt{1-r^{-2}}.
```

Since `d~v`,

```math
\boxed{\tau_{ball}=d/u_\omega\propto v^0.}
```

Thus the simplest absorptance-versus-ballistic-transit constraint does not erase the `v^-2` carrier-column benefit.

Do **not** reinterpret this as a full detector bandwidth theorem; scattering, diffusion, RC, field dependence, recombination, and contacts are absent.

---

# Quantitative witness

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

So `v -> 2v` produces

```text
n_e -> n_e/8
d -> 2d
Sigma_e -> Sigma_e/4
tau_ball -> unchanged.
```

---

# Planned parabolic comparator — corrected

A generic parabolic model that treats

```text
m_e,
m_h,
p_cv or v_cv
```

as independent is underconstrained and cannot support a first-principles bound.

If a parabolic edge model is derived from a self-consistent two-band `k.p` Hamiltonian, the same interband velocity `v` controls both its optical matrix element and

```math
m_D=\Delta/v^2,
```

so that model is simply the low-`k` limit of the massive-Dirac system, not an independent architecture.

Current disposition:

```text
CROSS-CLASS PARABOLIC COMPARISON = CONDITIONAL.
```

A fair comparison requires multiband `k.p`, oscillator-strength sum rules, and/or remote-band constraints.

---

# Prior-art boundary

Mandatory established comparators include:

```text
Tabert & Carbotte, Phys. Rev. B 93, 085442 (2016),
DOI 10.1103/PhysRevB.93.085442;

Malcolm & Nicol, Phys. Rev. B 92, 035118 (2015),
DOI 10.1103/PhysRevB.92.035118;

Ezawa, Phys. Rev. B 110, 195437 (2024),
DOI 10.1103/PhysRevB.110.195437;

Kopytko & Rogalski, Infrared Phys. Technol. 122, 104063 (2022);
Rogalski, J. Appl. Phys. 137, 170701 (2025).
```

Known ingredients are not novelty:

```text
3-D Dirac optical conductivity;
inverse-v optical scaling;
Kane optical physics;
alpha/G_th and alpha sqrt(tau) material metrics;
generic low-ni reasoning;
radiative detailed balance;
generic band-engineered Auger suppression;
Experiment-08 zero-gap Kane statistics.
```

A focused 2026-08-14 search did not find a direct prior statement of the complete matched-absorptance result

```math
\Sigma_e\propto v^{-2}
```

with equivalent-species cancellation and ballistic-transit invariance.

Disposition remains

```text
POSSIBLE USEFUL SYNTHESIS / NOVELTY NOT ESTABLISHED.
```

---

# DO NOT DO NEXT

Do not add Auger yet. Do not rank candidate compounds. Do not draft a paper. Do not reopen Experiment 08.

# NEXT ACTION

Resolve the microscopic freedom of `v`:

> Once full multiband `k.p` and oscillator-strength constraints are imposed at fixed finite `E_g`, is `v` genuinely a free material-design lever, or is there a microscopic upper bound/tradeoff that limits the `Sigma_e ~ v^-2` gain?

If a strict bound exists, derive it. If no universal bound exists, identify the minimum additional material parameters that control the admissible `v` range. Only after that should Auger phase space be introduced.
