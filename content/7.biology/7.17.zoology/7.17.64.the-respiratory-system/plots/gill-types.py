# Three types of vertebrate gills in schematic horizontal section (left half of the pharynx, anterior up),
# and one gill filament with secondary lamellae showing countercurrent flow. Not to scale.
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P
fig, ax = bio.canvas(24, 12.4)
WATER = P.edge("dna")


def flow(a, b):
    bio.arrow(ax, a, b, kind="process", color=WATER, lw=1.1, head=0.16)


def panel(x0, title):
    bio.label(ax, (x0, 12.0), title, size="small", ha="left")
    # pharynx (midline at x0 + 4.4) and body wall
    ax.plot([x0 + 4.4, x0 + 4.4], [5.4, 11.4], color=P.muted(), lw=0.8, ls=(0, (3, 2)), zorder=2)
    bio.label(ax, (x0 + 4.4, 5.1), "midline", size="tiny", color=P.muted())


# A lamprey: pouches
x0 = 0.4
panel(x0, "A  Lamprey: gill pouches")
bio.shape(ax, np.array([(x0 + 3.9, 5.6), (x0 + 4.4, 5.6), (x0 + 4.4, 11.3), (x0 + 3.9, 11.3)]), token="extracellular", zorder=3)
for k in range(6):
    y = 10.6 - k * 0.92
    bio.shape(ax, vs.oval((x0 + 2.4, y), 0.85, 0.36), token="blood", zorder=4, lw=0.8)
    for j in range(5):
        ax.plot([x0 + 1.8 + 0.3 * j, x0 + 1.8 + 0.3 * j], [y - 0.25, y + 0.25], color=P.on_fill(), lw=0.6, zorder=5)
    ax.plot([x0 + 3.25, x0 + 3.9], [y, y], color=P.edge("blood"), lw=1.6, zorder=4)
    ax.plot([x0 + 0.6, x0 + 1.55], [y, y], color=P.edge("blood"), lw=1.6, zorder=4)
    flow((x0 + 3.85, y + 0.08), (x0 + 3.3, y + 0.08)) if k == 0 else None
ax.plot([x0 + 0.6, x0 + 0.6], [5.6, 11.3], color=P.edge("animal"), lw=2.0, zorder=3)
bio.callout(ax, (x0 + 4.15, 8.0), (x0 + 5.2, 8.6), "respiratory tube", size="tiny")
bio.callout(ax, (x0 + 2.4, 7.84), (x0 + 3.2, 4.4), "pouch with gill folds", size="tiny")
bio.callout(ax, (x0 + 0.9, 6.0), (x0 + 0.4, 4.4), "external opening", size="tiny")

# B shark: septal gills
x0 = 8.4
panel(x0, "B  Shark: septal gills")
bio.shape(ax, np.array([(x0 + 3.0, 5.6), (x0 + 4.4, 5.6), (x0 + 4.4, 11.3), (x0 + 3.0, 11.3)]), token="extracellular", zorder=2)
for k in range(5):
    y = 10.4 - k * 1.05
    ax.plot([x0 + 3.0, x0 + 0.7], [y, y - 0.55], color=vs.edge("arch_3"), lw=4.5, zorder=4, solid_capstyle="round")
    ax.plot([x0 + 3.0, x0 + 3.0], [y - 0.12, y + 0.12], color=vs.edge("chondrocranium"), lw=6, zorder=5)
    for t in np.linspace(0.12, 0.85, 7):
        xa, ya = x0 + 3.0 - 2.3 * t, y - 0.55 * t
        ax.plot([xa, xa + 0.05], [ya + 0.07, ya + 0.38], color=P.edge("blood"), lw=1.3, zorder=3)
        ax.plot([xa, xa - 0.05], [ya - 0.07, ya - 0.38], color=P.edge("blood"), lw=1.3, zorder=3)
    flow((x0 + 2.7, y - 0.52), (x0 + 1.2, y - 0.85))
ax.plot([x0 + 0.7, x0 + 0.7], [5.6, 11.3], color=P.edge("animal"), lw=1.0, ls=(0, (2, 2)), zorder=3)
bio.callout(ax, (x0 + 1.4, 9.67), (x0 + 0.3, 4.4), "interbranchial septum", size="tiny")
bio.callout(ax, (x0 + 3.0, 6.2), (x0 + 5.0, 4.4), "gill arch", size="tiny")
bio.callout(ax, (x0 + 2.0, 10.6), (x0 + 1.3, 11.6), "filaments (hemibranchs)", size="tiny")
bio.callout(ax, (x0 + 0.75, 8.1), (x0 + 5.4, 8.1), "separate gill slits", size="tiny")

# C teleost: opercular gills
x0 = 16.4
panel(x0, "C  Teleost: opercular gills")
bio.shape(ax, np.array([(x0 + 3.0, 5.6), (x0 + 4.4, 5.6), (x0 + 4.4, 11.3), (x0 + 3.0, 11.3)]), token="extracellular", zorder=2)
for k in range(4):
    y = 10.2 - k * 1.2
    ax.plot([x0 + 3.0, x0 + 3.0], [y - 0.12, y + 0.12], color=vs.edge("arch_3"), lw=6, zorder=5)
    for s in (1, -1):
        ax.plot([x0 + 2.95, x0 + 1.4], [y, y + s * 0.55], color=P.edge("blood"), lw=3.0, zorder=4, solid_capstyle="round")
    flow((x0 + 2.6, y - 0.6), (x0 + 1.3, y - 0.6))
op = vs.smooth([(x0 + 1.2, 11.2), (x0 + 0.7, 9.0), (x0 + 0.7, 6.5), (x0 + 1.1, 5.7), (x0 + 0.9, 5.7), (x0 + 0.35, 7.5),
                (x0 + 0.4, 10.5)])
bio.shape(ax, op, token="bone", zorder=5)
bio.callout(ax, (x0 + 0.5, 8.5), (x0 - 0.4, 4.4), "operculum", size="tiny")
bio.callout(ax, (x0 + 1.9, 9.3), (x0 + 3.0, 4.4), "free filaments, septum reduced", size="tiny")
bio.callout(ax, (x0 + 1.1, 7.2), (x0 + 5.0, 11.6), "opercular cavity", size="tiny")

# D countercurrent filament
bio.label(ax, (0.4, 3.6), "D  One filament, secondary lamellae: water and blood flow in opposite directions", size="small", ha="left")
fx0, fy = 3.0, 1.6
bio.shape(ax, np.array([(fx0, fy - 0.25), (fx0 + 13, fy - 0.25), (fx0 + 13, fy + 0.25), (fx0, fy + 0.25)]), token="neutral",
          zorder=3)
for j in range(14):
    x = fx0 + 0.5 + j * 0.9
    lam = np.array([(x, fy + 0.25), (x + 0.45, fy + 0.25), (x + 0.45, fy + 1.3), (x, fy + 1.3)])
    bio.shape(ax, lam, token="blood", zorder=4, lw=0.6)
    lam2 = lam.copy(); lam2[:, 1] = 2 * fy - lam2[:, 1]
    bio.shape(ax, lam2, token="blood", zorder=4, lw=0.6)
bio.arrow(ax, (fx0 + 6.5, fy + 1.75), (fx0 + 2.5, fy + 1.75), kind="process", color=WATER, lw=1.6)
bio.label(ax, (fx0 + 6.8, fy + 1.75), "water", size="tiny", ha="left", color=WATER)
bio.arrow(ax, (fx0 + 9.5, fy - 1.6), (fx0 + 12.5, fy - 1.6), kind="process", color=P.edge("negative"), lw=1.6)
bio.label(ax, (fx0 + 9.3, fy - 1.6), "blood within lamellae", size="tiny", ha="right", color=P.edge("negative"))
bio.label(ax, (fx0 - 0.2, fy + 0.05), "filament", size="tiny", ha="right")
bio.callout(ax, (fx0 + 5.2, fy + 0.8), (fx0 + 16.0, fy + 1.0), "secondary lamella", size="tiny")
