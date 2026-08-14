# Agent recovery entrypoint

Read `AGENTS.md` first, then this file. Do not infer research chronology from `main` alone.

## Hard global constraint — ANALYTICAL / THEORETICAL ONLY

The user cannot perform real-life experiments. Active work is restricted to first-principles derivation, exact toy models, analytical bounds/invariants/no-go theorems, numerical thought experiments, and adversarial primary-literature audits.

Do not make fabrication, sample procurement, measurement pilots, instrumentation, annealing, device processing, or laboratory optimization the next step.

Preserve negative results. Do not use `novel`, `first`, `fundamental`, or priority language without a dedicated audit.

---

## Repository lineage

`main` contains the Experiment-01/Paper-A lineage and is not the current theory frontier.

Two later branches diverged after Experiment 07:

```text
experiment-07-isotope-srh
head at handoff: 49f0832c11452f1e869790de0075513a8ed11347

experiment-08-zero-gap-kane-statistics
head: d8f5138146561d9907a1d1d8d43d7df999bb6ed4

merge base: b88dce33bc02805a91931eb61db354ef7d89df6f
```

Treat both as project knowledge. Experiment 07 closes the isotope-SRH novelty path; Experiment 08 independently closes the zero-gap Kane-statistics path.

The subsequent QND screen on `agent/qnd-information-screen` is also closed: nondestructive acquisition of photon-number information is established quantum measurement physics.

---

# ACTIVE FRONTIER — Experiment 09: Coherence-Selective Photodetection

Branch:

```text
experiment-09-coherence-selective-photodetection
```

Read in order:

1. `experiments/09-coherence-selective-photodetection/CURRENT_STATE.md`
2. `experiments/09-coherence-selective-photodetection/FIRST_PRINCIPLES_BRIGHT_STATE_DISCRIMINATION_2026-08-14.md`
3. `experiments/09-coherence-selective-photodetection/DEPHASING_EXTRACTION_AND_DETAILED_BALANCE_2026-08-14.md`
4. `experiments/09-coherence-selective-photodetection/CRITICAL_COUPLING_THERMAL_REVERSE_COST_2026-08-14.md`

## Minimal Gedanken premise

Create an `N`-dimensional exactly degenerate excitation manifold. A photon prepares

```math
|B\rangle=\sum_j\sqrt{w_j}e^{i\phi_j}|j\rangle,
```

while the dark event is deliberately chosen to have the **same microscopic populations** but no coherence:

```math
\rho_D=\sum_jw_j|j\rangle\langle j|.
```

Thus every population-diagonal observable is exactly blind to event provenance. The only discriminator is coherence.

## Result 1 — static bright-state discrimination

For

```math
\Pi_B=|B\rangle\langle B|,
```

signal acceptance is unity and matched incoherent dark leakage is

```math
\boxed{
\epsilon_D=\sum_jw_j^2=1/N_{eff},
\qquad
N_{eff}=1/\sum_jw_j^2.
}
```

This is optimal among all POVMs constrained to unit signal acceptance.

For a general dark-generation Kossakowski/covariance matrix

```math
D=\sum_\alpha|l_\alpha\rangle\langle l_\alpha|,
```

and optical coupling vector `g`, the accepted dark-generation rate is

```math
\boxed{
\Gamma_D^B=\frac{g^\dagger Dg}{g^\dagger g}.
}
```

Interpretation: internal dark rejection is a Hilbert-space alignment problem. A same-mode thermal/background photon prepares the same bright state and is not rejected.

Generic quantum-state discrimination mathematics is established prior art; do not claim it as new.

## Result 2 — continuous extraction plus local dephasing

For uniform `|B>`, bright extraction `kappa`, and local pure dephasing `gamma`, define surviving excitation probability `P` and bright population `b`. Exactly,

```math
\dot P=-\kappa b,
```

```math
\dot b=-(\kappa+\gamma)b+(\gamma/N)P,
```

so

```math
\ddot P+(\kappa+\gamma)\dot P+(\kappa\gamma/N)P=0.
```

The decay rates are

```math
r_\pm
=\frac{\kappa+\gamma
\pm\sqrt{(\kappa+\gamma)^2-4\kappa\gamma/N}}2.
```

For every `gamma>0`, both photon and dark excitations are eventually extracted:

```math
C_S(\infty)=C_D(\infty)=1.
```

Thus coherence selection is a **finite decision-window resource**, not permanent rejection.

For large `N`,

```math
\boxed{
r_-\simeq\frac{\kappa\gamma}{N(\kappa+\gamma)},
\qquad
\tau_{leak}\simeq N(1/\kappa+1/\gamma).
}
```

High fast-window photon collection requires `kappa >> gamma`.

Bright/dark scattering under dephasing is established adjacent theory; detector-specific novelty is not established.

## Result 3 — local KMS detailed balance does not automatically cancel the effect

For `N` independent identical thermal local baths,

```math
L_j^+=\sqrt{d_\uparrow}|j\rangle\langle g|,
\qquad
L_j^-=\sqrt{d_\downarrow}|g\rangle\langle j|,
```

with

```math
d_\uparrow/d_\downarrow=e^{-E/(kT)},
```

the total raw upward dark rate is `N d_up`, but the bright-projected upward rate is only

```math
\Gamma_{D,B}^{\uparrow}=d_\uparrow.
```

The bright downward local-bath rate is `d_down`, so the projected channel itself obeys detailed balance without an extra factor of `N`.

Therefore the simplest KMS no-go fails: independent local thermal baths do not become optically coherent merely because the optical excitation is collective.

## Result 4 — passive critical-coupling reverse-channel cost

In a one-port resonant model,

```math
\eta=4\Gamma\kappa/(\Gamma+\kappa)^2.
```

If collective optical coupling gives

```math
\Gamma=N\gamma_o,
```

unit absorption requires `kappa=N gamma_o`.

If the counted conversion reservoir is itself passive and thermally reversible with free-energy drop `Delta F`,

```math
\kappa_{rev}/\kappa=e^{-\Delta F/(kT)}.
```

At critical coupling,

```math
\kappa_{rev}=N\gamma_o e^{-\Delta F/(kT)}.
```

Holding that reverse bright-aligned dark floor fixed as `N` grows requires the additional suppression

```math
\boxed{\Delta(\Delta F)=kT\ln N.}
```

This is a **conditional resource theorem**, not a universal detector law. It assumes stationary one-port critical coupling and a passive reversible counted-loss reservoir.

---

## Current prior-art risk

Strong adjacent areas already exist:

- Helstrom/state-verification theory;
- Dicke bright/dark states and superradiance;
- dephasing-induced bright/dark scattering;
- coherent excitonic photocurrent;
- fully quantum photodetector coherence/backaction theory;
- collective/strong-coupling infrared detectors with coherence-dependent electronic extraction;
- KMS/local detailed balance;
- coherent perfect absorption / critical coupling.

The focused searches have not yet established a direct prior statement of the full photodetector-specific chain

```text
population-identical coherent photon state vs incoherent internal dark state
-> bright-selective finite-window extraction
-> exact r_- leakage scale
-> passive reverse-channel kT ln N cost.
```

That is **not** proof of novelty.

```text
Experiment 09: ACTIVE PROVISIONAL
mathematical results: RETAIN
novel detector principle: NOT ESTABLISHED
paper drafting: DO NOT BEGIN
```

---

## Single next hard question

> Is there any fully passive, time-independent architecture in which accepted optical bright coupling and counted extraction both scale collectively, but the thermally reversed counted channel does not inherit the same collective enhancement, without violating unitarity, reciprocity, detailed balance, or an established scattering/sum-rule bound?

Attack this as a no-go theorem before adding any material/device complexity.

If no passive escape exists, Experiment 09 may close as a resource theorem rather than a new detector architecture. If an escape exists, identify precisely which assumption in the one-port critical-coupling derivation is removed and what physical resource replaces it.

---

## Closed-path reminders

- Experiment 08: zero-gap Kane asymptotics retained; publication frontier closed.
- Experiment 07: isotope-SRH identities retained; novelty path closed.
- Experiment 06: two-carrier SRH provenance architecture closed by direct prior art.
- Experiment 05: active-volume/bandwidth theorem failed with arbitrary lossless matching.
- Experiment 04: passive nonreciprocal sensitivity path closed by trace bound.
- Experiment 03: photon-recycling cross-noise path closed as established linear exchange information.
- Experiment 02: migrating-depth APD dominated by fixed-depth waveguide comparator.
- Experiment 01: equal-D* acquisition/information-spectrum path closed by established optimum-filter theory.
- QND information without absorption: closed by direct QND prior art.
