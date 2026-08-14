# Current State — Experiment 10: Room-Temperature LWIR Material Admissibility

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** **MATCHED-ABSORPTANCE LEVER SURVIVES / NO GENERIC UPPER-v BOUND FROM LOW-ENERGY SUM RULES / CONDITIONAL MICROSCOPIC LATTICE ADMISSIBILITY BOUND DERIVED / NOVELTY NOT ESTABLISHED / NO MANUSCRIPT YET**

## Research objective

Derive, from first principles, the electronic-structure conditions a passive LWIR interband absorber must satisfy to approach HgCdTe-class intrinsic detector quality near 300 K without sacrificing useful temporal response.

This is a finite-gap band-structure admissibility problem, not a materials leaderboard and not a new scalar figure of merit.

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

## Read first

1. `KANE_VELOCITY_RESOURCE_BOUND_STEP_2026-08-14.md`
2. `MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`
3. `PROGRESS_LOG.md`
4. founding/history files only as needed.

---

# Result 1 — matched-absorptance massive-Dirac lever

For

```math
H=\hbar v\tau_x\boldsymbol\sigma\cdot\mathbf k+\Delta\tau_z,
\qquad
\Delta=E_g/2,
```

with `N_D` equivalent Dirac species, exact finite-gap statistics give

```math
n_e
=\frac{N_D}{\pi^2}
\left(\frac{k_BT}{\hbar v}\right)^3F_2(\Delta/k_BT),
```

so

```math
n_e\propto N_Dv^{-3}.
```

The clean interband optical conductivity gives

```math
\alpha\propto N_Dv^{-1}.
```

For matched ideal single-pass absorptance,

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

The low-DOS advantage is not exactly canceled by reduced optical absorption inside this model.

At fixed normalized photon energy, the ideal ballistic crossing time remains

```math
\boxed{\tau_{ball}\propto v^0.}
```

because both absorber thickness and photoexcited group speed scale linearly with `v`.

At the actual 10-um / 300-K target, the exact finite-gap carrier density is about `1.8644x` the edge-parabolic estimate, so the simple parabolic density approximation is not quantitatively adequate.

---

# Result 2 — Kane energy resource interpretation

Using the simplified Kane normalization

```math
E_P=\frac{2m_0P^2}{\hbar^2},
```

```math
\boxed{v^2=E_P/(3m_0).}
```

Hence

```math
\boxed{\Sigma_e\propto E_P^{-1}.}
```

An improvement factor `Q` in matched thermal carrier column requires

```math
E_P=Q E_{P,ref},
\qquad
v=\sqrt Q\,v_{ref}.
```

Reference scales:

```text
v = 1.0e6 m/s  -> E_P = 17.06 eV
v = 1.07e6 m/s -> E_P = 19.53 eV
v = 2.0e6 m/s  -> E_P = 68.23 eV
v = 3.0e6 m/s  -> E_P = 153.51 eV
```

HgCdTe magneto-optical work reports a Kane velocity near `1.07e6 m/s` and uses the accepted `E_P ~ 18.8 eV` scale near the topological transition. This is a reference point, not a theoretical upper bound.

---

# Result 3 — generic low-energy constraints do NOT upper-bound large v

## Multiband k.p effective-mass identity

The band-edge inverse-mass tensor contains the signed remote-band sum

```math
\left(m_n^{-1}\right)_{ij}
=\frac{\delta_{ij}}{m_0}
+\frac{2}{m_0^2}
\sum_{m\ne n}
\frac{\langle n|p_i|m\rangle\langle m|p_j|n\rangle}
{E_n-E_m}.
```

Bands above and below the target band enter with opposite denominator signs. Therefore a finite effective mass does not isolate a positive oscillator-strength budget that universally upper-bounds the fundamental interband `P`.

Disposition:

```text
NO MATERIAL-INDEPENDENT UPPER-v BOUND FROM EFFECTIVE-MASS IDENTITY ALONE.
```

## Optical f-sum

For any detector-relevant **fixed photon-energy interval**,

```math
W_{12}=\int_{\omega_1}^{\omega_2}\sigma_1(\omega)d\omega
\propto v^{-1}.
```

Thus increasing `v` uses **less** low-energy optical spectral weight. A global positive optical sum rule does not obstruct large `v`; if anything, it can constrain an excessively small `v` for a specified low-energy sector.

A fixed momentum cutoff gives different scaling, but that is an additional ultraviolet assumption and is not imposed by the detector task.

## Remote-band energy

For fixed required quasiparticle energy `E_req`,

```math
k_req
=\frac{\sqrt{E_req^2-\Delta^2}}{\hbar v}
\propto v^{-1}.
```

A fixed remote-band separation in energy therefore limits the valid energy window but does not itself upper-bound `v`.

---

# Result 4 — conditional microscopic lattice velocity bound

Write a translationally invariant Wannier/tight-binding Hamiltonian

```math
H(\mathbf k)=\sum_{\mathbf R}H_{\mathbf R}e^{i\mathbf k\cdot\mathbf R}.
```

Then

```math
\hat v_i(\mathbf k)
=\frac{1}{\hbar}\frac{\partial H}{\partial k_i}
=\frac{i}{\hbar}
\sum_{\mathbf R}R_iH_{\mathbf R}e^{i\mathbf k\cdot\mathbf R}.
```

The operator norm gives

```math
\boxed{
\|\hat v_i(\mathbf k)\|
\le
\frac{1}{\hbar}
\sum_{\mathbf R}|R_i|\,\|H_{\mathbf R}\|
\equiv V_i^{hop}.
}
```

Every group-velocity expectation and interband velocity matrix element is bounded by this norm. Therefore an isotropic Kane/Dirac velocity satisfies, conditionally on the microscopic hopping resource,

```math
\boxed{v\le V_{hop}.}
```

The primitive resource is

```math
\boxed{
\mathcal J_i
=\sum_{\mathbf R}|R_i|\,\|H_{\mathbf R}\|,
\qquad
V_i^{hop}=\mathcal J_i/\hbar.
}
```

Large `v` requires large hopping amplitude, long hopping range, or both.

There is no numerical material-independent ceiling until this ultraviolet resource is itself bounded.

---

# First explicit admissibility inequality

For the clean matched-absorptance model,

```math
\Sigma_e
=\frac{C(T,E_g,A,r,n_b)}{v^2}.
```

Combining with the microscopic velocity resource gives

```math
\boxed{
\Sigma_e
\ge
\frac{C(T,E_g,A,r,n_b)}{V_{hop}^2}.
}
```

This is the first explicit microscopic-resource-conditioned admissibility inequality in Experiment 10.

For the previous witness

```text
T = 300 K
lambda_c = 10 um
r = 1.2
A = 0.90
n_b = 3.5
```

```math
C=1.06668\times10^{29}\ \mathrm{m^{-2}(m/s)^2}.
```

Hence

```text
V_hop = 1.0e6 m/s -> Sigma_e >= 1.067e13 cm^-2
V_hop = 2.0e6 m/s -> Sigma_e >= 2.667e12 cm^-2
V_hop = 3.0e6 m/s -> Sigma_e >= 1.185e12 cm^-2
```

These are conditional resource bounds, not universal semiconductor constants.

---

# Novelty status

Established ingredients include Kane `k.p`, band-edge effective-mass sums, optical conductivity sum rules, 3-D Dirac optical conductivity, HgCdTe Kane velocity measurements, and Wannier/tight-binding Bloch Hamiltonians.

Do not claim novelty for the operator-norm velocity inequality itself. The possible research contribution, if it survives a broader audit and later intrinsic-noise analysis, is the detector-specific synthesis

```math
matched absorptance
+ exact finite-gap Dirac statistics
+ microscopic velocity resource
-> Sigma_e >= C/V_hop^2.
```

Disposition remains

```text
POSSIBLE USEFUL SYNTHESIS / NOVELTY NOT ESTABLISHED.
```

---

# What is not established

```text
a chemistry-independent numerical upper bound on v;
a universal bound on hopping amplitude/range;
that HgCdTe maximizes E_P or v;
that the lattice bound is tight for a real semiconductor;
actual detector D* improvement;
Auger behavior;
novelty.
```

# NEXT ACTION

The obvious absorption/DOS cancellation, ballistic-time cancellation, generic `k.p` sum-rule cancellation, and remote-band-energy cancellation have now all failed to remove the high-`v` lever.

The next unavoidable intrinsic mechanism is Auger generation/recombination.

> For the same finite-gap massive-Dirac family, how does the **kinematically allowed Auger phase space** depend on `v`, `E_g`, and the minimal extra asymmetry/remote-band parameters, and does increasing `v` preserve the matched-absorptance advantage or introduce a stronger nonradiative cost?

Do not insert an empirical Auger coefficient as an independent free parameter. Begin from energy and crystal-momentum conservation plus the simplest Coulomb matrix-element structure.
