# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11  
**Status:** first logical step completed; one explicit counterexample establishes insufficiency of a single reference `D*` for arbitrary-signal SNR. No generalized theory yet.

---

## 1. Starting point

Two detectors satisfy

```math
D_A^*=D_B^*,
```

with

```math
\tau_A=1\ \mathrm{ns},
\qquad
\tau_B=1\ \mathrm{s}.
```

The question is whether the equality of conventional specific detectivity alone guarantees equal detection ability for an arbitrary optical signal.

---

## 2. First correction to the question

Bare equality of `D*` is incomplete unless its measurement conditions are specified.

For a narrowband spectral-density convention,

```math
D^*(f)=\frac{\sqrt A\,R(f)}{n_y(f)}.
```

Therefore the comparison depends on wavelength, temporal frequency/protocol, active area, estimator/noise bandwidth, bias, temperature, and the actual signal and noise transfer functions.

For the first thought experiment, interpret the given equality as **equal low-frequency/reference-condition `D*`**.

---

## 3. Simplest physically consistent model

Choose equal area `A`, equal low-frequency responsivity `R0`, and equal additive white output-noise density `n0` for the two detectors. Let only their normalized first-order temporal responses differ:

```math
H_i(f)=\frac{1}{1+i2\pi f\tau_i}.
```

Then at low frequency

```math
D_{A,0}^*=D_{B,0}^*=\frac{\sqrt A\,R_0}{n_0}.
```

The noise is placed after the detector pole, representing a physically allowed readout-noise-dominated limit. This is deliberately only one admissible realization.

---

## 4. Simplest comparison measurement

Illuminate both detectors with the same sinusoidal optical-power component of RMS amplitude `P_m` at frequency `f_m`. Estimate that component with the same equivalent noise bandwidth `B`.

The RMS signal is

```math
s_i=R_0|H_i(f_m)|P_m,
```

and RMS noise is

```math
\sigma_n=n_0\sqrt B.
```

Hence

```math
\mathrm{SNR}_i
=\frac{P_mD_0^*}{\sqrt{AB}}|H_i(f_m)|.
```

Thus

```math
\frac{\mathrm{SNR}_A}{\mathrm{SNR}_B}
=\frac{|H_A(f_m)|}{|H_B(f_m)|}.
```

For `f_m=1 Hz`, `tau_A=1 ns`, `tau_B=1 s`,

```math
|H_A|\approx1,
\qquad
|H_B|\approx0.157,
```

so

```math
\boxed{\mathrm{SNR}_A/\mathrm{SNR}_B\approx6.36.}
```

This one allowed optical measurement is sufficient to disprove the implication

```text
equal reference D* -> equal SNR for every optical signal.
```

---

## 5. Critical qualification

This does **not** establish that speed itself universally improves SNR.

If dominant noise is generated before and filtered by the same pole,

```math
n_i(f)=n_0|H_i(f)|,
```

then the attenuation of signal and noise can cancel in narrowband SNR.

Also, if equality is instead specified as

```math
D_A^*(f_m)=D_B^*(f_m)
```

using each detector's actual responsivity and noise density at the measurement frequency, then equal area, optical input, and bandwidth imply equal narrowband tone SNR by definition.

The first result is therefore about **insufficient information**, not a universal speed penalty.

---

## 6. What has been established

**DERIVED:** A single conventional `D*` equality at one reference condition is not sufficient to guarantee equal measurement SNR for arbitrary optical signals.

**DERIVED:** Temporal signal transfer and noise transfer cannot be omitted from the statement of the detection problem.

**COUNTEREXAMPLE:** Equal low-frequency `D*`, identical `R0`, identical white additive output-noise density, and different first-order response times produce unequal SNR for a 1 Hz optical tone.

---

## 7. What has not been established

- No universal statement that detector A is better than detector B.
- No universal speed-versus-detectivity tradeoff.
- No failure of properly frequency-specific `D*(f)` for the same narrowband frequency at which it is defined.
- No result yet for pulses, broadband waveforms, unknown arrival times, finite observation windows, or optimal filtering.
- No generalized detector-performance metric.
- No novelty claim.

---

## 8. Single natural next question — DO NOT ANSWER YET

> For a specified optical waveform and a fully specified linear detector with signal transfer `H(f)` and noise PSD `S_n(f)`, what determines the maximum achievable measurement SNR?

This is the natural next step because it asks what replaces the missing information without presupposing that a new detector metric exists.
