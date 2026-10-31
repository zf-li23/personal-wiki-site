"""The Vicsek model in two dimensions: N = 400 particles in a periodic box of side L = 10
(density 4), speed v0 = 0.3 per step, interaction radius R = 1; at each step every particle takes
the mean direction of the particles within R (itself included) plus a random angle uniform in
[-eta/2, eta/2]. A, B: snapshots after 800 steps at noise eta = 0.5 (ordered: all move together)
and eta = 4 (disordered); arrows show directions. C: the polar order parameter
Psi = |sum v_i|/(N v0), averaged over steps 300-600, against the noise amplitude, for N = 100
and 400 at the same density: order is lost continuously in these small systems as noise grows
(in large systems the transition is discontinuous, with traveling bands)."""

import numpy as np
from scipy.spatial import cKDTree
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(4)
v0, R = 0.3, 1.0


def vicsek(N, L, eta, steps, keep=False):
    x = rng.uniform(0, L, (N, 2))
    th = rng.uniform(-np.pi, np.pi, N)
    psi = []
    for s in range(steps):
        pr = cKDTree(x, boxsize=L).query_pairs(R, output_type="ndarray")
        co, sn = np.cos(th), np.sin(th)
        c = co + np.bincount(pr[:, 0], co[pr[:, 1]], N) + np.bincount(pr[:, 1], co[pr[:, 0]], N)
        si = sn + np.bincount(pr[:, 0], sn[pr[:, 1]], N) + np.bincount(pr[:, 1], sn[pr[:, 0]], N)
        th = np.arctan2(si, c) + eta * (rng.random(N) - 0.5)
        x = (x + v0 * np.column_stack((np.cos(th), np.sin(th)))) % L
        x[x >= L] = 0.0
        psi.append(np.hypot(np.cos(th).mean(), np.sin(th).mean()))
    return x, th, np.array(psi)


fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.5))
fig.subplots_adjust(wspace=0.3, left=0.05, right=0.98, bottom=0.15, top=0.88)
for ax, eta, ttl in ((axs[0], 0.5, r"A  $\eta$ = 0.5: flocking"), (axs[1], 4.0, r"B  $\eta$ = 4: disorder")):
    x, th, _ = vicsek(400, 10.0, eta, 800)
    ax.quiver(x[:, 0], x[:, 1], np.cos(th), np.sin(th), color=charts.line("bacterium"), scale=28,
              width=0.006, headwidth=4)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    charts.style_axes(ax, None, None, box=True)
    charts.title(ax, ttl)

ax = axs[2]
etas = np.linspace(0.25, 5.5, 9)
for N, L, tok in ((100, 5.0, "neutral"), (400, 10.0, "bacterium")):
    m = [vicsek(N, L, e, 600)[2][300:].mean() for e in etas]
    ax.plot(etas, m, "o-", color=charts.line(tok), ms=3.5, lw=1.1, label=f"N = {N}")
ax.set_ylim(0, 1.02)
ax.legend(frameon=False, fontsize=7, loc="upper right")
charts.style_axes(ax, r"noise $\eta$", r"order parameter $\Psi$")
charts.title(ax, "C  order against noise")
