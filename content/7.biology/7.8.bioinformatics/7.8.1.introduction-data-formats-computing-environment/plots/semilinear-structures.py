# Six kinds of semi-linear structure. A: an annotated sequence (a gene of two exons and a binding site as labelled
# intervals). B: a pairwise alignment with one gap. C: an RNA secondary structure as an arc diagram (nested,
# non-crossing pairs; dot-bracket shown below). D: a rooted tree of four sequences. E: the de Bruijn graph of the
# 3-mers of ATGCGTGC (nodes are 2-mers, one edge per 3-mer); the walk using every edge once spells the sequence.
# F: a profile drawn as a sequence logo (letter heights scaled by information content).
import numpy as np
from matplotlib.patches import Arc, Rectangle
import wikibio as bio
from wikibio import sequence as S

P = bio.P
fig, ax = bio.canvas(30.0, 13.0)


def title(xy, letter, text):
    bio.panel(ax, letter, xy)
    bio.label(ax, (xy[0] + 0.7, xy[1] - 0.25), text, size="normal", bold=True, ha="left")


# A: annotated sequence
title((0.3, 12.8), "A", "annotated sequence")
ax.plot([1, 9.2], [10.0, 10.0], color=P.edge("dna"), lw=2.0)
for (a, b, tok, lab) in [(2.0, 3.4, "dna", "exon 1"), (5.6, 7.2, "dna", "exon 2"), (8.0, 8.6, "highlight", "site")]:
    ax.add_patch(Rectangle((a, 9.7), b - a, 0.6, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=4))
    bio.label(ax, ((a + b) / 2, 10.75), lab, size="small")
ax.plot([3.4, 4.5, 5.6], [10.3, 10.7, 10.3], color=P.edge("dna"), lw=0.9)
bio.label(ax, (4.5, 9.2), "intervals [start, end) on one strand", size="tiny", color=P.muted())

# B: pairwise alignment
title((10.3, 12.8), "B", "alignment")
S.alignment(ax, {"seq1": "ACGTTGCAGCTA", "seq2": "ACGATGC-GCTA"}, at=(12.2, 11.0), cell=(0.55, 0.62),
            color_by="residue", consensus=False, conservation=False, ruler=False, marks=False)

# C: arc diagram
title((20.3, 12.8), "C", "nested base pairs")
db = "((((...))))..(((...)))"
xs = np.linspace(21.0, 29.4, len(db))
stack = []
for i, c in enumerate(db):
    if c == "(":
        stack.append(i)
    elif c == ")":
        j = stack.pop()
        cx, w = (xs[i] + xs[j]) / 2, xs[i] - xs[j]
        ax.add_patch(Arc((cx, 9.0), w, w * 0.9, theta1=0, theta2=180, color=P.edge("rna"), lw=1.1, zorder=3))
ax.plot([xs[0], xs[-1]], [9.0, 9.0], color=P.edge("rna"), lw=1.4, zorder=4)
ax.scatter(xs, np.full(len(xs), 9.0), s=8, color=P.edge("rna"), zorder=5)
bio.label(ax, ((xs[0] + xs[-1]) / 2, 8.4), db, size="small")

# D: tree
title((0.3, 7.6), "D", "tree")
tips = {"A": 6.4, "B": 5.4, "C": 4.0, "D": 3.0}
xr, xm, xt = 1.2, 3.2, 7.4
ax.plot([xr, xr], [5.9, 3.5], color=P.ink(), lw=1.3)
for (u, v, y) in [("A", "B", 5.9), ("C", "D", 3.5)]:
    ax.plot([xr, xm], [y, y], color=P.ink(), lw=1.3)
    ax.plot([xm, xm], [tips[u], tips[v]], color=P.ink(), lw=1.3)
    for t in (u, v):
        ax.plot([xm, xt], [tips[t], tips[t]], color=P.ink(), lw=1.3)
        bio.label(ax, (xt + 0.3, tips[t]), "seq " + t, size="small", ha="left")
ax.plot([0.7, xr], [4.7, 4.7], color=P.ink(), lw=1.3)
bio.label(ax, (4.5, 2.2), "((A,B),(C,D));", size="small", color=P.muted())

# E: de Bruijn graph
title((10.3, 7.6), "E", "de Bruijn graph of 3-mers")
pos = {"AT": (11.4, 4.6), "TG": (14.0, 4.6), "GC": (17.0, 4.6), "CG": (17.0, 2.4), "GT": (14.0, 2.4)}
for n, (x, y) in pos.items():
    bio.box(ax, (x, y), 1.2, 0.7, token="dna", text=n, size="small")
edges = [("AT", "TG", 0.0, "ATG"), ("TG", "GC", 0.5, "TGC"), ("TG", "GC", -0.5, "TGC"), ("GC", "CG", 0.0, "GCG"),
         ("CG", "GT", 0.0, "CGT"), ("GT", "TG", 0.0, "GTG")]
for u, v, bend, lab in edges:
    (xa, ya), (xb, yb) = pos[u], pos[v]
    d = np.array([xb - xa, yb - ya]); d = d / np.linalg.norm(d)
    a = (xa + 0.75 * d[0] * (abs(d[0]) > 0.5) + 0.0, ya + 0.45 * d[1])
    b = (xb - 0.75 * d[0] * (abs(d[0]) > 0.5), yb - 0.45 * d[1])
    bio.arrow(ax, a, b, kind="process", bend=bend, lw=1.0, head=0.16)
bio.label(ax, (15.5, 5.55), "TGC (x2)", size="tiny", color=P.muted())
bio.label(ax, (14.6, 1.4), "Eulerian walk spells ATGCGTGC", size="tiny", color=P.muted())

# F: profile (sequence logo)
title((20.3, 7.6), "F", "profile")
counts = np.array([[8, 1, 1, 0], [0, 0, 10, 0], [1, 7, 1, 1], [3, 3, 2, 2], [0, 0, 0, 10], [9, 0, 1, 0], [2, 1, 6, 1]])
S.logo(ax, counts, at=(21.6, 2.6), col_width=0.9, height=3.2)
