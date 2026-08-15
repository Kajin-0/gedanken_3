# Experiment 11 — Weighting-Field / Capacitance Duality

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Disposition:** **EXACT DETECTOR IDENTITY DERIVED / GENERALIZED TO NONUNIFORM GENERATION / CORE RESULT REDUCES TO ESTABLISHED MAXWELL-RELAXATION + RECIPROCAL-SENSITIVITY THEORY / CLOSED BY DEFAULT AS NOVELTY PATH**

## 1. Gedanken premise

Take two ideal two-terminal semiconductor photodetectors with the same:

- homogeneous active dielectric volume `Omega` of volume `V`;
- permittivity `epsilon`;
- electron and hole low-field mobilities `mu_e`, `mu_h`;
- applied terminal bias `V_b`;
- pair-generation probability density `p(r)`;
- no space charge, trapping, multiplication, or field-dependent mobility.

Allow only the electrode geometry to differ.

Question:

> Can electrode shaping increase the prompt Shockley-Ramo signal from a newly generated electron-hole pair without paying a corresponding detector-capacitance penalty?

The motivation was detector-specific: the same geometry determines both charge-motion coupling and front-end capacitive loading.

---

## 2. Weighting field and physical field coincide up to bias

Let the weighting potential `psi(r)` solve

```math
\nabla\cdot(\epsilon\nabla\psi)=0,
```

with

```text
psi = 1 on the sensing electrode,
psi = 0 on the return electrode(s).
```

Define

```math
\mathbf E_w=-\nabla\psi.
```

With the same two-terminal boundary conditions, no space charge, and a linear dielectric, the physical bias field is

```math
\boxed{\mathbf E_b=V_b\mathbf E_w.}
```

---

## 3. Prompt Ramo current of one newly generated pair

For an electron-hole pair created at the same point `r`, low-field drift gives

```math
\mathbf v_e=-\mu_e\mathbf E_b,
\qquad
\mathbf v_h=+\mu_h\mathbf E_b.
```

Using Shockley-Ramo,

```math
i=q\mathbf v\cdot\mathbf E_w,
```

the electron and hole contributions have the same terminal-current sign. Therefore

```math
\boxed{
i_{pair}(\mathbf r,0^+)
=e(\mu_e+\mu_h)V_b|\mathbf E_w(\mathbf r)|^2.
}
```

This identity is exact under the stated assumptions.

---

## 4. The same weighting-field energy defines capacitance

For a unit weighting voltage, electrostatic energy is

```math
U_w
=\frac12\int_{all}\epsilon(\mathbf r)|\mathbf E_w|^2dV
=\frac12 C_{tot}.
```

Hence

```math
\boxed{
C_{tot}=\int_{all}\epsilon(\mathbf r)|\mathbf E_w|^2dV.
}
```

If the active detector volume has homogeneous permittivity `epsilon`, then

```math
C_{tot}\ge
\epsilon\int_{\Omega}|\mathbf E_w|^2dV,
```

with equality when all relevant electrostatic field energy lies in that homogeneous active volume and no parasitic/fringing capacitance exists outside it.

---

## 5. Uniform-generation prompt-slew invariant

For uniform pair creation in `Omega`,

```math
p(\mathbf r)=1/V.
```

Average prompt current per generated pair is

```math
\langle i_{pair}(0^+)\rangle
=
\frac{e(\mu_e+\mu_h)V_b}{V}
\int_{\Omega}|\mathbf E_w|^2dV.
```

Therefore

```math
\boxed{
\frac{\langle i_{pair}(0^+)\rangle}{C_{tot}}
\le
\frac{e(\mu_e+\mu_h)V_b}{\epsilon V}.
}
```

For the ideal homogeneous two-terminal detector with no external/parasitic field energy,

```math
\boxed{
\frac{\langle i_{pair}(0^+)\rangle}{C}
=
\frac{e(\mu_e+\mu_h)V_b}{\epsilon V}.
}
```

Thus concentrating the weighting field can increase the local prompt current, but its volume-averaged increase is accompanied by the same increase in electrostatic capacitance.

For a sense node whose initial voltage slew is simply `dV_s/dt=i/C`,

```math
\boxed{
\left\langle\frac{dV_s}{dt}\right\rangle_{0^+}
\le
\frac{e(\mu_e+\mu_h)V_b}{\epsilon V}.
}
```

This is a prompt-signal statement, not a complete timing-resolution theorem.

---

## 6. Arbitrary generation profile

Let `p(r)` be any normalized nonnegative pair-generation probability density:

```math
\int_{\Omega}p(\mathbf r)dV=1.
```

Then

```math
\langle i_{pair}(0^+)\rangle
=e(\mu_e+\mu_h)V_b
\int_{\Omega}p(\mathbf r)|\mathbf E_w|^2dV.
```

Using

```math
p(\mathbf r)\le p_{max},
```

one obtains

```math
\boxed{
\frac{\langle i_{pair}(0^+)\rangle}{C_{tot}}
\le
\frac{e(\mu_e+\mu_h)V_b}{\epsilon}
\,p_{max}.
}
```

Interpretation:

- electrode geometry can exploit a localized optical-generation distribution by concentrating weighting-field energy where absorption is likely;
- the improvement cannot exceed the localization resource represented here by `p_max`;
- if the optical generation itself is allowed to become arbitrarily localized, no geometry-independent finite bound follows from capacitance alone.

This is the natural optical loophole of the prompt-slew bound.

---

## 7. Connection to ordinary conductance-capacitance duality

For a homogeneous Ohmic medium with conductivity `sigma`, the same Laplace field gives

```math
G
=\sigma\int|\mathbf E_w|^2dV,
```

while

```math
C
=\epsilon\int|\mathbf E_w|^2dV.
```

Therefore

```math
\boxed{\frac{G}{C}=\frac{\sigma}{\epsilon},}
```

or

```math
\boxed{RC=\frac{\epsilon}{\sigma}.}
```

This is the standard geometry-independent Maxwell dielectric-relaxation result.

The uniform photocarrier ensemble derived above is mathematically equivalent to a small uniform conductivity perturbation. Consequently, its geometry cancellation is not an independent new principle.

---

## 8. Prior-art collision

The following ingredients are established:

1. **Shockley-Ramo signal formation.** The induced current is `i=q v dot E_w`; semiconductor detector literature has used arbitrary weighting fields and weighting potentials for decades.

2. **Capacitance matrix from the same electrostatic boundary-value problem.** Weighting fields and detector capacitances are standard reciprocal/electrostatic quantities.

3. **Geometry-independent homogeneous `RC=epsilon/sigma`.** This is textbook electromagnetic-field theory and is the Maxwell dielectric-relaxation time.

4. **Nonuniform conductivity sensitivity kernels.** Lead-field / impedance-sensitivity theory expresses the response to a local conductivity perturbation through products of reciprocal electric fields. In the two-terminal reciprocal case this reduces to an `|E|^2` sensitivity kernel.

5. **Detector timing optimization already treats weighting-field uniformity and capacitance jointly.** Modern fast-timing detector literature explicitly identifies both weighting-field shape and capacitance as central geometric resources.

The present derivation combines these pieces in a clean per-photogenerated-pair form, but the first nontrivial result is too directly reducible to established electrostatics and reciprocal sensitivity theory.

```text
NOVELTY COLLISION: STRONG.
```

No dedicated paper-level novelty claim is justified.

---

## 9. Retained technical result

The useful result to preserve is

```math
\boxed{
\frac{\langle i_{pair}(0^+)\rangle}{C_{tot}}
\le
\frac{e(\mu_e+\mu_h)V_b}{\epsilon}\,p_{max}.
}
```

For uniform generation this becomes

```math
\boxed{
\frac{\langle i_{pair}(0^+)\rangle}{C_{tot}}
\le
\frac{e(\mu_e+\mu_h)V_b}{\epsilon V}.
}
```

It is a compact detector-design identity/bound, but it should be cited as a consequence of Shockley-Ramo plus electrostatic/Maxwell-relaxation reciprocity rather than presented as a new fundamental theorem.

---

## 10. Final disposition

```text
EXPERIMENT 11 CLOSED BY DEFAULT AS A NOVELTY / MANUSCRIPT PATH.
```

Reason:

```text
uniform-generation result -> Maxwell RC geometry cancellation;
nonuniform-generation result -> established reciprocal/lead-field sensitivity kernel;
fast-detector interpretation -> established weighting-field + capacitance design logic.
```

Do not deepen this branch by adding generic amplifier noise, matched filtering, or timing-jitter models merely to manufacture novelty.

The next experiment should again begin from a new specifically photodetector physical constraint.
