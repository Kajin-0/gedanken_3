# Experiment 02 — Isochronous Avalanche Photodetector

**Date:** 2026-08-13  
**Status:** ACTIVE DEVICE-PHYSICS HYPOTHESIS / FIRST REDUCED-ORDER DEVICE SURROGATE PASSED 20–30% GO GATE IN A RESTRICTED PARAMETER REGION / NOVELTY NOT ESTABLISHED

## Read first

1. `PROGRESS_LOG.md`
2. `REDUCED_ORDER_DEVICE_SURROGATE_2026-08-13.md`
3. `OPTIMAL_DELAY_MAP.md`
4. `RESIDUAL_JITTER_FLOOR.md`
5. `DIMENSIONLESS_FEASIBILITY_BOUND.md`
6. `DIRECTION_REVERSAL_TEST.md`
7. `FORWARD_REVERSE_ATTENUATION_BOUND.md`
8. `DEPTH_MAPPING_IMPLEMENTATION.md`
9. `REALISTIC_TARGET_INGAAS.md`
10. `MULTIPLICATION_REGION_REQUIREMENT.md`
11. `PRIOR_ART_AUDIT_2026-08-13.md`
12. `FIRST_PRINCIPLES_DERIVATION.md`

## Device-engineer question

In an APD/SPAD, random absorption depth creates a depth-dependent carrier-to-avalanche transit delay. Can the optical structure deliberately correlate optical propagation time with physical absorption depth so that the conditional mean trigger timestamp becomes independent of depth?

Plainly:

> Can a thick, efficient absorber retain its absorption volume while behaving, for event timing, more like a single timing depth?

## Exact timing condition

For random absorption coordinate `X`, define

```math
m(X)=t_o(X)+t_c(X)+t_e(X)+\mu_a(X).
```

The total variance is

```math
\boxed{Var(T)=Var[m(X)]+E[Var(T|X)].}
```

The absorption-position contribution to the conditional mean disappears exactly when

```math
\boxed{m(X)=constant.}
```

This removes only the position-dependent mean delay. Conditional avalanche stochasticity, drift/diffusion, local absorption-depth spread, optical dispersion, and electronics jitter remain.

## Prior-art narrowing

Generic longitudinal timing compensation is too close to established traveling-wave optical/electrical velocity matching. The active hypothesis is specifically **transverse absorption-depth compensation**:

> map physical absorption depth onto optical propagation time so that optical group delay cancels the depth-dependent carrier transit to the avalanche region.

For a designed mean depth `z_bar(x)` and constant velocities,

```math
t(x)=x/v_g+[d-z_bar(x)]/v_c,
```

with exact mean-depth compensation at

```math
\boxed{dz_bar/dx=v_c/v_g.}
```

Targeted journal and patent searching has not yet located this exact APD/SPAD design objective. That absence is not proof of novelty or priority.

## Exact optimal delay map

For a Maxwell-derived joint detected-photon distribution `p(x,z)`, define

```math
m_c(x)=E[t_c(Z)|X=x].
```

The variance-minimizing deterministic optical delay is

```math
\boxed{d_opt(x)=C-m_c(x).}
```

More generally include electrical propagation and mean avalanche buildup inside the conditional mean. The minimum deterministic residual is

```math
\boxed{E_X[Var(t_c(Z)|X)].}
```

Therefore the correct design target is the **conditional mean carrier delay**, not merely a moving optical-mode centroid.

## Residual-jitter benchmark

For the 90%-absorption distributed benchmark, normalize time by

```math
T_0=d/v_c.
```

The removable between-slice depth variance is

```math
\boxed{\sigma_{depth}^2/T_0^2=0.0651549.}
```

After perfect deterministic mean compensation, the leading reduced-order residual is

```math
\boxed{
\frac{\sigma_{floor}^2}{T_0^2}
=\left(\frac{\sigma_\perp}{d}\right)^2
+\frac{1.35363}{Pe}
+\left(\frac{\sigma_{other}}{T_0}\right)^2.
}
```

A 30% RMS improvement requires

```math
\boxed{\sigma_{floor}^2/T_0^2\le0.062600.}
```

This is the current go/no-go criterion.

## First realistic scale

Use the present InGaAs/InP scale only as a device surrogate:

```text
d = 2 um
v0 = 5e4 m/s
vg = 7.5e7 m/s
T0 = 40 ps
L = 3.0 mm
```

The removable 90%-absorption depth term is about

```text
10.2 ps RMS.
```

No final epistructure or operating field has been selected.

## First combined device-surrogate result

`REDUCED_ORDER_DEVICE_SURROGATE_2026-08-13.md` and `numerics/isochronous_device_surrogate.py` combine:

```text
Pe = 100
unresolved local depth RMS = 100 nm
avalanche buildup RMS = 5 ps
electronics RMS = 2 ps
optical pulse/dispersion RMS = 1 ps
```

At this stress-test point, analytic variance decomposition gives

```text
direct depth-sensitive control  12.645 ps RMS
forward matched                   7.460 ps RMS
decorrelated same-marginal       16.253 ps RMS
reverse anti-matched             21.741 ps RMS
```

A `N=1,000,000` event inverse-Gaussian first-passage Monte Carlo gives

```text
direct       12.650 ps RMS
forward       7.464 ps RMS
decorrelated 16.265 ps RMS
reverse      21.744 ps RMS
```

Thus

```math
\boxed{1-\sigma_f/\sigma_{direct}\simeq41.0\%.}
```

The first combined surrogate therefore passes the selected 20–30% practical go gate.

This is **not** a Maxwell/TCAD validation. It only shows that diffusion plus several-picosecond avalanche/electronics floors do not automatically kill the concept.

## Avalanche/transport feasibility boundary

At fixed

```text
sigma_perp = 100 nm
electronics RMS = 2 ps
optical RMS = 1 ps
```

the maximum avalanche RMS compatible with at least 30% total improvement is approximately

```text
Pe=20   -> impossible even at zero avalanche jitter
Pe=30   -> 4.35 ps
Pe=50   -> 6.92 ps
Pe=75   -> 7.89 ps
Pe=100  -> 8.34 ps
Pe=150  -> 8.76 ps
Pe=200  -> 8.96 ps
Pe=300  -> 9.16 ps
```

This makes the multiplication-region requirement explicit. Low-buildup-jitter multiplication is enabling prior art and remains a prerequisite, not the proposed novelty.

## Forward/reverse causal signature

At exact full-depth matching, the ideal between-slice timing terms obey

```text
forward matched      -> zero between-slice mean-delay variance
ordinary depth term  -> 0.2553 T0 RMS
reverse anti-match   -> 0.5105 T0 RMS
```

The first combined surrogate retains a large total contrast:

```text
forward  7.46 ps RMS
reverse 21.74 ps RMS.
```

Direction reversal remains the strongest causal discriminator because it changes the sign of the optical delay gradient while keeping the same underlying semiconductor depth map.

## Important correction — geometric match != total-jitter minimum in general

The earlier intuitive claim that the minimum total jitter should occur exactly at the geometric isochronous bias is **REJECTED**.

Let

```math
r=v/v_0.
```

For the reduced-order model with locally fixed diffusion coefficient,

```math
V_f(r)=
A(1-1/r)^2+a/r^2+\beta/r^3+c.
```

The deterministic conditional-mean slope is nulled at

```math
r=1.
```

But the complete variance is minimized at

```math
\boxed{r_*\approx1.2815}
```

for the current parameter point, because larger drift speed reduces diffusion and local-depth transit variance while introducing only a modest deterministic mismatch.

Therefore a realistic bias experiment must distinguish:

```text
conditional-mean slope null -> geometric isochronous point
total-jitter minimum        -> can shift with field-dependent residual variance
forward/reverse asymmetry   -> stronger causal test
```

A future TCAD/Monte Carlo treatment must model both conditional means and conditional variances versus field.

## Mapping tolerance at the present surrogate point

If `q` multiplies the ideal compensation coefficient,

```math
\sigma_f^2(q)/T_0^2=F+Var(U)(q-1)^2.
```

The present surrogate permits approximately

```text
>=20% improvement -> |q-1| <= 0.669
>=30% improvement -> |q-1| <= 0.467
>=40% improvement -> |q-1| <= 0.135
```

so a visible 20–30% effect does not require sub-percent map accuracy. Approaching the maximum improvement does require tighter matching.

## Current prior-art status

Known literature already covers:

- absorption/generation-position timing jitter in APDs/SPADs;
- waveguide/nanophotonic absorption engineering;
- lateral waveguide APDs;
- traveling-wave optical/electrical velocity matching;
- position-dependent carrier transit engineering;
- absorber-transit optimization;
- low-buildup-jitter/dead-space multiplication engineering;
- isochronous timing concepts in other detector systems.

Current disposition:

```text
Distinct transverse-depth compensation hypothesis: YES
Reduced-order feasibility: PASSES a restricted parameter region
Real Maxwell/transport implementation: NOT ESTABLISHED
Novelty: NOT ESTABLISHED
Priority language: NOT AUTHORIZED
Paper drafting: NOT AUTHORIZED
```

## Current frontier

Do not add another generic timing theorem.

The next hard step is a **finite discrete optical-depth ladder** that approximates

```math
d_opt(x)=C-E[t_c(Z)|X=x]
```

using a small number of depth-localized absorbing sections and explicit optical delay increments.

Determine:

1. the minimum number of sections needed to retain most of the continuous-map timing benefit;
2. depth/localization and optical-delay tolerances;
3. whether the forward/reverse signature remains above the 20–30% gate under those discretization errors.

If a small ladder cannot preserve the effect, the continuously migrated-mode implementation is likely too fabrication-sensitive to justify full Maxwell/TCAD work.

## Hard rules

- Do not claim novelty or priority.
- Do not draft a paper yet.
- Do not conflate this with ordinary longitudinal traveling-wave velocity matching.
- Do not claim zero detector jitter; only one conditional-mean depth term is being targeted.
- Preserve the correction that total-jitter minimum and geometric mean-delay match can differ.
- Kill the device realization if realistic localization, diffusion, avalanche buildup, or implementation error removes the material timing benefit.
