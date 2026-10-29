"""Induction, competence and reciprocal induction in the vertebrate eye (sections through the head).

A-C: the optic vesicle, an outgrowth of the forebrain, contacts the head ectoderm (A); the ectoderm, competent
because it expresses Pax6, thickens into the lens placode (B); the placode invaginates into the lens vesicle,
and the lens in turn induces the optic vesicle to fold into the two-layered optic cup (neural retina inside,
pigmented epithelium outside) (C): each tissue induces the other. D: tissue recombination in the mouse:
optic vesicle with normal ectoderm forms a lens; with ectoderm from Pax6 mutant (Small eye) embryos no lens
forms, whereas mutant optic vesicle with normal ectoderm induces a lens. Competence, here Pax6 in the
responding ectoderm, is as necessary as the inducer.
"""

import numpy as np
from matplotlib.patches import Ellipse, Wedge

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30, 9.0)
ECTO, NEUR = "ectoderm", "neuron"


def surface(x0, x1, y, thick=0.25, bulge=None, token=ECTO):
    xs = np.linspace(x0, x1, 120)
    yt = np.full_like(xs, y)
    yb = np.full_like(xs, y - thick)
    if bulge:
        xc, depth, width, extra = bulge
        g = np.exp(-((xs - xc) / width) ** 2)
        yt = yt - depth * g
        yb = yb - depth * g - extra * g
    bio.shape(ax, np.vstack([np.c_[xs, yt], np.c_[xs[::-1], yb[::-1]]]), token, lw=0.9, zorder=5)


titles = ["Optic vesicle contacts ectoderm", "Lens placode", "Lens vesicle and optic cup", "Recombination (mouse)"]
for k, ttl in enumerate(titles):
    bio.panel(ax, "ABCD"[k], (0.2 + k * 7.5, 8.8))
    bio.label(ax, (3.7 + k * 7.5, 8.35), ttl, size="small", bold=True)

# A
surface(0.6, 6.8, 6.6)
ax.add_patch(Ellipse((3.7, 4.9), 2.6, 2.6, facecolor=P.fill(NEUR), edgecolor=P.edge(NEUR), lw=1.1, zorder=4))
ax.add_patch(Ellipse((3.7, 4.9), 1.8, 1.8, facecolor=P.fill("vacuole"), edgecolor=P.edge(NEUR), lw=0.8, zorder=4.1))
ax.plot([3.7, 3.7], [3.6, 2.0], color=P.edge(NEUR), lw=8, zorder=3.9)
bio.label(ax, (1.2, 7.1), "head ectoderm (Pax6)", size="tiny", ha="left")
bio.label(ax, (3.7, 1.6), "optic vesicle (forebrain)", size="tiny")
bio.arrow(ax, (3.7, 5.95), (3.7, 6.3), kind="activation", head=0.16, bg=P.fill("vacuole"))

# B
surface(8.1, 14.3, 6.6, bulge=(11.2, 0.15, 0.8, 0.25))
ax.add_patch(Ellipse((11.2, 4.7), 2.5, 2.2, facecolor=P.fill(NEUR), edgecolor=P.edge(NEUR), lw=1.1, zorder=3.5))
ax.add_patch(Ellipse((11.2, 4.7), 1.7, 1.4, facecolor=P.fill("vacuole"), edgecolor=P.edge(NEUR), lw=0.8, zorder=3.6))
bio.label(ax, (11.2, 7.15), "lens placode", size="tiny")

# C
surface(15.6, 21.8, 6.9)
ax.add_patch(Wedge((18.7, 5.4), 1.65, 195, 345, width=0.55, facecolor=P.fill(NEUR), edgecolor=P.edge(NEUR), lw=1.1, zorder=4))
ax.add_patch(Wedge((18.7, 5.4), 1.95, 195, 345, width=0.28, facecolor=P.fill("chromatin"), edgecolor=P.edge("chromatin"), lw=0.8,
                   zorder=3.9))
ax.add_patch(Ellipse((18.7, 5.6), 1.4, 1.2, facecolor=P.fill(ECTO), edgecolor=P.edge(ECTO), lw=1.0, zorder=4.2))
ax.add_patch(Ellipse((18.7, 5.6), 0.7, 0.5, facecolor=P.fill("vacuole"), edgecolor=P.edge(ECTO), lw=0.6, zorder=4.3))
ax.plot([11.2, 11.2], [3.6, 2.0], color=P.edge(NEUR), lw=8, zorder=3.4)
ax.plot([18.7, 18.7], [3.5, 1.9], color=P.edge(NEUR), lw=7, zorder=3.8)
bio.callout(ax, (18.7, 5.9), (21.4, 7.9), "lens vesicle", size="tiny")
bio.callout(ax, (17.4, 4.6), (15.9, 2.6), "neural retina", size="tiny")
bio.callout(ax, (20.3, 4.1), (21.6, 2.6), "pigmented epithelium", size="tiny")
bio.arrow(ax, (18.0, 5.2), (17.6, 4.95), kind="activation", head=0.13, bg=P.surface())
bio.arrow(ax, (17.3, 5.4), (17.85, 5.65), kind="activation", head=0.13, bg=P.surface())
bio.label(ax, (18.7, 1.4), "reciprocal induction", size="tiny", color=P.muted())

# D recombination table
rows = [("normal", "normal", True), ("normal", "Pax6 mutant", False), ("Pax6 mutant", "normal", True)]
bio.label(ax, (24.2, 7.4), "optic vesicle", size="tiny", bold=True)
bio.label(ax, (26.4, 7.4), "ectoderm", size="tiny", bold=True)
bio.label(ax, (28.6, 7.4), "lens?", size="tiny", bold=True)
for k, (ov, ec, lens) in enumerate(rows):
    y = 6.4 - k * 1.5
    bio.box(ax, (24.2, y), 2.0, 0.8, NEUR if ov == "normal" else "neutral", text=ov, size="tiny")
    bio.box(ax, (26.4, y), 2.0, 0.8, ECTO if ec == "normal" else "neutral", text=ec, size="tiny")
    bio.box(ax, (28.6, y), 1.2, 0.8, "positive" if lens else "negative", text="yes" if lens else "no", size="tiny")
bio.label(ax, (26.4, 1.6), "the ectoderm must be competent:\nPax6 is required in the responding tissue", size="tiny",
          color=P.muted())

# trim the empty band at the bottom
ax.set_ylim(0.9, 9.0)
fig.set_size_inches(30 * 0.45, 8.1 * 0.45)
