# Active Frontier — Experiment 13 unified flagship Rev. 4

**Date:** 2026-08-15  
**Branch:** `experiment-13-observable-resource-unification`  
**Status:** **SCIENTIFIC CONTENT FROZEN / FLAGSHIP-FIRST STRATEGY AUTHORIZED / SUBMISSION PRODUCTION NEXT**

This file supersedes earlier Experiment-13 recovery notes whenever they disagree with it.

## Controlling manuscript

`PAPER_DRAFT_REV4_CLAIM_REFERENCE_CLEAN_2026-08-15.md`

Apply the bibliography corrections in:

`PAPER_REV4_REFERENCE_QA_2026-08-15.md`

The final scientific-freeze review is:

`PAPER_REV4_FINAL_HOSTILE_CLAIM_REFERENCE_REVIEW_2026-08-15.md`

Disposition:

```text
CENTRAL MATHEMATICAL CORRECTNESS:          PASS
EXPERIMENT-12 PHYSICAL THEOREM:            PASS
ACTIVITY-WEIGHTED CONNECTOR:               PASS
EXPERIMENT-09 SPECIALIZATION:              PASS
TASK SPECIALIZATION:                       PASS
SHELL DECOMPOSITION:                       PASS
PRODUCTION HgCdTe VALIDATION:              PASS
HgCdTe BIA/PT MODEL SCOPE:                 PASS
ENDPOINT POISSON CANCELLATION:             PASS under explicit hypotheses
CHANNEL/RAMO OBSERVABILITY:                PASS
CLAIM SCOPE:                               PASS
REFERENCE-NETWORK SCIENTIFIC ADEQUACY:      PASS
DIRECT PRIOR-ART COLLISION FOUND:          NO
SCIENTIFIC CONTENT FREEZE:                 AUTHORIZED
```

## Central physical theorem

For selected direct cross-chemical-potential transitions in an equilibrium independent-quasiparticle system,

```math
\boxed{
 n_e+n_h
 \ge
 n_{e,\mathcal B}^{act}+n_{h,\mathcal B}^{act}
 \ge
 \frac{2}{\pi e^2(v_{\mathcal B}^{cap})^2}
 \int_{\mathcal B}
 \frac{\hbar\omega\sigma_1^{cross}(\omega)}
 {e^{\hbar\omega/(2k_BT)}-1}d\omega.
}
```

Use the authoritative conductivity convention

```math
\sigma_1^{cross}(\omega)
=\frac{\pi e^2}{V}
\sum_{cv}^{cross}
\frac{D_{cv}|v_{cv}|^2}{E_{cv}}
\delta\!\left(\omega-\frac{E_{cv}}{\hbar}\right).
```

The theorem requires the **selected direct cross-mu conductivity contribution**, not arbitrary raw total conductivity.

## Unified admissible-domain reciprocity

For a physically declared admissible domain `D`,

```math
G_D=P_DGP_D\succeq0,
\qquad
\lambda_D=\lambda_{max}(G_D),
```

and positive activity `X` with `supp(X) subset D`, define

```math
\mathcal S_{X|D}
=\frac{\lambda_DTrX}{Tr(G_DX)},
```

```math
\tau_{X|D}
=\frac{Tr(G_DX)}{\lambda_DTrX}.
```

Then

```math
\boxed{\mathcal S_{X|D}\tau_{X|D}=1.}
```

This is organizing algebra, not a claim of new matrix theory. The novelty-bearing content lies in the detector-specific realizations and cross-relations.

## Exact specializations

### Coherent bright-state detector

For `G=|B><B|` and population-matched incoherent

```math
\rho_D=\sum_jw_j|j><j|,
```

```math
\boxed{
\mathcal S=\frac1{\sum_jw_j^2}=N_{eff}.
}
```

Experiment 09 independently proves this projector minimizes dark acceptance subject to unit signal acceptance.

### Uniform task ensemble

```math
r_{st}=TrG/\lambda_{max},
```

```math
\mathcal S_{mix}=d/r_{st}.
```

At fixed trace, at least one orthogonal task satisfies

```math
\boxed{
q_{worst}/q_{iso}
\le(d-\mathcal S_{mix})/(d-1).
}
```

Experiment 01 remains a separate physical unknown-arrival witness under its own eventual-SNR normalization; do not claim it is literally the equal-trace theorem.

### Thermal endpoint space

The endpoint-lifted operator `G_B` has

```math
\lambda_{max}(G_B)=(v_B^{cap})^2,
```

```math
Tr(G_BX_B^{act})/V=\mathcal R_B,
```

```math
TrX_B^{act}/V=n_B^{act}.
```

Therefore

```math
\boxed{
\mathcal S_{th,B}^{act}\tau_{cap}^{act}=1,
}
```

and with

```math
\eta_F=\mathcal L_B/\mathcal R_B,
```

```math
\boxed{
\mathcal S_{th,B}^{act}\tau_{obs}^{act}=\eta_F.
}
```

## Shell-resolved decomposition

For selected endpoint shells `a`,

```math
\boxed{
\tau_{cap}^{act}
=\sum_aw_a^{act}\frac{c_a}{\mathcal S_a^{act}},
}
```

```math
\boxed{
\tau_{obs}^{act}
=\eta_F\sum_aw_a^{act}\frac{c_a}{\mathcal S_a^{act}}.
}
```

This separates:

```text
Fermi/Kubo asymmetry;
shell-to-global capacity mismatch;
within-shell singular-spectrum concentration.
```

## Production HgCdTe closure

Broad 300-K `Eg..0.5 eV` production audit:

```text
mu                            = 0.1354615106 eV
n_ref                         = 1.005140525e17 cm^-3
R_B                           = 3.987420232e28 cm^-3 (m/s)^2
L_B                           = 1.223486457e28 cm^-3 (m/s)^2
n_B^act                       = 6.724111444e16 cm^-3
v_B^cap                       = 1.01764e6 m/s
eta_F                         = 0.306836598
tau_cap^act                   = 0.572622972
tau_obs^act                   = 0.175701685
S_th,B^act                    ~= 1.746
```

Thus

```math
0.306836598\times0.572622972=0.175701685.
```

The selected active exact-shell blocks satisfy

```math
\mathcal S_a^{act}=1
```

to about `4e-14` in this validation.

This is symmetry enforced **within the BIA-neglecting second-order Kane model** by fixed-k antiunitary `PT` doublets and quaternionic `PT`-even velocity blocks. Real zincblende HgCdTe has bulk inversion asymmetry; do not generalize the exact shell isotropy without a BIA-inclusive calculation.

## Channel-specific recycling observability

At fixed frequency,

```math
G_i(\omega)=M^\dagger|i><i|M\succeq0
```

is the positive observability effect of terminal `i`, while

```math
C_{ij}(\omega)=M^\dagger|j><i|M
```

gives the cross-channel overlap.

A positive internal sector null to one terminal has zero cross contribution with every other terminal.

Under independent conservative one-final-sink Poisson lineages, ideal endpoint counting can therefore yield exactly zero interterminal cross-noise even with nonzero internal recycling and mean crosstalk.

For a pair created internally and later recombining internally at a common point,

```math
\boxed{Q_i^{rec}=0}
```

for every electrode, but

```math
\boxed{
H_i^{rec}(\omega)
=i\omega e\int\Delta\phi_i(t)e^{-i\omega t}dt
}
```

can have finite-frequency support. Finite-transit Shockley-Ramo readout can therefore lift a source-channel endpoint null at finite frequency; a nonzero ensemble cross-spectrum is allowed, not guaranteed.

## Novelty boundary

Do not claim novelty for:

```text
positive/Gram operators;
stable rank or singular-value inequalities;
task/Fisher-information matrices;
bright/dark states or generic quantum discrimination;
Shockley-Ramo theory;
GR-noise coupling;
Poisson thinning/output;
HgCdTe photon recycling or mean crosstalk;
optical sum rules or geometric response bounds.
```

Candidate-new detector content is narrowly:

```text
1. detector-specific forward-selectivity / inverse-certification cross-identification;
2. exact mapping of nonuniform N_eff and thermal endpoint-capacity quantities;
3. shell-resolved decomposition of the optical population theorem;
4. production HgCdTe factor diagnosis and model-symmetry explanation;
5. conservative recycling final-sink channel null versus finite-transit Ramo lifting;
6. their causal organization into one staged detector argument.
```

No direct prior-art collision was found in the completed targeted audits. Use “we derive,” not unsupported priority language such as “first.”

## Bibliography correction controlling Rev. 4

Rev. 4 Ref. 33 must be typeset as:

```text
X. Cartoixà, D. Z.-Y. Ting, and T. C. McGill,
“Description of bulk inversion asymmetry in the effective-bond-orbital model,”
Phys. Rev. B 68, 235319 (2003),
doi:10.1103/PhysRevB.68.235319.
```

See `PAPER_REV4_REFERENCE_QA_2026-08-15.md` for the complete reference-QA disposition.

## Publication strategy

```text
Experiment 13 unified flagship:  PRIMARY path
Experiment 01 manuscript:        FREEZE as fallback / possible later distinct companion
Experiment 09 manuscript:        FREEZE as fallback / possible later distinct kinetics companion
Experiment 12 manuscript:        FREEZE as fallback PRB package
```

Do **not** simultaneously submit substantially overlapping flagship and standalone versions.

Do **not** delete or rewrite the standalone packages. They preserve scientifically mature fallback routes if the flagship is rejected for breadth/significance.

## Next action

Begin submission production from Rev. 4:

```text
1. choose journal target/format based on manuscript scope;
2. create lean article architecture and typeset source;
3. build only theorem-bearing figures;
4. normalize/verify final bibliography mechanically;
5. compile and perform all-page rendered QA;
6. subject the rendered manuscript to another extreme hostile review.
```

No new theory should be added by default unless production or external review reveals a concrete scientific defect.
