# Experiment 13 — final hostile claim/reference review of Rev. 4

**Date:** 2026-08-15  
**Manuscript:** `PAPER_DRAFT_REV4_CLAIM_REFERENCE_CLEAN_2026-08-15.md`  
**Reference correction:** `PAPER_REV4_REFERENCE_QA_2026-08-15.md`  
**Review posture:** reject on any central mathematical defect, physical-domain inconsistency, material overclaim, or novelty statement not supported by the cited boundary.  
**Disposition:** **SCIENTIFIC FREEZE PASS / NO CENTRAL DEFECT FOUND / CLAIM SCOPE ACCEPTABLE / REFERENCE NETWORK ADEQUATE / FLAGSHIP FRONTIER MAY BE PROMOTED**

---

# 1. Executive verdict

Rev. 4 passes the scientific-freeze gate.

The manuscript has changed substantially since the first unification attempt. The original vulnerable proposition — that several detector problems can all be written with a positive operator — is no longer the paper's novelty claim. Rev. 4 instead leads with the nontrivial thermal optical population theorem, uses the forward/inverse spectral reciprocity as an organizing connector, obtains a new shell-resolved tightness decomposition and production HgCdTe diagnosis, and then extends the same staged geometry to channel-specific internal observability.

No new central mathematical error was found in the act of combining the source papers.

No claim currently requires reopening the Experiment-01, -09, or -12 derivations.

The correct next phase is production: typeset architecture, figures, reference formatting, and rendered hostile review. New theory should be added only in response to a concrete scientific defect or a clearly superior result.

---

# 2. Principal optical population theorem — PASS

Rev. 4 uses the authoritative Experiment-12 conductivity convention

```math
\sigma_1^{cross}(\omega)
=\frac{\pi e^2}{V}
\sum_{cv}^{cross}
\frac{D_{cv}|v_{cv}|^2}{E_{cv}}
\delta\!\left(\omega-\frac{E_{cv}}{\hbar}\right),
```

and the exact pointwise Fermi inequality

```math
\frac{2D_{cv}}
{e^{E_{cv}/(2k_BT)}-1}
\le p_c+h_v.
```

The thermal kernel and Kubo normalization agree with the controlling Experiment-12 manuscript.

The exact-shell capacity is basis invariant within degenerate eigenspaces and does not permit coherent superposition of different equilibrium energies.

The central result

```math
n_e+n_h
\ge n_{e,B}^{act}+n_{h,B}^{act}
\ge
\frac{2}{\pi e^2(v_B^{cap})^2}
\int_B
\frac{\hbar\omega\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}d\omega
```

has not changed scientifically from the Rev. 11 theorem that already survived independent adversarial regression review.

**PASS.**

---

# 3. Conductivity interpretation — PASS

Rev. 4 repeatedly states that `sigma_1^cross` is the **selected direct cross-chemical-potential contribution**, not automatically the raw total measured conductivity.

This avoids the most dangerous experimental overclaim. Same-side-of-`mu` transitions, intraband response, phonon-assisted channels, excitons, and other contributions are explicitly outside the inserted conductivity unless separately decomposed or isolated.

The conclusion does not revert to saying that arbitrary measured optical conductivity directly yields the population bound.

**PASS.**

---

# 4. Admissible capacity domain — PASS

Rev. 4 correctly elevates the physical domain to part of the theorem.

The capacity

```math
lambda_D=lambda_max(P_DGP_D)
```

is evaluated only after the allowed task/microscopic/readout domain is declared. This prevents artificial weakening by padding the comparison space with irrelevant high-coupling directions.

In the optical theorem the allowed domain is fixed by:

```text
cross-mu endpoint condition;
selected optical window B;
chosen physical velocity polarization;
exact-energy-shell basis freedom.
```

The manuscript also states explicitly that the capacity-maximizing direction need not be strongly occupied in the actual ensemble. That is a physical source of inverse-bound looseness rather than an inconsistency.

**PASS.**

---

# 5. Activity-weighted reciprocity — CORRECT, PROPERLY DEMOTED FROM NOVELTY HEADLINE

For `X>=0` supported in the declared domain,

```math
S_{X|D}
=\frac{lambda_D TrX}{Tr(G_DX)},
```

```math
tau_{X|D}
=\frac{Tr(G_DX)}{lambda_D TrX},
```

so

```math
S_{X|D}tau_{X|D}=1.
```

This is algebraically elementary. Rev. 4 says so.

The paper's claim is now appropriately detector-specific: quantities derived independently in coherent discrimination and thermal optical population inference instantiate the two sides of this relation under their actual physical maps and activity ensembles.

The manuscript does not claim discovery of positive-operator theory, stable rank, or a general measurement principle.

**PASS.**

---

# 6. Experiment-09 specialization — PASS

For

```math
G=|B><B|,
```

and

```math
rho_D=\sum_jw_j|j><j|,
```

Rev. 4 obtains

```math
S=1/\sum_jw_j^2=N_eff.
```

This correctly recovers the nonuniform Experiment-09 result rather than restricting the flagship to the uniform `N` case.

The stronger operational statement — that the bright projector minimizes dark acceptance among yes/no measurements with unit signal acceptance — is retained only for this separately proven rank-one construction, not generalized to arbitrary `G`.

The manuscript also preserves the caveat that coherence selectivity does not alone solve dephasing, extraction, reverse injection, or finite-density kinetics.

**PASS.**

---

# 7. Task-space specialization — PASS

Stable rank appears only for the maximally mixed task ensemble. The equal-trace isotropic comparator and guaranteed worst-task penalty are mathematically correct.

Crucially, Rev. 4 does not falsely claim that the detailed Experiment-01 unknown-arrival theorem is obtained by setting two full task operators to equal trace. The standalone result remains a physical witness under its actual normalization: equal eventual event-specific matched-filter SNR for one transient plus a correlated timing search.

This avoids a hidden hypothesis substitution.

**PASS.**

---

# 8. Endpoint-lifted Experiment-12 positive space — PASS

The direct sum contains one upper-endpoint sector and one lower-endpoint sector because the theorem bounds electron-plus-hole population. This is not double counting an observable by mistake; it mirrors the two endpoint population terms generated by the Fermi inequality.

With the active thermal operator,

```math
TrX_B^{act}/V=n_B^{act},
```

and

```math
Tr(G_BX_B^{act})/V=R_B.
```

The spectral edge is exactly `(v_B^cap)^2` because the norm of a finite direct sum is the maximum block norm.

The global thermal capacity reciprocity is therefore internally consistent.

**PASS.**

---

# 9. Shell-resolved decomposition — PASS AND NOVELTY-BEARING

The identity

```math
tau_cap^{act}
=\sum_aw_a^{act}c_a/S_a^{act}
```

follows exactly from the shell traces, ranks, local spectral norms, global capacity, and thermal weights.

It preserves the energy resolution required by equilibrium occupations rather than mixing dispersive states into a single artificial global stable rank.

Its physical interpretation is clean:

```text
1/S_a^act:
    within-shell singular-spectrum concentration;

c_a:
    shell utilization of the global allowed capacity;

w_a^act:
    actual thermal active-population weight;

eta_F:
    independent Fermi/Kubo statistical conversion.
```

No direct prior-art collision was found for this detector-specific decomposition of the thermal population theorem.

**PASS.**

---

# 10. Production HgCdTe closure — PASS

The production stable-rank audit reproduces the controlling carrier state and broad-window optical sums:

```text
mu                            = 0.1354615106 eV
n_ref                         = 1.005140525e17 cm^-3
R_B                           = 3.987420232e28 cm^-3 (m/s)^2
L_B                           = 1.223486457e28 cm^-3 (m/s)^2
n_B^act                       = 6.724111444e16 cm^-3
v_B^cap                       = 1.01764e6 m/s
eta_F                         = 0.306836598
tau_cap^act                   = 0.572622972
tau_obs^act                   = 0.175701685.
```

The multiplicative closure is exact at the numerical precision relevant to the manuscript:

```math
0.306836598\times0.572622972=0.175701685.
```

The rounded main-text statement `0.573 x 0.307 = 0.1757` is appropriate.

**PASS.**

---

# 11. HgCdTe shell-isotropy claim — PASS WITH CORRECT MODEL SCOPE

Rev. 4 no longer presents `S_a^act=1` as a universal HgCdTe property.

It attributes the machine-precision equality to the **BIA-neglecting second-order Kane validation model**:

```text
fixed-k antiunitary PT doublets;
PT-even velocity operator;
quaternionic 2x2 block;
MM^dagger proportional to I;
equal nonzero singular values.
```

The manuscript explicitly states that real zincblende HgCdTe has bulk inversion asymmetry and that BIA-inclusive models can lift the exact relation.

The now-verified Cartoixà–Ting–McGill PRB reference supports this scope boundary.

The general population theorem itself does not depend on inversion symmetry.

**PASS.**

---

# 12. Photon-recycling endpoint cancellation — PASS UNDER EXPLICIT HYPOTHESES

Rev. 4 lists the hypotheses before claiming exact zero cross-noise:

```text
Poisson primary generation;
independent noninteracting complete lineages;
one final sink per lineage;
final-sink-only measurement;
no branching/gain producing multiple recorded descendants;
no common electronic channel coupling.
```

Under these assumptions, independent final-sink marking/thinning/displacement gives independent output streams.

The manuscript does not claim new Poisson-output mathematics and cites the classical stochastic-process boundary.

It also does not confuse mean optical crosstalk with noise correlation.

**PASS.**

---

# 13. Channel-specific observability and Ramo lifting — PASS

For each terminal,

```math
G_i(omega)=M^dagger|i><i|M>=0
```

correctly gives the channel auto-response. The off-diagonal overlap operator

```math
C_ij=M^dagger|j><i|M
```

is not incorrectly treated as positive.

If a positive internal sector is null to one channel, Cauchy-Schwarz forces its cross contribution with every other channel to vanish.

For an internally created electron-hole pair that later recombines internally at a common point,

```math
Q_i^{rec}=0
```

follows exactly from the Shockley-Ramo weighting-potential endpoint identity.

The finite-frequency expression

```math
H_i^{rec}(omega)
=i omega e int Delta phi_i(t)e^{-i omega t}dt
```

allows nonzero trajectory-level AC support while retaining the exact DC null.

Rev. 4 says this **can** lift the source-channel null and permit a cross-spectrum; it does not guarantee a nonzero ensemble result after symmetry or phase averaging.

The classical Ramo/GR-noise literature is cited and generic priority is not claimed.

**PASS.**

---

# 14. Prior-art/novelty boundary — PASS

The manuscript no longer depends on novelty of its elementary mathematical ingredients.

The candidate-new scientific content is confined to:

```text
- the detector-specific forward-selectivity / inverse-certification cross-identification;
- exact mapping of the nonuniform N_eff and thermal endpoint-capacity quantities;
- shell-resolved decomposition of the optical population theorem;
- production HgCdTe factor diagnosis and model-symmetry explanation;
- conservative photon-recycling final-sink channel null and finite-transit Ramo lifting;
- their organization into one staged detector argument.
```

Targeted searches and the three standalone prior-art audits have not located a direct source reproducing these cross-relations.

The manuscript uses “we derive” rather than unsupported “first” language.

**PASS.**

---

# 15. Reference network — PASS FOR SCIENTIFIC FREEZE

The bibliography now covers the necessary novelty boundaries:

```text
task-based detector/image information;
general quantum photodetector and detector-coherence theory;
state discrimination / bright-state context;
classic infrared material and detailed-balance context;
optical sum rules and modern optical-geometry neighbors;
Kane/HgCdTe parameterization and BIA scope;
Ramo/GR-noise theory;
HgCdTe photon recycling and crosstalk;
classical Poisson-output theory.
```

`PAPER_REV4_REFERENCE_QA_2026-08-15.md` supplies the exact published Ref. 33 and normalizes the 2012 HgCdTe recycling title.

Remaining bibliography work is mechanical journal formatting, not a scientific blocker.

**PASS.**

---

# 16. What still could cause rejection

The likely remaining risks are editorial rather than hidden correctness defects:

```text
1. The central reciprocity can look tautological if the paper does not keep
   the physical population theorem and shell decomposition in the foreground.

2. The paper spans task theory, quantum coherence, multiband semiconductor
   response, and stochastic terminal noise. An editor may view that breadth
   as ambitious or diffuse.

3. The Experiment-03/Ramo specialization has the highest residual historical
   prior-art risk because semiconductor-noise literature is old and broad.

4. The realistic HgCdTe example is one BIA-neglecting model validation rather
   than a universal material survey.

5. Practical application of Eq. (12) requires isolation/modeling of
   sigma_1^cross and an independently justified capacity.
```

These points should be handled by framing and scope, not by adding defensive pages of new theory.

---

# 17. Final disposition

```text
CENTRAL MATHEMATICAL CORRECTNESS:          PASS
EXPERIMENT-12 PHYSICAL THEOREM:            PASS
ACTIVITY-WEIGHTED CONNECTOR:               PASS / elementary algebra acknowledged
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
SCIENTIFIC CONTENT FREEZE:                 AUTHORIZE
EXPERIMENT-13 FLAGSHIP PROMOTION:           AUTHORIZE
TYPESSETTING / FIGURE PRODUCTION:           AUTHORIZE NEXT
NEW THEORY BY DEFAULT:                      STOP
```

## Next action

Promote Experiment 13 to the repository-wide active flagship frontier while explicitly preserving Experiments 01, 09, and 12 as frozen fallback manuscript packages. Then begin submission production from Rev. 4: article-length architecture, figures, complete typeset bibliography, and rendered adversarial QA.
