"""Quantal statistics at a central synapse with few release sites (binomial model).

The number of released vesicles is K ~ Bin(N, p); each vesicle adds a quantal current of mean q
with coefficient of variation CV_q (Gaussian). Parameters: N = 6 sites, q = 10 pA, CV_q = 0.25.
A: amplitude histograms of 600 simulated trials at p = 0.15, 0.45 and 0.8, with the binomial
mixture density (failures drawn as the bar at 0, recording noise 1.5 pA).
B: multiple-probability fluctuation (variance-mean) analysis. Each point is the mean and variance
of 200 simulated trials at one release probability; the parabola fitted through the origin,
sigma^2 = q' mu - mu^2 / N with q' = q (1 + CV_q^2), recovers q and N.
"""
import matplotlib.pyplot as plt
import numpy as np
from math import comb

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
N, q, cvq, noise = 6, 10.0, 0.25, 1.5


def trials(p, n):
    k = rng.binomial(N, p, size=n)
    amp = np.array([rng.normal(q, cvq * q, size=kk).sum() for kk in k])
    return amp + rng.normal(0, noise, size=n)


fig, axs = plt.subplots(1, 2, figsize=(11, 4.0), gridspec_kw={"width_ratios": [1.25, 1]})

ax = axs[0]
x = np.linspace(-5, 70, 600)
cols = [P.edge("dna"), P.edge("protein"), P.edge("negative")]
for p, c in zip((0.15, 0.45, 0.8), cols):
    a = trials(p, 600)
    ax.hist(a, bins=np.arange(-5, 70, 1.5), histtype="step", color=c, lw=1.0, alpha=0.9)
    dens = np.zeros_like(x)
    for k in range(N + 1):
        w = comb(N, k) * p**k * (1 - p) ** (N - k)
        s = np.sqrt(k * (cvq * q) ** 2 + noise**2)
        dens += w * np.exp(-0.5 * ((x - k * q) / s) ** 2) / (s * np.sqrt(2 * np.pi))
    ax.plot(x, dens * 600 * 1.5, color=c, lw=2.0, label=f"p = {p}  (mean {N * p * q:.0f} pA)")
for k in range(N + 1):
    ax.axvline(k * q, color=P.muted(), lw=0.6, ls=":")
ax.set_xlabel("EPSC amplitude / pA")
ax.set_ylabel("Number of trials")
ax.set_title("A  Amplitude distributions, N = 6, q = 10 pA", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8)
ax.set_xlim(-5, 70)

ax = axs[1]
ps = np.array([0.05, 0.12, 0.2, 0.3, 0.42, 0.55, 0.68, 0.8, 0.9])
mus, vs = [], []
for p in ps:
    a = trials(p, 200)
    mus.append(a.mean())
    vs.append(a.var(ddof=1) - noise**2)
mus, vs = np.array(mus), np.array(vs)
# least squares fit of v = a mu + b mu^2 (through the origin)
A = np.column_stack([mus, mus**2])
(a1, b1), *_ = np.linalg.lstsq(A, vs, rcond=None)
qhat, Nhat = a1 / (1 + cvq**2), -1 / b1
m = np.linspace(0, N * q, 200)
ax.plot(m, q * (1 + cvq**2) * m - m**2 / N, color=P.muted(), lw=1.2, ls="--", label="true parabola")
ax.plot(m, a1 * m + b1 * m**2, color=P.edge("positive"), lw=2.0, label="fit")
ax.scatter(mus, vs, s=22, color=P.edge("dna"), zorder=5, label="simulated (200 trials each)")
ax.annotate("initial slope = q (1 + CV$_q^2$)", xy=(8, 8 * a1), xytext=(18, 50),
            fontsize=8, color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.8))
ax.text(0.97, 0.97, f"fit: q = {qhat:.1f} pA, N = {Nhat:.1f}\n(true: q = {q:.0f} pA, N = {N})",
        transform=ax.transAxes, ha="right", va="top", fontsize=8, color=P.ink())
ax.set_xlabel("Mean amplitude $\\mu$ / pA")
ax.set_ylabel("Variance $\\sigma^2$ / pA$^2$")
ax.set_title("B  Variance-mean analysis", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="lower center")
ax.set_xlim(0, 62)
ax.set_ylim(0, None)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
