"""Neuronal avalanches as a branching process: size and duration distributions near criticality.

Each active unit activates a Poisson(sigma) number of units in the next time bin (branching ratio sigma).
An avalanche starts with one active unit and ends when no unit is active; its size is the total number
of activations and its duration the number of bins. 40000 avalanches per sigma, capped at 10^5
activations (supercritical avalanches that reach the cap are counted separately).
At sigma = 1 the size distribution is a power law P(s) ~ s^(-3/2) and the duration distribution
P(T) ~ T^(-2) (mean-field exponents, as found for avalanches in cortical slices and in vivo);
below 1 they are cut off exponentially, above 1 a fraction of avalanches never end.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
n_av, cap = 40000, 100000


def run(sigma):
    active = np.ones(n_av, dtype=np.int64)
    size = np.ones(n_av, dtype=np.int64)
    dur = np.ones(n_av, dtype=np.int64)
    alive = np.ones(n_av, dtype=bool)
    while alive.any():
        idx = np.nonzero(alive)[0]
        new = rng.poisson(sigma * active[idx])
        active[idx] = new
        size[idx] += new
        ended = (new == 0) | (size[idx] >= cap)
        dur[idx[~ended]] += 1
        alive[idx[ended]] = False
    return size, dur


def logbin(v, vmax):
    edges = np.unique(np.logspace(0, np.log10(vmax), 30).astype(int))
    h, e = np.histogram(v, bins=edges)
    width = np.diff(e)
    c = np.sqrt(e[:-1] * e[1:])
    p = h / (width * len(v))
    return c[h > 0], p[h > 0]


fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.0))
cols = {0.8: P.edge("dna"), 1.0: P.edge("negative"), 1.2: P.edge("protein")}
for sigma in (0.8, 1.0, 1.2):
    s, d = run(sigma)
    fin = s < cap
    frac = 1 - fin.mean()
    lab = f"$\\sigma$ = {sigma:g}" + (f" ({100 * frac:.1f} % runaway)" if frac > 0.001 else "")
    x, p = logbin(s[fin], cap)
    axs[0].loglog(x, p, "o-", ms=3.5, lw=1.2, color=cols[sigma], label=lab)
    x, p = logbin(d[fin], 3000)
    axs[1].loglog(x, p, "o-", ms=3.5, lw=1.2, color=cols[sigma], label=f"$\\sigma$ = {sigma:g}")
xs = np.logspace(0, 5, 10)
axs[0].loglog(xs, 0.4 * xs ** -1.5, "--", color=P.muted(), lw=1.0)
axs[0].text(300, 0.4 * 300 ** -1.5 * 3, "slope $-3/2$", fontsize=8, color=P.muted())
xd = np.logspace(0, 3.3, 10)
axs[1].loglog(xd, 0.6 * xd ** -2.0, "--", color=P.muted(), lw=1.0)
axs[1].text(60, 0.6 * 60 ** -2.0 * 3, "slope $-2$", fontsize=8, color=P.muted())
axs[0].set_xlabel("Avalanche size $s$ (activations)")
axs[0].set_ylabel("$P(s)$")
axs[0].set_title("A  Size distribution", loc="left", fontsize=10)
axs[1].set_xlabel("Avalanche duration $T$ (time bins)")
axs[1].set_ylabel("$P(T)$")
axs[1].set_title("B  Duration distribution", loc="left", fontsize=10)
for a in axs:
    a.legend(frameon=False, fontsize=7.5, loc="lower left")
    a.grid(True, alpha=0.3, which="major")
fig.tight_layout()
