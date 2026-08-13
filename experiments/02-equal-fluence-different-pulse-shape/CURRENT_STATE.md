# Current State — Experiment 02: Equal Fluence, Different Pulse Shape

**Date:** 2026-08-13
**Status:** **EARLY STOP — GOOD GEDANKEN RESULT, BUT THE CORE TWO-PULSE NONLINEAR-RECOMBINATION METHOD IS ESTABLISHED EXCITATION-CORRELATION SPECTROSCOPY.**

## Starting question

Two optical excitations deposit the same total absorbed carrier density into the same photoconductor. Must they produce the same integrated electrical response if their temporal shapes differ?

## Exact linear benchmark

For

```math
dn/dt=G(t)-n/\tau,
```

with the detector returned to baseline before and after the event,

```math
\boxed{\int n(t)dt=\tau\int G(t)dt.}
```

Thus equal absorbed fluence gives equal integrated photoconductive response in the linear one-lifetime model.

## Nonlinear result

For

```math
dn/dt=G(t)-n/\tau-Cn^3,
```

```math
\boxed{
\int n(t)dt
=\tau\left[\int G(t)dt-C\int n^3(t)dt\right].
}
```

Equal fluence therefore no longer guarantees equal response.

For one impulsive injection `n0`,

```math
\boxed{
A(n_0)=\sqrt{\tau/C}\arctan(n_0\sqrt{C\tau}).
}
```

The response relative to the linear prediction is

```math
A/(\tau n_0)=\arctan z/z,
\qquad z=n_0\sqrt{C\tau}.
```

## Exact split-pulse result

For two equal impulsive injections of fixed total fluence, increasing their temporal separation strictly increases the integrated response in the cubic model. See `SPLIT_PULSE_STEP.md`.

More generally, for autonomous recombination

```math
dn/dt=-R(n),
```

define

```math
\tau_eff(n)=n/R(n).
```

For two equal pulses separated by `Delta`,

```math
\boxed{
\frac{dA_2}{d\Delta}
=[\tau_eff(r+q)-\tau_eff(r)]r'(\Delta),
\qquad r'(\Delta)<0.
}
```

Hence:

```text
tau_eff decreases with density -> response rises with pulse separation
tau_eff constant               -> response is separation-independent
tau_eff increases with density -> response falls with pulse separation
```

See `GENERAL_SIGN_THEOREM.md`.

## Prior-art stop

The underlying HgCdTe high-injection physics is old: Auger-limited photoconductive saturation and injection-dependent lifetime were measured decades ago.

More importantly, excitation-correlation spectroscopy already performs the central two-pulse experiment. A close modern reference is:

- E. Rojas-Gatjens et al., *J. Phys. Chem. C* (2023), DOI 10.1021/acs.jpcc.3c04755.

That work applies two variably delayed femtosecond pulses, measures time-integrated photocurrent/photoluminescence, and explicitly models negative nonlinear photocurrent from

```math
\gamma n+B n^2
```

and

```math
\gamma n+A n^3
```

recombination laws.

Therefore the two-pulse diagnostic principle and its Auger/bimolecular interpretation are established prior art. The compact general sign identity is useful but not presently sufficient novelty for a theory paper.

A targeted search did not immediately locate the same excitation-correlation photocurrent method applied specifically to HgCdTe. That could motivate a future experiment, but no experiment is available here and it does not create a new theoretical principle.

## Disposition

```text
Gedanken value: strong
Exact derivation: retained
Device interpretation: useful
Theory novelty: insufficient / not established
HgCdTe experimental application: possible, not pursued here
```

Do not build a manuscript from this branch unless a materially different microscopic HgCdTe consequence is found.