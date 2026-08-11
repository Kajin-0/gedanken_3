# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment; stop after the first nontrivial consequence; no generalized replacement metric and no novelty claim.

Read this file first.

The repository follows the physics rather than a predetermined criticism of `D*`. Preserve assumptions, counterexamples, cancellations, invalidations, and unresolved branches.

---

## 1. Mandatory repository protocol

Before every material write:

1. fetch live `main` / current target;
2. inspect intervening changes when needed;
3. fetch the current blob SHA before replacing an existing file;
4. never overwrite stale state;
5. preserve failed/corrected branches and explain why they changed;
6. make narrow edits where practical;
7. update `CURRENT_STATE.md` whenever the scientific frontier changes;
8. append a timestamped entry to `PROGRESS_LOG.md` for consequential work.

**Live `main` overrides snapshots and recovery notes.**

---

## 2. Epistemic labels

Use explicitly where useful:

- **DEFINED** — a convention or model definition.
- **ASSUMED** — an idealization introduced for the thought experiment.
- **DERIVED** — follows mathematically from stated assumptions.
- **COUNTEREXAMPLE** — a physically consistent construction sufficient to disprove a claimed implication.
- **CONDITIONAL** — true only under listed assumptions.
- **OPEN** — not established.
- **INVALIDATED** — shown false under its stated generality.
- **NON-CLAIM** — deliberately not asserted.

Do not use `novel`, `universal`, `fundamental`, `first`, etc. without a separate prior-art audit.

---

## 3. Active starting question

Two hypothetical detectors satisfy

```math
D_A^*=D_B^*
```

but have

```math
\tau_A=1\ \mathrm{ns},
\qquad
\tau_B=1\ \mathrm{s}.
```

Question:

> Does equal conventional specific detectivity imply equal ability to detect an arbitrary optical signal?

The current task is only to establish the first nontrivial consequence.

---

## 4. Measurement discipline

Never write bare `D*` as though it were a complete detector state.

For a narrowband measurement at temporal frequency `f`, define output responsivity magnitude `R(f)` and one-sided output-noise amplitude spectral density `n_y(f)` locally over the measurement bandwidth. Then

```math
D^*(f)=\frac{\sqrt A\,R(f)}{n_y(f)}
```

for the spectral-density convention, equivalently

```math
D^*=\frac{\sqrt{A\,\Delta f}}{\mathrm{NEP}_{\Delta f}}
```

when `NEP_{Delta f}` is the total incident power needed for unit SNR in bandwidth `Delta f`.

A quoted `D*` is therefore condition-dependent. At minimum track:

```text
wavelength / optical spectrum
modulation frequency or temporal protocol
active area
noise bandwidth / estimator ENBW
bias
operating temperature
responsivity convention
noise spectral density and where the dominant noise enters
```

---

## 5. Minimal active detector model

Use two linear first-order detectors with identical area `A`, identical low-frequency responsivity `R0`, and identical additive white output-noise density `n0`. They differ only in response time:

```math
H_i(f)=\frac{1}{1+i2\pi f\tau_i},
```

```math
R_i(f)=R_0H_i(f).
```

The additive noise is intentionally placed after the detector pole (for example, dominant readout noise). This is physically consistent and makes the temporal response affect signal without automatically forcing the same filtering onto the dominant noise.

At sufficiently low reference frequency,

```math
D_{A,0}^*=D_{B,0}^*=\frac{\sqrt A\,R_0}{n_0}.
```

This construction is a counterexample candidate, not a universal detector model.

---

## 6. First nontrivial result

Drive both detectors with the same small sinusoidal optical-power component of RMS amplitude `P_m` at frequency `f_m`, and estimate that Fourier component using the same equivalent noise bandwidth `B`.

Then

```math
\mathrm{SNR}_i
=\frac{R_0|H_i(f_m)|P_m}{n_0\sqrt B}
=\frac{P_mD_0^*}{\sqrt{AB}}|H_i(f_m)|.
```

Therefore

```math
\frac{\mathrm{SNR}_A}{\mathrm{SNR}_B}
=\frac{|H_A(f_m)|}{|H_B(f_m)|}.
```

At `f_m = 1 Hz`,

```math
|H_A|\approx1,
```

while for `tau_B = 1 s`,

```math
|H_B|=\frac{1}{\sqrt{1+(2\pi)^2}}\approx0.157.
```

Thus

```math
\mathrm{SNR}_A/\mathrm{SNR}_B\approx6.36.
```

**DERIVED / COUNTEREXAMPLE:** equal low-frequency conventional `D*` does **not** guarantee equal SNR for an arbitrary optical signal.

---

## 7. Critical qualification — do not lose this

The result is not `fast detector always has higher SNR`.

If the dominant noise is generated before the same temporal pole so that

```math
n_i(f)=n_0|H_i(f)|,
```

then signal and noise attenuation can cancel in the narrowband ratio. Likewise, if `D*_A(f_m)=D*_B(f_m)` is explicitly specified at the *actual measurement frequency* using each detector's actual `R_i(f_m)` and `n_i(f_m)`, then equal area, optical power, and estimator bandwidth give equal narrowband tone SNR by definition.

Therefore the present result is an **insufficiency result**:

> a single scalar `D*` equality at one reference condition does not determine arbitrary-signal SNR unless temporal signal transfer, noise transfer/spectrum, and measurement protocol are also fixed.

No generalized performance principle has yet been derived.

---

## 8. What is established / not established

### Established

- `D*` is a measurement-condition-dependent signal-to-noise normalization, not a complete temporal detector description.
- Equal reference `D*` does not logically imply equal SNR for every optical waveform.
- A physically consistent one-pole + additive-output-noise model provides an explicit counterexample.

### Not established

- Fast detectors are not proven superior in general.
- Slow detectors are not proven inferior in general.
- No universal bandwidth penalty or speed-detectivity tradeoff has been derived.
- No claim has been made that conventional frequency-specific `D*(f)` fails for a narrowband measurement at that same frequency.
- No replacement for `D*` has been proposed.

### Single next question

> For a completely specified linear detector with signal transfer `H(f)` and noise PSD `S_n(f)`, what quantity determines the maximum achievable SNR for a specified optical waveform?

Do not answer this until explicitly prompted.
