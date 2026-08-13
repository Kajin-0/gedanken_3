# Paper A — full-scan validation addendum

**Date:** 2026-08-13

The first full-template scan calculation used one path ensemble to estimate both the noise threshold and signal-present power. Its effect is negligible at 100000 paths, but an independent calibration is cleaner.

A second production calculation therefore used:

```text
Delta = 0.005
120000 noise-only paths for threshold calibration
120000 independent signal-present paths for power
q0/L = 0, .1, .2, ..., 1
calibration seed = 2026081311
power seed       = 2026081312
```

The Matérn-3/2 state transition is exact on the grid; only the smooth path maximum is discretized. A separate nested-grid run at Delta=.020,.010,.005 showed negligible change.

For the slow channel (`ell=1.5`), the independently calibrated threshold is

```text
Gamma_grid = 2.02413605
```

and the complete full-template scan power across the eleven tested arrival positions is

```text
0.94583 <= P_D^scan,infinity <= 0.95555.
```

For the fast channel (`ell=9`),

```text
Gamma_grid = 2.58683790
```

and

```text
0.85651 <= P_D^scan,infinity <= 0.88315.
```

The largest fast-channel estimate has binomial standard error about `0.000927`, placing it roughly eighteen standard errors below `beta=.90` before the separately small calibration uncertainty.

Thus the independent-ensemble result confirms the original calculation: every tested slow-channel placement is above `.90`, while every tested fast-channel placement is below `.90`.

This is still a full-template numerical robustness check, not a theorem of finite-time exact-scan crossover. The Step-49 hard stop remains active.
