"""Operations on the Fischer projection of D-glyceraldehyde and their effect on the descriptor.
Descriptors are computed from the 3D meaning of the projection (horizontal bonds toward the
viewer, vertical bonds away), not typed in by hand."""

import numpy as np
import matplotlib.pyplot as plt

POS = {"top": (0, 1, -1), "bottom": (0, -1, -1), "left": (-1, 0, 1), "right": (1, 0, 1)}


def descriptor(groups, rank):
    """groups: {position: name}; rank: {name: CIP rank 1..4}. R if the triple product is negative
    (1 -> 2 -> 3 clockwise when viewed with 4 pointing away)."""
    p = {rank[name]: np.array(POS[pos], float) for pos, name in groups.items()}
    a, b, c = p[1] - p[4], p[2] - p[4], p[3] - p[4]
    return "R" if np.dot(a, np.cross(b, c)) < 0 else "S"


RANK = {"OH": 1, "CHO": 2, "CH$_2$OH": 3, "H": 4}
D_GLY = {"top": "CHO", "bottom": "CH$_2$OH", "left": "H", "right": "OH"}
L_GLY = {"top": "CHO", "bottom": "CH$_2$OH", "left": "OH", "right": "H"}
assert descriptor(D_GLY, RANK) == "R" and descriptor(L_GLY, RANK) == "S"


def fischer(ax, x0, y0, g, title=None, hl=None):
    ink = plt.rcParams["text.color"]
    ax.plot([x0 - 0.8, x0 + 0.8], [y0, y0], color=ink, lw=1.6)
    ax.plot([x0, x0], [y0 - 0.8, y0 + 0.8], color=ink, lw=1.6)
    off = {"top": (0, 1.05), "bottom": (0, -1.05), "left": (-1.15, 0), "right": (1.15, 0)}
    for pos, name in g.items():
        dx, dy = off[pos]
        col = "#dc2626" if hl and name in hl else ink
        ax.text(x0 + dx, y0 + dy, name, ha="center", va="center", fontsize=11, color=col)
    if title:
        ax.text(x0, y0 - 1.75, title, ha="center", fontsize=10)


# Figure 2: operations
ops = [
    ("original", D_GLY),
    ("rotate 180$^\\circ$ in plane", {"top": "CH$_2$OH", "bottom": "CHO", "left": "OH", "right": "H"}),
    ("rotate 90$^\\circ$", {"top": "H", "bottom": "OH", "left": "CH$_2$OH", "right": "CHO"}),
    ("swap H and OH", {"top": "CHO", "bottom": "CH$_2$OH", "left": "OH", "right": "H"}),
    ("cycle 3 groups, H fixed", {"top": "CH$_2$OH", "bottom": "OH", "left": "H", "right": "CHO"}),
]
fig2, ax2 = plt.subplots(figsize=(13, 3.0))
for k, (name, g) in enumerate(ops):
    d = descriptor(g, RANK)
    same = "same" if d == "R" else "enantiomer"
    fischer(ax2, 3.5 * k, 0, g, f"{name}\n({d}): {same}" if k else f"{name}\n(R)")
ax2.set_aspect("equal")
ax2.set_xlim(-1.7, 3.5 * 4 + 1.7)
ax2.set_ylim(-2.5, 1.5)
ax2.axis("off")
