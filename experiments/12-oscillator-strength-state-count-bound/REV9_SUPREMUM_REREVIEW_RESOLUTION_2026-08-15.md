# Experiment 12 — Rev9 supremum rereview resolution

**Date:** 2026-08-15  
**Branch:** `experiment-12-oscillator-strength-state-count-bound`  
**Disposition:** **REVIEWER FORMAL POINT VALID / PROPOSED GAMMA CORRECTION INVALID / SURGICAL REVISION REQUIRED**

## Trigger

An extreme adversarial rereview identified a mismatch between the finite-system capacity definition in Eqs. (21)–(22), which uses an ordinary supremum over exact energy shells, and the bulk HgCdTe implementation in Eq. (49), which was written with an essential supremum over crystal momentum.

The rereview then proposed that the isolated Gamma-point Gamma8 degeneracy forces a larger capacity of order `v_K ~= 1.05e6 m/s`, reducing the broad HgCdTe ratio from 0.118 to about 0.110.

## 1. The formal notation mismatch is real

The current theorem is built at finite volume. Its capacity is an ordinary shell supremum, followed by a thermodynamic `limsup`. The bulk validation should therefore not silently replace that object by an essential supremum unless a separate zero-density-exception theorem is proved.

For the present paper the cleanest repair is conservative and local:

- retain the finite-volume theorem exactly as written;
- implement the bulk validation with an **ordinary supremum** over local projected blocks on the stated bounded `k` domain;
- explicitly check special/high-symmetry points rather than discarding them as measure-zero sets.

No new density-essential-capacity theorem is needed.

## 2. The proposed Gamma-point correction does not apply to this HgCdTe state

The rereview's concrete Gamma argument overlooks the cross-chemical-potential selection condition.

The production charge-neutral state is

```text
Eg = 0.123984198 eV
mu = 0.135461511 eV
mu - Eg = +11.477 meV
```

At `k = 0`, the two Gamma6-derived states are at `Eg`, hence **below** `mu`. The Gamma8-derived states are also below `mu`.

Therefore there is no selected Gamma8 -> Gamma6 transition crossing `mu` at Gamma. The selected projected block in Eq. (21) is empty there. The first-order Gamma8/Gamma6 velocity scale `v_K` is consequently irrelevant to the cross-`mu` capacity at the isolated Gamma point for this numerical state.

The selected cross-`mu` set begins only after the Gamma6-derived pair rises through `mu` at finite momentum.

## 3. Ordinary-supremum audit

A direct continuous search of the second-order projected-block capacity over each stated bounded optical domain, with the same exact-shell clustering and cross-`mu` selection used by the production code, gives a common maximum to the reported precision:

```text
v_B^cap(sup) ~= 1.017640e6 m/s
|k| at maximum ~= 0.05535 nm^-1
```

The maximum occurs near the finite-`k` cross-`mu` onset. It is not an isolated Gamma-point block. Values arbitrarily close to the maximum occur on the selected side of the onset, so the ordinary and essential suprema coincide numerically for this model even though the paper should use the ordinary supremum to match Eqs. (21)–(22).

The production Gauss-Legendre grid had returned window-dependent sampled maxima near `1.015–1.017e6 m/s`; the continuous supremum audit raises the denominator only slightly.

Using the same converged optical numerators and `v_B^cap = 1.017640e6 m/s` gives approximately:

| window | Rev9 ratio | ordinary-sup ratio |
|---|---:|---:|
| `Eg .. 1.5 Eg` | 0.032046 | 0.031995 |
| `Eg .. 2 Eg` | 0.074922 | 0.074868 |
| `Eg .. 3 Eg` | 0.110977 | 0.110505 |
| `Eg .. 0.5 eV` | 0.118010 | **0.117540** |

Thus the correct conservative repair changes the broad result by about four tenths of one percent relative, not from 11.8% to 11.0%.

## 4. Pairwise diagnostic after continuous-supremum audit

A continuous search of the largest selected individual pairwise matrix element gives approximately

```text
max |v_cv| ~= 0.871651e6 m/s.
```

Using the ordinary projected-block supremum,

```text
(v_block / v_pair)^2 - 1 ~= 36.3%.
```

The qualitative point survives: replacing the projected block by a pairwise maximum would materially overstate the population lower bound.

## 5. Active-population decomposition

The rereview correctly notes that the old prose attributed looseness too broadly to heavy-hole/multiband asymmetry without separating the two gaps in

```text
n_bound <= n_B^act <= n_ref.
```

A production-grid support-rank diagnostic (`Nk=160`, `Ncos=10`, `Nphi=16`) gives:

| window | `n_B^act/n_ref` | `n_bound/n_B^act` | product |
|---|---:|---:|---:|
| `Eg .. 1.5 Eg` | 0.2642 | 0.1211 | 0.0320 |
| `Eg .. 2 Eg` | 0.4504 | 0.1662 | 0.0749 |
| `Eg .. 3 Eg` | 0.5619 | 0.1967 | 0.1105 |
| `Eg .. 0.5 eV` | 0.6690 | 0.1757 | 0.1175 |

For the broad window, about 67% of the cross-`mu` thermal population lies in selected optical support, while the Fermi/capacity step recovers about 17.6% of that active population. The old statement that the 11.8% product is simply caused by “heavy-hole and multiband asymmetry” is therefore too compressed. Both incomplete selected support and transition/capacity slack contribute, with the latter larger in the broad-window product.

The numerical support-rank result is stable against singular-value rank thresholds from `1e-6` through at least `1e4 m/s` on tested grids. A denser broad-window grid (`Nk=200`, `Ncos=12`, `Nphi=20`) gives `n_B^act/n_ref ~= 0.6689`, consistent with the production value.

## 6. Minor rereview points

### Eq. (48) window units

The general theorem defines `B` as an angular-frequency set, while the numerical section currently inserts an energy difference directly into `chi_B`.

Repair: define

```math
E_B = { hbar omega : omega in B }
```

in the numerical subsection and use `chi_{E_B}(E_m - E_n)`.

### Production quadrature orders

The main production orders already exist in the validation record and script:

```text
Nk       = 160 radial Gauss-Legendre nodes
Ncos     = 10 polar Gauss-Legendre nodes
Nphi     = 16 uniform azimuthal nodes
```

These should be stated explicitly in the manuscript. The denser audit grid used here is `200 x 12 x 20`.

## 7. Required manuscript action

Create a surgical referee-repair revision, without reopening the central theorem:

1. change Eq. (49) from `ess sup` to the ordinary `sup` consistent with Eqs. (21)–(22);
2. state explicitly that Gamma is not in the selected cross-`mu` set because `mu > E_Gamma6`;
3. replace sampled capacity diagnostics by the continuous ordinary-supremum audit (`~1.01764e6 m/s`);
4. update the broad exact numerical ratio from `0.118010` to `~0.11754` where precision warrants, while `0.118` and `11.8%` remain valid at the manuscript's coarse precision;
5. update the pairwise diagnostic to `~0.87165e6 m/s` and `~36.3%` if quoting the continuous supremum comparison;
6. correct Eq. (48) to use an energy-domain window;
7. state the production quadrature orders and the denser audit grid;
8. replace the unqualified causal statement about heavy-hole/multiband asymmetry with the measured active-support/Fermi-capacity decomposition.

## Bottom line

```text
CENTRAL EQ. (29):                     unchanged / passes
SUP vs ESS SUP NOTATION:              real issue / repair required
PROPOSED ISOLATED-GAMMA CORRECTION:   rejected for this cross-mu state
BROAD HGCDTE RATIO AFTER SUP AUDIT:   ~0.1175 (still 11.8% rounded)
SCIENTIFIC CONCLUSION:                unchanged
NEXT ACTION:                          surgical Rev10 manuscript + typeset QA
```
