# Progress Log — Experiment 01

## 2026-08-11 11:21 EDT — Initialization and first consequence

### Prompted question

Two photodetectors have equal conventional `D*` but response times `1 ns` and `1 s`. Determine whether equal `D*` guarantees equal ability to detect an arbitrary optical signal, proceeding only one logical step.

### Important assumptions made explicit

- The initial `D*` equality is interpreted as equality at a low-frequency/reference condition; a bare `D*` without conditions is incomplete.
- Both detectors are linear and first-order in temporal response.
- Equal active area `A`.
- Equal low-frequency responsivity `R0`.
- Equal additive white output-noise density `n0`.
- The dominant noise is placed after the detector pole; this is a physically consistent readout-noise-dominated counterexample, not a universal model.
- The comparison signal is a sinusoidal optical-power component measured with identical equivalent noise bandwidth `B`.

### Derivation

```math
H_i(f)=\frac{1}{1+i2\pi f\tau_i},
```

```math
D_0^*=\frac{\sqrt A R_0}{n_0},
```

```math
\mathrm{SNR}_i
=\frac{P_mD_0^*}{\sqrt{AB}}|H_i(f_m)|.
```

At `f_m=1 Hz`:

```text
A: tau = 1 ns -> |H_A| ~ 1
B: tau = 1 s  -> |H_B| ~ 0.157
SNR_A / SNR_B ~ 6.36
```

### First nontrivial consequence

**DERIVED / COUNTEREXAMPLE:** equal reference-condition `D*` does not guarantee equal SNR for every optical waveform.

### Adversarial check

If the dominant noise is filtered by the same detector pole, signal and noise attenuation can cancel. Likewise, equal `D*(f_m)` specified at the actual measurement frequency implies equal narrowband tone SNR under equal area, incident tone amplitude, and estimator bandwidth.

Therefore the correct conclusion is **not** `fast is always better`; it is that a scalar `D*` at one reference condition is insufficient to determine arbitrary-signal performance.

### Stopping point

No pulse analysis, matched filtering, generalized metric, or speed-detectivity theory has been pursued.

### Next question, held open

For a specified optical waveform and fully specified linear detector transfer/noise spectrum, what determines maximum achievable SNR?
