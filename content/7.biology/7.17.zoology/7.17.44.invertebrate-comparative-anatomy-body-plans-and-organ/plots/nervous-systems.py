"""Six architectures of animal nervous systems (schematic, not to scale; nervous tissue in the neuron
colour, gut grey-yellow in the lateral views).

A: nerve net of a cnidarian polyp (lateral view), condensed around the mouth. B: orthogon of a
flatworm (dorsal view): bilobed brain and several pairs of longitudinal cords joined by commissures,
the ventral pair dominant. C: tetraneury of a chiton (dorsal view): a circumoesophageal ring with two
pedal and two lateral (pleurovisceral) cords. D: ganglionated ventral nerve cord of an annelid or
arthropod (lateral view): a brain above the pharynx, connectives around it and a chain of segmental
ganglia below the gut. E: circumoral ring and five radial nerves of a sea star (oral view), without a
brain. F: dorsal hollow nerve cord of a chordate (lateral view), above the notochord and the gut,
with an anterior brain vesicle and a central canal.
"""

import numpy as np
from matplotlib.patches import Circle, Ellipse, Polygon

import wikibio as bio
from wikibio import quant

P = bio.P
NC = P.edge("neuron")
fig, ax = bio.canvas(24.0, 14.6)


def nerve(pts, lw=1.6):
    p = np.asarray(pts, float)
    ax.plot(p[:, 0], p[:, 1], color=NC, lw=lw, solid_capstyle="round", solid_joinstyle="round", zorder=8)


def ganglion(xy, rx, ry=None):
    ax.add_patch(Ellipse(xy, 2 * rx, 2 * (ry or rx), facecolor=P.fill("neuron"), edgecolor=P.edge("neuron"), lw=0.9, zorder=9))


def body(verts):
    ax.add_patch(Polygon(np.asarray(verts), closed=True, facecolor=P.light("neutral"), edgecolor=P.edge("neutral"), lw=1.0, zorder=3))


def title(x, y, letter, text, sub):
    bio.label(ax, (x, y), letter, size="title", bold=True, ha="left")
    bio.label(ax, (x + 0.55, y), text, size="small", bold=True, ha="left")
    bio.label(ax, (x + 0.55, y - 0.45), sub, size="tiny", ha="left", color=P.muted())


# A: nerve net (polyp)
title(0.4, 14.1, "A", "Nerve net", "cnidarians, ctenophores")
body(bio.smooth_closed([(2.2, 8.2), (3.8, 8.2), (3.9, 11.6), (3.4, 12.2), (2.6, 12.2), (2.1, 11.6)]))
for x0, sgn in ((2.7, -1), (3.3, 1)):
    nerve([(x0, 12.15), (x0 + sgn * 0.8, 13.0), (x0 + sgn * 1.3, 13.3)], lw=0.9)
rng = np.random.default_rng(3)
pts = np.c_[rng.uniform(2.35, 3.65, 44), rng.uniform(8.5, 11.8, 44)]
for i, a in enumerate(pts):
    d = np.hypot(*(pts - a).T)
    for j in np.argsort(d)[1:4]:
        nerve([a, pts[j]], lw=0.8)
    ax.add_patch(Circle(a, 0.06, color=NC, zorder=9))
ax.add_patch(Ellipse((3.0, 12.0), 1.0, 0.25, fill=False, edgecolor=NC, lw=1.6, zorder=9))
bio.callout(ax, (3.5, 12.0), (5.2, 12.6), "oral nerve ring", size="tiny")
bio.callout(ax, (3.5, 9.6), (5.2, 9.6), "net in both epithelia", size="tiny")

# B: orthogon (flatworm)
title(8.4, 14.1, "B", "Orthogon", "flatworms")
body(bio.smooth_closed([(11.0, 12.9), (12.2, 12.4), (12.6, 10.5), (12.1, 8.6), (11.0, 8.0), (9.9, 8.6), (9.4, 10.5), (9.8, 12.4)]))
ganglion((10.65, 12.2), 0.33, 0.25)
ganglion((11.35, 12.2), 0.33, 0.25)
for dx, lw in ((0.35, 2.0), (0.85, 1.0), (1.3, 0.8)):
    for s in (-1, 1):
        nerve([(11.0 + s * dx * 0.8, 12.1), (11.0 + s * dx, 11.3), (11.0 + s * dx, 9.3), (11.0 + s * dx * 0.6, 8.4)], lw=lw)
for y in np.linspace(9.0, 11.3, 6):
    nerve([(11.0 - 1.3, y), (11.0 + 1.3, y)], lw=0.6)
bio.callout(ax, (11.35, 12.3), (13.6, 13.0), "bilobed brain", size="tiny")
bio.callout(ax, (11.35, 10.3), (13.6, 10.0), "ventral cords", size="tiny")
bio.callout(ax, (12.3, 10.83), (13.6, 11.4), "commissures", size="tiny")

# C: tetraneury (chiton)
title(16.4, 14.1, "C", "Tetraneury", "molluscs (chitons), entoprocts")
body(bio.smooth_closed([(19.0, 13.0), (20.3, 12.5), (20.6, 10.5), (20.3, 8.5), (19.0, 8.0), (17.7, 8.5), (17.4, 10.5), (17.7, 12.5)]))
ax.add_patch(Ellipse((19.0, 12.2), 1.3, 0.6, fill=False, edgecolor=NC, lw=2.0, zorder=9))
for s in (-1, 1):
    nerve([(19.0 + s * 0.3, 11.95), (19.0 + s * 0.35, 9.0), (19.0 + s * 0.2, 8.4)], lw=1.8)
    nerve([(19.0 + s * 0.62, 12.1), (19.0 + s * 1.05, 11.3), (19.0 + s * 1.1, 9.4), (19.0 + s * 0.3, 8.35)], lw=1.4)
for y in np.linspace(9.2, 11.4, 7):
    nerve([(18.65, y), (19.35, y)], lw=0.6)
bio.callout(ax, (19.6, 12.35), (21.4, 13.0), "cerebral ring", size="tiny")
bio.callout(ax, (19.35, 10.3), (21.4, 10.5), "pedal cords", size="tiny")
bio.callout(ax, (20.1, 9.7), (21.4, 9.4), "lateral cords", size="tiny")

# D: ventral nerve cord (annelid/arthropod, lateral)
title(0.4, 6.9, "D", "Ventral nerve cord", "annelids, arthropods")
body(bio.smooth_closed([(0.9, 3.9), (1.5, 5.0), (4.5, 5.2), (7.0, 4.9), (7.4, 4.0), (7.0, 3.0), (4.5, 2.7), (1.5, 2.9)]))
for x in np.arange(2.2, 7.0, 0.7):
    ax.plot([x, x], [2.85, 5.1], color=P.muted(), lw=0.5, ls=(0, (2, 2)), zorder=4)
ax.add_patch(Ellipse((4.3, 4.0), 5.8, 0.55, facecolor=P.light("highlight"), edgecolor=P.edge("highlight"), lw=0.8, zorder=5))
ganglion((1.6, 4.55), 0.32, 0.25)
nerve([(1.75, 4.4), (1.95, 3.9), (1.95, 3.4)], lw=1.4)
nerve([(1.95, 3.35), (6.9, 3.35)], lw=1.8)
for x in np.arange(1.95, 6.4, 0.7):
    ganglion((x + 0.35, 3.35), 0.15, 0.12)
bio.callout(ax, (1.6, 4.7), (1.0, 5.9), "brain (dorsal)", size="tiny")
bio.callout(ax, (1.92, 3.9), (0.6, 2.2), "connective", size="tiny")
bio.callout(ax, (4.6, 3.35), (4.6, 1.9), "segmental ganglia, ventral to gut", size="tiny")
bio.callout(ax, (6.0, 4.0), (7.6, 5.7), "gut", size="tiny")

# E: ring and radial nerves (sea star, oral view)
title(8.4, 6.9, "E", "Ring and radial nerves", "echinoderms")
cx, cy = 11.0, 3.6
arm = []
for k in range(10):
    a = np.pi / 2 + k * np.pi / 5
    rr = 2.1 if k % 2 == 0 else 1.05
    arm.append((cx + rr * np.cos(a), cy + rr * np.sin(a)))
body(bio.smooth_closed(arm))
ax.add_patch(Circle((cx, cy), 0.45, fill=False, edgecolor=NC, lw=2.0, zorder=9))
for k in range(5):
    a = np.pi / 2 + k * 2 * np.pi / 5
    nerve([(cx + 0.45 * np.cos(a), cy + 0.45 * np.sin(a)), (cx + 1.85 * np.cos(a), cy + 1.85 * np.sin(a))], lw=1.6)
bio.callout(ax, (cx + 0.32, cy + 0.32), (13.7, 5.8), "circumoral nerve ring", size="tiny")
bio.callout(ax, (cx + 1.2 * np.cos(np.pi / 2 - 2 * np.pi / 5), cy + 1.2 * np.sin(np.pi / 2 - 2 * np.pi / 5)),
            (13.7, 3.6), "radial nerve", size="tiny")
bio.label(ax, (13.7, 2.4), "no brain", size="tiny", ha="left", color=P.muted())

# F: dorsal hollow nerve cord (chordate, lateral)
title(16.4, 6.9, "F", "Dorsal hollow nerve cord", "chordates")
body(bio.smooth_closed([(16.8, 3.9), (17.4, 4.9), (20.5, 5.1), (23.2, 4.2), (23.6, 3.9), (23.2, 3.6), (20.5, 2.8), (17.4, 2.9)]))
ax.add_patch(Ellipse((19.8, 3.3), 4.6, 0.45, facecolor=P.light("highlight"), edgecolor=P.edge("highlight"), lw=0.8, zorder=5))
ax.plot([17.6, 23.2], [3.95, 3.95], color=P.edge("metabolite"), lw=3.2, solid_capstyle="round", zorder=6)
ax.plot([17.4, 23.0], [4.45, 4.25], color=NC, lw=4.2, solid_capstyle="round", zorder=8)
ax.plot([17.5, 22.9], [4.45, 4.25], color=P.light("neutral"), lw=1.0, zorder=9)
ganglion((17.45, 4.5), 0.32, 0.22)
bio.callout(ax, (17.45, 4.65), (18.0, 6.0), "brain vesicle", size="tiny")
bio.callout(ax, (21.0, 4.33), (21.4, 5.6), "neural tube with canal", size="tiny")
bio.callout(ax, (21.8, 3.95), (23.2, 2.3), "notochord", size="tiny")
bio.callout(ax, (19.0, 3.3), (18.4, 1.9), "gut", size="tiny")
