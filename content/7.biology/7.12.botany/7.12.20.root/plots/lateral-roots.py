# Lateral root formation. (A-C) Origin in the pericycle (part of a transverse section, stele below):
# periclinal divisions in the pericycle (A), a dome-shaped primordium pushing through the endodermis (B),
# and the young lateral root with its own apex and root cap emerging through cortex and epidermis (C).
# (D-G) Position of lateral roots relative to the protoxylem poles in diarch, triarch, tetrarch and
# polyarch roots (xylem blue, phloem orange; arrows: sites of lateral root initiation).
import math

import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch, Polygon, Wedge

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30.0, 15.6)
ax.set_ylim(-0.6, 15.0)


def rect_cell(x, y, w, h, tok, lw=0.8, z=5):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.12", facecolor=P.fill(tok),
                                edgecolor=P.edge("cell_wall"), lw=lw, zorder=z))


def tissue_strip(x0, stage):
    """Layers from bottom (stele) to top: pericycle, endodermis, 3 cortex rows, epidermis."""
    rows = [("pericycle", 0.55), ("endodermis", 0.6), ("cytoplasm", 0.9), ("cytoplasm", 0.9), ("cytoplasm", 0.9),
            ("cell_wall", 0.55)]
    y = 7.6
    W = 7.0
    tops = []
    for tok, h in rows:
        n = int(W / (h * 1.3))
        w = W / n
        for i in range(n):
            xc = x0 + i * w
            if stage >= 2 and tok != "pericycle" and abs(xc + w / 2 - (x0 + W / 2)) < (1.1 + (0.6 if stage == 3 else 0)) and \
                    (y - 7.6) < (1.4 if stage == 2 else 5.0):
                continue  # cells crushed/separated by the primordium
            rect_cell(xc + 0.03, y + 0.03, w - 0.06, h - 0.06, tok)
        tops.append(y)
        y += h
    ax.add_patch(Polygon([(x0, 7.2), (x0 + W, 7.2), (x0 + W, 7.6), (x0, 7.6)], closed=True, facecolor=P.fill("xylem"),
                         edgecolor="none", alpha=0.35, zorder=4))
    cx = x0 + W / 2
    if stage == 1:
        for i in (-1, 0, 1):  # periclinally divided pericycle cells
            ax.plot([cx + i * 0.55 - 0.25, cx + i * 0.55 + 0.25], [7.88, 7.88], color=P.edge("pericycle"), lw=1.4, zorder=7)
    else:
        hgt = 1.8 if stage == 2 else 5.2
        wid = 1.1 if stage == 2 else 1.3
        t = np.linspace(0, np.pi, 60)
        dome = np.c_[cx + wid * np.cos(t), 7.6 + hgt * np.sin(t) ** 0.8]
        ax.add_patch(Polygon(np.vstack([[cx + wid, 7.6], dome, [cx - wid, 7.6]]), closed=True, facecolor=P.fill("plant"),
                             edgecolor=P.edge("plant"), lw=1.2, zorder=6))
        cap = np.c_[cx + wid * 0.75 * np.cos(t), 7.6 + hgt * 0.8 + hgt * 0.22 * np.sin(t)]
        ax.add_patch(Polygon(np.vstack([cap, [cx - wid * 0.75, 7.6 + hgt * 0.8]]), closed=True, facecolor=P.fill("highlight"),
                             edgecolor=P.edge("highlight"), lw=0.8, zorder=6.5))
        ax.plot([cx, cx], [7.4, 7.6 + hgt * 0.75], color=P.edge("xylem"), lw=2.0, zorder=6.6)
    return tops


titles = ["Pericycle divides", "Primordium", "Lateral root emerges"]
for k, x0 in enumerate((0.6, 10.4, 20.2)):
    bio.panel(ax, "ABC"[k], (x0 - 0.4, 14.8))
    bio.label(ax, (x0 + 3.5, 14.4), titles[k], size="normal", bold=True)
    tops = tissue_strip(x0, k + 1)
names = ["Pericycle", "Endodermis", "Cortex", "", "", "Epidermis"]
for name, y in zip(names, tops):
    if name:
        bio.label(ax, (27.5, y + 0.3), name, size="small", ha="left")
bio.label(ax, (27.5, 7.4), "Stele", size="small", ha="left", color=P.muted())

# D-G: positions
specs = [("D", "Diarch", 2, "between"), ("E", "Triarch", 3, "xylem"), ("F", "Tetrarch", 4, "xylem"), ("G", "Polyarch", 10, "phloem")]
for k, (L, name, n, rule) in enumerate(specs):
    c = np.array([3.6 + k * 7.4, 3.2])
    bio.panel(ax, L, (c[0] - 3.3, 6.4))
    bio.label(ax, (c[0], 6.0), name, size="normal", bold=True)
    ax.add_patch(Circle(c, 2.1, facecolor=P.fill("pericycle"), edgecolor=P.edge("pericycle"), lw=1.0, zorder=3))
    ax.add_patch(Circle(c, 1.9, facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=3.2))
    r_in = 0.55 if n > 6 else 0.0
    for i in range(n):
        a = 2 * math.pi * i / n + math.pi / 2
        # xylem arm
        tip = c + 1.8 * np.array([math.cos(a), math.sin(a)])
        side = 0.42 if n <= 4 else 0.18
        base_l = c + r_in * np.array([math.cos(a - side), math.sin(a - side)]) if r_in else c
        base_r = c + r_in * np.array([math.cos(a + side), math.sin(a + side)]) if r_in else c
        if r_in:
            arm = [base_l, tip, base_r]
        else:
            arm = [c + 0.45 * np.array([math.cos(a - math.pi / 2), math.sin(a - math.pi / 2)]), tip,
                   c + 0.45 * np.array([math.cos(a + math.pi / 2), math.sin(a + math.pi / 2)])]
        ax.add_patch(Polygon(arm, closed=True, facecolor=P.fill("xylem"), edgecolor=P.edge("xylem"), lw=0.8, zorder=4))
        # phloem strand between arms
        b = a + math.pi / n
        ax.add_patch(Circle(c + 1.45 * np.array([math.cos(b), math.sin(b)]), 0.28 if n <= 4 else 0.17, facecolor=P.fill("phloem"),
                            edgecolor=P.edge("phloem"), lw=0.8, zorder=4))
        targets = {"xylem": [a], "phloem": [b], "between": [a - math.pi / (2 * n), a + math.pi / (2 * n)]}[rule]
        for t in targets:
            p0 = c + 2.15 * np.array([math.cos(t), math.sin(t)])
            p1 = c + 2.9 * np.array([math.cos(t), math.sin(t)])
            bio.arrow(ax, tuple(p0), tuple(p1), kind="process", color=P.edge("plant"), lw=1.6)
    if r_in:
        ax.add_patch(Circle(c, r_in * 0.9, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cell_wall"), lw=0.6, zorder=4.5))
    sub = {"between": "between xylem and phloem", "xylem": "opposite protoxylem", "phloem": "opposite phloem"}[rule]
    bio.label(ax, (c[0], -0.0 + 0.0), "", size="tiny")
    bio.label(ax, (c[0] + 0.0, -0.35), sub, size="small", color=P.muted())
