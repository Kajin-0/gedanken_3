# Agent recovery entrypoint

Read `AGENTS.md` first, then this file. Do not infer chronology from `main` alone.

## Hard scope

Experiment 10 is analytical/theoretical only. Preserve negative/corrected paths. Do not use novelty or priority language without a dedicated audit.

# ACTIVE FRONTIER — Experiment 10

Branch:

```text
experiment-10-room-temperature-lwir-admissibility
```

No manuscript is justified yet.

## Read in this order

1. `experiments/10-room-temperature-lwir-admissibility/CURRENT_STATE.md`
2. `experiments/10-room-temperature-lwir-admissibility/AUGER_KINEMATIC_CLOSURE_STEP_2026-08-14.md`
3. `experiments/10-room-temperature-lwir-admissibility/KANE_VELOCITY_RESOURCE_BOUND_STEP_2026-08-14.md`
4. `experiments/10-room-temperature-lwir-admissibility/MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`
5. `experiments/10-room-temperature-lwir-admissibility/PROGRESS_LOG.md`
6. founding/history files only as needed.

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

For the exact finite-gap massive-Dirac model,

```math
n_e\propto N_Dv^{-3},
\qquad
\alpha\propto N_Dv^{-1},
\qquad
d\propto v/N_D.
```

Therefore

```math
\boxed{
\Sigma_e=n_ed\propto v^{-2},
\qquad
\Sigma_e\text{ independent of }N_D.
}
```

Ideal ballistic crossing time remains `v^0`.

## 2. Microscopic velocity resource

Using `v^2=E_P/(3m0)`, `Sigma_e ~ E_P^-1`.

No generic upper-`v` bound was obtained from effective-mass sums, global optical f-sum over a fixed detector energy window, or remote-band energy separation alone.

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

strict subadditivity gives

```math
\varepsilon(\mathbf p+\mathbf q)
<\varepsilon(\mathbf p)+\varepsilon(\mathbf q).
```

Therefore normal-momentum impact ionization

```text
e_0 -> e_1 + e_2 + h_3
```

cannot satisfy energy and momentum conservation simultaneously. The inverse phononless `eeh` Auger channel has empty exact kinematic support; the `hhe` mirror is also closed under particle-hole symmetry.

The exact minimum mismatch at hot energy `E` is

```math
\boxed{
\Delta_A(E)=\sqrt{E^2+2E_g^2}-E.
}
```

At fixed `E/Eg`, `v` cancels completely.

Hence:

```text
large v
    -> thermodynamic matched-column lever;

particle-hole-symmetric relativistic dispersion
    -> Auger kinematic closure.
```

These are distinct resources. Do not say high `v` itself closes Auger.

At 10 um / 300 K:

```text
E/Eg    Delta_A (meV)    Delta_A/kBT
1.5       69.62             2.69
2.0       55.73             2.16
3.0       39.26             1.52
5.0       24.32             0.94
10.0      12.34             0.48
```

Massless limit: closure becomes marginal/collinear rather than strict.

---

# Prior-art boundary

Broad Dirac/symmetric-dispersion Auger suppression is established and unavailable as novelty. Mandatory comparators:

```text
Alymov et al., PRB 97, 205411 (2018);
Alymov et al., ACS Photonics 7, 98–104 (2020);
But et al., Nature Photonics 13, 783–787 (2019);
Combescot & Combescot, PRB 37, 8781 (1988).
```

Real bulk HgCdTe is not the exact two-band symmetric model; heavy-hole/remote bands, disorder, phonons, linewidth, and many-body effects reopen channels.

Current disposition:

```text
POSSIBLE DETECTOR-SPECIFIC SYNTHESIS / NOVELTY NOT ESTABLISHED.
```

---

# DO NOT DO

Do not insert an empirical Auger coefficient. Do not rank candidate compounds. Do not draft a paper. Do not claim bulk HgCdTe has zero Auger recombination.

# NEXT ACTION

Add the smallest controlled particle-hole asymmetry and derive the exact Auger reopening boundary. Preferred model:

```math
E_\pm(k)=Dk^2\pm\sqrt{\Delta^2+(\hbar vk)^2}.
```

Determine the dimensionless asymmetry needed to overcome

```math
\Delta_A(E)=\sqrt{E^2+2E_g^2}-E
```

over the thermally relevant finite-energy window at `E_g/kBT ~= 4.8`.

Only after that boundary is derived should Coulomb matrix elements and finite rates be introduced.
