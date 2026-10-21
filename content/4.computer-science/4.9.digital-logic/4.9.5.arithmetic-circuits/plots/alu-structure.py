"""Structure of a simple 32-bit ALU: every functional unit computes in parallel and
a multiplexer driven by the ALU control code selects the result. Subtraction reuses
the adder by inverting B and setting the carry-in; set-less-than takes N xor V."""

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


fig, ax = plt.subplots(figsize=(9, 5))
# operands
label(ax, 0.3, 4.6, "A")
label(ax, 1.7, 4.6, "B")
wire(ax, [(0.3, 4.4), (0.3, 3.4)])
wire(ax, [(1.7, 4.4), (1.7, 4.1)])
box(ax, 1.15, 3.6, 1.1, 0.5, r"$B \oplus \mathrm{sub}$", fontsize=9)
wire(ax, [(1.7, 3.6), (1.7, 3.4)])
box(ax, 0.0, 2.6, 2.6, 0.8, "adder", fontsize=10)
wire(ax, [(2.6, 3.0), (2.95, 3.0)])
label(ax, 3.0, 3.0, "Cin = sub", fontsize=8, ha="left")
# logic units
for k, name in enumerate(("AND", "OR", "XOR")):
    box(ax, 3.2 + 1.3 * k, 2.6 - 1.3, 1.0, 0.7, name, fontsize=9)
box(ax, 3.2 + 1.3 * 3, 1.3, 1.1, 0.7, "shifter", fontsize=9)
box(ax, 3.2 + 1.3 * 4 + 0.1, 1.3, 1.0, 0.7, "SLT", fontsize=9)
# multiplexer
mx = [(0.6, -0.6), (8.6, -0.6), (8.0, -1.2), (1.2, -1.2), (0.6, -0.6)]
wire(ax, mx)
label(ax, 4.6, -0.9, "result multiplexer", fontsize=9)
wire(ax, [(1.3, 2.6), (1.3, -0.6)])
for k in range(5):
    x = 3.7 + 1.3 * k + (0.15 if k == 4 else 0.0) + (0.05 if k == 3 else 0.0)
    wire(ax, [(x, 1.3), (x, -0.6)])
wire(ax, [(2.6, 2.75), (8.95, 2.75), (8.95, 1.65), (8.9, 1.65)])
label(ax, 9.05, 2.2, "N xor V", fontsize=8, ha="left")
wire(ax, [(8.6, -0.9), (9.3, -0.9)])
label(ax, 9.45, -0.9, "ALUop", fontsize=9, ha="left")
wire(ax, [(4.6, -1.2), (4.6, -1.9)])
label(ax, 4.6, -2.1, "Y", fontsize=10)
label(ax, 5.9, -1.9, "Zero = (Y == 0)", fontsize=8, ha="left")
label(ax, 2.7, 2.35, "flags N, C, V", fontsize=8, ha="left")
label(ax, 6.0, 2.4, "A, B to every unit", fontsize=8)
ax.set_xlim(-0.5, 10.6)
ax.set_ylim(-2.4, 4.9)
ax.set_aspect("equal")
ax.axis("off")
fig.tight_layout()
