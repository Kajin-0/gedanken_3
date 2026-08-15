# Experiment 12 — Rev3 notation erratum

**Date:** 2026-08-14  
**Scope:** mechanical notation correction only  
**Affected file:** `MANUSCRIPT_REV3_2026-08-14.md`

## Controlling correction

The manuscript's basis-invariant optical-velocity resource is the **Latin** symbol

```math
u_{\mathcal B}
```

No Greek `\nu_{\mathcal B}` variable is defined or intended anywhere in the paper.

The following rendered occurrences in Rev3 are stale LaTeX escape artifacts and must be read as `u_{\mathcal B}`:

1. Abstract hierarchy:

```math
\mathcal R_{\mathcal B}(T)
\le
u_{\mathcal B}^2(n_e+n_h)
```

must read

```math
\mathcal R_{\mathcal B}(T)
\le
u_{\mathcal B}^2(n_e+n_h),
```

where the leading character is Latin `u`.

2. Equation (21), the resource definition:

```math
\boxed{
u_{\mathcal B}^2=\cdots}
```

must read

```math
\boxed{u_{\mathcal B}^2=\cdots}.
```

3. Equation (22):

```math
\mathcal R_{\mathcal B}(T)
\le
u_{\mathcal B}^2(n_e+n_h)
```

must read with Latin `u_{\mathcal B}`.

4. Concluding hierarchy, Eq. (35):

```math
\mathcal R_{\mathcal B}(T)
\le
u_{\mathcal B}^2(n_e+n_h)
```

must read with Latin `u_{\mathcal B}`.

## Scientific effect

None.

The denominator in Theorem 2, all low-energy corollaries, the parabolic and Dirac validations, the 10-um appendix, and the prose already use the intended Latin `u_{\mathcal B}`. No coefficient, inequality direction, numerical value, citation, or claim changes.

## Revision control

Treat `MANUSCRIPT_REV3_2026-08-14.md` **together with this erratum** as the current archival manuscript state. Any next rendered or journal-facing revision must mechanically replace every stale `\nu_{\mathcal B}` token with Latin `u_{\mathcal B}` before typesetting.
