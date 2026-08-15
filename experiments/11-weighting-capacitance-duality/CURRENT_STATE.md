# Current State — Experiment 11: Weighting-Field / Capacitance Duality

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** **EXACT PROMPT-SIGNAL / CAPACITANCE IDENTITY DERIVED / GENERALIZED TO NONUNIFORM GENERATION / NOVELTY COLLISION STRONG / CLOSED BY DEFAULT**

## Read first

1. `WEIGHTING_CAPACITANCE_DUALITY_STEP_2026-08-14.md`
2. `PROGRESS_LOG.md`

## Minimal model

Homogeneous two-terminal active volume `Omega`, volume `V`, permittivity `epsilon`, mobilities `mu_e`,`mu_h`, bias `V_b`, no space charge/trapping/multiplication, low-field drift.

Weighting field:

```math
\mathbf E_w=-\nabla\psi,
```

with unit sensing-electrode potential and zero return-electrode potential.

Because the physical bias problem has the same boundary-value equation,

```math
\boxed{\mathbf E_b=V_b\mathbf E_w.}
```

For a newly created electron-hole pair at `r`,

```math
\boxed{
i_{pair}(\mathbf r,0^+)
=e(\mu_e+\mu_h)V_b|\mathbf E_w(\mathbf r)|^2.
}
```

The total detector capacitance obeys

```math
\boxed{
C_{tot}=\int_{all}\epsilon(\mathbf r)|\mathbf E_w|^2dV.
}
```

Therefore for generation probability density `p(r)` bounded by `p_max`,

```math
\boxed{
\frac{\langle i_{pair}(0^+)\rangle}{C_{tot}}
\le
\frac{e(\mu_e+\mu_h)V_b}{\epsilon}p_{max}.
}
```

For uniform generation,

```math
\boxed{
\frac{\langle i_{pair}(0^+)\rangle}{C_{tot}}
\le
\frac{e(\mu_e+\mu_h)V_b}{\epsilon V}.
}
```

Equality holds in the ideal homogeneous case when all electrostatic field energy lies in the active volume.

## Novelty disposition

The core geometry cancellation reduces to established homogeneous-medium conductance/capacitance duality

```math
G/C=\sigma/\epsilon,
\qquad
RC=\epsilon/\sigma,
```

and therefore to Maxwell dielectric relaxation.

The nonuniform-generation extension uses the same reciprocal field-product sensitivity kernel long established in lead-field / electrical-impedance sensitivity theory.

Fast-detector literature already treats weighting-field uniformity and capacitance as coupled geometry constraints.

```text
EXPERIMENT 11 CLOSED BY DEFAULT AS A NOVELTY / MANUSCRIPT PATH.
```

Retain the prompt-slew inequality as a useful design identity, not a novelty claim.

## Next action

Return to premise screening. Do not add generic readout-noise or timing models to rescue this branch.
