"""The two classical modes of mesoderm and coelom formation (schematic cross sections of an embryo,
dorsal up; ectoderm blue, endoderm yellow, mesoderm red, coelom green).

Top, schizocoely (typical of spiralians such as annelids and molluscs): mesoderm arises from a pair of
teloblasts (descendants of the 4d cell) near the blastopore, proliferates into two solid mesodermal
bands between gut and ectoderm, and a cavity opens within each band by splitting: the coelom. Bottom,
enterocoely (typical of echinoderms, hemichordates and cephalochordates): pouches of the archenteron wall
bulge outward, pinch off and become coelomic sacs whose walls are the mesoderm. In both cases the result
is a coelom lined by mesoderm on the body-wall (somatic) and gut (splanchnic) sides. Vertebrates form their
coelom by splitting of the lateral plate mesoderm, and the modes are not strictly tied to the protostome
and deuterostome clades (see text).
"""

import numpy as np
import wikibio as bio
from matplotlib.patches import Ellipse, Circle

P = bio.P
fig, ax = bio.canvas(24.0, 11.0)
ECT, END, MES, COE = "ectoderm", "endoderm", "mesoderm", "coelom"


def ring(c, r, w, tok, z=5):
    ax.add_patch(Circle(c, r, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.0, zorder=z))
    ax.add_patch(Circle(c, r - w, facecolor=P.surface(), edgecolor=P.edge(tok), lw=0.8, zorder=z + 0.1))


def blob(c, rx, ry, tok, z=7, angle=0):
    ax.add_patch(Ellipse(c, 2 * rx, 2 * ry, angle=angle, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.0, zorder=z))


X = [4.0, 11.0, 18.0]
R = 2.1
# --- schizocoely
bio.label(ax, (0.3, 10.5), "Schizocoely", size="title", bold=True, ha="left")
for k, x in enumerate(X):
    y = 7.6
    ring((x, y), R, 0.35, ECT)
    ring((x, y - 0.2), 0.8, 0.3, END, z=6)
    for s in (-1, 1):
        if k == 0:
            blob((x + s * 0.55, y - 1.35), 0.22, 0.22, MES)
        elif k == 1:
            blob((x + s * 1.15, y - 0.4), 0.42, 0.85, MES, angle=s * 20)
        else:
            blob((x + s * 1.2, y - 0.2), 0.55, 1.15, MES, angle=s * 15)
            blob((x + s * 1.2, y - 0.2), 0.32, 0.85, COE, z=8, angle=s * 15)
bio.callout(ax, (X[0] + 0.55, 7.6 - 1.35), (X[0] + 2.6, 5.4), "Teloblast (from 4d)", size="tiny")
bio.callout(ax, (X[1] + 1.15, 7.2), (X[1] + 2.7, 5.4), "Mesodermal band", size="tiny")
bio.callout(ax, (X[2] + 1.2, 7.4), (X[2] + 2.8, 5.4), "Coelom opens\nby splitting", size="tiny")
bio.callout(ax, (X[0], 7.4), (X[0] - 2.7, 9.6), "Gut (endoderm)", size="tiny")
for a, b in ((X[0] + 2.4, X[1] - 2.4), (X[1] + 2.4, X[2] - 2.4)):
    bio.arrow(ax, (a, 7.6), (b, 7.6), kind="process", color=P.muted())

# --- enterocoely
bio.label(ax, (0.3, 4.9), "Enterocoely", size="title", bold=True, ha="left")
for k, x in enumerate(X):
    y = 2.3
    ring((x, y), R, 0.35, ECT)
    if k == 0:
        ring((x, y), 0.95, 0.3, END, z=6)
        for s in (-1, 1):
            blob((x + s * 0.95, y + 0.2), 0.32, 0.4, END, z=7)
    elif k == 1:
        ring((x, y - 0.1), 0.8, 0.3, END, z=6)
        for s in (-1, 1):
            blob((x + s * 1.2, y + 0.25), 0.55, 0.6, MES)
            blob((x + s * 1.2, y + 0.25), 0.3, 0.35, COE, z=8)
            ax.plot([x + s * 0.75, x + s * 0.85], [y + 0.15, y + 0.2], color=P.edge(MES), lw=2.5, zorder=9)
    else:
        ring((x, y - 0.15), 0.75, 0.3, END, z=6)
        for s in (-1, 1):
            blob((x + s * 1.2, y), 0.62, 1.25, MES)
            blob((x + s * 1.2, y), 0.4, 1.0, COE, z=8)
bio.callout(ax, (X[0] + 0.95, 2.5), (X[0] + 2.6, 4.4), "Archenteron pouch", size="tiny")
bio.callout(ax, (X[1] + 1.2, 2.55), (X[1] + 2.7, 4.4), "Sac pinches off", size="tiny")
bio.callout(ax, (X[2] + 1.2, 2.0), (X[2] + 2.8, 4.4), "Coelomic sac", size="tiny")
for a, b in ((X[0] + 2.4, X[1] - 2.4), (X[1] + 2.4, X[2] - 2.4)):
    bio.arrow(ax, (a, 2.3), (b, 2.3), kind="process", color=P.muted())

# legend
for j, (tok, name) in enumerate(((ECT, "Ectoderm"), (MES, "Mesoderm"), (END, "Endoderm"), (COE, "Coelom"))):
    yy = 9.4 - j * 0.6
    bio.box(ax, (21.6, yy), 0.35, 0.3, token=tok, radius=0.05)
    bio.label(ax, (22.0, yy), name, size="small", ha="left")
