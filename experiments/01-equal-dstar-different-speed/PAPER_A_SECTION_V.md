# V. Interpretation, limitations, and implications for detector comparison

The result above is easiest to misread if detector speed is treated only as a device-side bandwidth parameter. In the present task, changing the detector time scale changes two different quantities at once. It changes the physical rate at which signal evidence becomes available, but it also rescales the nuisance-parameter search through the dimensionless interval

```math
\ell=\frac{L}{\tau}.
```

The first effect favors the faster detector. The second can favor the slower detector because, over the same physical arrival-time uncertainty interval, the slower response produces a more strongly correlated timing scan and therefore a smaller normalized search domain. Proposition 1 shows that these two effects are sufficient, within the controlled equal-eventual-SNR family, to prevent a detector-only ordering by response time.

## A. The relevant ordering is a detector–task ordering

A detector specification such as `D*`, response time, or bandwidth describes a property of a device under stated measurement conditions. A decision time such as `T_D`, by contrast, belongs to a detector together with a task. In the present construction,

```math
\boxed{
T_D
=\tau X_D\!\left(\rho_0,\alpha,\beta,\frac{L}{\tau}\right),
}
```

so the ordering cannot be reduced to `tau` alone even after the eventual matched-filter SNR has been fixed. The same two detector channels can occupy different preference regimes as the allowed arrival-time uncertainty or decision criterion changes.

This does not make conventional detector figures of merit incorrect. It identifies the level at which they cease to define an ordering. If the scientific or engineering question is a finite-time decision with an unknown event time, then a statement that one detector is “better” than another is incomplete unless the task specifies, at minimum, the relevant waveform/noise model, the arrival-time uncertainty, and the false-alarm/detection criterion used to make the decision.

The result therefore suggests a distinction between **device characterization** and **task qualification**. Device characterization can report quantities such as responsivity, noise, detectivity, bandwidth, and temporal response. Task qualification asks what those properties imply under a specified measurement protocol. The present theorem concerns the second problem.

## B. Why a new scalar sensitivity–speed metric is not the conclusion

One possible reaction would be to search for a modified scalar figure of merit that combines sensitivity and speed. Such combinations are already established in detector literature, and the present result does not motivate a new universal product.

The reason is structural. In this family, the relevant search variable is not merely `tau` or bandwidth but the ratio

```math
\frac{L}{\tau},
```

and the decision surface also depends on

```math
\rho_0,\qquad \alpha,\qquad \beta,
```

as well as on the chosen search rule. Two tasks performed with the same detector can therefore correspond to different normalized search geometries. A scalar formed only from detector properties would erase precisely the task dependence that produces the crossover.

The practical lesson is consequently not to replace `D*` with another detector-only number. It is to attach detector comparisons to the measurement problem for which the comparison is intended. For the present model, the compact task descriptor is the dimensionless surface

```math
X_D(\rho_0,\alpha,\beta,L/\tau),
```

rather than a universal scalar ranking.

## C. What the crossover does and does not mean physically

The fast-to-slow crossover is not an intrinsic penalty for fast response. The detector family was normalized so that every member has the same eventual matched-filter SNR,

```math
\rho_{\tau,\infty}=\rho_0,
```

and Section III showed that every member benefits monotonically from additional observation time. The reversal is therefore neither a conventional sensitivity–speed tradeoff nor an artifact of choosing a poor integration duration.

Instead, the crossover arises from a change in the statistical geometry of the unknown-arrival search. Compressing the response in physical time compresses the matched-filter correlation length. For a fixed physical uncertainty interval `L`, the faster channel then contains more effectively distinct timing positions. Maintaining the same global false-alarm probability requires a correspondingly more stringent threshold. At small `L`, that additional search burden is weak and the faster physical time scale dominates. Near the faster detector's feasibility boundary, the search burden dominates strongly enough that the slower detector remains feasible while the faster detector does not.

This interpretation is deliberately protocol specific. A different treatment of arrival-time uncertainty can produce a different task surface. A Bayesian rule with an explicit arrival-time prior, a minimax test, a sequential procedure, or a joint detection/localization objective need not share the same boundary. Proposition 1 states what follows for the global-threshold matched-filter scan defined in this paper; it is not a theorem about every statistically admissible receiver.

## D. Scope and limitations

Several assumptions were chosen to isolate the timing-search mechanism cleanly.

First, the detector family is linear and time-scaled, and the output noise is additive, stationary, Gaussian, and white under the normalization used here. Real photodetectors can exhibit colored noise, signal-dependent noise, nonlinear response, saturation, dead time, drift, temperature dependence, and other effects that add task variables not represented by the present family.

Second, the two channels are deliberately normalized to equal eventual matched-filter SNR. This is a controlled comparison, not a claim that real fast and slow detectors generally have equal asymptotic sensitivity. Unequal eventual sensitivity can either reinforce or oppose the timing-search effect and would add another axis to the task boundary.

Third, the unknown parameter is arrival time. Unknown amplitude, phase, spectral shape, background level, or multiple simultaneous nuisance parameters would enlarge the search space and can change both threshold behavior and detector ordering.

Fourth, detection probability is defined at the true alignment while the threshold is set by the global noise-only timing scan. This criterion makes the mechanism transparent but is narrower than the full probability that the maximum of the signal-present scan exceeds threshold, and it does not directly impose a localization-accuracy requirement.

Finally, Proposition 1 proves existence of at least one fast-to-slow crossover under the stated continuity and large-search assumptions. It does not establish uniqueness of that crossover, and it does not imply that every practical parameter set contains a broad slow-preferred regime.

These restrictions are features of the construction rather than hidden generality assumptions: the aim is to exhibit a clean counterexample to detector-only ordering, not to claim a complete theory of transient photodetection.

## E. Implications for detector specification and experiment design

The theorem suggests a practical hierarchy for transient detector comparison. Reference-condition sensitivity remains useful for establishing the available signal-to-noise budget. Temporal response determines how quickly that budget can be accumulated. But when event timing is uncertain and a global false-alarm requirement is imposed, the correlation structure of the timing statistic becomes part of the measurement problem as well.

Accordingly, a task-oriented detector comparison should report enough information to reconstruct the decision problem rather than only a device scalar. In the present setting the essential quantities are the eventual matched-filter SNR (or the ingredients needed to calculate it), the temporal response or matched-filter template, the physical arrival-time uncertainty interval, and the required global false-alarm and detection probabilities. For more general noise or decision rules, the corresponding noise spectrum and protocol definition are also required.

This viewpoint is particularly relevant when detectors with substantially different temporal responses are compared for transient measurements. A bandwidth or rise-time advantage does not automatically translate into a lower decision time once the detector is embedded in an unknown-arrival search. Conversely, the theorem does not license choosing a slower detector solely to reduce the search burden; at low timing uncertainty the faster detector remains preferred in the constructed family. The comparison must be made at the operating point of interest.

The main conceptual change is therefore modest but consequential:

> **Detector specifications rank devices only relative to the task for which the ranking is being made. When arrival time is uncertain, response time affects both signal accumulation and the statistical size of the timing search.**

Within the controlled family studied here, that coupling is sufficient to reverse the fast/slow detection-time ordering even though eventual matched-filter sensitivity is identical.

## F. Conclusion

We considered two time-scaled photodetector channels normalized to equal eventual matched-filter SNR and asked whether the faster channel must reach a fixed detection operating point first when event arrival time is unknown. For the specified global-false-alarm matched-filter scan, the problem collapses to

```math
T_D(\alpha,\beta,L;\tau,\rho_0)
=\tau X_D\!\left(\rho_0,\alpha,\beta,\frac{L}{\tau}\right).
```

The faster channel benefits from a smaller physical time scale but pays a larger normalized timing-search burden. Under the assumptions of Proposition 1, these effects imply at least one finite fast-to-slow crossover and a slow-only feasibility regime before the slower detector reaches its own search-limited boundary.

The result should not be interpreted as a preference for slow detectors or as a replacement for established detector figures of merit. Its narrower implication is that equal asymptotic sensitivity does not define a detector-only ordering for this finite-time, unknown-arrival task. The ordering belongs to the detector together with the measurement protocol.