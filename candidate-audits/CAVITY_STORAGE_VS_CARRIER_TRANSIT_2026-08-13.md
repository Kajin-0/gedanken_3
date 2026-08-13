# Candidate audit: optical storage versus carrier transit

**Date:** 2026-08-13
**Status:** MATHEMATICALLY CLEAN / HEAVY PRIOR ART / DO NOT OPEN EXPERIMENT 02 YET

## Device-engineer question

A thin absorber shortens carrier transit. A resonant cavity can restore high absorption by forcing photons to dwell in the structure. Did the detector become arbitrarily fast, or was delay transferred from carriers to photons?

## Prior-art result

The basic answer is already known in resonant-cavity-enhanced (RCE) detector literature. By 1995, RCE photodetector reviews explicitly treated photon lifetime as an additional high-speed limitation after transit time and capacitance. Later microring/RCE models incorporated photon lifetime directly into bandwidth and bandwidth-efficiency calculations. Therefore `cavity storage is another detector time constant` is not a novel claim.

The only potentially sharper object is a closed lower bound obtained by combining the thickness dependence of critical-coupling storage with carrier transit.

## Minimal one-port coupled-mode model

Let a single optical resonance have external energy-decay rate `Gamma_e` and useful absorber loss rate `Gamma_a`. Its on-resonance useful absorptance is

```math
A_0=\frac{4\Gamma_e\Gamma_a}{(\Gamma_e+\Gamma_a)^2}.
```

For a weak optically thin absorber, take

```math
\Gamma_a(d)=\kappa d,
```

where `kappa` is the absorber-loss rate per unit active thickness.

Conditional on useful absorption, the cavity-energy dwell-time distribution is exponential with total energy-decay rate

```math
\Gamma=\Gamma_e+\Gamma_a,
```

so

```math
\langle t_{ph}\rangle=\sigma_{ph}=1/\Gamma.
```

### Perfect on-resonance absorption

At critical coupling,

```math
\Gamma_e=\Gamma_a,
```

and therefore

```math
\boxed{\tau_{ph}=\frac{1}{2\kappa d}.}
```

Thus the optical storage penalty diverges as `1/d` when the useful absorber is made arbitrarily thin while perfect resonant absorption is retained.

### Required absorptance eta < 1

For a required on-resonance absorptance `A_0 >= eta`, the shortest cavity dwell time occurs at the most strongly overcoupled solution that still satisfies the absorptance requirement. Let

```math
s=\sqrt{1-\eta}.
```

The allowed overcoupled rate ratio at equality is

```math
\frac{\Gamma_e}{\Gamma_a}=\frac{1+s}{1-s},
```

which gives

```math
\boxed{
\tau_{ph,min}(d,\eta)
=\frac{1-\sqrt{1-\eta}}{2\kappa d}.
}
```

This makes the absorption-delay tradeoff explicit: relaxing peak efficiency permits lower optical storage delay, but the `1/d` divergence remains for every fixed `eta>0`.

## Carrier-transit response

For a deliberately simple symmetric p-i-n model with:

- uniform generation across thickness `d`;
- equal saturated electron and hole speed `v`;
- Ramo-Shockley induced current;

let

```math
T=d/v.
```

The normalized transit impulse response is triangular,

```math
h_{tr}(t)=\frac{2}{T}\left(1-\frac{t}{T}\right),
\qquad 0<t<T.
```

Its temporal variance is

```math
\boxed{\sigma_{tr}^2=\frac{T^2}{18}=\frac{d^2}{18v^2}.}
```

If cavity absorption time and carrier transport are sequential independent stages, convolution adds temporal variances exactly:

```math
\sigma_{tot}^2
=\sigma_{ph}^2+\sigma_{tr}^2.
```

Using the minimum cavity dwell time compatible with required absorptance `eta`,

```math
\boxed{
\sigma_{tot}^2(d)
=\frac{[1-\sqrt{1-\eta}]^2}{4\kappa^2d^2}
+\frac{d^2}{18v^2}.
}
```

Therefore neither `d -> 0` nor `d -> infinity` can make this response arbitrarily narrow.

The optimizing thickness is

```math
\boxed{
d_{opt}^2
=\frac{3}{\sqrt 2}\frac{v}{\kappa}
[1-\sqrt{1-\eta}].
}
```

and the minimum variance is

```math
\boxed{
\sigma_{min}^2
=\frac{1-\sqrt{1-\eta}}{3\sqrt 2\,\kappa v}.
}
```

For perfect on-resonance absorption (`eta=1`):

```math
d_{opt}^2=\frac{3v}{\sqrt 2\kappa},
```

```math
\boxed{
\sigma_{min}^2=\frac{1}{3\sqrt 2\,\kappa v}.
}
```

## Fabry-Perot interpretation

For a weak absorber of coefficient `alpha` occupying thickness `d` in a cavity of effective optical length `L_eff` and group velocity `v_g`, the useful absorption energy-decay rate is approximately

```math
\Gamma_a\simeq\frac{\alpha d v_g}{L_{eff}},
```

so

```math
\kappa\simeq\frac{\alpha v_g}{L_{eff}}.
```

Then

```math
\boxed{
\sigma_{min}^2
\simeq
\frac{[1-\sqrt{1-\eta}]L_{eff}}
{3\sqrt 2\,\alpha v_g v}.
}
```

Within this model, the optimized latency is therefore controlled by absorber strength, optical energy velocity/cavity length, and carrier velocity rather than by thickness after optimization.

## Why this is not yet a research contribution

The ingredients are established:

1. RCE detectors decouple absorption efficiency from electrical absorber thickness.
2. Photon lifetime is a known speed limit in RCE and microring photodetectors.
3. Carrier transit, RC delay, and photon lifetime are routinely combined in total response models.
4. Critical coupling and absorption-bandwidth tradeoffs are established coupled-mode theory.
5. Closed-form optical/electrical small-signal models already optimize resonant photodiode responsivity-bandwidth products.

The variance bound above is compact and pedagogically useful, but it appears to be an algebraic synthesis of known ingredients rather than a sufficiently distinct physical principle.

## Disposition

```text
Candidate: optical-storage/carrier-transit total-latency closure
Mathematics: valid within stated model
Device interpretation: useful
Novelty: weak / not established
Action: DO NOT open Experiment 02 around this result alone
```

A new experiment should require a microscopic or thermodynamic ingredient not already reducible to standard RCE coupled-mode + carrier-transport optimization.