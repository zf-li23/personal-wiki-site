"""A fate map: the late blastula of Xenopus laevis, lateral view, animal pole up, dorsal side right.

The animal half will form ectoderm: epidermis ventrally and the neural plate dorsally. The marginal zone
around the equator will form mesoderm: notochord on the dorsal side (the region of the future dorsal
blastopore lip), somites, then lateral plate and blood ventrally; head mesoderm lies just above the dorsal
notochord region. The vegetal region will form endoderm (gut). The map shows normal fates only: it says what
each region becomes in an undisturbed embryo, not what it could become (its potency).
"""

import numpy as np
from matplotlib.patches import Circle, Polygon

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(20, 10.4)
C, R = (5.6, 5.2), 3.6


def sector(theta0, theta1, r0, r1, token, light=False):
    """A region between two angles (deg, measured from the dorsal side, anticlockwise = towards animal) and radii."""
    th = np.radians(np.linspace(theta0, theta1, 60))
    outer = np.c_[C[0] + r1 * np.cos(th), C[1] + r1 * np.sin(th)]
    inner = np.c_[C[0] + r0 * np.cos(th[::-1]), C[1] + r0 * np.sin(th[::-1])]
    ax.add_patch(Polygon(np.vstack([outer, inner]), closed=True, facecolor=P.light(token) if light else P.fill(token),
                         edgecolor=P.edge(token), lw=0.9, zorder=5))


def band(y0, y1, x_from, token, light=False):
    """The part of the disc between heights y0 and y1 (relative to the centre) and right of x_from."""
    ys = np.linspace(y0, y1, 80)
    xr = np.sqrt(np.clip(R**2 - ys**2, 0, None))
    keep = xr > x_from
    ys, xr = ys[keep], xr[keep]
    xl = np.maximum(-xr, x_from)
    pts = np.vstack([np.c_[C[0] + xr, C[1] + ys], np.c_[C[0] + xl[::-1], C[1] + ys[::-1]]])
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.light(token) if light else P.fill(token), edgecolor=P.edge(token),
                         lw=0.9, zorder=5))


# endoderm (vegetal), mesoderm (marginal zone), ectoderm (animal)
band(-R, -1.0, -R, "endoderm")
band(-1.0, 0.75, -R, "mesoderm", light=True)          # ventral and lateral mesoderm
band(-1.0, 0.75, 1.7, "mesoderm")                    # somites (dorsolateral)
band(-1.0, 0.95, 2.8, "drug")                      # notochord region (dorsal), slightly higher
band(0.75, R, -R, "ectoderm", light=True)             # epidermis
band(0.75, R, 1.0, "ectoderm")                       # neural plate (dorsal animal)
ax.add_patch(Circle(C, R, facecolor="none", edgecolor=P.edge("animal"), lw=1.4, zorder=6))

bio.callout(ax, (C[0] - 1.2, C[1] + 2.2), (0.5, 9.6), "epidermis", size="small")
bio.callout(ax, (C[0] + 2.0, C[1] + 2.0), (9.9, 9.6), "neural plate", size="small")
bio.callout(ax, (C[0] + 3.2, C[1] - 0.1), (10.6, 5.9), "notochord", size="small")
bio.callout(ax, (C[0] + 2.2, C[1] - 0.4), (10.6, 4.7), "somites", size="small")
bio.callout(ax, (C[0] - 2.2, C[1] - 0.1), (0.4, 4.0), "lateral plate,\nblood", size="small")
bio.callout(ax, (C[0], C[1] - 2.4), (2.0, 0.6), "endoderm (gut)", size="small")
bio.label(ax, (C[0], C[1] + R + 0.45), "animal pole", size="tiny", color=P.muted())
bio.label(ax, (C[0], C[1] - R - 0.4), "vegetal pole", size="tiny", color=P.muted())
bio.label(ax, (C[0] - R - 0.5, C[1] + 1.2), "ventral", size="tiny", color=P.muted(), rotation=90)
bio.label(ax, (C[0] + R + 0.5, C[1] + 1.2), "dorsal", size="tiny", color=P.muted(), rotation=90)
bio.label(ax, (C[0], 0.1), "Late blastula: fate map", size="small", bold=True)

# legend of germ layers
for k, (tok, text) in enumerate((("ectoderm", "ectoderm"), ("mesoderm", "mesoderm"), ("endoderm", "endoderm"))):
    y = 8.2 - k * 0.9
    bio.box(ax, (14.6, y), 0.7, 0.5, tok)
    bio.label(ax, (15.2, y), text, size="small", ha="left")
bio.label(ax, (15.9, 4.6), "a fate map records normal fates;\npotency is tested by isolation\nand grafting (7.5.1)", size="tiny",
          color=P.muted())
