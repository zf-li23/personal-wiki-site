# Dot plots of a random 300-nt sequence x against a rearranged copy y. y is built from x by a tandem
# duplication of x[40:60], an inversion (reverse complement) of x[120:180], a deletion of x[210:240]
# and 3 % point substitutions. A: every single-base identity (window 1): a quarter of all cells are dots
# and the structure is buried in noise. B: windows of 11 bases with at most one mismatch, forward
# matches in blue and reverse-complement matches in orange: the main diagonal, its repeated segment,
# the inverted segment on an anti-diagonal and the jump caused by the deletion become visible.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
rng = np.random.default_rng(0)
x = rng.choice(list("ACGT"), 300)
comp = {"A": "T", "C": "G", "G": "C", "T": "A"}


def revcomp(s):
    return np.array([comp[c] for c in s[::-1]])


y = np.concatenate([x[:60], x[40:60], x[60:120], revcomp(x[120:180]), x[180:210], x[240:300]])
mut = rng.random(len(y)) < 0.03
y[mut] = [rng.choice([b for b in "ACGT" if b != c]) for c in y[mut]]


def windowed(a, b, w, k):
    eq = (a[:, None] == b[None, :]).astype(int)
    n1, n2 = eq.shape[0] - w + 1, eq.shape[1] - w + 1
    cnt = sum(eq[t:t + n1, t:t + n2] for t in range(w))
    return np.argwhere(w - cnt <= k)


fig, ax = bio.canvas(24.0, 11.6)
pa = C.axes_at(ax, (1.9, 1.5, 9.0, 9.0))
pb = C.axes_at(ax, (14.2, 1.5, 9.0, 9.0))
one = windowed(x, y, 1, 0)
pa.scatter(one[:, 0], one[:, 1], s=0.9, color=C.line("dna"), linewidths=0)
w = 11
fwd = windowed(x, y, w, 1)
rev = windowed(x, revcomp(y), w, 1)
pb.scatter(fwd[:, 0] + w / 2, fwd[:, 1] + w / 2, s=1.2, color=C.line("dna"), linewidths=0, label="forward")
ny = len(y)
pb.scatter(rev[:, 0] + w / 2, ny - rev[:, 1] - w / 2, s=1.2, color=C.line("rna"), linewidths=0, label="reverse complement")
for p in (pa, pb):
    p.set_xlim(0, len(x))
    p.set_ylim(0, ny)
    C.style_axes(p, "position in x (nt)", "position in y (nt)", box=True)
C.title(pa, "window 1, exact")
C.title(pb, "window 11, at most 1 mismatch")
fs = bio.core.FONT["tiny"]
notes = [((50, 70), (95, 30), "tandem\nduplication"), ((140, 180), (85, 200), "inversion"),
         ((222, 229), (262, 175), "deletion")]
for xy, txt_xy, txt in notes:
    pb.annotate(txt, xy=xy, xytext=txt_xy, fontsize=fs, color=P.ink(), ha="center",
                arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
pb.legend(fontsize=fs, frameon=False, labelcolor=P.ink(), loc="upper left", markerscale=4)
bio.panel(ax, "A", (0.2, 11.2))
bio.panel(ax, "B", (12.5, 11.2))
