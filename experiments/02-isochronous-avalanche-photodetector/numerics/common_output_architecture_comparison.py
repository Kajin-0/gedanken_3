import math

T0_ps = 40.0
A = 0.06515490689
D3 = 0.0089928
D4 = 0.0051232
F_total = 0.03478633258   # includes 2 ps electronics from prior surrogate
F_e_2ps = (2.0 / T0_ps) ** 2
F_phys = F_total - F_e_2ps
sigma_direct_ps = 12.6454
sigma_target30_ps = 0.70 * sigma_direct_ps
L0_mm = 3.0
b = math.log(10.0)
Cprime_fF_per_mm_w1um = 57.5522207832


def readout_budget_ps(D):
    base = T0_ps * math.sqrt(F_phys + D)
    return base, math.sqrt(max(0.0, sigma_target30_ps**2 - base**2))


def reverse_det_var_near_end(D, r):
    # r = v_e / v_g.  Near-end electrical readout.
    c = (1.0 - r) / (1.0 + r)
    return c*c*D + (c - 1.0)**2 * (A - D)


def forward_det_var_with_slope(D, k):
    # Fixed centroid depth ladder Q=E[U|section], total propagation coefficient k.
    return k*k*D + (k - 1.0)**2 * (A - D)


print('READOUT BUDGETS FOR HISTORICAL 30% GATE')
for label, D in [('N=3', D3), ('N=4', D4), ('continuous', 0.0)]:
    base, budget = readout_budget_ps(D)
    print(f'{label:10s} no-readout RMS={base:7.4f} ps  max combined readout RMS={budget:7.4f} ps')

print('\nNEAR-END TRAVELING-WAVE COMMON OUTPUT, N=3')
print('r=ve/vg  L(mm)  section(mm)  alpha90(/mm)  reverse_RMS(ps)  lumped-equiv-C(fF)')
for r in [0.5, 1.0, 1.5, 2.0, 4.0, 10.0, 1e9]:
    L = L0_mm * r / (1.0 + r)
    Drev = reverse_det_var_near_end(D3, r)
    sigma_rev = T0_ps * math.sqrt(F_total + Drev)
    C = Cprime_fF_per_mm_w1um * L
    print(f'{r:7.2g} {L:7.4f} {L/3:11.4f} {b/L:13.4f} {sigma_rev:16.4f} {C:20.2f}')

print('\nFINITE-LADDER PROPAGATION-SLOPE OPTIMA')
for label, D in [('N=3', D3), ('N=4', D4)]:
    kstar = 1.0 - D / A
    s_iso = T0_ps * math.sqrt(F_total + forward_det_var_with_slope(D, 1.0))
    s_opt = T0_ps * math.sqrt(F_total + forward_det_var_with_slope(D, kstar))
    print(f'{label}: k_iso=1, k_RMS={kstar:.6f}, RMS_iso={s_iso:.4f} ps, RMS_opt={s_opt:.4f} ps')

# N=3 total propagation coefficient range preserving the historical 30% target.
Vtarget = (sigma_target30_ps / T0_ps)**2 - F_total
# A*k^2 - 2(A-D)k + (A-D) - Vtarget = 0
qa = A
qb = -2.0 * (A - D3)
qc = (A - D3) - Vtarget
disc = qb*qb - 4*qa*qc
klo = (-qb - math.sqrt(disc)) / (2*qa)
khi = (-qb + math.sqrt(disc)) / (2*qa)
print(f'\nN=3 matched-ladder total propagation coefficient for >=30% gate: {klo:.6f} <= k <= {khi:.6f}')
