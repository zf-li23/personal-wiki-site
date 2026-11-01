# The neighborhood-word threshold T of BLASTP (words of W = 3 residues, BLOSUM62, Robinson-Robinson
# background frequencies), computed exactly by convolving the score distributions of single positions.
# A: the mean number of words in the neighborhood of a query word (words scoring at least T against it),
# the number of database words that produce a hit at one query position. B: for each T, the probability that
# an aligned word pair is a hit when the two sequences are unrelated (horizontal) and when they are related
# with the target frequencies of BLOSUM62, about 30 % identity (vertical). Lowering T raises the sensitivity
# per word of a true alignment, and the number of chance hits, in nearly fixed proportion; exact word
# matches (open circle) have the chance rate of T = 15 but a lower sensitivity.
import numpy as np
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts as C

P = bio.P
AA = "ARNDCQEGHILKMFPSTWYV"
BLOSUM62 = [
    "4 -1 -2 -2 0 -1 -1 0 -2 -1 -1 -1 -1 -2 -1 1 0 -3 -2 0",
    "-1 5 0 -2 -3 1 0 -2 0 -3 -2 2 -1 -3 -2 -1 -1 -3 -2 -3",
    "-2 0 6 1 -3 0 0 0 1 -3 -3 0 -2 -3 -2 1 0 -4 -2 -3",
    "-2 -2 1 6 -3 0 2 -1 -1 -3 -4 -1 -3 -3 -1 0 -1 -4 -3 -3",
    "0 -3 -3 -3 9 -3 -4 -3 -3 -1 -1 -3 -1 -2 -3 -1 -1 -2 -2 -1",
    "-1 1 0 0 -3 5 2 -2 0 -3 -2 1 0 -3 -1 0 -1 -2 -1 -2",
    "-1 0 0 2 -4 2 5 -2 0 -3 -3 1 -2 -3 -1 0 -1 -3 -2 -2",
    "0 -2 0 -1 -3 -2 -2 6 -2 -4 -4 -2 -3 -3 -2 0 -2 -2 -3 -3",
    "-2 0 1 -1 -3 0 0 -2 8 -3 -3 -1 -2 -1 -2 -1 -2 -2 2 -3",
    "-1 -3 -3 -3 -1 -3 -3 -4 -3 4 2 -3 1 0 -3 -2 -1 -3 -1 3",
    "-1 -2 -3 -4 -1 -2 -3 -4 -3 2 4 -2 2 0 -3 -2 -1 -2 -1 1",
    "-1 2 0 -1 -3 1 1 -2 -1 -3 -2 5 -1 -3 -1 0 -1 -3 -2 -2",
    "-1 -1 -2 -3 -1 0 -2 -3 -2 1 2 -1 5 0 -2 -1 -1 -1 -1 1",
    "-2 -3 -3 -3 -2 -3 -3 -3 -1 0 0 -3 0 6 -4 -2 -2 1 3 -1",
    "-1 -2 -2 -1 -3 -1 -1 -2 -2 -3 -3 -1 -2 -4 7 -1 -1 -4 -3 -2",
    "1 -1 1 0 -1 0 0 0 -1 -2 -2 0 -1 -2 -1 4 1 -3 -2 -2",
    "0 -1 0 -1 -1 -1 -1 -2 -2 -1 -1 -1 -1 -2 -1 1 5 -2 -2 0",
    "-3 -3 -4 -4 -2 -2 -3 -2 -2 -3 -2 -3 -1 1 -4 -3 -2 11 2 -3",
    "-2 -2 -2 -3 -2 -1 -2 -3 2 -1 -1 -2 -1 3 -3 -2 -2 2 7 -1",
    "0 -3 -3 -3 -1 -2 -2 -3 -3 3 1 -2 1 -1 -2 -2 0 -3 -1 4",
]
S = np.array([[int(v) for v in r.split()] for r in BLOSUM62])
rob = dict(A=0.07805, R=0.05129, N=0.04487, D=0.05364, C=0.01925, Q=0.04264, E=0.06295, G=0.07377, H=0.02199,
           I=0.05142, L=0.09019, K=0.05744, M=0.02243, F=0.03856, P=0.05203, S=0.07120, T=0.05841, W=0.01330,
           Y=0.03216, V=0.06441)
q = np.array([rob[a] for a in AA])
q = q / q.sum()
lam = brentq(lambda l: (np.outer(q, q) * np.exp(l * S)).sum() - 1, 0.01, 2)
target = np.outer(q, q) * np.exp(lam * S)
lo = int(S.min())


def word_dist(weights, W=3):
    """Distribution (index = score - W*lo) of the sum of W independent position scores."""
    one = np.zeros(int(S.max()) - lo + 1)
    np.add.at(one, (S - lo).ravel(), weights.ravel())
    out = np.array([1.0])
    for _ in range(W):
        out = np.convolve(out, one)
    return out


Ts = np.arange(8, 19)
fig, ax = bio.canvas(24.0, 9.6)
a = C.axes_at(ax, (2.0, 1.5, 9.0, 7.0))
for W, tok in [(2, "neutral"), (3, "protein"), (4, "dna")]:
    nb = word_dist(np.repeat(q[:, None], 20, axis=1), W)   # weight q over the query letter, 1 per word letter
    size = [nb[max(T - W * lo, 0):].sum() for T in Ts]
    a.semilogy(Ts, size, "o-", ms=3, lw=1.2, color=C.line(tok), label=f"W = {W}")
a.axvline(11, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
C.style_axes(a, "threshold T", "mean neighborhood size (words)")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink())
b = C.axes_at(ax, (14.6, 1.5, 9.0, 7.0))
bg, tg = word_dist(np.outer(q, q)), word_dist(target)
pb = [bg[T - 3 * lo:].sum() for T in Ts]
pt = [tg[T - 3 * lo:].sum() for T in Ts]
b.loglog(pb, pt, "o-", ms=3, lw=1.2, color=C.line("protein"))
for T, x_, y_ in zip(Ts, pb, pt):
    if T in (9, 11, 13, 15, 17):
        b.text(x_ * 1.15, y_ * 0.85, f"T = {T}", fontsize=bio.core.FONT["tiny"], color=P.ink())
ex_b, ex_t = (q ** 2).sum() ** 3, np.trace(target) ** 3
b.loglog([ex_b], [ex_t], "o", ms=5, mfc="none", mec=C.line("negative"))
b.text(ex_b * 1.2, ex_t * 0.8, "exact match", fontsize=bio.core.FONT["tiny"], color=C.line("negative"))
C.style_axes(b, "P(hit) per word pair, unrelated", "P(hit) per word pair, related")
bio.panel(ax, "A", (0.2, 9.3))
bio.panel(ax, "B", (12.9, 9.3))
