"""Hasse diagram of the power set of {a, b, c} ordered by inclusion (Section 2.8): each subset is a node,
and a line joins x below y when y covers x, i.e. y = x plus one element. Subsets on the same level have
the same size and are pairwise incomparable."""

import itertools
import matplotlib.pyplot as plt

base = "abc"
subsets = [frozenset(s) for k in range(4) for s in itertools.combinations(base, k)]
pos = {}
for k in range(4):
    level = [s for s in subsets if len(s) == k]
    for i, s in enumerate(level):
        pos[s] = ((i - (len(level) - 1) / 2) * 1.6, k * 1.3)


def name(s):
    return r"$\varnothing$" if not s else r"$\{" + ", ".join(sorted(s)) + r"\}$"


fig, ax = plt.subplots(figsize=(6.4, 5.2))
for x, y in itertools.product(subsets, repeat=2):
    if x < y and len(y) == len(x) + 1:
        ax.plot(*zip(pos[x], pos[y]), color="0.55", lw=1.4, zorder=1)
for s, (px, py) in pos.items():
    ax.text(px, py, name(s), ha="center", va="center", fontsize=13, zorder=2,
            bbox=dict(boxstyle="round,pad=0.35", fc="C0", alpha=0.18, ec="C0", lw=1.2))
for k in range(4):
    ax.text(3.3, k * 1.3, f"{k} element" + ("" if k == 1 else "s"), ha="left", va="center", fontsize=10, color="0.5")
ax.set_xlim(-2.9, 4.6)
ax.set_ylim(-0.6, 4.5)
ax.axis("off")
