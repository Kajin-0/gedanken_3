#!/usr/bin/env python3
"""Reduced-order identifiability test for sequential two-electron trap filling.

Model:
    V0 --a--> V- --b--> V2-
with a=C1*n and b=C2*n. The normalized transient is the mean captured charge
relative to the final two-electron charge. Common carrier density rescales both
rates; the shape depends on r=b/a.

This is an optimistic metrology screen, not a microscopic Hg-vacancy model.
"""

import math
import numpy as np
from scipy.optimize import least_squares


def nbar(x, r):
    """Mean number of captured electrons, x=a*t, r=b/a."""
    x = np.asarray(x, dtype=float)
    d = r - 1.0
    if abs(d) < 1e-8:
        p1 = x * np.exp(-x)
    else:
        p1 = np.exp(-x) * (-np.expm1(-d*x)) / d
    p0 = np.exp(-x)
    return 2.0 - 2.0*p0 - p1


def sigma_log_r(r, eps=0.005, npts=25):
    """Fisher 1-sigma on ln(r), one sweep; baseline/amplitude/ln(a) are nuisance."""
    x = np.logspace(-2, 2, npts)

    def model(theta):
        baseline, amp, ln_a, ln_r = theta
        xx = x*np.exp(ln_a)
        return baseline + amp*nbar(xx, np.exp(ln_r))/2.0

    th = np.array([0.0, 1.0, 0.0, math.log(r)])
    cols = []
    h = 1e-5
    for k in range(4):
        tp = th.copy(); tm = th.copy()
        tp[k] += h; tm[k] -= h
        cols.append((model(tp)-model(tm))/(2*h))
    J = np.column_stack(cols)
    F = J.T @ J / eps**2
    cov = np.linalg.pinv(F, rcond=1e-14)
    return math.sqrt(cov[3, 3])


def single_exp_residual(r, npts=25):
    """RMS residual from best baseline+amplitude+single-exponential fit."""
    t = np.logspace(-2, 2, npts)
    truth = nbar(t, r)/2.0

    def resid(p):
        baseline, amp, ln_k = p
        fit = baseline + amp*(1.0-np.exp(-np.exp(ln_k)*t))
        return fit-truth

    sol = least_squares(resid, [0.0, 1.0, 0.0])
    rr = resid(sol.x)
    return math.sqrt(float(np.mean(rr**2)))


def main():
    print("Optimistic 25-point sweep, a*t=0.01...100, unknown baseline/amplitude/time scale")
    print("point noise eps=0.5% of full two-electron signal")
    print("r=b/a   sigma_ln_r/sweep   best-single-exp RMS   sweeps for 2% delta-r at 5 sigma")
    for r in (0.05,0.1,0.2,0.3,0.5,0.8,1,1.2,2,3,5,10,20,50):
        s = sigma_log_r(r)
        rms = single_exp_residual(r)
        m = (5*s/0.02)**2
        print(f"{r:6g}   {s:12.4f}        {100*rms:9.3f}%             {m:10.0f}")

    print("\nExact special case: r=0.5 gives Nbar/2 = 1-exp[-(a/2)t], a pure single exponential.")
    print("As r->infinity the second capture is instantaneous and the curve also approaches a single exponential.")


if __name__ == "__main__":
    main()
