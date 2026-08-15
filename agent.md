# Agent Handoff — Gedanken 3

**Date:** 2026-08-15  
**Active branch:** `experiment-13-observable-resource-unification`  
**Repository-wide frontier:** **Experiment 13 unified flagship Rev. 4 — scientific content frozen; submission production next**

## Read first

1. `experiments/13-observable-resource-unification/00_ACTIVE_FRONTIER_REV4_FLAGSHIP_2026-08-15.md`
2. `experiments/13-observable-resource-unification/PAPER_DRAFT_REV4_CLAIM_REFERENCE_CLEAN_2026-08-15.md`
3. `experiments/13-observable-resource-unification/PAPER_REV4_REFERENCE_QA_2026-08-15.md`
4. `experiments/13-observable-resource-unification/PAPER_REV4_FINAL_HOSTILE_CLAIM_REFERENCE_REVIEW_2026-08-15.md`
5. `experiments/13-observable-resource-unification/PAPER_REV3_EXTREME_NOVELTY_SIGNIFICANCE_REVIEW_2026-08-15.md`
6. `experiments/13-observable-resource-unification/HGCDTE_STABLE_RANK_PRODUCTION_QA_2026-08-15.md`
7. `experiments/13-observable-resource-unification/HGCDTE_PT_SYMMETRY_STABLE_RANK_EXPLANATION_2026-08-15.md`
8. `experiments/13-observable-resource-unification/CHANNEL_SPECIFIC_OBSERVABILITY_GEOMETRY_2026-08-15.md`

If those files conflict with older Experiment-13 notes, the order above controls.

---

# 1. Strategic state

Experiment 13 has passed the scientific-unity, production-HgCdTe, novelty/significance, claim/reference, and final hostile-review gates.

```text
SCIENTIFIC CONTENT FREEZE:       AUTHORIZED
FLAGSHIP-FIRST STRATEGY:         AUTHORIZED
NEW THEORY BY DEFAULT:           STOP
SUBMISSION PRODUCTION:           NEXT
```

The mature standalone manuscripts remain frozen fallback packages:

```text
Experiment 01 — Applied Optics task-order manuscript
Experiment 09 — PRA coherence-selective manuscript
Experiment 12 — PRB optical population-bound manuscript
```

Do not delete or casually rewrite them. Do not submit substantially overlapping standalone and flagship versions simultaneously.

---

# 2. Controlling physical theorem

For selected direct cross-chemical-potential transitions,

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

Authoritative conductivity convention:

```math
\sigma_1^{cross}(\omega)
=\frac{\pi e^2}{V}
\sum_{cv}^{cross}
\frac{D_{cv}|v_{cv}|^2}{E_{cv}}
\delta\!\left(\omega-\frac{E_{cv}}{\hbar}\right).
```

This requires the selected/direct cross-`mu` conductivity contribution, not arbitrary total measured conductivity.

---

# 3. Unified admissible-domain connector

For a physically declared domain `D`,

```math
G_D=P_DGP_D,
\qquad
\lambda_D=\lambda_{max}(G_D),
```

and positive activity `X` supported in `D`,

```math
\mathcal S_{X|D}
=\frac{\lambda_DTrX}{Tr(G_DX)},
```

```math
\tau_{X|D}
=\frac{Tr(G_DX)}{\lambda_DTrX}.
```

Hence

```math
\boxed{\mathcal S_{X|D}\tau_{X|D}=1.}
```

This is organizing algebra, not the novelty headline.

Important specializations:

```text
uniform task ensemble:
    S=d/r_st;

Experiment 09 bright projector:
    S=N_eff=1/sum_j w_j^2;

Experiment 12 endpoint-lifted thermal space:
    S_th,B^act=1/tau_cap^act.
```

---

# 4. Dispersive shell decomposition

For selected endpoint shells `a`,

```math
\boxed{
\tau_{cap}^{act}
=\sum_aw_a^{act}\frac{c_a}{\mathcal S_a^{act}},
}
```

and

```math
\boxed{
\tau_{obs}^{act}
=\eta_F
\sum_aw_a^{act}\frac{c_a}{\mathcal S_a^{act}}.
}
```

This separates:

```text
Fermi/Kubo asymmetry;
shell-to-global capacity mismatch;
within-shell singular-spectrum concentration.
```

---

# 5. Production HgCdTe numbers

Broad 300-K `Eg..0.5 eV` production result:

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

So

```math
0.306836598\times0.572622972=0.175701685.
```

Headline Experiment-12 values remain:

```text
bound/reference ~= 0.118
bound/active    ~= 0.176
lower bound     ~= 1.18e16 cm^-3.
```

Every contributing selected active shell in the current validation has

```math
S_a^{act}=1
```

to about `4e-14`.

That equality is enforced by fixed-k `PT` doublets and quaternionic `PT`-even velocity blocks **only in the BIA-neglecting second-order Kane validation model**. Real zincblende HgCdTe has BIA; do not universalize this result.

---

# 6. Recycling / terminal-observability result

At fixed frequency, terminal `i` has positive effect

```math
G_i(\omega)=M^\dagger|i><i|M.
```

A positive internal sector null to one terminal has zero cross contribution with every other terminal.

Under independent conservative one-final-sink Poisson lineages, final-sink-only counting can therefore give exactly zero interterminal cross-noise despite internal recycling and mean crosstalk.

For a pair created internally and later recombining internally at one point,

```math
Q_i^{rec}=0,
```

but

```math
H_i^{rec}(\omega)
=i\omega e\int\Delta\phi_i(t)e^{-i\omega t}dt
```

can have finite-frequency support. Finite-transit Shockley-Ramo readout can lift the endpoint source-channel null at finite frequency; an ensemble cross-spectrum becomes allowed, not guaranteed.

---

# 7. Novelty boundary

Generic ingredients are established. Do not claim novelty for Gram operators, stable rank, task/Fisher matrices, generic bright/dark states, Shockley-Ramo theory, GR-noise coupling, Poisson output, photon recycling/mean crosstalk, or optical sum rules.

Candidate-new detector content is narrowly:

```text
- forward-selectivity / inverse-certification cross-identification;
- exact mapping of nonuniform N_eff and thermal endpoint capacity;
- shell-resolved population-bound tightness decomposition;
- production HgCdTe factor diagnosis and PT/BIA model interpretation;
- conservative recycling final-sink channel null versus finite-transit Ramo lifting;
- one staged causal organization of these detector limits.
```

Use “we derive,” not unsupported priority language.

---

# 8. Reference correction

Rev. 4 Ref. 33 must be replaced in final typeset source by:

```text
X. Cartoixà, D. Z.-Y. Ting, and T. C. McGill,
“Description of bulk inversion asymmetry in the effective-bond-orbital model,”
Phys. Rev. B 68, 235319 (2003),
doi:10.1103/PhysRevB.68.235319.
```

See `PAPER_REV4_REFERENCE_QA_2026-08-15.md`.

---

# 9. Next action

No new Gedanken branch is authorized by default.

Proceed with unified manuscript production:

```text
1. choose an appropriate broad journal target and article format;
2. produce a lean typeset manuscript from Rev. 4;
3. create only theorem-bearing figures;
4. import/normalize the verified bibliography;
5. compile and perform all-page visual QA;
6. perform an extreme hostile review of the rendered manuscript;
7. only then decide submission target/final package.
```

If production reveals a real scientific defect, repair it. Do not reopen theory merely to make the paper longer or more ornate.
