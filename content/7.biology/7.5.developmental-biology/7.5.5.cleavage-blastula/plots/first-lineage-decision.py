"""The first lineage decision of the mammalian embryo (mouse, 16- to 32-cell stage). Left: a compacted morula
in section. Outer cells carry an apical domain (Par6–aPKC, purple cap) on their contact-free surface; in
them the Hippo kinase LATS is inactive, YAP enters the nucleus, and with TEAD4 activates Cdx2: they become
trophectoderm (pink). Inner cells are surrounded by cell contacts on all sides and have no apical domain;
angiomotin at their adherens junctions activates LATS, phosphorylated YAP stays in the cytoplasm, and Sox2
and Oct4 persist: they form the inner cell mass (green). Right: the pathway; polarity is read through the
Hippo pathway, so position (inside or outside) and polarity are two aspects of one mechanism."""
import math

import numpy as np
import wikibio as bio
from matplotlib.patches import Circle

P = bio.P
fig, ax = bio.canvas(22, 10)
c = (5.0, 5.0)
R = 3.6
bio.label(ax, (0.4, 9.6), "Morula, 16 to 32 cells (section)", size="small", bold=True, ha="left")
# outer ring of cells
n = 10
for k in range(n):
    a0, a1 = 360 * k / n + 2, 360 * (k + 1) / n - 2
    th = np.radians(np.linspace(a0, a1, 20))
    outer = np.c_[c[0] + R * np.cos(th), c[1] + R * np.sin(th)]
    inner = np.c_[c[0] + 1.75 * np.cos(th[::-1]), c[1] + 1.75 * np.sin(th[::-1])]
    bio.shape(ax, np.vstack([outer, inner]), "receptor", lw=1.0, zorder=5)
    cap = np.vstack([np.c_[c[0] + R * np.cos(th[3:-3]), c[1] + R * np.sin(th[3:-3])],
                     np.c_[c[0] + (R - 0.22) * np.cos(th[3:-3][::-1]), c[1] + (R - 0.22) * np.sin(th[3:-3][::-1])]])
    bio.shape(ax, cap, "protein", lw=0.6, zorder=6)
    m = math.radians((a0 + a1) / 2)
    nc = (c[0] + 2.65 * math.cos(m), c[1] + 2.65 * math.sin(m))
    ax.add_patch(Circle(nc, 0.34, facecolor=P.edge("receptor"), edgecolor=P.edge("receptor"), lw=0.6, zorder=7))
    if k == 2:
        out_nuc = nc
        out_cap = (c[0] + (R - 0.1) * math.cos(m), c[1] + (R - 0.1) * math.sin(m))
# inner cells
for k, (dx, dy) in enumerate(((-0.75, 0.6), (0.75, 0.6), (-0.75, -0.6), (0.75, -0.6))):
    p = (c[0] + dx, c[1] + dy)
    o = bio.blob(p, 0.68, 0.56, wobble=0.04, seed=k, k=8)
    bio.shape(ax, o, "positive", lw=1.0, zorder=5)
    ax.add_patch(Circle(p, 0.25, facecolor=P.light("positive"), edgecolor=P.edge("positive"), lw=0.6, zorder=6))
    for j in range(5):
        a = 2 * math.pi * j / 5 + k
        ax.add_patch(Circle((p[0] + 0.45 * math.cos(a), p[1] + 0.34 * math.sin(a)), 0.05, facecolor=P.edge("drug"), edgecolor="none", zorder=7))
    if k == 1:
        in_cell = p
bio.callout(ax, out_cap, (9.6, 9.0), "apical domain (Par6, aPKC)", size="tiny")
bio.callout(ax, out_nuc, (9.6, 8.2), "nuclear YAP: Cdx2 on", size="tiny")
bio.callout(ax, in_cell, (9.6, 3.0), "inner cell: no apical domain,\ncytoplasmic phospho-YAP", size="tiny")
bio.label(ax, (5.0, 0.7), "outer: trophectoderm     inner: inner cell mass", size="tiny", color=P.muted())

# pathway
x0 = 14.2
bio.label(ax, (x0 - 0.6, 9.6), "Pathway", size="small", bold=True, ha="left")
rows = [("apical domain\n(outside cells)", "protein", 8.4), ("angiomotin, NF2\n(junctions)", "neutral", 6.6), ("LATS1/2", "enzyme", 4.8),
        ("YAP / TAZ", "channel", 3.0)]
for text, tk, y in rows:
    bio.box(ax, (x0 + 1.6, y), 3.2, 1.05, tk, text, size="tiny")
bio.arrow(ax, (x0 + 1.6, 7.85), (x0 + 1.6, 7.15), kind="inhibition")
bio.label(ax, (x0 + 1.85, 7.5), "sequesters", size="tiny", color=P.muted(), ha="left")
bio.arrow(ax, (x0 + 1.6, 6.05), (x0 + 1.6, 5.35), kind="activation")
bio.arrow(ax, (x0 + 1.6, 4.25), (x0 + 1.6, 3.55), kind="inhibition")
bio.label(ax, (x0 + 1.85, 3.9), "phosphorylates", size="tiny", color=P.muted(), ha="left")
bio.box(ax, (x0 + 5.6, 3.0), 2.6, 1.05, "receptor", "TEAD4\nCdx2, Gata3", size="tiny")
bio.box(ax, (x0 + 5.6, 5.4), 2.6, 1.05, "positive", "Sox2, Oct4", size="tiny")
bio.arrow(ax, (x0 + 3.25, 3.0), (x0 + 4.25, 3.0), kind="activation")
bio.arrow(ax, (x0 + 5.6, 3.55), (x0 + 5.6, 4.85), kind="inhibition")
bio.label(ax, (x0 + 5.6, 1.9), "trophectoderm", size="tiny", color=P.muted())
bio.label(ax, (x0 + 5.6, 6.3), "inner cell mass", size="tiny", color=P.muted())
