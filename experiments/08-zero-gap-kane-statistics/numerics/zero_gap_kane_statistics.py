#!/usr/bin/env python3
"""Exact reduced-order Kane carrier statistics near Eg -> 0.

Theory-only numerical thought experiment.

Model:
- positive-gap simplified Kane electron/light-hole cones,
- finite parabolic heavy-hole curvature,
- full Fermi-Dirac statistics,
- intrinsic charge neutrality.

This is not a full 8-band HgCdTe calculation. It isolates the singular failure of
parabolic/nondegenerate intrinsic-carrier formulas at the massless-Kane point.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import expit, lambertw

HBAR = 1.054571817e-34
KB = 1.380649e-23
QE = 1.602176634e-19
M0 = 9.1093837015e-31

V = 1.07e6          # m/s, representative universal Kane velocity
MHH = 0.5*M0        # finite heavy-hole curvature regularizer


def I2(eta):
    return quad(lambda y: y*y*expit(eta-y), 0.0, max(100.0, eta+50.0),
                epsabs=1e-11, epsrel=1e-10, limit=500)[0]


def Ihalf_minus(eta):
    return quad(lambda y: math.sqrt(y)*expit(-(y+eta)), 0.0, 100.0,
                epsabs=1e-12, epsrel=1e-10, limit=500)[0]


def Jc(gamma, eta):
    lo = gamma
    def f(z):
        return (2.0*z-gamma)*math.sqrt(max(z*(z-gamma),0.0))*expit(eta-z)
    return quad(f, lo, max(100.0, eta+50.0, gamma+100.0),
                epsabs=1e-10, epsrel=1e-9, limit=500)[0]


def Jlh(gamma, eta):
    def f(z):
        return (2.0*z+gamma)*math.sqrt(z*(z+gamma))*expit(-(z+eta))
    return quad(f, 0.0, 100.0, epsabs=1e-10, epsrel=1e-9, limit=500)[0]


def solve_intrinsic(T, Eg_meV, mhh=MHH, v=V):
    kT = KB*T
    gamma = Eg_meV*1e-3*QE/kT
    A0 = kT**3/(2.0*math.pi**2*HBAR**3*v**3)
    Lambda = (2.0*mhh*v*v/kT)**1.5

    def neutrality(eta):
        return Jc(gamma,eta)-Jlh(gamma,eta)-Lambda*Ihalf_minus(eta)

    eta = brentq(neutrality,-50.0,80.0)
    n = A0*Jc(gamma,eta)
    plh = A0*Jlh(gamma,eta)
    phh = A0*Lambda*Ihalf_minus(eta)
    mu_meV = eta*kT/QE*1e3
    return eta,mu_meV,n/1e6,plh/1e6,phh/1e6


def naive_parabolic_ni(T, Eg_meV, mhh=MHH, v=V):
    if Eg_meV <= 0:
        return 0.0
    Eg = Eg_meV*1e-3*QE
    me = Eg/(2.0*v*v)
    Nc = 2.0*(me*KB*T/(2.0*math.pi*HBAR**2))**1.5
    Nv = 2.0*(mhh*KB*T/(2.0*math.pi*HBAR**2))**1.5
    ni = math.sqrt(Nc*Nv)*math.exp(-Eg/(2.0*KB*T))
    return ni/1e6


def parabolic_degeneracy_boundary(T, mhh=MHH, v=V):
    # Boundary at which the nondegenerate parabolic intrinsic Fermi level reaches Ec.
    # y = Eg/(kT) = (3/2) W[4 m_h v^2/(3 kT)].
    y = 1.5*lambertw(4.0*mhh*v*v/(3.0*KB*T)).real
    Eg_meV = y*KB*T/QE*1e3
    return float(y),float(Eg_meV)


def zero_gap_lambert_asymptotic(T, mhh=MHH, v=V):
    # Large-eta leading solution of zero-gap neutrality:
    # eta^3 exp(eta) ~= 3 sqrt(pi/2) (m_h v^2/kT)^(3/2).
    C = 3.0*math.sqrt(math.pi/2.0)*(mhh*v*v/(KB*T))**1.5
    eta = 3.0*lambertw(C**(1.0/3.0)/3.0).real
    A = (KB*T)**3/(math.pi**2*HBAR**3*v**3)
    n = A*eta**3/3.0
    return float(eta),float(n/1e6)


def main():
    T=77.0
    print(f"T={T:g} K; v={V:.3e} m/s; m_hh={MHH/M0:.3f} m0")
    ystar,Egstar=parabolic_degeneracy_boundary(T)
    print(f"parabolic self-consistency boundary: Eg/kT={ystar:.6f}, Eg={Egstar:.3f} meV")
    print()
    print("Eg(meV)  mu(meV)   n_exact(cm^-3)    n_par(cm^-3)   ratio")
    for Eg in [100,50,30,20,10,5,2,1,0.1,0]:
        eta,mu,n,plh,phh=solve_intrinsic(T,Eg)
        npv=naive_parabolic_ni(T,Eg)
        ratio=n/npv if npv>0 else float('inf')
        print(f"{Eg:7.1f} {mu:9.3f} {n:15.6e} {npv:15.6e} {ratio:8.3f}")
    print()
    eta,mu,n,plh,phh=solve_intrinsic(T,0.0)
    easym,nasym=zero_gap_lambert_asymptotic(T)
    print(f"zero gap exact: eta={eta:.6f}, mu={mu:.6f} meV, n={n:.6e} cm^-3")
    print(f"  light-hole holes={plh:.6e}; heavy-hole holes={phh:.6e} cm^-3")
    print(f"leading Lambert-W asymptotic: eta={easym:.6f}, n={nasym:.6e} cm^-3")
    print()
    print("Zero-gap temperature scaling")
    print("T(K) eta_exact  mu(meV) n(cm^-3)")
    for temp in [300,77,50,20,10,5,2,1,0.1]:
        eta,mu,n,_,_=solve_intrinsic(temp,0.0)
        print(f"{temp:6.1f} {eta:9.5f} {mu:9.5f} {n:12.5e}")


if __name__ == "__main__":
    main()
