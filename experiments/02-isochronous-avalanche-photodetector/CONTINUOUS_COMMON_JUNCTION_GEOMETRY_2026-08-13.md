# Continuous common-junction geometry

**Date:** 2026-08-13  
**Status:** CONSTRUCTIVE ARCHITECTURE FORK / LOCALIZATION-TRANSPORT TRADEOFF IDENTIFIED / NOVELTY NOT ESTABLISHED

## 1. Constraint inherited from the readout no-go

The first demonstrator should not consist of three electrically independent SPAD/APD sections. Section-specific electrical paths can reproduce the section-level timing correction.

The optical depth states must therefore live inside one continuous/common electrical detector degree of freedom.

## 2. Two implementation routes

### Route A — uniform absorber, optical-field localization

Use one continuous depleted InGaAs absorber and move the optical absorption distribution among three target depths while the electrical field and multiplication region remain continuous along `x`.

Advantages:

- no additional absorber/barrier heterointerfaces;
- carrier transport remains closest to the original drift-diffusion surrogate;
- cleanest physical interpretation.

Risk:

- optical conditional-depth localization is difficult.

At the current N=3, Pe=100, 5-ps avalanche, 2-ps electronics, 1-ps optical assumptions, perfect section transfer permits at most about

```text
sigma_z ~ 175 nm RMS
```

before the historical 30% gate is exhausted. The previous coupled-mode transfer calculation showed that with persistent state-transfer error near 5%, roughly `100 nm RMS` localization is the safer target.

### Route B — multiple thin absorber sheets inside one continuous junction

Place three absorbing sheets near the current target depths

```text
z ~ 0.29, 0.96, 1.62 um
```

inside one common depleted APD, and steer successive optical sections predominantly into successive sheets.

A uniformly absorbing sheet of physical thickness `t_s` has the scale

```math
sigma_z ~= t_s/sqrt(12).
```

Thus:

```text
100-nm sheet -> ~29-nm depth RMS
200-nm sheet -> ~58-nm depth RMS
300-nm sheet -> ~87-nm depth RMS
```

This makes the optical localization requirement much easier than confining a telecom-wavelength mode to a ~100-nm slice of a uniform 2-um absorber.

## 3. The heterointerface penalty

The thin-sheet route introduces additional material interfaces. In InGaAs/InP APDs, hole trapping at the absorption/multiplication heterointerface is established high-speed physics and grading layers are used to suppress it.

Represent all added sheet/interface transport by a conditional delay

```math
T_{int}=mu_j+delta T_{int}
```

for sheet `j`.

Stable sheet-dependent means `mu_j` can be included in the isochronous delay map. The dangerous term is the conditional variance

```math
E[Var(delta T_int|j)].
```

which adds directly to the post-compensation floor and cannot be removed by deterministic optical delay.

At N=3, using the current other assumptions, the maximum additional independent interface-delay RMS compatible with the historical 30% gate is approximately:

```text
local depth RMS  50 nm -> interface budget ~3.36 ps RMS
local depth RMS 100 nm -> interface budget ~2.88 ps RMS
local depth RMS 125 nm -> interface budget ~2.46 ps RMS
local depth RMS 150 nm -> interface budget ~1.82 ps RMS
```

Therefore a multi-sheet design is useful only if graded interfaces keep added stochastic transport on the few-picosecond scale.

## 4. New implementation tradeoff

```text
uniform absorber:
    cleaner transport
    harder optical localization

multiple thin absorber sheets:
    easier localization
    harder heterointerface transport
```

Neither route currently dominates.

## 5. Preferred first Maxwell/transport comparison

Do not simulate an arbitrary full device yet. Compare two deliberately minimal cross sections:

1. one continuous 2-um absorber with a vertically shifted/supermode-localized optical field;
2. three thin absorbing sheets in one common depleted junction, with ideal grading first and then an explicit interface-delay penalty.

For both, extract the actual joint absorbed-power distribution `p(x,z)`, compute `E[t_c|x]` and `Var(t_c|x)`, and evaluate the same forward/reverse impulse-response variance.

The thin-sheet route should be killed if realistic interface transport contributes more than a few picoseconds RMS; the uniform route should be killed if Maxwell localization cannot keep the absorption-weighted depth spread inside the previously derived 30% surface.

Do not claim novelty or begin manuscript construction.