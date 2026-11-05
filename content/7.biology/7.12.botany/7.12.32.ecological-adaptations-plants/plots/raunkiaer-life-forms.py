"""Raunkiaer life forms: position of the perennating buds (red dots) during the unfavourable season.
Parts that survive are drawn solid, parts that die back are pale and dashed. Phanerophyte (buds on shoots
more than 25 cm above the ground), chamaephyte (buds below 25 cm, under snow), hemicryptophyte (buds at
the soil surface under litter), cryptophyte (buds on bulbs, tubers or rhizomes below ground), therophyte
(only seeds survive).
"""
import numpy as np
from matplotlib.patches import Circle, Ellipse, Rectangle

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26.0, 11.0)
G = 3.0  # ground level
STEM, BUD, SOIL = "plant", "negative", "animal"
ax.add_patch(Rectangle((0.3, 0.9), 25.4, G - 0.9, facecolor=P.fill(SOIL), alpha=0.25, edgecolor="none", zorder=1))
ax.plot([0.3, 25.7], [G, G], color=P.edge(SOIL), lw=1.4, zorder=3)
ax.plot([0.3, 10.6], [G + 1.0, G + 1.0], color=P.muted(), lw=0.8, ls=(0, (4, 3)), zorder=2)
bio.label(ax, (0.4, G + 1.25), "25 cm", size="tiny", color=P.muted(), ha="left")


def bud(p, r=0.13):
    ax.add_patch(Circle(p, r, facecolor=P.fill(BUD), edgecolor=P.edge(BUD), lw=0.7, zorder=10))


def line(pts, lw=2.0, dead=False, tok=STEM, z=6):
    pts = np.asarray(pts)
    ax.plot(pts[:, 0], pts[:, 1], color=P.light(tok) if dead else P.edge(tok), lw=lw,
            ls=(0, (3, 2)) if dead else "-", solid_capstyle="round", zorder=z)


def name(x, title, sub):
    bio.label(ax, (x, 0.55), title, bold=True)
    bio.label(ax, (x, 0.05 + 0.0), sub, size="small", color=P.muted())


# phanerophyte
x = 2.8
line([(x, G), (x, G + 4.5)], lw=5, tok="animal")
for (dx, dy, ex, ey) in ((0, 2.6, -1.5, 4.4), (0, 3.2, 1.4, 5.0), (0, 4.5, -0.5, 6.4), (0, 4.0, 0.9, 6.6)):
    line([(x + dx, G + dy), (x + ex, G + ey)], lw=2.5, tok="animal")
    bud((x + ex, G + ey))
for k in range(4):
    line([(x, G), (x + (k - 1.5) * 0.7, G - 1.2)], lw=2, tok="bone")
name(x, "Phanerophyte", "buds > 25 cm up")

# chamaephyte under snow
x = 8.0
ax.add_patch(Rectangle((x - 2.0, G), 4.0, 1.3, facecolor=P.fill("neutral"), alpha=0.35, edgecolor="none", zorder=2))
bio.label(ax, (x + 1.5, G + 1.5), "snow", size="tiny", color=P.muted())
for a in np.linspace(30, 150, 7):
    t = np.radians(a)
    tip = (x + 1.3 * np.cos(t), G + 0.75 * np.sin(t) + 0.05)
    line([(x, G), tip], lw=2.2, tok="animal")
    bud(tip)
for k in range(3):
    line([(x, G), (x + (k - 1) * 0.6, G - 1.0)], lw=2, tok="bone")
name(x, "Chamaephyte", "buds just above ground")

# hemicryptophyte: rosette, dead flowering shoot
x = 13.2
line([(x, G + 0.1), (x, G + 4.0)], dead=True)
for s in (-1, 1):
    line([(x, G + 2.5), (x + s * 0.8, G + 3.3)], dead=True, lw=1.4)
ax.add_patch(Ellipse((x, G + 0.05), 2.6, 0.22, facecolor=P.fill("bract"), edgecolor=P.edge("bract"), lw=0.6, zorder=7))
bio.label(ax, (x + 1.8, G + 0.45), "litter", size="tiny", color=P.muted())
bud((x, G + 0.05), 0.16)
for k in range(5):
    line([(x, G), (x + (k - 2) * 0.35, G - 1.3)], lw=1.6, tok="bone")
name(x, "Hemicryptophyte", "buds at soil surface")

# cryptophyte: bulb
x = 18.4
line([(x, G - 1.0), (x, G + 3.5)], dead=True)
for s in (-1, 1):
    line([(x, G + 0.3), (x + s * 0.9, G + 2.6)], dead=True, lw=1.4)
ax.add_patch(Ellipse((x, G - 1.3), 1.2, 1.0, facecolor=P.fill("bone"), edgecolor=P.edge("bone"), lw=0.9, zorder=7))
bud((x, G - 0.85), 0.15)
for k in range(5):
    line([(x - 0.3 + k * 0.15, G - 1.8), (x - 0.6 + k * 0.3, G - 2.0)], lw=1.2, tok="bone")
name(x, "Cryptophyte", "buds below ground")

# therophyte: only seeds survive
x = 23.4
line([(x, G), (x, G + 2.6)], dead=True)
for s in (-1, 1):
    line([(x, G + 1.2), (x + s * 0.7, G + 2.0)], dead=True, lw=1.4)
line([(x, G), (x, G - 0.8)], dead=True, tok="bone", lw=1.4)
for p in [(x - 1.0, G + 0.08), (x - 0.4, G - 0.1), (x + 0.5, G + 0.05), (x + 1.1, G - 0.15), (x + 0.1, G - 0.3)]:
    ax.add_patch(Ellipse(p, 0.24, 0.15, facecolor=P.fill(BUD), edgecolor=P.edge(BUD), lw=0.6, zorder=10))
bio.label(ax, (x + 1.5, G + 0.5), "seeds", size="tiny", color=P.muted())
name(x, "Therophyte", "survives as seed")
