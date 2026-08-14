# DLTS sample architecture and paired replication

**Date:** 2026-08-14
**Status:** SAME-FINISHED-DEVICE A-B-A REJECTED BY DEFAULT / TWO-TIER SISTER-COUPON DESIGN RETAINED / PAIRING CAN MAKE 1-5% EFFECT TESTABLE / NOVELTY NOT ESTABLISHED

## 1. Why a finished MIS device should not be isotope-cycled by default

The attractive A-B-A idea was to measure the same electrical device after natural-Hg, enriched-Hg, and reverse natural-Hg anneals. That would suppress device-to-device scatter.

HgCdTe interface physics makes this unsafe as the default architecture. Published MIS studies show that annealing can change fixed interface charge, fast-state density, passivation morphology, and CdTe/HgCdTe interdiffusion substantially. Therefore a finished capacitor exposed repeatedly to long Hg anneals is not guaranteed to remain the same electrical transfer function even if the Hg isotope profile reverses.

This is especially damaging for Experiment 07 because normalized filling-curve registration assumes that the carrier/depletion weighting profile is reproducible between isotope states.

Disposition:

`finished MIS capacitor repeatedly cycled through isotope anneals: REJECT BY DEFAULT`.

Do not claim it is impossible. It could be revisited only after direct evidence that a chosen gate/passivation stack is stable under the exact isotope anneal.

## 2. Two-tier architecture

### Tier A — material crossover coupon

Use unprocessed/sacrificial HgCdTe material for the reversible sequence

`natural Hg -> 204Hg -> natural Hg`.

Purpose:
- establish isotope uptake and reversibility by SIMS/Raman;
- establish the anneal temperature/time needed for the desired isotope depth;
- measure irreversible composition/phonon drift under a matched natural-Hg A-A-A control;
- verify that Hg-vacancy populations can re-equilibrate on the much faster vacancy-diffusion timescale.

No DLTS novelty claim comes from Tier A.

### Tier B — analytical sister coupons

1. Cut adjacent/interleaved sister coupons from one HgCdTe wafer or epilayer.
2. Pair coupons by spatial adjacency before isotope assignment.
3. Randomize one member of each pair to natural-Hg and the other to 204Hg treatment.
4. Apply matched anneal temperature, duration, Hg chemical potential, cooldown and handling.
5. Verify isotope uptake on sacrificial companions and Raman on analytical pieces.
6. After all isotope anneals are complete, perform **one common surface preparation/passivation/MIS fabrication batch** on the analytical coupons.
7. Measure multiple capacitors per coupon to estimate within-coupon processing scatter, but treat the coupon/pair—not each capacitor—as the independent material replicate.
8. Analyze isotope labels blinded if practical.

This gives up electrical same-device A-B-A but avoids repeated annealing of the gate interface.

## 3. Why MIS is still a useful first structure

HgCdTe MIS-DLTS is established. In n-type bulk and LPE HgCdTe, MIS capacitors were used to observe an acceptor-like electron trap in the depletion region and extract its electron capture cross section. Thus a shallow MIS depletion region is a legitimate enabling structure for electron-capture DLTS.

The central risk is interface traps. A bulk mercury-vacancy assignment should therefore require depth/bias consistency rather than one transient peak.

Useful controls:
- repeat the filling-curve registration at several depletion/fill biases;
- verify the extracted isotope scale factor `q` is stable when the depletion width changes within the isotope-modified layer;
- check whether transient amplitude scales with depleted volume rather than behaving as a fixed interface sheet;
- use C-V/admittance to track fixed charge and interface-state changes;
- include multiple capacitor areas if needed, but do not mistake multiple capacitors on one coupon for independent isotope samples.

## 4. Surface preparation can consume the isotope-modified layer

The isotope profile is shallow by design. Any post-anneal etch/passivation step can remove or redistribute part of the enriched region.

Therefore the relevant isotope profile is **not** the profile immediately after Hg annealing. Sacrificial process-monitor pieces should be carried through the same surface preparation/passivation steps and measured by SIMS afterward.

The analytical depletion region must lie inside the isotope-modified region **after full device processing**.

This is a hard geometry gate.

## 5. Paired statistical model

Let the isotope effect be

`delta = ln(Cn_enriched/Cn_natural)`.

Let each coupon have RMS log-capture scatter `s`. If adjacent sister coupons have correlation `rho` from common wafer position/material history, the difference of one pair has

`sigma_pair = s sqrt[2(1-rho)]`.

For `N` independent sister pairs,

`Z = |delta| sqrt(N) / [s sqrt(2(1-rho))]`.

Hence

`boxed: N = 2 Z^2 s^2 (1-rho) / delta^2`.

This makes spatial pairing a material resource rather than an administrative detail.

At `Z=5`:

```text
per-coupon scatter s=2%, isotope effect=2%:
rho=0     -> 52 pairs (equivalent to the unpaired scale)
rho=0.50  -> 26 pairs
rho=0.75  -> 13 pairs
rho=0.90  ->  6 pairs
rho=0.95  ->  3 pairs
```

For `s=1%`, 2% isotope effect:

```text
rho=0     -> 13 pairs
rho=0.75  ->  4 pairs
rho=0.90  ->  2 pairs
```

For `s=2%`, 5% isotope effect:

```text
rho=0     -> 9 pairs
rho=0.50  -> 5 pairs
rho=0.75  -> 3 pairs
rho=0.90  -> 1 pair by the Gaussian planning formula
```

Do not interpret the one-pair number as sufficient scientific replication; systematic controls still require multiple independent pairs. The formula is only the statistical-noise floor.

Companion: `numerics/dlts_paired_replication.py`.

## 6. Pseudoreplication rule

If one coupon contains ten nominally identical MIS capacitors, those ten devices are useful for estimating within-coupon fabrication/readout variance. They are **not ten independent isotope-material replicates**.

The primary isotope inference should be hierarchical:

`device within coupon within sister pair`.

The pair-level effect is what tests isotope mass.

## 7. Practical first-stage go gate

Before purchasing a large isotope-material set, fabricate ordinary natural-Hg sister coupons through the proposed MIS process and measure registered electron filling curves.

Estimate:
- within-coupon device scatter;
- adjacent-coupon correlation `rho`;
- pair-level RMS scatter in `ln C_n` after horizontal curve registration;
- bias-to-bias stability of the registered scale;
- bulk/interface trap separation.

Decision rule:

```text
pair-level reproducibility <=~1%:
    a 1-2% isotope effect is experimentally credible with modest replication.

pair-level reproducibility ~2%:
    5% effects remain easy; a 2% effect needs strong sister correlation and several-to-tens of pairs.

pair-level reproducibility >=5%:
    the natural-Hg -> 204Hg experiment is unattractive unless theory predicts a much larger near-threshold response.
```

This natural-Hg reproducibility experiment is cheaper and should precede isotope procurement.

## 8. Current disposition

```text
same finished device A-B-A DLTS: REJECT BY DEFAULT
material-only A-B-A crossover: RETAIN as isotope-uptake/reversibility validation
post-anneal common-batch MIS fabrication: LEADING electrical architecture
adjacent sister-pair randomization: REQUIRED
multiple devices per coupon: REQUIRED for variance estimate, not independent n
post-process SIMS depth verification: REQUIRED
bulk-vs-interface bias/depth control: REQUIRED
novelty: NOT ESTABLISHED
paper drafting: DO NOT BEGIN
```

## 9. Next hard step

Run a natural-Hg-only process reproducibility surrogate analytically/numerically: determine what measured combination of filling-curve registration, C-V shift, depletion-width change and interface-transient contamination would cause a false 1-2% `C_n` isotope signal.

Then define a quantitative electrostatic-invariance gate for a real sample before isotope material is used.
