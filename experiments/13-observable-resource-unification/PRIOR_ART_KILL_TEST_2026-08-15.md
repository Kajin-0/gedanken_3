# Experiment 13 — severe prior-art kill test

**Date:** 2026-08-15  
**Scope:** unified photodetector operator/resource claim  
**Disposition:** **ABSTRACT MASTER OPERATOR NOVELTY KILLED / DETECTOR-SPECIFIC FOUR-BRANCH CLOSURE NOT DIRECTLY COLLIDED / FLAGSHIP MANUSCRIPT NOT YET AUTHORIZED**

## 1. Standard of review

The question is not whether the Experiment-13 notation is convenient. The question is whether a referee could point to established work and say that the proposed unified result is merely a repackaging of known task-based information theory, quantum detector effects, singular-value inequalities, Shockley–Ramo noise coupling, and optical sum-rule bounds.

The audit therefore assumes the strongest plausible prior-art comparator and kills any claim that is already standard at that level.

---

# 2. Claims that are NOT novel and must not headline a paper

## 2.1 Positive/Gram operator as a detector metric — KILLED AS GENERIC NOVELTY

The identity

```math
G=M^\dagger M,
\qquad
Q_G[X]=Tr(GX)
```

and spectral bounds

```math
lambda_- Tr X <= Tr(GX) <= lambda_+ Tr X
```

are elementary positive-operator/singular-value facts.

No novelty claim is possible at this level.

Likewise, the condition

```math
G=cI
```

for isotropic quadratic performance is elementary polarization/operator theory.

**Disposition:** retain as organizing language only.

---

## 2.2 Task-specific detector/imaging information operators — KILLED AS GENERIC NOVELTY

Strong prior art:

- H. H. Barrett, J. L. Denny, R. F. Wagner, and K. J. Myers, *J. Opt. Soc. Am. A* **12**, 834–852 (1995), DOI 10.1364/JOSAA.12.000834, derives task-performance figures of merit using Fisher-information and Fourier-crosstalk matrices, with direct links to NEQ/generalized NEQ and Hotelling-observer detection tasks.
- E. Clarkson and F. Shen, *J. Opt. Soc. Am. A* **27**, 2313–2326 (2010), DOI 10.1364/JOSAA.27.002313, develops Fisher-information kernels as task-based surrogate figures of merit for ideal-observer detection/estimation.

Therefore the statements

```text
performance is task dependent;
a matrix/operator can be more complete than one scalar;
quadratic task performance is a signal-direction pairing;
```

are not new.

Experiment 01 can still contain a detector-specific theorem/witness, but Experiment 13 cannot claim discovery of task-based operator performance.

**Disposition:** generic unification ingredient old; existing Experiment-01 hard-window reversal remains the nontrivial detector-specific content.

---

## 2.3 General quantum photodetector framework — STRONG COLLISION, NOT IDENTICAL

Strong comparator:

- S. M. Young, M. Sarovar, and F. Léonard, *Phys. Rev. A* **98**, 063835 (2018), DOI 10.1103/PhysRevA.98.063835, presents a general photodetector modeling framework in which the photon field, absorption process, amplification, internal degrees of freedom, and measurement record are treated within one coupled quantum system. It explicitly connects detector internal structure to multiple performance metrics and architecture tradeoffs.

This paper is broad enough that Experiment 13 must not claim to be the first "general framework for photodetectors" or the first to connect internal architecture to multiple performance metrics.

The current Experiment-13 construction is materially different in purpose: it seeks a compact positive-operator closure among four specific independently derived detector limits, including a thermal inverse-population theorem and a conservative-recycling terminal-noise theorem. But the bar for significance is much higher because a general photodetector framework already exists.

**Disposition:** major framing collision; title/abstract must avoid generic "unified framework for photodetectors" language unless the detector-specific theorem is substantially sharper.

---

## 2.4 Coherence sensitivity of detector POVMs — KILLED AS GENERIC NOVELTY

Strong comparator:

- H. Xu et al., *Phys. Rev. Lett.* **125**, 060404 (2020), DOI 10.1103/PhysRevLett.125.060404, reconstructs detector POVMs and quantifies the ability of a quantum detector to detect coherence.

Therefore these ideas are established:

```text
a detector measurement effect can be coherence sensitive;
POVM geometry can quantify that sensitivity;
coherence is a measurement resource.
```

Experiment 09's specific matched-population bright-state construction, extraction kinetics, and scaling theorem must carry its own novelty. Experiment 13 cannot claim detector-coherence selectivity in the abstract.

**Disposition:** generic coherence/effect-operator branch old; specific Experiment-09 detector theorem retained.

---

## 2.5 Shockley–Ramo treatment of photodiode impulse response and GR noise — KILLED AS GENERIC NOVELTY

Strong comparator:

- W. Dąbrowski, *Prog. Quantum Electron.* **13**, 233–266 (1989), DOI 10.1016/0079-6727(89)90004-9, treats semiconductor-detector impulse response and generation–recombination noise using transport and Ramo/corpuscular methods, explicitly emphasizing the coupling problem and the need for the correct terminal observable.
- Earlier associated corpuscular treatments of junction GR noise likewise use properly formulated Ramo induction.

Therefore Experiment 13 must not claim:

```text
first use of Ramo theory for GR noise;
first observation that internal carrier fluctuations and terminal current differ;
first weighting-field treatment of semiconductor detector noise.
```

**Disposition:** generic Ramo/noise-coupling claim old.

---

## 2.6 Photon recycling and deterministic HgCdTe pixel crosstalk — KILLED AS GENERIC NOVELTY

Relevant direct prior art includes:

- K. Jóźwikowski, M. Kopytko, and A. Rogalski, *Optical Engineering* **50**, 061003 (2011), modeling generation/recombination and photon recycling in HgCdTe photodiodes.
- A. Jóźwikowska and K. Jóźwikowski, *Optical and Quantum Electronics* **51**, 85 (2019), DOI 10.1007/s11082-019-1781-4, modeling photon reabsorption and optical crosstalk between HgCdTe photodiode pixels.

Thus photon recycling, radiative-lifetime modification, and mean optical crosstalk in HgCdTe arrays are established.

**Disposition:** only the noise-observable boundary can possibly be new.

---

## 2.7 Optical-weight/sum-rule bounds — ESTABLISHED NEIGHBORHOOD, EXPERIMENT-12 RESULT STILL DISTINCT

Relevant neighboring theory:

- Y. Onishi and L. Fu, *Phys. Rev. X* **14**, 011052 (2024), connects topology, quantum geometry, optical absorption, and a bound on topological gaps.
- D. Mao, J. F. Mendez-Valderrama, and D. Chowdhury, *Phys. Rev. B* **112**, 075116 (2025), develops a projected low-energy inverse-frequency-weighted optical sum rule in correlated insulators and relates it to projected quantum geometry / quantum Fisher information.

These works reinforce that optical-response moments, positive spectral weights, and geometric bounds are active established territory.

However the current Experiment-12 theorem remains structurally different: direct cross-chemical-potential transitions, a thermal Fermi kernel, a shellwise velocity-capacity bound, and inversion to a lower bound on equilibrium quasiparticle population.

**Disposition:** no direct collision identified with Experiment 12, but no generic "optical geometry bound" novelty may be claimed.

---

# 3. Finite-transit Shockley–Ramo result: what survives

Experiment 13 now derives exactly

```math
i_k(t)=e\frac{d}{dt}[\phi_k(r_e)-\phi_k(r_h)].
```

For a pair created at one point and later recombining internally at a common point,

```math
Q_k^{rec}=\int i_k dt=0
```

for every electrode, while

```math
H_k^{rec}(\omega)
=i\omega e\int\Delta\phi_k(t)e^{-i\omega t}dt
```

can be nonzero at finite frequency.

The zero integrated charge itself is a direct consequence of standard Shockley–Ramo theory and should not be sold as a new electrodynamic theorem.

The potentially new application is the combination with a **conservative photon-recycling lineage**:

```text
Ramo AC waveform in source pixel
-> internal radiative recombination
-> photon reabsorption in another pixel
-> final collection waveform in destination pixel.
```

This produces a complete event lineage with multichannel finite-frequency support even though the endpoint/DC source-pixel charge is zero.

In the endpoint-counting limit the pre-collection Ramo waveform is discarded and the same conservative lineage has support only in its final sink, restoring exact zero cross-noise.

Focused searches found established:

- Ramo treatment of GR noise;
- HgCdTe photon recycling/crosstalk;
- SPAD crosstalk correlations from branching secondary avalanches;
- segmented-detector weighting-field charge sharing.

The audit did **not** locate a paper explicitly deriving the conservative photon-recycling boundary

```text
endpoint Poisson output: zero interpixel cross-spectrum
versus
finite-transit Ramo readout: AC interpixel lineage overlap
```

for HgCdTe/ordinary photodiode pixels.

This is currently the strongest surviving new result in Experiment 13.

**Status:** novelty plausible, not certified.

---

# 4. Poisson-lineage theorem: mathematical novelty killed, detector specialization survives provisionally

The shot-noise identity

```math
S_y(\omega)
=\sum_a\lambda_a E[H_aH_a^\dagger]
```

is standard Campbell/marked-Poisson shot-noise structure.

The fact that a one-terminal-support lineage gives a diagonal outer product is elementary.

Therefore do not claim the lineage Gram formula as new stochastic-process theory.

What survives is its use as the exact bridge among detector classes:

```text
conservative routing + final sink only
    -> one-lineage/one-terminal support
    -> zero interterminal shot-noise correlation;

finite-transit Ramo or occupancy readout
    -> one lineage can contribute to multiple terminal waveforms
    -> finite-frequency cross-noise allowed;

branching gain/SPAD
    -> one primary lineage can create multiple recorded descendants
    -> correlated counts naturally allowed.
```

The combination gives a clean detector-observable taxonomy even though every mathematical ingredient is established.

---

# 5. Does the four-paper unification survive?

## 5.1 As an abstract theorem paper: NO

A manuscript whose main theorem is merely

```math
Tr(GX)
```

plus eigenvalue bounds would be weak and vulnerable to immediate rejection as elementary repackaging.

Likewise a paper whose thesis is merely

```text
measurement operator matters
```

would not meet the novelty threshold.

## 5.2 As a detector-specific synthesis paper: PROVISIONALLY YES

The audit did not locate a source that simultaneously derives the following as different projections of one detector coupling geometry:

1. task-dependent reversal of detectors with equal conventional scalar `D*`;
2. bright-state coherence rejection of population-identical internal generation;
3. optical cross-mu spectral weight forcing a minimum equilibrium quasiparticle population through a shellwise velocity capacity;
4. conservative photon-recycling dynamics becoming visible or invisible depending on complete lineage-to-terminal readout.

Absence of a search hit is not proof of novelty. More importantly, simple juxtaposition of four old/general mathematical ideas would still not be enough.

The unified paper becomes scientifically strong only if it contains at least one **cross-branch theorem or prediction that is not present in any individual paper**.

The finite-transit recycling result is one such candidate because it was generated by forcing the Experiment-03 observability problem through the unified operator/lineage language.

A second cross-branch theorem is still desirable before a flagship manuscript is authorized.

---

# 6. Strongest remaining significance test

The next research question should not be "can all four be written as `Tr(GX)`?" That has already been answered and is not enough.

The correct question is:

> Does the common spectral geometry impose a new relation between two previously separate detector resources — for example coherence selectivity and thermal population cost, or task anisotropy and microscopic response capacity — that neither Experiment 01, 09, nor 12 contains alone?

A successful theorem of that type would transform Experiment 13 from synthesis into genuinely new theory.

Promising direction:

- use the full singular spectrum of the microscopic optical coupling block, not only its largest singular value;
- connect its effective rank / participation to coherence-selective dark rejection;
- retain the largest singular value as the Experiment-12 population-capacity control;
- ask whether a fixed total optical-strength resource imposes a quantitative relation between selectivity, active-state participation, and the population lower bound.

This is now the highest-value continuation.

---

# 7. Manuscript strategy after this audit

```text
Existing Experiment-01 paper: DO NOT WITHDRAW.
Existing Experiment-09 paper: DO NOT WITHDRAW.
Existing Experiment-12 paper: DO NOT WITHDRAW.
Experiment-13 flagship replacement: NOT YET AUTHORIZED.
Experiment-13 as future synthesis/new-theory paper: KEEP ACTIVE.
```

Reason: the three existing papers have independent detector-specific results and clearer journal identities. Prematurely merging them would sacrifice publishable work for a unified manuscript whose generic mathematical framework is already heavily occupied by prior art.

Only supersede them if Experiment 13 produces a genuinely new cross-branch theorem of sufficient strength that the separate results become natural corollaries rather than loosely related examples.

---

# 8. Final disposition

```text
Generic positive-operator unification:          OLD / ORGANIZING LANGUAGE ONLY
Task/Fisher operator geometry:                  OLD
General quantum photodetector framework:        STRONG PRIOR-ART COLLISION
Detector POVM coherence sensitivity:            OLD
Ramo coupling of GR noise:                      OLD
HgCdTe photon recycling/crosstalk:              OLD
Experiment-12 thermal population theorem:       DISTINCT / RETAIN
Conservative-recycling endpoint cancellation:   DISTINCT DETECTOR SPECIALIZATION / NOVELTY PLAUSIBLE
Finite-transit Ramo recycling AC reopening:     NEW RESULT IN THIS BRANCH / NOVELTY PLAUSIBLE
Four-branch detector-specific closure:           NO DIRECT COLLISION FOUND / SIGNIFICANCE NOT YET ENOUGH
Flagship unified manuscript:                    HOLD
```

## NEXT ACTION

Seek a **second nontrivial cross-branch theorem** from the microscopic singular spectrum, with priority on connecting Experiment 09 coherence selectivity to Experiment 12 thermal-population capacity.

Do not spend time polishing prose or drafting a manuscript before that theorem attempt is completed.
