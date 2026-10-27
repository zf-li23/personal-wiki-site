"""Five ways in which animal cells communicate.

A contact-dependent (juxtacrine) signaling: a membrane-bound ligand on one cell binds a receptor on
an adjacent cell (Delta-Notch, ephrin-Eph). B paracrine signaling: a local mediator diffuses to
neighboring cells and is removed on the way, so its concentration falls with distance; in autocrine
signaling the secreting cell responds to its own signal. C synaptic signaling: a neuron releases a
neurotransmitter at a synapse onto one target cell. D endocrine signaling: a hormone secreted into
the blood reaches target cells anywhere in the body. E gap junctions: connexin channels join the
cytoplasms of adjacent cells and let ions and small molecules (below about 1 kDa) pass directly.
"""

import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(22.0, 7.0)
TOP = 6.4


def title(x, letter, text):
    bio.panel(ax, letter, (x - 2.05, TOP + 0.35))
    bio.label(ax, (x, TOP), text, size="small", bold=True)


def dots(points, token="metabolite", r=0.07):
    for p in points:
        ax.add_patch(Circle(p, r, facecolor=P.fill(token), edgecolor=P.edge(token), lw=0.6, zorder=14))


# A: contact-dependent
title(2.2, "A", "Contact-dependent")
bio.cell(ax, (1.25, 3.4), 1.05, 1.45, seed=2)
bio.cell(ax, (3.3, 3.4), 1.05, 1.45, seed=5)
for y in (2.8, 3.4, 4.0):
    bio.box(ax, (2.13, y), 0.22, 0.34, token="drug", radius=0.06, zorder=16)
    bio.box(ax, (2.40, y), 0.22, 0.34, token="receptor", radius=0.06, zorder=16)
bio.callout(ax, (2.1, 4.05), (1.2, 5.45), "membrane-bound\nligand", size="tiny")
bio.callout(ax, (2.45, 2.75), (3.4, 1.35), "receptor", size="tiny")
bio.label(ax, (2.2, 0.55), "Delta–Notch, ephrin–Eph", size="tiny", color=P.muted())

# B: paracrine and autocrine
title(6.6, "B", "Paracrine and autocrine")
bio.cell(ax, (5.4, 3.4), 0.95, 1.1, seed=7)
bio.cell(ax, (7.75, 4.5), 0.75, 0.7, seed=8)
bio.cell(ax, (7.85, 2.35), 0.75, 0.7, seed=9)
rng = np.random.default_rng(3)
pts = []
for _ in range(34):
    r = 0.25 + rng.exponential(0.7)
    a = rng.uniform(-1.1, 1.1)
    p = (5.4 + 1.0 + r * np.cos(a), 3.4 + r * np.sin(a) * 1.3)
    if 6.3 < p[0] < 8.9 and 1.4 < p[1] < 5.4 and np.hypot(p[0] - 7.75, p[1] - 4.5) > 0.8 and np.hypot(p[0] - 7.85, p[1] - 2.35) > 0.8:
        pts.append(p)
dots(pts)
bio.arrow(ax, (5.9, 4.45), (5.0, 4.55), kind="process", bend=0.45, color=P.ink(), lw=1.0)
bio.label(ax, (4.95, 5.25), "autocrine", size="tiny", color=P.muted())
bio.label(ax, (6.6, 0.95), "local mediator, removed\nas it spreads", size="tiny", color=P.muted())

# C: synaptic
title(11.0, "C", "Synaptic")
bio.cell(ax, (12.2, 1.9), 0.95, 0.75, seed=11)
bio.structures.neuron(ax, (10.55, 4.6), (11.75, 2.75), soma_r=0.3, dendrites=4, terminals=2, myelin=False)
dots([(11.95, 2.62), (11.82, 2.55), (12.05, 2.7)], r=0.05)
bio.callout(ax, (11.85, 2.65), (12.6, 3.5), "synapse", size="tiny")
bio.label(ax, (11.0, 0.55), "neurotransmitter, µm range, ms", size="tiny", color=P.muted())

# D: endocrine
title(15.5, "D", "Endocrine")
bio.cell(ax, (14.5, 4.6), 0.75, 0.65, seed=13)
ax.add_patch(FancyBboxPatch((13.6, 2.7), 4.0, 0.75, boxstyle="round,pad=0,rounding_size=0.36",
                            facecolor=P.light("blood"), edgecolor=P.edge("blood"), lw=1.2, zorder=6))
dots([(14.6, 3.07), (15.3, 2.95), (15.9, 3.15), (16.6, 3.0), (17.2, 3.1)], token="drug")
for x in (14.1, 15.0, 16.3):
    ax.add_patch(Circle((x, 3.12), 0.12, facecolor=P.fill("blood"), edgecolor=P.edge("blood"), lw=0.6, zorder=13))
bio.arrow(ax, (14.55, 3.95), (14.6, 3.5), kind="process", color=P.ink(), lw=1.0)
bio.arrow(ax, (15.5, 3.75), (16.7, 3.75), kind="process", color=P.muted(), lw=1.0)
bio.cell(ax, (16.9, 1.55), 0.75, 0.6, seed=14)
bio.arrow(ax, (16.9, 2.68), (16.9, 2.2), kind="process", color=P.ink(), lw=1.0)
bio.label(ax, (15.4, 4.6), "endocrine\ncell", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (15.6, 2.1), "blood", size="tiny", color=P.edge("blood"))
bio.label(ax, (15.5, 0.55), "hormone, whole body, min–h", size="tiny", color=P.muted())

# E: gap junctions
title(19.9, "E", "Gap junction")
bio.cell(ax, (18.95, 3.4), 0.95, 1.4, seed=16)
bio.cell(ax, (20.85, 3.4), 0.95, 1.4, seed=17)
for y in (2.85, 3.4, 3.95):
    bio.box(ax, (19.9, y), 0.5, 0.3, token="channel", radius=0.08, zorder=16)
    ax.plot([19.67, 20.13], [y, y], color=P.surface(), lw=1.2, zorder=17)
bio.arrow(ax, (19.3, 4.6), (20.6, 4.6), kind="process", color=P.ink(), lw=1.0)
bio.callout(ax, (19.9, 2.75), (20.7, 1.35), "connexons", size="tiny")
bio.label(ax, (19.95, 5.05), "ions, cAMP, IP₃ (< 1 kDa)", size="tiny", color=P.muted())
bio.label(ax, (19.9, 0.55), "direct cytoplasmic coupling", size="tiny", color=P.muted())
