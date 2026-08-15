# Experiment 13 Rev. 6 — response to extreme Rev. 5 re-review

**Date:** 2026-08-15  
**Target:** Physical Review Applied — Regular Article  
**Disposition:** **PUBLICATION ARCHITECTURE RESOLVED / FOUR TECHNICAL REPAIRS APPLIED / STANDALONE NUMERICAL REPRODUCIBILITY RESTORED / CENTRAL THEOREM UNCHANGED**

## 1. Publication-overlap issue — resolved structurally

The re-review correctly identified a potentially blocking issue if Experiment 12 and Experiment 13 were intended as two separate publications: Experiment 13 inherits the same cross-chemical-potential population theorem and substantially the same production HgCdTe validation.

The controlling project strategy is now explicit:

```text
Experiment 13: primary active submission manuscript;
Experiment 12: frozen fallback/development record;
simultaneous or second overlapping submission of the present Experiment-12 manuscript: prohibited.
```

A dedicated hold notice now exists at

`experiments/12-oscillator-strength-state-count-bound/00_SUBMISSION_HOLD_EXPERIMENT13_SUPERSESSION_2026-08-15.md`.

Experiment 13 therefore replaces Experiment 12 for the current publication path. It must be self-contained enough to support the inherited theorem and HgCdTe validation on its own.

## 2. Thermodynamic uniform-capacity condition — restored

Rev. 5 accidentally compressed away a formal distinction that the mature Experiment-12 theorem had already established: finite capacity at each finite normalization volume does not by itself imply a nonzero macroscopic density floor.

Rev. 6 restores

```math
\boxed{
\bar v_{\mathcal B}^{\rm cap}
=\limsup_{j\to\infty}v_{\mathcal B,V_j}^{\rm cap}<\infty.
}
```

The manuscript now states explicitly:

```text
Eq. (main theorem) is an exact finite-system inequality at finite V;
its macroscopic density interpretation additionally requires the uniform thermodynamic capacity condition;
finite v_cap at every finite V is insufficient if v_cap diverges with V.
```

The limitation is repeated in the Discussion.

No finite-system theorem changes.

## 3. HgCdTe numerical reproducibility — restored

Because Experiment 13 now replaces Experiment 12, Rev. 6 restores the numerical-method details needed to interpret and reproduce the production validation.

The manuscript now states:

```text
Eg = 0.123984 eV;
x = 0.17973;
Delta = 1.04945 eV;
F = -0.01618;
gamma1 = 3.6273;
gamma2 = 0.3598;
gamma3 = 1.0717;
EP = 18.8 eV;
carrier cutoff |k| <= 2.0 nm^-1;
chemical potential from eight-band charge neutrality;
production optical quadrature = 160 x 10 x 16;
independent support check = 200 x 12 x 20;
degeneracy clustering tolerance = 1e-7 eV;
capacity = continuous (k,theta,phi) projected-block supremum, not maximum quadrature node;
selected broad-window transitions sampled through |k| = 0.583 nm^-1.
```

These are inherited production settings, not new parameter choices introduced in Rev. 6.

## 4. Numerical support-rank criterion — stated and stress-tested

For diagnostic support populations, Rev. 6 now states the numerical realization of exact support rank:

```math
s>10^{-6}\ {\rm m/s}
```

is counted as nonzero.

The manuscript also reports the existing audit:

```text
reduced audit grid: 40 x 6 x 8;
threshold sweep: 1e-9 through 1e4 m/s;
broad-window active-support fraction: unchanged to printed precision.
```

The text makes clear that this threshold enters the support diagnostic only. The central population lower bound itself is rank-threshold independent.

The degeneracy-clustering tolerance was also previously swept from `1e-10` to `1e-5 eV` with no change in the reported capacity precision; Rev. 6 now states that check.

## 5. Optical `observability` terminology collision — removed

Rev. 5 used

```math
\tau_{\rm obs}^{\rm act}
```

for optical bound tightness while later reserving observability for terminal-map null spaces.

Rev. 6 renames the optical quantity everywhere to

```math
\boxed{\tau_{\rm bound}^{\rm act}}
```

and renames the shell equation label accordingly.

A hard CI regression check rejects any remaining `tau_obs^act` token in the generated manuscript.

Terminal `observability` is now reserved for the internal/readout stage.

## 6. Fermi/Kubo terminology — corrected

The `0.3068` factor is now called the **Fermi-statistical factor**

```math
\eta_F=\mathcal L_{\mathcal B}/\mathcal R_{\mathcal B}\le1.
```

The manuscript explicitly states that the inequality/slack arises from the endpoint Fermi bound, whereas Kubo--Greenwood is the exact spectral bookkeeping map and introduces no additional slack.

Figures likewise use `Fermi factor`, `Fermi-statistical asymmetry`, and `Kubo map + Fermi bound` rather than treating Kubo as an independent loss mechanism.

## 7. Task/coherence section — retained deliberately

The re-review correctly identifies the uniform-task subsection as the easiest material to compress if an editor asks for a narrower manuscript.

No technical defect was identified there. It is retained in Rev. 6 because the current flagship goal is the stage-specific unified detector framework and because the task/coherence branch provides the forward-selectivity side of that framework.

If editorial compression is later required, the order of sacrifice is:

```text
compress generic uniform-task exposition first;
retain the N_eff coherent photodetection specialization if possible;
do not compress the central semiconductor theorem, full tightness hierarchy, HgCdTe reproducibility, or recycling/Ramo boundary merely to preserve generic task algebra.
```

## 8. Central result — unchanged

Rev. 6 does not alter the cross-mu Fermi inequality, Kubo-Greenwood normalization, exact-shell capacity definition, singular-value/rank theorem, shell decomposition, HgCdTe production values, Poisson final-sink theorem, or Shockley--Ramo result.

The full tightness hierarchy remains

```math
\boxed{
\frac{n_{\rm bound}}{n_{\rm ref}}
=
\frac{n_{\mathcal B}^{\rm act}}{n_{\rm ref}}
\eta_F
\sum_a w_a^{\rm act}\frac{c_a}{\mathcal S_a^{\rm act}}.
}
```

with the broad HgCdTe closure

```math
0.66897\times0.30684\times0.57262=0.1175398\ldots.
```

## 9. Production status

Rev. 6 is generated deterministically from the reconstructed Rev. 5 source by `typeset/build_rev6.py` and compiled independently in GitHub Actions.

The controlling production identity is recorded in `REV6_PRAPPLIED_PRODUCTION_QA_2026-08-15.md`.

## Recommendation

Rev. 6 should supersede Rev. 5. The second adversarial review found real formal/reproducibility issues worth correcting, but it did not expose a new theorem failure. With Experiment 12 explicitly held as a nonconcurrent fallback, the remaining overlap concern is a project-publication constraint rather than a defect in the unified manuscript.
