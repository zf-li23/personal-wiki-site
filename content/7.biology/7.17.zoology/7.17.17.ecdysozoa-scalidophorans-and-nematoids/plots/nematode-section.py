# Cross-section of a female nematode (Ascaris-like), schematic, not to scale.
# Outside in: collagenous cuticle, syncytial hypodermis thickened into dorsal, ventral and two lateral
# cords, longitudinal muscle cells only (no circular muscle) in four quadrants, each cell with an outer
# contractile part and an inner cytoplasmic bag sending a muscle arm to the dorsal or ventral nerve cord,
# the pseudocoel with the reproductive tubes, and the intestine (a single layer of endoderm).
import numpy as np
from matplotlib.patches import Wedge, Circle, Ellipse
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(17, 11)
C = np.array([5.6, 5.5])
R = 4.6


def ring(r_out, r_in, tok, t1=0, t2=360, z=5):
    ax.add_patch(Wedge(C, r_out, t1, t2, width=r_out - r_in, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=z))


def pol(r, deg):
    a = np.radians(deg)
    return C + r * np.array([np.cos(a), np.sin(a)])


# pseudocoel (background), cuticle and hypodermis
ax.add_patch(Circle(C, R * 0.84, facecolor=P.light("pseudocoel"), edgecolor=P.edge("pseudocoel"), lw=0.6, zorder=3))
ring(R, R * 0.93, "bone", z=6)
ring(R * 0.93, R * 0.885, "ectoderm", z=6)
# cords: lateral (0, 180 deg) wide, dorsal (90) and ventral (270) narrow
cords = {0: (13, 0.62), 180: (13, 0.62), 90: (7, 0.76), 270: (7, 0.76)}
for deg, (half, rin) in cords.items():
    ring(R * 0.9, R * rin, "ectoderm", deg - half, deg + half, z=7)
# excretory canals in the lateral cords, nerve cords in dorsal and ventral cords
for deg in (0, 180):
    ax.add_patch(Circle(pol(R * 0.75, deg), 0.2, facecolor=P.fill("vesicle"), edgecolor=P.edge("vesicle"), lw=0.8, zorder=9))
for deg in (90, 270):
    ax.add_patch(Circle(pol(R * 0.83, deg), 0.17, facecolor=P.fill("neuron"), edgecolor=P.edge("neuron"), lw=0.8, zorder=9))

# muscle cells in four quadrants: contractile strip (outer) + cytoplasmic bag (inner) + arm to a nerve cord
for q0, q1 in ((14, 82), (98, 166), (194, 262), (278, 346)):
    angs = np.linspace(q0 + 4, q1 - 4, 6)
    target = 90 if q0 < 180 else 270
    for a in angs:
        ring(R * 0.885, R * 0.80, "muscle", a - 5.2, a + 5.2, z=7)
        bag = pol(R * 0.74, a)
        ax.add_patch(Ellipse(bag, 0.6, 0.36, angle=a, facecolor=P.light("muscle"), edgecolor=P.edge("muscle"), lw=0.6, zorder=6))
        # muscle arm: a thin process curving to the nerve cord
        t = np.linspace(0, 1, 30)
        end = pol(R * 0.77, target + (6 if a < target else -6) * (1 if q0 < 180 else 1))
        mid = pol(R * 0.6, (a + target) / 2)
        pts = (1 - t)[:, None] ** 2 * bag + 2 * ((1 - t) * t)[:, None] * mid + (t ** 2)[:, None] * end
        ax.plot(pts[:, 0], pts[:, 1], color=P.edge("muscle"), lw=0.6, zorder=5)

# intestine: single epithelial layer around a slit lumen
gut = C + np.array([0.0, 0.25])
ax.add_patch(Ellipse(gut, 2.5, 1.7, facecolor=P.fill("endoderm"), edgecolor=P.edge("endoderm"), lw=0.9, zorder=8))
ax.add_patch(Ellipse(gut, 1.5, 0.35, facecolor=P.surface(), edgecolor=P.edge("endoderm"), lw=0.7, zorder=9))
# reproductive tubes (ovary, oviduct, uterus with eggs) in the pseudocoel
for xy, r, tok in (((4.2, 3.3), 0.42, "ovary"), ((6.9, 3.4), 0.5, "ovary"), ((3.8, 7.3), 0.35, "ovary"), ((7.3, 7.2), 0.6, "ovule")):
    ax.add_patch(Circle(xy, r, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=8))

lab = dict(size="small")
bio.callout(ax, pol(R * 0.83, 90), (12.0, 10.2), "Dorsal nerve cord (in dorsal cord)", **lab)
bio.callout(ax, pol(R * 0.91, 66), (12.0, 9.5), "Hypodermis (syncytial)", **lab)
bio.callout(ax, pol(R * 0.965, 52), (12.0, 8.8), "Cuticle (collagen)", **lab)
bio.callout(ax, pol(R * 0.84, 37), (12.0, 8.1), "Muscle cell: contractile part", **lab)
bio.callout(ax, pol(R * 0.72, 22), (12.0, 7.4), "Muscle cell: cytoplasmic bag", **lab)
bio.callout(ax, gut + np.array([1.1, 0.3]), (12.0, 6.4), "Intestine (one cell layer)", **lab)
bio.callout(ax, pol(R * 0.75, 0), (12.0, 5.5), "Lateral cord with excretory canal", **lab)
bio.callout(ax, pol(R * 0.42, -22), (12.0, 4.6), "Pseudocoel (fluid under pressure)", **lab)
bio.callout(ax, (6.9, 3.4), (12.0, 3.4), "Uterus / ovary", **lab)
bio.callout(ax, pol(R * 0.83, 270), (12.0, 1.0), "Ventral nerve cord (in ventral cord)", **lab)
bio.label(ax, (C[0], 10.6), "Dorsal", size="small", color=P.muted())
bio.label(ax, (C[0], 0.4), "Ventral", size="small", color=P.muted())
