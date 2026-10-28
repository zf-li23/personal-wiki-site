"""The hierarchy of segmentation genes in Drosophila and the class of mutant pattern that defines each tier
(schematic; anterior to the left). Left: the expression of a representative gene of each tier in the
blastoderm. Right: the segmental units present in the corresponding class of mutant larva."""
import numpy as np
import wikibio as bio
from wikibio import development as D

P = bio.P
fig, ax = bio.canvas(19.0, 12.6)
L, H, XE, XM = 6.6, 1.7, 7.5, 14.8
rows = [10.9, 8.5, 6.1, 3.7]
tiers = [("Maternal-effect", "gradients from the egg", "receptor"),
         ("Gap", "broad domains", "channel"),
         ("Pair-rule", "seven stripes", "positive"),
         ("Segment-polarity", "fourteen stripes", "highlight")]

bio.label(ax, (XE, 12.2), "Expression in the blastoderm", size="title", bold=True)
bio.label(ax, (XM, 12.2), "Mutant larval pattern", size="title", bold=True)

for k, ((name, sub, tok), y) in enumerate(zip(tiers, rows)):
    bio.box(ax, (1.9, y), 3.0, 0.8, token=tok, text=name, size="small")
    bio.label(ax, (1.9, y - 0.65), sub, size="tiny", color=P.muted(), va="top")
    if k:
        bio.arrow(ax, (1.9, rows[k - 1] - 1.15), (1.9, y + 0.5), kind="activation")
    e = D.FlyEmbryo(ax, (XE, y), L, H)
    if k == 0:
        e.gradients([(lambda f: np.exp(-f / 0.22), tok), (lambda f: 0.85 * np.exp(-(1 - f) / 0.14), "metabolite")],
                    floor=0.04)
    elif k == 1:
        for a, b in ((0.08, 0.3), (0.38, 0.55), (0.63, 0.8)):
            e.domain(a, b, tok)
    elif k == 2:
        e.stripes(0.32 + 0.07 * np.arange(7), 0.028, tok)
    else:
        e.stripes(0.30 + 0.035 * np.arange(14), 0.012, tok)
    # mutant pattern: the segmental units of the larva, those missing drawn as outlines
    n = 14
    x0, w = XM - 3.5, 0.46
    present = {0: [i >= 7 for i in range(n)],
               1: [not (3 <= i <= 7) for i in range(n)],
               2: [i % 2 == 0 for i in range(n)],
               3: [True] * n}[k]
    for i in range(n):
        xx = x0 + i * (w + 0.06)
        col = P.fill(tok) if present[i] else "none"
        ax.add_patch(bio.core.FancyBboxPatch((xx, y - 0.45), w, 0.9, boxstyle="round,pad=0,rounding_size=0.08",
                                             facecolor=col, edgecolor=P.edge(tok) if present[i] else P.muted(),
                                             lw=1.0, ls="-" if present[i] else (0, (2, 2)), zorder=10))
        if k == 3:
            ax.plot([xx + w * 0.62, xx + w * 0.62], [y - 0.4, y + 0.4], color=P.edge("negative"), lw=1.2, zorder=12)
    note = {0: "a whole region missing", 1: "a contiguous block missing",
            2: "alternate units missing", 3: "all units present, each defective"}[k]
    bio.label(ax, (XM, y - 0.75), note, size="small", color=P.muted(), va="top")

# homeotic tier
y = 1.3
bio.box(ax, (1.9, y), 3.0, 0.8, token="drug", text="Homeotic", size="small")
bio.label(ax, (1.9, y - 0.65), "segment identity", size="tiny", color=P.muted(), va="top")
bio.arrow(ax, (1.9, rows[-1] - 1.15), (1.9, y + 0.5), kind="activation")
x0, w = XM - 3.5, 0.46
for i in range(14):
    xx = x0 + i * (w + 0.06)
    tok = "drug" if i in (5, 6) else "neutral"
    ax.add_patch(bio.core.FancyBboxPatch((xx, y - 0.45), w, 0.9, boxstyle="round,pad=0,rounding_size=0.08",
                                         facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.0, zorder=10))
bio.label(ax, (XM, y - 0.75), "all units present, one has the identity of another", size="small",
          color=P.muted(), va="top")
bio.label(ax, (XE, y), "identity is assigned after the segments exist", size="small", color=P.muted())
