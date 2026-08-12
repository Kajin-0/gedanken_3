#!/usr/bin/env python3
"""Step-33 excursion-cluster moment enclosure.

For a continuous timing scan z(t), choose a finite amplitude gap Delta>0 and
set

    a = u - Delta.

Decompose {t in [0,ell] : z(t)>a} into connected components.  Count a
component as successful if its maximum exceeds u.  Let C_Delta be the number
of successful components.  Then pathwise

    {sup z > u} == {C_Delta >= 1},

so

    E[C]^2 / E[C^2] <= P_FA <= E[C].

The first two cluster moments are estimated under a lower-level occupation-Palm
measure.  Choose T uniformly in [0,ell] and condition on z(T)>a.  If L is the
duration of the selected lower-level component, S indicates whether that
component is successful, and C is the total successful-component count, then

    E[C]   = ell Q(a) E_a[S/L]
    E[C^2] = ell Q(a) E_a[S C/L].

This avoids direct simulation of a ~1e-6 event and remains meaningful at the
rough kappa=infinity endpoint because no derivative/upcrossing count is used.

The implementation is still numerical: finite FFT period, finite timing grid,
Monte Carlo path count, and sampled-max classification remain.  It is not
formal interval arithmetic.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np
from scipy.stats import norm


RHO_FULL = 6.2407571
BETA = 0.90
ALPHA = 1.0e-6


def eta(x: float) -> float:
    return 1.0 - math.exp(-2.0 * x) * (1.0 + 2.0 * x + 2.0 * x * x)


def H_x(omega: np.ndarray, x: float) -> np.ndarray:
    z = 1.0 + 1j * omega
    return (1.0 - np.exp(-z * x) * (1.0 + z * x)) / (z * z)


def finite_rho(x: float, kappa: float, d_omega: float = 0.05) -> float:
    if math.isinf(kappa):
        return RHO_FULL * math.sqrt(eta(x))
    upper = max(30.0, 6.0 * kappa)
    n = int(math.ceil(upper / d_omega)) + 1
    omega = np.linspace(0.0, upper, n)
    density = np.abs(H_x(omega, x)) ** 2 * np.exp(-(omega / kappa) ** 2)
    i0 = 2.0 * float(np.trapezoid(density, omega))
    return RHO_FULL * math.sqrt(i0 / (math.pi / 2.0))


@dataclass
class PeriodicModel:
    delta: float
    period: float
    sqrt_eig: np.ndarray
    covariance: np.ndarray


def build_model(
    *,
    x: float,
    kappa: float,
    delta: float,
    period_target: float,
) -> PeriodicModel:
    nfft = 1
    while nfft * delta < period_target:
        nfft *= 2

    omega = 2.0 * math.pi * np.fft.fftfreq(nfft, d=delta)
    eig = np.abs(H_x(omega, x)) ** 2
    if not math.isinf(kappa):
        eig *= np.exp(-(omega / kappa) ** 2)
    eig /= eig.mean()

    return PeriodicModel(
        delta=delta,
        period=nfft * delta,
        sqrt_eig=np.sqrt(eig),
        covariance=np.fft.ifft(eig).real,
    )


def component_duration(
    segment: np.ndarray,
    start: int,
    end: int,
    *,
    level: float,
    delta: float,
) -> float:
    """Linearly interpolate lower-level crossing times at component edges."""
    n = len(segment) - 1

    if start == 0:
        t_left = 0.0
    else:
        z0 = float(segment[start - 1])
        z1 = float(segment[start])
        denom = z1 - z0
        frac = (level - z0) / denom if denom != 0.0 else 1.0
        frac = min(max(frac, 0.0), 1.0)
        t_left = (start - 1 + frac) * delta

    if end == n:
        t_right = n * delta
    else:
        z0 = float(segment[end])
        z1 = float(segment[end + 1])
        denom = z0 - z1
        frac = (z0 - level) / denom if denom != 0.0 else 1.0
        frac = min(max(frac, 0.0), 1.0)
        t_right = (end + frac) * delta

    return max(t_right - t_left, 0.5 * delta)


def cluster_moment_enclosure(
    *,
    x: float,
    ell: float,
    kappa: float,
    u: float,
    amplitude_gap: float,
    target_delta: float,
    period_target: float,
    n_paths: int,
    batch_size: int,
    seed: int,
) -> dict[str, float]:
    if amplitude_gap <= 0.0:
        raise ValueError("amplitude_gap must be positive")
    if ell <= 0.0 or target_delta <= 0.0:
        raise ValueError("ell and target_delta must be positive")

    a = u - amplitude_gap
    q_a = float(norm.sf(a))
    m_a = ell * q_a

    n_intervals = max(20, int(round(ell / target_delta)))
    delta = ell / n_intervals
    model = build_model(
        x=x,
        kappa=kappa,
        delta=delta,
        period_target=period_target,
    )

    nfft = len(model.sqrt_eig)
    offsets = np.arange(-n_intervals, n_intervals + 1)
    idx = offsets % nfft
    covariance = model.covariance[idx]

    rng = np.random.default_rng(seed)
    sum_g1 = 0.0
    sum_g2 = 0.0
    sum_g1_sq = 0.0
    sum_g2_sq = 0.0
    sum_g1g2 = 0.0
    selected_successes = 0
    selected_multi_success = 0

    for start_path in range(0, n_paths, batch_size):
        b = min(batch_size, n_paths - start_path)

        white = rng.standard_normal((b, nfft))
        process = np.fft.ifft(
            np.fft.fft(white, axis=1) * model.sqrt_eig[None, :],
            axis=1,
        ).real

        # If Y~N(0,1) conditioned on Y>a, then Q(Y)=U Q(a).
        y_cond = norm.isf(rng.random(b) * q_a)
        local = (
            process[:, idx]
            + covariance[None, :] * (y_cond - process[:, 0])[:, None]
        )

        selected = rng.integers(0, n_intervals + 1, size=b)

        for j in range(b):
            m = int(selected[j])
            left = n_intervals - m
            segment = local[j, left : left + n_intervals + 1]
            above = segment > a

            if not above[m]:
                # Should not occur except for severe numerical pathology because the
                # selected point is conditioned to lie above a.
                continue

            starts = np.where(above & np.r_[True, ~above[:-1]])[0]
            ends = np.where(above & np.r_[~above[1:], True])[0]

            C = 0
            selected_success = False
            selected_length = None

            for s, e in zip(starts, ends):
                success = bool(np.max(segment[s : e + 1]) > u)
                if success:
                    C += 1

                if s <= m <= e:
                    selected_success = success
                    selected_length = component_duration(
                        segment,
                        int(s),
                        int(e),
                        level=a,
                        delta=delta,
                    )

            if selected_length is None:
                continue

            if selected_success:
                g1 = 1.0 / selected_length
                g2 = C / selected_length
                selected_successes += 1
                selected_multi_success += int(C > 1)
            else:
                g1 = 0.0
                g2 = 0.0

            sum_g1 += g1
            sum_g2 += g2
            sum_g1_sq += g1 * g1
            sum_g2_sq += g2 * g2
            sum_g1g2 += g1 * g2

    n = float(n_paths)
    mean_g1 = sum_g1 / n
    mean_g2 = sum_g2 / n

    E_C = m_a * mean_g1
    E_C2 = m_a * mean_g2
    lower = E_C * E_C / E_C2 if E_C2 > 0.0 else 0.0
    upper = E_C

    var_g1 = max((sum_g1_sq - n * mean_g1 * mean_g1) / (n - 1.0), 0.0)
    var_g2 = max((sum_g2_sq - n * mean_g2 * mean_g2) / (n - 1.0), 0.0)
    cov_g12 = (sum_g1g2 - n * mean_g1 * mean_g2) / (n - 1.0)

    se_E_C = m_a * math.sqrt(var_g1 / n)

    # Delta-method MC uncertainty for the lower moment ratio.
    if mean_g2 > 0.0:
        d1 = m_a * 2.0 * mean_g1 / mean_g2
        d2 = -m_a * mean_g1 * mean_g1 / (mean_g2 * mean_g2)
        var_lower = (
            d1 * d1 * var_g1
            + d2 * d2 * var_g2
            + 2.0 * d1 * d2 * cov_g12
        ) / n
        se_lower = math.sqrt(max(var_lower, 0.0))
    else:
        se_lower = 0.0

    success_fraction = selected_successes / n_paths
    multi_fraction = (
        selected_multi_success / selected_successes if selected_successes else 0.0
    )

    return {
        "a": a,
        "Q_a": q_a,
        "occupation_normalizer": m_a,
        "E_C": E_C,
        "E_C2": E_C2,
        "PFA_lower": lower,
        "PFA_upper": upper,
        "SE_E_C": se_E_C,
        "SE_PFA_lower_delta": se_lower,
        "selected_success_fraction": success_fraction,
        "selected_multi_success_fraction": multi_fraction,
        "delta": delta,
        "period": model.period,
        "n_paths": float(n_paths),
    }


def detector_cluster_bounds(
    *,
    kappa_fast: float,
    X: float,
    Lambda: float,
    amplitude_gap: float,
    target_delta: float,
    period_target: float,
    n_paths: int,
    batch_size: int,
    seed: int,
) -> tuple[dict[str, float], dict[str, float]]:
    r = 2.0
    z_beta = float(norm.ppf(BETA))

    kf = kappa_fast
    ks = math.inf if math.isinf(kf) else r * kf

    x_f = X
    x_s = X / r
    ell_f = Lambda
    ell_s = Lambda / r

    u_f = finite_rho(x_f, kf) - z_beta
    u_s = finite_rho(x_s, ks) - z_beta

    fast = cluster_moment_enclosure(
        x=x_f,
        ell=ell_f,
        kappa=kf,
        u=u_f,
        amplitude_gap=amplitude_gap,
        target_delta=target_delta,
        period_target=period_target,
        n_paths=n_paths,
        batch_size=batch_size,
        seed=seed,
    )
    slow = cluster_moment_enclosure(
        x=x_s,
        ell=ell_s,
        kappa=ks,
        u=u_s,
        amplitude_gap=amplitude_gap,
        target_delta=target_delta,
        period_target=period_target,
        n_paths=n_paths,
        batch_size=batch_size,
        seed=seed + 1,
    )

    fast["u"] = u_f
    slow["u"] = u_s
    return fast, slow


def parse_kappa(text: str) -> float:
    return math.inf if text.strip().lower() in {"inf", "infinity"} else float(text)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--kappas", default="300,1000,inf")
    p.add_argument("--X", type=float, default=7.16)
    p.add_argument("--Lambda", type=float, default=0.895)
    p.add_argument("--gap", type=float, default=0.15)
    p.add_argument("--delta", type=float, default=0.001)
    p.add_argument("--period", type=float, default=16.0)
    p.add_argument("--paths", type=int, default=10000)
    p.add_argument("--batch", type=int, default=25)
    p.add_argument("--seed", type=int, default=20260811)
    args = p.parse_args()

    kappas = [parse_kappa(x) for x in args.kappas.split(",") if x.strip()]

    print("Excursion-cluster finite-u moment enclosure")
    print(
        f"X={args.X}, Lambda={args.Lambda}, gap={args.gap}, "
        f"alpha={ALPHA}, paths={args.paths}"
    )
    print(
        "kappa_f detector lower/alpha upper/alpha SE_upper/alpha "
        "SE_lower/alpha multi_success"
    )

    for i, kappa in enumerate(kappas):
        fast, slow = detector_cluster_bounds(
            kappa_fast=kappa,
            X=args.X,
            Lambda=args.Lambda,
            amplitude_gap=args.gap,
            target_delta=args.delta,
            period_target=args.period,
            n_paths=args.paths,
            batch_size=args.batch,
            seed=args.seed + 100 * i,
        )

        label = "inf" if math.isinf(kappa) else f"{kappa:g}"
        for name, result in (("fast", fast), ("slow", slow)):
            print(
                f"{label:>7s} {name:>8s} "
                f"{result['PFA_lower']/ALPHA:11.6f} "
                f"{result['PFA_upper']/ALPHA:11.6f} "
                f"{result['SE_E_C']/ALPHA:11.6f} "
                f"{result['SE_PFA_lower_delta']/ALPHA:11.6f} "
                f"{result['selected_multi_success_fraction']:11.6f}"
            )

    print(
        "\nInterpretation: if fast PFA_upper < alpha < slow PFA_lower "
        "at the same X, the cluster moment enclosure separates the detector "
        "decision times without raw micro-upcrossing counts."
    )
    print(
        "NOTE: inequalities are exact for the continuum cluster count; displayed "
        "moments are finite-grid Monte Carlo estimates, not formal interval bounds."
    )


if __name__ == "__main__":
    main()
