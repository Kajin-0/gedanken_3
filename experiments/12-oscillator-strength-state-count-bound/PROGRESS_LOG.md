# Progress Log — Experiment 12: Oscillator-Strength / Thermal-State-Count Bound

## 2026-08-14 — branch opened provisionally

Branch:

```text
experiment-12-oscillator-strength-state-count-bound
```

Opened only after the premise survived a focused search better than the preceding rejected candidates.

Question: can fixed low-energy direct-interband optical spectral weight coexist with arbitrarily small equilibrium thermal quasiparticle population when the microscopic interband velocity resource remains finite?

---

## 2026-08-14 — exact two-manifold theorem

For flat conduction/valence manifolds separated by `E_gamma`, intrinsic neutrality and exact Fermi occupations were combined with the singular-value bound

```math
\|P_c\hat v_iP_v\|_F^2
\le
v_{max}^2\min(N_c,N_v).
```

Including Pauli blocking gives the tight result

```math
\boxed{
N_{th}
\ge
\frac{S_{abs}}{v_{max}^2}
\frac{1}{e^{E_\gamma/(2k_BT)}-1}.
}
```

Kubo-Greenwood converts this to

```math
\boxed{
n_{th}
\ge
\frac{E_\gamma}{\pi e^2v_{max}^2}
\frac{W_\sigma}{e^{E_\gamma/(2k_BT)}-1}.
}
```

Low-energy limit at fixed integrated optical spectral weight:

```math
\boxed{
n_{th,min}
\to
\frac{2k_BT}{\pi e^2v_{max}^2}W_\sigma.
}
```

Disposition:

```text
FIRST EXACT RESULT SURVIVES.
NOVELTY NOT ESTABLISHED.
```

---

## 2026-08-14 — arbitrary dispersive multiband generalization

The expected state-reuse loophole did **not** break the theorem.

For every transition from `E_v<mu` to `E_c>mu`, exact Fermi algebra gives

```math
\boxed{
D_{cv}
\le
\frac{e^{E_{cv}/(2k_BT)}-1}{2}
(p_c+h_v).
}
```

If each row and column of the crossing-transition velocity matrix has squared norm at most `v_*^2`, then for partial interband spectral weight

```math
W(E_\Omega)
=\int_0^{E_\Omega/\hbar}
\sigma_1^{inter}(\omega)d\omega,
```

```math
\boxed{
n_e+n_h
\ge
\frac{2E_\Omega}{\pi e^2v_*^2}
\frac{W(E_\Omega)}
{e^{E_\Omega/(2k_BT)}-1}.
}
```

No flat bands, equal degeneracies, momentum conservation, or frequency-bin additivity are required.

Controlling file:

`DISPERSIVE_MULTIBAND_GENERALIZATION_STEP_2026-08-14.md`

---

## 2026-08-14 — global cutoff-free thermal optical sum

The pointwise Fermi inequality can be inverted before any frequency cutoff is introduced.

Summing with the same row/column velocity-strength budget and using Kubo gives

```math
\boxed{
n_e+n_h
\ge
\frac{2}{\pi e^2v_*^2}
\int_0^\infty
\frac{\hbar\omega\,\sigma_1^{inter}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
d\omega.
}
```

For an intrinsic neutral absorber,

```math
\boxed{
n_{th}
\ge
\frac{1}{\pi e^2v_*^2}
\int_0^\infty
\frac{\hbar\omega\,\sigma_1^{inter}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
d\omega.
}
```

The thermal kernel

```math
K_T(E)=E/[e^{E/(2k_BT)}-1]
```

approaches `2 kBT` for low-energy optical transitions. Thus fixed low-energy optical spectral weight implies a finite thermal-population floor even as the optical energy tends to zero.

The two-manifold and cutoff theorems are corollaries.

Controlling file:

`THERMAL_OPTICAL_SUM_INEQUALITY_STEP_2026-08-14.md`

---

## 2026-08-14 — independent validation

Reproducible script:

`numerics/thermal_optical_sum_dirac_validation.py`

Results:

```text
2-D neutral massless Dirac / graphene: bound/exact = 1/2
3-D massless Dirac:                    bound/exact = 2/3
```

For the 3-D massive-Dirac family:

```text
Delta/kBT       bound/exact
0                0.6667
0.5              0.6863
1.0              0.7191
2.39796146       0.794684
4.0              0.8454
8.0              0.9045
16.0             0.9459
```

Thus at the 10-um / 300-K Experiment-10 point, the theorem recovers about `79.5%` of the exact thermal population without using the Dirac DOS in the derivation.

---

## 2026-08-14 — many-body boundary

Bound excitons provide a real escape from a theorem stated in terms of **free quasiparticle** population:

```text
low-energy neutral excitonic oscillator strength can exist below the free electron-hole continuum;
photocurrent then requires a separate dissociation process.
```

Therefore the theorem is not universal across all photodetector architectures.

Current valid class:

```text
independent-quasiparticle direct interband charge absorbers.
```

Static single-particle disorder does not automatically break the theorem if exact eigenstates are used. Interaction-generated lifetime broadening and collective optical states are outside scope.

---

## Focused novelty status

Audited adjacent primary literature includes:

```text
Kubo-Greenwood;
standard/generalized optical f-sums;
partial/restricted optical sums;
graphene finite-T optical sum rules;
quantum-geometric optical sums;
finite-temperature QFI response kernels;
classic infrared alpha/G_th detector criteria.
```

No direct collision with the exact thermal carrier-population inequality has yet been identified.

```text
NOVELTY NOT ESTABLISHED.
```

---

## Active frontier

The theorem itself has survived the first major mathematical generalizations.

Next attacks:

```text
localized-state / electrical-activity loophole;
carrier-number fluctuation/noise corollary;
dedicated exact-kernel novelty audit beyond photodetector literature.
```

Do not move to a manuscript until these are resolved.
