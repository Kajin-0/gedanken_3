# Experiment 12 — Failed Universal Response-Time to Thermal-Generation Corollary

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Disposition:** **FAILED AS A UNIVERSAL DETECTOR COROLLARY / COUNTEREXAMPLE IDENTIFIED / DO NOT USE IN MANUSCRIPT CLAIMS**

## 1. Tempting extension

The controlling Experiment-12 theorem bounds equilibrium thermally excited quasiparticle population by low-energy direct-interband optical spectral weight.

It is tempting to convert this immediately into a thermal generation-rate bound by combining

```math
N=G\tau
```

with a detector response-time requirement `tau <= tau_max`.

That would suggest schematically

```math
G_{th}
\stackrel{?}{\ge}
\frac{n_{th}}{\tau_{response}}
```

and hence an absorption–generation–speed inequality.

This is **not universal**.

---

## 2. Why the argument fails

The residence/lifetime that determines equilibrium thermal generation-recombination turnover need not be the same timescale that determines detector response.

A simple counterexample is a depleted photovoltaic detector:

```text
intrinsic bulk recombination lifetime can be very long;
thermal generation can therefore be small;
photoexcited carriers can nevertheless be swept out rapidly by drift;
terminal response can be transit-time / RC limited rather than recombination-lifetime limited.
```

Thus one may have

```math
\tau_{recomb}\gg\tau_{transit}
```

without contradiction.

The equilibrium identity

```math
n_{eq}=G_{th}\tau_{recomb}
```

therefore does not imply

```math
G_{th}\ge n_{eq}/\tau_{response}.
```

External collection can shorten the nonequilibrium carrier residence time without setting the intrinsic equilibrium generation lifetime.

---

## 3. Architecture-specific case where the conversion is valid

For a simple relaxation-limited photoconductor or other detector in which the **same** single-particle lifetime controls

```text
equilibrium generation-recombination occupancy,
photoconductive gain,
and signal reset,
```

one may use

```math
G_{th}=n_{th}/\tau
```

and combine Experiment 12 with a specified `tau`.

But this is an architecture-specific corollary, not a theorem for direct interband photodetectors in general.

---

## 4. Relation to established IR detector figures of merit

Classic infrared-detector theory treats thermal generation rate directly. Piotrowski and Rogalski/Gawron introduced the material criterion based on

```math
\alpha/G_{th},
```

while later comparisons often use lifetime-dependent forms such as

```math
\alpha\sqrt\tau.
```

The fact that long carrier lifetime can improve generation-limited sensitivity is established and must not be collapsed into a universal detector response-time penalty.

Experiment 12 is therefore complementary:

```text
Experiment 12:
    low-energy direct-interband optical spectral weight -> minimum equilibrium quasiparticle population, conditional on v_*;

classic detector FOM:
    useful absorption -> thermal generation/recombination rate and detector noise.
```

A universal bridge between the two requires an additional kinetic hypothesis.

---

## 5. Final disposition

```text
DO NOT CLAIM:
    G_th >= n_th / tau_response
for arbitrary photodetectors.
```

Retain the thermal-population theorem as the robust result.

If a later manuscript discusses dark current or generation noise, it must either:

```text
state a specific recombination/collection kinetic model;
use an independently known thermal generation rate;
or remain at the level of a necessary population/material admissibility condition.
```
