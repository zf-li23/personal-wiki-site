"""Complementation groups from a pairwise complementation matrix.
Data: nine recessive X-linked eye-color mutations of Drosophila (white, garnet, ruby, vermilion, cherry, coral,
apricot, buff, carnation) tested in all pairs in trans-heterozygous females; + = wild-type eyes (complementation),
- = mutant eyes (no complementation). (A) The matrix as published, in the order of isolation. (B) The same matrix
with rows and columns reordered by the complementation groups found by Algorithm 13.1.1 (connected components of the
'fails to complement' graph): one group of five alleles of white and four single-member groups."""

import numpy as np
from matplotlib.patches import Rectangle

import wikibio as bio

P = bio.P

names = ["white", "garnet", "ruby", "vermilion", "cherry", "coral", "apricot", "buff", "carnation"]
fail = {("white", n) for n in ("cherry", "coral", "apricot", "buff")}
fail |= {(a, b) for a in ("cherry", "coral", "apricot", "buff") for b in ("cherry", "coral", "apricot", "buff")}
n = len(names)
M = np.zeros((n, n), bool)  # True = fails to complement
for i, a in enumerate(names):
    for j, b in enumerate(names):
        M[i, j] = i == j or (a, b) in fail or (b, a) in fail

# connected components (union-find)
parent = list(range(n))


def find(i):
    while parent[i] != i:
        parent[i] = parent[parent[i]]
        i = parent[i]
    return i


for i in range(n):
    for j in range(n):
        if M[i, j]:
            parent[find(i)] = find(j)
groups = {}
for i in range(n):
    groups.setdefault(find(i), []).append(i)
order_groups = sorted(groups.values(), key=lambda g: (-len(g), g[0]))
order = [i for g in order_groups for i in g]

fig, ax = bio.canvas(20.0, 9.4)


def draw(x0, y0, idx, title, boxes=None):
    c = 0.72
    bio.label(ax, (x0 + n * c / 2, y0 + 1.75), title, size="normal", bold=True)
    for r, i in enumerate(idx):
        bio.label(ax, (x0 - 0.15, y0 - r * c - c / 2), names[i], size="tiny", ha="right", italic=True)
        bio.label(ax, (x0 + r * c + c / 2, y0 + 0.15), names[i], size="tiny", ha="left", italic=True, rotation=50)
        for k, j in enumerate(idx):
            if k < r:
                continue
            no = M[i, j]
            ax.add_patch(Rectangle((x0 + k * c, y0 - (r + 1) * c), c, c, facecolor=P.fill("negative") if no
                                   else P.fill("positive"), edgecolor=P.surface(), lw=1.2, zorder=3))
            bio.label(ax, (x0 + k * c + c / 2, y0 - r * c - c / 2), "-" if no else "+", size="small",
                      color=P.on_fill(), zorder=4)
    if boxes:
        s = 0
        for g in boxes:
            L = len(g)
            ax.add_patch(Rectangle((x0 + s * c, y0 - (s + L) * c), L * c, L * c, fill=False, edgecolor=P.ink(),
                                   lw=1.6, zorder=5))
            s += L


draw(2.2, 7.0, list(range(n)), "A  Complementation tests")
draw(12.4, 7.0, order, "B  Reordered by complementation group", boxes=order_groups)
bio.label(ax, (16.0, 0.35), f"{len(order_groups)} complementation groups (genes)", size="small")
ax.add_patch(Rectangle((2.2, 0.15), 0.4, 0.4, facecolor=P.fill("negative"), edgecolor="none"))
bio.label(ax, (2.75, 0.35), "- no complementation (same gene)", size="tiny", ha="left")
ax.add_patch(Rectangle((7.4, 0.15), 0.4, 0.4, facecolor=P.fill("positive"), edgecolor="none"))
bio.label(ax, (7.95, 0.35), "+ complementation", size="tiny", ha="left")
