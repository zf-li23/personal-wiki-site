"""Two multicellular life cycles of soil bacteria (schematic).
A: Streptomyces. A spore germinates into branching substrate hyphae that form a mycelium; on
starvation, aerial hyphae grow into the air, nourished by the lysis of the substrate mycelium, and this
is when antibiotics and other secondary metabolites are made; the aerial hyphae then septate at regular
intervals into chains of spores, which disperse.
B: Myxococcus xanthus. Cells glide on surfaces in swarms and lyse their prey with secreted enzymes
(adventurous motility of single cells uses a cell-envelope motor, social motility uses retractile type
IV pili); on starvation about 100000 cells aggregate by rippling and streaming into a fruiting body, in
which a minority differentiates into resistant myxospores while most of the population lyses."""

import numpy as np
from matplotlib.patches import Circle, Ellipse

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
fig, ax = bio.canvas(26.0, 11.0)


def hypha(start, angle, length, width=0.1, token="fungus", n=60, curve=0.25, seed=0, zorder=6):
    r = np.random.default_rng(seed)
    t = np.linspace(0, 1, n)
    a = np.radians(angle) + curve * np.sin(2.2 * t) + 0.04 * r.standard_normal(n).cumsum() / n ** 0.5
    pts = np.c_[np.cumsum(np.cos(a)), np.cumsum(np.sin(a))] * (length / n) + np.asarray(start, float)
    ax.plot(pts[:, 0], pts[:, 1], color=P.edge(token), lw=width * 18, solid_capstyle="round", zorder=zorder)
    return pts


def spore(xy, r=0.16, token="plant"):
    ax.add_patch(Circle(xy, r, facecolor=P.fill(token), edgecolor=P.edge(token), lw=0.9, zorder=12))


TOK = "plant"
bio.panel(ax, "A", (0.2, 10.9))
bio.label(ax, (1.0, 10.6), "Streptomyces", size="small", bold=True, ha="left", italic=True)
ground = 6.6
ax.plot([0.8, 12.4], [ground, ground], color=P.muted(), lw=1.0, ls="--", zorder=2)
bio.label(ax, (12.3, ground - 0.35), "surface", size="tiny", color=P.muted(), ha="right")

# 1 spore and germ tube
spore((1.8, ground - 0.9))
hypha((1.8, ground - 0.9), -40, 1.1, token=TOK, seed=1)
bio.label(ax, (1.9, ground - 2.6), "spore\ngerminates", size="tiny", color=P.muted())
# 2 substrate mycelium
for k, a in enumerate((-20, -50, -80, -110, -140, -160)):
    hypha((5.2, ground - 0.4), a, 1.8 + 0.3 * (k % 3), token=TOK, seed=10 + k)
for k, a in enumerate((-35, -95, -130)):
    hypha((5.2 + 1.1 * np.cos(np.radians(a)), ground - 0.4 + 1.1 * np.sin(np.radians(a))), a - 35, 1.1,
          token=TOK, seed=20 + k)
bio.label(ax, (5.2, ground - 3.0), "substrate mycelium\n(nutrients exhausted)", size="tiny", color=P.muted())
# 3 aerial hyphae and spore chains
for k, a in enumerate((-30, -70, -110, -150)):
    hypha((9.6, ground - 0.3), a, 1.5, token=TOK, seed=30 + k)
for k, (x0, a) in enumerate(((9.0, 100), (9.6, 85), (10.3, 70))):
    pts = hypha((x0, ground + 0.1), a, 2.4, token=TOK, seed=40 + k, curve=0.12)
    for s in np.linspace(0.45, 1.0, 5):
        spore(pts[int(s * (len(pts) - 1))], 0.14)
bio.label(ax, (9.9, ground + 3.4), "aerial hyphae become\nchains of spores", size="tiny", color=P.muted())
bio.label(ax, (9.6, ground - 2.6), "antibiotics made as the\nsubstrate mycelium is cannibalized", size="tiny",
          color=P.muted())
for a, b in (((2.9, ground - 1.2), (3.7, ground - 1.2)), ((6.9, ground - 1.2), (7.9, ground - 1.2))):
    bio.arrow(ax, a, b, kind="process", lw=1.0, head=0.16)
bio.arrow(ax, (11.4, ground + 1.2), (1.9, ground - 0.3), kind="process", lw=1.0, head=0.18, bend=-0.18)
bio.label(ax, (6.4, ground - 0.1), "dispersal", size="tiny", color=P.muted())

# ---------------------------------------------------------------- B
bio.panel(ax, "B", (13.4, 10.9))
bio.label(ax, (14.2, 10.6), "Myxococcus xanthus", size="small", bold=True, ha="left", italic=True)


def rods(center, n, spread, length=0.55, seed=0, token="bacterium"):
    r = np.random.default_rng(seed)
    for _ in range(n):
        x = center[0] + r.normal(0, spread)
        y = center[1] + r.normal(0, spread * 0.55)
        a = r.uniform(0, 180)
        ax.add_patch(Ellipse((x, y), length, 0.16, angle=a, facecolor=P.fill(token), edgecolor=P.edge(token),
                             lw=0.6, zorder=8))


# swarm feeding on prey
rods((16.2, 8.4), 60, 0.9, seed=2)
for xy in [(16.9, 8.9), (15.5, 8.0), (16.5, 7.8)]:
    ax.add_patch(Circle(xy, 0.12, facecolor=P.fill("receptor"), edgecolor=P.edge("receptor"), lw=0.6, zorder=7))
bio.label(ax, (16.2, 6.7), "swarm glides and lyses prey\n(A and S motility)", size="tiny", color=P.muted())
# aggregation
rods((21.0, 8.4), 70, 0.55, seed=3)
for r0 in (0.9, 1.3):
    ax.add_patch(Circle((21.0, 8.4), r0, facecolor="none", edgecolor=P.edge("neutral"), lw=0.8, ls=":", zorder=6))
bio.label(ax, (21.0, 6.7), "starvation: rippling\nand aggregation", size="tiny", color=P.muted())
bio.arrow(ax, (17.9, 8.4), (19.4, 8.4), kind="process", lw=1.0, head=0.16)
# fruiting body
fx, fy = 18.6, 2.9
ax.plot([fx - 2.2, fx + 2.2], [fy - 0.8, fy - 0.8], color=P.muted(), lw=1.0, ls="--", zorder=2)
ax.add_patch(Ellipse((fx, fy + 0.1), 2.6, 2.0, facecolor=P.fill("bacterium"), edgecolor=P.edge("bacterium"),
                     lw=1.4, zorder=8))
ax.add_patch(Ellipse((fx, fy - 0.75), 1.9, 0.6, facecolor=P.fill("bacterium"), edgecolor=P.edge("bacterium"),
                     lw=1.4, zorder=7))
for _ in range(16):
    a, rr = rng.uniform(0, 2 * np.pi), rng.uniform(0, 0.75)
    ax.add_patch(Circle((fx + rr * np.cos(a), fy + 0.1 + rr * np.sin(a) * 0.8), 0.14,
                        facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=0.7, zorder=10))
bio.callout(ax, (fx - 0.5, fy + 0.3), (fx - 2.4, fy + 1.5), "myxospores (about 10 %)", size="tiny")
bio.label(ax, (fx, fy - 1.5), "fruiting body (about $10^5$ cells);\nmost cells lyse", size="tiny", color=P.muted())
bio.arrow(ax, (21.0, 6.9), (19.3, 4.2), kind="process", lw=1.0, head=0.18)
rods((23.6, 3.2), 25, 0.7, seed=4)
bio.arrow(ax, (20.0, 3.2), (22.4, 3.2), kind="process", lw=1.0, head=0.16)
bio.label(ax, (23.6, 1.9), "germination into\na new swarm", size="tiny", color=P.muted())
