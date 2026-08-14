# Agent recovery entrypoint

Read `AGENTS.md` first.

## Active Experiment 07 — isotope-tuned HgCdTe SRH capture

Branch: `experiment-07-isotope-srh`

### Read first

1. `experiments/07-isotope-srh/NATURAL_HG_PILOT_GATE_2026-08-14.md`
2. `experiments/07-isotope-srh/ELECTROSTATIC_DEGENERACY_AND_CALIBRATION_2026-08-14.md`
3. `experiments/07-isotope-srh/DLTS_SAMPLE_ARCHITECTURE_AND_REPLICATION_2026-08-14.md`
4. `experiments/07-isotope-srh/ELECTRON_DETUNING_CLOSURE_2026-08-14.md`
5. `experiments/07-isotope-srh/ELECTRON_CAPTURE_BOTTLENECK_AND_REGISTRATION_2026-08-14.md`
6. `experiments/07-isotope-srh/DLTS_OBSERVABILITY_AND_ISOTOPE_DECOMPOSITION_2026-08-14.md`
7. `experiments/07-isotope-srh/TWO_STEP_SRH_KILL_TEST_2026-08-13.md`
8. `experiments/07-isotope-srh/ISOTOPE_AXIS_FINGERPRINT_2026-08-13.md`

Companion numerics now include:
- `numerics/electron_capture_registration.py`
- `numerics/electron_detuning_observability.py`
- `numerics/dlts_paired_replication.py`
- `numerics/natural_hg_pilot_gate.py`
- earlier isotope/DLTS scripts.

## Controlling physics

The detector-relevant target is **electron capture `C_n`** on the mercury-vacancy SRH center. Recent narrow-gap HgCdTe theory states that electron capture is substantially slower than hole capture and governs the SRH rate.

For a one-optical-phonon electron transition,

`Delta_e = hbar omega_op - (E_c-E_t)`.

Isotope substitution changes both terms:

`delta Delta_e = hbar delta omega_op - delta(E_c-E_t)`.

Therefore a `C_n` isotope change alone is not a phonon proof.

The strongest mechanism closure is:

`d[D_I ln C_n]/d[1/(kT)] = -D_I Delta_e`

for the minimal pure one-phonon model, while independently

`D_I Delta_e = hbar D_I omega_op - D_I(E_c-E_t)`

from Raman plus differential emission/capture DLTS.

The two energy shifts must agree. Parallel isotope-insensitive capture reduces the capture slope relative to the independently reconstructed detuning.

## Major metrology correction

Normalized filling-curve registration is useful but does **not** by itself identify `C_n`.

For

`F(t)=integral w(z)[1-exp(-C_n n(z)t)]dz / integral w dz`,

if state B has

`C_B=q_C C_A`

and a uniform fill-density rescaling

`n_B(z)=q_n n_A(z)`,

then exactly

`F_B(t)=F_A(q_C q_n t)`.

Thus

`boxed q_fit = q_C q_n`.

A common multiplicative minority-electron density change is exactly degenerate with a microscopic capture-coefficient change. Multi-time/multi-bias curve collapse detects profile-shape changes but cannot detect this scalar density rescaling.

For an expected 2% isotope signal, the current systematic target is roughly

`uncertainty in Delta ln n_fill <= 0.5%`.

A simple forward-bias quasi-equilibrium density estimate is too sensitive to small `E_g`/electrostatic shifts to serve as the only calibration at low temperature.

The tempting n-type-majority-carrier shortcut is **not yet authorized**: Hg vacancies are double acceptors with Fermi-level-dependent charge states, and current evidence does not establish that simple n-type electron filling measures the same initial charge transition that bottlenecks p-type SRH.

Potential rescues, in order:
1. physical C-V/Hall/Eg/current correction if it reaches sub-percent density-ratio precision;
2. co-located reference electron trap to cancel the common density scale;
3. injection-DLTS-style controlled minority-carrier structure as fallback. Injection-DLTS is established metrology, but no simple HgCdTe implementation has yet been justified.

## Device architecture correction

Do not repeatedly isotope-anneal a finished MIS structure by default. HgCdTe annealing measurably changes passivation/interface charge and CdTe/HgCdTe interdiffusion, so the electrical device would not remain invariant.

Leading architecture:
- adjacent/interleaved sister coupons from one wafer;
- natural-Hg versus enriched-Hg anneals first;
- isotope uptake verified on sacrificial process monitors;
- **one common randomized post-anneal MIS/junction fabrication batch**;
- multiple devices per coupon for within-coupon variance, but coupon pair is the independent material replicate;
- post-process SIMS must verify that surface preparation did not remove the isotope-modified region.

MIS-DLTS in HgCdTe is established and can observe bulk electron traps, but interface-state contamination must be controlled with depletion/fill-bias dependence and C-V/admittance.

## Cheap pre-isotope gate

Do **not** buy enriched Hg yet.

Run a natural-Hg-only sister-pair pilot using the exact proposed anneal/fabrication/DLTS workflow. Artificially label each pair A/B and fit the same registered capture ratio that would be used for isotopes.

For pair/bias `r_jb=ln q_fit`, separate a dangerous pair-level common shift from bias-dependent mismatch and repeat/device noise.

For observed pair RMS `s_obs` from `N` independent pairs, the one-sided 95% upper bound is

`sigma_pair,95 = s_obs sqrt[(N-1)/chi2_(0.05,N-1)]`.

To bound the false common-scale floor below `0.5%`:

```text
s_obs=0.20% -> ~5 pairs
0.30% -> ~10 pairs
0.35% -> ~17 pairs
0.40% -> ~36 pairs
```

Recommended first pilot: **10 adjacent natural-Hg sister pairs**, roughly 3-5 devices/coupon, several filling biases.

Decision:

```text
pair RMS <=~0.3%, bias-invariant q_fit, common-density correction <=~0.5%:
    PASS; 1-2% isotope effect becomes credible.

pair RMS ~0.5-1%:
    only a larger ~5% isotope effect remains attractive.

pair RMS >~1%:
    STOP isotope procurement unless internal-reference or controlled-injection metrology removes the common scale.
```

## Current scientific disposition

```text
heavy-isotope dark-current engineering: STOP
whole-device lifetime isotope experiment: REJECT
finished-device A-B-A anneal: REJECT BY DEFAULT
post-anneal sister-coupon DLTS: LEADING ARCHITECTURE
electron capture C_n: PRIMARY TARGET
horizontal curve registration: RETAIN, but measures C_n*n_fill without extra calibration
overdetermined detuning closure: RETAIN
10-pair natural-Hg pilot: NEXT PHYSICAL GATE
novelty: NOT ESTABLISHED
paper drafting: DO NOT BEGIN
```

## Next hard step

The next research task is to determine whether the minority-density degeneracy can be removed cheaply enough. First test C-V/Hall/Eg/current corrections in the natural-Hg pilot. If those cannot reach the ~0.5-1% common-scale level, identify whether a stable co-located electron trap can provide an internal density reference. Only then consider a custom injection-DLTS HgCdTe structure.

Preserve all negative results and do not reopen closed Experiments 01, 02, 04, 05, or 06 without a new physical constraint.
