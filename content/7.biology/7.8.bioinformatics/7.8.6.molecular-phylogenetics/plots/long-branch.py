# Long-branch attraction in the Felsenstein zone. A: the true tree ((A, B), (C, D)), in which the
# non-sister taxa A and C have long branches (1.0 expected substitutions per site) and B, D and the internal
# branch are short (0.1). B: the proportion of 100 simulated data sets (Jukes-Cantor evolution) for which
# each method recovers the true topology, against the number of sites: maximum parsimony (sites supporting
# each split counted), neighbor joining on Jukes-Cantor distances (for four taxa, the pairing with the
# smallest sum of distances), and maximum likelihood under the Jukes-Cantor model (branch lengths
# optimized for each of the three topologies from six starting points). Parsimony converges to the wrong
# tree ((A, C), (B, D)), which groups the long branches; the model-based methods converge to the true
# tree (lba.csv).
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
d = np.genfromtxt("lba.csv", delimiter=",", names=True)
fig, ax = bio.canvas(22.0, 9.0)
# panel A: the quartet drawn by hand (unrooted)
cx, cy = 4.0, 4.6
left, right = (cx - 0.5, cy), (cx + 0.5, cy)
tips = {"A": (left, (left[0] - 2.6, cy + 2.6)), "B": (left, (left[0] - 0.45, cy - 0.45)),
        "C": (right, (right[0] + 2.6, cy - 2.6)), "D": (right, (right[0] + 0.45, cy + 0.45))}
ax.plot([left[0], right[0]], [cy, cy], color=P.ink(), lw=1.6)
for name, (base, tip) in tips.items():
    ax.plot([base[0], tip[0]], [base[1], tip[1]], color=P.ink(), lw=1.6)
    dx, dy = np.sign(tip[0] - base[0]) * 0.3, np.sign(tip[1] - base[1]) * 0.3
    bio.label(ax, (tip[0] + dx, tip[1] + dy), name, size="normal", bold=True)
bio.label(ax, (cx, cy - 0.35), "0.1", size="tiny", color=P.muted())
bio.label(ax, (left[0] - 1.6, cy + 1.0), "1.0", size="tiny", color=P.muted())
bio.label(ax, (right[0] + 1.6, cy - 1.0), "1.0", size="tiny", color=P.muted())
bio.label(ax, (cx, 0.9), "true tree ((A, B), (C, D))", size="small")
b = C.axes_at(ax, (11.0, 1.5, 10.0, 6.8))
for col, tok, lab in [("mp", "negative", "maximum parsimony"), ("nj", "rna", "neighbor joining (JC distances)"),
                      ("ml", "dna", "maximum likelihood (JC)")]:
    b.semilogx(d["n"], d[col], "o-", ms=4, lw=1.3, color=C.line(tok), label=lab)
b.set_ylim(-0.03, 1.05)
b.axhline(1 / 3, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
b.text(55, 0.36, "random choice", fontsize=bio.core.FONT["tiny"], color=P.muted())
C.style_axes(b, "number of sites", "proportion correct topology")
b.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="center right")
bio.panel(ax, "A", (0.3, 8.7))
bio.panel(ax, "B", (9.4, 8.7))
