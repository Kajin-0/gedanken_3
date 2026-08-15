# Post-Experiment-10 Theoretical Premise Screen — 2026-08-14

**Scope:** analytical/theoretical only  
**Purpose:** reject known/reducible premises before opening Experiment 11.  
**Disposition:** **FIVE CANDIDATES REJECTED / EXPERIMENT 11 NOT OPENED**

Experiment 10 is closed by default as a novelty/manuscript path. This screen follows the repository protocol: derive the first nontrivial consequence, check primary literature immediately, and kill the premise if the surviving idea reduces to established theory.

---

## Candidate 1 — causal / nonminimum-phase detectivity

### Gedanken premise

Take two stable linear photodetectors with identical

```text
DC responsivity;
|H(omega)|;
output noise PSD;
nominal -3 dB bandwidth;
area and conventional D*.
```

Let their phases differ by an all-pass/nonminimum-phase factor.

Question:

> Can equal `D*` and equal transfer-function magnitude still imply different detectability when a decision must be made causally before a hard deadline?

### First result

For a known signal with a complete offline record and stationary Gaussian noise, matched-filter SNR depends on

```math
\int \frac{|H(\omega)S(\omega)|^2}{S_n(\omega)}d\omega
```

and is therefore phase-independent if `|H|` and `S_n` are identical.

For a finite observation window `[0,T]`, however, the received waveform is truncated in time. An all-pass/nonminimum-phase factor can move signal energy beyond `T`, so finite-deadline detectability can differ even though infinite-record matched-filter SNR is unchanged.

### Prior-art collision

The underlying pieces are established:

- J. D. Victor, *Temporal impulse responses from flicker sensitivities: causality, linearity, and amplitude data do not determine phase*, JOSA A **6**, 1302–1303 (1989), explicitly points out that causality and amplitude response do not determine phase without a minimum-phase assumption.
- Wang et al., *3-lambda characterization of phase response for optical receivers*, Optics Letters **39**, 670–673 (2014), experimentally characterizes photodiode phase response up to 20 GHz.
- Causal/finite-horizon Wiener filtering, nonminimum-phase all-pass factors, and delay-performance tradeoffs are standard signal-processing/control theory.

### Disposition

```text
REJECT.
```

The detector example is valid, but the first nontrivial result is a direct application of standard finite-window detection and minimum-phase theory. No detector-specific invariant emerged.

---

## Candidate 2 — spatially correlated noise breaks the sqrt(area) D* normalization

### Gedanken premise

Compare detectors with equal local responsivity and local noise intensity but different spatial noise covariance length.

Question:

> Does conventional `D* = sqrt(A Delta f)/NEP` remain area-invariant when noise is spatially correlated across the active region?

### First result

For integrated current over active area `A`, stationary spatial covariance `C(r-r')` gives

```math
\operatorname{Var} I_A
=\int_A d^2r\int_A d^2r'\,C(r-r').
```

Therefore:

```text
A much larger than correlation area:
    Var I_A ~ A integral(C), recovering sqrt(A)-type scaling;

A much smaller than correlation area:
    Var I_A ~ A^2 C(0), so conventional sqrt(A) normalization fails.
```

### Prior-art collision

The result is simply covariance-weighted spatial integration. Infrared focal-plane-array literature has long treated spatially correlated/fixed-pattern noise and inverse-covariance/Kalman approaches, e.g. Hayat et al., Applied Optics **42**, 5872 (2003), and related FPA noise-correction work.

Classical detectivity theory already makes area normalization an assumption-dependent construction rather than a universal law; Nudelman, Applied Optics **1**, 627–636 (1962), explicitly analyzes area and bandwidth dependence of detector detectivity.

### Disposition

```text
REJECT.
```

Potentially useful pedagogically, but mathematically standard and not a strong research premise.

---

## Candidate 3 — non-normal detector dynamics

### Gedanken premise

Model a detector by a stable multistate linear system

```math
\dot x=Ax+bu+\xi,
\qquad y=c^Tx,
```

and compare normal and strongly non-normal `A` with identical stable eigenvalues and matched steady-state gain.

Question:

> Can one detector show much larger/earlier transient signal excursions without a correspondingly slower eigenvalue bandwidth?

### First result

Yes. Nonorthogonal eigenvectors allow transient norm amplification even when every eigenvalue is stable.

### Prior-art collision

This is generic non-normal dynamics. Makris, Ge and Tuereci, *Anomalous Transient Amplification of Waves in Non-normal Photonic Media*, Physical Review X **4**, 041044 (2014), develops exactly this phenomenon in photonics. More recent work continues to unify nonnormal amplification with resonance and spectral criticality.

If two scalar detectors are additionally forced to have identical full transfer functions, the transient distinction disappears; if only eigenvalues/DC gain are matched, the result is already ordinary non-normal state-space theory.

### Disposition

```text
REJECT.
```

No uniquely photodetector-specific theorem survives.

---

## Candidate 4 — detect LWIR with a large fundamental gap using an intraband/intersubband transition

### Gedanken premise

Try to evade the room-temperature `Eg ~ hc/lambda` thermal-carrier problem by choosing a wide-gap semiconductor but detecting 10-um photons through a lower-energy internal transition rather than the fundamental band gap.

### First result

The optical transition energy can indeed be decoupled from the fundamental bulk gap, while dark transport is controlled by confinement/barrier structure rather than ordinary intrinsic electron-hole generation across `hc/lambda`.

### Prior-art collision

This is the core quantum-well infrared photodetector idea. B. F. Levine, *Quantum Well Intersubband Infrared Detectors* (1989), already discusses 10-um GaAs/AlGaAs intersubband detectors, and 8–10-um QWIP focal-plane arrays were established by the 1990s.

### Disposition

```text
REJECT.
```

The proposed escape from Experiment-10 interband-gap logic is a known detector architecture, not a new theorem premise.

---

## Candidate 5 — same D* variance, different false-alarm tails

### Gedanken premise

Construct two detectors with identical responsivity, bandwidth, and output noise variance/PSD, but different higher-order dark-event statistics:

```text
Detector A: approximately Gaussian noise;
Detector B: rare large burst / point-process noise.
```

Question:

> Can equal D* imply radically different probability of detection at a fixed false-alarm rate?

### First result

Yes. `D*` is a second-order SNR metric; Neyman-Pearson detection depends on the full likelihood. Equal variance does not fix tail probabilities or false-alarm rates.

### Prior-art collision

This is standard statistical detection theory and has direct photodetector precedent. Photon-counting/Geiger-mode laser-radar literature derives detection and false-alarm probabilities directly from Poisson/event statistics; e.g. Henriksson, Applied Optics **44**, 5140–5147 (2005), and earlier/later Geiger-mode false-alarm analyses.

### Disposition

```text
REJECT.
```

A useful criticism of variance-only metrics, but not a novel photodetector principle.

---

# Overall screen

```text
Candidate 1 — causal/nonminimum phase: REJECT
Candidate 2 — spatial covariance / D* area scaling: REJECT
Candidate 3 — non-normal transient amplification: REJECT
Candidate 4 — wide-gap intersubband escape: REJECT
Candidate 5 — non-Gaussian false-alarm detectivity: REJECT
```

No Experiment-11 branch should be created from these candidates.

## Lessons for the next screen

Avoid premises whose first result is immediately reducible to:

```text
standard linear systems / matched filtering;
standard covariance scaling;
generic non-normal dynamics;
known detector architectures such as QWIPs/QCDs;
ordinary Neyman-Pearson / point-process detection theory.
```

The next premise should contain a genuinely photodetector-specific physical constraint that is not merely a task-dependent redefinition of performance.
