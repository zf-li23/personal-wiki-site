"""Why walking beats pointing. The same alignment rule (take the mean direction of the neighbors
within distance 1, including oneself, and add a random angle uniform in [-eta/2, eta/2], here
eta = 2.8) applied to agents fixed on a square lattice ("pointing", four nearest neighbors) and to
agents that move at speed 2 in the direction they point (the Vicsek model at density 1.6, about
five agents within range, as on the lattice). A: the polar order parameter Psi = |mean of the unit
vectors| in the stationary state against the number of agents N: for fixed agents it decreases
steadily with system size, as the Mermin-Wagner argument predicts (no true long-range order in two
dimensions), while for moving agents it stays high. B: snapshot of the directions of fixed agents
on a 48 x 48 lattice (colour = angle, cyclic): patches of similar direction that wander, on a
background of strong local noise. Each point
averages the second half of a run of 3000 (fixed) or 1500 (moving) updates."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import cKDTree
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(12)
eta = 2.8


def lattice(n, steps=3000):
    th = np.zeros((n, n)) + 0.3 * rng.standard_normal((n, n))
    psi = []
    for s in range(steps):
        c = np.cos(th)
        si = np.sin(th)
        cs = c + np.roll(c, 1, 0) + np.roll(c, -1, 0) + np.roll(c, 1, 1) + np.roll(c, -1, 1)
        ss = si + np.roll(si, 1, 0) + np.roll(si, -1, 0) + np.roll(si, 1, 1) + np.roll(si, -1, 1)
        th = np.arctan2(ss, cs) + eta * (rng.random((n, n)) - 0.5)
        if s >= steps // 2:
            psi.append(np.hypot(np.cos(th).mean(), np.sin(th).mean()))
    return np.mean(psi), th


def moving(N, rho=1.6, v0=2.0, steps=1500):
    L = np.sqrt(N / rho)
    x = rng.uniform(0, L, (N, 2))
    th = 0.3 * rng.standard_normal(N)
    psi = []
    for s in range(steps):
        pr = cKDTree(x, boxsize=L).query_pairs(1.0, output_type="ndarray")
        co, sn = np.cos(th), np.sin(th)
        c = co + np.bincount(pr[:, 0], co[pr[:, 1]], N) + np.bincount(pr[:, 1], co[pr[:, 0]], N)
        si = sn + np.bincount(pr[:, 0], sn[pr[:, 1]], N) + np.bincount(pr[:, 1], sn[pr[:, 0]], N)
        th = np.arctan2(si, c) + eta * (rng.random(N) - 0.5)
        x = (x + v0 * np.column_stack((np.cos(th), np.sin(th)))) % L
        x[x >= L] = 0.0
        if s >= steps // 2:
            psi.append(np.hypot(np.cos(th).mean(), np.sin(th).mean()))
    return np.mean(psi)


fig, axs = plt.subplots(1, 2, figsize=(9.0, 3.6), gridspec_kw=dict(width_ratios=(1.3, 1)))
fig.subplots_adjust(wspace=0.3, left=0.08, right=0.97, bottom=0.15, top=0.89)
ax = axs[0]
sides = [8, 16, 32, 64]
ax.semilogx([s * s for s in sides], [lattice(s)[0] for s in sides], "s-", color=charts.line("neutral"),
            ms=4, lw=1.1, label="fixed agents (pointing)")
Ns = [64, 256, 1024, 2048]
ax.semilogx(Ns, [moving(N) for N in Ns], "o-", color=charts.line("bacterium"), ms=4, lw=1.1,
            label="moving agents (walking)")
ax.set_ylim(0, 1)
ax.legend(frameon=False, fontsize=7, loc="lower left")
charts.style_axes(ax, "number of agents N", r"order parameter $\Psi$")
charts.title(ax, "A  order against system size")

ax = axs[1]
_, th = lattice(48)
ax.imshow(np.mod(th, 2 * np.pi), cmap="twilight", interpolation="nearest", vmin=0, vmax=2 * np.pi)
ax.set_xticks([])
ax.set_yticks([])
charts.style_axes(ax, None, None, box=True)
charts.title(ax, "B  fixed agents, 48 x 48")
