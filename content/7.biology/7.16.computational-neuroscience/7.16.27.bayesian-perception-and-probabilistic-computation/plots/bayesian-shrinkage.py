"""Priors bias perception: the slow-speed prior and central-tendency bias.

A: Gaussian prior on speed N(0, 4^2) deg/s, likelihoods for the same measurement x = 6 deg/s at high
contrast (sd 0.5) and low contrast (sd 2.0), and the posteriors; the low-contrast posterior mean
(4.8) lies closer to zero. B: mean perceived speed (posterior mean) against true speed for the two
contrasts, v_hat = v sigma0^2 / (sigma0^2 + sigma^2); points are means of 3000 simulated trials.
C: interval reproduction. The measurement of a duration t has s.d. 0.1 t (scalar noise); the prior
is uniform over a short range (0.4-0.8 s) or a long range (0.8-1.2 s); the estimate is the posterior
mean on a grid. The estimates regress toward the middle of the prior range, more strongly where the
measurement noise is larger.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
s0 = 4.0
fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.1))

ax = axs[0]
v = np.linspace(-4, 14, 600)
g = lambda m, s: np.exp(-(v - m) ** 2 / (2 * s ** 2)) / (np.sqrt(2 * np.pi) * s)
x = 6.0
ax.plot(v, g(0, s0), color=P.muted(), lw=1.8, label="prior")
for s, c, lab in ((0.5, P.edge("dna"), "high contrast"), (2.0, P.edge("rna"), "low contrast")):
    post_m = x * s0 ** 2 / (s0 ** 2 + s ** 2)
    post_s = np.sqrt(1 / (1 / s ** 2 + 1 / s0 ** 2))
    ax.plot(v, g(x, s), color=c, lw=1.4, ls="--")
    ax.plot(v, g(post_m, post_s), color=c, lw=2.4, label=f"{lab}: posterior (mean {post_m:.1f})")
ax.axvline(x, color=P.ink(), lw=0.6, ls=":")
ax.set_xlabel("Speed / deg s$^{-1}$")
ax.set_ylabel("Density (dashed: likelihoods)")
ax.legend(frameon=False, fontsize=7.5, loc="upper left")
ax.set_title("A  Prior, likelihood, posterior", loc="left", fontsize=10)

ax = axs[1]
vt = np.linspace(0, 10, 100)
ax.plot(vt, vt, color=P.muted(), lw=0.8)
for s, c, lab in ((0.5, P.edge("dna"), "high contrast"), (2.0, P.edge("rna"), "low contrast")):
    ax.plot(vt, vt * s0 ** 2 / (s0 ** 2 + s ** 2), color=c, lw=2, label=lab)
    vp = np.arange(1, 11, 1.5)
    sim = [np.mean((v0 + rng.normal(0, s, 3000)) * s0 ** 2 / (s0 ** 2 + s ** 2)) for v0 in vp]
    ax.plot(vp, sim, "o", color=c, ms=4)
ax.set_xlabel("True speed / deg s$^{-1}$")
ax.set_ylabel("Perceived speed / deg s$^{-1}$")
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_aspect("equal")
ax.set_title("B  Low contrast looks slower", loc="left", fontsize=10)

ax = axs[2]
w = 0.1


def bls(m, lo, hi):
    grid = np.linspace(lo, hi, 600)
    lik = np.exp(-(m[:, None] - grid[None, :]) ** 2 / (2 * (w * grid[None, :]) ** 2)) / (w * grid[None, :])
    return (lik * grid).sum(1) / lik.sum(1)


tt = np.linspace(0.4, 1.2, 9)
ax.plot([0.35, 1.25], [0.35, 1.25], color=P.muted(), lw=0.8)
for (lo, hi), c, lab in (((0.4, 0.8), P.edge("dna"), "short prior (0.4-0.8 s)"), ((0.8, 1.2), P.edge("rna"), "long prior (0.8-1.2 s)")):
    ts = tt[(tt >= lo - 1e-9) & (tt <= hi + 1e-9)]
    est = [np.mean(bls(rng.normal(t, w * t, 1500), lo, hi)) for t in ts]
    ax.plot(ts, est, "o-", color=c, lw=2, ms=4, label=lab)
ax.set_xlabel("Presented interval / s")
ax.set_ylabel("Reproduced interval / s")
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("C  Central tendency", loc="left", fontsize=10)
fig.tight_layout()
