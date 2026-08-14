# Progress Log — Experiment 10: Room-Temperature LWIR Material Admissibility

## 2026-08-14 — branch initialization

Established the fixed target

```math
T=300\ \mathrm K,
\qquad
\lambda_c=10\ \mu\mathrm m,
\qquad
E_g\approx0.12398\ \mathrm{eV},
\qquad
E_g/(k_BT)\approx4.80.
```

Created branch

```text
experiment-10-room-temperature-lwir-admissibility
```

with the objective of deriving a finite-gap band-structure admissibility theorem or no-go result rather than ranking known materials.

Novelty hazards excluded at founding: generic `alpha/G_th`, `alpha sqrt(tau)`, low-`n_i` arguments, radiative detailed balance, generic Auger suppression, and Experiment-08 zero-gap Kane statistics.

---

## 2026-08-14 — matched massive-Dirac absorptance

Controlling file:

`MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`

For the intrinsic isotropic massive-Dirac model

```math
H=\hbar v\tau_x\boldsymbol\sigma\cdot\mathbf k+\Delta\tau_z,
\qquad
\Delta=E_g/2,
```

with `N_D` equivalent species, exact finite-gap statistics give

```math
n_e\propto N_Dv^{-3}.
```

The clean interband optical conductivity gives

```math
\alpha\propto N_Dv^{-1}.
```

Matching ideal single-pass absorptance requires

```math
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

The ideal ballistic crossing time satisfies

```math
\tau_{ball}\propto v^0.
```

The generic parabolic comparator was rejected as underconstrained unless its masses and optical matrix elements are derived from a common microscopic Hamiltonian.

At 10 um / 300 K, the exact Dirac carrier density is `1.8644x` the edge-parabolic estimate, so exact finite-gap nonparabolicity must be retained.

Disposition:

```text
MATCHED-ABSORPTANCE HIGH-v LEVER SURVIVES.
NOVELTY NOT ESTABLISHED.
```

---

## 2026-08-14 — Kane velocity freedom and microscopic resource bound

Controlling file:

`KANE_VELOCITY_RESOURCE_BOUND_STEP_2026-08-14.md`

### Kane-energy interpretation

Using

```math
E_P=2m_0P^2/\hbar^2,
\qquad
v^2=E_P/(3m_0),
```

the matched column law becomes

```math
\boxed{\Sigma_e\propto E_P^{-1}.}
```

An improvement factor `Q` requires

```math
E_P=Q E_{P,ref},
\qquad
v=\sqrt Q\,v_{ref}.
```

### Generic upper-bound attempts that failed

1. **Multiband effective-mass identity:** remote bands above and below the target band enter with opposite denominator signs, so the identity does not isolate a positive upper bound on the fundamental interband momentum matrix element.

2. **Global optical f-sum:** over a fixed detector-relevant photon-energy interval,

```math
\int\sigma_1d\omega\propto v^{-1}.
```

Increasing `v` therefore uses less low-energy optical spectral weight. The global sum does not upper-bound large `v`.

3. **Remote-band energy separation:** at fixed required quasiparticle energy,

```math
k_req\propto v^{-1}.
```

A fixed remote-band energy limits the valid energy interval but does not by itself upper-bound `v`.

Disposition:

```text
NO MATERIAL-INDEPENDENT UPPER-v BOUND FROM THESE LOW-ENERGY CONSTRAINTS.
```

### Conditional microscopic lattice bound

For

```math
H(\mathbf k)=\sum_{\mathbf R}H_{\mathbf R}e^{i\mathbf k\cdot\mathbf R},
```

```math
\hat v_i
=\hbar^{-1}\partial_{k_i}H
=\frac{i}{\hbar}\sum_{\mathbf R}R_iH_{\mathbf R}e^{i\mathbf k\cdot\mathbf R}.
```

The operator norm gives

```math
\boxed{
\|\hat v_i\|
\le
\frac1\hbar\sum_{\mathbf R}|R_i|\|H_{\mathbf R}\|
\equiv V_i^{hop}.
}
```

Therefore the Dirac/Kane velocity is conditionally bounded by the microscopic hopping-range resource:

```math
\boxed{v\le V_{hop}.}
```

Combining with the matched-absorptance result yields

```math
\boxed{
\Sigma_e\ge C(T,E_g,A,r,n_b)/V_{hop}^2.
}
```

This is the first explicit microscopic-resource-conditioned admissibility inequality in Experiment 10.

For the prior witness (`T=300 K`, `lambda_c=10 um`, `r=1.2`, `A=0.90`, `n_b=3.5`),

```math
C=1.06668\times10^{29}\ \mathrm{m^{-2}(m/s)^2}.
```

So

```text
V_hop = 1e6 m/s -> Sigma_e >= 1.067e13 cm^-2
V_hop = 2e6 m/s -> Sigma_e >= 2.667e12 cm^-2
V_hop = 3e6 m/s -> Sigma_e >= 1.185e12 cm^-2
```

### Literature status

Checked primary literature on HgCdTe Kane velocity, `k.p` effective masses, optical sum rules, and Bloch/Wannier Hamiltonians. All ingredients are established. The detector-specific combination remains a possible synthesis only.

```text
NOVELTY NOT ESTABLISHED.
```

### Next frontier

The high-`v` lever has survived the obvious optical/DOS, ballistic-time, effective-mass, global-sum-rule, and remote-band-energy cancellation attempts.

Next step:

> Derive the kinematically allowed intrinsic Auger phase space for the same finite-gap family from energy and crystal-momentum conservation, without inserting an empirical Auger coefficient as an independent parameter.
