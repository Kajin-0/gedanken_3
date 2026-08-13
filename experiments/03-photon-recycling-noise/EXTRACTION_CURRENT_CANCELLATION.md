# Ideal extraction-current cancellation

**Date:** 2026-08-13
**Status:** EXACT NO-GO RESULT FOR LINEAR POISSON EXTRACTION READOUT / DEVICE-CLASS BOUNDARY

## Question

Experiment 03 first derived a sign-changing cross-spectrum for the **internal carrier populations** of two exchange-coupled pixels. Does a photovoltaic pixel necessarily expose that same spectrum in its measured terminal current?

No.

If the terminal observable is idealized as counting final carrier-extraction events, the internal population correlation can cancel exactly from the output current.

## 1. Linear two-pixel state model

Let `x=(x1,x2)^T` be carrier-number fluctuations about equal stationary mean `m`.

Split the local non-transfer loss rate into measurable extraction and all other loss:

```math
\gamma=\Gamma_e+\Gamma_o.
```

Conservative exchange occurs at rate `k` per carrier. The drift matrix is

```math
M=
\begin{pmatrix}
\gamma+k & -k\\
-k & \gamma+k
\end{pmatrix}.
```

The internal fluctuation process obeys

```math
\dot x=-Mx+\xi.
```

For stationary Poisson birth/death/exchange reactions,

```math
Q_\xi=2mM,
```

so with

```math
R(\omega)=(M+i\omega I)^{-1},
```

```math
\boxed{
S_x(\omega)
=R Q_\xi R^\dagger
=m(R+R^\dagger).
}
```

This is the sign-changing internal spectrum already derived in `CURRENT_STATE.md`.

## 2. Extraction is both an output event and a state-loss event

Let `\zeta_e` denote the white shot-noise source associated with extraction events. Its two-sided event-rate PSD is

```math
D_e=\Gamma_e m I.
```

The same extraction event that appears at the terminal also removes one carrier from the internal state. Therefore the state equation contains `-zeta_e`.

The ideal extraction-counting current in event-rate units is

```math
\boxed{
j_e=\Gamma_e x+\zeta_e.
}
```

Because `zeta_e` enters the state with the opposite sign,

```math
S_{x\zeta_e}
=-R D_e,
```

```math
S_{\zeta_e x}
=-D_e R^\dagger.
```

Hence

```math
S_{j_e}
=\Gamma_e^2 S_x
+D_e
+\Gamma_e(S_{x\zeta_e}+S_{\zeta_e x}).
```

Substitute the expressions above:

```math
S_{j_e}
=\Gamma_e^2 m(R+R^\dagger)
+\Gamma_e m I
-\Gamma_e^2 m(R+R^\dagger).
```

Therefore

```math
\boxed{
S_{j_e}(\omega)=\Gamma_e m I.
}
```

In electrical-current units multiply by `q^2` for the two-sided PSD convention used here.

Thus, in this ideal model:

```text
internal carrier populations: dynamically cross-correlated
final extraction streams:     white Poisson and mutually uncorrelated
```

The cancellation is exact for every frequency.

## 3. Exact point-process interpretation

The result is stronger than the chemical-Langevin approximation.

Assume:

1. external/thermal generation events form independent Poisson processes;
2. carriers do not interact, so every generated excitation evolves independently;
3. each excitation may hop between pixels any number of times;
4. it eventually terminates in exactly one sink, such as extraction from pixel 1, extraction from pixel 2, nonradiative loss, or radiative escape;
5. the measured current counts only the final extraction event.

Each Poisson generation event can then be assigned an independent random mark consisting of:

```text
(final sink, random delay to that sink).
```

Independent marking, thinning, random displacement, and superposition of Poisson processes preserve the Poisson property. Different final-sink classes are independent Poisson streams.

Therefore the extraction-current result is exact even if the internal routing contains many exchange steps and non-exponential independent delays.

This is closely related to the classical Poisson-output property of `M/G/infinity` systems and open infinite-server networks.

## 4. Counterintuitive consequence: mean crosstalk without noise correlation

A localized steady optical input in pixel 1 can still change the **mean** extraction rates in both pixels because some carrier lineages are routed to pixel 2 before final extraction.

Thus a detector may have ordinary deterministic optical crosstalk while its ideal stationary extraction currents have

```math
\boxed{S_{I,12}(\omega)=0.}
```

under independent Poisson generation.

Mean crosstalk therefore does **not** imply passive current-noise cross-correlation.

The earlier fluctuation/response closure applies to the internal occupancy observable, not automatically to an extraction-counting observable.

## 5. Why SPAD optical crosstalk is different

SPAD optical crosstalk is a branching process rather than conservative one-for-one routing. An avalanche in one pixel is already recorded while hot carriers emit secondary photons that can trigger additional avalanches in neighboring pixels.

One primary event can therefore create multiple measured output events, producing genuine inter-pixel count correlations. This is why dark-event timing correlations can measure SPAD optical crosstalk without contradicting the cancellation theorem above.

## 6. Device-class boundary

### Occupancy-sensitive photoconductor

Under fixed bias, terminal current is approximately proportional to instantaneous carrier population:

```math
\delta I_i=g_{I,i}x_i.
```

The internal exchange cross-spectrum is directly observable, apart from electrical filtering and independent additive noise.

### Ideal extraction-counting photodiode

If terminal current records only final extraction events, the cross-spectrum cancels exactly in the linear Poisson model.

### Real junction photodiode

A real terminal current is not necessarily pure endpoint counting. Carrier motion induces current through the Shockley-Ramo weighting field before final collection, and finite transit, diffusion, junction capacitance, charge storage, and distributed generation-recombination can couple internal state dynamics to the terminals.

Therefore a real photovoltaic pixel lies between the two ideal observables and requires a transport/Ramo readout model before Experiment 03 predicts a measurable cross-spectrum.

## 7. Conditions that break the cancellation

The no-go theorem can fail if any assumption of independent one-for-one routing fails, including:

- branching or gain: one excitation produces multiple measured descendants;
- non-Poisson or spatially correlated generation;
- carrier-carrier interactions / nonlinear recombination or space charge;
- occupancy-sensitive or Shockley-Ramo current before final extraction;
- common electronic coupling between output channels;
- a measurement in which one carrier lineage contributes to more than one terminal waveform.

Finite independent routing delays by themselves do **not** break the exact Poisson-departure result.

## 8. Numerical validation

An exact Gillespie simulation was run for

```text
gamma = 1
gamma_e = 0.6
gamma_o = 0.4
k = 1.5
mean population m ~ 2 per pixel
```

The internal carrier cross/auto ratio approaches the theoretical limits

```text
low frequency:  +k/(gamma+k) = +0.60
high frequency: -k/(gamma+k) = -0.60
```

with simulated band averages approximately `+0.57` and `-0.60`.

The simultaneously counted extraction streams had cross/auto ratios consistent with zero in every tested frequency band (typically at the `10^-3` to `10^-2` level for the finite run), while their auto-spectrum was white.

A reproducible simulation script is stored in `numerics/extraction_current_cancellation_gillespie.py`.

## 9. Prior-art boundary

The mathematics has clear classical roots:

- Mirasol (1963), DOI `10.1287/opre.11.2.282`, proved Poisson output for the `M/G/infinity` queue;
- Harrison & Lemoine (1981), DOI `10.2307/3213306`, treated open networks of infinite-server queues with independent customer motion;
- semiconductor-detector literature has long emphasized that junction current and GR noise require a Shockley-Ramo/transport coupling treatment, notably Dąbrowski (1989), DOI `10.1016/0079-6727(89)90004-9`.

Therefore do **not** claim Poisson-output cancellation as new stochastic-process theory.

The potentially useful detector result is the device-observable distinction:

```text
same internal photon-recycling exchange
+ occupancy readout   -> cross-spectrum visible
+ ideal endpoint count -> cross-spectrum can vanish exactly
```

Novelty of that detector-facing formulation is not established.