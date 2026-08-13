# Prior-Art Audit — Detector-Level Task Reversal Claim

**Date:** 2026-08-12  
**Status:** PRIOR-ART AUDIT / NOVELTY NOT ESTABLISHED / POSSIBLE SYNTHESIS CONTRIBUTION. The mathematical closure branch ended at Step 49. This document audits the detector-facing claims before any novelty language is allowed.

---

## 1. Audit question

The core surviving detector result is not simply that speed and sensitivity trade off. It is the narrower task statement:

> Under a specified global-false-alarm, unknown-arrival matched-filter scanning protocol, two detector channels can have equal eventual matched-filter SNR yet reverse their finite-time detection ranking because temporal compression changes both evidence accumulation and the correlation structure of the timing search.

The audit asks which parts of this statement are already established prior art and whether the combined photodetector construction appears distinct.

This is a focused literature audit, not a legal patentability opinion and not an exhaustive novelty search.

---

## 2. Direct prior art: scalar D* is not a complete pulsed-detection metric

### R. Clark Jones, 1960 — energy detectivity

Jones explicitly distinguished ordinary detectivity `D*(f)` from detection of a radiation pulse and introduced an energy-detectivity quantity for pulses. His result gives the maximum energy detectivity from the frequency-dependent detectivity through an integral of `D*(f)^2`.

Reference:

- R. Clark Jones, **"Energy Detectable by Radiation Detectors,"** *Journal of the Optical Society of America* **50**, 883–886 (1960). DOI: `10.1364/JOSA.50.000883`.

Disposition:

```text
Claim: a scalar D* at one modulation condition is insufficient for arbitrary pulse/waveform detection.
Assessment: DIRECT PRIOR ART / NOT NOVEL.
```

This also means that the Step-02 move from one scalar `D*` toward a spectral overlap is conceptually in a long-established line of detector theory, even though the repo's exact matched-filter normalization is independently derived.

---

## 3. Direct prior art: sensitivity–speed and detectivity–bandwidth tradeoffs

The detector literature has treated speed jointly with detectivity for decades.

### Garcia & Dereniak, 1990

A high-speed Si:Ga infrared photoconductor was explicitly characterized using a detectivity-bandwidth product `D*f*`.

- J. P. Garcia and E. L. Dereniak, **"Extrinsic silicon photodetector characterization,"** *Applied Optics* **29**, 559–569 (1990). DOI: `10.1364/AO.29.000559`.

### Modern characterization guidance

Current photodetector consensus guidance treats detectivity and response speed as distinct operating-condition-dependent figures of merit rather than implying that one scalar `D*` captures dynamic performance.

- V. Pecunia et al., **"Guidelines for accurate evaluation of photodetectors based on emerging semiconductor technologies,"** *Nature Photonics* **19**, 1178–1188 (2025). DOI: `10.1038/s41566-025-01759-1`.

### Yang et al., 2026 — USBL

A 2026 *Nature Communications* paper explicitly defines

```math
USBL = D^* \times \text{bandwidth}
```

as a sensitivity-bandwidth comparison figure of merit.

- Y. Yang et al., **"Overcoming the sensitivity–speed trade-off in two-dimensional photodetectors via a functional oxide interlayer,"** *Nature Communications* **17**, 6077 (2026).

Disposition:

```text
Claim: detector sensitivity and speed need to be considered jointly.
Assessment: DIRECT PRIOR ART / NOT NOVEL.

Claim: a simple D* × bandwidth scalar is a new replacement metric.
Assessment: CLEARLY NOT NOVEL and not the direction this project should pursue.
```

The repository should therefore avoid positioning its contribution as a new generic "sensitivity-speed product."

---

## 4. Direct adjacent prior art: unknown arrival/location raises matched-filter false-alarm thresholds

The timing-search mechanism is also established detection theory.

### Vio & Andreani / Vio et al.

Matched filtering is Neyman–Pearson optimal when the signal position is known. When the signal position is unknown and one searches peaks of the matched-filtered Gaussian field, the false-alarm probability depends on the peak process and on how many opportunities for noise peaks exist.

Representative references:

- R. Vio and P. Andreani, **"On the Correct Estimate of the Probability of False Detection of the Matched Filter in Weak-Signal Detection Problems,"** arXiv:1602.02392 (2016).
- R. Vio, P. Andreani, A. Biggs, N. Hayatsu, **"Correct estimate of the probability of false detection of the matched filter in weak-signal detection problems. III,"** arXiv:1907.01465 (2019).

### Morras et al., 2023

For matched-filter SNR time series in Gaussian noise, Morras et al. derive a false-alarm rate that depends on the template autocorrelation. They introduce an effective sampling rate depending on the template, noise PSD, and threshold, and show that maintaining a fixed false-alarm rate imposes a template-dependent minimum SNR threshold.

- G. Morras, J. F. Nuño Siles, J. Garcia-Bellido, E. Ruiz Morales, **"The False Alarms induced by Gaussian Noise in Gravitational Wave Detectors,"** *Physical Review D* **107**, 023027 (2023). DOI: `10.1103/PhysRevD.107.023027`.

### Correlator-bank literature

The global false-alarm threshold of a correlated template bank and its effect on detection efficiency have long been analyzed in gravitational-wave matched filtering.

- R. P. Croce et al., **"Correlator Bank Detection of GW chirps. False-Alarm Probability, Template Density and Thresholds: Behind and Beyond the Minimal-Match Issue,"** *Physical Review D* **70**, 122001 (2004). DOI: `10.1103/PhysRevD.70.122001`.

Disposition:

```text
Claim: unknown arrival introduces a look-elsewhere/search penalty.
Assessment: DIRECT PRIOR ART / NOT NOVEL.

Claim: the penalty depends on template correlation time / effective number of timing opportunities rather than raw ADC sample count.
Assessment: DIRECT ADJACENT PRIOR ART / NOT NOVEL AS A SIGNAL-DETECTION PRINCIPLE.
```

This is important: the repo's mechanism is physically meaningful, but the mechanism itself is not new probability theory.

---

## 5. Phase information and finite observation windows

The repo shows that two channels with identical magnitude response can have different finite-window performance if their phase/group-delay structure differs; an all-pass construction removes the trivial pure-delay case.

All-pass filters preserving magnitude while changing dispersion are standard optical/signal-processing objects. Examples include optical all-pass dispersion-control work such as:

- G. Lenz and C. K. Madsen, **"General Optical All-Pass Filter Structures for Dispersion Control in WDM Systems,"** *Journal of Lightwave Technology* **17**, 1248 (1999).

In the focused searches performed for this audit, I did **not** find a photodetector paper whose central result is the same finite-observation all-pass counterexample to a magnitude-only `D*(f)` ordering.

Disposition:

```text
Claim: magnitude response alone cannot determine finite-window temporal energy placement when phase differs.
Assessment: STANDARD SYSTEM-THEORY CONSEQUENCE; EXPLICIT PHOTODETECTOR PRECEDENT NOT FOUND IN THIS SEARCH.

Novelty confidence: LOW as a stand-alone theorem, potentially useful as a clean pedagogical detector counterexample.
```

---

## 6. The specific ranking-reversal construction

The focused search included combinations of:

```text
photodetector + unknown arrival time
matched filter + template duration + false alarm
matched filter + correlation time + threshold
response time + unknown delay
ranking reversal + matched filter
specific detectivity + bandwidth / pulse / time response
```

No direct hit was found for the following complete construction:

1. two photodetector channels normalized to equal eventual matched-filter SNR;
2. different temporal response scales;
3. one fixed unknown-arrival interval and global false-alarm requirement;
4. finite-time evidence accumulation compared with template-dependent timing-search complexity;
5. an explicit task region in which the fast/slow detection ranking reverses.

The closest adjacent work establishes the individual ingredients:

- pulsed/energy detection cannot be reduced to one scalar `D*`;
- detectivity and speed/bandwidth trade off;
- unknown-location matched filtering incurs a search penalty;
- matched-filter false-alarm rate depends on template autocorrelation/effective sampling rate.

What was **not** located is the detector-specific synthesis that holds eventual SNR equal and asks whether changing only temporal scale can reverse which detector satisfies a deadline/global-PFA task first.

Disposition:

```text
Core fast/slow ranking-reversal construction:
POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.
```

The correct confidence level is **moderate-low**, not high. The neighboring literatures in radar, sonar, astronomy, gravitational waves, sequential detection, and optical receivers are large, and this audit is not exhaustive enough to support a legal or publication-level novelty claim.

---

## 7. What appears strongest for a paper

The strongest defensible paper-level contribution is not a new scalar figure of merit. It is a task-dependent ordering statement:

> **Specific detectivity, even when extended to eventual matched-filter sensitivity, does not by itself order detectors for finite-deadline, unknown-arrival tasks. Under a specified global-false-alarm scanning protocol, detector response time changes both evidence accumulation and the correlation structure of the timing search, and these effects can reverse the ordering in an equal-eventual-SNR family.**

This should be presented explicitly as a **task/protocol theorem**, not as a universal claim that faster detectors can be worse.

The clean hierarchy is:

```text
single-condition D*
    ↓ insufficient for arbitrary pulses (old result)
frequency-dependent D*(f)
    ↓ sufficient for restricted full-observation known-waveform SNR
complex temporal response + finite observation
    ↓ phase/time placement matters
unknown arrival + global false alarm
    ↓ task-level search geometry matters
constructed equal-eventual-SNR family
    → possible fast/slow ranking reversal under the defined protocol
```

The likely publishable value, if novelty survives a deeper search, is the **photodetector-facing synthesis and explicit task construction**, not the individual mathematical ingredients.

---

## 8. What should not be claimed

Do not claim any of the following based on the present audit:

- that scalar `D*` failing for pulse detection is new;
- that detectivity–bandwidth tradeoffs are new;
- that unknown-arrival matched-filter search penalties are new;
- that correlation time controlling false-alarm opportunities is new;
- that `D* × bandwidth` is a new metric;
- that faster detectors are generally worse;
- that the defined scan is the universally optimal composite-hypothesis detector;
- that the ranking-reversal synthesis is novel.

The last item remains an **open novelty question**, not a negative conclusion.

---

## 9. Search limitations

This audit used focused web searches across Optica, Nature, IEEE-indexed material, arXiv/Physical Review adjacent signal-detection literature, and direct searches for combinations of the key concepts.

It did not perform:

- exhaustive citation-network traversal;
- Web of Science/Scopus subscription searches;
- exhaustive Google Scholar backward/forward citation chaining;
- patent-family searching;
- non-English literature searching;
- a formal claim chart against all prior art.

Therefore absence of a direct hit is evidence only for **possible novelty**, never proof of novelty.

---

## 10. Audit disposition

```text
A. Scalar D* insufficiency for arbitrary temporal/pulsed tasks
   → established prior art.

B. Spectral integration / energy detectivity
   → established prior art since at least 1960.

C. Sensitivity-speed or D*×bandwidth comparison
   → established prior art; explicit modern metric exists.

D. Unknown-arrival matched-filter search penalty and template-dependent false-alarm rate
   → established adjacent detection theory.

E. Magnitude-identical / phase-different finite-window detector counterexample
   → standard-system consequence; explicit detector precedent not found in focused search.

F. Equal-eventual-SNR photodetector family with a protocol-specific fast/slow detection-time ranking reversal
   → no direct prior-art match found in this audit; possible synthesis contribution, novelty not established.
```

### Single next question

> Can the detector-facing result now be compressed into a short theorem/counterexample paper whose novelty burden rests only on item F, with all established ingredients cited as prior art and Steps 13–49 moved to a technical companion?