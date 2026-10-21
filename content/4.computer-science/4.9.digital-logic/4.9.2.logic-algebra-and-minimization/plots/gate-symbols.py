"""Distinctive-shape symbols (IEEE Std 91) of the common logic gates."""

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


fig, ax = plt.subplots(figsize=(9, 3.6))
items = [("AND", r"AND  $F = AB$"), ("OR", r"OR  $F = A + B$"), ("NOT", r"NOT  $F = \overline{A}$"),
         ("BUF", r"buffer  $F = A$"), ("NAND", r"NAND  $F = \overline{AB}$"),
         ("NOR", r"NOR  $F = \overline{A + B}$"), ("XOR", r"XOR  $F = A \oplus B$"),
         ("XNOR", r"XNOR  $F = \overline{A \oplus B}$")]
for k, (kind, text) in enumerate(items):
    cx, cy = 2.6 * (k % 4), -2.0 * (k // 4)
    ins, out = gate(ax, kind, cx, cy)
    for p in ins:
        wire(ax, [(cx - 0.45, p[1]), p])
    wire(ax, [out, (out[0] + 0.4, out[1])])
    label(ax, cx + 0.5, cy - 0.85, text, fontsize=9)
ax.set_xlim(-0.8, 9.6)
ax.set_ylim(-3.2, 0.8)
ax.set_aspect("equal")
ax.axis("off")
fig.tight_layout()
