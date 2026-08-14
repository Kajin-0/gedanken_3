#!/usr/bin/env python3
"""Natural-Hg sister-pair pilot gate for Experiment 07.

Uses a normal random-effects planning approximation and the one-sided chi-square
upper confidence bound for a standard deviation. This is a planning calculation,
not a model of actual HgCdTe process statistics.
"""
import math
from scipy.stats import chi2

ALPHA=0.05
TARGET=0.005  # desired upper bound on pair-level false ln-rate scatter

def upper_sigma(s_obs,n):
    df=n-1
    return s_obs*math.sqrt(df/chi2.ppf(ALPHA,df))

for s in (0.002,0.003,0.0035,0.004,0.005,0.01):
    nmin=None
    for n in range(3,501):
        if upper_sigma(s,n) < TARGET:
            nmin=n; break
    print(f"observed pair RMS={100*s:.2f}% -> Nmin={nmin} for 95% upper sigma <0.50%")

print("\nSelected N=10 upper bounds")
for s in (0.002,0.003,0.004,0.005,0.01):
    print(f"s_obs={100*s:.2f}% -> sigma95={100*upper_sigma(s,10):.3f}%")
