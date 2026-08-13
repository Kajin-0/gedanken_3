#!/usr/bin/env python3
import math
import numpy as np

B=math.log(10.0); D_UM=2.0; L_UM=3000.0; T0_PS=40.0
F_TOTAL=0.03478633258; SIGMA_UM=0.100
S0=SIGMA_UM/D_UM; F_REST=F_TOTAL-S0*S0
N=3; H=1/N; MU=1/B-H/(math.exp(B*H)-1)
Q=np.array([j*H+MU for j in range(N)])
A=1/B**2-math.exp(B)/(math.exp(B)-1)**2
DIRECT=T0_PS*math.sqrt(F_TOTAL+A)
U=np.linspace(0,1,1000001)

def w(direction):
    if direction=='f': x=B*np.exp(-B*U)/(1-math.exp(-B))
    else: x=B*np.exp(-B*(1-U))/(1-math.exp(-B))
    return x/np.trapezoid(x,U)

def finite(lc_um):
    idx=np.minimum((U*N).astype(int),N-1)
    m=Q[idx].copy(); m2=Q[idx]**2
    if lc_um>0:
        delta=lc_um/L_UM
        for j,c in enumerate((1/3,2/3)):
            lo=c-delta/2; hi=c+delta/2; mask=(U>=lo)&(U<=hi)
            s=(U[mask]-lo)/delta; p=np.sin(np.pi*s/2)**2
            z1,z2=Q[j],Q[j+1]
            m[mask]=(1-p)*z1+p*z2; m2[mask]=(1-p)*z1*z1+p*z2*z2
    return m,m2+S0*S0

def rms(m,m2,direction):
    ww=w(direction)
    if direction=='f':
        e=np.trapezoid(ww*(U-m),U); e2=np.trapezoid(ww*(U*U-2*U*m+m2),U)
    else:
        e=np.trapezoid(ww*(U+m),U); e2=np.trapezoid(ww*(U*U+2*U*m+m2),U)
    return T0_PS*math.sqrt(F_REST+e2-e*e)

def trans_frac(lc_um):
    if lc_um<=0:return 0.0
    dlt=lc_um/L_UM; mask=np.zeros_like(U,dtype=bool)
    for c in (1/3,2/3): mask|=(U>=c-dlt/2)&(U<=c+dlt/2)
    return np.trapezoid(w('f')*mask,U)

def imperfect(eta,sigma_um=SIGMA_UM):
    m=np.zeros_like(U); m2=np.zeros_like(U)
    masks=(U<1/3,(U>=1/3)&(U<2/3),U>=2/3)
    ps=(np.array([1,0,0.]),np.array([1-eta,eta,0.]),np.array([1-eta,eta*(1-eta),eta*eta]))
    lv=(sigma_um/D_UM)**2
    for mask,p in zip(masks,ps): m[mask]=np.sum(p*Q); m2[mask]=np.sum(p*Q*Q)+lv
    return rms(m,m2,'f')

def eta30(sigma_um):
    lo,hi=.5,1.; target=.7*DIRECT
    for _ in range(70):
        mid=(lo+hi)/2
        if imperfect(mid,sigma_um)<=target: hi=mid
        else: lo=mid
    return hi

print('depth centroids um',Q*D_UM)
print('direct ps',DIRECT)
print('alpha_eff mm^-1',B/(L_UM/1000),'absorption per 1 mm',1-math.exp(-B/3))
print('\nLc_um frac forward_ps improvement_pct reverse_ps')
for lc in (0,25,50,100,200,400,1000):
    m,m2=finite(lc); sf=rms(m,m2,'f'); sr=rms(m,m2,'r')
    print(lc,trans_frac(lc),sf,100*(1-sf/DIRECT),sr)
print('\neta forward_ps improvement_pct')
for eta in (1,.99,.98,.97,.95,.9474,.94,.90,.80):
    sf=imperfect(eta); print(eta,sf,100*(1-sf/DIRECT))
print('\nrequired eta for 30 percent')
for s in (.05,.10,.125,.15,.175): print(s,eta30(s))
req=eta30(.1); ratio=2*math.sqrt(1/req-1)
kappa=math.pi/(2*50e-6); k0=2*math.pi/1.55e-6
print('eta_req',req,'DeltaBeta/kappa max',ratio,'Delta n_eff at 50 um',ratio*kappa/k0)
