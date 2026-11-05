"""Carpogonial branch and cystocarp of Polysiphonia (schematic). A: before fertilization. A pericentral cell of
a fertile segment becomes the supporting cell and bears a four-celled carpogonial branch; its terminal cell, the
carpogonium, extends into a long trichogyne, to which a spermatium has attached. B: after fertilization. The
supporting cell cuts off an auxiliary cell, the zygote nucleus passes into it, and supporting cell, auxiliary
cell and sterile filaments fuse into a large fusion (placental) cell, which produces gonimoblast filaments
ending in carposporangia; the surrounding gametophyte cells form an urn-shaped pericarp with an ostiole."""
import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, PathPatch
from matplotlib.path import Path
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26, 14)
R, CP, GN = "negative", "highlight", "dna"


def rcell(c, w, h, tok=R, strong=False, z=5):
    ax.add_patch(FancyBboxPatch((c[0] - w / 2, c[1] - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.15",
                                facecolor=P.fill(tok) if strong else P.light(tok), edgecolor=P.edge(tok), lw=1.0, zorder=z))


# ---- A
bio.panel(ax, "A", (0.2, 13.8))
bio.label(ax, (0.8, 13.55), "Before fertilization", size="small", bold=True, ha="left")
for k in range(5):
    rcell((3.0, 2.0 + 1.9 * k), 1.0, 1.7, strong=True)
bio.label(ax, (3.0, 1.0), "axial cells", size="tiny", color=P.muted())
sc = np.array([4.5, 5.9])
rcell(sc, 1.2, 1.4, tok=CP, strong=True)
bio.callout(ax, sc + np.array([0.3, -0.5]), (6.6, 2.6), "supporting cell", size="tiny")
pts = [sc + np.array([0.9, 0.5]), sc + np.array([1.6, 1.3]), sc + np.array([1.7, 2.3]), sc + np.array([1.2, 3.1])]
for p in pts[:3]:
    rcell(p, 0.7, 0.7, tok=CP)
cp = pts[3]
ax.add_patch(Ellipse(cp, 0.9, 1.1, facecolor=P.fill(CP), edgecolor=P.edge(CP), lw=1.2, zorder=6))
ax.add_patch(Circle(cp + np.array([0, -0.15]), 0.18, color=P.edge("nucleus"), zorder=7))
t = np.linspace(0, 1, 60)
tr = np.c_[cp[0] - 0.1 + 0.6 * np.sin(2.2 * t) * t, cp[1] + 0.5 + 3.2 * t]
ax.plot(tr[:, 0], tr[:, 1], color=P.edge(CP), lw=3.0, solid_capstyle="round", zorder=6)
ax.add_patch(Circle(tr[-1] + np.array([0.25, 0.05]), 0.25, facecolor=P.fill("rna"), edgecolor=P.edge("rna"), lw=1.0, zorder=8))
bio.callout(ax, tuple(tr[30]), (8.6, 10.2), "trichogyne", size="tiny")
bio.callout(ax, tuple(cp), (8.6, 8.4), "carpogonium (egg nucleus)", size="tiny")
bio.callout(ax, tuple(pts[1]), (8.6, 6.8), "carpogonial branch (4 cells)", size="tiny")
bio.callout(ax, tuple(tr[-1] + np.array([0.25, 0.05])), (8.6, 12.4), "spermatium", size="tiny")
for k in range(3):
    rcell(sc + np.array([0.5 + 0.45 * k, -1.0 - 0.25 * k]), 0.4, 0.4)
bio.label(ax, (6.3, 4.2), "sterile filament", size="tiny", color=P.muted(), ha="left")

# ---- B
bio.panel(ax, "B", (13.2, 13.8))
bio.label(ax, (13.8, 13.55), "Cystocarp after fertilization", size="small", bold=True, ha="left")
cx, cy = 19.2, 6.0
verts = []
t = np.linspace(-1, 1, 80)
outer_x = cx + 4.2 * np.sin(np.pi / 2 * t) * (1 - 0.35 * np.clip(t, 0, 1) ** 4) * 1.0
# urn outline: bottom wide, narrowing to an ostiole at the top
yy = np.linspace(0, 1, 60)
half = 3.6 * np.sin(np.pi * (0.12 + 0.82 * yy)) + 0.35
left = np.c_[cx - half, cy - 3.6 + 8.0 * yy]
right = np.c_[cx + half, cy - 3.6 + 8.0 * yy][::-1]
ax.fill(np.r_[left[:, 0], right[:, 0]], np.r_[left[:, 1], right[:, 1]], facecolor=P.light(R), edgecolor=P.edge(R), lw=1.3, zorder=3)
inner_half = half - 0.6
li = np.c_[cx - inner_half, cy - 3.0 + 7.4 * yy]
ri = np.c_[cx + inner_half, cy - 3.0 + 7.4 * yy][::-1]
ax.fill(np.r_[li[:, 0], ri[:, 0]], np.r_[li[:, 1], ri[:, 1]], facecolor=P.fill("cytoplasm"), edgecolor=P.edge(R), lw=0.8, zorder=4)
bio.callout(ax, (cx - half[30] + 0.3, cy - 3.6 + 8.0 * 0.5), (14.3, 9.0), "pericarp", size="tiny")
bio.label(ax, (cx, cy + 4.85), "ostiole", size="tiny")
fc = np.array([cx, cy - 1.9])
ax.add_patch(Ellipse(fc, 2.6, 1.1, facecolor=P.fill(GN), edgecolor=P.edge(GN), lw=1.2, zorder=6))
bio.callout(ax, tuple(fc + np.array([1.0, -0.2])), (24.2, 1.2), "fusion (placental) cell", size="tiny")
rng = np.random.default_rng(2)
for a in np.linspace(35, 145, 7):
    r = np.radians(a)
    p0 = fc + np.array([0.9 * np.cos(r), 0.4 * np.sin(r)])
    p1 = fc + np.array([2.0 * np.cos(r), 2.8 * np.sin(r)])
    ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=P.edge(GN), lw=2.0, zorder=5)
    ax.add_patch(Ellipse(p1 + np.array([0.3 * np.cos(r), 0.45 * np.sin(r)]), 0.7, 0.95, angle=a - 90,
                         facecolor=P.fill(GN), edgecolor=P.edge(GN), lw=1.0, zorder=6))
bio.callout(ax, (cx + 2.0 * np.cos(np.radians(55)) + 0.2, fc[1] + 2.8 * np.sin(np.radians(55)) + 0.4), (24.2, 8.6), "carposporangium (2n)", size="tiny")
bio.callout(ax, (cx + 1.2 * np.cos(np.radians(125)), fc[1] + 1.6 * np.sin(np.radians(125))), (14.3, 3.6), "gonimoblast filament", size="tiny")
bio.label(ax, (19.2, 0.9), "carposporophyte (2n) + pericarp (n) = cystocarp", size="tiny", color=P.muted())
