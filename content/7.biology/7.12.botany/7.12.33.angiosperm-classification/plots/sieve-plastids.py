# Main types of sieve-element plastids (after Behnke's classification). Top: single plastids drawn as
# double-membraned ellipses. S type: starch grains only. PI: one polygonal protein crystal (here with a
# few starch grains). PII: several wedge-shaped (cuneate) protein crystals in a ring (monocots). PIII: a
# peripheral ring of protein filaments around a central crystal (Caryophyllales). Bottom: a sieve-tube
# element in longitudinal section with plastids lying against the wall, P-protein strands, sieve plates
# with callose and an adjacent companion cell.
import math

import numpy as np
import wikibio as bio
from matplotlib.patches import Ellipse, FancyBboxPatch, Polygon, Rectangle

P = bio.P
fig, ax = bio.canvas(28, 15.6)


def plastid(c, w=4.6, h=3.4):
    ax.add_patch(Ellipse(c, w, h, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("chloroplast"), lw=1.6, zorder=5))
    ax.add_patch(Ellipse(c, w - 0.28, h - 0.28, fill=False, edgecolor=P.edge("chloroplast"), lw=0.9, zorder=6))


def starch(c, r):
    ax.add_patch(Ellipse(c, 2 * r, 1.7 * r, facecolor=P.fill("carbohydrate"), edgecolor=P.edge("carbohydrate"), lw=1.0,
                         zorder=7))
    ax.add_patch(Ellipse(c, 0.9 * r, 0.7 * r, fill=False, edgecolor=P.edge("carbohydrate"), lw=0.6, zorder=8))


def crystal(pts):
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=1.0, zorder=7))


X = [3.6, 10.4, 17.2, 24.0]
Y = 12.6
NAMES = [("S type", "starch grains only", "most eudicots"), ("PI type", "one polygonal crystal", "many magnoliids"),
         ("PII type", "cuneate crystals in a ring", "monocots"), ("PIII type", "ring of protein filaments",
                                                                 "Caryophyllales")]
for x, (t, d, w) in zip(X, NAMES):
    plastid((x, Y))
    bio.label(ax, (x, Y + 2.35), t, size="title")
    bio.label(ax, (x, Y - 2.25), d, size="small")
    bio.label(ax, (x, Y - 2.85), w, size="small", italic=False, color=P.muted())
# S type
for dx, dy, r in [(-0.9, 0.5, 0.55), (0.6, 0.7, 0.45), (0.2, -0.6, 0.6), (-1.2, -0.5, 0.35), (1.3, -0.3, 0.38)]:
    starch((X[0] + dx, Y + dy), r)
# PI type
c = np.array([X[1] + 0.2, Y])
crystal([c + 0.85 * np.array([math.cos(a), math.sin(a)]) for a in np.linspace(0.3, 2 * math.pi + 0.3, 7)[:-1]])
starch((X[1] - 1.3, Y + 0.6), 0.35)
starch((X[1] - 1.2, Y - 0.6), 0.3)
# PII type: wedges in a ring
for k in range(8):
    a = 2 * math.pi * k / 8
    u = np.array([math.cos(a), math.sin(a)])
    v = np.array([-u[1], u[0]])
    base = np.array([X[2], Y]) + 0.35 * u
    crystal([base - 0.12 * v, base + 0.12 * v, base + 0.95 * u + 0.3 * v, base + 0.95 * u - 0.3 * v])
# PIII type: filament ring + central crystal
for rr in (1.05, 1.18, 1.31):
    ax.add_patch(Ellipse((X[3], Y), 2 * rr * 1.25, 2 * rr * 0.92, fill=False, edgecolor=P.edge("protein"), lw=1.1,
                         zorder=7))
crystal([(X[3] - 0.4, Y - 0.25), (X[3] + 0.4, Y - 0.25), (X[3] + 0.4, Y + 0.25), (X[3] - 0.4, Y + 0.25)])

# Sieve-tube element in longitudinal section
y0, y1 = 2.0, 5.6
ax.add_patch(Rectangle((3.0, y0), 20.0, y1 - y0, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cell_wall"), lw=2.2,
                       zorder=3))
ax.add_patch(Rectangle((3.0, y1), 20.0, 1.3, facecolor=P.fill("nucleus"), edgecolor=P.edge("cell_wall"), lw=1.6,
                       zorder=3))
ax.add_patch(Ellipse((13.0, y1 + 0.65), 1.6, 0.8, facecolor=P.fill("chromatin"), edgecolor=P.edge("chromatin"), lw=1.0,
                     zorder=4))
for xp in (3.0, 23.0):
    for yy in np.linspace(y0 + 0.35, y1 - 0.35, 6):
        ax.add_patch(Ellipse((xp, yy), 0.5, 0.28, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"),
                             lw=0.7, zorder=5))
    ax.plot([xp, xp], [y0, y1], color=P.edge("cell_wall"), lw=3.0, ls=(0, (2, 1.6)), zorder=4)
for k, xp in enumerate(np.linspace(5.0, 21.0, 7)):
    yy = y0 + 0.45 if k % 2 == 0 else y1 - 0.45
    ax.add_patch(Ellipse((xp, yy), 0.9, 0.62, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("chloroplast"), lw=1.0,
                         zorder=6))
    ax.add_patch(Ellipse((xp, yy), 0.38, 0.3, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.6, zorder=7))
for yy in (3.1, 3.6, 4.2):
    xs = np.linspace(3.4, 22.6, 200)
    ax.plot(xs, yy + 0.12 * np.sin(xs * 1.7 + yy * 3), color=P.edge("protein"), lw=0.8, alpha=0.8, zorder=5)
bio.callout(ax, (23.0, 4.0), (25.4, 4.6), "Sieve plate", size="small")
bio.callout(ax, (23.0, 2.7), (25.4, 2.2), "Callose", size="small")
bio.callout(ax, (9.67, y0 + 0.45), (8.0, 0.9), "Plastid", size="small")
bio.callout(ax, (15.0, 3.6), (16.4, 0.9), "P-protein", size="small")
bio.callout(ax, (13.0, y1 + 0.65), (13.0, 8.3), "Companion cell (nucleus)", size="small")
bio.label(ax, (0.4, 3.8), "Sieve-tube\nelement", size="small", ha="left")
