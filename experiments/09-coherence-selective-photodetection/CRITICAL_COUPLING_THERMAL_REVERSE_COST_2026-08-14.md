# Experiment 09 — Critical Coupling and the Thermal Reverse-Channel Cost

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** CONDITIONAL RESOURCE THEOREM / DOES NOT CLOSE EXPERIMENT 09 / NOVELTY NOT ESTABLISHED

## 1. Question

The preceding result shows that `N` independent local thermal-generation channels contribute only one local-channel rate to the collective bright readout, while the optical bright coupling can add coherently.

But efficient detection requires the bright optical excitation to be irreversibly converted into a counted degree of freedom.

If that conversion channel is itself passive and thermally reversible, does its reverse process restore an `N`-scaling dark floor?

Use the simplest one-resonance model that can answer the question exactly.

---

## 2. One-port resonant absorber

Let the bright excitation couple to the accepted optical port with rate

```math
\Gamma.
```

Let counted internal conversion/extraction provide an irreversible loss rate

```math
\kappa.
```

For a one-port single resonance, temporal coupled-mode theory gives the resonant absorbed/conversion fraction

```math
\boxed{
\eta
=\frac{4\Gamma\kappa}{(\Gamma+\kappa)^2}.
}
```

Perfect absorption occurs at critical coupling:

```math
\boxed{\kappa=\Gamma.}
```

This is established critical-coupling physics; it is used here only as the minimal detector conversion model.

---

## 3. Collective optical rate

For `N` equivalent constituents coupled phase coherently to one accepted optical mode, take

```math
\boxed{\Gamma=N\gamma_o}
```

inside the ideal Dicke/collective single-bright-mode limit, where `gamma_o` is the corresponding single-constituent optical-port rate.

Thus unit resonant conversion requires

```math
\boxed{\kappa=N\gamma_o.}
```

So the counted conversion channel must become faster in proportion to the collectively enhanced optical coupling if the device is to remain critically coupled.

---

## 4. Thermal reversibility of the counted conversion channel

Now impose a deliberately strong passive constraint: the same reservoir that converts a bright excitation into a counted output is in thermal equilibrium and admits the reverse transition.

Let the effective free-energy drop for the forward counted transition be

```math
\Delta F>0.
```

Local detailed balance gives

```math
\boxed{
\frac{\kappa_{rev}}{\kappa}
=e^{-\Delta F/(kT)}.
}
```

A reverse event creates a bright excitation without an incident signal photon and is therefore a bright-aligned dark source in this reduced detector model.

At critical coupling,

```math
\boxed{
\kappa_{rev}
=N\gamma_o e^{-\Delta F/(kT)}.
}
```

Hence the local-defect dark channel may remain `N`-independent after coherence selection while the **thermally reversible extractor channel grows linearly with `N`** unless its reverse probability is additionally suppressed.

---

## 5. Exact `kT ln N` scaling requirement

Require the reverse-extractor dark rate to remain below some fixed allowed floor `D_0`:

```math
\kappa_{rev}\le D_0.
```

Then

```math
\boxed{
\Delta F
\ge
kT\ln\left(\frac{N\gamma_o}{D_0}\right).
}
```

Relative to the corresponding `N=1` requirement, increasing collective dimension from `1` to `N` demands the additional free-energy separation

```math
\boxed{
\Delta(\Delta F)=kT\ln N.
}
```

Thus, in this passive critically coupled model, a parametric collective advantage is not free. The reverse channel can be held fixed only by paying a **logarithmically increasing thermodynamic bias**.

Representative increments:

```text
T = 77 K   (kT = 6.635 meV)
N = 10      -> kT ln N = 15.28 meV
N = 100     -> kT ln N = 30.56 meV
N = 1000    -> kT ln N = 45.84 meV

T = 300 K  (kT = 25.852 meV)
N = 10      -> kT ln N = 59.53 meV
N = 100     -> kT ln N = 119.05 meV
N = 1000    -> kT ln N = 178.58 meV
```

These numbers are thermodynamic scale illustrations, not material targets.

---

## 6. Finite-efficiency generalization

Perfect critical coupling is stronger than necessary. Let a required resonant conversion efficiency be

```math
\eta\ge\eta_0.
```

Define

```math
x=\kappa/\Gamma.
```

The efficiency condition is

```math
\eta=\frac{4x}{(1+x)^2}.
```

For a given `eta_0`, the smallest allowed extractor rate is

```math
\boxed{
x_{min}(\eta_0)
=\frac{1-\sqrt{1-\eta_0}}
{1+\sqrt{1-\eta_0}}.
}
```

Therefore

```math
\boxed{
\kappa
\ge
N\gamma_o x_{min}(\eta_0).
}
```

and the passive reverse floor obeys

```math
\boxed{
\kappa_{rev}
\ge
N\gamma_o x_{min}(\eta_0)
 e^{-\Delta F/(kT)}.
}
```

To hold this below `D_0`,

```math
\boxed{
\Delta F
\ge
kT\ln\left[
\frac{N\gamma_o x_{min}(\eta_0)}{D_0}
\right].
}
```

The `N`-dependent part remains exactly `kT ln N`.

Examples:

```text
eta_0 = 0.90  -> x_min = 0.5195
eta_0 = 0.99  -> x_min = 0.8182
eta_0 = 0.999 -> x_min = 0.9387
```

Near-unit resonant absorption therefore forces the internal conversion rate to track the collective optical rate closely.

---

## 7. What this theorem does and does not establish

It establishes, **conditional on the one-port resonant coupled-mode model and a passive thermal counted reservoir**, that

```text
collective optical coupling ~ N
+
high conversion efficiency
+
thermal reversibility of the conversion channel
```

implies an `N`-growing reverse bright-dark floor unless the forward/reverse free-energy bias grows as `kT ln N`.

It does **not** establish a universal `kT ln N` cost for every photodetector.

Possible escape routes include:

- a nonequilibrium extractor maintained by external work or chemical potential;
- time-dependent/coherent loading rather than stationary one-port critical coupling;
- an extraction architecture not representable as one thermally reversible loss channel;
- a very large fixed `Delta F` already making the reverse channel negligible over the relevant `N` range.

Those routes are not free; they move the resource into nonequilibrium work, control, bandwidth, or architecture.

---

## 8. Relation to the local dark bath

This result does **not** reverse the previous KMS conclusion for independent local nonradiative dark generation.

For the local bath,

```math
Gamma_{D,B}^{local}=d_\uparrow
```

remains independent of `N` in the ideal symmetric model.

The new `N`-dependent floor comes from the **separate bright-selective conversion reservoir whose coupling must scale with the optical port to preserve efficiency**.

Thus two dark sectors must be distinguished:

```text
local incoherent internal generation:
    coherence selection can prevent N-fold accumulation

bright-aligned reverse extraction:
    high-efficiency passive conversion can make it scale with N
```

This separation is central to the current Experiment-09 architecture.

---

## 9. Prior-art / novelty boundary

The ingredients are individually established:

- Dicke/collective optical-rate enhancement;
- one-port critical coupling and coherent perfect absorption;
- thermal local detailed balance / KMS reverse rates.

The present `kT ln N` result is an elementary consequence of combining them under the reduced detector assumptions. It is not presently authorized as a novel thermodynamic law.

Its value is as a **resource-accounting theorem** that prevents the coherence-selective detector idea from hiding the cost of maintaining a fast, one-way-looking bright extractor.

A dedicated literature search has not yet established whether this exact detector-specific scaling has already been stated.

---

## 10. Current interpretation

Experiment 09 is not killed, but the original apparent scaling has been narrowed substantially:

```text
coherence can reject local incoherent dark generation
without an N-fold local-dark penalty,

BUT

high-efficiency passive bright extraction introduces
an N-fold reverse-channel tendency,
which requires ~kT ln N additional free-energy suppression
if that floor is to remain fixed.
```

The next hard question is now sharper:

> Is there a fully passive, time-independent architecture in which optical bright-state coupling and counted extraction can both scale collectively while the reverse counted channel does **not** inherit the same collective enhancement, without violating unitarity, detailed balance, or an established scattering/sum-rule bound?

If the answer is no, the strongest surviving Experiment-09 result may be a no-go/resource theorem rather than a new detector architecture.
