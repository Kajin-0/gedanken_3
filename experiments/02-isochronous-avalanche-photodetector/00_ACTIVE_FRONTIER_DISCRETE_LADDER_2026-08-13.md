# Active frontier supplement — discrete optical-depth ladder

**Date:** 2026-08-13  
**Controlling step:** `DISCRETE_DEPTH_LADDER_2026-08-13.md`

This note exists because the repository connector refused replacement writes to the existing recovery files after the discrete-ladder step. It is the newest non-destructive recovery pointer on `agent/noise-coupling-study`.

## Latest result

The finite-section implementation test passed at the current reduced-order residual floor.

For equal longitudinal sections in the 90%-absorption exponential benchmark:

```text
N=2 -> forward 9.322 ps RMS, 26.28% improvement
N=3 -> forward 8.369 ps RMS, 33.81% improvement, reverse 20.724 ps
N=4 -> forward 7.991 ps RMS, 36.81% improvement, reverse 21.167 ps
N=6 -> forward 7.703 ps RMS, 39.09% improvement
N=9 -> forward 7.570 ps RMS, 40.14% improvement
continuous -> 7.460 ps RMS, 41.00% improvement
```

Thus three equal sections already clear the current 30% timing-improvement target; four equal sections recover about 90% of the continuous-map RMS benefit.

## Exact finite-section relation

Let `U=X/L`, `b=ln(10)`, `h=1/N`, and choose each section depth at its conditional absorption centroid:

```math
q_j=(j-1)h+\frac1b-\frac{h}{e^{bh}-1}.
```

The forward discretization variance is

```math
D_N=\frac1{b^2}-\frac{h^2e^{bh}}{(e^{bh}-1)^2}.
```

Centroid orthogonality gives

```math
Var(U+Q_N)=4Var(U)-3D_N.
```

So nominal reverse anti-matching strengthens as forward discretization improves.

## Concrete first optical targets

```text
N=3: section length 1.0 mm
     depth centroids 0.291, 0.958, 1.624 um
     optical delay increment 13.333 ps

N=4: section length 0.75 mm
     depth centroids 0.226, 0.726, 1.226, 1.726 um
     optical delay increment 10.000 ps
```

For the 30% target, allowed weighted section-to-section mean timing RMS is about `2.88 ps` for `N=3` and `3.81 ps` for `N=4` under the current stochastic floor.

Nonuniform longitudinal section optimization changes the `N=3-4` timing result by only about `0.1 ps` or less.

## Preserved correction

Do not equate the geometric mean-delay match with the minimum total RMS timing point. Field-dependent diffusion and local transport variance can shift the total-RMS minimum.

## Next hard step

Build a constructive transverse optical-mode surrogate for the `N=3` or `N=4` staircase. Test whether a coupled-waveguide, multilayer, or related eigenmode construction can localize absorption near the target depths with roughly `100 nm` conditional absorption-depth RMS while retaining useful absorption and low transition reflection/scattering.

Do not begin manuscript construction or use novelty/priority language.