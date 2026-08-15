# Agent recovery entrypoint

Read `AGENTS.md` first, then this file. Do not infer chronology from `main` alone.

## Hard scope

All active research is analytical/theoretical only. Preserve failed/corrected/conditional paths. Do not use novelty or priority language without dedicated prior-art audit.

# Experiment 10 — CLOSED BY DEFAULT

Branch:

```text
experiment-10-room-temperature-lwir-admissibility
```

Final disposition:

```text
CLOSED BY DEFAULT AS A NOVELTY / MANUSCRIPT PATH.
```

Recovery files:

1. `experiments/10-room-temperature-lwir-admissibility/CURRENT_STATE.md`
2. `experiments/10-room-temperature-lwir-admissibility/FINAL_PHOTONIC_AUDIT_AND_DISPOSITION_2026-08-14.md`
3. `experiments/10-room-temperature-lwir-admissibility/THEOREM_CORE_2026-08-14.md`

Retained conditional result:

```math
\Sigma_c\ge C/[\min(V_{hop},v_{spec})]^2.
```

Technically useful; novelty/manuscript path closed.

---

# Post-Experiment-10 premise screen

Read:

`candidate-audits/POST_EXP10_THEORETICAL_SCREEN_2026-08-14.md`

Five rejected premises:

```text
causal/nonminimum-phase detectivity;
spatial covariance correction to D* area scaling;
non-normal transient detector dynamics;
wide-gap intersubband LWIR escape;
non-Gaussian false-alarm detectivity.
```

---

# Experiment 11 — CLOSED BY DEFAULT

Branch:

```text
experiment-11-weighting-capacitance-duality
```

Read:

1. `experiments/11-weighting-capacitance-duality/CURRENT_STATE.md`
2. `experiments/11-weighting-capacitance-duality/WEIGHTING_CAPACITANCE_DUALITY_STEP_2026-08-14.md`
3. `experiments/11-weighting-capacitance-duality/PROGRESS_LOG.md`

Question: can electrode geometry increase prompt Shockley-Ramo signal independently of detector capacitance?

For homogeneous two-terminal drift,

```math
\mathbf E_b=V_b\mathbf E_w
```

and a newly generated pair gives

```math
\boxed{
i_{pair}(\mathbf r,0^+)
=e(\mu_e+\mu_h)V_b|\mathbf E_w(\mathbf r)|^2.
}
```

The same weighting field defines capacitance,

```math
C_{tot}=\int\epsilon|\mathbf E_w|^2dV.
```

Therefore for `p(r)<=p_max`,

```math
\boxed{
\frac{\langle i_{pair}(0^+)\rangle}{C_{tot}}
\le
\frac{e(\mu_e+\mu_h)V_b}{\epsilon}p_{max}.
}
```

For uniform generation in active volume `V`,

```math
\boxed{
\frac{\langle i_{pair}(0^+)\rangle}{C_{tot}}
\le
\frac{e(\mu_e+\mu_h)V_b}{\epsilon V}.
}
```

Disposition:

```text
CLOSED BY DEFAULT AS A NOVELTY / MANUSCRIPT PATH.
```

Reason: uniform result reduces to established Maxwell `RC=epsilon/sigma`; nonuniform extension reduces to reciprocal lead-field / impedance sensitivity theory. Do not rescue with generic readout-noise or timing models.

# ACTIVE NEXT ACTION

Resume theoretical premise screening.

Avoid immediate rediscoveries of:

```text
Maxwell dielectric relaxation / geometry-independent RC;
lead-field / impedance-sensitivity reciprocity;
Shockley-Ramo itself;
detailed balance / FDT;
generic LTI/matched-filter/minimum-phase theory;
generic covariance / non-normal dynamics;
standard likelihood or point-process detection theory;
QWIP/QCD intersubband detection;
known Auger engineering;
standard cavity/delay-bandwidth/passivity bounds.
```

Open a new experiment only when the first nontrivial consequence is specifically photodetector physics and survives a primary-literature collision test.
