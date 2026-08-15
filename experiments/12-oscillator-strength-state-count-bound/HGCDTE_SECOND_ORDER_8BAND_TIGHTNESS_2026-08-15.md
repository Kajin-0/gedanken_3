# Experiment 12 — Second-order HgCdTe 8-band tightness validation

**Date:** 2026-08-15  
**Branch:** `experiment-12-oscillator-strength-state-count-bound`  
**Disposition:** **REALISTIC MULTIBAND TIGHTNESS TEST COMPLETE / BOUND NONTRIVIAL BUT LOOSE / CENTRAL THEOREM UNCHANGED / NOVELTY NOT ESTABLISHED**

## Question

The Rev7 external re-review left one high-value significance test:

> In the same realistic multiband narrow-gap model, compute the selected optical capacity, the thermally weighted cross-`mu` optical response, the exact theorem population, and the ratio `n_bound/n_exact`.

Rev7 had only shown that the capacity resource is microscopically bounded in the first-order 8x8 Kane Hamiltonian. This step tests the complete inequality quantitatively.

## Why the second-order model is required

The simplified first-order 8x8 Kane Hamiltonian has an exactly flat heavy-hole branch. At finite temperature that branch makes a bulk equilibrium carrier-density calculation depend on the ultraviolet/momentum cutoff.

For the quantitative population test we therefore use the bulk constant-parameter limit of the second-order 8-band `k.p` Hamiltonian in:

```text
E. G. Novik et al., Phys. Rev. B 72, 035321 (2005),
DOI 10.1103/PhysRevB.72.035321.
```

This Hamiltonian treats the Gamma6, Gamma8 and Gamma7 sectors explicitly and restores the remote-band quadratic terms/valence curvature. The calculation is deliberately restricted to a bounded momentum domain where the `k.p` model is being used.

## Representative 10-um / 300-K model

Target:

```text
T = 300 K
Eg = 0.123984198 eV
```

Using the Laurenti `Eg(x,T)` convention cited by Novik gives

```text
x = 0.179727548.
```

For this representative calculation, the remote-band parameters are linearly interpolated between the HgTe and CdTe endpoint values tabulated by Novik:

```text
Delta  = 1.049446 eV
F      = -0.016175
gamma1 = 3.627317
gamma2 = 0.359813
gamma3 = 1.071746
kappa  = -0.563552
EP     = 18.8 eV
P/hbar = 1.285804e6 m/s
```

The interpolation is a modeling choice for this validation, not a claim of a unique measured 300-K parameter set.

## Numerical method

Reproducibility script:

`numerics/kane_8band_tightness.py`

Main calculation:

```text
carrier domain: |k| <= 2.0 nm^-1
radial Gauss-Legendre points: 160
polar points: 10
azimuthal points: 16
```

The charge-neutral chemical potential is solved from equality of the conventional upper-band electron density and lower-band hole density.

For the optical theorem integral, no phenomenological linewidth is introduced. The frequency delta function is integrated analytically, leaving a transition sum weighted by

```math
[f(E_v)-f(E_c)]
\frac{|v_{cv}|^2}{\exp[E_{cv}/(2k_BT)]-1}.
```

For each exact Kramers-degenerate shell, selected upper/lower velocity blocks are formed and their largest singular value is used to compute the basis-invariant `v_B^cap`.

Because the homogeneous velocity operator conserves crystal momentum, the full shell operator is a direct sum over `k`; its norm is the maximum local selected-shell singular value.

## Equilibrium state

The second-order model gives

```text
mu - Ev = 0.135461511 eV
mu - Ec = +11.477 meV
```

so the charge-neutral chemical potential is weakly inside the nominal conduction sector because of the strongly asymmetric valence/heavy-hole density of states.

Conventional semiconductor carrier densities:

```text
conduction electron density = 5.050214e16 cm^-3
valence hole density        = 5.050214e16 cm^-3
physical e+h total          = 1.010043e17 cm^-3
```

The theorem is defined by exact states relative to `mu`, giving

```text
cross-mu upper-state electron density = 4.722888e16 cm^-3
cross-mu lower-state hole density     = 5.328518e16 cm^-3
n_e+n_h exact theorem population      = 1.005141e17 cm^-3
```

Thus the theorem population differs from the conventional electron-plus-hole total by only about `0.49%` in this representative state.

## Full windowed theorem test

| selected transition-energy window | `v_B^cap` (m/s) | theorem lower bound (cm^-3) | bound/exact |
|---|---:|---:|---:|
| `Eg .. 1.5 Eg` | `1.016823e6` | `3.221119e15` | `0.032046` |
| `Eg .. 2 Eg` | `1.017273e6` | `7.530675e15` | `0.074922` |
| `Eg .. 3 Eg` | `1.015473e6` | `1.115475e16` | `0.110977` |
| `Eg .. 0.5 eV` | `1.015611e6` | `1.186163e16` | **`0.118010`** |

The broad low-energy model window through `0.5 eV` therefore recovers about

```math
\boxed{11.8\%}
```

of the exact cross-`mu` thermal excitation population.

This is substantially looser than the ideal mirror-symmetric and Dirac validation families, as expected from the heavy-hole/multiband asymmetry, but it is not numerically vacuous. The realistic multiband check remains at order `10^-1`, not `10^-3`.

## Selected capacity versus first-order global ceiling

Rev7 derived the first-order microscopic ceiling

```math
v_B^{cap}\le P/\hbar\simeq1.286\times10^6\ \mathrm{m/s}.
```

The direct second-order selected-window calculation instead gives approximately

```text
v_B^cap ~= 1.016e6 m/s
```

over the broad low-energy windows above.

Therefore the first-order global operator norm should not be described as the actual selected-window capacity. It is an upper bound; the second-order selected capacity is materially smaller.

Also, the first-order ceiling is not automatically a ceiling for the second-order Hamiltonian because the quadratic terms add `k`-dependent velocity contributions. In the second-order calculation the capacity is evaluated directly on the stated bounded `k` domain.

## Convergence

Carrier-domain convergence at reduced angular resolution:

| `kmax` (nm^-1) | `mu` (eV) | conventional electron density (cm^-3) | cross-`mu` total (cm^-3) |
|---:|---:|---:|---:|
| 1.2 | 0.134473 | 4.898713e16 | 9.758782e16 |
| 1.5 | 0.135213 | 5.011758e16 | 9.976805e16 |
| 1.8 | 0.135362 | 5.034785e16 | 1.002105e17 |
| 2.0 | 0.135382 | 5.037939e16 | 1.002925e17 |

Additional checks through `kmax=3.0 nm^-1` change the carrier population by less than about `0.3%` from the production result.

For the `Eg .. 0.5 eV` optical window, changes in radial/angular quadrature and optical `kmax` give

```text
bound/exact ~= 0.1179 - 0.1186
v_B^cap     ~= 1.010e6 - 1.017e6 m/s.
```

The reported `0.1180` result is therefore stable at the level relevant to the manuscript.

## Interpretation

What this calculation establishes:

```text
1. a realistic second-order narrow-gap multiband Hamiltonian has a finite selected optical capacity on its bounded domain of validity;
2. the complete Experiment-12 inequality can be evaluated without an arbitrary linewidth;
3. in representative 10-um/300-K HgCdTe-like parameters, the bound captures about 12% of the exact theorem population over a broad low-energy window;
4. multiband/heavy-hole asymmetry materially degrades tightness relative to the symmetric parabolic/Dirac examples but does not make the theorem numerically empty.
```

What it does not establish:

```text
no claim that this interpolation is a unique measured 300-K HgCdTe parameter set;
no claim that the 8-band k.p model is valid to arbitrarily large k;
no claim that 0.5 eV is a detector operating bandwidth;
no claim that the theorem population is a dark-current or D* floor;
no priority/novelty claim.
```

The `Eg .. 0.5 eV` window is a model-validation window chosen to test how much of the equilibrium cross-`mu` population the optical theorem can recover before approaching the split-off scale; it is not a proposed device bandwidth.

## Rev8 consequence

This result should replace the Rev7 statement that only the capacity scale has been anchored. A Rev8 manuscript can now state that the theorem has been tested end-to-end in a realistic second-order multiband narrow-gap model.

The same revision should also implement the remaining re-review fixes:

```text
formal double-uniformity over a moving low-energy window sequence;
first-order Kane value described only as a capacity upper bound;
second-order finite-capacity statement explicitly restricted to a bounded k-domain of model validity;
Appendix-A lower edge shifted above the exact absorption threshold.
```

**Novelty remains not established.**