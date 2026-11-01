# Liftover with a chain file, toy coordinates in kb. Gap-free aligned blocks pair segments of the source assembly
# (top) with the target (bottom). Block 1 maps with offset 0 and block 2 with offset -8 (the 8 kb between them
# are absent from the target); 8 kb are inserted in the target after block 2; blocks 3 and 4 are swapped and
# block 3 is inverted (a reversed chain). Position 50 maps to 50 - 8 = 42; position 34 lies in the deleted
# segment and fails; position 75, in the inverted block, maps to 100 - (75 - 70) - 1 = 94 on the other strand.
from matplotlib.patches import Polygon, Rectangle
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26.0, 9.0)
x0, sc = 3.0, 0.21  # canvas x of position 0, units per kb
ys, yt, h = 6.6, 2.4, 0.55


def X(p):
    return x0 + p * sc


blocks = [(0, 30, 0, 30, False, "dna"), (38, 70, 30, 62, False, "dna"), (70, 85, 85, 100, True, "rna"),
          (85, 100, 70, 85, False, "protein")]
for y, lab in [(ys, "source (old assembly)"), (yt, "target (new assembly)")]:
    ax.add_patch(Rectangle((X(0), y - h / 2), X(100) - X(0), h, facecolor=P.light("neutral"),
                           edgecolor=P.edge("neutral"), lw=0.6, zorder=2))
    bio.label(ax, (X(0) - 0.3, y), lab, size="small", ha="right")
for k, (s0, s1, t0, t1, rev, tok) in enumerate(blocks):
    for y, a, b in [(ys, s0, s1), (yt, t0, t1)]:
        ax.add_patch(Rectangle((X(a), y - h / 2), X(b) - X(a), h, facecolor=P.fill(tok), edgecolor=P.edge(tok),
                               lw=0.8, zorder=3))
    top = [(X(s0), ys - h / 2), (X(s1), ys - h / 2)]
    bot = [(X(t1), yt + h / 2), (X(t0), yt + h / 2)] if not rev else [(X(t0), yt + h / 2), (X(t1), yt + h / 2)]
    ax.add_patch(Polygon(top + bot, closed=True, facecolor=P.light(tok), edgecolor=P.edge(tok), lw=0.5, zorder=1))
    bio.label(ax, ((X(s0) + X(s1)) / 2, ys + 0.65), f"block {k + 1}" + (" (reversed)" if rev else ""), size="tiny")
bio.label(ax, (X(34), ys + 0.65), "deleted", size="tiny", color=P.edge("negative"))
bio.label(ax, (X(66), yt - 0.7), "inserted", size="tiny", color=P.muted())
for p in range(0, 101, 20):
    for y in (ys, yt):
        bio.label(ax, (X(p), y - 0.65 if y == ys else y - 1.15), f"{p}", size="tiny", color=P.muted())
# mapped positions
for p, q, ok in [(50, 42, True), (34, None, False), (75, 94, True)]:
    col = P.edge("positive") if ok else P.edge("negative")
    ax.plot([X(p)], [ys + 0.05], marker="v", color=col, ms=7, zorder=8)
    if ok:
        bio.arrow(ax, (X(p), ys - h / 2 - 0.05), (X(q), yt + h / 2 + 0.05), kind="process", color=col, lw=1.3, head=0.2)
        ax.plot([X(q)], [yt - 0.05], marker="^", color=col, ms=7, zorder=8)
    else:
        ax.plot([X(p), X(p)], [ys - h / 2, ys - 1.6], color=col, lw=1.3)
        bio.label(ax, (X(p), ys - 1.95), "x  fails", size="small", color=col)
bio.label(ax, (X(50) + 0.3, 4.9), "50 -> 42", size="small", ha="left", color=P.edge("positive"))
bio.label(ax, (X(75) + 0.4, 4.2), "75 -> 94 (minus strand)", size="small", ha="left", color=P.edge("positive"))
bio.label(ax, (X(50), 0.35), "position (kb)", size="tiny", color=P.muted())
