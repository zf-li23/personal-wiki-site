"""The nucleolus and ribosome biogenesis (schematic).
(A) Nucleolus in section (FC, DFC, GC) with rDNA from NORs of several acrocentric chromosomes converging on it.
(B) A transcribed rRNA gene as in Miller spreads: nascent RNP fibrils lengthen from the promoter ("Christmas tree"),
separated from the next gene by nontranscribed spacer. (C) The pathway from Pol I transcription to cytoplasmic
maturation."""

import numpy as np

import wikibio as bio
from wikibio import nuclear as N

P = bio.P
fig, ax = bio.canvas(23.0, 8.4)

# A
bio.panel(ax, "A", (0.1, 8.3))
c = (3.4, 5.0)
for k, a in enumerate(np.radians([200, 250, 300, 345, 150])):
    p0 = (c[0] + 2.7 * np.cos(a), c[1] + 2.7 * np.sin(a))
    ax.plot([p0[0], c[0] + 1.6 * np.cos(a)], [p0[1], c[1] + 1.6 * np.sin(a)], color=P.edge("chromatin"), lw=4,
            solid_capstyle="round", zorder=4)
nl = N.nucleolus(ax, c, 2.0, units=4, seed=7)
u = nl["units"][0]
bio.callout(ax, u[0], (6.6, 7.6), "FC (rDNA, Pol I)")
bio.callout(ax, (u[0][0] + u[2] * 0.85, u[0][1]), (6.6, 7.0), "DFC (nascent pre-rRNA, fibrillarin)")
bio.callout(ax, (4.9, 3.8), (6.6, 3.6), "GC (preribosomes, nucleophosmin)")
bio.callout(ax, (3.4 + 2.5 * np.cos(np.radians(300)), 5.0 + 2.5 * np.sin(np.radians(300))), (6.6, 2.8),
            "chromatin with NORs (13, 14, 15, 21, 22)")

# B: Christmas trees
bio.panel(ax, "B", (0.1, 0.9 + 0.0))
y = 0.5
ax.plot([0.4, 10.6], [y, y], color=P.edge("dna"), lw=1.6)
for g0 in (0.9, 6.0):
    L = 3.9
    for k in range(26):
        x = g0 + L * (k + 0.5) / 26
        h = 0.08 + 0.9 * (k + 0.5) / 26
        ax.plot([x, x - 0.12 * h], [y, y + h], color=P.edge("rrna"), lw=0.9)
        ax.add_patch(__import__("matplotlib.patches", fromlist=["Circle"]).Circle((x, y), 0.035, color=P.edge("enzyme"), zorder=6))
    bio.label(ax, (g0 + L / 2, y - 0.3), "rRNA gene (13.3 kb)", size="tiny", va="top")
bio.label(ax, (5.45, y + 0.25), "spacer", size="tiny", color=P.muted())
bio.arrow(ax, (1.0, y + 1.25), (2.2, y + 1.25), kind="process")
bio.label(ax, (1.0, y + 1.45), "transcription", size="tiny", ha="left")

# C: pathway
bio.panel(ax, "C", (12.4, 8.3))
steps = [("Pol I transcribes 47S pre-rRNA", "fc", "FC/DFC border"),
         ("snoRNA-guided modification;\nSSU processome, early cleavages", "dfc", "DFC"),
         ("cleavage to 18S, 5.8S, 28S; assembly with\nimported r-proteins and 5S RNP", "gc", "GC"),
         ("export of pre-40S and pre-60S\n(CRM1 and other receptors)", "neutral", "nuclear pore"),
         ("final maturation and quality control", "vesicle", "cytoplasm")]
toks = {"fc": "dna2", "dfc": "rrna", "gc": "nucleolus"}
for k, (t, tk, where) in enumerate(steps):
    yy = 7.4 - k * 1.5
    bio.box(ax, (17.8, yy), 6.6, 1.05, token=toks.get(tk, tk), text=t, size="small")
    bio.label(ax, (21.3, yy), where, size="tiny", ha="left", color=P.muted())
    if k:
        bio.arrow(ax, (17.8, yy + 0.98), (17.8, yy + 0.55), kind="process")
bio.label(ax, (14.2, 0.6), "5S rRNA: Pol III, outside the nucleolus", size="tiny", ha="left", color=P.muted())
