# Step 43 — Short Successful Clusters Are a High-Level Gaussian Discordance Event

**Date:** 2026-08-12 17:02 EDT  
**Status:** DERIVED / SHORT-CLUSTER GAUSSIAN ENVELOPE / NUMERICAL SPECTRAL FLOOR / PARTIAL CERTIFICATE / REFINEMENT / OPEN. Step 42 split the exact false-alarm upper bound into a bounded long-cluster term plus the probability of a successful lower-level excursion cluster shorter than a deterministic duration cutoff `L0`. This step bounds the short-cluster term directly. A successful cluster of duration `<L0` must contain a level-`u` point and a level-`a=u-Delta` boundary point separated by `<L0`; thus it forces a full amplitude-`Delta` change while the process is already near the rare high level. A fine deterministic time net reduces this to a union of highly discordant bivariate-Gaussian events. For the original fast high-band family with `Delta=.15`, `L0=.02`, conservative correlation floor `rho_*=.99980`, and local metric envelope `K_*=2e-4`, the resulting analytic conditional-Gaussian/union bound is `P(C_short>=1) < 3.9e-11`, or `<3.9e-5 alpha` for `alpha=1e-6`. The net-modulus failure probability is astronomically smaller. The probability inequality is analytic; the uniform `rho_*` and `K_*` constants are conservative deterministic floating-point spectral/covariance envelopes rather than formal interval arithmetic. No novelty claim.

---

## 1. Geometry of a short successful cluster

Recall the lower level

```math
a=u-\Delta,
```

and let `I` be one connected component of

```math
\{t\in[0,\ell]:z(t)>a\}.
```

Suppose `I` is successful,

```math
\sup_I z>u,
```

and has duration

```math
|I|<L_0<\ell.
```

Because `I` is shorter than the entire observation window, it cannot touch both endpoints of `[0,ell]`. Therefore at least one boundary point `t_a` of `I` lies in the interior of the observation interval, and continuity gives

```math
z(t_a)=a.
```

Choose `t_u in I` at which the continuous path attains a value above `u`. Then

```math
|t_u-t_a|<L_0
```

and

```math
z(t_u)-z(t_a)>u-a=\Delta.
```

Hence pathwise

```math
\boxed{
\{C_{short}\ge1\}
\subseteq
\left\{\exists s,t:\ |t-s|<L_0,\ z(t)>u,\ z(s)=a\right\}.
}
```

The important point is that the short-cluster event is not merely a large increment somewhere. It is a large increment tied to a rare high-level value near `u~5`.

---

## 2. Deterministic time net

Use

```text
ell      = 0.895
L0       = 0.02
Delta    = 0.15
h        = 1e-5
gamma    = 0.0025.
```

Cover `[0,ell]` by a uniform time net with spacing `h`. Let `G_gamma` be the event that every continuum point differs from a neighboring net point by at most `gamma`.

On `G_gamma`, any short successful cluster produces two net points `i,j` satisfying

```math
|t_i-t_j|\le L_0+2h,
```

```math
z(t_i)\ge U:=u-\gamma,
```

and

```math
z(t_j)\le A:=a+\gamma.
```

Therefore

```math
\boxed{
P(C_{short}\ge1)
\le P(G_\gamma^c)
+N_{pair}\sup_{|r|\le L_0+2h}
P\{X\ge U,Y\le A\},
}
```

where `(X,Y)` is a unit-variance Gaussian pair with correlation equal to the timing covariance at lag `r`.

The net has

```text
N_t = ceil(ell/h)+1 = 89501
```

points. For each possible high point, an upper bound on the number of net points within `L0+2h` on either side is

```text
N_neighbor = 2 ceil((L0+2h)/h)+1 = 4005.
```

Thus

```math
\boxed{
N_{pair}\le 358451505.
}
```

This intentionally counts ordered candidate pairs and is conservative.

---

## 3. Uniform short-lag correlation floor

At the rough endpoint the covariance is the exact finite-window template autocorrelation

```math
R_0(r)
=\frac{\int_0^{X-r}v(v+r)e^{-2v-r}\,dv}
{\int_0^Xv^2e^{-2v}\,dv},
\qquad 0\le r<X.
```

At

```text
X = 7.16
r = L0+2h = 0.02002,
```

direct deterministic evaluation gives

```text
R_0(0.02002) ~= 0.9998009903.
```

Finite Gaussian information weighting suppresses high-frequency timing power. Direct deterministic spectral evaluation over

```text
0 <= q <= 0.0767
```

shows the covariance at this lag is no smaller than the rough endpoint value; representative finite-`q` values are slightly larger.

Retain the rounded conservative working floor

```math
\boxed{\rho_*=0.99980.}
```

**QUALIFICATION:** `rho_*` is a deterministic floating-point envelope, not formal interval arithmetic. The probability argument below is exact conditional on this floor.

---

## 4. Analytic bivariate-Gaussian discordance bound

Let `(X,Y)` be standard normal with correlation `rho>=rho_*>0`. For any `U>0`, condition on `X=x`:

```math
Y\mid X=x
\sim
N\!\left(\rho x,1-\rho^2\right).
```

For `x>=U`,

```math
P(Y\le A\mid X=x)
\le
\Phi\!\left(
\frac{A-\rho U}{\sqrt{1-\rho^2}}
\right).
```

For the present high/low configuration, making `rho` smaller makes the discordant event larger; therefore the conservative floor `rho_*` gives

```math
\boxed{
P(X\ge U,Y\le A)
\le
Q(U)
\Phi\!\left(
\frac{A-\rho_*U}{\sqrt{1-\rho_*^2}}
\right).
}
```

No asymptotic extreme-value approximation enters this inequality.

Use the established endpoint threshold

```text
u ~= 4.95898348
```

and

```text
a = u-Delta ~= 4.80898348.
```

With `gamma=.0025`,

```text
U = 4.95648348
A = 4.81148348.
```

For `rho_*=.99980`,

```text
sqrt(1-rho_*^2) ~= 0.0199990
(A-rho_* U)/sqrt(1-rho_*^2) ~= -7.2008
Q(U) ~= 3.5890e-7
Phi(-7.2008) ~= 2.9931e-13.
```

Hence each candidate pair obeys

```math
\boxed{
P(X\ge U,Y\le A)
\le 1.075\times10^{-19}.
}
```

The ordered-pair union bound is therefore

```math
\boxed{
N_{pair}P_{pair}
<3.86\times10^{-11}.
}
```

For reference only, direct numerical integration of the exact bivariate-normal pair probability is about two orders of magnitude smaller; it is not needed for the certificate.

---

## 5. Net-modulus failure is negligible

It remains to bound `P(G_gamma^c)`.

For one time cell of width `h=1e-5`, direct rough-endpoint covariance evaluation gives

```text
2[1-R_0(h)]/h ~= 1.3383e-4.
```

Finite-band members are smoother at this scale in deterministic spectral checks. Retain the deliberately larger uniform local metric envelope

```math
\boxed{
E[(z(t+s)-z(t))^2]
\le K_*|s|,
\qquad
K_*=2\times10^{-4},
\quad |s|\le h.
}
```

For a cell anchored at one endpoint, Sudakov-Fernique comparison with `sqrt(K_*)B(s)` gives the one-sided expected supremum bound

```math
m_h\le\sqrt{\frac{2K_*h}{\pi}}
\approx3.5683\times10^{-5}.
```

Borell concentration and a union bound over cells and signs yield

```math
P(G_\gamma^c)
\le
2N_t
\exp\!\left[
-\frac{(\gamma-m_h)^2}{2K_*h}
\right].
```

For `gamma=.0025`, the base-10 logarithm of this bound is approximately

```text
log10 P(G_gamma^c) < -654.
```

Thus the continuum-to-grid approximation term is negligible relative to the bivariate-pair term.

Again, the bound is analytic conditional on the conservative numerical metric constant `K_*`.

---

## 6. Short-cluster probability envelope

Combining the pair and modulus terms gives

```math
\boxed{
P(C_{short}\ge1)
<3.9\times10^{-11}
}
```

for the established fast high-band family with

```text
Delta=.15,
L0=.02,
0<=q<=.0767,
```

conditional on the stated conservative covariance/metric floors.

At

```math
\alpha=10^{-6},
```

this is

```math
\boxed{
\frac{P(C_{short}\ge1)}{\alpha}
<3.9\times10^{-5}.
}
```

Thus the short-cluster term consumes less than four hundred-thousandths of the false-alarm budget.

A tighter exact bivariate-normal integration gives an absolute pair-union term of order `5e-13`, but the looser analytic conditional bound already exceeds what is needed.

---

## 7. First nontrivial consequence

Step 42's duration decomposition was

```math
P_{FA}
\le
E[C_{long}]
+P(C_{short}\ge1).
```

For `L0=.02`, this step shows that the second term is negligible on the `alpha=1e-6` scale:

```math
P(C_{short}\ge1)/\alpha<3.9\times10^{-5}.
```

Therefore the short-duration tail that caused the enormous formal inverse-duration range is **not** physically important for the actual false-alarm probability. It is a support-level pathology of the raw importance variable.

The remaining endpoint-statistics problem is now almost entirely the bounded long-cluster mean

```math
E[C_{long}],
```

whose finite-grid Palm contribution has support

```math
0\le Y^{(L_0)}\le m_a/L_0
```

and can be treated with genuine finite-sample concentration once its truncated per-path mean and sample variance are stored.

**REFINEMENT:** no additional short-cluster Monte Carlo is required for the probability budget at `L0=.02`; the next calculation should concentrate resources on the long-cluster estimator.

---

## 8. What remains open

- rerun/store the duration-truncated long-cluster Palm contributions and apply a finite-sample empirical-Bernstein upper confidence bound;
- choose a simultaneous confidence allocation across required high-band node anchors/paired corrections;
- rigorous lower confidence control for the slow `E[C]^2/E[C^2]` ratio;
- formal interval certification of `rho_*`, `K_*`, and the other spectral constants;
- continuum timing-grid bias rather than finite-grid estimator statistics;
- extension to other task parameters and detector models;
- hardware interpretation;
- novelty.

---

## 9. Stopping point

A successful amplitude-`.15` cluster shorter than `.02` is forced into an extraordinarily discordant high-level Gaussian pair. Its probability is negligible compared with `alpha`, so the duration-truncated decomposition has removed the support pathology without introducing a meaningful probability penalty.

### Single natural next question

> With the short-cluster term now negligible, does a dedicated `L0=.02` truncated occupation-Palm run give a rigorous empirical-Bernstein upper confidence bound on `E[C_long]` below the remaining fast endpoint budget?
