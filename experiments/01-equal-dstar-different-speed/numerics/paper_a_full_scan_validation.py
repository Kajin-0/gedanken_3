import math
import numpy as np
from scipy.linalg import expm

RHO0=3.5
ALPHA=0.05
ELL=(1.5,9.0)
DT=0.005
STRIDES=(4,2,1)
N=100000
Q0=(0.0,0.25,0.5,0.75,1.0)
SEED=2026081307

def R(y):
    y=np.abs(y)
    return (1+y)*np.exp(-y)

def transition(dt):
    A=np.array([[0.,1.],[-1.,-2.]])
    F=expm(A*dt)
    Q=np.eye(2)-F@F.T
    return F,np.linalg.cholesky((Q+Q.T)/2)

def run(ell):
    F,L=transition(DT)
    steps=int(round(ell/DT))
    q=np.arange(steps+1)*DT
    mean={f:R(q-f*ell)*RHO0 for f in Q0}
    rng=np.random.default_rng(SEED)
    noise={s:np.empty(N) for s in STRIDES}
    signal={(s,f):np.empty(N) for s in STRIDES for f in Q0}
    done=0
    while done<N:
        b=min(1000,N-done)
        state=rng.standard_normal((b,2))
        mn={s:state[:,0].copy() for s in STRIDES}
        ms={(s,f):state[:,0]+mean[f][0] for s in STRIDES for f in Q0}
        for k in range(1,steps+1):
            state=state@F.T+rng.standard_normal((b,2))@L.T
            z=state[:,0]
            for s in STRIDES:
                if k%s==0:
                    mn[s]=np.maximum(mn[s],z)
                    for f in Q0:
                        ms[(s,f)]=np.maximum(ms[(s,f)],z+mean[f][k])
        for s in STRIDES:
            noise[s][done:done+b]=mn[s]
            for f in Q0:
                signal[(s,f)][done:done+b]=ms[(s,f)]
        done+=b
    for s in STRIDES:
        thr=np.quantile(noise[s],1-ALPHA)
        print('ell',ell,'dt',DT*s,'thr',thr)
        for f in Q0:
            p=np.mean(signal[(s,f)]>thr)
            se=math.sqrt(p*(1-p)/N)
            print(' q0/L',f,'PD',p,'SE',se)

if __name__=='__main__':
    for ell in ELL:
        run(ell)
