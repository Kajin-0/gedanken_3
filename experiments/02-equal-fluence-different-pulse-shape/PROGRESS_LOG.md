# Progress Log — Experiment 02

## 2026-08-13 — premise

Question: if two optical excitations produce the same total absorbed carrier number but different temporal concentration, must a HgCdTe photoconductor produce the same integrated electrical response?

## Linear result

For `dn/dt=G-n/tau`, complete-transient integration gives

```math
integral n dt = tau integral G dt.
```

Equal fluence is exactly reciprocal in the linear model.

## Nonlinear result

Adding cubic recombination gives

```math
integral n dt = tau[integral G dt - C integral n^3 dt].
```

Thus pulse shape matters through carrier-density history.

For an impulsive injection,

```math
A(n0)=sqrt(tau/C) atan(n0 sqrt(C tau)).
```

The integrated response saturates in the formal strong-injection limit of the minimal model.

## Split-pulse theorem

For two equal impulses of fixed total fluence, integrated response rises strictly with pulse separation in the cubic model.

The result generalizes to arbitrary autonomous recombination `R(n)`:

```math
dA2/dDelta = [tau_eff(r+q)-tau_eff(r)] r'(Delta),
```

where `tau_eff=n/R(n)` and `r'(Delta)<0`.

Thus the sign of the separation dependence is controlled by the density dependence of effective lifetime.

## Prior-art audit

High-flux HgCdTe Auger saturation and injection-dependent lifetime are longstanding results.

A decisive close prior-art match was found in excitation-correlation spectroscopy. Rojas-Gatjens et al., J. Phys. Chem. C (2023), DOI 10.1021/acs.jpcc.3c04755, use two delayed pulses and time-integrated photocurrent/PL to resolve nonlinear recombination and explicitly treat `gamma n + Bn^2` and `gamma n + An^3` kinetics.

Decision: do not build a theory manuscript from Experiment 02. A HgCdTe-specific experimental implementation might still be useful, but that is not a new theoretical principle and no experiment is available here.

## Adjacent candidate screened and rejected

Candidate: use equality/mismatch of the photoresponse time constant and GR-noise Lorentzian corner as a one-state-model falsification test.

Early literature search shows that HgCdTe photoconductor literature already ties the GR corner to effective lifetime, and multi-lifetime device models explicitly generate multiple GR Lorentzians associated with different regions/lifetimes.

Decision: useful engineering consistency check, not opened as a new experiment.

## Current rule

Continue novelty-first screening. Prefer microscopic device-physics questions whose first consequence is not already a standard spectroscopy or detector-characterization method.