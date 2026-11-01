# Linear-space alignment (Hirschberg 1975) of two DNA sequences (match +1, mismatch -1, gap -2). A: the
# recursion. The middle row of each subproblem (dashed) is crossed by the optimal path at the column that
# maximizes forward score plus reverse score; the point found there (dot) splits the subproblem into an
# upper-left and a lower-right rectangle, whose outlines are drawn darker for earlier levels. The
# subproblems shrink to single rows, and the points chain into the optimal path (line), the same as a
# full Needleman-Wunsch traceback, computed while storing only two rows at a time. B: cells evaluated
# per level: about mn at the first level, mn/2 at the second, and so on, 2mn in total.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
rng = np.random.default_rng(4)
x = "".join(rng.choice(list("ACGT"), 30))
y = list(x[:8] + x[13:30])
for k in rng.choice(len(y), 3, replace=False):
    y[k] = "ACGT"[("ACGT".index(y[k]) + 1) % 4]
y = "".join(y[:18]) + "GTA" + "".join(y[18:])


def s(a, b):
    return 1 if a == b else -1


G = 2


def last_row(a, b):
    row = -G * np.arange(len(b) + 1, dtype=float)
    for i in range(1, len(a) + 1):
        new = np.empty_like(row)
        new[0] = -G * i
        for j in range(1, len(b) + 1):
            new[j] = max(row[j - 1] + s(a[i - 1], b[j - 1]), row[j] - G, new[j - 1] - G)
        row = new
    return row


rects, points, cells = [], [], {}


def hirschberg(i0, i1, j0, j1, depth):
    """Rows i0..i1 of x (vertical), columns j0..j1 of y; records subproblems and split points."""
    rects.append((i0, i1, j0, j1, depth))
    if i1 - i0 <= 1:
        return
    mid = (i0 + i1) // 2
    f = last_row(x[i0:mid], y[j0:j1])
    r = last_row(x[mid:i1][::-1], y[j0:j1][::-1])[::-1]
    cells[depth] = cells.get(depth, 0) + (i1 - i0) * (j1 - j0)
    jm = j0 + int(np.argmax(f + r))
    points.append((mid, jm, depth))
    hirschberg(i0, mid, j0, jm, depth + 1)
    hirschberg(mid, i1, jm, j1, depth + 1)


hirschberg(0, len(x), 0, len(y), 0)
fig, ax = bio.canvas(24.0, 12.0)
a = C.axes_at(ax, (1.6, 1.0, 10.0, 10.0))
for i0, i1, j0, j1, dep in rects:
    if dep <= 3:
        shade = [P.ink(), C.line("protein"), C.line("dna"), P.muted()][dep]
        a.add_patch(__import__("matplotlib.patches", fromlist=["x"]).Rectangle(
            (j0, i0), j1 - j0, i1 - i0, fill=False, edgecolor=shade, lw=1.6 - 0.35 * dep))
        if i1 - i0 > 1:
            a.plot([j0, j1], [(i0 + i1) // 2] * 2, color=shade, lw=0.6, ls=(0, (2, 2)))
pts = sorted([(0, 0)] + [(m, j) for m, j, _ in points] + [(len(x), len(y))])
a.plot([p[1] for p in pts], [p[0] for p in pts], color=C.line("negative"), lw=1.4)
a.plot([p[1] for p in pts], [p[0] for p in pts], "o", color=C.line("negative"), ms=3)
a.set_xlim(0, len(y))
a.set_ylim(len(x), 0)
C.style_axes(a, "position in y", "position in x", box=True)
b = C.axes_at(ax, (15.0, 1.6, 8.0, 8.6))
lv = sorted(cells)
b.bar(lv, [cells[k] for k in lv], color=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.8)
mn = len(x) * len(y)
b.plot(lv, [mn / 2 ** k for k in lv], "o--", color=C.line("negative"), ms=3, lw=0.8, label="mn / 2^level")
b.set_xticks(lv)
C.style_axes(b, "recursion level", "cells evaluated")
b.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink())
bio.panel(ax, "A", (0.2, 11.7))
bio.panel(ax, "B", (13.4, 11.7))
