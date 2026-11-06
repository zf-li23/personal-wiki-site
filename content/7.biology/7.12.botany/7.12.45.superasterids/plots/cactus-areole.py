# Cactaceae: the areole and its homology. A: Pereskia, with ordinary flat leaves; the short shoot in
# each leaf axil (areole) bears spines. B: a flattened stem segment (cladode) of Opuntia with areoles
# in a spiral, each with long spines and a tuft of barbed glochids; a flower and a new segment arise
# from areoles. C: an areole enlarged: a condensed short shoot whose spines are modified leaves around
# a central growing point. D: cross-section of a columnar cactus: ribs, epidermis, green
# chlorenchyma, central water-storage parenchyma and a ring of vascular bundles.
import numpy as np
from matplotlib.patches import Circle, Ellipse, Polygon

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(34, 13)


def areole(c, r=0.18, spines=5, length=0.7, glochids=True, seed=0):
    rng = np.random.default_rng(seed)
    for k in range(spines):
        a = np.radians(30 + 300 / max(1, spines - 1) * k + rng.uniform(-8, 8))
        ax.plot([c[0], c[0] + length * np.cos(a)], [c[1], c[1] + length * np.sin(a)], color=P.ink(), lw=0.8, zorder=8)
    ax.add_patch(Circle(c, r, facecolor=P.light("neutral"), edgecolor=P.edge("neutral"), lw=0.6, zorder=9))
    if glochids:
        for k in range(8):
            a = rng.uniform(0, 2 * np.pi)
            ax.plot([c[0], c[0] + 0.25 * np.cos(a)], [c[1], c[1] + 0.25 * np.sin(a)], color=P.edge("anther"), lw=0.5, zorder=9)


# A: Pereskia
bio.panel(ax, "A", (0.3, 12.8))
x = 4.2
bio.shape(ax, [(x - 0.2, 0.6), (x + 0.2, 0.6), (x + 0.15, 11.6), (x - 0.15, 11.6)], token="plant", lw=0.9, zorder=3)
for i, y in enumerate((2.6, 5.2, 7.8, 10.2)):
    s = 1 if i % 2 == 0 else -1
    t = np.linspace(0, 1, 40)
    base = np.array([x + s * 0.15, y])
    up = np.c_[base[0] + s * 3.0 * t, base[1] + 0.6 * t + 0.7 * np.sin(np.pi * t)]
    lo = np.c_[base[0] + s * 3.0 * t[::-1], base[1] + 0.6 * t[::-1] - 0.7 * np.sin(np.pi * t[::-1])]
    bio.shape(ax, np.vstack([up, lo]), token="plant", lw=0.9, zorder=4)
    areole((x + s * 0.25, y + 0.35), spines=3, length=0.6, glochids=False, seed=i)
bio.label(ax, (4.2, 12.2), "Pereskia", italic=True, size="title")
bio.callout(ax, (x - 0.25, 5.55), (6.6, 6.4), "Areole in leaf axil")
bio.callout(ax, (x + 2.0, 2.9), (6.6, 1.2), "Leaf")

# B: Opuntia cladode
bio.panel(ax, "B", (8.6, 12.8))
c = np.array([12.6, 5.6])
ax.add_patch(Ellipse(c, 5.2, 8.2, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.2, zorder=4))
ax.add_patch(Ellipse(c + (1.6, 5.0), 2.0, 2.8, angle=-25, facecolor=P.light("plant"), edgecolor=P.edge("plant"), lw=1.0, zorder=3))
k = 0
for i in range(-3, 4):
    for j in range(-2, 3):
        p = c + np.array([1.0 * j + 0.5 * (i % 2), 1.05 * i])
        if ((p - c) / np.array([2.3, 3.7])) @ ((p - c) / np.array([2.3, 3.7])) < 1:
            areole(p, spines=2, length=0.55, seed=k)
            k += 1
# flower on a marginal areole
f = c + np.array([-2.2, 3.4])
for a in np.linspace(0, 2 * np.pi, 9)[:-1]:
    ax.add_patch(Ellipse(f + 0.45 * np.array([np.cos(a), np.sin(a)]), 0.8, 0.45, angle=np.degrees(a), facecolor=P.fill("anther"),
                         edgecolor=P.edge("anther"), lw=0.6, zorder=10))
ax.add_patch(Circle(f, 0.28, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=0.6, zorder=11))
bio.label(ax, (12.6, 12.2), "Opuntia", italic=True, size="title")
bio.callout(ax, f + (-0.5, 0.3), (9.0, 11.0), "Flower from an areole")
bio.callout(ax, c + (2.4, 5.6), (16.6, 11.4), "New segment")
bio.callout(ax, c + (1.0, -1.05), (16.8, 2.6), "Areole: spines + glochids")

# C: areole enlarged
bio.panel(ax, "C", (17.8, 12.8))
c = np.array([21.6, 6.6])
ax.add_patch(Circle(c, 2.9, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.0, zorder=3))
ax.add_patch(Circle(c, 1.1, facecolor=P.light("neutral"), edgecolor=P.edge("neutral"), lw=0.8, zorder=4))
for k in range(9):
    a = np.radians(k * 40 + 10)
    d = np.array([np.cos(a), np.sin(a)])
    q0, q1 = c + 0.6 * d, c + (3.6 if k % 3 else 4.2) * d
    ax.add_patch(Polygon([q0 + 0.12 * d[::-1] * (1, -1), q1, q0 - 0.12 * d[::-1] * (1, -1)], closed=True,
                                  facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=0.6, zorder=6))
ax.add_patch(Circle(c, 0.35, facecolor=P.fill("positive"), edgecolor=P.edge("positive"), lw=0.6, zorder=7))
bio.callout(ax, c + (0.0, 0.3), (25.6, 11.0), "Growing point (axillary bud)")
bio.callout(ax, c + (1.93, 2.3), (25.6, 9.6), "Spine (modified leaf)")
bio.callout(ax, c + (-0.6, -0.7), (21.0, 0.6), "Areole cushion (hairs)")

# D: cross-section of a columnar cactus
bio.panel(ax, "D", (26.4, 12.8))
c = np.array([30.4, 6.4])
ang = np.linspace(0, 2 * np.pi, 400)
r = 2.9 + 0.35 * np.cos(8 * ang)
bio.shape(ax, np.c_[c[0] + r * np.cos(ang), c[1] + r * np.sin(ang)], token="plant", lw=1.2, zorder=3)
r2 = r - 0.7
ax.fill(c[0] + r2 * np.cos(ang), c[1] + r2 * np.sin(ang), color=P.light("vacuole"), zorder=4)
for k in range(16):
    a = 2 * np.pi * k / 16
    ax.add_patch(Ellipse(c + 1.35 * np.array([np.cos(a), np.sin(a)]), 0.3, 0.2, angle=np.degrees(a), facecolor=P.fill("xylem"),
                         edgecolor=P.edge("xylem"), lw=0.5, zorder=5))
bio.callout(ax, c + (3.2, 0.0), (33.6, 10.8), "Rib")
bio.callout(ax, c + (-2.55, -0.9), (27.0, 1.2), "Chlorenchyma")
bio.callout(ax, c + (0.0, 0.3), (33.6, 2.0), "Water-storage parenchyma")
bio.callout(ax, c + (1.35, 0.0), (33.6, 8.6), "Vascular bundles")
