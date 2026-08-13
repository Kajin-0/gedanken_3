# Forward/reverse optical-direction causal test

**Date:** 2026-08-13
**Status:** STRONG EXPERIMENTAL DISCRIMINANT

## 1. Forward matched direction

Let the fixed device coordinate be `x in [0,L]`. Design the conditional mean absorption depth as

```math
z_bar(x)=s x,
```

with avalanche region at depth `d` and constant carrier speed `v_c`.

For forward optical propagation from `x=0`,

```math
t_forward(x)=x/v_g+[d-sx]/v_c.
```

The derivative is

```math
dt_forward/dx=1/v_g-s/v_c.
```

At

```math
\boxed{s=v_c/v_g,}
```

```math
\boxed{t_forward(x)=d/v_c}
```

for every mapped absorption position.

## 2. Reverse optical propagation

Illuminate the same physical device from `x=L`. The optical propagation delay to fixed coordinate `x` is

```math
(L-x)/v_g,
```

while the semiconductor carrier-depth map is unchanged. Therefore

```math
t_reverse(x)=(L-x)/v_g+[d-sx]/v_c.
```

At the forward matching slope `s=v_c/v_g`,

```math
\boxed{dt_reverse/dx=-2/v_g.}
```

Thus reversing optical propagation changes the correlation from compensating to reinforcing.

For exact full-depth mapping,

```math
L=d v_g/v_c,
```

so the deterministic reverse-direction timestamp spans

```math
\boxed{Delta t_reverse=2d/v_c.}
```

whereas the ideal forward mapped mean has zero position spread.

## 3. Why this is a strong control

Forward/reverse comparison uses the same:

- absorber and multiplication epistructure;
- electric-field profile;
- carrier transport physics;
- avalanche statistics;
- contacts and readout electronics;
- nominal optical path geometry.

The principal changed quantity is the sign of the optical propagation-time gradient relative to the fixed carrier-depth gradient.

This provides a causal signature of delay-correlation physics rather than a generic comparison between a nanophotonic detector and a control detector.

## 4. Important caveats

The two directions will not automatically have identical detected-photon weighting because distributed absorption attenuates the optical field. A realistic analysis must compute separate joint distributions `p_forward(x,z)` and `p_reverse(x,z)` from Maxwell propagation.

The most informative device therefore aims for:

- sufficiently weak/distributed absorption per unit length that both directions sample much of the mapping;
- or a symmetric/coupled optical structure designed to make forward and reverse marginal absorption comparable.

Even when the marginals differ, the exact prediction follows from the measured/simulated joint absorption distributions and the optimal-delay framework.

## 5. Experimental prediction

A genuine isochronous device should show:

```text
forward matched direction -> timing minimum
reverse direction         -> broadened or anti-matched timing
```

with the contrast changing predictably with bias because `v_c(E)` changes while the photonic depth map is fixed.

The combination of **direction reversal + bias tuning** is a particularly strong falsification test.