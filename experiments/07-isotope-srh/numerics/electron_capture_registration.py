#!/usr/bin/env python3
"""Experiment 07: electron-capture filling-curve registration and isotope toy model.

Reduced-order calculations only. The optical-phonon phase-space model is not a
microscopic Hg-vacancy capture calculation.
"""
import math
import numpy as np
from numpy.polynomial.hermite import hermgauss

KB_MEV_K = 8.617333262e-2
T = 77.0
KT = KB_MEV_K*T
CM1_TO_MEV = 0.1239841984
M_HG_NAT, M_HG_204, M_TE = 200.59, 204.0, 127.60
E_PH = 143.0*CM1_TO_MEV

def mu(a,b): return a*b/(a+b)
r_hg = math.sqrt(mu(M_HG_NAT,M_TE)/mu(M_HG_204,M_TE))
E_PH_204 = E_PH*r_hg

# Fisher precision for A-B-A normalized filling curves. Each state gets its own
# unknown saturation amplitude. Baseline log-capture rate may drift linearly with
# cycle index. The B state has the isotope log-ratio q.
x = np.logspace(-1,1,9)
rows=[]
for j in (-1,0,1):
    for z in x:
        f=1.0-math.exp(-z)
        df=z*math.exp(-z)
        d=np.zeros(6)
        d[{-1:0,0:1,1:2}[j]]=f
        d[3]=df             # common log rate
        d[4]=j*df           # linear cycle drift
        d[5]=(j==0)*df      # isotope log-ratio
        rows.append(d)
J=np.array(rows)
coef=math.sqrt(np.linalg.inv(J.T@J)[5,5])

# Hg-only optical-threshold stress, using the same Gaussian broadening and fixed
# bypass convention as two_step_srh_isotope.py. Here delta_e = hbar*omega-(Ec-Et).
XH,WH=hermgauss(64); WH=WH/math.sqrt(math.pi)
sigma_E=(8.9*CM1_TO_MEV)/2.354820045

def phase(delta):
    delta=np.asarray(delta,float)
    return np.where(delta>0,np.sqrt(np.maximum(delta,0))*np.exp(-np.maximum(delta,0)/KT),0.0)

def avg_phase(Esep,Ephon):
    Esep=np.atleast_1d(Esep).astype(float)
    z=Esep[:,None]+math.sqrt(2)*sigma_E*XH[None,:]
    return phase(Ephon-z)@WH

def capture_ratio(delta_e,f_ref):
    phi_ref=avg_phase(np.array([E_PH-1.0]),E_PH)[0]
    bypass=phi_ref*(1-f_ref)/f_ref if f_ref<1 else 0.0
    Esep=np.array([E_PH-delta_e])
    return float((bypass+avg_phase(Esep,E_PH_204)[0])/(bypass+avg_phase(Esep,E_PH)[0]))

print(f"Hg-only phonon shift: {E_PH_204-E_PH:.6f} meV ({(r_hg-1)*100:.4f}%)")
print(f"Fisher sigma[ln q] = {coef:.4f} * epsilon/sqrt(m)")
print("5-sigma repeat counts for per-point normalized RMS epsilon")
for eps in (0.005,0.01,0.02):
    out=[]
    for effect in (0.05,0.02,0.01):
        m=math.ceil((5*coef*eps/abs(math.log1p(effect)))**2)
        out.append(m)
    print(f"epsilon={100*eps:.1f}% -> m for 5%,2%,1% = {out}")
print("\nHg-only heavy/natural Cn stress ratios; sigma_E=8.9 cm^-1 FWHM proxy")
for de in (0.10,0.25,0.50,1.00,2.00):
    vals=[capture_ratio(de,f) for f in (0.5,0.7,0.9,0.99)]
    print(f"delta_e={de:.2f} meV: " + " ".join(f"f={f:.2f}:{r:.4f}" for f,r in zip((0.5,0.7,0.9,0.99),vals)))
