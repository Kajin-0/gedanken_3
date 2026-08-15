# Experiment 12 — Rev11 final adversarial regression audit

**Date:** 2026-08-15  
**Branch:** `experiment-12-oscillator-strength-state-count-bound`  
**Scope:** analytical/theoretical only  
**Disposition:** **CENTRAL THEOREM SURVIVES / HgCdTe VALIDATION REMAINS INTERNALLY CONSISTENT / ONE CONCRETE PRE-SUBMISSION LITERATURE-COMPLETENESS AMENDMENT IDENTIFIED / NO SCIENTIFIC REVISION TRIGGERED**

## 1. Audit target

This audit independently re-read the controlling Rev9 exposition source together with the complete Rev9→Rev10 and Rev10→Rev11 patches, then rechecked the theorem chain and the HgCdTe numerical implementation at the level most likely to expose a referee-grade regression.

Primary objects checked:

1. pointwise Fermi inequality;
2. Kubo-Greenwood normalization and thermal-kernel conversion;
3. exact-energy-shell projected-block capacity;
4. singular-value/rank conversion from velocity strength to active population;
5. thermodynamic and moving-window quantifiers;
6. clean-bulk specialization of the exact shell capacity to a k-resolved ordinary supremum;
7. second-order 8-band HgCdTe implementation and numerical interpretation;
8. scope statements and forbidden downstream inferences;
9. nearest optical-sum-rule literature, including literature not currently cited in Rev11.

No reliance was placed on the historical claim that earlier reviews had passed. The central algebra was re-derived independently.

---

# 2. Central theorem regression check

The controlling hierarchy is

```math
n_e+n_h
\ge n_{e,\mathcal B}^{\rm act}+n_{h,\mathcal B}^{\rm act}
\ge
\frac{2}{\pi e^2(v_{\mathcal B}^{\rm cap})^2}
\int_{\mathcal B}
\frac{\hbar\omega\,\sigma_1^{\rm cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}\,d\omega.
```

## 2.1 Pointwise Fermi inequality — PASS

For a crossing pair `E_v < mu < E_c`, define

```math
a=e^{-(E_c-\mu)/(k_BT)},
\qquad
b=e^{-(\mu-E_v)/(k_BT)},
\qquad
ab=e^{-E_{cv}/(k_BT)}.
```

Then

```math
D_{cv}=\frac{1-ab}{(1+a)(1+b)},
```

and

```math
p_c+h_v=\frac{a+b+2ab}{(1+a)(1+b)}.
```

At fixed `E_cv`, `ab` is fixed. AM-GM gives `a+b >= 2 sqrt(ab)`, which is exactly equivalent to

```math
\frac{2D_{cv}}
{e^{E_{cv}/(2k_BT)}-1}
\le p_c+h_v.
```

Equality occurs iff `a=b`, equivalently

```math
E_c-\mu=\mu-E_v=E_{cv}/2.
```

No hidden nondegenerate or Maxwell-Boltzmann approximation is present.

## 2.2 Kubo-Greenwood normalization — PASS

With the manuscript convention

```math
\sigma_1^{\rm cross}(\omega)
=
\frac{\pi e^2}{V}
\sum_{cv}
\frac{D_{cv}|v_{cv}|^2}{E_{cv}}
\delta\!\left(\omega-\frac{E_{cv}}{\hbar}\right),
```

the thermal kernel

```math
K_T(E)=\frac{E}{e^{E/(2k_BT)}-1}
```

cancels the `1/E_cv` factor at the delta-function support. Therefore

```math
\frac{2}{\pi e^2}
\int_{\mathcal B}
K_T(\hbar\omega)\sigma_1^{\rm cross}(\omega)d\omega
```

is exactly

```math
\frac{2}{V}
\sum_{(c,v)\in\mathcal T_{\mathcal B}}
\frac{D_{cv}|v_{cv}|^2}
{e^{E_{cv}/(2k_BT)}-1}.
```

The prefactor and frequency/energy delta-function normalization are consistent. Rev10's explicit introduction of the energy-domain window `\mathcal E_\mathcal B={\hbar\omega:\omega\in\mathcal B}` in the numerical section correctly removes the earlier notation ambiguity.

## 2.3 Projected-shell capacity and rank step — PASS

For one exact upper shell,

```math
A_{\epsilon_c,\mathcal B}
=P_{\epsilon_c}\hat v_iQ^-_{\epsilon_c,\mathcal B},
```

and for one lower shell,

```math
B_{\epsilon_v,\mathcal B}
=Q^+_{\epsilon_v,\mathcal B}\hat v_iP_{\epsilon_v}.
```

Regrouping the thermally weighted velocity strength by exact shell produces traces of `AA^dagger` and `B^dagger B`. For every finite-dimensional block,

```math
Tr(XX^\dagger)
=\sum_j s_j^2
\le s_{\max}^2\,rank(X)
=\|X\|_{op}^2 rank(X).
```

Since all vectors in an exact energy shell have the same equilibrium Fermi factor, multiplication by shell occupation commutes with this basis-invariant regrouping. Summing the shell inequalities gives

```math
\mathcal R_{\mathcal B}(T)
\le(v_{\mathcal B}^{\rm cap})^2
(n_{e,\mathcal B}^{\rm act}+n_{h,\mathcal B}^{\rm act}).
```

The support-rank construction therefore closes the state-reuse loophole correctly. A pairwise `max |v_cv|` is not sufficient in a multidegenerate block.

Independent random finite-matrix stress tests of the same algebra satisfied, case by case,

```text
thermal optical lower sum <= R_B
R_B <= vcap^2 n_B^act
thermal optical lower sum / vcap^2 <= n_B^act
```

with arbitrary complex multiband coupling blocks and shell dimensions. This is a regression check of the algebra, not an additional proof assumption.

## 2.4 Total-population inequality — PASS

For every exact shell,

```math
rank(A_{\epsilon_c,\mathcal B}) <= dim P_{\epsilon_c},
```

and similarly for the lower shell. Consequently

```math
n_{e,\mathcal B}^{\rm act}\le n_e,
\qquad
n_{h,\mathcal B}^{\rm act}\le n_h.
```

No oscillator-strength threshold enters this exact theorem. The numerical `1e-6 m/s` singular-value cutoff is correctly restricted to the diagnostic active-support decomposition in Table II.

---

# 3. Thermodynamic and low-energy statements

## 3.1 Fixed-window thermodynamic limit — PASS, conditional as stated

A finite-volume inequality does not by itself imply a nonzero macroscopic density floor if one exact shell can acquire a diverging optical norm as volume grows. Rev11 explicitly requires

```math
\limsup_{V\to\infty}v_{\mathcal B,V}^{\rm cap}<\infty.
```

That is the correct missing hypothesis. The manuscript does not pretend to prove a chemistry-independent universal velocity ceiling.

## 3.2 Moving-window low-energy theorem — PASS

Rev11 correctly requires all three ingredients:

```text
sup_{omega in B_m} hbar omega -> 0,
int_{B_m} sigma_cross d omega -> W0 > 0,
uniform capacity bound over both V and m.
```

Since

```math
K_T(E)=2k_BT-E/2+O(E^2/k_BT),
```

the convergence to `2 k_B T` is uniform on a window whose maximum energy tends to zero. Therefore the stated `liminf` lower bound follows.

This theorem is importantly not equivalent to saying that `E_g -> 0` alone forces finite carrier density. The integrated-weight and capacity hypotheses are indispensable and are stated explicitly.

### Minor notation observation

A maximally formal presentation could define the thermodynamic-limit active density for every `B_m` before writing the outer `liminf_m`. The present prose already specifies the order of limits well enough that this is not a correctness defect and does not justify another derivational rewrite.

---

# 4. Rev11 bulk ordinary-supremum repair

## 4.1 `sup`, not `ess sup` — PASS

The finite-system theorem uses an ordinary supremum over exact energy shells. Rev10 correctly repaired the HgCdTe specialization from an essential supremum to an ordinary supremum.

## 4.2 Complete energy shell versus one momentum block — PASS after Rev11

For a finite periodic normalization volume, the homogeneous one-body velocity operator conserves crystal momentum. If an exact energy value occurs at multiple momenta, the complete shell is a direct sum of those momentum sectors and

```math
P_\epsilon v_xQ_{\epsilon,\mathcal B}
=\bigoplus_{\mathbf k}
P_{\epsilon,\mathbf k}v_x(\mathbf k)Q_{\epsilon,\mathbf k,\mathcal B}.
```

The operator norm of a direct sum is the maximum block norm. The finite-volume maximum becomes the ordinary `k` supremum in the bulk limit. Rev11 therefore closes the earlier possible mismatch between Eq. (21) and Eq. (49).

This argument is specific to the translationally invariant validation model. The general theorem does not require momentum labels and remains formulated in exact eigenstates.

---

# 5. HgCdTe numerical validation

## 5.1 Hamiltonian implementation — internally consistent

The production script implements the bulk constant-parameter second-order 8-band Hamiltonian with

```text
T = 300 K
Eg = 0.123984198 eV
EP = 18.8 eV
bounded carrier domain |k| <= 2.0 nm^-1
```

and interpolated `Delta, F, gamma1, gamma2, gamma3, kappa`. The velocity operator is obtained from the analytic derivative

```math
v_x=(1/\hbar)\partial H/\partial k_x.
```

The 3-D integration measure includes

```math
k^2 dk d(cos theta) d phi /(2 pi)^3,
```

with the correct `nm^-3 -> cm^-3` conversion.

The charge-neutral chemical potential is solved before the theorem's exact cross-`mu` partition is constructed. Because `mu` lies above the nominal Gamma6 edge, the validation correctly uses the general Eq. (29), not the intrinsic-gap Eq. (30).

## 5.2 Gamma-point objection — correctly rejected

At the computed charge-neutral state,

```text
mu - E_Gamma6 ~= +11.477 meV.
```

Thus the nominal Gamma6 and Gamma8 states at `k=0` are all on the same side of `mu`; there is no selected cross-`mu` Gamma8→Gamma6 block exactly at Gamma. The selected set begins at finite momentum near

```text
|k| ~= 0.05535 nm^-1.
```

The earlier suggested isolated-Gamma capacity correction therefore does not apply to this state.

## 5.3 Controlling numerical values — consistent

The Rev11 controlling values are

```text
cross-mu reference population      1.005141e17 cm^-3
ordinary projected-block sup       ~1.01764e6 m/s
broad bound/reference              ~0.1175
headline rounded ratio             0.118 / 11.8%
broad lower bound                  ~1.18e16 cm^-3
active-support/reference           ~0.669
bound/active-support               ~0.176
ordinary pairwise sup              ~0.87165e6 m/s
pairwise substitution bias         ~+36.3%
selected broad-window k max        ~0.583 nm^-1
```

The decomposition

```math
\frac{n_{bound}}{n_{ref}}
=
\frac{n_{bound}}{n_{\mathcal B}^{act}}
\frac{n_{\mathcal B}^{act}}{n_{ref}}
```

is numerically consistent with the reported broad-window factors to rounding.

The fact that the pairwise maximum is materially below the full block singular value confirms that the projected-block construction is not decorative: substituting the simpler pairwise quantity would materially overstate the lower bound.

## 5.4 Numerical supremum status — acceptable, but not a certified mathematical maximum

The ordinary capacity supremum is obtained by a reproducible continuous global optimization (`scipy.optimize.differential_evolution`) over `(k,theta,phi)` with fixed seeds and polishing. The audit script explicitly states that this is a numerical supremum search, not interval arithmetic.

This is appropriate because the HgCdTe section is presented as a numerical model validation rather than part of the proof of Eq. (29). It would become a problem only if the manuscript claimed a rigorously certified material-specific constant.

A hostile numerical referee could still request one of the following:

```text
multi-seed/global-optimizer replication;
deterministic angular/radial bracketing around the maximizing branch;
interval/branch-and-bound certification of the ordinary supremum.
```

No such addition is required by the current claim level. If requested, multi-seed replication is the cheapest next check.

## 5.5 Parameter sensitivity — correctly limited

The one-at-a-time `+/-5%` remote-band perturbation scan gives a reduced-grid broad ratio range

```text
0.1098 ... 0.1293
```

around reduced-grid baseline `0.1226`. Rev11 correctly labels this only as an order-of-magnitude robustness diagnostic, not an experimental uncertainty propagation.

## 5.6 Significance of 11.8% — nonzero but editorially vulnerable

The realistic model does not approach the near-equality behavior of the symmetric parabolic family. The broad validation window recovers about `11.8%` of the reference population; the near-edge windows recover only about `3.2%`, `7.5%`, and `11.1%` as the window expands.

This is not a theorem defect. It does mean that the paper should continue to present the HgCdTe calculation as evidence that the inequality is quantitatively non-vacuous in a strongly asymmetric multiband system, not as a tight detector-design bound.

The `0.5 eV` upper edge is appropriately labeled a model-validation window rather than a detector operating bandwidth.

---

# 6. Scope regression check — PASS

Rev11 correctly refuses the following inferences:

```text
population -> universal dark current;
population -> universal thermal generation rate;
population -> universal D* limit;
occupation variance -> finite-bandwidth noise floor;
material conductivity -> arbitrary external absorptance without photonic resources.
```

It also excludes or separately conditions:

```text
neutral excitons / collective modes;
phonon-assisted indirect absorption;
interaction-generated many-body spectral functions;
unconstrained resonant or slow-light photonic enhancement;
experimental use of total measured conductivity without isolating sigma_cross.
```

These caveats are substantive and necessary. Removing them to make the paper sound broader would make the manuscript less defensible.

---

# 7. Literature collision audit

## 7.1 Onishi-Fu — correctly added, not a collision

Rev11 now cites Y. Onishi and L. Fu, Phys. Rev. X 14, 011052 (2024), which derives topology/quantum-geometry-conditioned optical bounds on an energy gap. This is neighboring optical-bound literature but does not state the Experiment-12 thermal quasiparticle population inequality.

## 7.2 Concrete omission: Mao–Mendez-Valderrama–Chowdhury, PRB 112, 075116 (2025)

A targeted final search identified a closer neighboring paper that is not in the Rev11 bibliography:

```text
D. Mao, J. F. Mendez-Valderrama, and D. Chowdhury,
"Low-energy optical absorption in correlated insulators:
Projected sum rules and the role of quantum geometry,"
Phys. Rev. B 112, 075116 (2025).
```

This paper is materially relevant because it develops a **partial/projected low-energy optical sum rule** rather than an all-frequency sum rule. It restricts the response to a low-energy Hilbert space and studies an inverse-frequency-weighted optical integral. Its finite-temperature discussion also introduces a thermally weighted projected optical sum related to quantum Fisher information.

This is the closest literature-completeness issue found in the final audit because Experiment 12 also emphasizes a selected low-energy window and a thermally weighted optical integral.

### Why it is not a direct collision

The objects and conclusions are different:

```text
Mao et al.:
    projected/interacting low-energy Hilbert space;
    inverse-frequency-weighted optical sum;
    quantum geometry / projected quantum weight / QFI target;
    many-body current contributions explicitly allowed.

Experiment 12:
    independent-quasiparticle direct cross-mu transition graph;
    kernel hbar*omega/[exp(hbar*omega/(2kBT))-1];
    exact endpoint Fermi population inequality;
    per-exact-shell projected velocity capacity + support rank;
    lower bound on equilibrium thermal one-body quasiparticle population.
```

The Mao et al. paper therefore does not reproduce Eq. (29), its Fermi lemma, or its shell-capacity state-count inference. It is nevertheless close enough in **windowed optical-sum methodology** that omitting it creates an avoidable referee vulnerability.

### Recommended manuscript amendment

Add one sentence/short paragraph in Sec. VI.B after the quantum-geometric sum-rule discussion, for example:

> Projected low-energy optical sum rules have also been developed for correlated insulators, including finite-temperature weighted forms connected to projected many-body quantum geometry and quantum Fisher information [Mao et al.]. Those results restrict optical response to a low-energy many-body Hilbert space and constrain geometric/fluctuation quantities. Equation (29) instead isolates direct cross-chemical-potential one-body transitions and combines its distinct Fermi thermal kernel with a per-shell velocity-capacity bound to constrain equilibrium quasiparticle population.

Then add the bibliographic entry.

This should be treated as a **literature-completeness amendment**, not a scientific Rev12 rewrite. No equation or numerical result needs to change.

---

# 8. Overall hostile disposition

A referee attempting to reject Rev11 on technical correctness would have to attack one of four points:

```text
1. the transition-level Fermi inequality;
2. the Kubo conversion;
3. the shell singular-value/rank population conversion;
4. the thermodynamic capacity hypothesis.
```

The first three survive direct re-derivation. The fourth is an explicit hypothesis rather than a hidden assertion and is microscopically realized in the first-order Kane example.

The HgCdTe numerical result is model-conditioned and numerically rather than interval-certified, but the manuscript says so. No numerical inconsistency was identified that changes the `~0.118` headline or the theorem.

The most credible remaining criticisms are therefore:

```text
A. significance: the realistic bound is only order 10^-1 and smaller near edge;
B. applicability: sigma_cross is not always directly separable from measured total conductivity;
C. scope: the theorem excludes important many-body/indirect/excitonic detector classes;
D. resource character: v_B^cap must be independently bounded/estimated for a material;
E. literature completeness: projected low-energy optical sum-rule work by Mao et al. should be cited.
```

A-D are already acknowledged limitations or editorial judgments. E is the only concrete pre-submission amendment identified by this audit.

## Final decision

```text
CENTRAL EQ. (29):                    PASS
POINTWISE FERMI LEMMA:              PASS
KUBO NORMALIZATION:                 PASS
SHELL CAPACITY/RANK STEP:           PASS
THERMODYNAMIC QUANTIFIERS:          PASS / EXPLICITLY CONDITIONAL
REV11 ORDINARY-SUP BULK REPAIR:     PASS
HGCDTE NUMERICAL CONSISTENCY:       PASS AT CLAIMED NUMERICAL LEVEL
DARK-CURRENT/D*/NOISE OVERCLAIM:    NONE FOUND
DIRECT PRIOR-ART COLLISION:         NOT FOUND IN TARGETED AUDIT
NEW LITERATURE-COMPLETENESS GAP:    YES — MAO ET AL. PRB 112, 075116 (2025)
SCIENTIFIC REV12 REQUIRED:          NO
PRE-SUBMISSION CITATION AMENDMENT:  YES
```

**Recommended next action:** make the single literature-positioning amendment, rebuild the Rev11 production source with that citation, run the same compile/hash/all-page QA, and then stop rewriting unless a new concrete defect is discovered.
