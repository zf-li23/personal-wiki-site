# Accessible mutational paths on fitness landscapes. Genotypes are binary strings of L = 5 mutations;
# fitness is the "rough Mount Fuji" model, an additive part (each mutation adds a_i, a_i uniform in
# [0.5, 1.5]) plus an independent random part of standard deviation sigma for each genotype. A path
# from the wild type 00000 to the quintuple mutant 11111 that adds one mutation at a time (5! = 120
# orders) is accessible to natural selection in the strong-selection, weak-mutation regime if fitness
# increases at every step. A: an example landscape with sigma = 1.5 drawn by number of mutations
# (genotypes as points, single-mutation steps as lines; accessible paths in color). B: mean fraction of
# accessible paths among landscapes in which 11111 is fitter than 00000, against sigma (2000 landscapes
# per value): all 120 are accessible without epistasis, few with strong sign epistasis; the dashed line
# marks 18 of 120, the number found for five resistance mutations of TEM-1 beta-lactamase
# (Weinreich and colleagues 2006).
import itertools

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(3)
L = 5
G = np.array(list(itertools.product((0, 1), repeat=L)))
idx = {tuple(g): i for i, g in enumerate(G)}
perms = list(itertools.permutations(range(L)))


def landscape(sigma):
    a = rng.uniform(0.5, 1.5, L)
    return G @ a + sigma * rng.normal(size=len(G))


def accessible(f):
    acc = []
    for p in perms:
        g = np.zeros(L, int)
        ok = True
        path = [idx[tuple(g)]]
        for m in p:
            g[m] = 1
            j = idx[tuple(g)]
            if f[j] <= f[path[-1]]:
                ok = False
                break
            path.append(j)
        if ok:
            acc.append(path)
    return acc


fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.2))
ax = axs[0]
while True:
    f = landscape(1.5)
    if f[-1] > f[0]:
        acc = accessible(f)
        if 3 <= len(acc) <= 20:
            break
nmut = G.sum(1)
for i, g in enumerate(G):
    for m in range(L):
        if g[m] == 0:
            h = g.copy(); h[m] = 1
            j = idx[tuple(h)]
            ax.plot([nmut[i], nmut[j]], [f[i], f[j]], color=P.muted(), lw=0.5, alpha=0.5, zorder=1)
for path in acc:
    ax.plot(nmut[path], f[path], color=charts.line("negative"), lw=1.8, alpha=0.7, zorder=2)
ax.scatter(nmut, f, s=18, color=charts.line("protein"), zorder=3)
ax.text(0.03, 0.95, f"{len(acc)} of 120 paths accessible", transform=ax.transAxes, fontsize=8, color=P.ink(), va="top")
charts.style_axes(ax, "number of mutations", "fitness (arbitrary units)")
charts.title(ax, "A   A rugged landscape")

ax = axs[1]
sig = np.array([0, 0.1, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0])
mean_frac = []
for s in sig:
    fr = []
    while len(fr) < 400:
        f = landscape(s)
        if f[-1] > f[0]:
            fr.append(len(accessible(f)) / 120)
    mean_frac.append(np.mean(fr))
ax.plot(sig, mean_frac, "o-", color=charts.line("negative"), lw=1.8, ms=5)
ax.axhline(18 / 120, color=P.muted(), lw=0.8, ls="--")
ax.text(3.2, 18 / 120 + 0.02, "TEM-1: 18 of 120", fontsize=7.5, color=P.ink())
ax.set_ylim(0, 1.05)
charts.style_axes(ax, "roughness $\\sigma$ (random part / mean mutational effect)", "fraction of accessible paths")
charts.title(ax, "B   Epistasis closes paths")
fig.tight_layout()
