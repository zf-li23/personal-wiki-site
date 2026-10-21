"""Even-parity generator for eight data bits: a balanced tree of seven XOR gates,
three gate levels deep. P = 1 exactly when the data contain an odd number of ones,
so that the nine bits together always contain an even number of ones."""

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


fig, ax = plt.subplots(figsize=(8, 4.4))
ys = [3.5 - k for k in range(8)]
level1 = []
for k in range(4):
    yc = (ys[2 * k] + ys[2 * k + 1]) / 2
    ins, out = gate(ax, "XOR", 1.2, yc, s=0.8)
    for j in range(2):
        y = ys[2 * k + j]
        wire(ax, [(0.2, y), (0.8, y), (0.8, ins[j][1]), ins[j]])
        label(ax, -0.05, y, f"$d_{2 * k + j}$", fontsize=9)
    level1.append(out)
level2 = []
for k in range(2):
    a, b = level1[2 * k], level1[2 * k + 1]
    yc = (a[1] + b[1]) / 2
    ins, out = gate(ax, "XOR", 3.0, yc, s=0.8)
    for p, q in ((a, ins[0]), (b, ins[1])):
        wire(ax, [p, (2.6, p[1]), (2.6, q[1]), q])
    level2.append(out)
a, b = level2
ins, out = gate(ax, "XOR", 4.8, (a[1] + b[1]) / 2, s=0.8)
for p, q in ((a, ins[0]), (b, ins[1])):
    wire(ax, [p, (4.4, p[1]), (4.4, q[1]), q])
wire(ax, [out, (out[0] + 0.5, out[1])])
label(ax, out[0] + 0.75, out[1], "P")
for x, t in ((1.5, "level 1"), (3.3, "level 2"), (5.1, "level 3")):
    label(ax, x, -4.0, t, fontsize=9)
ax.set_xlim(-0.4, 6.6)
ax.set_ylim(-4.3, 4.0)
ax.set_aspect("equal")
ax.axis("off")
fig.tight_layout()
