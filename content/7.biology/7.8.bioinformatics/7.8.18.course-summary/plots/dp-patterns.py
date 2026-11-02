# Five dependency patterns of the dynamic programs of the course. In each panel the target entry (filled)
# is computed from the entries its arrows come from, which have been computed before it.
# A: pairwise alignment (Needleman-Wunsch, Smith-Waterman, Gotoh): a cell from three neighbours, O(mn).
# B: hidden Markov models (Viterbi, forward, profile HMMs, Li-Stephens): a state at position i from all
#    states at i - 1, O(L K^2) in general.
# C: trees (Felsenstein pruning, Fitch, Sankoff): a vertex from its two children, in post-order.
# D: nested pairs (Zuker, CYK, inside): an interval [i, j] from a smaller interval inside it and from
#    splits [i, k] + [k + 1, j], O(n^3).
# E: colinear chaining of anchors: the best chain ending at an anchor from earlier compatible anchors.
import numpy as np
import wikibio as bio

P = bio.P
FT = bio.core.FONT
fig, ax = bio.canvas(37.5, 10.4)

def cell(x, y, s, tok=None, done=False):
    if tok is not None:
        fc = P.fill(tok)
    elif done:
        fc = P.mix(P.light("dna"), P.surface(), 0.55)
    else:
        fc = "none"
    ax.add_patch(bio.core.plt.Rectangle((x, y), s, s, facecolor=fc, edgecolor=P.muted(), lw=0.6, zorder=3))

def arr(a, b, tok="dna", rad=0.0):
    ax.annotate("", xy=b, xytext=a, zorder=6,
                arrowprops=dict(arrowstyle="-|>", color=P.edge(tok), lw=1.1, shrinkA=2, shrinkB=2,
                                mutation_scale=8, connectionstyle=f"arc3,rad={rad}"))

def caption(x, title, lines):
    bio.label(ax, (x, 9.7), title, size="small", bold=True)
    for k, t in enumerate(lines):
        bio.label(ax, (x, 1.25 - 0.55 * k), t, size="tiny", color=P.muted())

# A: alignment grid
s = 0.95
x0, y0 = 1.0, 2.6
for i in range(6):
    for j in range(6):
        cell(x0 + j * s, y0 + (5 - i) * s, s, done=(i < 3 or (i == 3 and j < 3)))
ti, tj = 3, 3
cell(x0 + tj * s, y0 + (5 - ti) * s, s, tok="highlight")
c = lambda i, j: (x0 + (j + 0.5) * s, y0 + (5 - i + 0.5) * s)
arr(c(2, 2), c(3, 3)); arr(c(2, 3), c(3, 3)); arr(c(3, 2), c(3, 3))
bio.label(ax, (x0 + 3 * s, y0 + 6 * s + 0.35), "sequence y", size="tiny")
bio.label(ax, (x0 - 0.4, y0 + 3 * s), "sequence x", size="tiny", rotation=90)
caption(x0 + 3 * s, "A  alignment", ["F(i, j) from 3 neighbours", "NW, SW, Gotoh: O(mn)"])

# B: HMM trellis
bx = 8.6
xs = [bx + 1.25 * k for k in range(5)]
ys = [7.2, 5.6, 4.0]
for k, x in enumerate(xs):
    for m, y in enumerate(ys):
        tok = "highlight" if (k == 3 and m == 1) else None
        fc = P.fill(tok) if tok else (P.mix(P.light("dna"), P.surface(), 0.55) if k < 3 else P.surface())
        ax.add_patch(bio.core.plt.Circle((x, y), 0.32, facecolor=fc, edgecolor=P.muted(), lw=0.7, zorder=4))
for m, y in enumerate(ys):
    arr((xs[2], y), (xs[3], ys[1]), tok="dna")
for k, x in enumerate(xs):
    bio.label(ax, (x, 3.1), f"{k + 1}", size="tiny", color=P.muted())
bio.label(ax, (xs[2], 2.55), "position i", size="tiny")
for m, (y, name) in enumerate(zip(ys, ["state 1", "state 2", "state 3"])):
    bio.label(ax, (bx - 0.95, y), name, size="tiny", color=P.muted(), ha="right")
caption(xs[2], "B  hidden Markov model", ["V(k, i) from all states at i - 1", "Viterbi, forward: O(LK²)"])

# C: tree in post-order
cx = 17.6
leaves = [(cx - 2.4, 3.6), (cx - 1.2, 3.6), (cx, 3.6), (cx + 1.2, 3.6), (cx + 2.4, 3.6)]
u = (cx - 1.8, 5.2)
v = (cx + 1.8, 5.2)
w = (cx - 0.9, 6.7)
r = (cx + 0.2, 8.1)
edges = [(u, leaves[0]), (u, leaves[1]), (w, u), (w, leaves[2]), (v, leaves[3]), (v, leaves[4]), (r, w), (r, v)]
for a, b in edges:
    ax.plot([a[0], b[0]], [a[1], b[1]], color=P.muted(), lw=0.9, zorder=2)
for p in leaves:
    ax.add_patch(bio.core.plt.Circle(p, 0.28, facecolor=P.mix(P.light("dna"), P.surface(), 0.55),
                                     edgecolor=P.muted(), lw=0.7, zorder=4))
for p, tok in ((u, None), (v, None), (w, "highlight"), (r, None)):
    fc = P.fill(tok) if tok else P.mix(P.light("dna"), P.surface(), 0.55) if p in (u, v) else P.surface()
    ax.add_patch(bio.core.plt.Circle(p, 0.3, facecolor=fc, edgecolor=P.muted(), lw=0.7, zorder=4))
arr(u, w); arr(leaves[2], w)
bio.label(ax, (cx, 2.85), "leaves: observed states", size="tiny", color=P.muted())
caption(cx, "C  tree", ["L_v(a) from the two children", "pruning O(ns²) per site; Fitch"])

# D: triangular interval table
dx, dy = 23.0, 2.6
n = 6
s = 0.95
for i in range(n):
    for j in range(i, n):
        done = (j - i) < 3
        cell(dx + j * s, dy + (n - 1 - i) * s, s, done=done)
ti, tj = 1, 4
cell(dx + tj * s, dy + (n - 1 - ti) * s, s, tok="highlight")
cc = lambda i, j: (dx + (j + 0.5) * s, dy + (n - 1 - i + 0.5) * s)
arr(cc(2, 3), cc(1, 4), tok="rna")
arr(cc(1, 2), cc(1, 4), tok="dna", rad=-0.35)
arr(cc(3, 4), cc(1, 4), tok="dna", rad=0.35)
bio.label(ax, (dx + 3 * s, dy + n * s + 0.35), "end j", size="tiny")
bio.label(ax, (dx - 0.4, dy + 3 * s), "start i", size="tiny", rotation=90)
caption(dx + 3 * s, "D  nested pairs", ["[i, j] from [i+1, j-1] and splits", "Zuker, CYK, inside: O(n³)"])

# E: chaining of anchors
ex = 34.2
pts = [(ex - 2.2, 3.4), (ex - 1.4, 4.4), (ex - 0.9, 5.3), (ex + 0.1, 4.0), (ex + 0.4, 6.3), (ex + 1.6, 7.4)]
for k, p in enumerate(pts):
    tok = "highlight" if k == 4 else None
    fc = P.fill(tok) if tok else P.mix(P.light("dna"), P.surface(), 0.55)
    ax.add_patch(bio.core.plt.Rectangle((p[0] - 0.28, p[1] - 0.12), 0.56, 0.24, facecolor=fc,
                                        edgecolor=P.muted(), lw=0.7, zorder=4))
for k in (0, 1, 2):
    arr(pts[k], pts[4], tok="dna", rad=-0.15)
ax.plot([ex - 2.8, ex + 2.4], [2.7, 2.7], color=P.muted(), lw=0.7)
ax.plot([ex - 2.8, ex - 2.8], [2.7, 8.2], color=P.muted(), lw=0.7)
bio.label(ax, (ex - 0.2, 2.25), "reference position", size="tiny")
bio.label(ax, (ex - 3.2, 5.4), "read position", size="tiny", rotation=90)
caption(ex - 0.2, "E  chaining", ["f(i) from earlier anchors", "minimap2: O(hN)"])
