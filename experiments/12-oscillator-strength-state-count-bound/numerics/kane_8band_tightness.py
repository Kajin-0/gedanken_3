#!/usr/bin/env python3
"""Eight-band HgCdTe tightness test for Experiment 12.

Implements the bulk, constant-parameter limit of the second-order 8-band
Kane Hamiltonian in Novik et al., Phys. Rev. B 72, 035321 (2005), Eq. (5)-(6).
The calculation is deliberately restricted to a bounded k-domain.

Outputs:
  * alloy composition solving the Laurenti Eg(x,T) convention for 10 um at 300 K;
  * charge-neutral chemical potential and carrier densities;
  * selected-window optical-capacity v_B^cap;
  * theorem lower bound and bound/exact ratio for several low-energy windows;
  * simple k-domain convergence checks.

No phenomenological linewidth is required because the theorem's frequency
integral can be evaluated directly as a transition sum before introducing a
broadened delta function.
"""

import math
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq

HBAR_EV_S = 6.582119569e-16
A0 = 0.0380998212  # hbar^2/(2m0), eV nm^2
KB_EV_K = 8.617333262e-5
T_K = 300.0
KT = KB_EV_K * T_K
EG = 1.239841984e-1  # eV, hc/(10 um)
EP = 18.8  # eV, Novik endpoint table / standard HgCdTe Kane energy


def eg_laurenti(x: float, T: float) -> float:
    """Laurenti empirical Eg(x,T) relation, eV."""
    return (
        -0.303 * (1.0 - x)
        + 1.606 * x
        - 0.132 * x * (1.0 - x)
        + (6.3 * (1.0 - x) - 3.25 * x - 5.92 * x * (1.0 - x))
        * 1.0e-4
        * T * T
        / (11.0 * (1.0 - x) + 78.7 * x + T)
    )


X = brentq(lambda xx: eg_laurenti(xx, T_K) - EG, 0.10, 0.30)

# Representative linear interpolation of Novik Table-I endpoint parameters.
DELTA = (1 - X) * 1.08 + X * 0.91
F = (1 - X) * 0.0 + X * (-0.09)
G1 = (1 - X) * 4.1 + X * 1.47
G2 = (1 - X) * 0.5 + X * (-0.28)
G3 = (1 - X) * 1.3 + X * 0.03
KAPPA = (1 - X) * (-0.4) + X * (-1.31)
MUW = 0.5 * (G3 - G2)
GBAR = 0.5 * (G3 + G2)
P = math.sqrt(EP * A0)  # eV nm because EP = P^2/A0


def h8(kx: float, ky: float, kz: float) -> np.ndarray:
    """Bulk second-order 8-band Kane Hamiltonian in eV."""
    kp = kx + 1j * ky
    km = kx - 1j * ky
    k2 = kx * kx + ky * ky + kz * kz
    kp2 = kx * kx + ky * ky

    Tc = EG + A0 * (2.0 * F + 1.0) * k2
    U = -A0 * G1 * k2
    V = -A0 * G2 * (kp2 - 2.0 * kz * kz)
    R = -A0 * math.sqrt(3.0) * (MUW * kp * kp - GBAR * km * km)

    # Bulk constant parameters: commutators vanish and Sbar=S_tilde.
    Sm = -2.0 * A0 * math.sqrt(3.0) * G3 * km * kz
    Sp = -2.0 * A0 * math.sqrt(3.0) * G3 * kp * kz
    tSm, tSp = Sm, Sp
    C = 0j

    H = np.zeros((8, 8), dtype=complex)
    H[0] = [Tc, 0, -P * kp / math.sqrt(2), math.sqrt(2 / 3) * P * kz,
            P * km / math.sqrt(6), 0, -P * kz / math.sqrt(3), -P * km / math.sqrt(3)]
    H[1] = [0, Tc, 0, -P * kp / math.sqrt(6), math.sqrt(2 / 3) * P * kz,
            P * km / math.sqrt(2), -P * kp / math.sqrt(3), P * kz / math.sqrt(3)]
    H[2] = [-P * km / math.sqrt(2), 0, U + V, -Sm, R, 0,
            np.conj(Sm) / math.sqrt(2), -math.sqrt(2) * R]
    H[3] = [math.sqrt(2 / 3) * P * kz, -P * km / math.sqrt(6), -np.conj(Sm),
            U - V, C, R, math.sqrt(2) * V, -math.sqrt(3 / 2) * tSm]
    H[4] = [P * kp / math.sqrt(6), math.sqrt(2 / 3) * P * kz, np.conj(R),
            np.conj(C), U - V, np.conj(Sp), -math.sqrt(3 / 2) * tSp, -math.sqrt(2) * V]
    H[5] = [0, P * kp / math.sqrt(2), 0, np.conj(R), Sp, U + V,
            math.sqrt(2) * np.conj(R), np.conj(Sp) / math.sqrt(2)]
    H[6] = [-P * kz / math.sqrt(3), -P * km / math.sqrt(3), Sm / math.sqrt(2),
            math.sqrt(2) * V, -math.sqrt(3 / 2) * np.conj(tSp), math.sqrt(2) * R,
            U - DELTA, C]
    H[7] = [-P * kp / math.sqrt(3), P * kz / math.sqrt(3), -math.sqrt(2) * np.conj(R),
            -math.sqrt(3 / 2) * np.conj(tSm), -math.sqrt(2) * V, Sp / math.sqrt(2),
            np.conj(C), U - DELTA]
    return H


def dh_dkx(kx: float, ky: float, kz: float) -> np.ndarray:
    """Analytic derivative dH/dkx, in eV nm."""
    kp = kx + 1j * ky
    km = kx - 1j * ky
    dT = 2.0 * A0 * (2.0 * F + 1.0) * kx
    dU = -2.0 * A0 * G1 * kx
    dV = -2.0 * A0 * G2 * kx
    dR = -2.0 * A0 * math.sqrt(3.0) * (MUW * kp - GBAR * km)
    dSm = -2.0 * A0 * math.sqrt(3.0) * G3 * kz
    dSp = dSm
    dC = 0j

    D = np.zeros((8, 8), dtype=complex)
    D[0] = [dT, 0, -P / math.sqrt(2), 0, P / math.sqrt(6), 0, 0, -P / math.sqrt(3)]
    D[1] = [0, dT, 0, -P / math.sqrt(6), 0, P / math.sqrt(2), -P / math.sqrt(3), 0]
    D[2] = [-P / math.sqrt(2), 0, dU + dV, -dSm, dR, 0,
            np.conj(dSm) / math.sqrt(2), -math.sqrt(2) * dR]
    D[3] = [0, -P / math.sqrt(6), -np.conj(dSm), dU - dV, dC, dR,
            math.sqrt(2) * dV, -math.sqrt(3 / 2) * dSm]
    D[4] = [P / math.sqrt(6), 0, np.conj(dR), np.conj(dC), dU - dV,
            np.conj(dSp), -math.sqrt(3 / 2) * dSp, -math.sqrt(2) * dV]
    D[5] = [0, P / math.sqrt(2), 0, np.conj(dR), dSp, dU + dV,
            math.sqrt(2) * np.conj(dR), np.conj(dSp) / math.sqrt(2)]
    D[6] = [0, -P / math.sqrt(3), dSm / math.sqrt(2), math.sqrt(2) * dV,
            -math.sqrt(3 / 2) * np.conj(dSp), math.sqrt(2) * dR, dU, dC]
    D[7] = [-P / math.sqrt(3), 0, -math.sqrt(2) * np.conj(dR),
            -math.sqrt(3 / 2) * np.conj(dSm), -math.sqrt(2) * dV,
            dSp / math.sqrt(2), np.conj(dC), dU]
    return D


def vx(kx: float, ky: float, kz: float) -> np.ndarray:
    return dh_dkx(kx, ky, kz) * 1.0e-9 / HBAR_EV_S


def grid(kmax: float, nr: int, nmu: int, nphi: int):
    xr, wr = leggauss(nr)
    ks = 0.5 * kmax * (xr + 1.0)
    wks = 0.5 * kmax * wr
    mus, wm = leggauss(nmu)
    phis = np.linspace(0, 2.0 * math.pi, nphi, endpoint=False)
    wp = 2.0 * math.pi / nphi
    for k, wk in zip(ks, wks):
        for mu, wmu in zip(mus, wm):
            st = math.sqrt(max(0.0, 1.0 - mu * mu))
            for phi in phis:
                kk = np.array([k * st * math.cos(phi), k * st * math.sin(phi), k * mu])
                # d^3k/(2pi)^3; nm^-3 -> cm^-3 gives 1e21.
                weight = k * k * wk * wmu * wp / (2.0 * math.pi) ** 3 * 1.0e21
                yield kk, weight


def fermi(E, chemical_potential):
    x = np.clip((E - chemical_potential) / KT, -100.0, 100.0)
    return 1.0 / (np.exp(x) + 1.0)


def carrier_state(kmax=2.0, nr=160, nmu=10, nphi=16):
    energies = []
    weights = []
    for kk, w in grid(kmax, nr, nmu, nphi):
        energies.append(np.linalg.eigvalsh(h8(*kk)))
        weights.append(w)
    E = np.asarray(energies)
    W = np.asarray(weights)

    def neutrality(mu):
        f = fermi(E, mu)
        ne = np.sum(W[:, None] * f[:, 6:8])
        nh = np.sum(W[:, None] * (1.0 - f[:, :6]))
        return ne - nh

    mu = brentq(neutrality, 0.10, 0.17)
    f = fermi(E, mu)
    ne_band = np.sum(W[:, None] * f[:, 6:8])
    nh_band = np.sum(W[:, None] * (1.0 - f[:, :6]))
    below = E < mu
    ne_cross = np.sum(W[:, None] * np.where(~below, f, 0.0))
    nh_cross = np.sum(W[:, None] * np.where(below, 1.0 - f, 0.0))
    return mu, ne_band, nh_band, ne_cross, nh_cross


def energy_clusters(vals, tol=1.0e-7):
    groups = []
    used = np.zeros(len(vals), dtype=bool)
    for i, e in enumerate(vals):
        if used[i]:
            continue
        inds = np.where(np.abs(vals - e) < tol)[0]
        used[inds] = True
        groups.append(list(inds))
    return groups


def optical_point(kk, mu, elo, ehi):
    vals, U = np.linalg.eigh(h8(*kk))
    M = U.conj().T @ vx(*kk) @ U
    f = fermi(vals, mu)
    lower = np.where(vals < mu)[0]
    upper = np.where(vals > mu)[0]

    # The theorem-weighted optical integral after performing the delta-function
    # frequency integral. Units: density * velocity^2.
    s = 0.0
    for i in lower:
        for j in upper:
            de = vals[j] - vals[i]
            if elo <= de <= ehi:
                s += (f[i] - f[j]) * abs(M[j, i]) ** 2 / (math.exp(de / (2.0 * KT)) - 1.0)

    # Basis-invariant selected-shell capacity. Because v_x conserves k, the
    # energy-shell operator is block diagonal in k. Exact Kramers degeneracies
    # are grouped before taking the singular value.
    cap2 = 0.0
    groups = energy_clusters(vals)
    for g in groups:
        eg = float(np.mean(vals[g]))
        if eg > mu:
            partners = []
            for gl in groups:
                el = float(np.mean(vals[gl]))
                if el < mu and elo <= eg - el <= ehi:
                    partners += gl
            if partners:
                cap2 = max(cap2, np.linalg.svd(M[np.ix_(g, partners)], compute_uv=False)[0] ** 2)
        elif eg < mu:
            partners = []
            for gu in groups:
                eu = float(np.mean(vals[gu]))
                if eu > mu and elo <= eu - eg <= ehi:
                    partners += gu
            if partners:
                cap2 = max(cap2, np.linalg.svd(M[np.ix_(partners, g)], compute_uv=False)[0] ** 2)
    return s, cap2


def optical_bound(mu, exact_cross_population, elo, ehi, kmax,
                  nr=160, nmu=10, nphi=16):
    weighted = 0.0
    cap2 = 0.0
    for kk, w in grid(kmax, nr, nmu, nphi):
        s, c2 = optical_point(kk, mu, elo, ehi)
        weighted += w * s
        cap2 = max(cap2, c2)
    cap = math.sqrt(cap2)
    bound = 2.0 * weighted / cap2
    return cap, bound, bound / exact_cross_population


def main():
    print("HgCdTe second-order 8-band tightness test")
    print(f"T = {T_K:.1f} K")
    print(f"Eg = {EG:.9f} eV (10 um target)")
    print(f"Laurenti composition x = {X:.9f}")
    print(f"Delta = {DELTA:.6f} eV, F = {F:.6f}, gamma1 = {G1:.6f}, gamma2 = {G2:.6f}, gamma3 = {G3:.6f}")
    print(f"P/hbar = {P*1e-9/HBAR_EV_S:.3f} m/s")

    mu, ne, nh, ne_cross, nh_cross = carrier_state()
    ncross = ne_cross + nh_cross
    print("\nCarrier state (|k| <= 2.0 nm^-1):")
    print(f"mu - Ev = {mu:.9f} eV")
    print(f"mu - Ec = {(mu-EG)*1e3:.3f} meV")
    print(f"band electron density = {ne:.6e} cm^-3")
    print(f"band hole density     = {nh:.6e} cm^-3")
    print(f"cross-mu upper-state electron density = {ne_cross:.6e} cm^-3")
    print(f"cross-mu lower-state hole density     = {nh_cross:.6e} cm^-3")
    print(f"cross-mu thermal population ne+nh     = {ncross:.6e} cm^-3")
    print(f"conventional electron+hole total      = {ne+nh:.6e} cm^-3")
    print(f"cross/physical total ratio            = {ncross/(ne+nh):.9f}")

    windows = [
        ("Eg..1.5Eg", EG, 1.5 * EG, 0.30),
        ("Eg..2Eg", EG, 2.0 * EG, 0.45),
        ("Eg..3Eg", EG, 3.0 * EG, 0.70),
        ("Eg..0.5eV", EG, 0.50, 1.00),
    ]
    print("\nWindowed theorem test:")
    print("window          vcap(m/s)      n_bound(cm^-3)   bound/exact")
    for name, lo, hi, km in windows:
        cap, bound, ratio = optical_bound(mu, ncross, lo, hi, km)
        print(f"{name:12s} {cap:12.3f}   {bound:14.6e}   {ratio:10.6f}")

    print("\nCarrier k-domain convergence (nr=100,nmu=8,nphi=12):")
    for km in (1.2, 1.5, 1.8, 2.0):
        m, ne_k, nh_k, nex_k, nhx_k = carrier_state(kmax=km, nr=100, nmu=8, nphi=12)
        print(f"kmax={km:3.1f} nm^-1  mu={m:.6f} eV  n_band={ne_k:.6e}  n_cross={nex_k+nhx_k:.6e}")


if __name__ == "__main__":
    main()
