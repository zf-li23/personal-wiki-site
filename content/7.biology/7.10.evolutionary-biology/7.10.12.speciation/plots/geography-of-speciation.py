"""Geographic modes of speciation (schematic). Each column follows populations from top (past) to bottom
(present); colour shows genetic divergence. Allopatric: a barrier (grey) splits a widespread population and the
halves diverge in isolation. Peripatric: a small isolate founded at the edge of the range diverges rapidly.
Parapatric: neighbouring populations along an environmental gradient diverge while exchanging genes across a
narrowing hybrid zone. Sympatric: two forms arise within one interbreeding population without any spatial
separation. Double arrows mark gene flow."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle

import wikibio as bio

P = bio.P
FT = bio.core.FONT
fig, ax = bio.canvas(24, 11)
A, B, M = "dna", "rna", "neutral"


def ell(x, y, w, h, tok, alpha=None):
    ax.add_patch(Ellipse((x, y), w, h, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.2, zorder=5))


def flow(x0, x1, y):
    bio.arrow(ax, (x0, y), (x1, y), kind="process", head=0.14, color=P.muted())
    bio.arrow(ax, (x1, y), (x0, y), kind="process", head=0.14, color=P.muted())


rows = [8.6, 5.6, 2.6]
titles = ["Allopatric", "Peripatric", "Parapatric", "Sympatric"]
for k, title in enumerate(titles):
    cx = 3 + 6 * k
    bio.label(ax, (cx, 10.5), title, size="normal", bold=True)
    if k == 0:
        ell(cx, rows[0], 4.6, 1.6, M)
        for j, y in enumerate(rows[1:]):
            ax.add_patch(Rectangle((cx - 0.15, y - 1.0), 0.3, 2.0, facecolor=P.fill("neutral"), edgecolor=P.muted(), zorder=6))
            ell(cx - 1.35, y, 2.1, 1.5, M if j == 0 else A)
            ell(cx + 1.35, y, 2.1, 1.5, M if j == 0 else B)
        bio.label(ax, (cx, 4.35), "barrier", size="tiny", color=P.muted())
    elif k == 1:
        ell(cx - 0.4, rows[0], 4.0, 1.6, M)
        ell(cx - 0.4, rows[1], 4.0, 1.6, M)
        ell(cx + 2.1, rows[1] + 0.2, 0.8, 0.6, A)
        ell(cx - 0.4, rows[2], 4.0, 1.6, M)
        ell(cx + 2.1, rows[2] + 0.2, 1.4, 1.0, B)
        bio.label(ax, (cx + 2.1, rows[1] - 0.65), "founders", size="tiny", color=P.muted())
    elif k == 2:
        ell(cx, rows[0], 4.6, 1.6, M)
        ell(cx - 1.2, rows[1], 2.6, 1.6, A)
        ell(cx + 1.2, rows[1], 2.6, 1.6, B)
        ell(cx - 1.25, rows[2], 2.4, 1.6, A)
        ell(cx + 1.25, rows[2], 2.4, 1.6, B)
        flow(cx - 0.5, cx + 0.5, rows[1] - 1.1)
        bio.label(ax, (cx, rows[2] - 1.15), "hybrid zone", size="tiny", color=P.muted())
    else:
        ell(cx, rows[0], 4.6, 1.6, M)
        ell(cx, rows[1], 4.6, 1.6, M)
        rng = np.random.default_rng(1)
        for _ in range(22):
            px, py = rng.uniform(-1.9, 1.9), rng.uniform(-0.5, 0.5)
            if (px / 2.1) ** 2 + (py / 0.7) ** 2 < 1:
                tok = A if rng.random() < 0.5 else B
                ax.add_patch(Ellipse((cx + px, rows[2] + py), 0.28, 0.28, facecolor=P.fill(tok), edgecolor=P.edge(tok),
                                     lw=0.8, zorder=7))
        ax.add_patch(Ellipse((cx, rows[2]), 4.6, 1.6, facecolor="none", edgecolor=P.muted(), lw=1.2, zorder=6))
        bio.label(ax, (cx, rows[2] - 1.15), "one area, two forms", size="tiny", color=P.muted())
bio.arrow(ax, (0.4, 9.4), (0.4, 1.6), kind="process", head=0.2, color=P.muted())
bio.label(ax, (0.15, 5.5), "time", size="small", color=P.muted(), rotation=90)
