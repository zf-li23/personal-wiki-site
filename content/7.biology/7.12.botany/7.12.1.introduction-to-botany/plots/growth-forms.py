"""Growth forms of seed plants (schematic, not to scale). A tree has a single dominant trunk that
branches well above the ground; a shrub branches at or near ground level into several stems of
similar size; a subshrub is woody only at the base, its upper shoots dying back each
winter (drawn as green shoots on a short woody base); a herb
has soft, little-lignified stems (here a leafy shoot of an annual); a vine cannot stand by itself
and twines round, or climbs on, a support (here a stem twining round a pole).
"""

import math

import numpy as np
import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(26, 11)
ground = 1.4
ax.plot([0.3, 25.7], [ground, ground], color=P.muted(), lw=1.0, zorder=3)

# tree
B.crown_tree(ax, (3.6, ground), 7.6, crown=(0.42, 0.40), seed=2)
bio.label(ax, (3.6, 0.6), "Tree", bold=True)

# shrub: several stems of similar size from the base, each ending in leafy twigs
from matplotlib.patches import Circle

rng = np.random.default_rng(3)
sx = 8.8
for a in (58, 70, 82, 94, 106, 118):
    r = math.radians(a)
    L = 2.6 + 0.5 * rng.random()
    tip = (sx + L * math.cos(r), ground + L * math.sin(r))
    ax.plot([sx + 0.05 * (a - 88) / 10, tip[0]], [ground, tip[1]], color=P.edge("bone"), lw=2.0, zorder=5,
            solid_capstyle="round")
    for b in (-28, 0, 28):
        rb = math.radians(a + b)
        q = (tip[0] + 0.6 * math.cos(rb), tip[1] + 0.6 * math.sin(rb))
        ax.plot([tip[0], q[0]], [tip[1], q[1]], color=P.edge("bone"), lw=1.0, zorder=5)
        ax.add_patch(Circle(q, 0.32, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=0.8, zorder=6))
bio.label(ax, (8.8, 0.6), "Shrub", bold=True)

# subshrub: short woody base with herbaceous upper shoots that die back each winter
base = np.array([12.8, ground])
for dx in (-0.35, 0.0, 0.35):
    ax.plot([base[0] + dx * 0.4, base[0] + dx], [ground, ground + 0.9], color=P.edge("bone"), lw=3.2, zorder=6,
            solid_capstyle="round")
    B.shoot(ax, (base[0] + dx, ground + 0.9), 2.4, arrangement="alternate", nodes=4, leaf_length=0.55)
bio.callout(ax, (base[0] - 0.12, ground + 0.5), (base[0] - 1.9, ground + 0.4), "woody base", size="tiny")
bio.label(ax, (12.8, 0.6), "Subshrub", bold=True)

# herb (annual): leafy shoot with a flower and a fibrous root system below ground
B.shoot(ax, (17.0, ground), 4.2, arrangement="opposite", nodes=4, leaf_length=0.9)
B.flower(ax, (17.0, ground + 4.45), 0.35)
for a in np.linspace(-150, -30, 7):
    r = math.radians(a)
    ax.plot([17.0, 17.0 + 0.8 * math.cos(r)], [ground, ground + 0.8 * math.sin(r) * 0.9], color=P.edge("bone"),
            lw=0.8, zorder=4)
bio.label(ax, (17.0, 0.6), "Herb", bold=True)

# vine twining on a support
px = 22.6
ax.plot([px, px], [ground, ground + 8.4], color=P.edge("neutral"), lw=5.0, zorder=4, solid_capstyle="butt")
t = np.linspace(0, 5.2 * 2 * math.pi, 600)
x = px + 0.38 * np.sin(t)
y = ground + 0.05 + t / t[-1] * 7.8
front = np.cos(t) > 0
xs, ys = x.copy(), y.copy()
xs[~front], ys[~front] = np.nan, np.nan
xb, yb = x.copy(), y.copy()
xb[front], yb[front] = np.nan, np.nan
ax.plot(xb, yb, color=P.edge("plant"), lw=1.4, zorder=3.5, alpha=0.55)
ax.plot(xs, ys, color=P.edge("plant"), lw=1.8, zorder=5)
for k in range(1, 9):
    i = int(k / 9 * 599)
    side = 1 if k % 2 else -1
    B.leaf(ax, (x[i], y[i]), 0.85, angle=90 - side * 55, shape="cordate", venation="palmate")
bio.label(ax, (px, 0.6), "Vine (twining)", bold=True)
