# Agent recovery entrypoint

Read `AGENTS.md` first, then this file. Do not infer chronology from `main` alone.

## Hard scope

Experiment 10 is analytical/theoretical only. Preserve failed/corrected/conditional paths. Do not use novelty or priority language without a dedicated audit.

# ACTIVE FRONTIER — Experiment 10

Branch:

```text
experiment-10-room-temperature-lwir-admissibility
```

No manuscript is justified yet.

## Read in this order

1. `experiments/10-room-temperature-lwir-admissibility/CURRENT_STATE.md`
2. `experiments/10-room-temperature-lwir-admissibility/AUGER_ASYMMETRY_REOPENING_STEP_2026-08-14.md`
3. `experiments/10-room-temperature-lwir-admissibility/AUGER_KINEMATIC_CLOSURE_STEP_2026-08-14.md`
4. `experiments/10-room-temperature-lwir-admissibility/KANE_VELOCITY_RESOURCE_BOUND_STEP_2026-08-14.md`
5. `experiments/10-room-temperature-lwir-admissibility/MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`
6. `experiments/10-room-temperature-lwir-admissibility/PROGRESS_LOG.md`

Fixed target:

```math
T=300\ \mathrm K,
\qquad
\lambda_c=10\ \mu\mathrm m,
\qquad
E_g=0.1239841984\ \mathrm{eV},
\qquad
E_g/(k_BT)\approx4.796.
```

---

# CONTROLLING RESULTS

## 1. Matched absorptance

For the exact finite-gap massive-Dirac family,

```math
n_e\propto N_Dv^{-3},
\qquad
\alpha\propto N_Dv^{-1},
\qquad
d\propto v/N_D,
```

therefore

```math
\boxed{
\Sigma_e=n_ed\propto v^{-2},
\qquad
\Sigma_e\text{ independent of }N_D.
}
```

Ideal ballistic crossing time remains `v^0`.

## 2. Microscopic velocity resource

No generic upper-`v` bound was obtained from low-energy effective-mass sums, a global optical f-sum over a fixed detector energy window, or remote-band energy separation alone.

For a Wannier Hamiltonian,

```math
\boxed{
\|\hat v_i\|
\le\frac1\hbar\sum_R|R_i|\|H_R\|
\equiv V_i^{hop},
}
```

so conditionally

```math
\boxed{v\le V_{hop}}
```

and

```math
\boxed{\Sigma_e\ge C/V_{hop}^2.}
```

## 3. Exact symmetric-Dirac Auger closure

For

```math
\varepsilon(k)=\sqrt{\Delta^2+(\hbar vk)^2},
\qquad\Delta=E_g/2>0,
```

normal-momentum phononless `eeh` and `hhe` Auger channels have empty exact kinematic support in the particle-hole-symmetric two-band model.

The exact mismatch is

```math
\boxed{
\Delta_A(E)=\sqrt{E^2+2E_g^2}-E.
}
```

At fixed `E/Eg`, `v` cancels. High `v` and symmetry are distinct resources.

## 4. Finite particle-hole asymmetry reopening

Add

```math
E_\pm(k)=Dk^2\pm\sqrt{\Delta^2+(\hbar vk)^2}.
```

Define

```math
\beta=D\Delta/(\hbar^2v^2),
```

and

```math
\boxed{
\mathcal A_m
=\frac{|m_e^{-1}-m_h^{-1}|}
{m_e^{-1}+m_h^{-1}}
=2|\beta|.
}
```

The exact reduced-model reopening boundary is

```math
\boxed{
\beta_c(q_0)
=
\min_{0\le x\le q_0/2}
\frac{2s(x)+s(q_0-2x)-s(q_0)}
{2(q_0-x)^2},
\qquad s(q)=\sqrt{1+q^2}.
}
```

Weak-asymmetry asymptotic:

```math
\boxed{
\beta_c\sim4/q_{th}^3,
\qquad
q_{th}\sim(4/|\beta|)^{1/3}.
}
```

Therefore

```math
\boxed{
K_{th}\sim E_g\mathcal A_m^{-1/3}.
}
```

At the fixed 10-um / 300-K target:

```text
A_m      K_th/kBT
0.40       5.873
0.20       7.536
0.10       9.470
0.04      12.848
0.02      16.273
0.01      20.675
```

To place the direct-channel threshold above `10 kBT`, the exact toy model requires approximately

```math
\boxed{\mathcal A_m\lesssim0.0848.}
```

Do not convert this into a universal real-material edge-mass rule. The actual requirement is small finite-momentum electron-hole dispersion asymmetry over the Auger-active window.

Reproducible script:

`experiments/10-room-temperature-lwir-admissibility/numerics/auger_asymmetry_threshold.py`

---

# Prior-art boundary

Broad Dirac/symmetric-dispersion Auger suppression and large Auger thresholds near Dirac-like HgCdTe-QW regimes are established. Mandatory adjacent work includes Alymov et al. PRB 2018 and ACS Photonics 2020, Aleshkin et al. JPCM 2019, Morozov et al. ACS Photonics 2021, and classical threshold/anisotropy work.

The cube-root law is retained as a reduced-model analytical result only.

```text
NOVELTY NOT ESTABLISHED.
```

Real bulk HgCdTe is not the exact two-band model; heavy-hole/remote bands, phonons, disorder, linewidth, and many-body effects can reopen channels.

---

# DO NOT DO

Do not rank candidate compounds. Do not insert a phenomenological Auger coefficient and declare closure. Do not draft a paper yet.

# NEXT ACTION

Retain the exact threshold and derive the **leading near-threshold thermal/phase-space scaling** of the direct Auger rate with the minimum screened-Coulomb structure.

Question:

> Does the thresholded rate combine with `Sigma_e ~ v^-2` into a detector-level room-temperature admissibility inequality whose dominant dependence is fixed by band structure before interaction-prefactor details enter?

Separate universal threshold exponents from model-dependent Coulomb amplitude/screening.
