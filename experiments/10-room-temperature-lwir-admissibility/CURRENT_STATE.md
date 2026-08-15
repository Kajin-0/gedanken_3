# Current State — Experiment 10: Room-Temperature LWIR Material Admissibility

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** **CONDITIONAL ELECTRONIC THEOREM PACKAGE + RESONANT OPTICAL RESPONSE EXTENSION DERIVED / FINITE RESPONSE ALONE DOES NOT RESTORE UNIVERSAL CARRIER-COLUMN FLOOR / PHOTONIC PARTICIPATION RESOURCE NOW REQUIRED / NOVELTY NOT ESTABLISHED / NO MANUSCRIPT YET**

## Fixed target

```math
T=300\ \mathrm K,
\qquad
\lambda_c=10\ \mu\mathrm m,
\qquad
E_g=0.1239841984\ \mathrm{eV},
\qquad
E_g/(k_BT)\approx4.796.
```

## Read first

1. `RESONANT_PATH_ENHANCEMENT_RESPONSE_BOUND_STEP_2026-08-14.md`
2. `THEOREM_CORE_2026-08-14.md`
3. `JOINT_ADMISSIBILITY_NOVELTY_AUDIT_2026-08-14.md`
4. `GENERAL_SPECTATOR_BAND_ADMISSIBILITY_THEOREM_STEP_2026-08-14.md`
5. `HEAVY_HOLE_AUGER_RATE_AND_JOINT_BOUND_STEP_2026-08-14.md`
6. `RADIATIVE_BOUNDARY_ADMISSIBILITY_STEP_2026-08-14.md`
7. earlier derivations as needed.

---

# A. Active-pair material scaling

For the finite-gap 3-D massive-Dirac active pair,

```math
n_c\propto v^{-3},
\qquad
\alpha_D\propto v^{-1}.
```

For a controlled single-pass active-pair optical depth,

```math
\boxed{\Sigma_c=C/v^2}
```

in the two-band neutral model.

Adding thermally accessible spectator **hole** bands shifts intrinsic `mu>0`, increases active electron density and weakens active interband absorption. Therefore the rigorous multiband statement is

```math
\boxed{\Sigma_c\ge C/v^2}
```

for the same required active-pair single-pass optical depth.

For the standard 90%-absorption witness (`r=1.2`, `n_b=3.5`),

```math
C=1.06668\times10^{29}\ \mathrm{m^{-2}(m/s)^2}.
```

---

# B. Electronic velocity ceilings

## Microscopic lattice resource

```math
\boxed{v\le V_{hop}.}
```

## General spectator-band Auger closure

For a positive isotropic convex spectator-hole excitation `E_s(p)`, define

```math
\boxed{
 v_s^{crit}=\inf_{p>0}\frac{E_s(p)}{p}.
}
```

Exact finite-energy normal-momentum spectator-assisted CCCH closure is equivalent to

```math
\boxed{v\le v_s^{crit}.}
```

For multiple spectators,

```math
\boxed{v_{spec}=\min_s v_s^{crit}.}
```

The construction is mathematically Landau-like and uses classical equal-group-velocity impact-ionization threshold physics. It is not a novelty claim.

For a parabolic heavy-hole spectator,

```math
E_{hh}(p)=\Delta+\delta_{hh}+p^2/(2M_{hh}),
```

```math
\boxed{M_{hh}v^2\le2(\Delta+\delta_{hh}).}
```

---

# C. Strongest current single-pass electronic theorem

Define

```math
\boxed{v_{adm}=\min(V_{hop},v_{spec}).}
```

Under the controlled single-pass, active-pair-optically-dominant hypotheses and exact normal-momentum spectator-assisted Auger closure,

```math
\boxed{
\Sigma_c
\ge
\frac{C}{v_{adm}^2}
=
\max\!\left[
C/V_{hop}^2,
\max_s C/(v_s^{crit})^2
\right].
}
```

Parabolic heavy-hole corollary:

```math
\boxed{
\Sigma_c
\ge
\max\!\left[
C/V_{hop}^2,
C M_{hh}/(2(\Delta+\delta_{hh}))
\right].
}
```

This is mathematically defensible under the stated hypotheses, but novelty is not established.

---

# D. Auger/radiative supporting results

Exact particle-hole-symmetric massive-Dirac `eeh/hhe` direct Auger is kinematically closed.

Scalar particle-hole asymmetry reopens it with weak-asymmetry threshold

```math
\boxed{K_{th}\sim E_g\mathcal A_m^{-1/3}.}
```

Interior threshold phase space scales as

```math
\Phi\propto(K-K_{th})^2,
```

with possible extra microscopic overlap powers.

For an open parabolic heavy-hole CCCH channel, the local threshold shell is also quadratic. The flat-heavy-hole limit has finite normalized local threshold phase space; the heavy band primarily collapses the activation threshold rather than creating a universal `M_hh^(3/2)` threshold-DOS divergence.

For complete external optical-boundary matching, external absorption/emission at equilibrium is fixed by Kirchhoff/detailed balance:

```math
\Phi_{abs}^{ext}=\Phi_{em}^{ext}=\Phi_0.
```

At the ideal 10-um/300-K hemispherical step benchmark:

```text
Phi_0 = 4.89777e17 cm^-2 s^-1
q Phi_0 = 0.0784710 A/cm^2
```

Internal radiative recombination is not the invariant denominator because photon recycling changes internal event count.

---

# E. Optical loophole — one-port resonator result

Controlling file:

`RESONANT_PATH_ENHANCEMENT_RESPONSE_BOUND_STEP_2026-08-14.md`

For one-port TCMT,

```math
A(\omega)
=\frac{4\gamma_e\gamma_i}
{(\omega-\omega_0)^2+(\gamma_e+\gamma_i)^2}.
```

Define cavity field-envelope response time

```math
\boxed{\tau_{opt}=1/(\gamma_e+\gamma_i).}
```

For target resonant absorptance `A_0`, the over-coupled branch minimizes required internal loss at a given response time. Define

```math
\boxed{g(A_0)=1-\sqrt{1-A_0}.}
```

Then

```math
\boxed{
2\gamma_i
\ge
\frac{g(A_0)}{\tau_{max}}
}
```

for `tau_opt <= tau_max`.

Define the electromagnetic absorber sampling-rate resource

```math
\boxed{
\Lambda_a
=\frac{2\gamma_i}{\alpha_D d}
=\frac{P_{abs}}{\alpha_Dd\,U}.
}
```

Then

```math
\boxed{
\alpha_Dd
\ge
\frac{g(A_0)}{\Lambda_a\tau_{max}}.
}
```

Let

```math
\frac{n_c}{\alpha_D}\ge\frac{B}{v^2},
```

with `C=zeta B` for the earlier single-pass coefficient. Combining with the electronic ceiling gives

```math
\boxed{
\Sigma_c
\ge
\frac{B}{v_{adm}^2}
\frac{g(A_0)}{\Lambda_a\tau_{max}}.
}
```

This is the resonant-response extension of the electronic theorem.

---

# F. Decisive new no-go

TCMT does **not** supply a universal upper bound on `Lambda_a`.

Therefore

```math
\boxed{
\text{finite temporal response alone does not restore a universal physical carrier-column lower bound.}
}
```

A universal bound requires an additional electromagnetic resource such as

```text
maximum modal energy concentration / absorber participation;
material susceptibility;
minimum resonator size;
accepted optical bandwidth;
number/density of resonances;
passive thickness-bandwidth / matching constraints.
```

For a simple cavity/ring with effective path length `L` and energy velocity `v_E`,

```math
\Lambda_a\simeq v_E/L,
```

so

```math
\boxed{
\Sigma_c
\gtrsim
\frac{B}{v_{adm}^2}
g(A_0)\frac{L}{v_E\tau_{max}}.
}
```

Path enhancement is directly paid for by optical dwell time in this restricted architecture.

At 10 um, `L=lambda/n`, `v_E=c/n`, and `A_0=0.90`, a 1-ps optical-response requirement permits a resonant column floor about `0.0099x` the original 90%-absorbing single-pass bound—roughly a `100x` escape in this simple model.

Reproducible check:

`numerics/resonant_path_response_bound.py`.

---

# G. Prior-art boundary

Established and not novelty:

```text
critical coupling and TCMT linewidth/lifetime relations;
resonant-cavity-enhanced photodetectors used to improve efficiency-bandwidth tradeoffs;
passive absorber thickness-bandwidth tradeoffs including Rozanov-type bounds;
alpha/G_th detector optimization;
Landau-like min[E/p] critical-velocity structure;
multiband Auger engineering;
radiative detailed balance and photon recycling.
```

The focused audit has not established novelty for the composed detector theorem.

---

# Hard limitations

1. **Optically active spectators:** unbounded spectator optical strength destroys the active-pair physical-thickness bound.
2. **Photonic enhancement:** finite response alone leaves the new resource `Lambda_a`; without bounding it, physical carrier column can still tend to zero in the reduced theory.
3. **Exact Auger closure:** sufficient, not necessary, for radiative/background-limited operation.
4. **Assisted channels:** not covered by the exact normal-momentum theorem.

---

# NEXT ACTION

Do not add more electronic mechanisms or another cavity example.

Audit and, only where necessary, derive bounds on `Lambda_a` from established passive-electromagnetic theory:

```text
Rozanov-type absorption thickness-bandwidth sum rules;
Bode-Fano matching limits;
delay-bandwidth limits;
material-susceptibility / field-concentration bounds;
finite number/density of resonances;
complete external optical boundary.
```

Question:

> Do established passivity/causality/material-response bounds already supply the missing photonic resource strongly enough to close Experiment 10, or is there a detector-specific gap worth deriving?
