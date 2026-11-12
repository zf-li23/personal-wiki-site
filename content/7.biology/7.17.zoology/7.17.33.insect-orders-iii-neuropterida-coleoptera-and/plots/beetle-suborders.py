# Ventral view of the thorax and abdomen in the two large suborders of beetles (schematic, legs cut
# off at the coxae). In Adephaga (ground beetles, diving beetles) the hind coxae are immovably fused to
# the metasternum and extend backward so that they divide the first visible abdominal sternite completely
# into two lateral pieces; the prothorax shows a notopleural suture. In Polyphaga the hind coxae are
# movable and do not divide the first visible sternite, which extends across the body behind them.
import numpy as np
from matplotlib.patches import Polygon
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(28, 12.5)


def piece(pts, tok, z=5, lw=0.9):
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=lw, zorder=z,
                         joinstyle="round"))


def beetle(cx, adephaga):
    W = 2.6
    # head
    piece([(cx - 1.0, 10.6), (cx + 1.0, 10.6), (cx + 0.8, 11.5), (cx - 0.8, 11.5)], "neutral")
    # prosternum and its process
    piece([(cx - W * 0.85, 10.6), (cx + W * 0.85, 10.6), (cx + W * 0.95, 9.0), (cx - W * 0.95, 9.0)], "protein")
    for s in (-1, 1):  # fore coxae
        piece([(cx + s * 0.25, 9.9), (cx + s * 1.0, 9.9), (cx + s * 1.0, 9.2), (cx + s * 0.25, 9.2)], "coxa", z=6)
        if adephaga:  # notopleural suture
            ax.plot([cx + s * W * 0.88, cx + s * W * 0.6], [10.0, 9.05], color=P.edge("protein"), lw=1.2, zorder=7)
    # mesothorax
    piece([(cx - W * 0.95, 9.0), (cx + W * 0.95, 9.0), (cx + W, 8.0), (cx - W, 8.0)], "enzyme")
    for s in (-1, 1):
        piece([(cx + s * 0.25, 8.85), (cx + s * 1.0, 8.85), (cx + s * 1.0, 8.2), (cx + s * 0.25, 8.2)], "coxa", z=6)
    # metathorax (metasternum)
    piece([(cx - W, 8.0), (cx + W, 8.0), (cx + W, 6.3), (cx - W, 6.3)], "channel")
    # abdomen: sternites
    ys = [6.3, 5.4, 4.6, 3.85, 3.15, 2.5]
    widths = [W, W * 0.97, W * 0.93, W * 0.86, W * 0.74, W * 0.55]
    for i in range(5):
        y0, y1 = ys[i], ys[i + 1]
        w0, w1 = widths[i], widths[i + 1]
        piece([(cx - w0, y0), (cx + w0, y0), (cx + w1, y1), (cx - w1, y1)], "bone")
    piece([(cx - widths[5], 2.5), (cx + widths[5], 2.5), (cx, 1.9)], "bone")
    # hind coxae
    for s in (-1, 1):
        if adephaga:
            pts = [(cx + s * 0.05, 6.6), (cx + s * 2.0, 6.6), (cx + s * 2.2, 6.1), (cx + s * 0.05, 5.4)]
        else:
            pts = [(cx + s * 0.2, 6.65), (cx + s * 2.1, 6.65), (cx + s * 2.1, 6.3), (cx + s * 0.2, 6.3)]
        piece(pts, "coxa", z=7, lw=1.1)
    return ys


A, B = 8.5, 19.5
beetle(A, True)
beetle(B, False)
bio.label(ax, (A, 12.2), "Adephaga", size="title", bold=True)
bio.label(ax, (B, 12.2), "Polyphaga", size="title", bold=True)
bio.callout(ax, (A - 2.05, 9.6), (4.9, 10.6), "Notopleural suture", size="small")
bio.callout(ax, (A - 1.0, 6.0), (4.9, 7.3), "Hind coxae reach back and\ndivide the first sternite", size="small")
bio.callout(ax, (A - 2.4, 5.85), (4.9, 4.6), "First visible sternite:\ntwo lateral pieces", size="small")
bio.callout(ax, (B + 1.6, 6.45), (23.1, 7.3), "Hind coxae movable,\nnot dividing the sternite", size="small")
bio.callout(ax, (B + 1.8, 5.85), (23.1, 4.6), "First visible sternite\nentire", size="small")
for (y, t) in ((9.8, "Prothorax"), (8.5, "Mesothorax"), (7.2, "Metathorax"), (4.0, "Abdominal\nsternites")):
    bio.label(ax, (14.0, y), t, size="small", color=P.muted())
bio.label(ax, (27.8, 0.4), "Schematic ventral views; legs removed at the coxae", size="tiny", color=P.muted(), ha="right")
