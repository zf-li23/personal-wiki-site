# Covariation in an alignment of transfer RNAs recovers the cloverleaf. Data: the seed alignment of the
# Rfam family RF00005 (tRNA, 954 sequences from all domains of life, Rfam is released into the public
# domain), restricted to its 71 consensus columns (trna-seed.csv). Sequences are weighted by 1 over the
# number of sequences at 62 % identity or more; the mutual information of every pair of columns is
# computed with a pseudocount, and the average product correction subtracts the part explained by the
# overall variability of each column. A: corrected mutual information (lower triangle) against the
# consensus secondary structure of the family (upper triangle, one color per stem). B: the 24 highest
# scoring pairs of columns, colored by whether they are pairs of the consensus structure.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FT = bio.core.FONT
rows = open("trna-seed.csv").read().split()
ss = rows[0].split(",", 1)[1]
A = np.array([list(r.split(",", 1)[1]) for r in rows[1:]])
N, L = A.shape
opens, closes = "(<", ")>"
stack = {c: [] for c in opens}
cons = []
for k, ch in enumerate(ss):
    if ch in opens:
        stack[ch].append(k)
    elif ch in closes:
        cons.append((stack[opens[closes.index(ch)]].pop(), k))
X = np.stack([(A == c) for c in "ACGU"], 2).astype(float)
ident = np.einsum("ika,jka->ij", X, X) / L
w = 1 / (ident >= 0.62).sum(1)
MI = np.zeros((L, L))
for i in range(L):
    fij = np.einsum("n,na,njb->jab", w, X[:, i], X) + 0.1 / 16
    fij /= fij.sum((1, 2), keepdims=True)
    fi, fj = fij.sum(2), fij.sum(1)
    MI[i] = (fij * np.log2(fij / (fi[:, :, None] * fj[:, None, :]))).sum((1, 2))
np.fill_diagonal(MI, 0)
MI = (MI + MI.T) / 2
mean = MI.sum(1) / (L - 1)
CMI = MI - np.outer(mean, mean) / (MI.sum() / (L * (L - 1)))
ranked = sorted(((i, j) for i in range(L) for j in range(i + 4, L)), key=lambda p: -CMI[p])
inpair = set(cons)
stems = (("acceptor", 0, 7, "dna"), ("D", 7, 11, "rna"), ("anticodon", 11, 16, "positive"), ("T", 16, 21, "enzyme"))
owner = {}
for name, a, b, tok in stems:
    for p in sorted(cons)[a:b]:
        owner[p] = tok

fig, ax = bio.canvas(27.0, 12.5)
a = C.axes_at(ax, (2.0, 1.3, 10.4, 10.4))
low = np.where(np.tril(np.ones((L, L), bool), -1) & (CMI > 0.05), CMI, np.nan)
im = a.imshow(low, cmap="Blues", vmin=0, vmax=1.2, extent=(0.5, L + 0.5, L + 0.5, 0.5), interpolation="nearest")
for (i, j), tok in owner.items():
    a.scatter(j + 1, i + 1, s=10, marker="s", color=C.line(tok))
a.plot([0.5, L + 0.5], [0.5, L + 0.5], color=P.muted(), lw=0.6)
C.style_axes(a, "alignment column", "alignment column", box=True)
a.text(L * 0.70, L * 0.14, "consensus structure", fontsize=FT["tiny"], color=P.ink(), ha="center")
a.text(L * 0.26, L * 0.90, "corrected mutual information", fontsize=FT["tiny"], color=P.ink(), ha="center")
cb = C.axes_at(ax, (12.8, 1.3, 0.3, 4.2))
fig.colorbar(im, cax=cb)
C.style_axes(cb, None, None, box=True)
cb.set_ylabel("bits", fontsize=FT["tiny"], color=P.ink())
for k, (name, _, _, tok) in enumerate(stems):
    ax.text(12.8, 11.3 - 0.55 * k, f"{name} stem", fontsize=FT["tiny"], color=C.line(tok))
b = C.axes_at(ax, (16.6, 1.3, 9.4, 10.4))
top = ranked[:24]
ys = np.arange(len(top))[::-1]
b.barh(ys, [CMI[p] for p in top], height=0.7,
       color=[C.line(owner[p]) if p in inpair else C.line("negative") for p in top])
b.set_yticks(ys)
b.set_yticklabels([f"{i + 1}–{j + 1}" for i, j in top], fontsize=FT["tiny"] * 0.95)
C.style_axes(b, "corrected mutual information (bits)", "pair of columns (rank 1 at the top)")
first_other = [k for k, p in enumerate(top) if p not in inpair][:1]
for k in first_other:
    b.text(CMI[top[k]] + 0.03, ys[k], "not a consensus pair", va="center", fontsize=FT["tiny"],
           color=C.line("negative"))
bio.panel(ax, "A", (0.2, 12.1))
bio.panel(ax, "B", (15.2, 12.1))
