# Schematic structure of a lymph node (A) and of a cross-section through splenic white pulp (B).
import numpy as np
from matplotlib.patches import Circle, Ellipse, PathPatch
from matplotlib.path import Path

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24.0, 11.0)


def fill_path(pts, tok, z=3, lw=1.2, light=False):
    ax.add_patch(PathPatch(Path(pts, closed=True), facecolor=P.light(tok) if light else P.fill(tok),
                           edgecolor=P.edge(tok), lw=lw, zorder=z))


# ---- A: lymph node -------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 10.9))
c = np.array([7.0, 5.4])
th = np.linspace(0, 2 * np.pi, 300)
rx, ry = 5.6, 4.3
# bean: an ellipse with an indentation (hilum) on the right
r_in = 1 - 0.28 * np.exp(-((th - 0.0 + np.pi) % (2 * np.pi) - np.pi) ** 2 / 0.12)
outer = np.c_[c[0] + rx * r_in * np.cos(th), c[1] + ry * r_in * np.sin(th)]
fill_path(outer, "neutral", z=2, light=True)                     # capsule + subcapsular sinus
fill_path(np.c_[c[0] + (rx - 0.35) * r_in * np.cos(th), c[1] + (ry - 0.35) * r_in * np.sin(th)], "dna2", z=3, light=True)
# paracortex band
fill_path(np.c_[c[0] - 0.6 + 3.6 * r_in * np.cos(th), c[1] + 2.75 * r_in * np.sin(th)], "channel", z=4)
# medulla near hilum
fill_path(np.c_[c[0] + 2.2 + 1.7 * np.cos(th), c[1] + 1.9 * np.sin(th)], "antibody", z=5, light=True)
for k in range(5):
    a = -1.0 + k * 0.5
    ax.plot([c[0] + 2.2 + 0.2 * np.cos(a), c[0] + 2.2 + 1.6 * np.cos(a)],
            [c[1] + 0.2 * np.sin(a), c[1] + 1.8 * np.sin(a)], color=P.edge("antibody"), lw=2.4, zorder=6)
# follicles around the outer cortex
for ang, gc in ((95, True), (135, False), (175, True), (215, False), (255, True), (60, False), (300, False)):
    a = np.radians(ang)
    fx, fy = c[0] + 4.45 * np.cos(a), c[1] + 3.25 * np.sin(a)
    ax.add_patch(Circle((fx, fy), 0.72, facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=1.0, zorder=7))
    if gc:
        ax.add_patch(Circle((fx, fy), 0.4, facecolor=P.light("highlight"), edgecolor=P.edge("highlight"), lw=0.8, zorder=8))
# HEVs in the paracortex
for x, y in ((4.2, 6.4), (5.4, 3.6), (6.5, 7.0), (3.6, 4.6), (6.9, 4.4), (5.0, 5.4)):
    ax.add_patch(Circle((x, y), 0.17, facecolor=P.fill("blood"), edgecolor=P.edge("blood"), lw=0.8, zorder=9))
    ax.add_patch(Circle((x, y), 0.07, facecolor=P.surface(), edgecolor="none", zorder=9.5))
# afferent and efferent lymphatics, vessels at the hilum
for ang in (110, 150, 200, 245):
    a = np.radians(ang)
    p0 = (c[0] + 6.6 * np.cos(a), c[1] + 5.1 * np.sin(a))
    p1 = (c[0] + 5.65 * np.cos(a), c[1] + 4.35 * np.sin(a))
    bio.arrow(ax, p0, p1, kind="process", head=0.17, color=P.edge("dna2"))
bio.arrow(ax, (c[0] + 4.0, c[1] + 0.25), (c[0] + 6.4, c[1] + 0.9), kind="process", head=0.18, color=P.edge("dna2"))
ax.plot([c[0] + 4.0, c[0] + 6.4], [c[1] - 0.25, c[1] - 0.75], color=P.edge("blood"), lw=2.6, zorder=6)
bio.callout(ax, (c[0] + np.cos(np.radians(150)) * 6.3, c[1] + np.sin(np.radians(150)) * 4.9), (0.9, 10.3),
            "afferent lymphatics")
bio.callout(ax, (c[0] + 6.0, c[1] + 0.82), (13.4, 7.6), "efferent lymphatic")
bio.callout(ax, (c[0] + 6.0, c[1] - 0.66), (13.4, 3.4), "artery and vein (hilum)")
bio.callout(ax, (c[0] + 4.45 * np.cos(np.radians(95)), c[1] + 3.25 * np.sin(np.radians(95)) + 0.3), (7.9, 10.6),
            "secondary follicle with germinal center")
bio.callout(ax, (c[0] + 4.45 * np.cos(np.radians(135)) - 0.3, c[1] + 3.25 * np.sin(np.radians(135))), (2.0, 9.6),
            "primary follicle (B cells)")
bio.callout(ax, (5.9, 5.8), (0.5, 1.0), "paracortex (T cells, DCs)")
bio.callout(ax, (5.4, 3.6), (5.0, 0.4), "HEV")
bio.callout(ax, (c[0] + 3.0, c[1] - 0.8), (10.2, 0.6), "medulla: cords and sinuses")
bio.callout(ax, (c[0] - 2.5, c[1] + 3.85), (0.3, 8.5), "subcapsular sinus")

# ---- B: splenic white pulp -----------------------------------------------------------------------------
bio.panel(ax, "B", (15.0, 10.9))
cx, cy = 19.6, 5.3
ax.add_patch(Circle((cx, cy), 4.2, facecolor=P.light("blood"), edgecolor=P.edge("blood"), lw=1.0, zorder=2))
for k in range(26):
    a = k * 2 * np.pi / 26
    rr = 3.85 + 0.15 * np.sin(5 * a)
    ax.add_patch(Ellipse((cx + rr * np.cos(a), cy + rr * np.sin(a)), 0.32, 0.2, angle=np.degrees(a),
                         facecolor=P.fill("blood"), edgecolor=P.edge("blood"), lw=0.4, zorder=2.5))
ax.add_patch(Circle((cx, cy), 3.0, facecolor=P.light("enzyme"), edgecolor=P.edge("enzyme"), lw=1.0, zorder=3))
ax.add_patch(Circle((cx, cy), 2.72, fill=False, edgecolor=P.edge("blood"), lw=1.0, ls="--", zorder=3.5))
ax.add_patch(Circle((cx - 0.5, cy - 0.3), 1.6, facecolor=P.fill("channel"), edgecolor=P.edge("channel"), lw=1.0, zorder=4))
ax.add_patch(Circle((cx + 1.2, cy + 1.05), 1.2, facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=1.0, zorder=5))
ax.add_patch(Circle((cx + 1.3, cy + 1.15), 0.6, facecolor=P.light("highlight"), edgecolor=P.edge("highlight"), lw=0.8, zorder=6))
ax.add_patch(Circle((cx - 0.5, cy - 0.3), 0.26, facecolor=P.fill("blood"), edgecolor=P.edge("blood"), lw=1.2, zorder=7))
bio.callout(ax, (cx - 0.5, cy - 0.3), (15.6, 1.2), "central arteriole")
bio.callout(ax, (cx - 1.3, cy - 1.0), (15.6, 2.3), "PALS (T cells)")
bio.callout(ax, (cx + 1.3, cy + 1.15), (17.6, 10.4), "follicle with germinal center")
bio.callout(ax, (cx - 2.2, cy + 1.6), (15.3, 9.3), "marginal zone")
bio.callout(ax, (cx + 2.0, cy - 1.75), (23.9, 1.0), "marginal sinus")
bio.callout(ax, (cx + 3.7, cy + 1.3), (23.9, 9.6), "red pulp")
