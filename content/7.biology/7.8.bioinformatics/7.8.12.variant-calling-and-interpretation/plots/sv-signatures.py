# The four signatures of a structural variant in mapped paired-end reads, drawn for a deletion, a
# tandem duplication and an inversion. In each panel the reference is the grey bar, the sample's true
# arrangement is shown above it, and below are the read pairs as they appear after mapping: mates as
# arrows (direction = strand) joined by a thin line. A deletion gives pairs whose insert is larger than
# expected, reads split across the breakpoint (soft-clipped, drawn in two parts) and a drop in depth; a
# tandem duplication gives pairs in the wrong order (the right mate points left of its partner) and a
# rise in depth; an inversion gives pairs whose mates lie on the same strand, with no change of depth.
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(33.0, 10.5)
W = 7.6


def panel(x0, title, brk, depth, pairs, seg_labels, row_labels=False):
    bio.label(ax, (x0 + W / 2, 9.9), title, size="small", bold=True)
    # the sample's arrangement
    for (a, b, tok, txt, arrow) in seg_labels:
        bio.box(ax, (x0 + (a + b) / 2, 8.8), (b - a), 0.5, token=tok, text=txt, size="small")
        if arrow:
            bio.label(ax, (x0 + (a + b) / 2, 8.25), arrow, size="tiny", color=P.muted())
    if row_labels:
        bio.label(ax, (x0 - 0.35, 8.8), "sample", size="tiny", ha="right", color=P.muted())
    # the reference
    bio.box(ax, (x0 + W / 2, 7.3), W, 0.42, token="neutral", text=None)
    for b in brk:
        ax.plot([x0 + b, x0 + b], [6.9, 7.7], color=P.edge("negative"), lw=1.1, ls="--")
    if row_labels:
        bio.label(ax, (x0 - 0.35, 7.3), "reference", size="tiny", ha="right", color=P.muted())
    # read pairs
    for i, (xa, xb, sa, sb, tok, note) in enumerate(pairs):
        y = 6.4 - 0.62 * i
        ax.plot([x0 + xa, x0 + xb], [y, y], color=P.edge(tok), lw=0.7)
        for xx, s in ((xa, sa), (xb, sb)):
            dx = 0.34 * s
            ax.annotate("", xy=(x0 + xx + dx, y), xytext=(x0 + xx - dx, y),
                        arrowprops=dict(arrowstyle="-|>", color=P.edge(tok), lw=1.6, shrinkA=0, shrinkB=0))
        if note:
            bio.label(ax, (x0 + W + 0.1, y), note, size="tiny", ha="left", color=P.muted())
    # depth track
    xs = np.linspace(0, W, 400)
    if row_labels:
        bio.label(ax, (x0 - 0.35, 1.5), "depth", size="tiny", ha="right", color=P.muted())
    ax.plot(x0 + xs, 1.0 + 0.9 * depth(xs), color=P.edge("dna"), lw=1.4)
    ax.plot([x0, x0 + W], [1.0 + 0.9, 1.0 + 0.9], color=P.muted(), lw=0.5, ls="--")


panel(1.6, "A  Deletion", (2.8, 4.8),
      lambda x: np.where((x > 2.8) & (x < 4.8), 0.5, 1.0),
      [(2.2, 5.4, +1, -1, "negative", "insert too large"),
       (2.0, 5.1, +1, -1, "negative", "insert too large"),
       (2.6, 5.2, +1, -1, "highlight", "split read at the junction"),
       (1.2, 2.4, +1, -1, "neutral", "normal"),
       (5.2, 6.6, +1, -1, "neutral", "normal")],
      [(0.0, 2.8, "dna", "A", None), (2.8, 5.0, "dna", "C", None)], row_labels=True)
panel(12.0, "B  Tandem duplication", (2.8, 4.8),
      lambda x: np.where((x > 2.8) & (x < 4.8), 1.5, 1.0),
      [(3.2, 4.4, -1, +1, "negative", "mates in the wrong order"),
       (3.6, 4.6, -1, +1, "negative", "mates in the wrong order"),
       (4.5, 3.0, +1, -1, "highlight", "split read: end joined to start"),
       (1.0, 2.3, +1, -1, "neutral", "normal"),
       (5.1, 6.4, +1, -1, "neutral", "normal")],
      [(0.0, 2.8, "dna", "A", None), (2.8, 4.8, "rna", "B", None),
       (4.8, 6.8, "rna", "B", None)])
panel(22.4, "C  Inversion", (2.8, 4.8),
      lambda x: np.ones_like(x),
      [(2.3, 3.6, +1, +1, "negative", "mates on the same strand"),
       (4.1, 5.4, -1, -1, "negative", "mates on the same strand"),
       (2.6, 4.9, +1, +1, "highlight", "split read at a breakpoint"),
       (0.9, 2.2, +1, -1, "neutral", "normal"),
       (5.3, 6.6, +1, -1, "neutral", "normal")],
      [(0.0, 2.8, "dna", "A", None), (2.8, 4.8, "negative", "B", "reversed"),
       (4.8, 6.8, "dna", "C", None)])
