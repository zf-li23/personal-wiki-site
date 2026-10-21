"""Left: a full adder built from two half adders and an OR gate,
S = A xor B xor Cin, Cout = AB + (A xor B) Cin. Right: a 4-bit ripple-carry adder,
in which each carry must wait for the carry of the bit below."""

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


fig, axes = plt.subplots(1, 2, figsize=(11, 4), gridspec_kw={"width_ratios": [1.15, 1]})
ax = axes[0]
yA, yB, yC = 1.2, 0.8, -0.6
x1i, x1o = gate(ax, "XOR", 1.2, 1.0)
a1i, a1o = gate(ax, "AND", 1.2, -1.6)
x2i, x2o = gate(ax, "XOR", 3.4, 0.2)
a2i, a2o = gate(ax, "AND", 3.4, -0.8)
oi, oo = gate(ax, "OR", 5.4, -1.2)
label(ax, -0.4, yA, "A")
label(ax, -0.4, yB, "B")
label(ax, -0.4, yC, r"$C_{\mathrm{in}}$")
wire(ax, [(-0.2, yA), (0.6, yA), (0.6, x1i[0][1]), x1i[0]])
wire(ax, [(-0.2, yB), (0.4, yB), (0.4, x1i[1][1]), x1i[1]])
wire(ax, [(0.6, x1i[0][1]), (0.6, a1i[0][1]), a1i[0]], dot_start=True)
wire(ax, [(0.4, x1i[1][1]), (0.4, a1i[1][1]), a1i[1]], dot_start=True)
wire(ax, [x1o, (2.8, x1o[1]), (2.8, x2i[0][1]), x2i[0]])
wire(ax, [(2.8, x2i[0][1]), (2.8, a2i[0][1]), a2i[0]], dot_start=True)
wire(ax, [(-0.2, yC), (2.6, yC), (2.6, x2i[1][1]), x2i[1]])
wire(ax, [(2.6, yC), (2.6, a2i[1][1]), a2i[1]], dot_start=True)
wire(ax, [x2o, (6.8, x2o[1])])
label(ax, 7.05, x2o[1], "S")
wire(ax, [a2o, (5.0, a2o[1]), (5.0, oi[0][1]), oi[0]])
wire(ax, [a1o, (5.0, a1o[1]), (5.0, oi[1][1]), oi[1]])
wire(ax, [oo, (6.8, oo[1])])
label(ax, 7.15, oo[1], r"$C_{\mathrm{out}}$")
label(ax, 2.2, 1.75, "half adder 1", fontsize=8)
label(ax, 4.4, 0.95, "half adder 2", fontsize=8)
ax.set_xlim(-0.9, 7.6)
ax.set_ylim(-2.4, 2.0)
ax.set_title("full adder", fontsize=10)

ax = axes[1]
for k in range(4):
    x = 4.5 - 1.6 * k
    box(ax, x, 0, 1.1, 1.0, "FA", fontsize=10)
    wire(ax, [(x + 0.3, 1.7), (x + 0.3, 1.0)])
    wire(ax, [(x + 0.8, 1.7), (x + 0.8, 1.0)])
    label(ax, x + 0.3, 1.95, f"$A_{k}$", fontsize=9)
    label(ax, x + 0.8, 1.95, f"$B_{k}$", fontsize=9)
    wire(ax, [(x + 0.55, 0), (x + 0.55, -0.6)])
    label(ax, x + 0.55, -0.85, f"$S_{k}$", fontsize=9)
    wire(ax, [(x, 0.5), (x - 0.5, 0.5)])
    label(ax, x - 0.25, 0.75, f"$C_{k + 1}$", fontsize=8)
wire(ax, [(6.1, 0.5), (5.6, 0.5)])
label(ax, 6.35, 0.5, r"$C_0$", fontsize=9)
ax.set_xlim(-0.6, 6.8)
ax.set_ylim(-1.4, 2.4)
ax.set_title("4-bit ripple-carry adder", fontsize=10)
for ax in axes:
    ax.set_aspect("equal")
    ax.axis("off")
fig.tight_layout()
