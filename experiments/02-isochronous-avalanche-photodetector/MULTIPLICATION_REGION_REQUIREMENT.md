# Multiplication-region requirement

**Date:** 2026-08-13
**Status:** PRACTICAL TARGET NARROWING / PRIOR-ART-CONSTRAINED

Experiment 02 can only produce a material total timing improvement if stochastic avalanche buildup is not already much larger than the removable absorption-depth term.

Photon-counting APD prior art explicitly reports regimes where avalanche buildup dominates timing jitter and absorption-region transit variation is secondary. Conversely, thin/dead-space-engineered multiplication regions can narrow impact-ionization path-length distributions and reduce avalanche buildup time and its variation.

Therefore the strongest target regime is:

```text
thick or intentionally depth-sensitive absorber
+ drift-dominated carrier transport
+ tightly localized conditional absorption depth
+ low-buildup-jitter multiplication region
+ low readout/electronics timing floor
```

The multiplication architecture is not itself the proposed novelty. It is a prerequisite that exposes the absorption-depth term Experiment 02 is designed to remove.

Relevant established approaches include:

- submicron/thin multiplication regions exploiting dead-space effects;
- highly localized high-field multiplication regions;
- single-carrier-dominated low-k multiplication materials;
- engineered heterostructure multiplication regions.

Current literature includes APDs in which thinning/localizing the multiplication region makes the impact-ionization process more deterministic and reduces avalanche buildup time/jitter. This should be treated as enabling prior art, not as part of a novelty claim.

## Device-selection criterion

Let

```math
r_a=\sigma_{avalanche}^2/\sigma_{depth}^2.
```

Together with local optical-width, diffusion, and electronics terms, the total residual variance must satisfy the dimensionless feasibility bound in `DIMENSIONLESS_FEASIBILITY_BOUND.md`.

For a preferred >=30% total RMS improvement, the complete residual variance after ideal depth compensation must be no larger than about

```math
0.0626 (d/v_c)^2.
```

Thus a candidate APD whose avalanche buildup alone exceeds this budget should be rejected before photonic design work.