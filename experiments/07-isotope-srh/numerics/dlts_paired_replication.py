#!/usr/bin/env python3
"""Paired sister-coupon replication scales for Experiment 07.

This is a Gaussian log-effect planning calculation, not a claim about achievable
HgCdTe process reproducibility.
"""
import math

Z=5.0
scatters=(0.005,0.01,0.02,0.05)
effects=(0.05,0.02,0.01)
rhos=(0.0,0.5,0.75,0.9,0.95)

print("N sister pairs for Z=5; s is per-coupon RMS in ln Cn")
for s in scatters:
    print(f"\ns={100*s:.1f}%")
    for eff in effects:
        d=abs(math.log1p(eff))
        vals=[]
        for rho in rhos:
            n=math.ceil(2*Z*Z*s*s*(1-rho)/(d*d))
            vals.append(n)
        print(f"effect={100*eff:.1f}% -> " + ", ".join(f"rho={r:.2f}:{n}" for r,n in zip(rhos,vals)))

print("\nUnpaired equal-group comparison is rho=0 in the same formula.")
