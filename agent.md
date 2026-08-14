# Agent recovery entrypoint

Read `AGENTS.md` first.

## Active Experiment 07 — isotope-tuned HgCdTe SRH capture

Branch: `experiment-07-isotope-srh`

### Read first

1. `experiments/07-isotope-srh/00_ACTIVE_FRONTIER_INTERNAL_REFERENCE_2026-08-14.md`
2. `experiments/07-isotope-srh/NEGATIVE_U_INTERNAL_REFERENCE_SCREEN_2026-08-14.md`
3. `experiments/07-isotope-srh/NATURAL_HG_PILOT_GATE_2026-08-14.md`
4. `experiments/07-isotope-srh/ELECTROSTATIC_DEGENERACY_AND_CALIBRATION_2026-08-14.md`
5. `experiments/07-isotope-srh/DLTS_SAMPLE_ARCHITECTURE_AND_REPLICATION_2026-08-14.md`
6. `experiments/07-isotope-srh/ELECTRON_DETUNING_CLOSURE_2026-08-14.md`
7. `experiments/07-isotope-srh/ELECTRON_CAPTURE_BOTTLENECK_AND_REGISTRATION_2026-08-14.md`
8. `experiments/07-isotope-srh/DLTS_OBSERVABILITY_AND_ISOTOPE_DECOMPOSITION_2026-08-14.md`
9. `experiments/07-isotope-srh/TWO_STEP_SRH_KILL_TEST_2026-08-13.md`

Relevant numerics include `negative_u_two_capture_identifiability.py`, `electron_capture_registration.py`, `electron_detuning_observability.py`, `natural_hg_pilot_gate.py`, and earlier isotope/DLTS scripts.

## Controlling physics

The detector-relevant target is mercury-vacancy **electron capture `C_n`**. Current narrow-gap theory finds electron capture slower than hole capture and therefore rate-limiting for SRH.

For a one-optical-phonon electron transition use the electron-side energy release/detuning; do not reuse the hole binding energy. Isotope substitution can shift both the phonon energy and the electronic vacancy-band separation. A `C_n` change alone is not proof of a phonon mechanism.

The strongest closure remains the isotope-temperature slope of direct capture compared with the independently reconstructed detuning shift from Raman plus emission/capture DLTS.

## Critical metrology degeneracy

Normalized filling-curve registration measures a product. If

```math
C_B=q_C C_A,
\qquad n_B(z)=q_n n_A(z),
```

then

```math
F_B(t)=F_A(q_Cq_n t),
```

so

```math
q_{fit}=q_Cq_n.
```

A common minority-density rescaling is exactly degenerate with a microscopic capture-coefficient change. Multi-bias curve collapse detects profile-shape changes but not this scalar rescaling.

For an expected ~2% isotope effect, target common-density uncertainty is roughly <=0.5%.

## Internal-reference result

A second resolved electron capture in the same filling population would cancel the unknown density:

```math
D_{ij}=\ln[(\lambda_i/\lambda_j)_B/(\lambda_i/\lambda_j)_A]
=\Delta_I\ln C_i-\Delta_I\ln C_j.
```

A same-defect negative-U version is possible in principle if two sequential electron captures are actually resolved. For

```text
V0 --a=C1*n--> V- --b=C2*n--> V2-
```

```math
\bar N_e(t)=2-\frac{2b-a}{b-a}e^{-at}+\frac{a}{b-a}e^{-bt}.
```

The shape contains `b/a=C2/C1`, independent of `n`.

But this is **not the baseline solution**:

- the Hg-vacancy intermediate charge state is negative-U and can be hidden in thermal measurements;
- `b/a=1/2` gives an exact single exponential;
- `b/a >> 1` also approaches a single exponential because the intermediate state is scarcely occupied;
- available HgCdTe SRH theory does not establish that the operating recombination loop gives two simultaneously observable electron-capture rates.

Retain same-defect two-rate fitting only as a bonus if the natural-Hg pilot actually reveals it. Do not force the interpretation.

## Leading physical experiment

Do **not** buy enriched Hg yet.

Run a natural-Hg-only pilot using adjacent sister coupons, matched Hg anneals, then one common randomized post-anneal device-fabrication batch. Use ~10 independent sister pairs, several devices/coupon and several filling biases.

The pilot must measure the false isotope-like pair shift. A practical pass target remains roughly <=0.3% pair RMS plus <=0.5% common minority-density correction for a 1-2% expected isotope effect.

Add one new requirement: acquire filling curves across 3-4 decades of pulse duration and explicitly test for a stable second electron-capture rate. If present and reproducible across bias/temperature, evaluate it as an internal density reference. If absent, retain external density calibration.

## Current disposition

```text
heavy-isotope dark-current engineering: STOP
whole-lifetime isotope experiment: REJECT
finished-device A-B-A anneal: REJECT BY DEFAULT
post-anneal sister-coupon DLTS: LEADING ARCHITECTURE
electron capture C_n: PRIMARY TARGET
horizontal registration alone: INSUFFICIENT; measures C_n*n_fill
same-defect negative-U internal reference: CONDITIONAL BONUS ONLY
co-located reference electron trap: USEFUL IF ACTUALLY RESOLVED
10-pair natural-Hg pilot: NEXT PHYSICAL GATE
custom injection-DLTS: FALLBACK ONLY
novelty: NOT ESTABLISHED
paper drafting: DO NOT BEGIN
```

Preserve all negative results. Experiments 01, 02, 04, 05 and 06 remain closed unless a genuinely new physical constraint defeats their documented stop.
