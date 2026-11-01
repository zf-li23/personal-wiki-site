# Seeds and extensions of BLASTP on a real pair: residues 356-475 of human MCM6 (horizontal) against
# residues 535-654 of yeast Mcm6 (vertical), the region containing the Walker A motif GDPSTAKSQ. A: every
# pair of 3-residue words scoring at least T = 11 with BLOSUM62 is a hit (dots); hits on the same diagonal
# within A = 40 positions form two-hit pairs (ringed), which trigger an ungapped extension (shaded line).
# B: running scores of the ungapped extension to the right from the first two-hit pair on the homologous
# diagonal (top, which runs to the end of the segment) and from a chance two-hit pair (bottom), which stops
# when the score falls more than X = 16 below its maximum (X-drop).
import numpy as np
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
ix = {a: i for i, a in enumerate(AA)}
x = "PTIHGNDEVKRGVLLMLFGGVPKTTGEGTSLRGDINVCIVGDPSTAKSQFLKHVEEFSPRAVYTSGKASSAAGLTAAVVRDEESHEFVIEAGALMLADNGVCCIDEFDKMDVRDQVAIHE"
y = "PAVFGHEAVKKGILLQMLGGVHKSTVEGIKLRGDINICVVGDPSTSKSQFLKYVVGFAPRSVYTSGKASSAAGLTAAVVRDEEGGDYTIEAGALMLADNGICCIDEFDKMDISDQVAIHE"
X0, Y0 = 356, 535
xi = np.array([ix[c] for c in x])
yi = np.array([ix[c] for c in y])
W, T, A, XD = 3, 11, 40, 16
pair = S[xi[:, None], yi[None, :]]
word = sum(pair[k:len(x) - W + 1 + k, k:len(y) - W + 1 + k] for k in range(W))
hits = np.argwhere(word >= T)
two = []
by_diag = {}
for i, j in hits:
    by_diag.setdefault(i - j, []).append(i)
for dg, lst in by_diag.items():
    lst = sorted(lst)
    for a_, b_ in zip(lst[:-1], lst[1:]):
        if W <= b_ - a_ <= A:
            two.append((a_, a_ - dg, b_, b_ - dg))
fig, ax = bio.canvas(24.0, 11.0)
a = C.axes_at(ax, (1.8, 1.4, 8.6, 8.6))
a.plot(hits[:, 0] + X0, hits[:, 1] + Y0, "o", ms=2.2, color=C.line("dna"), label=f"word hits (T = {T})")
for i1, j1, i2, j2 in two:
    a.plot([i1 + X0, i2 + X0], [j1 + Y0, j2 + Y0], "o", ms=5.5, mfc="none", mec=C.line("negative"), mew=0.9)
a.plot([], [], "o", ms=5.5, mfc="none", mec=C.line("negative"), label="two-hit pairs")
a.set_xlim(X0, X0 + len(x))
a.set_ylim(Y0, Y0 + len(y))
C.style_axes(a, "human MCM6 residue", "yeast Mcm6 residue", box=True)
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper left")


def extend(i1, j1):
    """Ungapped X-drop extension to the right from (i1, j1); returns running scores and the best."""
    run, best, best_k, scores, k = 0, 0, 0, [], 0
    while i1 + k < len(x) and j1 + k < len(y):
        run += S[xi[i1 + k], yi[j1 + k]]
        scores.append(run)
        if run > best:
            best, best_k = run, k
        if best - run > XD:
            break
        k += 1
    return np.array(scores), best, best_k


main = min(p for p in two if p[0] - p[1] == 0)
chance = min(p for p in two if p[0] - p[1] != 0)
panels = [(main, (13.6, 6.2, 9.6, 3.8), "two-hit pair on the homologous diagonal"),
          (chance, (13.6, 1.4, 9.6, 3.2), "chance two-hit pair")]
for (i1, j1, _, _), rect, title in panels:
    sc, best, bk = extend(i1, j1)
    a.plot([i1 + X0, i1 + bk + X0], [j1 + Y0, j1 + bk + Y0], color=C.line("protein"), lw=2.4, alpha=0.6)
    b = C.axes_at(ax, rect)
    pos = np.arange(len(sc)) + i1 + X0
    b.plot(pos, sc, color=C.line("protein"), lw=1.5)
    b.plot(pos[bk], best, "o", color=C.line("negative"), ms=4)
    stop = "end of segment" if len(sc) + i1 >= len(x) or len(sc) + j1 >= len(y) else f"drop > X = {XD}"
    b.set_title(f"{title}: maximum {best}, stop at {stop}", fontsize=bio.core.FONT["tiny"], color=P.ink(), loc="left")
    C.style_axes(b, "human MCM6 residue" if rect[1] < 2 else None, "running score")
bio.panel(ax, "A", (0.2, 10.7))
bio.panel(ax, "B", (12.0, 10.7))
