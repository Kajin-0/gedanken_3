# Paper A — Closest Prior-Art Audit: Acquisition / Unknown-Delay Lineage

**Date:** 2026-08-12  
**Status:** DEEPER PRIOR-ART AUDIT / NOVELTY BURDEN NARROWED / NO DIRECT MATCH TO COMPLETE DETECTOR-SCALING REVERSAL FOUND / NOVELTY STILL NOT ESTABLISHED

---

## 1. Why a second audit was necessary

The first detector-facing prior-art audit correctly identified established work on:

- pulse/energy detectivity;
- sensitivity-bandwidth comparison;
- unknown-position matched-filter false alarms;
- correlated scan thresholds;
- ladar acquisition in a range window.

The adversarial review showed that this was not yet the closest conceptual neighborhood. The Paper-A object is now an operationally defined **guarantee time** for an unknown-arrival batch search. That language places the work much closer to the classical **signal/code acquisition** literature than the first audit emphasized.

The relevant question is therefore not merely:

> Has someone studied a photodetector with unknown arrival time?

It is:

> Has acquisition theory already combined uncertainty-region size, integration/dwell time, detection probability, false alarms, matched-filter structure, and acquisition time—and if so, what remains distinct in Paper A?

The answer to the first clause is clearly **yes**.

---

## 2. Classical PN / spread-spectrum acquisition is direct conceptual prior art

### 2.1 Unknown delay/code phase as a search problem is old

Classical pseudonoise and direct-sequence spread-spectrum acquisition treats unknown code phase or signal epoch as a search over candidate states/cells. Acquisition-time statistics depend on the search strategy, per-cell detection probability, false-alarm probability, dwell/integration time, and available a priori information.

A particularly direct early source is:

- A. Weinberg, **"Search strategy effects on PN acquisition performance,"** conference proceedings (1981), NASA NTRS record `19830038551`.

The NTRS summary explicitly states that PN acquisition-time statistics are developed as functions of predetection SNR, detection and false-alarm probabilities, and a priori information on epoch location, for random and expanding-window search strategies.

This is conceptually close to Paper A's use of an uncertainty interval plus a specified false-alarm/detection operating point.

### 2.2 Matched-filter acquisition and mean acquisition time are established

The canonical matched-filter lineage includes:

- A. Polydoros and C. L. Weber, **"A Unified Approach to Serial Search Spread-Spectrum Code Acquisition—Part I: General Theory,"** *IEEE Transactions on Communications* **32**(5), 542–549 (1984). DOI `10.1109/TCOM.1984.1096109`.
- A. Polydoros and C. L. Weber, **"A Unified Approach to Serial Search Spread-Spectrum Code Acquisition—Part II: A Matched-Filter Receiver,"** *IEEE Transactions on Communications* **32**(5), 550–560 (1984). DOI `10.1109/TCOM.1984.1096113`.
- Y.-T. Su, **"Rapid Code Acquisition Algorithms Employing PN Matched Filters,"** *IEEE Transactions on Communications* **36**(6), 724–733 (1988). DOI `10.1109/26.2793`.

Su explicitly derives detector operating characteristics and mean acquisition times for several PN matched-filter search architectures. The historical literature also includes fixed-dwell, variable-dwell, serial, parallel, and sequential acquisition procedures.

Therefore the broad statement

```text
unknown delay/search size + dwell/integration + detection/false alarm
-> acquisition-time tradeoff
```

is established acquisition theory and cannot carry Paper A's novelty.

---

## 3. Search strategy and a priori uncertainty are established axes

The acquisition literature goes beyond a uniform blind scan.

NASA records from the late 1970s and early 1980s explicitly study how a priori signal-location distributions and expanding/random search windows alter acquisition time. Examples include:

- J. K. Holmes and K. T. Woo, **"An optimum PN code search technique for a given apriori signal location density,"** NTC 1978 / NASA NTRS record `19790056533`.
- A. Weinberg, **"Search strategy effects on PN acquisition performance,"** 1981 / NASA NTRS `19830038551`.
- W. R. Braun, **"Performance analysis for the expanding search PN acquisition algorithm,"** *IEEE Transactions on Communications* **30** (1982), NASA NTRS record `19820043175`.

Thus Paper A should not imply that making detector ranking depend on `L`, `alpha`, `beta`, or the acquisition protocol is conceptually new by itself. Acquisition performance has long been task/protocol dependent.

---

## 4. Optical code acquisition makes the overlap more direct

The closest photonics precedent is not limited to ladar.

### 4.1 Optical CDMA synchronization/acquisition

Optical CDMA literature explicitly studies acquisition/synchronization time in systems where optical signals are detected and threshold decisions are made over uncertain code alignment.

Representative sources include:

- M. M. Mustapha and R. F. Ormondroyd, **"Dual-Threshold Sequential Detection Code Synchronization for an Optical CDMA Network in the Presence of Multi-User Interference,"** *Journal of Lightwave Technology* **18**(12), 1742–1748 (2000). DOI `10.1109/50.908711`.
- A. Keshavarzian and J. A. Salehi, **"Optical Orthogonal Code Acquisition in Fiber-Optic CDMA Systems via the Simple Serial-Search Method,"** *IEEE Transactions on Communications* **50**(3), 473–483 (2002). DOI `10.1109/26.990909`.
- A. T. Pham and H. Yashima, **"Performance Analysis of MDSS Code Acquisition Using SLS for Optical CDMA Systems,"** *IEICE Transactions on Communications* **E88-B**(12), 4570–4577 (2005). DOI `10.1093/ietcom/e88-b.12.4570`.

Mustapha and Ormondroyd derive mean acquisition time for an asynchronous optical-CDMA synchronizer and optimize it through detector thresholds. Pham and Yashima explicitly analyze multiple-dwell serial-search optical code acquisition and study the effects of threshold, mean photon count, dark current, and user interference on acquisition performance.

This makes the following claim clearly non-novel:

```text
photodetection + uncertain temporal/code alignment + threshold search
-> acquisition time depends on receiver operating parameters.
```

### 4.2 Direct-detection ladar

Milstein et al. provide an even closer unknown-range optical detection precedent:

- A. B. Milstein, L. A. Jiang, J. X. Luu, E. L. Hines, and K. I. Schultz, **"Acquisition algorithm for direct-detection ladars with Geiger-mode avalanche photodiodes,"** *Applied Optics* **47**, 296–311 (2008). DOI `10.1364/AO.47.000296`.

Their problem is target detection within a specified range window. They construct a constant-false-alarm acquisition algorithm and minimize acquisition time for Geiger-mode APD ladar.

Again, this is not the same detector-family theorem as Paper A, but it eliminates any plausible claim that the intersection

```text
photodetector + unknown delay/range window + false alarm + acquisition time
```

is new.

---

## 5. What acquisition theory does NOT automatically supply

The classical acquisition papers generally hold the receiver architecture/waveform family fixed and ask how search strategy, threshold, SNR, dwell time, code uncertainty, or detector structure affects acquisition.

Paper A makes a more specific comparison:

1. one **fixed optical event** is applied to both detector channels;
2. the detector channels are causal and physically realizable;
3. their time scales `tau` differ;
4. their gains are deliberately normalized so the specified event has the same eventual matched-filter SNR `rho0` in every channel;
5. changing `tau` simultaneously changes
   - finite-time evidence accumulation, and
   - the physical correlation length of the timing statistic;
6. one fixed physical arrival-time uncertainty `L` therefore becomes a different normalized search length `L/tau` for each channel;
7. this creates a **fast/slow guarantee-time ordering reversal** and a slow-only guarantee-feasibility regime within the constructed family.

This coupling is not the same as merely comparing two acquisition algorithms or two dwell times. The detector's temporal scaling changes both the evidence clock and the nuisance-parameter geometry while eventual event SNR is held equal.

That is the only part of the current story that still plausibly carries a synthesis contribution.

---

## 6. Revised novelty claim matrix

### A. Scalar `D*` does not determine arbitrary pulse detection

```text
DIRECT PRIOR ART.
```

Jones 1960 already establishes pulse/energy detectivity from frequency-dependent sensitivity.

### B. Sensitivity and temporal bandwidth must be considered jointly

```text
DIRECT PRIOR ART.
```

Detector characterization literature and explicit `D* x bandwidth` metrics exist.

### C. Unknown arrival/delay creates a search penalty

```text
DIRECT PRIOR ART.
```

Matched-filter, acquisition, astronomy, GW, radar/communications, and synchronization literatures all contain this principle.

### D. Acquisition time depends on uncertainty-region size, SNR, detection probability, false alarm, dwell/integration time, and search strategy

```text
DIRECT PRIOR ART.
```

This is classical spread-spectrum / synchronization theory.

### E. The same acquisition concepts exist in optical detection systems

```text
DIRECT PRIOR ART.
```

Optical-CDMA synchronization and Geiger-mode ladar provide clear examples.

### F. A detector's response time can alter both evidence accumulation and the normalized timing-search geometry

```text
NATURAL CONSEQUENCE OF THE PRESENT SCALING CONSTRUCTION;
NO DIRECT PRIOR-ART MATCH FOUND IN THIS AUDIT.
```

The individual ingredients are old; the coupled detector comparison is narrower.

### G. Equal-eventual-SNR causal photodetector channels can reverse fast/slow guarantee-time ordering under one fixed physical unknown-arrival task

```text
POSSIBLE SYNTHESIS CONTRIBUTION.
NOVELTY NOT ESTABLISHED.
NO DIRECT MATCH FOUND IN THE SOURCES REVIEWED HERE.
```

This is now the correct novelty burden for Paper A.

---

## 7. Manuscript consequence

The Introduction should explicitly acknowledge acquisition theory, not only generic matched-filter false alarms.

A defensible positioning paragraph is:

> Unknown-delay acquisition itself is a mature subject. Classical spread-spectrum work derives acquisition-time distributions and mean acquisition times from search-region size, dwell strategy, SNR, detection probability, and false alarms, and analogous synchronization/acquisition problems have been studied in optical CDMA and direct-detection ladar. The present construction does not claim these ingredients as new. Its narrower question is what happens when the **detector response time itself** rescales both finite-time evidence accumulation and the normalized unknown-arrival search while eventual matched-filter SNR for the specified optical event is held fixed.

This paragraph materially improves novelty honesty and should appear before the paper states its specific question.

---

## 8. Search limitations

This remains a scientific literature audit, not a legal novelty opinion.

The search included:

- canonical spread-spectrum / PN acquisition lineages;
- matched-filter acquisition;
- search-strategy / a-priori epoch uncertainty;
- optical-CDMA synchronization/acquisition;
- direct-detection ladar acquisition;
- prior matched-filter false-alarm literature already audited.

It did not exhaustively search:

- all radar and sonar monographs;
- every synchronization textbook;
- patents and patent families;
- non-English literature;
- every citing/cited-by branch of the classic acquisition papers;
- proprietary or subscription-only indexing databases.

Therefore absence of a direct equal-eventual-SNR detector-speed reversal hit cannot establish novelty.

---

## 9. Disposition after the deeper audit

The novelty position is **narrower than before but cleaner**:

```text
OLD overly broad neighborhood:
unknown arrival + false alarm + detector speed -> possible novelty

REJECTED: acquisition theory already owns most of that structure.

CURRENT candidate contribution:
same optical event
+ causal detector family
+ equal eventual matched-filter SNR
+ detector time-scale change
+ simultaneous evidence-clock and search-correlation rescaling
+ fixed physical unknown-arrival interval
-> fast/slow guarantee-time reversal and slow-only feasibility.
```

No source reviewed here directly reproduces that full construction.

Final status remains:

```text
POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.
```

No "first," "novel," or priority language is authorized by this audit.

---

## 10. Next manuscript action

The prior-art objection is now sufficiently characterized for Paper A drafting:

1. add the mature acquisition-theory acknowledgment to the Introduction;
2. cite one canonical spread-spectrum matched-filter acquisition source;
3. cite one optical-CDMA acquisition source;
4. retain Milstein et al. as the closest direct-detection range-window precedent;
5. keep the claimed contribution restricted to the equal-eventual-SNR detector-scaling reversal.

After those edits, the next appropriate action is a final adversarial manuscript/citation QA—not another theoretical branch by default.
