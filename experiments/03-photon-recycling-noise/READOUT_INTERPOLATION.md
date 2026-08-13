# Readout interpolation

**Date:** 2026-08-13
**Status:** EXACT TOY READOUT RESULT / BRIDGE BETWEEN OCCUPANCY AND ENDPOINT COUNTING

## Model

Let the internal carrier-population fluctuation vector be `x` and let extraction occur independently from each pixel at rate `Gamma_e` per carrier.

The ideal extraction event-rate observable is

```math
j_e=\Gamma_e x+\zeta_e,
```

where `zeta_e` is the extraction shot-noise source and the same reaction enters the state equation with sign `-zeta_e`.

Now define a toy terminal current containing two components:

```math
\boxed{
I=gx+qj_e.
}
```

Here:

- `g` is an occupancy-sensitive current coefficient per carrier;
- `q j_e` is the endpoint extraction current.

This is not asserted to be a complete Shockley-Ramo photodiode model. It is the simplest interpolation between continuous population sensing and pure final-event counting.

## Exact PSD

Write

```math
I=(g+q\Gamma_e)x+q\zeta_e.
```

For the symmetric linear network,

```math
S_x=m(R+R^\dagger),
```

```math
S_{x\zeta_e}=-\Gamma_e mR,
```

and

```math
S_{\zeta_e}=\Gamma_e mI.
```

Substitution gives

```math
\boxed{
S_I(\omega)
=g(g+q\Gamma_e)S_x(\omega)
+q^2\Gamma_e mI.
}
```

Therefore every off-diagonal element is

```math
\boxed{
S_{I,ij}(\omega)
=g(g+q\Gamma_e)S_{x,ij}(\omega),
\qquad i\ne j.
}
```

## Limits

### Pure occupancy readout

For `q=0`,

```math
S_I=g^2S_x.
```

The full exchange cross-spectrum is visible.

### Pure endpoint counting

For `g=0`,

```math
S_I=q^2\Gamma_e mI.
```

The internal exchange contribution cancels exactly and output channels are independent white shot-noise streams.

### Mixed observable

For any `g != 0`, the internal cross-spectrum reappears, scaled by

```math
g(g+q\Gamma_e).
```

Thus observability changes continuously with the amount of carrier-state sensitivity in the terminal waveform.

## Independent readout noise

If independent additive electronics contribute diagonal PSD `S_r(omega)`,

```math
S_I^{meas}
=g(g+q\Gamma_e)S_x
+[q^2\Gamma_e m+S_r(\omega)]I.
```

Independent floors do not bias the cross-spectrum but dilute coherence and cross/auto ratios.

In particular, when an independent white floor dominates at high frequency, the measured normalized cross/auto ratio tends to zero even though the intrinsic cross-spectrum can retain its negative `1/omega^2` tail.

## Interpretation

The experiment should not classify devices only as `photoconductor` or `photodiode`. The physically relevant question is:

> How much of the terminal impulse response is sensitive to the internal carrier trajectory before final collection?

Pure endpoint counting erases conservative exchange correlations. Any occupancy, transit, weighting-field, charge-storage, or other trajectory-sensitive contribution can restore them.

A real junction detector requires its actual Shockley-Ramo / transport impulse response; `g` is only a pedagogical bridge parameter.