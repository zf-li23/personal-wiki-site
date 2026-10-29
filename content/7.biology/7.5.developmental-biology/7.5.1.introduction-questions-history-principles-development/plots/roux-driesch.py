"""Two classic experiments on early blastomeres.

A, Roux (1888): one blastomere of a 2-cell frog embryo is killed with a hot needle and left in place; the
surviving blastomere forms a half-embryo (here a half neurula), as the mosaic hypothesis predicted.
B, Driesch (1892): the blastomeres of a 2-cell sea urchin embryo are separated by shaking (later, in
calcium-free seawater); each forms a complete, smaller pluteus larva: the embryo regulates.
C, the later reinterpretation of Roux's result: if the frog blastomeres are separated instead of one being
killed and left attached, each can form a whole (small) embryo, provided that the first cleavage plane
divided the grey crescent (the future dorsal side) between them.
"""

import numpy as np
from matplotlib.patches import Ellipse, Polygon

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30, 7.4)


def two_cell(c, r=1.0, dead=None, sep=0.0, token="animal"):
    for s in (-1, 1):
        cc = (c[0] + s * (r * 0.5 + sep), c[1])
        dead_cell = dead == s
        ax.add_patch(Ellipse(cc, r * 0.98, r * 1.95, facecolor=P.light("neutral") if dead_cell else P.fill(token),
                             edgecolor=P.edge("neutral") if dead_cell else P.edge(token), lw=1.1,
                             ls=(0, (3, 2)) if dead_cell else "-", zorder=5))
        if dead_cell:
            for d in (-1, 1):
                ax.plot([cc[0] - 0.22, cc[0] + 0.22], [cc[1] - 0.22 * d, cc[1] + 0.22 * d], color=P.edge("negative"), lw=1.6, zorder=6)


def neurula_half(c, L=3.0, H=1.6, half=True):
    t = np.linspace(0, 2 * np.pi, 100)
    xs, ys = c[0] + L / 2 * np.cos(t), c[1] + H / 2 * np.sin(t)
    if half:
        keep = ys >= c[1] - 0.02
        poly = np.c_[xs[keep], ys[keep]]
        poly = np.vstack([poly, [[c[0] - L / 2, c[1]], [c[0] + L / 2, c[1]]]])
        ax.add_patch(Polygon(np.c_[xs, np.maximum(ys, c[1])], closed=True, facecolor=P.fill("animal"), edgecolor=P.edge("animal"),
                             lw=1.1, zorder=5.1))
        ax.add_patch(Polygon(np.c_[xs, np.minimum(ys, c[1])], closed=True, facecolor=P.light("neutral"), edgecolor=P.edge("neutral"),
                             lw=1.0, ls=(0, (3, 2)), zorder=5.0))
        # one neural fold only
        ax.plot(c[0] + np.linspace(-L * 0.4, L * 0.4, 30), c[1] + 0.22 + 0.05 * np.sin(np.linspace(0, 3, 30)),
                color=P.edge("ectoderm"), lw=2.2, zorder=5.3)
    else:
        ax.add_patch(Ellipse(c, L, H, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=1.1, zorder=5.1))
        for s in (-1, 1):
            ax.plot(c[0] + np.linspace(-L * 0.4, L * 0.4, 30), c[1] + s * 0.22 + 0.04 * np.sin(np.linspace(0, 3, 30)),
                    color=P.edge("ectoderm"), lw=2.0, zorder=5.3)


def pluteus(c, s=1.0):
    """A pluteus larva: triangular body with two long arms, gut inside."""
    x, y = c
    body = [(x - 0.9 * s, y + 0.9 * s), (x + 0.9 * s, y + 0.9 * s), (x + 0.45 * s, y - 0.6 * s), (x - 0.45 * s, y - 0.6 * s)]
    ax.add_patch(Polygon(body, closed=True, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("membrane"), lw=1.1, zorder=5))
    for sgn in (-1, 1):
        ax.plot([x + sgn * 0.75 * s, x + sgn * 1.15 * s], [y + 0.85 * s, y + 1.9 * s], color=P.edge("membrane"), lw=3.0 * s,
                solid_capstyle="round", zorder=4.9)
        ax.plot([x + sgn * 0.75 * s, x + sgn * 1.15 * s], [y + 0.85 * s, y + 1.9 * s], color=P.fill("cytoplasm"), lw=1.6 * s,
                solid_capstyle="round", zorder=4.95)
    ax.add_patch(Ellipse((x, y + 0.05 * s), 0.55 * s, 0.7 * s, facecolor=P.fill("endoderm"), edgecolor=P.edge("endoderm"), lw=0.8,
                         zorder=5.2))


# A Roux
bio.panel(ax, "A", (0.2, 7.3))
bio.label(ax, (5.2, 6.8), "Roux 1888: kill one blastomere (frog)", size="normal", bold=True)
two_cell((2.2, 4.0), dead=1)
bio.label(ax, (2.2, 1.8), "hot needle,\ncell left in place", size="tiny", color=P.muted())
bio.arrow(ax, (3.6, 4.0), (5.4, 4.0), kind="process")
neurula_half((7.6, 4.0), half=True)
bio.label(ax, (7.6, 1.8), "half-embryo", size="small", color=P.edge("negative"), bold=True)

# B Driesch
bio.panel(ax, "B", (10.4, 7.3))
bio.label(ax, (15.2, 6.8), "Driesch 1892: separate blastomeres (sea urchin)", size="normal", bold=True)
two_cell((12.4, 4.0), sep=0.25, token="cytoplasm")
bio.label(ax, (12.4, 1.8), "shaken apart", size="tiny", color=P.muted())
bio.arrow(ax, (13.9, 4.0), (15.6, 4.0), kind="process")
pluteus((16.9, 3.8), 0.95)
pluteus((19.2, 3.8), 0.95)
bio.label(ax, (17.95, 1.8), "two small complete larvae", size="small", color=P.edge("positive"), bold=True)

# C Roux revisited
bio.panel(ax, "C", (20.6, 7.3))
bio.label(ax, (25.2, 6.8), "Frog blastomeres separated", size="normal", bold=True)
two_cell((22.6, 4.0), sep=0.25)
bio.label(ax, (22.6, 1.8), "each half contains\ngrey crescent", size="tiny", color=P.muted())
bio.arrow(ax, (24.1, 4.0), (25.6, 4.0), kind="process")
neurula_half((27.6, 5.0), L=2.2, H=1.1, half=False)
neurula_half((27.6, 3.1), L=2.2, H=1.1, half=False)
bio.label(ax, (27.6, 1.8), "two whole small embryos", size="small", color=P.edge("positive"), bold=True)

# trim the empty band at the bottom
ax.set_ylim(1.15, 7.4)
fig.set_size_inches(30 * 0.45, 6.25 * 0.45)
