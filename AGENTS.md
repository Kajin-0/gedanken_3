# AGENTS.md — Research Objective, Recovery, and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Most recently active branch:** `experiment-11-weighting-capacitance-duality`

Before material writes, fetch live targets and exact blob SHAs. Preserve failed, corrected, conditional, and negative paths. Do not use novelty or priority language without a dedicated prior-art audit.

## Primary objective

Generate analytical/theoretical photodetector research from simple Gedanken experiments. The target is a defensible theorem, bound, invariant, counterexample, scaling law, or escape condition—not a materials list or a new scalar FOM.

## Hard global scope — ANALYTICAL / THEORETICAL ONLY

Allowed work: first-principles derivations, exact toy models, analytical bounds/no-go theorems, asymptotics, numerical thought experiments, analytical comparisons, and prior-art audits.

Do not make fabrication, measurement, instrumentation, sample procurement, or laboratory optimization the next step.

## Research protocol

```text
premise
-> minimal model
-> first nontrivial result
-> immediate primary-literature audit
-> kill if established
-> deepen only if something survives
-> theorem/bound/invariant/counterexample
-> quantitative witness
-> adversarial audit
-> manuscript only if novelty survives.
```

Do not keep adding phenomenology to rescue a weak novelty case.

---

# Experiment 10 — FINAL DISPOSITION

Branch:

```text
experiment-10-room-temperature-lwir-admissibility
```

```text
CLOSED BY DEFAULT AS A NOVELTY / MANUSCRIPT PATH.
```

Read for recovery:

1. `experiments/10-room-temperature-lwir-admissibility/CURRENT_STATE.md`
2. `experiments/10-room-temperature-lwir-admissibility/FINAL_PHOTONIC_AUDIT_AND_DISPOSITION_2026-08-14.md`
3. `experiments/10-room-temperature-lwir-admissibility/THEOREM_CORE_2026-08-14.md`

Retained conditional single-pass theorem:

```math
\Sigma_c\ge C/[\min(V_{hop},v_{spec})]^2
```

under active-pair optical dominance and exact normal-momentum spectator-assisted Auger closure. This is technically useful but not established as novel.

---

# Post-Experiment-10 premise screen — five rejections

Read:

`candidate-audits/POST_EXP10_THEORETICAL_SCREEN_2026-08-14.md`

Rejected before Experiment 11:

```text
1. causal / nonminimum-phase detectivity;
2. spatially correlated noise / D* area scaling;
3. non-normal detector transient amplification;
4. wide-gap LWIR detection via intersubband transition;
5. equal D* but different non-Gaussian false-alarm tails.
```

Each reduced to established generic theory or a known detector architecture.

---

# Experiment 11 — FINAL DISPOSITION

Branch:

```text
experiment-11-weighting-capacitance-duality
```

Read:

1. `experiments/11-weighting-capacitance-duality/CURRENT_STATE.md`
2. `experiments/11-weighting-capacitance-duality/WEIGHTING_CAPACITANCE_DUALITY_STEP_2026-08-14.md`
3. `experiments/11-weighting-capacitance-duality/PROGRESS_LOG.md`

Premise: can electrode geometry increase prompt Shockley-Ramo signal independently of detector capacitance?

Exact retained result for homogeneous two-terminal drift:

```math
\boxed{
i_{pair}(\mathbf r,0^+)
=e(\mu_e+\mu_h)V_b|\mathbf E_w(\mathbf r)|^2.
}
```

Since

```math
C_{tot}=\int\epsilon|\mathbf E_w|^2dV,
```

for generation density `p(r)<=p_max`,

```math
\boxed{
\frac{\langle i_{pair}(0^+)\rangle}{C_{tot}}
\le
\frac{e(\mu_e+\mu_h)V_b}{\epsilon}p_{max}.
}
```

Uniform generation in active volume `V` gives

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

Reason: the uniform result is the photocarrier form of established homogeneous `RC=epsilon/sigma` Maxwell relaxation; the nonuniform extension is established reciprocal/lead-field conductivity-sensitivity theory. Fast-detector literature already treats weighting-field shape and capacitance as coupled geometry resources.

Do not add generic amplifier noise or timing models to rescue Experiment 11.

---

# ACTIVE NEXT ACTION

Resume screening new purely theoretical photodetector Gedanken premises.

Reject immediately if the first nontrivial result is merely an application of:

```text
detailed balance / reciprocity / FDT;
Landauer/reset thermodynamics;
standard information or detection theory;
minimum-phase / matched-filter / generic LTI theory;
standard quantum measurement limits;
critical coupling / delay-bandwidth / Bode-Fano / Rozanov;
generic non-normal dynamics;
known Auger suppression / band engineering;
ordinary shot-noise / Fano-factor arguments;
QWIP/QCD intersubband detection;
Maxwell dielectric relaxation / ordinary RC geometry cancellation;
lead-field / impedance-sensitivity reciprocity;
Experiment-08 zero-gap Kane statistics;
Experiment-09 collective/coherence line unless a genuinely new invariant appears.
```

Prefer premises whose first consequence arises from specifically photodetector physics and cannot be factored into a generic theorem plus a detector example.
