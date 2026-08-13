import math
import numpy as np
from scipy import signal

# Exact Gillespie check: internal population cross-noise survives; extraction-count cross-noise cancels.
rng=np.random.default_rng(20260813)
ge,go,k,m=0.6,0.4,1.5,2.0
g=ge+go; birth=g*m; T=10000.; dt=.05; nb=int(T/dt)
o1=np.zeros(nb);o2=np.zeros(nb);e1=np.zeros(nb);e2=np.zeros(nb)
x1=x2=2;t=0.;si=0;ns=dt/2
while t<T:
    rr=(birth,birth,ge*x1,ge*x2,go*x1,go*x2,k*x1,k*x2); R=sum(rr)
    te=t+rng.exponential(1/R); stop=min(te,T)
    if ns<stop:
        end=min(int((stop-dt/2)/dt)+1,nb)
        o1[si:end]=x1;o2[si:end]=x2;si=end;ns=dt/2+si*dt
    if te>=T: break
    u=rng.random()*R;c=0
    for ev,r in enumerate(rr):
        c+=r
        if u<c: break
    b=min(int(te/dt),nb-1)
    if ev==0:x1+=1
    elif ev==1:x2+=1
    elif ev==2:x1-=1;e1[b]+=1
    elif ev==3:x2-=1;e2[b]+=1
    elif ev==4:x1-=1
    elif ev==5:x2-=1
    elif ev==6:x1-=1;x2+=1
    else:x2-=1;x1+=1
    t=te
o1[si:]=x1;o2[si:]=x2
z=int(200/dt); fs=1/dt

def sp(a,b):
    a=a[z:]-a[z:].mean();b=b[z:]-b[z:].mean()
    f,c=signal.csd(a,b,fs=fs,nperseg=8192,detrend='constant')
    _,p=signal.welch(a,fs=fs,nperseg=8192,detrend='constant')
    return f,p,c
f,po,co=sp(o1,o2);_,pe,ce=sp(e1,e2)
print('theory occupancy low/high:',k/(g+k),-k/(g+k))
print('theory zero f:',math.sqrt(g*(g+2*k))/(2*math.pi))
for a,b in [(0.02,.08),(.1,.3),(.4,.8),(1,2),(3,6)]:
    q=(f>=a)&(f<b)
    print(a,b,'occupancy',np.mean(np.real(co[q])/po[q]),'extraction',np.mean(np.real(ce[q])/pe[q]))
