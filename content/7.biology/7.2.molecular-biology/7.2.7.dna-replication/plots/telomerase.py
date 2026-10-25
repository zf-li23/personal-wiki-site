# The end-replication problem and one catalytic cycle of human telomerase.
# A: the right-hand end of a linear chromosome (G-rich strand 5'->3' towards the end). After replication,
# the daughter whose new strand is the lagging strand lacks the end of that strand (the last RNA primer
# is removed and cannot be replaced), leaving a 3' overhang; the leading-strand daughter is blunt until
# its C-rich 5' end is resected. B: telomerase aligns the 3' end ...GTTAG-3' with the 3' end of its RNA
# template 3'-CAAUCCCAAUC-5', copies the rest of the template (adding GGTTAG), translocates and repeats.
import numpy as np
import wikibio as bio
from wikibio import molbio as MB

P = bio.P
fig, ax = bio.canvas(20.5, 10.6)
half = 0.22
lab = dict(size="tiny", bold=True)


# ---------------------------------------------------------------- A: end-replication problem
def duplex(y, x0, x1, top=(None, None), bot=(None, None), seed="d", top_new=False, bot_new=False, primer=None):
    """Two strands from x0 to x1; top/bot give (start, end) of each strand if shorter."""
    xs = np.arange(x0 + 0.1, x1, 0.2)
    seq = MB.sequence(len(xs), seed)
    t0, t1 = top[0] or x0, top[1] or x1
    b0, b1 = bot[0] or x0, bot[1] or x1
    ut = (xs >= t0) & (xs <= t1)
    ub = (xs >= b0) & (xs <= b1)
    both = ut & ub
    tp, bp = MB.track(xs, y + half), MB.track(xs, y - half)
    MB.ladder(ax, tp[both], bp[both], [seq[i] for i in np.where(both)[0]])
    MB.stubs(ax, tp[ut & ~ub], (0, -1), [seq[i] for i in np.where(ut & ~ub)[0]])
    MB.stubs(ax, bp[ub & ~ut], (0, 1), [MB.complement(seq)[i] for i in np.where(ub & ~ut)[0]])
    MB.backbone(ax, [(t0, y + half), (t1, y + half)], "dna", shade="fill" if top_new else "edge")
    MB.backbone(ax, [(b0, y - half), (b1, y - half)], "dna", shade="fill" if bot_new else "edge")
    if primer:
        MB.backbone(ax, [(primer[0], y - half), (primer[1], y - half)], "rna", dashed=True)


bio.panel(ax, "A", (0.3, 10.1))
bio.label(ax, (0.9, 10.1), "The end-replication problem", size="normal", bold=True, ha="left")
xL, xR = 1.0, 8.6

# parental end
y = 8.7
duplex(y, xL, xR, seed="par")
bio.label(ax, (xL - 0.35, y + half), "5′", **lab)
bio.label(ax, (xR + 0.35, y + half), "3′", **lab)
bio.label(ax, (xL - 0.35, y - half), "3′", **lab)
bio.label(ax, (xR + 0.35, y - half), "5′", **lab)
bio.label(ax, (4.8, y + 0.75), "Parental chromosome end (G-rich strand on top)", size="small", color=P.muted())
bio.arrow(ax, (4.8, 7.75), (4.8, 7.15), kind="process")
bio.label(ax, (5.0, 7.45), "replication", size="tiny", color=P.muted(), ha="left")

# daughter 1: top parental, bottom new = lagging strand, missing its end
y = 6.2
duplex(y, xL, xR, bot=(None, 7.1), seed="par", bot_new=True, primer=(7.15, 7.95))
bio.label(ax, (xL - 0.35, y + half), "5′", **lab)
bio.label(ax, (xR + 0.35, y + half), "3′", **lab)
bio.label(ax, (xL - 0.35, y - half), "3′", **lab)
bio.label(ax, (7.1, y - half - 0.38), "5′", **lab)
bio.label(ax, (4.0, y - 0.95), "Lagging-strand daughter: the last primer (dashed) is removed,", size="tiny", color=P.muted())
bio.label(ax, (4.0, y - 1.3), "and the gap cannot be filled: 3′ overhang", size="tiny", color=P.muted())

# daughter 2: bottom parental, top new = leading strand, complete; then resected
y = 3.4
duplex(y, xL, xR, seed="par", top_new=True)
bio.label(ax, (xL - 0.35, y + half), "5′", **lab)
bio.label(ax, (xR + 0.35, y + half), "3′", **lab)
bio.label(ax, (xL - 0.35, y - half), "3′", **lab)
bio.label(ax, (xR + 0.35, y - half), "5′", **lab)
bio.label(ax, (4.0, y - 0.75), "Leading-strand daughter: copied to the end (blunt) ...", size="tiny", color=P.muted())
y = 1.4
duplex(y, xL, xR, bot=(None, 7.0), seed="par", top_new=True)
bio.label(ax, (xR + 0.35, y + half), "3′", **lab)
bio.label(ax, (7.0, y - half - 0.38), "5′", **lab)
bio.label(ax, (4.0, y - 0.75), "... then the C-rich 5′ end is resected: G-rich 3′ overhang", size="tiny", color=P.muted())

# ---------------------------------------------------------------- B: telomerase cycle
bio.panel(ax, "B", (10.3, 10.1))
bio.label(ax, (10.9, 10.1), "One cycle of telomerase", size="normal", bold=True, ha="left")
dx = 0.36
xr = 15.4                    # left edge of the RNA template (its 3' end)
RNA = "CAAUCCCAAUC"          # written 3' -> 5', left to right
rows = [
    (8.25, "GGTTAGGGTTAG", 5, "1  Alignment: 3′ end of the DNA pairs with the template"),
    (5.25, "GGTTAGGGTTAGGGTTAG", 11, "2  Elongation: reverse transcription adds GGTTAG"),
    (2.25, "GGTTAGGGTTAGGGTTAG", 5, "3  Translocation: the new 3′ end re-pairs; repeat"),
]
for k, (yd, dna, paired, text) in enumerate(rows):
    yr = yd - 0.62
    n = len(dna)
    x0 = xr - (n - paired) * dx
    MB.polymerase(ax, (xr + 2.0, yr - 0.05), 5.6, 1.55, "enzyme", alpha=0.55, seed="tert", zorder=3)
    xs_d = MB.codons(ax, x0, yd, dna, dx=dx)
    xs_r = MB.codons(ax, xr, yr, RNA, dx=dx)
    ax.plot([x0 - 0.1, x0 + n * dx - 0.08], [yd + 0.25] * 2, color=P.edge("dna"), lw=2.2, solid_capstyle="round", zorder=10)
    ax.plot([xr - 0.1, xr + len(RNA) * dx - 0.08], [yr - 0.25] * 2, color=P.edge("rna"), lw=2.2, solid_capstyle="round", zorder=10)
    bio.label(ax, (x0 - 0.35, yd + 0.05), "5′", **lab)
    bio.label(ax, (x0 + n * dx + 0.2, yd + 0.05), "3′", **lab)
    bio.label(ax, (xr - 0.35, yr - 0.05), "3′", **lab)
    bio.label(ax, (xr + len(RNA) * dx + 0.2, yr - 0.05), "5′", **lab)
    if k == 1:
        a, b = x0 + (n - 6) * dx - 0.15, x0 + n * dx - 0.2
        ax.plot([a, a, b, b], [yd + 0.42, yd + 0.55, yd + 0.55, yd + 0.42], color=P.edge("highlight"), lw=1.2, zorder=11)
        bio.label(ax, ((a + b) / 2, yd + 0.8), "added", size="tiny", color=P.edge("highlight"))
    bio.label(ax, (10.8, yd + 0.95), text, size="small", ha="left")
    if k == 0:
        bio.label(ax, (xr + 2.0, yr - 0.62), "RNA template (TR)", size="tiny", color=P.muted())
bio.label(ax, (19.3, 1.05), "TERT + TR", size="tiny", color=P.edge("enzyme"), ha="right")
for y0, y1 in ((7.15, 6.45), (4.15, 3.45)):
    bio.arrow(ax, (12.2, y0), (12.2, y1), kind="process")
