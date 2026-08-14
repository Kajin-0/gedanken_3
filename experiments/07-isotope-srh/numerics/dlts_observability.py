#!/usr/bin/env python3
import math

kB=1.380649e-23
h=6.62607015e-34
m0=9.1093837015e-31
k_eV=8.617333262e-5
mrel=0.65

def vth(T):
    return math.sqrt(3*kB*T/(mrel*m0))*100.0

def Nv(T):
    return 2*(2*math.pi*mrel*m0*kB*T/h**2)**1.5/1e6

def C(T,sigma):
    return sigma*vth(T)

def tau_capture(T,sigma,p):
    return 1/(C(T,sigma)*p)

def emission(T,Ea_meV,sigma):
    return C(T,sigma)*Nv(T)*math.exp(-(Ea_meV/1000)/(k_eV*T))

def fill_fraction(T,Ea_meV,p):
    r=Nv(T)*math.exp(-(Ea_meV/1000)/(k_eV*T))/p
    return 1/(1+r)

print('77 K capture times')
for p in (1e13,1e14,1e15):
    print('p=',p)
    for s in (1e-16,1e-15,4e-15):
        print(s,C(77,s),tau_capture(77,s,p))

print('\noptical-threshold crossover fillability')
hw=17.73
for delta,Tx in ((0.5,11.6),(1.0,23.2),(2.0,47.0),(3.0,74.3)):
    Ea=hw-delta
    print('delta',delta,'Ea',Ea,'Tx',Tx)
    for p in (1e14,1e15,1e16):
        print(p,fill_fraction(Tx,Ea,p))

print('\nfilling-curve sensitivity max =',math.exp(-1))