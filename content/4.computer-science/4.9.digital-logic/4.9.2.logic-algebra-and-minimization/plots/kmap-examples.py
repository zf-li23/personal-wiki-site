"""Karnaugh-map minimization. Left: the four pairs are all essential, and the
large group BD (dashed) is a prime implicant that is redundant. Right: a BCD digit
x >= 5, where the codes 10-15 never occur and are used as don't-cares (X)."""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

FG = plt.rcParams["text.color"]
GRAY = ["00", "01", "11", "10"]


def kmap(ax, rows, cols, rvars, cvars, cell_text, title=""):
    """Draw a Karnaugh map. rows/cols are lists of Gray-ordered labels;
    cell_text(r, c) returns the string shown in cell (r, c)."""
    nr, nc = len(rows), len(cols)
    for i in range(nr + 1):
        ax.plot([0, nc], [-i, -i], color=FG, lw=1)
    for j in range(nc + 1):
        ax.plot([j, j], [0, -nr], color=FG, lw=1)
    ax.plot([-0.9, 0], [0.9, 0], color=FG, lw=1)
    ax.text(-0.15, 0.55, cvars, ha="right", va="center", color=FG, fontsize=10)
    ax.text(-0.55, 0.15, rvars, ha="right", va="center", color=FG, fontsize=10)
    for j, c in enumerate(cols):
        ax.text(j + 0.5, 0.25, c, ha="center", va="center", color=FG, fontsize=9, family="monospace")
    for i, r in enumerate(rows):
        ax.text(-0.25, -i - 0.5, r, ha="center", va="center", color=FG, fontsize=9, family="monospace")
    for i, r in enumerate(rows):
        for j, c in enumerate(cols):
            txt = cell_text(i, j)
            if txt:
                ax.text(j + 0.5, -i - 0.5, txt, ha="center", va="center", color=FG, fontsize=11)
    if title:
        ax.set_title(title, fontsize=10)
    ax.set_xlim(-1.2, nc + 0.3)
    ax.set_ylim(-nr - 0.3, 1.1)
    ax.set_aspect("equal")
    ax.axis("off")


def group(ax, r0, c0, nr, nc, color, ls="-", pad=0.12):
    """Outline a rectangular group of cells starting at row r0, column c0."""
    ax.add_patch(FancyBboxPatch((c0 + pad, -r0 - nr + pad), nc - 2 * pad, nr - 2 * pad,
                                boxstyle="round,pad=0,rounding_size=0.25",
                                facecolor="none", edgecolor=color, lw=2.0, ls=ls))


def cells(ones, dcs=()):
    def f(i, j):
        m = int(GRAY[i] + GRAY[j], 2)
        return "1" if m in ones else ("X" if m in dcs else "0")
    return f


fig, axes = plt.subplots(1, 2, figsize=(9, 4.2))
ax = axes[0]
kmap(ax, GRAY, GRAY, "AB", "CD", cells({3, 4, 5, 7, 9, 13, 14, 15}),
     r"$F=\sum m(3,4,5,7,9,13,14,15)$")
group(ax, 1, 0, 1, 2, "C0")          # A'BC'
group(ax, 0, 2, 2, 1, "C1")          # A'CD
group(ax, 2, 1, 2, 1, "C2")          # AC'D
group(ax, 2, 2, 1, 2, "C3")          # ABC
group(ax, 1, 1, 2, 2, "C4", ls="--", pad=0.3)   # BD (redundant)
ax = axes[1]
kmap(ax, GRAY, GRAY, "AB", "CD", cells({5, 6, 7, 8, 9}, set(range(10, 16))),
     r"$F = A + BD + BC$  ($x \geq 5$)")
group(ax, 2, 0, 2, 4, "C0", pad=0.08)  # A
group(ax, 1, 1, 2, 2, "C1", pad=0.2)   # BD
group(ax, 1, 2, 2, 2, "C2", pad=0.3)   # BC
fig.tight_layout()
