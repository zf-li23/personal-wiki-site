"""Analysis example: four NAND gates. Writing the output of every gate in turn
gives Y = A xor B."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch, Circle

FG = plt.rcParams["text.color"]
LW = 1.4


def _patch(ax, verts, codes):
    ax.add_patch(PathPatch(Path(verts, codes), facecolor="none", edgecolor=FG, lw=LW))


def bubble(ax, x, y, r=0.07):
    ax.add_patch(Circle((x + r, y), r, facecolor="none", edgecolor=FG, lw=LW))
    return x + 2 * r


def gate(ax, kind, x, y, s=1.0, n_in=2):
    """Draw a distinctive-shape gate whose left edge is at x, centred on y.
    Returns (input points, output point)."""
    h = 0.5 * s
    M, L, C3, C4 = Path.MOVETO, Path.LINETO, Path.CURVE3, Path.CURVE4
    base = kind.lstrip("N") if kind not in ("NOT",) else "NOT"
    if kind in ("NAND", "NOR", "XNOR"):
        base = {"NAND": "AND", "NOR": "OR", "XNOR": "XOR"}[kind]
    inv = kind in ("NAND", "NOR", "XNOR", "NOT")
    if base == "AND":
        th = np.linspace(np.pi / 2, -np.pi / 2, 30)
        verts = [(x, y - h), (x, y + h), (x + h, y + h)]
        verts += [(x + h + h * np.cos(t), y + h * np.sin(t)) for t in th]
        verts += [(x, y - h)]
        _patch(ax, verts, [M] + [L] * (len(verts) - 1))
        out = x + 2 * h
        xin = x
    elif base in ("OR", "XOR"):
        verts = [(x, y + h), (x + 1.2 * h, y + h), (x + 2 * h, y),
                 (x + 1.2 * h, y - h), (x, y - h), (x + 0.45 * h, y), (x, y + h)]
        codes = [M, C3, C3, C3, C3, C3, C3]
        _patch(ax, verts, codes)
        if base == "XOR":
            d = 0.22 * h
            _patch(ax, [(x - d, y + h), (x - d + 0.45 * h, y), (x - d, y - h)], [M, C3, C3])
        out = x + 2 * h
        xin = x + 0.25 * h
    elif base in ("NOT", "BUF"):
        verts = [(x, y - 0.8 * h), (x, y + 0.8 * h), (x + 1.5 * h, y), (x, y - 0.8 * h)]
        _patch(ax, verts, [M, L, L, L])
        out = x + 1.5 * h
        xin = x
    if inv:
        out = bubble(ax, out, y, 0.13 * h)
    if base in ("NOT", "BUF"):
        ins = [(x, y)]
    else:
        ys = np.linspace(y + 0.6 * h, y - 0.6 * h, n_in) if n_in > 1 else [y]
        ins = [(xin if base == "AND" else x + 0.3 * h, yy) for yy in ys]
    return ins, (out, y)


def wire(ax, pts, dot_start=False, dot_end=False):
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color=FG, lw=1.1, solid_capstyle="round")
    for flag, p in ((dot_start, pts[0]), (dot_end, pts[-1])):
        if flag:
            ax.plot(*p, "o", color=FG, ms=3.5)


def label(ax, x, y, text, **kw):
    kw.setdefault("ha", "center")
    kw.setdefault("va", "center")
    kw.setdefault("fontsize", 10)
    ax.text(x, y, text, color=FG, **kw)


def box(ax, x, y, w, h, text="", fontsize=10):
    ax.add_patch(plt.Rectangle((x, y), w, h, facecolor="none", edgecolor=FG, lw=LW))
    if text:
        label(ax, x + w / 2, y + h / 2, text, fontsize=fontsize)


fig, ax = plt.subplots(figsize=(8, 3.6))
ins1, o1 = gate(ax, "NAND", 1.4, 0.0)
ins2, o2 = gate(ax, "NAND", 3.4, 1.0)
ins3, o3 = gate(ax, "NAND", 3.4, -1.0)
ins4, o4 = gate(ax, "NAND", 5.4, 0.0)
yA, yB = 1.3, -1.3
label(ax, -0.25, yA, "A")
label(ax, -0.25, yB, "B")
# A to gate 1 and gate 2
wire(ax, [(0, yA), ins2[0]])
wire(ax, [(0.8, yA), (0.8, ins1[0][1]), ins1[0]], dot_start=True)
# B to gate 1 and gate 3
wire(ax, [(0, yB), ins3[1]])
wire(ax, [(1.0, yB), (1.0, ins1[1][1]), ins1[1]], dot_start=True)
# N1 to gates 2 and 3
xm = o1[0] + 0.4
wire(ax, [o1, (xm, o1[1])])
wire(ax, [(xm, o1[1]), (xm, ins2[1][1]), ins2[1]], dot_start=True)
wire(ax, [(xm, o1[1]), (xm, ins3[0][1]), ins3[0]])
label(ax, o1[0] + 0.15, o1[1] + 0.25, r"$N_1$", fontsize=9)
# N2, N3 to gate 4
xn = o2[0] + 0.4
wire(ax, [o2, (xn, o2[1]), (xn, ins4[0][1]), ins4[0]])
wire(ax, [o3, (xn, o3[1]), (xn, ins4[1][1]), ins4[1]])
label(ax, o2[0] + 0.2, o2[1] + 0.25, r"$N_2$", fontsize=9)
label(ax, o3[0] + 0.2, o3[1] - 0.25, r"$N_3$", fontsize=9)
wire(ax, [o4, (o4[0] + 0.5, o4[1])])
label(ax, o4[0] + 0.75, o4[1], "Y")
ax.set_xlim(-0.6, 7.2)
ax.set_ylim(-1.8, 1.8)
ax.set_aspect("equal")
ax.axis("off")
fig.tight_layout()
