# Recognising Cyperaceae and Poaceae (schematic). A: sedge culm in transverse section, triangular and
# solid, with bundles scattered in ground tissue. B: grass culm internode in transverse section, round and
# hollow, bundles in two rings. C: sedge leaves in three ranks (top view) with a closed tubular sheath.
# D: grass leaves in two ranks (top view) with a sheath split on one side, and a ligule. E: sedge flower:
# one scale subtending three stamens and a pistil with a three-branched style, perianth bristles at the
# base. F: grass floret: lemma and palea enclosing two lodicules, three stamens and a pistil with two
# feathery stigmas.
import numpy as np
from matplotlib.patches import Polygon, Circle, Wedge, Ellipse, PathPatch
from matplotlib.path import Path
import wikibio as bio
from wikibio.core import smooth_closed

P = bio.P
fig, ax = bio.canvas(30, 15)
rng = np.random.default_rng(3)


def head(letter, xy, text):
    bio.panel(ax, letter, (xy[0] - 4.0, xy[1] + 0.2))
    bio.label(ax, xy, text, size="title")


def bundle(p, r=0.16):
    ax.add_patch(Circle(p, r, facecolor=P.fill("xylem"), edgecolor=P.edge("sclerenchyma"), lw=1.0, zorder=6))


# A sedge culm
head("A", (5.0, 14.2), "Sedge culm")
c = np.array([5.0, 10.6])
tri = [c + 2.8 * np.array([np.cos(a), np.sin(a)]) for a in np.radians([90, 210, 330])]
ax.add_patch(PathPatch(Path(smooth_closed(tri + [tri[0] * 0.98 + c * 0.02], n=6), closed=True), alpha=0))
ax.add_patch(Polygon(tri, closed=True, joinstyle="round", facecolor=P.light("parenchyma"), edgecolor=P.edge("plant"), lw=1.6, zorder=4))
for _ in range(22):
    while True:
        p = c + np.array([rng.uniform(-2.4, 2.4), rng.uniform(-1.4, 2.6)])
        bary = np.linalg.solve(np.array([[tri[0][0] - tri[2][0], tri[1][0] - tri[2][0]], [tri[0][1] - tri[2][1], tri[1][1] - tri[2][1]]]), p - tri[2])
        if bary.min() > 0.12 and bary.sum() < 0.88:
            break
    bundle(p)
bio.label(ax, (5.0, 6.9), "triangular, solid", size="small")

# B grass culm
head("B", (14.0, 14.2), "Grass culm")
c2 = np.array([14.0, 10.6])
ax.add_patch(Wedge(c2, 2.6, 0, 360, width=0.9, facecolor=P.light("parenchyma"), edgecolor=P.edge("plant"), lw=1.6, zorder=4))
for k in range(16):
    a = 2 * np.pi * k / 16
    bundle(c2 + 2.3 * np.array([np.cos(a), np.sin(a)]), r=0.12)
    bundle(c2 + 1.95 * np.array([np.cos(a + 0.2), np.sin(a + 0.2)]), r=0.17)
bio.label(ax, (14.0, 6.9), "round, hollow internode", size="small")


def leafblade(base, ang, L, W, token="plant", z=5):
    a = np.radians(ang)
    u = np.array([np.cos(a), np.sin(a)]); v = np.array([-u[1], u[0]])
    pts = [base + v * W / 2, base + u * L * 0.7 + v * W / 2, base + u * L, base + u * L * 0.7 - v * W / 2, base - v * W / 2]
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill(token), edgecolor=P.edge(token), lw=1.1, zorder=z))


# C sedge leaves
head("C", (23.6, 14.2), "Sedge: 3 ranks, closed sheath")
c3 = np.array([23.6, 10.6])
for k, ang in enumerate((90, 210, 330)):
    leafblade(c3 + 0.7 * np.array([np.cos(np.radians(ang)), np.sin(np.radians(ang))]), ang, 2.6, 0.7)
ax.add_patch(Circle(c3, 0.7, facecolor=P.light("plant"), edgecolor=P.edge("plant"), lw=1.4, zorder=6))
ax.add_patch(Polygon([c3 + 0.4 * np.array([np.cos(a), np.sin(a)]) for a in np.radians([90, 210, 330])], closed=True,
                     facecolor=P.fill("parenchyma"), edgecolor=P.edge("plant"), lw=1.0, zorder=7))
bio.callout(ax, c3 + [0.5, -0.5], (27.0, 7.6), "Closed sheath")

# D grass leaves
head("D", (5.0, 6.0), "Grass: 2 ranks, open sheath")
c4 = np.array([5.0, 2.8])
for ang in (90, 270):
    leafblade(c4 + 0.75 * np.array([0, np.sin(np.radians(ang))]), ang, 2.0, 0.8)
ax.add_patch(Wedge(c4, 0.8, 115, 425, width=0.18, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.2, zorder=6))
ax.add_patch(Circle(c4, 0.55, facecolor=P.light("parenchyma"), edgecolor=P.edge("plant"), lw=1.0, zorder=6))
ax.add_patch(Ellipse(c4 + [0, 0.95], 0.6, 0.2, facecolor=P.light("neutral"), edgecolor=P.edge("neutral"), lw=0.9, zorder=8))
bio.callout(ax, c4 + [0.0, 0.85], (8.2, 4.4), "Sheath split")
bio.callout(ax, c4 + [0.25, 0.98], (8.4, 5.4), "Ligule")


def anther(p, s=0.45, z=8):
    ax.add_patch(Ellipse(p, s * 0.45, s * 1.2, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=0.9, zorder=z))


# E sedge flower
head("E", (14.0, 6.0), "Sedge flower")
sc = np.array([12.4, 0.8])
ax.add_patch(PathPatch(Path(smooth_closed([sc + [-1.0, 0.3], sc + [-1.2, 2.6], sc + [-0.6, 4.4], sc + [-0.2, 2.6], sc + [-0.3, 0.3]], n=80),
                            closed=True), facecolor=P.fill("bract"), edgecolor=P.edge("bract"), lw=1.1, zorder=4))
base = np.array([14.2, 1.0])
for dx in (-0.6, 0.0, 0.6):
    ax.plot([base[0] + dx * 0.4, base[0] + dx], [base[1], 3.8], color=P.edge("anther"), lw=0.9, zorder=6)
    anther((base[0] + dx, 4.1))
ax.add_patch(Ellipse((15.6, 1.5), 0.6, 0.9, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=1.0, zorder=6))
ax.plot([15.6, 15.6], [1.95, 3.2], color=P.edge("ovary"), lw=1.0, zorder=6)
for s in (-0.5, 0.0, 0.5):
    ax.plot([15.6, 15.6 + s], [3.2, 4.2], color=P.edge("ovary"), lw=1.0, zorder=6)
for k in range(5):
    ax.plot([15.3 + 0.12 * k, 15.0 + 0.3 * k], [1.0, 2.6], color=P.edge("neutral"), lw=0.7, zorder=5)
bio.callout(ax, sc + [-0.7, 2.4], (10.4, 5.0), "Scale (glume)")
bio.callout(ax, (15.6 + 0.5, 4.2), (16.6, 4.9), "Style 3-branched")
bio.callout(ax, (15.9, 2.2), (17.4, 1.2), "Bristles")

# F grass floret
head("F", (23.6, 6.0), "Grass floret")
for x0, L, W, tok in ((20.8, 4.4, 1.4, "plant"), (22.2, 3.8, 1.1, "plant")):
    ax.add_patch(PathPatch(Path(smooth_closed([(x0 - W / 2, 0.6), (x0 - W / 2, 2.4), (x0, 0.6 + L), (x0 + W / 2, 2.4), (x0 + W / 2, 0.6)], n=80),
                                closed=True), facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.1, zorder=4))
for dx in (-0.25, 0.25):
    ax.add_patch(Ellipse((23.4 + dx, 1.0), 0.35, 0.6, facecolor=P.light("tepal"), edgecolor=P.edge("tepal"), lw=0.8, zorder=5))
for dx in (-0.5, 0.0, 0.5):
    ax.plot([24.6 + dx * 0.3, 24.6 + dx], [0.7, 3.8], color=P.edge("anther"), lw=0.9, zorder=6)
    anther((24.6 + dx, 4.1))
ax.add_patch(Ellipse((26.4, 1.3), 0.6, 0.9, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=1.0, zorder=6))
for s in (-1, 1):
    b0 = np.array([26.4 + 0.15 * s, 1.7])
    ax.plot([b0[0], b0[0] + 0.6 * s], [b0[1], 3.6], color=P.edge("ovary"), lw=1.0, zorder=6)
    for t in np.linspace(0.1, 1, 7):
        p = b0 + np.array([0.6 * s * t, 1.9 * t])
        ax.plot([p[0], p[0] + 0.2 * s], [p[1], p[1] + 0.1], color=P.edge("ovary"), lw=0.6, zorder=6)
bio.callout(ax, (20.8, 2.5), (20.0, 6.3), "Lemma")
bio.callout(ax, (22.2, 2.6), (21.6, 5.9), "Palea")
bio.callout(ax, (23.4, 1.2), (23.8, 2.9), "Lodicules")
bio.callout(ax, (27.0, 3.6), (28.4, 4.6), "Feathery stigmas")
