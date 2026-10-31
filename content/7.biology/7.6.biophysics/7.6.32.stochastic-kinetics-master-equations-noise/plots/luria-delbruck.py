"""The Luria-Delbrueck distribution from its generating function G(z) = exp[m (1 - z)/z ln(1 - z)]
(Lea-Coulson model in the limit of a large final culture). A: the exact probabilities from the
recursion p_0 = e^-m, p_r = (m/r) sum_k p_k/(r - k + 1) for m = 1 and 4 (lines) and from 10^5
simulated cultures (points), in which each of a Poisson(m) number of mutations founds a clone of
geometric size with success probability x drawn uniformly from (0, 1), as derived in the text; the
dashed lines are the asymptote m/r^2 and the Poisson distribution with mean m, which the induced
hypothesis would predict for comparable numbers. B: the probability of at least r mutants and the
heavy tail m/r: rare jackpots make the sample mean useless as an estimator."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(6)
R = 3000


def ld(m):
    p = np.zeros(R)
    p[0] = np.exp(-m)
    for r in range(1, R):
        k = np.arange(r)
        p[r] = m / r * np.sum(p[:r] / (r - k + 1))
    return p


def simulate(m, cultures):
    out = np.zeros(cultures, int)
    nm = rng.poisson(m, cultures)
    for i in range(cultures):
        if nm[i]:
            x = rng.random(nm[i])
            out[i] = rng.geometric(x).sum()
    return out


fig, axs = plt.subplots(1, 2, figsize=(9.0, 3.4))
fig.subplots_adjust(wspace=0.28, left=0.08, right=0.98, bottom=0.17, top=0.88)
r = np.arange(R)
for m, tok in ((1.0, "dna"), (4.0, "blood")):
    p = ld(m)
    sim = simulate(m, 100000)
    cnt = np.bincount(sim, minlength=R)[:R] / sim.size
    ax = axs[0]
    ax.plot(r[1:], p[1:], color=charts.line(tok), lw=1.4, label=f"m = {m:g}")
    sel = np.unique(np.round(np.logspace(0, 2.7, 25)).astype(int))
    ax.plot(sel, cnt[sel], "o", ms=3, color=charts.line(tok))
    ax.plot(r[10:], m / r[10:] ** 2, color=charts.line(tok), lw=0.8, ls="--")
    ax.plot(r[1:30], stats.poisson.pmf(r[1:30], m), color=charts.line(tok), lw=0.8, ls=":")
    ax = axs[1]
    surv = 1 - np.cumsum(p) + p
    ax.plot(r[1:], surv[1:], color=charts.line(tok), lw=1.4, label=f"m = {m:g}")
    ax.plot(r[10:], m / r[10:], color=charts.line(tok), lw=0.8, ls="--")
ax = axs[0]
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_ylim(1e-7, 1)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink())
ax.text(150, 3e-3, r"$m/r^2$", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.text(12, 2e-6, "Poisson", fontsize=bio.core.FONT["tiny"], color=P.ink())
charts.style_axes(ax, "mutants per culture r", "probability")
charts.title(ax, "A  Exact distribution and simulation")
ax = axs[1]
ax.set_xscale("log")
ax.set_yscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink())
ax.text(200, 0.04, r"$m/r$", fontsize=bio.core.FONT["tiny"], color=P.ink())
charts.style_axes(ax, "r", r"$\mathbb{P}(R \geq r)$")
charts.title(ax, "B  Heavy tail")
