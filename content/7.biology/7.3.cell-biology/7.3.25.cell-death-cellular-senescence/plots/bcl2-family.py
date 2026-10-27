"""The Bcl-2 family: domain architecture and the selectivity of BH3-only proteins.

(A) Three classes defined by Bcl-2 homology (BH) domains: anti-apoptotic proteins (Bcl-2, Bcl-xL, Bcl-w,
Mcl-1, A1) have BH1-4 and usually a C-terminal transmembrane anchor (TM); the effectors Bax and Bak have
BH1-3 and TM; BH3-only proteins share only the amphipathic BH3 helix, which binds the hydrophobic groove
formed by BH1-3 of the other two classes.
(B) Binding of BH3 peptides to anti-apoptotic proteins (qualitative, after Chen et al. 2005, Mol. Cell 17:393,
and Certo et al. 2006, Cancer Cell 9:351): the activators Bim and Puma (and tBid) bind all five, Bad only
Bcl-2, Bcl-xL and Bcl-w, Noxa only Mcl-1 and A1. Killing by sensitizers needs both groups neutralized, so
Bad and Noxa together, but neither alone, kill a cell protected by Bcl-xL and Mcl-1.
"""

import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(25.0, 9.0)

# ---------------------------------------------------------------- A: domains
bio.panel(ax, "A", (0.2, 8.8))
DOM = {"BH4": "highlight", "BH3": "negative", "BH1": "enzyme", "BH2": "channel", "TM": "membrane"}
rows = [
    ("anti-apoptotic", "Bcl-2, Bcl-xL, Bcl-w,\nMcl-1, A1", [("BH4", 0.6), ("BH3", 2.6), ("BH1", 4.0), ("BH2", 5.6), ("TM", 7.2)]),
    ("pro-apoptotic effectors", "Bax, Bak (Bok)", [("BH3", 2.6), ("BH1", 4.0), ("BH2", 5.6), ("TM", 7.2)]),
    ("BH3-only", "Bim, Bid, Puma,\nBad, Noxa, Bik, Hrk", [("BH3", 2.6)]),
]
x0 = 4.8
for i, (cls, names, doms) in enumerate(rows):
    y = 7.0 - i * 2.4
    bio.label(ax, (0.3, y + 0.35), cls, size="small", bold=True, ha="left")
    bio.label(ax, (0.3, y - 0.45), names, size="tiny", ha="left", color=P.muted())
    L = 8.2 if i < 2 else 5.0
    ax.plot([x0, x0 + L], [y, y], color=P.muted(), lw=2.0, solid_capstyle="round", zorder=3)
    for name, at in doms:
        w = 0.9 if name != "TM" else 0.7
        ax.add_patch(FancyBboxPatch((x0 + at, y - 0.32), w, 0.64, boxstyle="round,pad=0,rounding_size=0.1",
                                    facecolor=P.fill(DOM[name]), edgecolor=P.edge(DOM[name]), lw=0.9, zorder=5))
        bio.label(ax, (x0 + at + w / 2, y), name, size="tiny", color=P.on_fill(), zorder=6)
bio.label(ax, (x0, 1.0), "N", size="tiny", color=P.muted())
bio.label(ax, (x0 + 8.2, 1.0), "C", size="tiny", color=P.muted())
bio.label(ax, (x0 + 4.1, 0.4), "BH3 helix binds the groove formed by BH1–BH3", size="tiny", color=P.muted())

# ---------------------------------------------------------------- B: selectivity matrix
bio.panel(ax, "B", (14.2, 8.8))
anti = ["Bcl-2", "Bcl-xL", "Bcl-w", "Mcl-1", "A1"]
bh3 = ["Bim", "Puma", "tBid", "Bad", "Noxa"]
M = np.array([[2, 2, 2, 2, 2],
              [2, 2, 2, 2, 2],
              [1, 2, 2, 2, 2],
              [2, 2, 2, 0, 0],
              [0, 0, 0, 2, 2]])
cx, cy, s = 17.4, 7.2, 1.05
for j, a in enumerate(anti):
    bio.label(ax, (cx + j * s, cy + 0.85), a, size="tiny", rotation=0)
for i, b in enumerate(bh3):
    bio.label(ax, (cx - 0.75, cy - i * s), b, size="small", ha="right")
    for j in range(len(anti)):
        v = M[i, j]
        tok = {2: "negative", 1: "drug", 0: "neutral"}[v]
        ax.add_patch(Rectangle((cx + j * s - s / 2 + 0.04, cy - i * s - s / 2 + 0.04), s - 0.08, s - 0.08,
                               facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.6, zorder=5))
        bio.label(ax, (cx + j * s, cy - i * s), {2: "++", 1: "+", 0: "–"}[v], size="tiny", color=P.on_fill(), zorder=6)
bio.label(ax, (cx + 2 * s, cy + 1.6), "anti-apoptotic partner", size="small", bold=True)
ax.plot([cx - 1.9, cx - 1.9], [cy + 0.4, cy - 2.4], color=P.muted(), lw=0.8)
bio.label(ax, (cx - 2.25, cy - 1.0), "activators", size="tiny", color=P.muted(), rotation=90)
ax.plot([cx - 1.9, cx - 1.9], [cy - 2.7, cy - 4.4], color=P.muted(), lw=0.8)
bio.label(ax, (cx - 2.25, cy - 3.55), "sensitizers", size="tiny", color=P.muted(), rotation=90)
for k, (tok, txt) in enumerate([("negative", "++ tight"), ("drug", "+ weaker"), ("neutral", "– no binding")]):
    xx = cx - 0.6 + k * 2.0
    ax.add_patch(Rectangle((xx, 1.0), 0.35, 0.35, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.6))
    bio.label(ax, (xx + 0.5, 1.17), txt, size="tiny", ha="left")
