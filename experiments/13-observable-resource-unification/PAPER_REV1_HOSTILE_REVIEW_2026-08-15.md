# Experiment 13 — hostile review of unified manuscript Rev. 1

**Date:** 2026-08-15  
**Manuscript:** `PAPER_DRAFT_REV1_2026-08-15.md`  
**Disposition:** **NO CENTRAL ERROR / REV0 REGRESSIONS FIXED / REV1 SCIENTIFICALLY COHERENT / CENTRAL THEOREM NOW KNOWN TO BE UNNECESSARILY RESTRICTED / REV2 REQUIRED**

---

# 1. Executive verdict

Rev. 1 successfully repairs every blocking issue identified in the Rev. 0 hostile review:

```text
authoritative Kubo convention restored;
staged detector maps made explicit;
generic response selectivity separated from quantum-optimal rejection;
Experiment-01 hypotheses no longer conflated with equal-trace normalization;
cross-mu conductivity scope made explicit;
Poisson endpoint hypotheses listed;
finite-frequency Ramo visibility qualified as permitted rather than guaranteed.
```

No mathematical regression was found in the corrected Experiment-12 theorem, the shellwise decomposition, or the Ramo lineage argument.

A production-resolution HgCdTe rerun also now closes the decomposition:

```text
eta_F              = 0.30684
capacity tightness = 0.57262
observable product = 0.17570
max shell selectivity departure from unity ~= 4e-14.
```

Thus the realistic-material result is no longer merely a moderate-grid audit.

However, Rev. 1 should not be polished or typeset because a stronger central theorem has now been derived.

---

# 2. Principal revision trigger: the uniform-shell theorem is not the fundamental result

Rev. 1 presents

```math
A_max=S_resp=1/tau_count=d/r_st
```

under a uniform incoherent comparison and common shell occupation.

That statement is correct, but the restriction is unnecessary.

For arbitrary positive activity/population operator `X`, define

```math
rho_X=X/TrX,
```

```math
S_X
=lambda_max(G)/Tr(G rho_X),
```

and

```math
tau_X
=Tr(GX)/[lambda_max(G)TrX].
```

Then exactly

```math
\boxed{S_X tau_X=1.}
```

No uniform population, commutation, common shell occupation, or stable-rank assumption is required.

Stable rank is only the special case `X proportional I`.

This is a materially better manuscript spine.

---

# 3. Why the generalized theorem improves the Experiment-09 connection

For Experiment 09,

```math
G=|B><B|,
```

```math
X=rho_D=\sum_jw_j|j><j|.
```

Then

```math
Tr(GX)=\sum_jw_j^2,
```

and therefore

```math
\boxed{
S_X=1/\sum_jw_j^2=N_eff.
}
```

Thus the full nonuniform coherence dimension is recovered exactly from the activity-weighted theorem.

Rev. 1 currently needs to retreat to the uniform `N` case to make the stable-rank identity exact. Rev. 2 will not.

This is a substantial conceptual improvement.

---

# 4. Why the generalized theorem improves the Experiment-12 connection

Experiment 12 can be written on the direct sum of selected endpoint energy shells.

Define the block-diagonal endpoint Gram operator `G_B` from the upper-shell `A A^dagger` and lower-shell `B^dagger B` blocks. Then

```math
lambda_max(G_B)=(v_B^cap)^2.
```

Let `X_B` contain the actual Fermi electron/hole occupations on the selected active endpoint supports. Then

```math
Tr(G_BX_B)/V=R_B,
```

```math
TrX_B/V=n_B^act.
```

Therefore

```math
\boxed{
S_{th,B}^{act}
=\frac{(v_B^cap)^2 n_B^act}{R_B}
=1/tau_cap^{act}.
}
```

This relation is **global and exact**, including nonuniform thermal occupations and shell-to-shell capacity variation.

The shellwise decomposition

```math
tau_cap^{act}
=\sum_aw_a^{act}c_a/S_a^{act}
```

then becomes a diagnostic of *why* the global thermal ensemble has `S_th>1`, not the first place where reciprocity is rescued.

For production HgCdTe,

```text
tau_cap^act = 0.57262
```

so

```text
S_th,B^act ~= 1.746.
```

The shellwise audit simultaneously shows `S_a^act=1`. Hence the global selectivity comes from shell-to-global capacity variation, not within-shell singular anisotropy.

This is a clearer physical story than Rev. 1 currently presents.

---

# 5. Experiment-01 connection remains a special case, not a forced identification

For a uniform task ensemble `X=I_d`, the activity-weighted theorem reduces to

```math
S_X=d/r_st.
```

This is the equal-trace task-selectivity result already used in Rev. 1.

The physical unknown-arrival paper remains a separate witness under its own normalization. No change is required to that boundary.

The guaranteed task-penalty inequality remains valid and useful in Rev. 2.

---

# 6. Experiment-03 connection remains through the null endpoint

If

```math
Tr(GX)=0,
```

then positive activity `X` is invisible to the map and

```math
tau_X=0.
```

The formal selectivity is infinite relative to that hidden ensemble.

This gives a static null-space endpoint that is structurally consistent with the endpoint-counting recycling result. Finite-frequency Ramo motion changes the readout map and can lift the relevant null.

Do not overstate this as a derivation of the full stochastic lineage theorem from `S_X tau_X=1`; the Poisson/Ramo result remains an independent downstream theorem.

---

# 7. Production HgCdTe gate now passes

The production-scale stable-rank QA uses

```text
nr=160,
nmu=10,
nphi=16,
```

and reproduces

```text
mu = 0.1354615106 eV
cross-mu reference population = 1.005140525e17 cm^-3
R_B = 3.987420232e28 cm^-3 (m/s)^2
L_B = 1.223486457e28 cm^-3 (m/s)^2
n_active = 6.724111444e16 cm^-3.
```

With the controlling continuous ordinary supremum

```text
v_B^cap = 1.01764e6 m/s,
```

```text
tau_cap^act = 0.572622972
tau_obs^act = 0.175701685
eta_F       = 0.306836598.
```

And

```text
min S_a^act = 1
max S_a^act = 1 + 3.8e-14.
```

The material-validation gate therefore passes at the resolution relevant to the existing PRB calculation.

---

# 8. Fresh Ramo/photon-recycling prior-art screen

The deeper search continues to find:

```text
classical Ramo/corpuscular treatment of p-n junction GR noise;
proper coupling of carrier motion to terminal current;
HgCdTe photon recycling effects on lifetime/performance;
HgCdTe photon reabsorption and deterministic optical crosstalk.
```

The searched sources do not state the combined conservative-lineage result

```text
one-final-sink Poisson readout -> exact zero interpixel cross-spectrum
while
finite-transit internally recombining Ramo segments -> zero DC area but possible AC multichannel support.
```

This remains a plausible detector-specific novelty, not a certified priority claim.

---

# 9. Remaining weaknesses before Rev2

## A. The central identity remains elementary algebra

Even in its activity-weighted form,

```math
S_X tau_X=1
```

is a normalized spectral-capacity identity. It should not be presented as surprising mathematics.

The manuscript must make its scientific contribution depend on the **independent physical realizations**:

```text
N_eff quantum rejection;
thermal Kubo population theorem;
HgCdTe factor decomposition;
Ramo recycling observability.
```

## B. The word "selectivity" needs stage labels

Use terminology such as

```text
activity-weighted response selectivity;
quantum bright-state rejection;
global thermal capacity selectivity;
task response anisotropy.
```

Do not imply they are operationally identical experiments.

## C. Full reference network remains incomplete

Rev. 1's working bibliography is not journal ready. This remains a production blocker, not a theory blocker.

---

# 10. Referee disposition

```text
REV0 REPAIR:                         PASS
REV1 INTERNAL CORRECTNESS:           PASS
EXPERIMENT-12 NORMALIZATION:         PASS
PRODUCTION HgCdTe DECOMPOSITION:     PASS
RAMO/POISSON RESULT:                 PASS mathematically
CENTRAL UNIFORM-SHELL FORMULATION:   CORRECT BUT SUPERSEDED
ACTIVITY-WEIGHTED GENERALIZATION:    ADOPT AS NEW SPINE
FLAGSHIP UNITY:                      STRENGTHENED
REV2:                                REQUIRED
TYPESETTING/SUBMISSION:              PREMATURE
STANDALONE PAPER WITHDRAWAL:         NOT AUTHORIZED
```

## Rev. 2 action

Rebuild the paper around

```math
\boxed{S_X tau_X=1}
```

as the general forward-selectivity / inverse-certification reciprocity.

Then present, in order:

```text
uniform task/stable-rank special case;
Experiment-09 nonuniform N_eff exact specialization;
Experiment-12 direct-sum thermal specialization;
shellwise decomposition and production HgCdTe closure;
Poisson-lineage / finite-transit Ramo observability theorem.
```

This should reduce caveats and make the unity stronger rather than broader.
