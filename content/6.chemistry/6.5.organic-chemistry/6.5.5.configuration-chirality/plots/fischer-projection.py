"""Fischer projections. The wedge (bow-tie) drawing of D-glyceraldehyde and its Fischer
projection (horizontal bonds point toward the viewer, vertical bonds away), and L-glyceraldehyde.
Descriptors are computed from the 3D meaning of the projection, not typed in by hand."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

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


def bowtie(ax, x0, y0, g):
    """Wedge drawing: horizontal groups on solid wedges toward the viewer, vertical on hashed bonds."""
    ink = plt.rcParams["text.color"]
    for pos, end in (("left", (-0.75, -0.35)), ("right", (0.75, -0.35))):
        e = np.array(end) + [x0, y0]
        d = e - [x0, y0]
        n = np.array([-d[1], d[0]]) / np.linalg.norm(d) * 0.08
        ax.add_patch(Polygon([[x0, y0], e + n, e - n], color=ink))
    for end in ((-0.0, 0.8), (0.0, -0.8)):
        e = np.array(end) + [x0, y0]
        for t in np.linspace(0.15, 1, 6):
            p = np.array([x0, y0]) + t * (e - [x0, y0])
            ax.plot([p[0] - 0.08 * t, p[0] + 0.08 * t], [p[1], p[1]], color=ink, lw=1.2)
    off = {"top": (0, 1.05), "bottom": (0, -1.05), "left": (-1.0, -0.45), "right": (1.0, -0.45)}
    for pos, name in g.items():
        dx, dy = off[pos]
        ax.text(x0 + dx, y0 + dy, name, ha="center", va="center", fontsize=11, color=ink)
    ax.plot([x0], [y0], "o", color=ink, ms=3)


fig, ax = plt.subplots(figsize=(10, 3.4))
bowtie(ax, 0, 0, D_GLY)
ax.text(0, -1.75, "wedge drawing", ha="center", fontsize=10)
ax.annotate("", xy=(2.3, 0), xytext=(1.5, 0), arrowprops=dict(arrowstyle="-|>", color=plt.rcParams["text.color"]))
fischer(ax, 3.6, 0, D_GLY, f"D-glyceraldehyde = ({descriptor(D_GLY, RANK)})-(+)")
fischer(ax, 7.6, 0, L_GLY, f"L-glyceraldehyde = ({descriptor(L_GLY, RANK)})-($-$)")
ax.plot([5.6, 5.6], [-1.3, 1.3], ls="--", color="0.6")
ax.text(5.6, 1.45, "mirror", ha="center", fontsize=9, color="0.5")
ax.set_aspect("equal")
ax.set_xlim(-1.5, 9.2)
ax.set_ylim(-2.1, 1.7)
ax.axis("off")
