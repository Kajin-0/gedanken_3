# Feasibility scale

At exact path-dilation compensation,

```math
sin(theta*)=v_c/v_g,
```

and the required optical path across absorber depth `d` is

```math
S*=d v_g/v_c.
```

The deterministic timestamp is then `d/v_c` for every absorption depth.

Illustrative assumptions:

```text
d=2 um, v_c=1e5 m/s, v_g=7.5e7 m/s
```

give

```text
theta*=0.0764 deg
S*=1.50 mm
common deterministic delay=20 ps
```

For useful modal absorption coefficient `a`, total absorption is

```math
eta=1-exp(-a S*),
```

so

```math
a=-(v_c/(d v_g)) ln(1-eta).
```

The illustrative device requires about 15.35 1/cm modal absorption for 90% absorption or 30.70 1/cm for 99%.

For a conventional truncated exponential depth distribution over the same `d`, the simple constant-velocity absorption-depth jitter is about 5.1 ps RMS at 90% absorption for the assumed `v_c`.

Thus this concept is aimed at removing a several-picosecond position term in an already-fast detector. It is not expected to remove avalanche, diffusion, or electronics jitter.