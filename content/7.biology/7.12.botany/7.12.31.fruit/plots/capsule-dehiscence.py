"""Modes of capsule dehiscence and the silique. Top row: transverse sections of a three-carpellate capsule
with axile placentation; dehiscence sites in the highlight colour. Loculicidal: along the midrib of each
carpel, into the locules. Septicidal: through the septa, carpels separating. Septifragal: valves fall
away and the septa stay attached to the central column. Bottom row, outer views: poricidal (poppy, a ring
of pores under the stigmatic disc), circumscissile (purslane, a lid), denticidal (Caryophyllaceae,
apical teeth), and a silique (Brassica: two valves detach from the base upwards, seeds stay on the
replum).
"""
import numpy as np
from matplotlib.patches import Circle, Ellipse, PathPatch, Polygon, Wedge
from matplotlib.path import Path

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26.0, 15.5)
WALL, SEED, HI = "ovary", "animal", "highlight"
sc = bio.smooth_closed


def patch(pts, tok, lw=0.9, z=6, fill=None):
    pts = np.asarray(pts, float)
    ax.add_patch(PathPatch(Path(np.vstack([pts, pts[:1]]), closed=True), facecolor=fill or P.fill(tok),
                           edgecolor=P.edge(tok), lw=lw, joinstyle="round", zorder=z))


def arc_band(c, r0, r1, a0, a1, tok, z=6, shift=(0, 0)):
    t = np.radians(np.linspace(a0, a1, 40))
    cx, cy = c[0] + shift[0], c[1] + shift[1]
    outer = np.c_[cx + r1 * np.cos(t), cy + r1 * np.sin(t)]
    inner = np.c_[cx + r0 * np.cos(t[::-1]), cy + r0 * np.sin(t[::-1])]
    patch(np.vstack([outer, inner]), tok, z=z)


def seeds(c, k, r=1.0):
    for s in (-14, 14):
        a = np.radians(90 + 120 * k + s)
        p = (c[0] + r * np.cos(a), c[1] + r * np.sin(a))
        ax.add_patch(Ellipse(p, 0.32, 0.22, angle=np.degrees(a), facecolor=P.fill(SEED), edgecolor=P.edge(SEED), lw=0.6,
                             zorder=8))


def septum(c, a, r0=0.25, r1=1.75, w=0.12, shift=(0, 0), tok=WALL):
    a = np.radians(a)
    u = np.array([np.cos(a), np.sin(a)])
    n = np.array([-u[1], u[0]])
    c = np.asarray(c) + np.asarray(shift)
    patch([c + u * r0 + n * w, c + u * r1 + n * w, c + u * r1 - n * w, c + u * r0 - n * w], tok, lw=0.6, z=7)


R0, R1 = 1.75, 2.1
# loculicidal
c = (4.0, 11.0)
for k in range(3):
    mid = 90 + 120 * k
    for a0, a1 in ((mid - 60, mid - 6), (mid + 6, mid + 60)):
        arc_band(c, R0, R1, a0, a1, WALL)
    a = np.radians(mid)
    ax.plot([c[0] + R0 * np.cos(a), c[0] + R1 * np.cos(a)], [c[1] + R0 * np.sin(a), c[1] + R1 * np.sin(a)],
            color=P.edge(HI), lw=3.0, zorder=9)
    septum(c, mid + 60)
    seeds(c, k)
ax.add_patch(Circle(c, 0.3, facecolor=P.fill(WALL), edgecolor=P.edge(WALL), lw=0.7, zorder=8))
bio.label(ax, (c[0], 7.9), "Loculicidal", bold=True)
bio.label(ax, (c[0], 7.35), "split along each midrib", size="small", color=P.muted())

# septicidal: each carpel separates, septa split
c = (12.4, 11.0)
for k in range(3):
    mid = 90 + 120 * k
    a = np.radians(mid)
    sh = (0.35 * np.cos(a), 0.35 * np.sin(a))
    arc_band(c, R0, R1, mid - 57, mid + 57, WALL, shift=sh)
    septum(c, mid - 58, w=0.06, shift=sh)
    septum(c, mid + 58, w=0.06, shift=sh)
    seeds((c[0] + sh[0], c[1] + sh[1]), k)
    for s in (-60, 60):
        b = np.radians(mid + s)
        ax.plot([c[0] + 0.3 * np.cos(b), c[0] + R1 * np.cos(b)], [c[1] + 0.3 * np.sin(b), c[1] + R1 * np.sin(b)],
                color=P.edge(HI), lw=2.0, zorder=5, alpha=0.8)
bio.label(ax, (c[0], 7.9), "Septicidal", bold=True)
bio.label(ax, (c[0], 7.35), "split through the septa", size="small", color=P.muted())

# septifragal: valves away, septa on the column
c = (20.8, 11.0)
for k in range(3):
    mid = 90 + 120 * k
    a = np.radians(mid)
    sh = (0.55 * np.cos(a), 0.55 * np.sin(a))
    arc_band(c, R0, R1, mid - 55, mid + 55, WALL, shift=sh)
    septum(c, mid + 60, r1=1.65, tok=HI)
    seeds(c, k, 0.9)
ax.add_patch(Circle(c, 0.3, facecolor=P.fill(HI), edgecolor=P.edge(HI), lw=0.7, zorder=8))
bio.label(ax, (c[0], 7.9), "Septifragal", bold=True)
bio.label(ax, (c[0], 7.35), "septa stay on the central column", size="small", color=P.muted())

# poricidal (poppy)
x, y = 3.0, 3.3
patch(sc([(x - 0.9, y - 1.6), (x - 1.25, y - 0.2), (x - 1.0, y + 1.2), (x, y + 1.5), (x + 1.0, y + 1.2), (x + 1.25, y - 0.2),
          (x + 0.9, y - 1.6), (x, y - 1.9)], n=200), WALL)
ax.add_patch(Ellipse((x, y + 1.6), 2.1, 0.45, facecolor=P.fill("bract"), edgecolor=P.edge("bract"), lw=0.8, zorder=8))
for dx in np.linspace(-0.75, 0.75, 6):
    ax.add_patch(Ellipse((x + dx, y + 1.15), 0.18, 0.22, facecolor=P.fill(HI), edgecolor=P.edge(HI), lw=0.6, zorder=9))
ax.plot([x, x], [y - 1.9, y - 2.4], color=P.edge("plant"), lw=2.0, zorder=5)
bio.label(ax, (x, 0.55), "Poricidal", bold=True)
bio.label(ax, (x, 0.0 + 0.05), "poppy", size="small", color=P.muted())

# circumscissile (pyxis)
x = 9.3
patch(sc([(x - 1.0, y + 0.3), (x - 1.1, y - 0.6), (x - 0.7, y - 1.5), (x + 0.7, y - 1.5), (x + 1.1, y - 0.6), (x + 1.0, y + 0.3)],
         n=160), WALL)
lid = sc([(x - 1.0, y + 0.85), (x - 0.6, y + 1.6), (x + 0.6, y + 1.6), (x + 1.0, y + 0.85)], n=120)
patch(lid, WALL, z=7)
ax.plot([x - 1.05, x + 1.05], [y + 0.32, y + 0.32], color=P.edge(HI), lw=3, zorder=9)
for dx in (-0.4, 0, 0.4):
    ax.add_patch(Circle((x + dx, y + 0.1), 0.14, facecolor=P.fill(SEED), edgecolor=P.edge(SEED), lw=0.5, zorder=9))
ax.plot([x, x], [y - 1.5, y - 2.1], color=P.edge("plant"), lw=2.0, zorder=5)
bio.label(ax, (x, 0.55), "Circumscissile", bold=True)
bio.label(ax, (x, 0.05), "purslane, plantain", size="small", color=P.muted())

# denticidal
x = 15.0
pts = [(x - 0.7, y - 1.6), (x - 0.8, y + 1.0)]
for k in range(5):
    x0 = x - 0.8 + 0.32 * k
    pts += [(x0 + 0.16, y + 1.55), (x0 + 0.32, y + 1.05)]
pts += [(x + 0.8, y + 1.0), (x + 0.7, y - 1.6)]
patch(pts, WALL)
for k in range(5):
    x0 = x - 0.8 + 0.32 * k
    ax.plot([x0 + 0.16, x0 + 0.32], [y + 1.55, y + 1.05], color=P.edge(HI), lw=2.0, zorder=9)
ax.add_patch(Ellipse((x, y - 1.6), 1.6, 0.4, facecolor=P.fill("sepal"), edgecolor=P.edge("sepal"), lw=0.7, zorder=7))
ax.plot([x, x], [y - 1.8, y - 2.3], color=P.edge("plant"), lw=2.0, zorder=5)
bio.label(ax, (x, 0.55), "Denticidal", bold=True)
bio.label(ax, (x, 0.05), "Caryophyllaceae", size="small", color=P.muted())

# silique
x = 21.8
ax.plot([x, x], [y - 2.4, y + 2.1], color=P.edge("plant"), lw=1.6, zorder=6)
rep = [(x - 0.12, y - 1.7), (x + 0.12, y - 1.7), (x + 0.12, y + 1.6), (x, y + 1.85), (x - 0.12, y + 1.6)]
patch(rep, HI, lw=0.7, z=7)
for yy in np.linspace(y - 1.4, y + 1.3, 7):
    for s in (-1, 1):
        ax.add_patch(Circle((x + s * 0.24, yy), 0.12, facecolor=P.fill(SEED), edgecolor=P.edge(SEED), lw=0.5, zorder=8))
for s in (-1, 1):
    v = [(x + s * 0.3, y + 1.6), (x + s * 0.6, y + 1.3), (x + s * 1.2, y - 0.4), (x + s * 1.55, y - 1.6), (x + s * 1.25, y - 1.75),
         (x + s * 0.8, y - 0.5), (x + s * 0.3, y + 1.2)]
    patch(sc(v, n=120), WALL, z=6)
bio.callout(ax, (x + 0.1, y + 0.6), (x + 2.2, y + 1.9), "Replum")
bio.callout(ax, (x + 1.25, y - 0.9), (x + 2.2, y - 1.4), "Valve")
bio.label(ax, (x, 0.55), "Silique", bold=True)
bio.label(ax, (x, 0.05), "cabbage: valves detach upwards", size="small", color=P.muted())
