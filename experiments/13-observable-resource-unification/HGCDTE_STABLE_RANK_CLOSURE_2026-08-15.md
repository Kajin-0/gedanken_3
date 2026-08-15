# Experiment 13 — eight-band HgCdTe stable-rank closure

**Date:** 2026-08-15  
**Scope:** numerical validation of the Experiment-13 dispersive decomposition using the Experiment-12 second-order eight-band Kane model  
**Status:** **CLOSURE PASSED / REALISTIC MATERIAL VALIDATION OBTAINED / COHERENCE-SELECTIVITY FACTOR IS UNITY IN THIS MODEL**

## 1. Question

The dispersive Experiment-13 theorem predicts that the capacity-step tightness of the Experiment-12 active-population bound decomposes as

```math
\tau_{cap}^{act}
=\sum_a w_a^{act}
\frac{c_a}{\mathcal S_a^{act}},
```

with

```math
c_a=\lambda_a/u_B^2,
```

```math
\mathcal S_a^{act}=r_a/r_{st,a}.
```

The full observable theorem should then satisfy

```math
\tau_{obs}^{act}
=\eta_F\tau_{cap}^{act}.
```

This note tests those identities in the realistic HgCdTe validation model already used by Experiment 12.

---

## 2. Numerical implementation

A companion audit script was added at

```text
experiments/13-observable-resource-unification/numerics/
hgcdte_selectivity_capacity_decomposition.py
```

It dynamically loads the authoritative Experiment-12 implementation

```text
experiments/12-oscillator-strength-state-count-bound/numerics/
kane_8band_tightness.py
```

and does not reimplement the Kane Hamiltonian.

For every selected exact-energy cluster at every quadrature point, the audit records:

```text
largest singular value squared lambda_a;
Frobenius norm squared Tr(G_a);
numerical rank r_a;
stable rank r_st,a;
local selectivity S_a^act=r_a/r_st,a;
thermal active-population weight;
capacity utilization c_a.
```

The broad validation window is

```text
Eg <= Delta E <= 0.5 eV.
```

A moderately refined audit used

```text
nr=100,
nmu=10,
nphi=16,
kmax=1.0 nm^-1,
```

with the chemical potential independently obtained from the Experiment-12 carrier-state model.

---

# 3. Direct numerical result

The audit gives approximately

```text
mu                         = 0.13538234 eV
R_exact                    = 3.97799e28 cm^-3 (m/s)^2
L_observable               = 1.22324e28 cm^-3 (m/s)^2
eta_F = L/R                = 0.307502
N_active                   = 6.72443e16 cm^-3
sampled v_cap              = 1.01388e6 m/s
```

Using the sampled grid capacity gives

```text
tau_capacity               = 0.575485
tau_observable             = 0.176963
```

and the independently reconstructed shell decomposition gives

```text
sum_a w_a c_a/S_a          = 0.575485
```

to numerical precision.

Thus the dispersive identity closes directly:

```math
\boxed{
\tau_{cap}^{act}
=\sum_a w_a^{act}c_a/\mathcal S_a^{act}
}
```

with no residual numerical discrepancy beyond floating-point/quadrature precision.

The observable closure also holds:

```text
eta_F * tau_capacity
= 0.307502 * 0.575485
= 0.176963,
```

matching the directly evaluated observable bound/active-population ratio.

---

# 4. Use the separately validated ordinary supremum

Experiment 12's production result does not use the sampled capacity as the final theorem resource. Its separate continuous search gives approximately

```text
v_B^cap = 1.01764e6 m/s.
```

Keeping the same shell integrals but substituting that production capacity gives

```text
tau_capacity,production    ~= 0.571242
tau_observable,production  ~= 0.175658
```

with

```text
eta_F * tau_capacity,production
~= 0.175658.
```

This is consistent with the controlling Experiment-12 statement that the broad-window bound captures roughly `17.6%` of the optically active thermal population.

The small difference from the sampled-capacity result is exactly the expected ordinary-supremum correction, not a failure of the decomposition.

---

# 5. Unexpected but important result: no shellwise coherence-selectivity penalty

For every thermally weighted selected exact-shell block in this audit,

```math
\boxed{
\mathcal S_a^{act}
=1
}
```

to numerical precision.

Equivalently,

```math
r_{st,a}=r_a
```

for all contributing active shell blocks.

The observed numerical range was indistinguishable from unity at floating-point scale.

Therefore, in this particular second-order eight-band HgCdTe model,

```text
singular-spectrum anisotropy / coherence concentration
```

contributes essentially **no** looseness to the active-population theorem.

The capacity-step loss is instead caused by shell-to-shell variation in how closely each block approaches the **global** capacity `u_B`.

Because `S_a=1`,

```math
\tau_{cap}^{act}
=\sum_a w_a^{act}c_a
\approx0.571
```

when the production capacity is used.

The independent Fermi/Kubo factor is then

```math
\eta_F\approx0.308.
```

Their product gives

```math
\boxed{
0.571\times0.308\approx0.176,
}
```

which explains essentially the entire broad-window active-population tightness.

---

# 6. Physical interpretation

This is a useful falsification of an overly convenient narrative.

The Experiment-13 theory does **not** say that every material exhibiting the Experiment-12 population bound must also exhibit Experiment-09-style coherence selectivity.

Instead it identifies coherence selectivity as one possible singular-spectrum contribution to bound slack. The realistic HgCdTe model says that contribution is absent here.

For this HgCdTe case, the hierarchy is:

```text
local selected shell:
    nonzero singular channels are effectively isotropic;
    S_a^act = 1;

across shells:
    their absolute capacities vary substantially;
    weighted global capacity utilization ~= 0.57;

thermal occupation / optical kernel:
    Fermi/Kubo efficiency ~= 0.308;

final bound/active population:
    ~= 0.176.
```

Thus Experiments 09 and 12 are connected by the same theorem without being forced to exhibit the same physical regime.

Experiment 09 deliberately engineers the opposite singular-spectrum extreme: oscillator strength is concentrated into a coherent bright direction against a large incoherent parent space.

---

# 7. Relation to total versus active population

The audit finds

```text
N_parent_selected ~= N_active
```

for the selected HgCdTe exact-shell blocks at this numerical resolution.

That is consistent with the contributing selected shell blocks having no exact internal kernel after the Experiment-12 rank construction is applied.

This statement concerns only the **selected endpoint shells** in the broad optical window. It is not the same as saying every thermally occupied state in the full eight-band model participates in the window; the earlier Experiment-12 active/reference ratio remains below unity.

---

# 8. Robustness checks already implicit

A coarser independent audit (`nr=80,nmu=8,nphi=12`) gave the same qualitative decomposition:

```text
eta_F                  ~= 0.3081
tau_capacity(sampled)  ~= 0.5772
tau_observable         ~= 0.1778
S_a^act                = 1 to numerical precision.
```

Thus the stable-rank conclusion is not created by the modest quadrature refinement from the first audit to the second.

Production-quality publication numbers should still be generated by the repository script using the same convergence discipline as Experiment 12.

---

# 9. Scientific consequence for the unified paper

This validation materially strengthens Experiment 13 for two reasons.

First, the stable-rank/selectivity theorem is now connected to the realistic material example rather than only to flat-manifold constructions.

Second, the realistic example does **not** trivially mimic the coherence-selective Gedanken detector. It lands at a different endpoint of the same decomposition and thereby demonstrates that the framework distinguishes physical mechanisms rather than merely relabeling them.

A useful unified-paper figure could eventually show three singular-spectrum regimes:

```text
Experiment 09 bright selector:
    strong full-parent coherence selectivity;

Experiment 12 ideal equality family:
    isotropic shell coupling + uniform capacity -> exact state-count closure;

realistic HgCdTe:
    locally isotropic shell coupling but nonuniform shell capacity
    + substantial Fermi asymmetry -> ~17.6% active-population closure.
```

Do not produce such a figure until the prior-art audit and manuscript authorization are complete.

---

# 10. Disposition

```text
exact dispersive decomposition:             PASS
independent numerical reconstruction:       PASS
HgCdTe active-shell selectivity factor:      unity within numerical precision
shell-capacity contribution:                 ~0.57
Fermi/Kubo contribution:                     ~0.308
combined active-bound tightness:             ~0.176
realistic-material validation:               PASS
```

## NEXT ACTION

Complete the focused prior-art kill test for the **reciprocal selectivity/state-count theorem**, then reassess whether Experiment 13 now has enough genuinely new cross-branch content to authorize a manuscript architecture.
