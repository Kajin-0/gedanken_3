#!/usr/bin/env python3
import math
import numpy as np
TAU=1.15e-6; G=1/TAU; F1=5e3; F2=5e5

def pars(c):
    k=c*G/(1-c); lm=G+2*k; fx=math.sqrt(G*lm)/(2*math.pi)
    return k,lm,fx

def auto_rel(f,c):
    w=2*np.pi*f; _,lm,_=pars(c)
    a=G/(G*G+w*w)+lm/(lm*lm+w*w)
    return a/(1/G+1/lm)

def chi(f,c):
    w=2*np.pi*f; _,lm,_=pars(c); x=G*lm
    return (x-w*w)/(x+w*w)

def beff(c,d0):
    f=np.geomspace(F1,F2,200000); a=auto_rel(f,c)
    d=a/(a+(1-d0)/d0)
    return np.trapezoid(d*d*chi(f,c)**2,f)

def t5(c,d0):
    b=beff(c,d0); return 25/(2*c*c*b),b

print('tau_us',TAU*1e6,'fc_kHz',G/(2*math.pi)/1e3)
for c in (.005,.01,.02):
    k,_,fx=pars(c); print('c',c,'k_s-1',k,'fx_kHz',fx/1e3)
for c in (.005,.01):
    for d0 in (.9,.7,.5,.3):
        t,b=t5(c,d0); print('resource',c,d0,b,t)
for c in (.005,.01):
    for d in (1,.5):
        eps=.1*c*d/2
        print('mix',c,d,eps,20*math.log10(eps))
