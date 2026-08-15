# Experiment 13 — production-scale HgCdTe stable-rank QA

**Date:** 2026-08-15  
**Scope:** production-resolution regression of the Experiment-13 decomposition against the authoritative Experiment-12 eight-band Kane model  
**Status:** **PASS / STABLE-RANK CONCLUSION SURVIVES PRODUCTION QUADRATURE / ~17.6% ACTIVE TIGHTNESS RECONSTRUCTED**

## 1. Purpose

The earlier stable-rank closure used moderate refined quadrature and then substituted the independently validated continuous ordinary-supremum capacity from Experiment 12. Before using the decomposition in the unified manuscript, the thermal shell sums themselves needed to be rerun at the production quadrature used by the controlling broad-window HgCdTe validation.

This QA uses

```text
T = 300 K
Eg = hc/(10 um)
window = Eg .. 0.5 eV
carrier k-domain = 2.0 nm^-1
optical k-domain = 1.0 nm^-1
carrier / optical radial quadrature nr = 160
nmu = 10
nphi = 16
exact-shell clustering tolerance = 1e-7 eV
```

and the existing Experiment-12 production ordinary-supremum capacity

```text
v_B^cap = 1.01764e6 m/s.
```

The Hamiltonian, analytic velocity operator, Fermi function, exact-shell grouping, and selected cross-mu transition rules are those of `numerics/kane_8band_tightness.py`.

---

# 2. Charge-neutral state

The production quadrature gives

```text
mu = 0.1354615106 eV
cross-mu electron+hole population
   = 1.005140525e17 cm^-3.
```

This reproduces the controlling Experiment-12 reference population

```text
~1.005141e17 cm^-3.
```

---

# 3. Exact selected velocity strength and optical lower functional

For the broad `Eg..0.5 eV` window,

```text
R_B exact thermally weighted velocity strength
    = 3.987420232e28 cm^-3 (m/s)^2

L_B observable Fermi/Kubo lower functional
    = 1.223486457e28 cm^-3 (m/s)^2
```

Therefore

```math
\boxed{
\eta_F=L_B/R_B=0.306836598.
}
```

The selected active thermal population is

```text
n_active = 6.724111444e16 cm^-3.
```

The selected parent-shell population equals the active population at this numerical resolution, consistent with no exact kernel dimensions inside the contributing selected endpoint shell blocks.

---

# 4. Stable-rank / selectivity result

For every contributing selected active exact-shell block,

```math
\mathcal S_a^{act}
=\frac{r_a}{r_{st,a}}
```

remains unity to floating-point precision.

The production audit gives

```text
min S_a^act = 1.000000000000000
max S_a^act = 1.000000000000038
max |S_a^act - 1| ~= 3.84e-14.
```

Thus

```math
\boxed{\mathcal S_a^{act}=1}
```

is numerically exact for the contributing shell blocks in the present model to the precision of the calculation.

The broad HgCdTe theorem slack therefore contains no detectable active-shell stable-rank/selectivity penalty.

---

# 5. Capacity and observable tightness

The production quadrature's sampled-grid capacity is

```text
v_cap,sampled = 1.015610872e6 m/s.
```

The theorem does not use that sampled value as its final resource. Substituting the separately validated continuous ordinary supremum

```text
v_B^cap = 1.01764e6 m/s
```

gives

```math
\boxed{
\tau_{cap}^{act}
=\frac{R_B}{(v_B^{cap})^2 n_{active}}
=0.572622972.
}
```

The full observable active-population tightness is

```math
\boxed{
\tau_{obs}^{act}
=\frac{L_B}{(v_B^{cap})^2 n_{active}}
=0.175701685.
}
```

and the independent product closes exactly at numerical precision:

```math
\eta_F\tau_{cap}^{act}
=0.306836598\times0.572622972
=0.175701685.
```

Hence

```text
shell/global capacity factor ~= 0.573
Fermi/Kubo factor             ~= 0.307
product                        ~= 0.1757.
```

This reproduces the controlling Experiment-12 statement that the broad-window lower bound captures approximately `17.6%` of the selected optically active thermal population.

---

# 6. Comparison with the earlier moderate audit

Earlier moderate refined audit:

```text
eta_F                 ~= 0.3075
production tau_cap    ~= 0.5712
production tau_obs    ~= 0.1757
S_a^act               = 1 within floating point.
```

Production-scale audit:

```text
eta_F                 = 0.30684
tau_cap               = 0.57262
tau_obs               = 0.17570
S_a^act               = 1 within ~4e-14.
```

The individual factor split shifts by only a few parts in `10^-3` while their observable product is essentially unchanged at the manuscript precision relevant to the existing `~17.6%` statement.

---

# 7. Scientific interpretation

The production rerun strengthens the Experiment-13 conclusion:

```text
realistic broad-window HgCdTe active-shell coupling
    is locally singular-value isotropic;

its global state-count capacity is loose mainly because
    thermally occupied shells do not all reach the global v_B^cap;

and the optical observable lower functional is further reduced because
    the Fermi/Kubo inequality is not saturated across the realistic band structure.
```

Numerically,

```math
\boxed{
0.573\times0.307\approx0.176.
}
```

The stable-rank/selectivity theorem therefore survives a realistic material validation without falsely attributing the HgCdTe slack to coherence concentration.

---

# 8. Disposition

```text
production carrier-state regression:       PASS
production thermal velocity strength:      PASS
production active-population sum:          PASS
stable-rank/selectivity unity:              PASS
continuous-capacity substitution:           PASS
capacity decomposition closure:             PASS
Fermi/Kubo multiplicative closure:          PASS
~17.6% active tightness reconstruction:     PASS
```

The unified manuscript may now use rounded decomposition values

```text
~0.57 x ~0.31 ~= ~0.176
```

without labeling them merely as coarse-grid estimates. Exact extra significant figures remain unnecessary in the main text.
