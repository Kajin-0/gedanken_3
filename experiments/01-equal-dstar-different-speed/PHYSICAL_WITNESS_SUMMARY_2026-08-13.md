# First-order physical witness

Date: 2026-08-13

Use one common unit-area exponential optical pulse p(t)=tau_p^-1 exp(-t/tau_p)u(t) and two ordinary first-order detectors G_j(s)=R_j/(1+s tau_j).

Take tau_p=tau_f and tau_s=10 tau_f. With the same additive downstream white-noise PSD N in both channels,

rho_j,infinity^2 = R_j^2/[2 N (tau_p+tau_j)].

Equal eventual SNR therefore requires

R_s/R_f = sqrt(11/2) = 2.34520787991.

Over this pair, R_dc proportional tau^g with g=0.370181344747. Normalize the common event strength so both eventual matched-filter SNRs are rho0=3.5.

For alpha=.05 and beta=.90, the exact known-arrival guarantee times are

T_G,f(0)=1.80519795247 tau_f,
T_G,s(0)=7.53280266002 tau_f.

Thus fast is strongly preferred at known arrival.

The normalized full-template covariance is

R_j(Delta)=[tau_p exp(-|Delta|/tau_p)-tau_j exp(-|Delta|/tau_j)]/(tau_p-tau_j).

For the fast channel tau_p=tau_f, so

R_f(Delta)=(1+|Delta|/tau_f) exp(-|Delta|/tau_f),

exactly the smooth covariance used in Paper A, now produced by a common finite optical pulse followed by a standard first-order detector.

At rho0=3.5, alpha=.05, beta=.90, c=2.21844843445540. Choose L=7.5 tau_f.

For the slow channel, -R_s''(0)=1/(10 tau_f^2). Rice plus the initial-point union bound gives

P_FA,s <= 0.0454867946313 < .05.

For the fast channel, use six points separated by 1.5 tau_f. Every distinct-pair covariance is at most epsilon=R_f(1.5 tau_f)=0.557825400371075. Slepian comparison with six equicorrelated Gaussians gives

P_FA,f >= 0.0561848873819 > .05.

Therefore

P_FA,s <= .0454868 < .05 < .0561849 <= P_FA,f.

The slow channel is full-template guarantee-feasible while the fast channel is not at the same finite physical arrival uncertainty. Together with the known-arrival ordering and ordinary first-crossing continuity, this yields at least one finite fast-to-slow sufficient-guarantee-time crossover.

This reproduces the central Paper-A phenomenon with one common finite optical event, ordinary first-order detectors, one common downstream white-noise level, one responsivity-versus-response-time law, and exactly equal eventual matched-filter SNR. There is no event-matched detector zero or pole-zero cancellation.

This is a candidate replacement for the original Paper-A construction and should be adversarially audited before changing the manuscript.