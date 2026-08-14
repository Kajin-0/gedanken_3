# Experiment 09 — Dephasing, Continuous Extraction, and Detailed-Balance Stress

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** EXACT REDUCED DYNAMICS / FIRST KMS NO-GO TEST SURVIVED / NOVELTY NOT ESTABLISHED

## 1. Why the static projection theorem is not enough

The first Experiment-09 result assumes an ideal projective readout applied before coherence is lost. A real detector-like readout is closer to continuous irreversible extraction from the bright state.

A crucial question is therefore:

> If local dephasing continuously converts bright and dark collective components into one another, does a coherence-selective detector eventually accept every dark excitation anyway?

The answer is **yes** for any nonzero ergodic local dephasing in the minimal symmetric model. Coherence selection is a finite-time resource, not an infinite-time dark-event rejection mechanism.

---

## 2. Symmetric model

Take `N` exactly degenerate local excitations `|j>` and the uniform bright state

```math
|B\rangle=\frac1{\sqrt N}\sum_{j=1}^N|j\rangle.
```

Let the bright state be extracted irreversibly to a counted sink at rate `kappa`:

```math
L_X=\sqrt\kappa\,|X\rangle\langle B|.
```

Let every local basis state undergo independent pure dephasing with identical rate `gamma`:

```math
L_{\phi j}=\sqrt\gamma\,|j\rangle\langle j|.
```

With this convention, off-diagonal local-basis coherences decay at rate `gamma`.

Track the density operator only inside the excited manifold; its trace decreases when extraction occurs.

By permutation symmetry, write

```math
\rho_{ii}=x,
\qquad
\rho_{i\ne j}=y.
```

Define surviving excitation probability

```math
P=Nx
```

and instantaneous bright population

```math
b=\langle B|\rho|B\rangle
=x+(N-1)y.
```

The cumulative detection probability is

```math
C(t)=1-P(t).
```

---

## 3. Exact two-dimensional closure

The master equation closes exactly on `(P,b)`:

```math
\boxed{\dot P=-\kappa b}
```

and

```math
\boxed{
\dot b
=-(\kappa+\gamma)b
+\frac\gamma N P.
}
```

Eliminating `b` gives

```math
\boxed{
\ddot P
+(\kappa+\gamma)\dot P
+\frac{\kappa\gamma}{N}P=0.
}
```

The two positive decay rates are

```math
\boxed{
r_{\pm}
=\frac{\kappa+\gamma
\pm\sqrt{(\kappa+\gamma)^2-4\kappa\gamma/N}}{2},
}
```

with `r_+>=r_->0` for every `kappa>0`, `gamma>0`.

Thus

```math
P(t)=A e^{-r_-t}+B e^{-r_+t}.
```

For arbitrary initial bright population `b_0` and `P(0)=1`,

```math
B=\frac{\kappa b_0-r_-}{r_+-r_-},
\qquad
A=1-B.
```

---

## 4. Signal versus dark initial conditions

### Photon-created signal

The absorbed photon prepares `|B>`:

```math
P(0)=1,
\qquad
b_0^{(S)}=1.
```

### Local incoherent dark generation

A uniformly random local dark event gives the ensemble state

```math
\rho_D(0)=I_N/N,
```

so

```math
P(0)=1,
\qquad
b_0^{(D)}=1/N.
```

Both evolve under the **same** subsequent dynamics. Their different detection-time distributions originate only from the initial coherence.

---

## 5. New no-go: infinite observation time erases the discrimination

If `gamma=0`, then

```math
r_-=0,
\qquad
r_+=\kappa.
```

A dark excitation has only its initial `1/N` bright component extracted, so

```math
C_D(\infty)=1/N.
```

But for every

```math
\gamma>0,
```

both `r_+` and `r_-` are strictly positive. Hence

```math
\boxed{
P_S(\infty)=P_D(\infty)=0,
}
```

and therefore

```math
\boxed{
C_S(\infty)=C_D(\infty)=1.
}
```

So any nonzero local dephasing that continually repopulates the bright component makes every excitation eventually extractable.

**Coherence-selective dark rejection requires a finite decision window.**

This is stronger than the static statement that dephasing reduces the instantaneous projection contrast.

---

## 6. Emergent slow dark-leakage time

For large `N`, the slow rate is

```math
\boxed{
r_-
\simeq
\frac{\kappa\gamma}{N(\kappa+\gamma)}.
}
```

Thus the slow leakage timescale is

```math
\boxed{
\tau_{leak}
\simeq
N\left(\frac1\kappa+\frac1\gamma\right).
}
```

Two limits:

```text
fast extraction:   kappa >> gamma  -> tau_leak ~ N/gamma
fast dephasing:    gamma >> kappa  -> tau_leak ~ N/kappa
```

Therefore collective dimension creates a **timescale separation**, not permanent rejection.

The useful detector regime is

```math
\boxed{
1/(\kappa+\gamma)
\ll t_{decision}
\ll 1/r_-.
}
```

Signal is collected on the fast mode while incoherent dark population leaks into the bright channel only on the slow mode.

---

## 7. Extraction must outrun dephasing

For large `N`, the signal survival has a slow-tail amplitude approximately

```math
A_S\simeq\frac\gamma{\kappa+\gamma}.
```

Hence the fast-time signal-collection plateau is approximately

```math
\boxed{
C_S^{fast}\simeq\frac\kappa{\kappa+\gamma}.
}
```

Thus high signal efficiency before the slow dark leakage starts requires

```math
\boxed{\kappa\gg\gamma.}
```

For example, achieving a `~99%` fast-collection plateau requires roughly

```math
\kappa/\gamma\gtrsim99
```

in the large-`N` limit.

This is the exact dynamical version of the intuitive requirement that extraction act before the optical coherence is destroyed.

---

## 8. Numerical thought-experiment scale

Take dimensionless units `gamma=1`, with

```text
N = 100
kappa = 100 gamma.
```

The exact rates are approximately

```text
r_+ = 100.9901 gamma
r_- = 0.009902 gamma
```

so the fast extraction time is `~0.0099/gamma` while the slow dark-leakage time is `~101/gamma`.

At decision times expressed in units of `1/kappa`:

```text
t = 1/kappa:   C_S ~0.6295,   C_D ~0.00633
t = 3/kappa:   C_S ~0.9423,   C_D ~0.00963
t = 5/kappa:   C_S ~0.9839,   C_D ~0.01023
t =10/kappa:   C_S ~0.9902,   C_D ~0.01078
```

This is not a materials prediction. It demonstrates the existence of a broad analytical time window in which nearly all photon-created bright excitations can be extracted while only about the initial `1/N` fraction of incoherent dark excitations has leaked through.

---

## 9. Thermal detailed-balance stress test

Now ask whether equilibrium detailed balance automatically destroys this distinction.

Let each local excitation couple to an independent identical thermal bath with upward and downward jumps

```math
L_j^+
=\sqrt{d_\uparrow}\,|j\rangle\langle g|,
```

```math
L_j^-
=\sqrt{d_\downarrow}\,|g\rangle\langle j|.
```

For excitation energy `E`, thermal detailed balance gives, in the standard weak-coupling thermal limit,

```math
\boxed{
\frac{d_\uparrow}{d_\downarrow}
=e^{-E/(kT)}.
}
```

The total raw upward dark-generation rate is

```math
N d_\uparrow.
```

But the rate injected directly into the uniform bright state is

```math
\Gamma_{D,B}^{\uparrow}
=\sum_j d_\uparrow|\langle B|j\rangle|^2
=d_\uparrow.
```

Similarly, the local-bath decay rate of a bright excitation is

```math
\Gamma_{B}^{\downarrow}
=\sum_j d_\downarrow|\langle j|B\rangle|^2
=d_\downarrow.
```

Therefore the projected bright channel itself obeys

```math
\boxed{
\frac{\Gamma_{D,B}^{\uparrow}}
{\Gamma_B^{\downarrow}}
=e^{-E/(kT)},
}
```

with **no extra factor of `N`**.

Hence KMS/detailed balance within the local nonradiative bath does not force the `N` local dark channels to add coherently in the bright direction. It preserves the local-bath bright projection.

This means the simplest thermodynamic no-go fails:

```text
local thermal detailed balance
DOES NOT by itself erase
collective-optical / local-dark mode mismatch.
```

---

## 10. What detailed balance *does* require

Every separate passive thermal coupling channel has its own reverse process.

Therefore, if the bright-state extractor itself is an equilibrium thermal channel between `|B>` and a sink state `|X>`, its forward extraction must be accompanied by a reverse bright-aligned excitation channel with the appropriate Boltzmann/KMS ratio.

That creates a separate dark floor associated with the extractor bath.

However, microscopic detailed balance does **not** generally impose an identity between

```text
local defect/phonon bath coupling matrix
```

and

```text
optical bright-state coupling vector
```

when they are physically distinct reservoirs/operators.

Thus there is no generic KMS theorem, found at this stage, that forces an independent local nonradiative dark bath to become bright-aligned merely because optical absorption is collective.

---

## 11. Prior-art boundary

The dynamical ingredients are established:

- local dephasing mixes collective bright and dark sectors in superradiant systems;
- bright/dark quasiparticle scattering and lifetimes under dephasing have been analyzed;
- thermodynamically consistent local-bath master equations and KMS detailed balance are established open-system theory.

The present exact two-variable detector reduction and its interpretation as a **finite decision-window dark-count filter** are therefore not claimed as generic new open-system mathematics.

The focused prior-art screen has not yet located the specific detector result

```math
r_-\simeq\frac{\kappa\gamma}{N(\kappa+\gamma)}
```

used to quantify the time window separating coherent photon extraction from incoherent internal dark-event leakage.

Novelty remains unestablished.

---

## 12. Updated frontier

Experiment 09 has survived two immediate kill tests:

```text
static state discrimination: survives, but math is standard
local KMS detailed balance: does not automatically cancel the effect
```

It has also acquired a strong limitation:

```text
infinite-time dark rejection: impossible for gamma > 0
```

The next question should be resource-level rather than another toy extension:

> After imposing optical oscillator-strength/sum-rule constraints and counting the thermally reversible bright extractor channel, can the finite-window signal-to-dark advantage grow parametrically with `N`, or does a stronger passive-system bound cancel that scaling?

That is the next hard gate. Do not optimize a device or choose a material before this analytical bound is resolved.
