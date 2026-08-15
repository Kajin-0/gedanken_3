# Experiment 13 — activity-weighted selectivity / resource reciprocity

**Date:** 2026-08-15  
**Scope:** arbitrary positive activity/population operator; exact finite-dimensional statement, with direct-sum extension to finite-volume energy shells  
**Status:** **STRONGER CENTRAL THEOREM / REMOVES UNIFORM-ENSEMBLE RESTRICTION / EXACTLY RECOVERS NONUNIFORM EXPERIMENT-09 `N_eff` AND GLOBAL EXPERIMENT-12 CAPACITY TIGHTNESS**

## 1. Motivation

The first Experiment-13 reciprocity was written for a uniform incoherent comparison state `I/d` and a common shell occupation `p`:

```math
S_{resp}\tau_{count}=1.
```

That form is useful but unnecessarily restrictive.

The actual algebra depends only on a positive activity/population operator `X`. Normalizing `X` produces the ensemble against which the brightest direction is compared. The same average response then appears in the capacity lower bound.

This removes the artificial uniform-state restriction and directly connects:

```text
Experiment 09:
    arbitrary population-matched incoherent dark weights w_j;

Experiment 12:
    nonuniform thermal occupations across exact energy shells;

Experiment 01:
    the uniform task ensemble as one special comparator;

Experiment 03:
    positive innovation/activity covariances after choosing the relevant readout map.
```

---

# 2. Theorem

Let

```math
G\succeq0
```

be a nonzero bounded positive coupling/effect operator on a finite-dimensional space, with

```math
\lambda_+=\lambda_{max}(G)>0.
```

Let

```math
X\succeq0,
\qquad
N_X=TrX>0
```

be any positive activity, population, covariance, or ensemble-weight operator.

Define its normalized ensemble

```math
\boxed{
\rho_X=X/N_X.
}
```

The ensemble-average coupling per unit activity is

```math
\bar q_X
=Tr(G\rho_X)
=\frac{Tr(GX)}{TrX}.
```

The largest response available to a normalized pure direction is `lambda_+`. Define the **activity-weighted selectivity**

```math
\boxed{
\mathcal S_X
=\frac{\lambda_+}{\bar q_X}
=\frac{\lambda_+TrX}{Tr(GX)},
}
```

provided `Tr(GX)>0`.

Now use the spectral-capacity inequality

```math
Tr(GX)\le\lambda_+TrX.
```

The corresponding lower estimate of total activity is

```math
\boxed{
N_{cap}
=\frac{Tr(GX)}{\lambda_+}.
}
```

Define its tightness relative to the true activity

```math
\boxed{
\tau_X
=\frac{N_{cap}}{N_X}
=\frac{Tr(GX)}{\lambda_+TrX}.
}
```

Therefore exactly

```math
\boxed{
\mathcal S_X\tau_X=1.
}
```

Equivalently,

```math
\boxed{
\mathcal S_X=1/\tau_X.
}
```

If `Tr(GX)=0`, the activity lies entirely in the null space of `G`; then `tau_X=0` and the selectivity ratio is formally infinite. This is the complete-invisibility endpoint.

---

# 3. Interpretation

The theorem is algebraically a normalized form of the upper spectral bound. Its detector content comes from assigning two independently meaningful questions to the same physical coupling map:

```text
forward/selective question:
    how much more strongly can the map respond to its brightest direction
    than to the actual internal activity ensemble X/TrX?

inverse/resource question:
    what fraction of the true total activity TrX is certified if the observed
    response Tr(GX) is inverted using only the largest allowed per-direction
    coupling lambda_+?
```

The answers are exact reciprocals.

The theorem does not require:

```text
uniform populations;
commutation of X and G;
a diagonal X in the eigenbasis of G;
a rank-one G;
equal energy levels;
a fixed trace of G.
```

It requires only positivity and a finite upper spectral edge on the relevant subspace.

---

# 4. Uniform-shell stable-rank theorem as a corollary

If

```math
X=pI_d,
```

then

```math
rho_X=I_d/d
```

and

```math
Tr(GX)=pTrG.
```

Hence

```math
\mathcal S_X
=\frac{d\lambda_+}{TrG}
=\frac{d}{r_{st}},
```

and

```math
\tau_X
=\frac{r_{st}}d.
```

Thus the earlier result

```math
\boxed{
\mathcal S_{resp}\tau_{count}=1
}
```

is the maximally mixed special case of the activity-weighted theorem.

The stable rank is therefore not the fundamental object in the fully weighted problem; it is the uniform-ensemble specialization of the more general response-average ratio.

---

# 5. Experiment 09: exact recovery of nonuniform `N_eff`

Experiment 09 has

```math
G=\Pi_B=|B><B|,
```

so

```math
\lambda_+=1.
```

The population-matched incoherent dark state is

```math
X=\rho_D
=\sum_jw_j|j><j|,
```

with

```math
TrX=1.
```

Because

```math
Tr(GX)
=<B|rho_D|B>
=\sum_jw_j^2,
```

we obtain

```math
\boxed{
\tau_X=\sum_jw_j^2,
}
```

and therefore

```math
\boxed{
\mathcal S_X
=\frac1{\sum_jw_j^2}
=N_{eff}.
}
```

Thus the general Experiment-09 coherence dimension is **exactly** the activity-weighted selectivity of the same positive operator.

In this particular rank-one projector construction, `S_X` is more than a generic response ratio. Experiment 09 independently proves that the bright projector is the minimum-dark-acceptance yes/no measurement among all measurements with unit acceptance of `|B>`. Hence the physical conditional rejection factor equals the activity-weighted selectivity.

The uniform case `w_j=1/N` gives `S_X=N` as before.

---

# 6. Experiment 12: global thermal ensemble

The Experiment-12 thermally weighted velocity strength can be written as one positive pairing on a direct sum of selected endpoint energy shells.

For every selected upper endpoint shell define

```math
G_{\epsilon_c}^{+}
=A_{\epsilon_c,B}A_{\epsilon_c,B}^\dagger
```

on the upper eigenspace. For every selected lower endpoint shell define

```math
G_{\epsilon_v}^{-}
=B_{\epsilon_v,B}^\dagger B_{\epsilon_v,B}
```

on the lower eigenspace.

Form the direct-sum operator

```math
\boxed{
G_B
=\bigoplus_{\epsilon_c>\mu}G_{\epsilon_c}^{+}
\oplus
\bigoplus_{\epsilon_v<\mu}G_{\epsilon_v}^{-}.
}
```

Its largest eigenvalue is precisely the basis-invariant selected-shell capacity:

```math
\boxed{
\lambda_{max}(G_B)
=(v_B^{cap})^2.
}
```

Now define the thermal endpoint activity operator

```math
X_B
=\bigoplus_{\epsilon_c>\mu}
f(\epsilon_c)P_{\epsilon_c}^{sel}
\oplus
\bigoplus_{\epsilon_v<\mu}
[1-f(\epsilon_v)]P_{\epsilon_v}^{sel},
```

where `P^{sel}` is either the full selected parent-shell projector or, for the active theorem, the projector onto the support of the corresponding optical Gram block.

For the active choice,

```math
\frac1VTrX_B
=n_{e,B}^{act}+n_{h,B}^{act}.
```

And exactly

```math
\boxed{
\frac1VTr(G_BX_B)
=\mathcal R_B.
}
```

Therefore the activity-weighted thermal selectivity is

```math
\boxed{
\mathcal S_{th,B}^{act}
=
\frac{(v_B^{cap})^2
(n_{e,B}^{act}+n_{h,B}^{act})}
{\mathcal R_B}.
}
```

The capacity-step active-population tightness is

```math
\boxed{
\tau_{cap}^{act}
=\frac{\mathcal R_B}
{(v_B^{cap})^2
(n_{e,B}^{act}+n_{h,B}^{act})}.
}
```

Hence

```math
\boxed{
\mathcal S_{th,B}^{act}
\tau_{cap}^{act}=1.
}
```

This is the exact global Experiment-12 counterpart of the Experiment-09 `N_eff` identity. It already includes nonuniform Fermi occupations and shell-to-shell capacity variation.

---

# 7. Add the observable Fermi/Kubo step

Experiment 12 does not observe `R_B` directly. It proves the lower functional

```math
\mathcal L_B\le\mathcal R_B.
```

Define

```math
\eta_F=\mathcal L_B/\mathcal R_B.
```

The observable population-bound tightness is

```math
\tau_{obs}^{act}
=\frac{\mathcal L_B}
{(v_B^{cap})^2 n_B^{act}}
=\eta_F\tau_{cap}^{act}.
```

Therefore

```math
\boxed{
\mathcal S_{th,B}^{act}
\tau_{obs}^{act}
=\eta_F.
}
```

The thermal statistical asymmetry is thus cleanly separated from the spectral-capacity reciprocity.

For the current production HgCdTe audit,

```text
tau_cap^act ~= 0.5726
```

so the corresponding global thermal-ensemble selectivity is

```math
\boxed{
\mathcal S_{th,B}^{act}
\approx1/0.5726
\approx1.746.
}
```

This global selectivity does **not** come from unequal singular values inside each active exact shell; the shellwise audit finds `S_a^act=1`. It arises because the globally maximizing shell capacity is larger than the thermally weighted average capacity over the actual active ensemble.

This distinction is physically important.

---

# 8. Relation to the shellwise decomposition

The global identity

```math
S_{th,B}^{act}=1/tau_{cap}^{act}
```

is compact but does not explain **why** the average response lies below the global capacity.

The shellwise theorem resolves it:

```math
\boxed{
\tau_{cap}^{act}
=\sum_aw_a^{act}
\frac{c_a}{S_a^{act}}.
}
```

Therefore

```math
\boxed{
\mathcal S_{th,B}^{act}
=
\left[
\sum_aw_a^{act}
\frac{c_a}{S_a^{act}}
\right]^{-1}.
}
```

The global activity-weighted selectivity can arise from either:

```text
within-shell singular-spectrum concentration (S_a>1),
```

or

```text
shell-to-global capacity variation (c_a<1),
```

or both.

The realistic HgCdTe model is the second case.

---

# 9. Experiment 01 as the uniform task-ensemble special case

For a task information operator `G_task`, choose the uniform task ensemble

```math
X=I_d.
```

Then

```math
S_X=d/r_st
```

is exactly the maximum task response relative to the isotropic ensemble-average response.

If a second detector has the same trace but a different operator, trace-zero indefiniteness guarantees task-order reversal somewhere.

The physical Experiment-01 unknown-arrival theorem is more specific and uses a different normalization — equal eventual event-specific matched-filter SNR for one waveform. The present theorem supplies a spectral comparison principle; it does not retroactively change Experiment 01's hypotheses.

---

# 10. Null-space / hidden-activity endpoint

If

```math
Tr(GX)=0
```

with `X>=0`, positivity implies that the support of `X` lies in the null space of `G` (up to zero-weight components).

Then

```math
\tau_X=0.
```

No finite inversion of the measured response can certify the hidden activity.

This is the static positive-operator analogue of the Experiment-03 endpoint-counting situation: internal activity can exist while the chosen readout map assigns it no support in a measured terminal channel.

Finite-transit Ramo motion modifies the readout map and can lift such a null at finite frequency.

---

# 11. Why this theorem is a better manuscript spine

The previous manuscript architecture required a caveat every time the simple stable-rank relation was used because it assumed a uniform comparison ensemble.

The activity-weighted theorem gives one exact statement for the actual ensemble:

```math
\boxed{
\text{brightest available response relative to actual ensemble average}
=
\frac{1}{\text{fraction of total activity certified by a max-capacity inversion}}.
}
```

Special cases then become:

```text
uniform task ensemble -> stable-rank task selectivity;
Experiment-09 rho_D   -> N_eff exactly;
Experiment-12 X_th    -> global thermal capacity tightness exactly;
null ensemble         -> complete hidden activity.
```

This is the strongest current candidate for the central Experiment-13 theorem.

---

# 12. Novelty boundary

The algebraic identity is a normalized spectral inequality and should not be claimed as new mathematics.

The candidate detector contribution is the physically explicit identification that the same positive pairing answers two independently posed questions — forward selectivity and inverse resource certification — and that this relation maps exactly onto the nonuniform coherence dimension of Experiment 09 and the global thermal population-capacity tightness of Experiment 12.

The shellwise HgCdTe decomposition and the recycling/Ramo theorem remain the nontrivial physical consequences that prevent the unified paper from reducing to a normalization identity.

---

# 13. Manuscript action

Rev. 2 of the unified manuscript should replace the uniform-shell stable-rank equality as the primary theorem with the activity-weighted statement

```math
S_X tau_X=1.
```

Stable rank should be introduced as the maximally mixed special case, not as the fundamental definition.

This will:

```text
remove the nonuniform Experiment-09 caveat from the main theorem;
make the Experiment-12 global thermal ensemble connection exact before shell decomposition;
clarify that the shell decomposition diagnoses the origin of global selectivity;
reduce the appearance that the flagship theorem is built around a specially chosen uniform ensemble.
```
