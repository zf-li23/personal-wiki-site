# Binning metagenomic contigs by composition and coverage (simulated). Six genomes contribute 40-120 contigs
# each (lengths log-normal, median 6 kb); a contig's GC content scatters around its genome's value with a
# standard deviation that shrinks with length, and its coverage around the genome's coverage in each of two
# samples. Genomes 4 and 5 have almost the same GC content and the same coverage in sample 1; they differ only
# in sample 2. Contigs (points sized by length) are coloured by the bin assigned by k-means (k = 6, best of 20
# starts) on GC content and log coverage in both samples, standardized. A: GC against coverage in sample 1,
# where genomes 4 and 5 overlap. B: coverage in the two samples, where they separate. The text gives the
# length-weighted purity of the bins, the fraction of each genome's length in its main bin, and the purity
# reached with GC content and sample 1 alone.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
rng = np.random.default_rng(0)
gen = [(0.38, 60, 30, 80), (0.50, 45, 50, 70), (0.51, 9, 12, 100), (0.64, 20, 5, 60), (0.635, 21, 45, 60),
       (0.45, 4, 6, 120)]                                 # GC, coverage in sample 1, in sample 2, contigs
gc, c1, c2, ln, lab = [], [], [], [], []
for g, (mu, a, b, k) in enumerate(gen):
    L = np.exp(rng.normal(np.log(6000), 0.8, k)).clip(1500, 2e5)
    gc.append(rng.normal(mu, 0.025 * np.sqrt(5000 / L)))
    c1.append(a * np.exp(rng.normal(0, 0.12, k)))
    c2.append(b * np.exp(rng.normal(0, 0.12, k)))
    ln.append(L)
    lab.append(np.full(k, g))
gc, c1, c2, ln, lab = map(np.concatenate, (gc, c1, c2, ln, lab))
X = np.c_[gc / 0.03, np.log2(c1) / 0.5, np.log2(c2) / 0.5]


def kmeans(X):
    best = None
    for s in range(20):
        r = np.random.default_rng(100 + s)
        cen = X[r.choice(len(X), 6, replace=False)]
        for _ in range(100):
            cl = ((X[:, None] - cen[None]) ** 2).sum(2).argmin(1)
            cen = np.array([X[cl == j].mean(0) if np.any(cl == j) else cen[j] for j in range(6)])
        inert = ((X - cen[cl]) ** 2).sum()
        if best is None or inert < best[0]:
            best = (inert, cl)
    return best[1]


def purity(cl):
    return sum(max(ln[(cl == j) & (lab == g)].sum() for g in range(6)) for j in range(6)) / ln.sum()


cl = kmeans(X)
pure, pure1 = purity(cl), purity(kmeans(X[:, :2]))
comp = [max(ln[(cl == j) & (lab == g)].sum() for j in range(6)) / ln[lab == g].sum() for g in range(6)]

fig, ax = bio.canvas(28.0, 10.6)
toks = ["dna", "rna", "enzyme", "protein", "receptor", "plant"]
a = C.axes_at(ax, (2.2, 1.6, 10.6, 7.8))
b = C.axes_at(ax, (16.4, 1.6, 10.6, 7.8))
for j in range(6):
    s = cl == j
    a.scatter(gc[s], c1[s], s=ln[s] / 1500, color=C.line(toks[j]), alpha=0.7, lw=0)
    b.scatter(c1[s], c2[s], s=ln[s] / 1500, color=C.line(toks[j]), alpha=0.7, lw=0)
a.set_yscale("log")
b.set_xscale("log")
b.set_yscale("log")
for g, (mu, c, d, _) in enumerate(gen):
    a.text(mu + (0.012 if g == 4 else -0.012 if g == 3 else 0), c * 1.6, f"{g + 1}",
           fontsize=bio.core.FONT["tiny"], color=P.ink(), ha="center")
    b.text(c * 1.35, d * 1.35, f"{g + 1}", fontsize=bio.core.FONT["tiny"], color=P.ink())
C.style_axes(a, "GC content of contig", "coverage in sample 1")
C.style_axes(b, "coverage in sample 1", "coverage in sample 2")
b.text(2.2, 110, f"bin purity {100 * pure:.1f} %\nlength in main bin, genomes 1-6:\n"
       + ", ".join(f"{100 * x:.0f}" for x in comp) + f" %\nGC and sample 1 only: purity {100 * pure1:.1f} %", fontsize=bio.core.FONT["tiny"], color=P.ink(), va="top")
b.set_xlim(1.5, 150)
b.set_ylim(2, 150)
bio.panel(ax, "A", (0.3, 10.2))
bio.panel(ax, "B", (14.6, 10.2))
