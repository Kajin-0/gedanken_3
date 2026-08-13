# Three-state coupled-mode optical surrogate

**Date:** 2026-08-13  
**Status:** REDUCED-ORDER OPTICAL PASS / MAXWELL NOT YET DONE / NOVELTY NOT ESTABLISHED

The three-section discrete depth ladder was replaced by a minimal physical coupled-mode transfer model. The three localized absorption states are centered at

```text
z = 0.291, 0.958, 1.624 um
```

for the current `d=2 um` absorber. Their benchmark local absorption-depth RMS is `100 nm`.

## Coupled-mode transfer

For a resonant transition between adjacent depth states,

```math
d[a_1,a_2]^T/dx
=
-i[[0,kappa],[kappa,0]][a_1,a_2]^T
-(alpha_eff/2)[a_1,a_2]^T,
```

so

```math
P_1=cos^2(kappa s),\qquad
P_2=sin^2(kappa s),\qquad
L_c=pi/(2 kappa).
```

If the depth states have equal effective modal absorption, coupling does not change the total survival law. Keeping 90% absorption over `L=3 mm` requires

```text
alpha_eff = ln(10)/L = 0.7675 mm^-1 = 7.675 cm^-1
```

or `53.584%` absorption of the power entering each 1-mm interval.

## Important correction: pointwise 100-nm width is not required

During 50/50 transfer between neighboring states separated by `d/3=0.6667 um`,

```math
Var(Z|x)=sigma_z^2+P_1P_2(Delta z)^2.
```

With `sigma_z=100 nm`, the instantaneous conditional depth RMS reaches `0.348 um`.

Nevertheless, timing barely changes because the relevant quantity is the **absorption-weighted timing error**, not the maximum local depth width. A broad/bimodal transfer is acceptable when it occurs where the two neighboring timing errors are already similar.

Therefore the earlier heuristic

```text
conditional absorption-depth RMS must stay near 100 nm everywhere
```

is **REJECTED**.

The correct constraint is the integrated contribution of conditional-mean error plus conditional depth variance to the timing budget.

## Transfer-length sweep

Using the existing combined floor (`Pe=100`, 5-ps avalanche, 2-ps electronics, 1-ps optical), the direct control is `12.645 ps RMS`.

| Lc per transfer | forward RMS | improvement | reverse RMS |
|---:|---:|---:|---:|
| 0 um | 8.369 ps | 33.815% | 20.724 ps |
| 50 um | 8.370 ps | 33.809% | 20.724 ps |
| 100 um | 8.372 ps | 33.793% | 20.723 ps |
| 200 um | 8.380 ps | 33.727% | 20.722 ps |
| 400 um | 8.414 ps | 33.464% | 20.714 ps |
| 1000 um | 8.645 ps | 31.632% | 20.661 ps |

Thus **transfer length is not the primary optical bottleneck**. Even ~1-mm transfers retain the 30% gate.

## Incomplete transfer is the stronger constraint

A pessimistic stress test leaves all untransferred power permanently in the old depth state.

At `sigma_z=100 nm`:

| transfer efficiency | forward RMS | improvement |
|---:|---:|---:|
| 1.00 | 8.369 ps | 33.815% |
| 0.99 | 8.466 ps | 33.053% |
| 0.98 | 8.560 ps | 32.309% |
| 0.97 | 8.652 ps | 31.583% |
| 0.95 | 8.829 ps | 30.178% |
| 0.9474 | 8.852 ps | 30.000% |
| 0.94 | 8.915 ps | 29.499% |
| 0.90 | 9.240 ps | 26.926% |

Therefore the current 30% gate requires approximately

```math
\boxed{eta_c >= 0.9474}
```

per depth-state transfer.

The localization/transfer tradeoff is:

| local depth RMS | minimum transfer efficiency for >=30% |
|---:|---:|
| 50 nm | 0.9275 |
| 100 nm | 0.9474 |
| 125 nm | 0.9620 |
| 150 nm | 0.9795 |
| 175 nm | 0.99965 |

This is now the principal optical Maxwell go/no-go surface.

For a detuned two-mode coupler,

```math
eta_max=kappa^2/[kappa^2+(Delta beta/2)^2].
```

At the 100-nm / 30% gate,

```math
|Delta beta| <= 0.471 kappa.
```

For a 50-um resonant transfer (`kappa=31.42 mm^-1`) at 1.55 um, the corresponding effective-index-mismatch scale is about `0.00365`. This is only a coupled-mode design target, not a material result.

## Adjacent technology and prior-art stress

Established work already covers high-efficiency vertical/adiabatic waveguide transfer and vertically/evanescently coupled avalanche photodetectors. Examples include Sun, Liu & Yariv, *Opt. Lett.* 34, 280 (2009), DOI `10.1364/OL.34.000280`; Liu et al., *JLT* 36, 755 (2018), reporting simulated >96% vertical transfer on a ~55-um scale; a 2023 *Optics Letters* vertical directional-coupler mode multiplexer reporting >97% experimental transfer; and vertically coupled hybrid/heterogeneous InGaAs/InAlAs SPAD integration, DOI `10.1088/2058-9565/acb730`.

These establish adjacent ingredients, not the present timing objective.

A new prior-art search also found **US20240063321A1** (priority 2021-02-07), which explicitly treats NIR SPAD absorption-depth timing uncertainty using a waveguide with multiple longitudinal SPAD segments and discusses exponential absorption and timing-jitter constraints. This is closer adjacent art than previously logged.

The inspected disclosure still does not show the specific operation

```text
longitudinal optical delay
+ transverse absorption-depth state
-> constant conditional mean carrier-to-avalanche timestamp.
```

So:

```text
adjacent prior-art risk: increased
exact transverse-depth compensation match: not found in this search
novelty: not established
priority language: not authorized
```

## New frontier

Generic coupled-mode optics no longer looks like the first kill mechanism. The next risk is the **electrical/avalanche footprint of the required 3-mm optical path**.

Before full Maxwell work, build a distributed electrical surrogate covering:

1. junction width and active area;
2. depletion/multiplication capacitance;
3. electrode/readout propagation delay;
4. one common avalanche region versus segmented regions;
5. dark-count scaling with active area;
6. whether optical path length can be large while electrical active area remains small.

If the 3-mm optical path forces an electrically large APD/SPAD whose readout or avalanche-spreading floor is already above roughly 10 ps, this implementation should be killed or re-architected before TCAD/Maxwell refinement.

Companion numerical script: `numerics/three_state_coupled_mode.py`.
