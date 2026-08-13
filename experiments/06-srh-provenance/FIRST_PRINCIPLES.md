# Experiment 06 — SRH provenance from complementary Ramo pulses

**Date:** 2026-08-13  
**Status:** PROVISIONAL / IDEAL DISCRIMINATOR DERIVED / NOVELTY NOT ESTABLISHED

## Question

Can a linear depleted photodiode distinguish a photon event from SRH thermal generation by retaining the individual electron/hole Shockley-Ramo waveforms?

The waveform physics itself is prior art. Maione et al., Phys. Rev. B 83, 155309 (2011), explicitly model individual trap capture/emission current pulses. The candidate is only the event-provenance use of the complementary pulse pair.

## Planar diode

For `0<x<d`, read electrode at `x=d`, weighting potential `phi_w=x/d`, constant drift speeds:

```math
i_e(t;x)=\frac{qv_e}{d}\,1_{0<t<(d-x)/v_e},
```

```math
i_h(t;x)=\frac{qv_h}{d}\,1_{0<t<x/v_h}.
```

Integrated induced charges:

```math
Q_e=q(1-x/d),
\qquad
Q_h=qx/d,
```

so

```math
\boxed{Q_e+Q_h=q.}
```

A photon at `t=0` launches both carriers simultaneously:

```math
i_\gamma=i_e+i_h.
```

Before either carrier is collected,

```math
i_\gamma(0^+)=q(v_e+v_h)/d,
```

independent of absorption depth in this ideal planar model.

## SRH cycle

Use trap states `0=empty`, `1=filled` and generation transitions

```text
0 -> 1 + mobile hole      rate r_h
1 -> 0 + mobile electron  rate r_e.
```

The mean full-cycle generation rate is

```math
\boxed{g=\frac{r_e r_h}{r_e+r_h}.}
```

The opposite-carrier launch times are separated by exponential dwell times. Thus a same-trap SRH pair is sequential, whereas a photon pair is simultaneous.

The trap charge change does not add a complete-pair impulse: at each local transition the trap charge change and newly created mobile carrier appear at the same position and cancel instantaneously in weighting charge; subsequent induced current comes from carrier motion.

## Ideal distinguishability

For perfect continuous-time waveform observation,

```text
photon: Delta t = 0 with probability 1
SRH:    Delta t has a continuous exponential distribution
```

so

```math
P_{SRH}(\Delta t=0)=0.
```

Under the isolated-lineage model the ideal Bayes error is therefore zero. This is an observability statement, not a practical detector claim.

## Finite timing resolution

For one exponential dwell rate `r` and effective coincidence resolution `delta_t`,

```math
P_{unresolved}=1-e^{-r\delta t}\simeq r\delta t.
```

For one alternating trap, the same-trap false-doublet rate is

```math
R_{same}
=g[(1-e^{-r_e\delta t})+(1-e^{-r_h\delta t})].
```

At small window,

```math
\boxed{R_{same}\simeq r_e r_h\delta t.}
```

## Many-trap accidental floor

For trap `a`, let

```math
g_a=r_{e,a}r_{h,a}/(r_{e,a}+r_{h,a})
```

and total electron/hole half-event rate

```math
G=\sum_a g_a.
```

Cross-trap opposite-carrier coincidences in a symmetric `+/-delta_t` window occur at approximately

```math
\boxed{
R_{cross}\simeq
2\delta t\left[G^2-\sum_a g_a^2\right].
}
```

For many weak traps this approaches `2 G^2 delta_t`.

## Ramo charge as lineage fingerprint

A same-position pair satisfies

```math
Q_e+Q_h=q.
```

For unrelated electron and hole half-events at `x_e` and `x_h`,

```math
(Q_e+Q_h-q)/q=(x_h-x_e)/d.
```

Require

```math
|Q_e+Q_h-q|<\epsilon q.
```

For independent uniformly distributed trap depths, the random cross-trap acceptance is

```math
\boxed{p_Q=2\epsilon-\epsilon^2.}
```

Thus

```math
R_{cross,Q}\simeq
2\delta t(2\epsilon-\epsilon^2)
\left[G^2-\sum_a g_a^2\right].
```

The complementary fractional charges are the strongest device-specific provenance variable found so far.

## Prior-art boundary

Already established: trap capture/emission terminal pulses and their correlations; RTS/trap spectroscopy; coincidence rejection with multiple detectors; APD photo/dark discrimination through multiplication-history pulse heights; single-e-h-pair resolution in specialized cryogenic detectors.

No exact prior-art match to the single-linear-photodiode complementary-Ramo provenance veto has been found in the targeted search. Absence is not proof of novelty.

## Next step

Test whether any physically plausible front end can preserve sub-electron/fractional-charge information and sub-transit-time timing simultaneously without a nonlinear gain stage erasing provenance.