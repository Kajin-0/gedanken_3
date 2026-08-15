import math
import numpy as np

# x-polarized dimensionless velocity matrix M_x from the first-order
# 8x8 Kane Hamiltonian of Malcolm & Nicol, Phys. Rev. B 92, 035118 (2015),
# Eq. (1), with H = hbar v_K M(k) + diagonal band-edge terms.
# Since k_+ = k_x + i k_y and k_- = k_x - i k_y,
# d k_+/d k_x = d k_-/d k_x = 1.

s2 = math.sqrt(2.0)
s3 = math.sqrt(3.0)
Mx = np.zeros((8, 8), dtype=float)
for i, j, a in [
    (0, 1, s3 / 2),
    (1, 2, -1 / 2),
    (1, 3, -1 / s2),
    (4, 6, -1 / s2),
    (5, 6, 1 / 2),
    (6, 7, -s3 / 2),
]:
    Mx[i, j] = Mx[j, i] = a

vals = np.linalg.eigvalsh(Mx)
capacity_factor = np.linalg.norm(Mx, 2)
expected = math.sqrt(3.0 / 2.0)

# Accepted Kane energy used in HgCdTe literature.
e = 1.602176634e-19
m0 = 9.1093837015e-31
E_P_eV = 18.8
E_P = E_P_eV * e
v_from_EP = math.sqrt(E_P / (3.0 * m0))
vcap_from_EP = math.sqrt(E_P / (2.0 * m0))

# Experimentally extracted universal Kane velocity (central value).
vK_meas = 1.07e6
vcap_meas = expected * vK_meas

# Rev6 Appendix-A 10-um/300-K internal-absorptance witness scales exactly
# as 1/(v_B^cap)^2.  The 1e6 m/s row is 9.1495e11 cm^-2.
base_column = 9.1495e11
kane_column = base_column * (1.0e6 / vcap_meas) ** 2

print("eig(Mx) =", np.array2string(vals, precision=12))
print("||Mx||_op =", capacity_factor)
print("sqrt(3/2) =", expected)
print("match =", abs(capacity_factor - expected) < 1e-12)
print(f"E_P = {E_P_eV:.1f} eV -> v_K = {v_from_EP:.6e} m/s")
print(f"E_P = {E_P_eV:.1f} eV -> v_cap = {vcap_from_EP:.6e} m/s")
print(f"v_K = 1.07e6 m/s -> v_cap = {vcap_meas:.6e} m/s")
print(f"10-um internal-90%-absorptance witness -> Sigma_e >= {kane_column:.6e} cm^-2")