"""Resegmentation of the vertebral column (dorsal view of one side, anterior up)."""
import numpy as np
from matplotlib.patches import FancyBboxPatch
import wikibio as bio

fig, ax = bio.canvas(18, 12.5)
P = bio.P
H = 3.0           # somite length
y_top = 11.0
ys = [y_top - k * H for k in range(4)]   # somite tops


def rect(x, y, w, h, tok, light=False, ls="-", lw=0.9, z=5, rr=0.1):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=%g" % rr,
                                facecolor=P.light(tok) if light else P.fill(tok), edgecolor=P.edge(tok), lw=lw, linestyle=ls, zorder=z))


# panel A: somites
bio.panel(ax, "A", (0.2, 12.2))
for k in range(3):
    yt = ys[k]
    rect(1.0, yt - H / 2 + 0.05, 2.2, H / 2 - 0.1, "bone", light=True)        # rostral half
    rect(1.0, yt - H + 0.05, 2.2, H / 2 - 0.1, "bone")                         # caudal half
    rect(3.4, yt - H + 0.1, 1.4, H - 0.2, "muscle")                           # myotome
    ax.plot([0.2, 5.8], [yt - H / 4, yt - H / 4], color=P.edge("neuron"), lw=1.8, zorder=7)
    bio.label(ax, (2.1, yt - H / 4 - 0.45), "rostral", size="tiny")
    bio.label(ax, (2.1, yt - 3 * H / 4), "caudal", size="tiny")
    bio.label(ax, (4.1, yt - H / 2), "myotome", size="tiny", rotation=90, color=P.on_fill())
    bio.label(ax, (0.4, yt - H / 2), "somite %d" % (k + 1), size="tiny", rotation=90, color=P.muted())
bio.label(ax, (3.0, 11.6), "Sclerotome halves and myotomes", size="small", bold=True)
bio.callout(ax, (5.6, ys[0] - H / 4), (6.6, ys[0] + 0.25), "Spinal nerve")

# panel B: vertebrae
bio.panel(ax, "B", (8.6, 12.2))
X = 10.0
for k in range(4):
    yt = ys[k]
    ax.plot([X - 0.3, X + 6.4], [yt, yt], color=P.muted(), lw=0.5, ls=":", zorder=3)
for k in range(4):
    yd = ys[k] - H / 2      # discs at mid-somite
    if k < 3:
        rect(X, yd + 0.12 - H, 2.2, H - 0.24, "bone", z=5)                    # vertebral body spans caudal(k)+rostral(k+1)
        ax.add_patch(FancyBboxPatch((X + 0.02, yd - H + 0.14), 2.16, H / 2 - 0.14, boxstyle="round,pad=0,rounding_size=0.1",
                                    facecolor=P.light("bone"), edgecolor="none", zorder=5.1))
        rect(X + 2.25, yd - H / 2 + 0.2, 0.5, H / 2 - 0.4, "bone", z=5.2, rr=0.15)   # pedicle from caudal half (upper half of each vertebra)
    rect(X, yd - 0.12, 2.2, 0.24, "channel", z=6, rr=0.08)
for k in range(3):
    yt = ys[k]
    rect(X + 3.1, yt - H + 0.1, 1.4, H - 0.2, "muscle")
    bio.label(ax, (X + 3.8, yt - H / 2), "muscle", size="tiny", rotation=90, color=P.on_fill())
    ax.plot([X + 2.2, X + 5.4], [yt - H / 4, yt - H / 4], color=P.edge("neuron"), lw=1.8, zorder=7)
bio.label(ax, (X + 2.5, 11.6), "Vertebrae after resegmentation", size="small", bold=True)
bio.callout(ax, (X + 1.1, ys[0] - H / 2), (X + 5.9, ys[0] - 0.9), "Disc")
bio.callout(ax, (X + 1.1, ys[1] - H / 2 - 0.9), (X + 6.0, ys[1] - 0.6), "Vertebral body")
bio.callout(ax, (X + 2.5, ys[1] - 0.75 * H), (X + 6.0, ys[1] - 2.2), "Pedicle")
bio.label(ax, (0.6, 0.3), "light: from rostral halves; dark: from caudal halves", size="tiny", ha="left", color=P.muted())
