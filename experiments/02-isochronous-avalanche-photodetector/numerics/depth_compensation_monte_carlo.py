"""Monte Carlo stress test for Experiment 02.

Toy model only. It compares an ordinary depth-distributed APD timestamp with an
isochronous optical-depth-mapped timestamp using stochastic drift-diffusion
first-passage transport.
"""

import numpy as np

SEED = 20260813
N = 2_000_000

d = 2e-6                 # m
v_c = 1e5                # m/s
v_g = 7.5e7              # m/s
eta = 0.90
sigma_perp = 100e-9      # m RMS unresolved depth
Pe = 100.0
sigma_other = 3e-12      # s RMS avalanche/electronics placeholder

rng = np.random.default_rng(SEED)

L = d * v_g / v_c
b = -np.log(1.0 - eta)
a = b / L
D = v_c * d / Pe

# Detected-photon coordinate for exponential distributed absorption truncated at L.
u = rng.random(N)
x = -np.log(1.0 - u * (1.0 - np.exp(-a * L))) / a

# Designed mean depth map and unresolved transverse absorption coordinate.
z_bar = d * x / L
delta_z = rng.normal(0.0, sigma_perp, N)
z = np.clip(z_bar + delta_z, 0.0, d)
ell = d - z

# First-passage time for dY = v_c dt + sqrt(2D) dW over distance ell.
# The inverse-Gaussian parameters are mean ell/v_c and shape ell^2/(2D).
ell_safe = np.maximum(ell, 1e-12)
mu = ell_safe / v_c
shape = ell_safe**2 / (2.0 * D)
t_transport = rng.wald(mu, shape)
t_transport[ell <= 1e-12] = 0.0

other = rng.normal(0.0, sigma_other, N)

# Baseline: same carrier-depth distribution with no compensating optical delay.
t_base = t_transport + other

# Perfect depth map: x/v_g cancels the designed mean carrier-depth gradient.
t_iso = x / v_g + t_transport + other


def report(name, t):
    t_ps = t * 1e12
    p = np.percentile(t_ps, [1, 10, 50, 90, 99])
    print(name)
    print(f"  mean_ps = {np.mean(t_ps):.6f}")
    print(f"  rms_ps  = {np.std(t_ps):.6f}")
    print(f"  p01,p10,p50,p90,p99 = {p}")
    print(f"  p99-p01_ps = {p[-1] - p[0]:.6f}")


report("baseline", t_base)
report("isochronous", t_iso)
print(f"RMS reduction = {1.0 - np.std(t_iso) / np.std(t_base):.6%}")

# Scale the compensating optical delay. c=0 is baseline; c=1 is analytic match.
print("\ncompensation scan")
for c in np.linspace(0.0, 2.0, 21):
    t = c * x / v_g + t_transport + other
    print(f"c={c:.2f}, rms_ps={np.std(t) * 1e12:.6f}")
