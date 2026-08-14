# Progress Log — Experiment 10: Room-Temperature LWIR Material Admissibility

## 2026-08-14 — branch initialization

Established target

```math
T=300\ \mathrm K,
\qquad
\lambda_c=10\ \mu\mathrm m,
\qquad
E_g\approx0.12398\ \mathrm{eV},
\qquad
E_g/(k_BT)\approx4.80.
```

Objective: derive a finite-gap band-structure admissibility theorem/bound rather than rank known materials.

---

## 2026-08-14 — matched massive-Dirac absorptance

Controlling file: `MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`.

Derived

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

Ideal ballistic crossing time obeys `tau_ball ~ v^0`.

At 10 um / 300 K the exact finite-gap Dirac carrier density is `1.8644x` the edge-parabolic estimate.

Disposition:

```text
MATCHED-ABSORPTANCE HIGH-v LEVER SURVIVES.
NOVELTY NOT ESTABLISHED.
```

---

## 2026-08-14 — Kane velocity freedom and microscopic resource bound

Controlling file: `KANE_VELOCITY_RESOURCE_BOUND_STEP_2026-08-14.md`.

Using

```math
E_P=2m_0P^2/\hbar^2,
\qquad
v^2=E_P/(3m_0),
```

```math
\Sigma_e\propto E_P^{-1}.
```

Generic upper-bound attempts based on the multiband effective-mass identity, global optical f-sum over a fixed detector energy window, and fixed remote-band energy failed to provide a material-independent upper bound on `v`.

For a Wannier Hamiltonian,

```math
\boxed{
\|\hat v_i\|
\le\frac1\hbar\sum_R|R_i|\|H_R\|
\equiv V_i^{hop}.
}
```

Hence conditionally

```math
v\le V_{hop}
```

and

```math
\boxed{\Sigma_e\ge C/V_{hop}^2.}
```

Disposition:

```text
FIRST MICROSCOPIC-RESOURCE-CONDITIONED DETECTOR INEQUALITY DERIVED.
NOVELTY NOT ESTABLISHED.
```

---

## 2026-08-14 — exact Auger kinematic closure

Controlling file: `AUGER_KINEMATIC_CLOSURE_STEP_2026-08-14.md`.

For the exact particle-hole-symmetric finite-gap massive-Dirac dispersion,

```math
\varepsilon(k)=\sqrt{\Delta^2+(\hbar vk)^2},
```

strict subadditivity gives empty exact normal-momentum phononless `eeh` Auger/impact-ionization support; the `hhe` mirror is also closed.

The exact off-shell mismatch is

```math
\boxed{
\Delta_A(E)=\sqrt{E^2+2E_g^2}-E.
}
```

At fixed `E/E_g`, `v` cancels. Therefore large `v` and particle-hole symmetry are distinct resources.

Broad Dirac/symmetric-dispersion Auger suppression is established prior art.

---

## 2026-08-14 — particle-hole-asymmetry reopening law

Controlling file:

`AUGER_ASYMMETRY_REOPENING_STEP_2026-08-14.md`

Reproducible calculation:

`numerics/auger_asymmetry_threshold.py`

### Perturbation

Add

```math
E_\pm(k)=Dk^2\pm\sqrt{\Delta^2+(\hbar vk)^2}.
```

Define

```math
q=\hbar vk/\Delta,
\qquad
\beta=D\Delta/(\hbar^2v^2),
```

and normalized inverse-mass asymmetry

```math
\boxed{
\mathcal A_m
=\frac{|m_e^{-1}-m_h^{-1}|}
{m_e^{-1}+m_h^{-1}}
=2|\beta|.
}
```

### Exact reduced-model reopening boundary

For the favorable-sign `eeh` channel, the first on-shell configuration at fixed total dimensionless momentum `q_0` reduces to two equal electron momenta `x`, a hole momentum `q_0-2x`, and

```math
\boxed{
\beta_c(q_0)
=
\min_{0\le x\le q_0/2}
\frac{2\sqrt{1+x^2}
+\sqrt{1+(q_0-2x)^2}
-\sqrt{1+q_0^2}}
{2(q_0-x)^2}.
}
```

Selected unconstrained vector optimizations independently returned the same collinear minima.

### Weak-asymmetry asymptotic

For small `|beta|`, the threshold occurs at large `q`. The optimal momentum partition tends to

```text
q1 = q2 = q0/4
q3 = q0/2
```

and

```math
\boxed{\beta_c(q_0)\sim4/q_0^3.}
```

Hence

```math
\boxed{q_{th}\sim(4/|\beta|)^{1/3}.}
```

The hot-electron kinetic threshold above the conduction edge therefore obeys

```math
\boxed{
K_{th}\sim E_g\mathcal A_m^{-1/3}.
}
```

At fixed temperature,

```math
\boxed{
K_{th}/k_BT
\sim(E_g/k_BT)\mathcal A_m^{-1/3}.
}
```

### 10-um / 300-K exact thresholds

```text
A_m      K_th/kBT
0.40       5.873
0.20       7.536
0.10       9.470
0.04      12.848
0.02      16.273
0.01      20.675
```

Inverting the exact relation:

```text
required K_th/kBT    max A_m
8                     0.1671
10                    0.08476
12                    0.04900
15                    0.02536
```

Thus the scalar `Dk^2` model requires approximately

```math
\mathcal A_m\lesssim0.0848
```

to place the direct-channel threshold above `10 k_BT` at the fixed Experiment-10 target.

The edge-mass interpretation is model-specific; the physical requirement is symmetry over the finite Auger-active momentum window.

### Prior-art disposition

Full HgCdTe-QW theory already shows strongly enhanced/diverging normalized Auger thresholds near Dirac-like regimes, and later work explicitly ties massive-Dirac Auger suppression to electron-hole symmetry and nonparabolicity. Therefore the broad threshold concept is old.

The compact reduced-model cube-root law is retained as a derived analytical result only.

```text
NOVELTY NOT ESTABLISHED.
```

### Next frontier

Do not rank materials yet.

Next question:

> With the exact threshold structure retained, what is the leading near-threshold thermal/phase-space scaling of the direct Auger rate, and can it be combined with `Sigma_e ~ v^-2` into a detector-level room-temperature admissibility inequality before model-dependent Coulomb prefactors dominate?
