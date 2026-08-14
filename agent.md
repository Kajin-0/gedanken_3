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
2. `experiments/10-room-temperature-lwir-admissibility/KANE_VELOCITY_RESOURCE_BOUND_STEP_2026-08-14.md`
3. `experiments/10-room-temperature-lwir-admissibility/MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`
4. `experiments/10-room-temperature-lwir-admissibility/PROGRESS_LOG.md`
5. founding/history files only as needed.
6. Experiment-08 novelty stop before any zero-gap Kane limit.

## Fixed target

```math
T=300\ \mathrm K,
\qquad
\lambda_c=10\ \mu\mathrm m,
\qquad
E_g=0.1239841984\ \mathrm{eV},
\qquad
E_g/(k_BT)\approx4.796.
```

Research target: a finite-gap band-structure admissibility theorem/bound/escape condition for room-temperature LWIR detector quality, not a materials leaderboard or scalar FOM.

---

# CONTROLLING RESULTS

## 1. Exact massive-Dirac matched-absorptance result

For

```math
H=\hbar v\tau_x\boldsymbol\sigma\cdot\mathbf k+\Delta\tau_z,
\qquad
\Delta=E_g/2,
```

with `N_D` equivalent species,

```math
n_e\propto N_Dv^{-3},
\qquad
\alpha\propto N_Dv^{-1}.
```

Matching ideal single-pass absorptance gives

```math
d\propto v/N_D.
```

Hence

```math
\boxed{
\Sigma_e=n_ed\propto v^{-2},
\qquad
\Sigma_e\text{ independent of }N_D.
}
```

Ideal ballistic crossing time remains

```math
\boxed{\tau_{ball}\propto v^0.}
```

At 10 um / 300 K, the exact finite-gap carrier density is `1.8644x` the simple edge-parabolic estimate. Do not revert to the ordinary parabolic density formula.

## 2. Kane energy form

Use

```math
E_P=2m_0P^2/\hbar^2,
\qquad
v^2=E_P/(3m_0).
```

Therefore

```math
\boxed{\Sigma_e\propto E_P^{-1}.}
```

A factor `Q` column improvement requires `E_P -> Q E_P` and `v -> sqrt(Q) v`.

Reference scale: HgCdTe work near the topological transition reports `v ~ 1.07e6 m/s` and accepted `E_P ~ 18.8 eV`.

## 3. Negative bound results

The following obvious mechanisms do **not** provide a useful material-independent upper bound on large `v`:

```text
multiband k.p effective-mass identity;
global optical f-sum over a fixed photon-energy window;
Kramers-Kronig low-energy dielectric loading;
fixed remote-band separation in energy.
```

Reasoning:

- effective-mass remote-band contributions have opposite denominator signs;
- fixed-energy low-energy Dirac optical spectral weight scales as `1/v`, so large `v` consumes less of the total f-sum;
- detector-required momentum radius at fixed energy scales as `1/v`.

Do not revive these as proposed upper-v no-go mechanisms without a new assumption.

## 4. Conditional microscopic lattice velocity bound

For

```math
H(\mathbf k)=\sum_{\mathbf R}H_{\mathbf R}e^{i\mathbf k\cdot\mathbf R},
```

```math
\hat v_i
=\frac1\hbar\partial_{k_i}H
=\frac{i}{\hbar}\sum_{\mathbf R}R_iH_{\mathbf R}e^{i\mathbf k\cdot\mathbf R}.
```

Thus

```math
\boxed{
\|\hat v_i\|
\le
\frac1\hbar\sum_{\mathbf R}|R_i|\|H_{\mathbf R}\|
\equiv V_i^{hop}.
}
```

Every group/interband velocity matrix element is bounded by this operator norm. Therefore, conditionally,

```math
\boxed{v\le V_{hop}.}
```

The ultraviolet resource is the hopping-range-weighted norm

```math
\mathcal J_i=\sum_R|R_i|\|H_R\|.
```

Without bounding this resource, no numerical material-independent upper `v` follows from the continuum theory.

## 5. First explicit admissibility inequality

For matched ideal absorptance,

```math
\Sigma_e=C(T,E_g,A,r,n_b)/v^2.
```

Hence

```math
\boxed{
\Sigma_e\ge C/V_{hop}^2.
}
```

For the existing witness

```text
T=300 K
lambda_c=10 um
r=1.2
A=0.90
n_b=3.5
```

```math
C=1.06668\times10^{29}\ \mathrm{m^{-2}(m/s)^2}.
```

This is a conditional microscopic-resource detector bound, not a universal semiconductor constant.

---

# Novelty boundary

Known ingredients are not novelty:

```text
Kane k.p and E_P;
3-D Dirac optical conductivity;
HgCdTe Kane velocity;
effective-mass sums;
optical f-sum rules;
Wannier/tight-binding Bloch Hamiltonians;
alpha/G_th and alpha sqrt(tau) detector-material metrics;
generic Auger band engineering;
Experiment-08 zero-gap Kane statistics.
```

Do not claim novelty for the operator-norm velocity bound itself.

Current disposition:

```text
POSSIBLE DETECTOR-SPECIFIC SYNTHESIS / NOVELTY NOT ESTABLISHED.
```

---

# DO NOT DO

Do not rank candidate compounds yet. Do not draft a paper. Do not reopen Experiment 08. Do not insert an empirical Auger coefficient as a free material parameter.

# NEXT ACTION

The high-`v` matched-absorptance lever has survived the obvious generic cancellation attacks.

Proceed to the first intrinsic nonradiative mechanism:

> For the finite-gap massive-Dirac/Kane family, derive the kinematically allowed Auger phase space from energy and crystal-momentum conservation. Determine how the threshold/phase space scales with `v`, `E_g`, and the minimum additional asymmetry or remote-band parameter, and whether the `Sigma_e ~ v^-2` advantage survives.

Start with the simplest Coulomb process and exact kinematics before evaluating matrix elements or rates.
