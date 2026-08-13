#!/usr/bin/env python3
import math

# Existing Experiment-02 benchmark
D_UM = 2.0
V_C = 5.0e4
V_G = 7.5e7
T0_PS = 40.0
PE = 100.0
B = math.log(10.0)
A = 1.0/B**2 - math.exp(B)/(math.exp(B)-1.0)**2

# Previously retained common stochastic terms
SIGMA_AV_PS = 5.0
SIGMA_ELEC_PS = 2.0
SIGMA_OPT_PS = 1.0
F_COMMON = (SIGMA_AV_PS/T0_PS)**2 + (SIGMA_ELEC_PS/T0_PS)**2 + (SIGMA_OPT_PS/T0_PS)**2

# Historical direct control used throughout Experiment 02
SIGMA_LOCAL_OLD_UM = 0.100
F_OLD = F_COMMON + (SIGMA_LOCAL_OLD_UM/D_UM)**2 + 1.353633258/PE
DIRECT_PS = T0_PS * math.sqrt(F_OLD + A)
TARGET30_PS = 0.70 * DIRECT_PS


def fixed_sheet(sheet_um, length_um, interface_ps=0.0):
    """Fixed shallow absorber adjacent to multiplication region.

    Uniform absorption through sheet thickness; mean carrier path is sheet/2.
    No electrical velocity compensation is assumed. Longitudinal optical delay
    therefore enters conservatively as (L/vg)^2 Var(U).
    """
    sigma_z_um = sheet_um / math.sqrt(12.0)
    mean_path_over_d = (sheet_um/2.0) / D_UM
    f_local = (sigma_z_um/D_UM)**2
    f_diff = 2.0 * mean_path_over_d / PE
    tx_ps = (length_um*1e-6 / V_G) * 1e12
    f_long = A * (tx_ps/T0_PS)**2
    f_int = (interface_ps/T0_PS)**2
    f = F_COMMON + f_local + f_diff + f_long + f_int
    return T0_PS * math.sqrt(f)


def max_length_for_30(sheet_um, interface_ps=0.0):
    lo, hi = 0.0, 10000.0
    for _ in range(100):
        mid = 0.5*(lo+hi)
        if fixed_sheet(sheet_um, mid, interface_ps) <= TARGET30_PS:
            lo = mid
        else:
            hi = mid
    return lo

print('A Var(U) =', A)
print('historical direct RMS ps =', DIRECT_PS)
print('30% gate ps =', TARGET30_PS)
print('\nFixed 200-nm absorber, no electrical velocity matching:')
for L in (10,20,40,100,1000,3000):
    s = fixed_sheet(0.200, L)
    print(f'L={L:4d} um  RMS={s:.6f} ps  improvement={100*(1-s/DIRECT_PS):.3f}%')

Lmax = max_length_for_30(0.200)
print('\nmax length retaining >=30% improvement =', Lmax, 'um')

s40 = fixed_sheet(0.200, 40)
int_budget = math.sqrt(max(0.0, TARGET30_PS**2 - s40**2))
print('40-um baseline RMS =', s40, 'ps')
print('extra independent interface/readout budget to 30% gate =', int_budget, 'ps RMS')

print('\nSheet-thickness sweep at L=40 um:')
for t in (0.100,0.200,0.300,0.400,0.600):
    s = fixed_sheet(t,40)
    print(f't={t:.3f} um  RMS={s:.6f} ps  improvement={100*(1-s/DIRECT_PS):.3f}%')

# Conservative fixed-depth dielectric-mode comparator: 198.4-nm absorption RMS,
# mean carrier path 0.2 um, 40-um optical length.
def fixed_mode(sigma_z_um=0.1984, mean_path_um=0.200, length_um=40.0):
    f_local=(sigma_z_um/D_UM)**2
    f_diff=2.0*(mean_path_um/D_UM)/PE
    tx_ps=(length_um*1e-6/V_G)*1e12
    f_long=A*(tx_ps/T0_PS)**2
    return T0_PS*math.sqrt(F_COMMON+f_local+f_diff+f_long)

sm = fixed_mode()
print('\nfixed-depth 198.4-nm-RMS mode, mean path 0.2 um, L=40 um:')
print('RMS =',sm,'ps; improvement =',100*(1-sm/DIRECT_PS),'%')
