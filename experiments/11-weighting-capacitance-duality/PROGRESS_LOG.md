# Progress Log — Experiment 11: Weighting-Field / Capacitance Duality

## 2026-08-14 — branch opened provisionally

Branch:

```text
experiment-11-weighting-capacitance-duality
```

Premise: ask whether electrode geometry can increase prompt Shockley-Ramo signal independently of detector capacitance.

## First exact result

For homogeneous two-terminal drift with no space charge,

```math
\mathbf E_b=V_b\mathbf E_w.
```

A newly created electron-hole pair gives

```math
\boxed{
i_{pair}(\mathbf r,0^+)
=e(\mu_e+\mu_h)V_b|\mathbf E_w(\mathbf r)|^2.
}
```

The same weighting field determines capacitance:

```math
\boxed{C_{tot}=\int\epsilon|\mathbf E_w|^2dV.}
```

Thus for uniform generation in active volume `V`,

```math
\boxed{
\frac{\langle i_{pair}(0^+)\rangle}{C_{tot}}
\le
\frac{e(\mu_e+\mu_h)V_b}{\epsilon V}.
}
```

General generation profile `p(r)` gives

```math
\boxed{
\frac{\langle i_{pair}(0^+)\rangle}{C_{tot}}
\le
\frac{e(\mu_e+\mu_h)V_b}{\epsilon}p_{max}.
}
```

## Immediate novelty audit

The uniform result is the single-pair / photocarrier form of the established homogeneous-medium identity

```math
RC=\epsilon/\sigma,
```

i.e. Maxwell dielectric relaxation.

The nonuniform result maps onto established reciprocal lead-field / impedance-sensitivity theory, where local conductivity perturbations are weighted by products of reciprocal fields; in the two-terminal case the kernel is proportional to `|E|^2`.

Fast timing detector literature already couples weighting-field uniformity with capacitance/readout loading.

## Disposition

```text
CLOSED BY DEFAULT AS A NOVELTY / MANUSCRIPT PATH.
```

Reason: technically exact but too directly reducible to established electrostatics and sensitivity theory.

Do not add generic amplifier-noise or timing models to rescue it.
