"""Layout of 3- and 4-variable Karnaugh maps: rows and columns follow the
Gray code, so cells that touch (including across the edges) differ in one variable.
Each cell shows the index i of its minterm m_i (A is the most significant bit)."""

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


fig, axes = plt.subplots(1, 2, figsize=(9, 4))
kmap(axes[0], ["0", "1"], GRAY, "A", "BC",
     lambda i, j: f"$m_{{{int(['0', '1'][i] + GRAY[j], 2)}}}$", "3 variables")
kmap(axes[1], GRAY, GRAY, "AB", "CD",
     lambda i, j: f"$m_{{{int(GRAY[i] + GRAY[j], 2)}}}$", "4 variables")
fig.tight_layout()
