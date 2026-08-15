# Current State — Experiment 13: Spectral Geometry / Observable-Resource Unification

**Date:** 2026-08-15  
**Scope:** analytical/theoretical only  
**Target:** Physical Review Applied — Regular Article  
**Status:** **FLAGSHIP REV. 4 SCIENTIFICALLY FROZEN / PRODUCTION PDF QA-PASSED / RENDERED HOSTILE REVIEW PASSED / HUMAN METADATA REQUIRED**

## Read first

1. `00_ACTIVE_FRONTIER_REV4_FLAGSHIP_2026-08-15.md`
2. `REV4_PRAPPLIED_PRODUCTION_QA_2026-08-15.md`
3. `PAPER_REV4_RENDERED_HOSTILE_REVIEW_2026-08-15.md`
4. `PAPER_DRAFT_REV4_CLAIM_REFERENCE_CLEAN_2026-08-15.md`
5. `PAPER_REV4_REFERENCE_QA_2026-08-15.md`
6. `PAPER_REV4_FINAL_HOSTILE_CLAIM_REFERENCE_REVIEW_2026-08-15.md`
7. `HGCDTE_STABLE_RANK_PRODUCTION_QA_2026-08-15.md`
8. `HGCDTE_PT_SYMMETRY_STABLE_RANK_EXPLANATION_2026-08-15.md`
9. `CHANNEL_SPECIFIC_OBSERVABILITY_GEOMETRY_2026-08-15.md`

If an older Experiment-13 note disagrees with the files above, this recovery order controls.

## Production identity

```text
GitHub Actions run:   31900965632
head commit:          f41bdc6a4e580bfadd8155903f4127b2b63655ca
artifact ID:          9251078733
artifact digest:      1b4375f9953707ddf1e6b35bf55f91377370274d230298429398096f1b42e01a
PDF SHA-256:          84c86c30019a0517246493ad4b9aacd60ac54051164b27ca7dfedac2fdba800f
built TeX SHA-256:    c1459c18e4bf5d20f09a9a956c23b565c76bd0a913fe9636adc2ca7fe1e2b8f9
pages:                7
undefined refs/cites: none
overfull boxes:       none
all-page visual QA:   PASS
rendered hostile QA:  PASS
```

Five native vector figures are present and visually clean. The remaining underfull/float warnings are nonblocking in the inspected artifact.

## Scientific center

The controlling theorem remains

```math
\boxed{
 n_e+n_h
 \ge n_{e,\mathcal B}^{act}+n_{h,\mathcal B}^{act}
 \ge
 \frac{2}{\pi e^2(v_{\mathcal B}^{cap})^2}
 \int_{\mathcal B}
 \frac{\hbar\omega\sigma_1^{cross}(\omega)}
 {e^{\hbar\omega/(2k_BT)}-1}d\omega.
}
```

It uses selected direct cross-`mu` conductivity and the basis-invariant exact-shell capacity. It is an equilibrium one-body population theorem, not a universal dark-current, generation-rate, finite-bandwidth-noise, or `D*` theorem.

## Unified connector

For a physically declared admissible domain,

```math
\boxed{
\mathcal S_{X|D}\tau_{X|D}=1.
}
```

This is organizing algebra, not a generic matrix novelty claim.

Specializations:

```text
uniform task ensemble:       S=d/r_st
coherent rank-one detector:  S=N_eff=1/sum_j w_j^2
thermal endpoint ensemble:   S_th,B^act=1/tau_cap^act
```

The shell-resolved thermal decomposition is

```math
\tau_{cap}^{act}=\sum_aw_a^{act}\frac{c_a}{\mathcal S_a^{act}},
```

```math
\tau_{obs}^{act}=\eta_F\sum_aw_a^{act}\frac{c_a}{\mathcal S_a^{act}}.
```

## Production HgCdTe result

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
bound/reference               ~= 0.118
bound/active                  ~= 0.176
```

The factor closure is

```math
0.306836598\times0.572622972=0.175701685.
```

Every contributing selected active shell has `S_a^act=1` to about `4e-14` in the BIA-neglecting second-order Kane model. This exact isotropy is model-specific and is not generalized to full zincblende HgCdTe with BIA.

## Recycling / observability result

A terminal has positive observability effect

```math
G_i(\omega)=M^\dagger|i><i|M.
```

A positive internal sector null to one terminal cannot contribute cross-noise with another terminal.

Under independent conservative one-final-sink Poisson lineages, ideal endpoint counting can therefore have exactly zero interterminal cross-spectrum despite internal recycling and mean crosstalk.

For an internally created/recombined pair,

```math
Q_i^{rec}=0
```

while finite-transit Shockley-Ramo motion can give finite-frequency waveform support. The endpoint source-channel null can therefore be lifted at finite frequency; a nonzero ensemble cross-spectrum is allowed, not guaranteed.

## Novelty / significance state

No direct prior-art collision was found in the completed targeted audits. Historical priority is not established and priority language is not authorized.

The strongest remaining referee vulnerabilities are:

```text
breadth / significance of the unified paper;
practical isolation of sigma_cross;
need to establish v_B^cap for a target material;
independent-quasiparticle scope;
realistic bound tightness (~11.8% full / ~17.6% active);
idealized endpoint-Poisson assumptions in the recycling result.
```

These are applicability/editorial questions, not identified theorem defects.

## Standalone manuscripts

```text
Experiment 01 Applied Optics: frozen fallback
Experiment 09 PRA:            frozen fallback
Experiment 12 PRB:            frozen fallback
Experiment 13 flagship:       primary path
```

Do not delete the standalones and do not simultaneously submit materially overlapping versions.

## Remaining blockers

The production source intentionally still contains placeholders for:

```text
author name
institutional affiliation
corresponding email
acknowledgments / funding
```

Those are the only known submission blockers.

## Next action

Do not open a new theory branch by default.

When human metadata is supplied:

```text
insert metadata only;
rebuild through CI;
record the new hashes;
inspect all pages again;
submit if the metadata-only build remains clean.
```

Reopen science only for a concrete mathematical defect, numerical inconsistency, direct prior-art collision, explicit referee/editor request, or specific journal requirement.
