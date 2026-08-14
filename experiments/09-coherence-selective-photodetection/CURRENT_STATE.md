# Current State — Experiment 09: Coherence-Selective Photodetection

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** ACTIVE PROVISIONAL / THREE EXACT REDUCED RESULTS RETAINED / NOVELTY NOT ESTABLISHED / NEXT STEP IS A PASSIVE-ARCHITECTURE NO-GO TEST

## Minimal Gedanken premise

A photon-created event and a dark event are forced to have identical populations in an `N`-dimensional degenerate excitation manifold. The photon creates a coherent pure bright state

```math
|B\rangle=\sum_j\sqrt{w_j}e^{i\phi_j}|j\rangle,
```

while the dark process creates its completely dephased population-matched state

```math
\rho_D=\sum_jw_j|j\rangle\langle j|.
```

Thus energy, carrier number, and every observable diagonal in the microscopic basis are exactly unable to distinguish them. Only coherence differs.

Read in order:

1. `FIRST_PRINCIPLES_BRIGHT_STATE_DISCRIMINATION_2026-08-14.md`
2. `DEPHASING_EXTRACTION_AND_DETAILED_BALANCE_2026-08-14.md`
3. `CRITICAL_COUPLING_THERMAL_REVERSE_COST_2026-08-14.md`

---

## Result 1 — exact zero-signal-loss dark leakage

For the ideal coherent readout

```math
\Pi_B=|B\rangle\langle B|,
```

```math
\eta_\gamma=1,
```

while

```math
\boxed{
\epsilon_D=\sum_jw_j^2=1/N_{eff}.
}
```

with

```math
N_{eff}=1/\sum_jw_j^2.
```

Among all POVM elements that accept the photon state with probability one, `Pi_B` minimizes dark acceptance. For uniform weights, `epsilon_D=1/N`.

This is a detector specialization of established quantum-state-discrimination/state-verification mathematics; do not claim the generic theorem as new.

General dark-generation covariance:

```math
D=\sum_\alpha|l_\alpha\rangle\langle l_\alpha|,
```

with optical coupling vector `g`. Then the accepted dark-generation rate is

```math
\boxed{
\Gamma_D^B
=\frac{g^\dagger Dg}{g^\dagger g}.
}
```

So the physically relevant quantity is Hilbert-space alignment of optical excitation and dark-generation covariance, not raw dark rate alone.

Thermal/background photons in the same accepted optical mode create the same bright state and cannot be rejected by this mechanism.

---

## Result 2 — finite-time theorem under local dephasing

For the uniform bright state, bright extraction rate `kappa`, and independent local pure-dephasing rate `gamma`, the surviving excitation probability `P` and bright population `b` obey exactly

```math
\dot P=-\kappa b,
```

```math
\dot b=-(\kappa+\gamma)b+(\gamma/N)P.
```

Therefore

```math
\ddot P+(\kappa+\gamma)\dot P+(\kappa\gamma/N)P=0,
```

with rates

```math
r_\pm
=\frac{\kappa+\gamma
\pm\sqrt{(\kappa+\gamma)^2-4\kappa\gamma/N}}2.
```

For every `gamma>0`, both signal and dark excitations are eventually extracted:

```math
C_S(\infty)=C_D(\infty)=1.
```

Thus permanent dark rejection is impossible in this dephasing model. The effect is a finite-time separation.

For large `N`,

```math
\boxed{
r_-\simeq\frac{\kappa\gamma}{N(\kappa+\gamma)}}
```

and

```math
\boxed{
\tau_{leak}\simeq N(1/\kappa+1/\gamma).
}
```

High fast-window signal collection requires `kappa>>gamma`.

This is adjacent to established bright/dark dephasing and superradiance theory; photodetector-specific novelty remains unestablished.

---

## Result 3 — passive critical-coupling reverse cost

In a one-port resonant model,

```math
\eta=4\Gamma\kappa/(\Gamma+\kappa)^2.
```

If collective optical coupling gives

```math
\Gamma=N\gamma_o,
```

perfect absorption requires

```math
\kappa=N\gamma_o.
```

If the counted conversion reservoir is passive and thermally reversible with effective free-energy drop `Delta F`,

```math
\kappa_{rev}/\kappa=e^{-\Delta F/(kT)}.
```

Hence at critical coupling

```math
\kappa_{rev}=N\gamma_o e^{-\Delta F/(kT)}.
```

Holding this reverse bright-aligned dark floor fixed as `N` grows requires

```math
\boxed{
\Delta(\Delta F)=kT\ln N.
}
```

This is a **conditional resource theorem**, not a universal detector thermodynamic law. It assumes stationary one-port critical coupling and a passive thermally reversible counted conversion channel.

---

## Prior-art status

Strong adjacent established areas:

- quantum hypothesis testing/state verification;
- Dicke bright/dark collective states and superradiance;
- dephasing-induced bright/dark scattering;
- coherent excitonic photocurrent;
- fully quantum photodetector coherence/backaction models;
- quantum infrared detectors whose photocurrent is driven by collective electronic polarization and coherence-dependent extraction;
- KMS/local detailed balance;
- coherent perfect absorption / critical coupling.

No priority language is authorized.

Current status:

```text
simple Gedanken premise: useful and internally consistent
static theorem: exact
continuous-time theorem: exact in reduced symmetric model
local KMS cancellation: NO
passive extractor reverse-cost theorem: exact under stated reduced assumptions
novel detector principle: NOT ESTABLISHED
paper drafting: DO NOT BEGIN
```

---

## Single next hard question

> Is there any fully passive, time-independent architecture in which the accepted optical bright coupling and counted extraction both scale collectively, but the thermally reversed counted channel does not inherit the same collective enhancement, without violating unitarity, detailed balance, reciprocity, or established scattering/sum-rule bounds?

Attack this as a theorem/no-go problem before adding more device detail.

If no passive escape exists, Experiment 09 may still close with a useful resource theorem:

```text
coherence can reject local incoherent dark generation,
but scalable high-efficiency passive extraction restores a collective reverse-channel cost.
```

If a passive escape does exist, identify exactly which assumption in the one-port critical-coupling argument it violates and whether that resource is genuinely distinct from ordinary mode filtering or non-equilibrium work.
