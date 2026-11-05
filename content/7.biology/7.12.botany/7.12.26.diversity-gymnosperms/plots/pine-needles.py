"""Cross sections of pine needle fascicles (schematic). The needles of one fascicle fit together into a
cylinder, so their cross section is a half circle (two needles), a sector of 120 degrees (three) or of 72
degrees (five). Inside the hypodermis lies the mesophyll with resin ducts, and inside the endodermis the
transfusion tissue with one vascular bundle (subgenus Strobus, soft pines) or two (subgenus Pinus, hard
pines). Examples: Pinus tabuliformis (2 needles, 2 bundles, resin ducts marginal), P. bungeana (3 needles,
1 bundle; a soft pine), P. massoniana (2 needles, 2 bundles), P. koraiensis (5 needles, 1 bundle, resin
ducts medial)."""
import numpy as np
from matplotlib.patches import Circle, Ellipse, Polygon

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(28, 10)


def needle(c, r, a0, a1, bundles, ducts, gap=0.06):
    """One needle: sector a0..a1 (deg) of radius r around c."""
    cx, cy = c
    am = np.radians((a0 + a1) / 2)
    off = np.array([np.cos(am), np.sin(am)]) * gap
    t = np.radians(np.linspace(a0, a1, 60))
    pts = np.vstack([[cx + off[0], cy + off[1]], np.c_[cx + off[0] + r * np.cos(t), cy + off[1] + r * np.sin(t)]])
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.2, zorder=5))
    inner = np.vstack([[cx + off[0] * 3.2, cy + off[1] * 3.2],
                       np.c_[cx + off[0] + (r - 0.13) * np.cos(t[3:-3]), cy + off[1] + (r - 0.13) * np.sin(t[3:-3])]])
    ax.add_patch(Polygon(inner, closed=True, fill=False, edgecolor=P.edge("protein"), lw=0.8, zorder=6))
    span = np.radians(a1 - a0)
    ctr = np.array([cx, cy]) + off + np.array([np.cos(am), np.sin(am)]) * r * (0.42 if span > 2 else 0.5)
    ew = r * (0.55 if span > 2 else 0.4)
    ax.add_patch(Ellipse(ctr, ew, ew * 0.7, angle=np.degrees(am) + 90, facecolor=P.light("golgi"), edgecolor=P.edge("golgi"), lw=0.9,
                         zorder=7))
    tang = np.array([-np.sin(am), np.cos(am)])
    for k in range(bundles):
        p = ctr + tang * (0 if bundles == 1 else (k - 0.5) * ew * 0.42)
        ax.add_patch(Circle(p, ew * 0.13, facecolor=P.fill("channel"), edgecolor=P.edge("channel"), lw=0.6, zorder=8))
    for kind, frac in ducts:
        a = np.radians(a0 + (a1 - a0) * frac)
        rr = r - 0.22 if kind == "marginal" else r * 0.72
        p = np.array([cx, cy]) + off + rr * np.array([np.cos(a), np.sin(a)])
        ax.add_patch(Circle(p, 0.075, facecolor=P.surface(), edgecolor=P.edge("highlight"), lw=0.9, zorder=8))


R = 2.3
panels = [
    (r"$\it{Pinus\ tabuliformis}$", "2 needles, 2 bundles", r"subg. $\it{Pinus}$", 2, 2, [("marginal", f) for f in (0.12, 0.3, 0.5, 0.7, 0.88)]),
    (r"$\it{P.\ massoniana}$", "2 needles, 2 bundles", r"subg. $\it{Pinus}$", 2, 2, [("marginal", f) for f in (0.15, 0.38, 0.62, 0.85)]),
    (r"$\it{P.\ bungeana}$", "3 needles, 1 bundle", r"subg. $\it{Strobus}$", 3, 1, [("marginal", f) for f in (0.15, 0.5, 0.85)]),
    (r"$\it{P.\ koraiensis}$", "5 needles, 1 bundle", r"subg. $\it{Strobus}$", 5, 1, [("medial", f) for f in (0.2, 0.5, 0.8)]),
]
for k, (name, l1, l2, n, b, ducts) in enumerate(panels):
    c = (3.5 + 7.0 * k, 5.0)
    for i in range(n):
        a0 = 90 + 360 / n * i
        needle(c, R, a0, a0 + 360 / n, b, ducts)
    bio.label(ax, (c[0], 9.3), name, size="normal")
    bio.label(ax, (c[0], 1.8), l1, size="small")
    bio.label(ax, (c[0], 1.2), l2, size="small", color=P.muted())
c = (3.5, 5.0)
bio.callout(ax, (c[0] - 1.6, c[1] + 1.4), (c[0] - 3.0, c[1] + 3.6), "hypodermis")
bio.callout(ax, (c[0] - 0.97, c[1] + 0.62), (c[0] + 0.2, c[1] + 3.6), "endodermis")
bio.callout(ax, (c[0] - 0.97, c[1] + 0.27), (c[0] + 2.4, c[1] + 3.3), "vascular bundles")
bio.label(ax, (14.0, 0.4), "Open circles: resin ducts (marginal: next to the hypodermis; medial: in the mesophyll)", size="small",
          color=P.muted())
