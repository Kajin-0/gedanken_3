# Experiment 12 — Resonant-Manifold Oscillator-Strength / Thermal-State-Count Theorem

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Disposition:** **EXACT TWO-MANIFOLD BOUND DERIVED / KUBO OBSERVABLE FORM DERIVED / LOW-ENERGY PLATEAU DERIVED / NOVELTY NOT ESTABLISHED**

## 1. Model

Use two flat single-particle manifolds in finite volume `V`:

```math
E_c-E_v=E_\gamma>0,
```

with dimensions `N_c` and `N_v`.

Let `p_e` be the equilibrium occupation probability of each conduction state and `p_h` the equilibrium hole probability of each valence state. Intrinsic neutrality requires

```math
\boxed{N_c p_e=N_v p_h\equiv N_{th}.}
```

The exact Fermi odds are

```math
x=\frac{p_e}{1-p_e}=e^{-\beta(E_c-\mu)},
```

```math
y=\frac{p_h}{1-p_h}=e^{-\beta(\mu-E_v)},
```

so

```math
\boxed{xy=e^{-\beta E_\gamma}\equiv z.}
```

For one optical polarization `i`, define the interband velocity block

```math
M=P_c\hat v_iP_v.
```

Assume the physical velocity operator obeys

```math
\boxed{\|\hat v_i\|\le v_{max}.}
```

Therefore every singular value of `M` is at most `v_max`.

---

## 2. Rank / singular-value optical-state budget

Define the unblocked Frobenius oscillator-strength quantity

```math
S_0
=\|M\|_F^2
=\operatorname{Tr}(M^\dagger M)
=\sum_{cv}|v_{cv}|^2.
```

If `r=rank(M)`, then

```math
S_0=\sum_{a=1}^{r}s_a^2
\le r v_{max}^2.
```

Since

```math
r\le\min(N_c,N_v),
```

```math
\boxed{
S_0\le v_{max}^2\min(N_c,N_v).
}
```

This is the microscopic state-count bottleneck: one cannot place arbitrary total interband velocity strength into fewer than `S_0/v_max^2` independent resonant channels.

---

## 3. Include exact Fermi blocking

The absorptive occupation difference for every transition between the two flat manifolds is

```math
D_f=f_v-f_c
=(1-p_h)-p_e.
```

Using the odds variables,

```math
\boxed{
D_f
=\frac{1-z}{(1+x)(1+y)}.
}
```

Define the **absorptively active** oscillator-strength sum

```math
\boxed{
S_{abs}
=D_fS_0
=\sum_{cv}(f_v-f_c)|v_{cv}|^2.
}
```

Then

```math
S_{abs}
\le
D_fv_{max}^2\min(N_c,N_v).
```

---

## 4. Exact optimization over conduction/valence degeneracy imbalance

Assume without loss of generality

```math
N_c\le N_v.
```

Neutrality then requires

```math
p_e\ge p_h,
```

hence

```math
x\ge y.
```

Since `xy=z`,

```math
\boxed{x\ge\sqrt z.}
```

The thermal electron number is

```math
N_{th}=N_cp_e.
```

Using the optical bound,

```math
\frac{N_{th}}{S_{abs}}
\ge
\frac{p_e}{D_fv_{max}^2}.
```

But

```math
\frac{p_e}{D_f}
=
\frac{x+z}{1-z}.
```

This expression is strictly increasing in `x`, so its minimum occurs at

```math
x=y=\sqrt z,
```

which corresponds to equal electron and hole occupations and, under neutrality, equal manifold dimensions.

Therefore

```math
\boxed{
\frac{N_{th}}{S_{abs}}
\ge
\frac{1}{v_{max}^2}
\frac{1}{e^{E_\gamma/(2k_BT)}-1}.
}
```

Equivalently,

```math
\boxed{
N_{th}
\ge
\frac{S_{abs}}{v_{max}^2}
\frac{1}{e^{E_\gamma/(2k_BT)}-1}.
}
```

The same result follows when `N_v<=N_c` by interchanging electron and hole labels.

### Equality conditions

The bound is saturated only when all of the following hold:

```text
N_c = N_v;
mu lies at the midpoint of the two manifolds;
rank(M) = N_c = N_v;
every nonzero singular value of M equals v_max;
no additional thermally occupied bands contribute carriers.
```

Thus the theorem is tight inside the stated two-manifold model.

---

## 5. Why a Bose-like factor appears

The factor

```math
\frac{1}{e^{E_\gamma/(2k_BT)}-1}
```

has Bose form even though the microscopic quasiparticles are fermions.

It is **not** a bosonic occupation assumption. It is the exact optimized ratio between

```text
thermal fermion occupation needed by intrinsic neutrality
```

and

```text
Pauli-unblocked interband oscillator strength.
```

In the nondegenerate limit,

```math
\frac{1}{e^{E_\gamma/(2k_BT)}-1}
\sim
e^{-E_\gamma/(2k_BT)},
```

recovering the expected intrinsic Boltzmann factor.

---

## 6. Kubo-Greenwood observable form

For the two exactly resonant manifolds, the real optical conductivity for polarization `i` is

```math
\sigma_1(\omega)
=
\frac{\pi e^2}{V\omega}
S_{abs}
\delta(E_\gamma-\hbar\omega).
```

Integrating over positive angular frequency,

```math
W_\sigma
\equiv
\int_0^\infty\sigma_1(\omega)d\omega
=
\frac{\pi e^2}{VE_\gamma}S_{abs}.
```

Therefore

```math
S_{abs}
=
\frac{VE_\gamma}{\pi e^2}W_\sigma.
```

Substitution into the exact state-count bound gives the first observable Experiment-12 theorem:

```math
\boxed{
n_{th}
\equiv\frac{N_{th}}{V}
\ge
\frac{E_\gamma}{\pi e^2v_{max}^2}
\frac{W_\sigma}
{e^{E_\gamma/(2k_BT)}-1}.
}
```

This concerns the **integrated intrinsic interband optical conductivity**, not merely a peak absorption coefficient.

Line broadening cannot increase the integrated spectral weight when the line shape is normalized; therefore using `W_sigma` removes the trivial infinitely narrow/high-peak loophole.

---

## 7. Sheet form

For absorber thickness `d`, define

```math
W_\sigma^{sheet}=dW_\sigma
```

and the equilibrium electron column

```math
\Sigma_{th}=n_{th}d.
```

Then

```math
\boxed{
\Sigma_{th}
\ge
\frac{E_\gamma}{\pi e^2v_{max}^2}
\frac{W_\sigma^{sheet}}
{e^{E_\gamma/(2k_BT)}-1}.
}
```

This is the direct analogue of the Experiment-10 matched-column question, but it does not assume Dirac or parabolic dispersion inside the resonant two-manifold model.

---

## 8. Single-pass optical-depth corollary

For a weakly absorbing homogeneous material in background refractive index `n_b`,

```math
\alpha(\omega)
\simeq
\frac{\sigma_1(\omega)}{n_b\epsilon_0c}.
```

Define optical depth

```math
\tau(\omega)=\alpha(\omega)d.
```

Then

```math
W_\sigma^{sheet}
=n_b\epsilon_0c
\int\tau(\omega)d\omega.
```

Hence

```math
\boxed{
\Sigma_{th}
\ge
\frac{n_b\epsilon_0cE_\gamma}
{\pi e^2v_{max}^2}
\frac{\int\tau(\omega)d\omega}
{e^{E_\gamma/(2k_BT)}-1}.
}
```

If a narrow useful optical band of width `Delta_omega` requires at least absorptance `A_0` in ideal single-pass Beer-Lambert form,

```math
A(\omega)=1-e^{-\tau(\omega)},
```

then

```math
\tau(\omega)\ge\zeta_0,
\qquad
\zeta_0=-\ln(1-A_0),
```

throughout that band, giving the corollary

```math
\boxed{
\Sigma_{th}
\ge
\frac{n_b\epsilon_0cE_\gamma}
{\pi e^2v_{max}^2}
\frac{\zeta_0\Delta\omega}
{e^{E_\gamma/(2k_BT)}-1}.
}
```

This corollary is conditional on intrinsic active-material absorption dominating the specified single-pass optical response. Arbitrary resonant/path-enhancing photonic structures introduce independent optical resources, as already established in Experiment 10.

---

## 9. Low-transition-energy limit

The energy-dependent factor obeys

```math
\frac{E_\gamma}{e^{E_\gamma/(2k_BT)}-1}
\to
2k_BT
```

as `E_gamma -> 0`.

Therefore, at fixed integrated intrinsic optical spectral weight,

```math
\boxed{
n_{th}
\ge
\frac{2k_BT}{\pi e^2v_{max}^2}W_\sigma
+O(E_\gamma).
}
```

The lower bound does **not** vanish as the transition energy goes to zero.

Interpretation:

```text
lower transition energy increases Fermi occupation;
Pauli blocking simultaneously reduces the useful interband absorption per state;
the optimized combination leaves a finite T-controlled floor at fixed spectral weight.
```

This is a stronger statement than simply noting that narrow gaps have large intrinsic carrier densities.

---

## 10. 10-um / 300-K single-pass witness

Use

```text
lambda = 10 um
T = 300 K
n_b = 3.5
A_0 = 0.90
Delta_omega / omega_0 = 0.10
```

so

```text
E_gamma/kBT = 4.7959229
1/[exp(E_gamma/2kBT)-1] = 0.0999927
zeta_0 = 2.3025851.
```

The sheet-column lower bound is

```text
v_max (m/s)      Sigma_th,min (cm^-2)
5.0e5              3.96998e12
1.0e6              9.92495e11
1.07e6             8.66883e11
2.0e6              2.48124e11
3.0e6              1.10277e11
```

Thus the observable theorem retains the Experiment-10 `v^-2` matched-column scaling without assuming massive-Dirac DOS or conductivity.

The numerical values are not a universal detector floor because they depend on the required optical-depth bandwidth and the single-pass optical hypothesis.

---

## 11. Relationship to Experiment 10

The massive-Dirac model had

```math
n\propto v^{-3},
\qquad
\alpha\propto v^{-1},
```

so matched optical depth gave

```math
\Sigma\propto v^{-2}.
```

Experiment 12 explains the same scaling at a more abstract level:

```text
fixed useful sheet spectral weight
requires a minimum rank/state count;

finite velocity-operator norm
limits oscillator strength per independent optical channel;

intrinsic neutrality
thermally populates those required states.
```

The Dirac result is therefore a concrete realization of the rank/state-count structure rather than the only route to it.

---

## 12. Focused prior-art audit so far

Established adjacent ingredients found in the first screen:

```text
Kubo-Greenwood optical conductivity and matrix-element/DOS decomposition;
full and restricted optical f-sum rules;
quantum-metric control of interband optical conductivity, including flat-band systems;
classical infrared detector alpha/G_th material figures of merit;
modern superlattice calculations that jointly evaluate oscillator strength, DOS, carrier density, and dark current.
```

The focused searches did **not** identify a prior photodetector theorem with the specific form

```math
thermal carrier number
>=
absorptive interband velocity-matrix spectral weight
x exact neutrality/Pauli factor
/ velocity-operator norm squared,
```

or its equivalent singular-value/rank statement.

This absence is not evidence of novelty. A dedicated literature audit is still required.

```text
NOVELTY NOT ESTABLISHED.
```

---

## 13. Hard boundaries before further generalization

Not yet covered:

```text
dispersive nondegenerate manifolds;
transitions spread over a broad frequency interval;
additional bands that shift the intrinsic chemical potential;
excitons and correlated many-body optical states;
collective/superradiant oscillator strength;
phonon-assisted transitions;
non-Hermitian or strongly broadened quasiparticles;
intentional doping;
photonic path enhancement / cavities;
full generation-recombination rate or D*.
```

Do not claim a universal semiconductor theorem until these escape routes are tested.

## Next action

First attempt to generalize from two flat resonant manifolds to **energy-resolved dispersive bands**. The key question is whether the rank/state-count argument can be applied to frequency bins without double-counting states or losing control of the global neutrality chemical potential.

If that fails, determine exactly why; the failure mode itself may identify the missing microscopic resource.
