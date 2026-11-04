# Relative evolutionary divergence (RED), the rank normalization of the Genome Taxonomy Database.
# A toy rooted tree of eight genomes in two lineages that evolve at different rates (branch lengths in
# substitutions per site). For each node n with parent p,
#     RED(n) = RED(p) + (d / u) (1 - RED(p)),
# where d is the length of the branch p -> n and u is d plus the mean distance from n to the tips below it;
# the root has RED 0 and every tip RED 1. A: the phylogram, x = distance from the root: the four
# inner clades (candidate genera) lie at very different depths because lineage A evolves faster.
# B: the same tree with x = RED: the four clades line up at similar values (printed), so they can be
# given the same rank.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
# node: (parent, branch length)
tree = {
    "A": ("root", 0.10), "B": ("root", 0.05),
    "A1": ("A", 0.40), "A2": ("A", 0.45), "B1": ("B", 0.12), "B2": ("B", 0.10),
    "a1": ("A1", 0.20), "a2": ("A1", 0.25), "a3": ("A2", 0.20), "a4": ("A2", 0.30),
    "b1": ("B1", 0.06), "b2": ("B1", 0.05), "b3": ("B2", 0.07), "b4": ("B2", 0.05),
}
kids = {}
for n, (p, _) in tree.items():
    kids.setdefault(p, []).append(n)
tips = [n for n in tree if n not in kids]


def tip_dists(n):
    """Distances from node n to each tip below it."""
    if n not in kids:
        return [0.0]
    return [tree[c][1] + x for c in kids[n] for x in tip_dists(c)]


depth, red = {"root": 0.0}, {"root": 0.0}
for n in ["A", "B", "A1", "A2", "B1", "B2"] + tips:
    p, d = tree[n]
    depth[n] = depth[p] + d
    u = d + np.mean(tip_dists(n))
    red[n] = red[p] + d / u * (1 - red[p])

order = ["a1", "a2", "a3", "a4", "b1", "b2", "b3", "b4"]
ypos = {t: 7 - i for i, t in enumerate(order)}
for n in ["A1", "A2", "B1", "B2", "A", "B", "root"]:
    ypos[n] = np.mean([ypos[c] for c in kids[n]])

fig, axs = plt.subplots(1, 2, figsize=(11.5, 3.9), gridspec_kw=dict(wspace=0.25))
clade = {"A1": "rna", "A2": "rna", "B1": "dna", "B2": "dna"}
for ax, xs, title, xlabel in [(axs[0], depth, "A   Phylogram: depth depends on rate", "distance from root / substitutions per site"),
                              (axs[1], red, "B   RED: comparable ranks", "relative evolutionary divergence")]:
    for n, (p, _) in tree.items():
        col = P.edge(clade.get(n, clade.get(p, "neutral"))) if (n in clade or p in clade) else P.ink()
        ax.plot([xs[p], xs[p]], [ypos[p], ypos[n]], color=P.ink(), lw=1.1)
        ax.plot([xs[p], xs[n]], [ypos[n], ypos[n]], color=col, lw=1.6 if col != P.ink() else 1.1)
    for n, tok in clade.items():
        ax.plot(xs[n], ypos[n], "o", ms=6, color=P.fill(tok), mec=P.edge(tok), zorder=5)
        ax.text(xs[n] - 0.012 * (max(xs.values())), ypos[n] + 0.3, n if ax is axs[0] else f"{n}: {red[n]:.2f}",
                fontsize=7, ha="right", color=P.ink())
    for t in tips:
        ax.text(xs[t] + 0.01 * max(xs.values()), ypos[t], t, fontsize=7, va="center", color=P.muted())
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    charts.style_axes(ax, xlabel)
    ax.spines["left"].set_visible(False)
    charts.title(ax, title)
axs[0].text(0.02, 6.9, "lineage A: fast", fontsize=7, color=P.edge("rna"))
axs[0].text(0.3, 1.5, "lineage B: slow", fontsize=7, color=P.edge("dna"))
axs[1].set_xlim(0, 1.08)
