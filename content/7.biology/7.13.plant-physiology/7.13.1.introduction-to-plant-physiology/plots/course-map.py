# Map of this course: the six parts of the course (rows) against the levels of biological organization they
# are treated at (columns, from molecules to ecosystems); the disc area shows how much weight each level gets
# (an editorial judgement of this course's emphasis). Chapter numbers are given in brackets. Plant physiology connects these levels: molecular mechanisms explain
# cell and organ function, which in turn explain whole-plant behaviour, crop yield and ecosystem fluxes.
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(24.0, 11.0)
pa = charts.axes_at(ax, (8.4, 1.6, 15.0, 8.4))
levels = ["molecule", "cell", "tissue,\norgan", "whole\nplant", "canopy,\ncrop", "ecosystem,\nEarth"]
parts = [
    ("Water and mineral nutrients (2-6)", [1, 3, 2, 3, 2, 1], "dna"),
    ("Photosynthesis and carbon metabolism (7-12)", [3, 2, 3, 2, 2, 2], "chloroplast"),
    ("Hormones and light signals (13-16)", [3, 3, 2, 2, 0, 0], "receptor"),
    ("Growth and development (17-24)", [1, 3, 3, 3, 1, 0], "plant"),
    ("Plants and their environment (25-27)", [2, 2, 2, 3, 2, 2], "metabolite"),
    ("Crop domestication and biotechnology (28-29)", [2, 1, 1, 3, 3, 1], "antibody"),
]
for k, (name, w, tok) in enumerate(parts):
    y = len(parts) - 1 - k
    pa.plot([-0.4, 5.4], [y, y], color=P.mix(P.muted(), P.surface(), 0.7), lw=0.6, zorder=1)
    for j, wj in enumerate(w):
        if wj:
            pa.scatter([j], [y], s=110 * wj, color=P.fill(tok), edgecolor=P.edge(tok), lw=1.0, zorder=3)
    bio.label(ax, (8.1, 1.6 + 8.4 * (y + 0.5) / len(parts)), name, size="small", ha="right")
pa.set_xlim(-0.6, 5.6)
pa.set_ylim(-0.5, len(parts) - 0.5)
pa.set_xticks(range(6))
pa.set_xticklabels(levels)
pa.set_yticks([])
charts.style_axes(pa)
pa.spines["left"].set_visible(False)
bio.label(ax, (15.9, 10.6), "Level of organization", size="small", bold=True)
