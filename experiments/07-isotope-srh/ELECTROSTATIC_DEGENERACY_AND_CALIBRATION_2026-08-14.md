# Electrostatic degeneracy and calibration requirement

**Date:** 2026-08-14
**Status:** IMPORTANT CORRECTION / HORIZONTAL REGISTRATION DOES NOT REMOVE COMMON FILL-DENSITY CHANGES / MINORITY-DENSITY CALIBRATION IS NOW A HARD GATE

## 1. Exact degeneracy

The normalized filling curve for a spatially varying minority-electron population is

`F(t)=integral w(z)[1-exp(-C_n n(z)t)]dz / integral w(z)dz`.

Earlier work correctly noted that the absolute carrier-density scale need not be known if the electrostatic filling state is reproduced. The stronger statement that registration by itself removes carrier-density uncertainty is false.

If isotope/process state B has

`C_B = q_C C_A`

and

`n_B(z)=q_n n_A(z)`,

then exactly

`F_B(t)=F_A(q_C q_n t)`.

Therefore horizontal registration returns

`boxed: q_fit = q_C q_n`.

A uniform multiplicative change in minority-electron density is exactly indistinguishable from a capture-coefficient change.

This is a structural identifiability problem, not statistical noise. More repetitions do not remove it.

## 2. What multi-bias / full-curve collapse can and cannot do

Let a small state-dependent density perturbation be

`delta ln n(z)=eta(z)`.

The component of `eta(z)` that projects onto a uniform time scaling is absorbed into `q_fit`. Spatially varying components alter the filling-curve shape and should produce incomplete horizontal collapse.

Therefore:

- multiple filling times detect non-scaling transient changes;
- multiple filling biases test whether `q_fit` is stable as the depletion/filling profile changes;
- exact curve collapse is strong evidence that one multiplicative rate changed;
- exact curve collapse **cannot say whether that multiplier was `C_n` or the common scale of `n_fill`**.

A separate common-density calibration is mandatory.

## 3. Forward-bias quasi-equilibrium sensitivity

In a simple p-type quasi-equilibrium injection picture,

`n_fill proportional to (N_c N_v / p) exp[-(E_g-qV)/(kT)]`.

Hence, to first order,

`Delta ln n_fill = Delta ln(N_c N_v) - Delta ln p - [Delta E_g-q Delta V]/(kT)`.

At 25 K, `kT~=2.15 meV`. An uncorrected `0.02 meV` change in the effective bandgap/electrostatic energy therefore creates about a `0.93%` false capture change.

If the expected isotope effect in `C_n` is 2%, a reasonable systematic budget is

`sigma_Dlnn <=~0.5%`

so density uncertainty consumes no more than about one quarter of the target signal.

If bandgap uncertainty alone set this floor, it would require roughly

`0.011 meV` differential `E_g` precision at 25 K.

That is too demanding to use as the only calibration route.

At higher temperature the same energy uncertainty produces a smaller density error, but Experiment 07 also needs low-temperature capture/emission data for the one-phonon closure.

## 4. n-type majority-carrier shortcut is not yet authorized

MIS-DLTS of electron traps in n-type HgCdTe is established, and a 2025 calculation treats conduction-electron capture on an `A_2^-2` mercury-vacancy level in wider-gap material.

However mercury vacancies are double acceptors with multiple charge states. The relevant initial charge-state occupancy depends on Fermi level. Current primary evidence does not yet establish that a simple n-type majority-carrier fill measures the **same vacancy charge transition** that bottlenecks SRH recombination in the p-type narrow-gap calculation.

Therefore:

`n-type majority-electron measurement as a replacement for the p-type SRH transition: NOT YET VALIDATED`.

Do not adopt it merely because the carrier density would be easier to know.

## 5. Calibration / rescue hierarchy

### A. Physical minority-density correction

Use C-V/Hall, measured `E_g`, pulse voltage, and a transport/electrostatic model to estimate the isotope-state ratio of the effective minority-electron density.

This is the simplest route but must demonstrate <=~0.5-1% ratio uncertainty for a 2-5% capture signal.

### B. Internal reference trap

If a second resolvable electron trap occupies the same filling region,

`lambda_target/lambda_ref = C_target/C_ref`

for a common local electron-density scale.

The isotope double ratio cancels the density exactly:

`[(lambda_t/lambda_r)_B]/[(lambda_t/lambda_r)_A] = (C_t,B/C_t,A)/(C_r,B/C_r,A)`.

This only helps if the reference trap's own isotope response is negligible or independently characterized. A far-from-resonance reference could be useful because a smooth isotope prefactor would primarily affect an intercept rather than the near-threshold `1/T` slope, but this is not guaranteed.

### C. Injection-DLTS fallback

Fleming et al., J. Appl. Phys. 118, 015703 (2015), DOI `10.1063/1.4923358`, developed injection-DLTS in a bipolar structure specifically to control minority-carrier density while measuring capture rates over electric field and carrier energy.

This is a strong established metrology comparator. No simple off-the-shelf HgCdTe bipolar implementation has been identified in the focused search. A custom three-terminal HgCdTe injector/sense structure should therefore be a fallback only, not the baseline, because its transport calibration could add more complexity than it removes.

### D. Direct simultaneous minority-density monitor

A future option is to measure the free-carrier density during filling by an independent photoconductive/optical/electrical observable and fit trap occupancy against cumulative carrier exposure rather than pulse time. This has not yet been reduced to a clean HgCdTe implementation and is not the current default.

## 6. Strong isotope claim hierarchy

A convincing target result now requires all of the following:

1. normalized A/B filling curves collapse under one horizontal time scale at each fill bias;
2. the extracted scale is stable across several fill biases/profiles;
3. a separate estimate/reference constrains the common `Delta ln n_fill` below the isotope-signal budget;
4. the corrected `Delta ln C_n(T)` obeys the electron-detuning closure from Raman + differential emission DLTS;
5. natural-Hg controls give zero within the same analysis.

Without item 3, even perfect filling-curve collapse does **not** identify an isotope-dependent microscopic capture coefficient.

## 7. Current disposition

```text
horizontal registration as statistical metrology: RETAIN
horizontal registration as self-sufficient C_n identification: REJECT
multi-bias curve collapse: RETAIN as shape/electrostatic control
n-type shortcut: HOLD until charge-transition equivalence proven
physical density correction: LEADING baseline, hard precision gate
internal reference trap: STRONG optional control
injection-DLTS: ESTABLISHED fallback, HgCdTe implementation not yet justified
novelty: NOT ESTABLISHED
paper drafting: DO NOT BEGIN
```

## 8. Next hard step

Build the cheapest pre-isotope pilot that measures the actual **pair-level false `q_fit` floor** in natural-Hg sister devices while deliberately varying fill bias and carrier injection. Determine whether C-V/Hall/Eg corrections can reduce the common-scale variation below 0.5-1%.

If not, search for a stable second electron trap that can serve as an internal density reference before committing to a custom injection-DLTS structure.
