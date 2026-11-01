# Scores of optimal local alignments of unrelated proteins. 4000 pairs of random sequences of 300 residues
# (Robinson-Robinson background frequencies) were aligned with BLOSUM62, once with affine gaps (11 + k) and
# once without gaps (random-scores.csv, computed with Biopython's PairwiseAligner). A: histograms with
# maximum-likelihood Gumbel fits. B: the empirical tail probability P(S >= x) on a log scale is linear in x
# with slope -lambda: the fits give lambda = 0.28 (gapped) and 0.32 (ungapped), against the asymptotic values
# 0.267 and 0.3176 used by BLAST. C: the mean gapped score grows linearly in ln(mn) with slope close to
# 1/lambda (600 pairs per length; dashed line slope 1/0.267).
import numpy as np
from scipy import stats
import wikibio as bio
from wikibio import charts as C

P = bio.P
d = np.genfromtxt("random-scores.csv", delimiter=",", names=True)
fig, ax = bio.canvas(30.0, 9.6)
a = C.axes_at(ax, (1.8, 1.5, 7.6, 6.8))
b = C.axes_at(ax, (11.6, 1.5, 7.6, 6.8))
c = C.axes_at(ax, (21.6, 1.5, 7.6, 6.8))
for col, tok, lab in [("gapped", "protein", "gapped (11 + k)"), ("ungapped", "dna", "ungapped")]:
    v = d[col]
    u, beta = stats.gumbel_r.fit(v)
    bins = np.arange(v.min() - 0.5, v.max() + 1.5, 1)
    a.hist(v, bins=bins, density=True, histtype="step", color=C.line(tok), lw=1.0)
    xs = np.linspace(15, 60, 300)
    a.plot(xs, stats.gumbel_r.pdf(xs, u, beta), color=C.line(tok), lw=1.6, label=f"{lab}: lambda = {1 / beta:.2f}")
    xx = np.unique(v)
    surv = np.array([(v >= x).mean() for x in xx])
    b.semilogy(xx, surv, "o", ms=2.5, color=C.line(tok))
    b.semilogy(xs, stats.gumbel_r.sf(xs, u, beta), color=C.line(tok), lw=1.2)
a.set_xlim(15, 60)
C.style_axes(a, "optimal local score S", "density")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink())
b.set_xlim(15, 65)
b.set_ylim(1e-4, 1.5)
C.style_axes(b, "score x", "P(S >= x)")
L = np.array([100, 200, 400, 800])
means = np.array([23.54, 28.90, 33.99, 39.46])
lnmn = np.log(L * L)
c.plot(lnmn, means, "o", color=C.line("protein"), ms=5)
xl = np.linspace(9, 13.6, 10)
c.plot(xl, means.mean() + (xl - lnmn.mean()) / 0.267, color=P.muted(), lw=0.9, ls=(0, (3, 2)))
for Li, xv, yv in zip(L, lnmn, means):
    c.text(xv + 0.1, yv - 1.4, f"{Li} x {Li}", fontsize=bio.core.FONT["tiny"], color=P.ink())
C.style_axes(c, "ln(mn)", "mean optimal score")
bio.panel(ax, "A", (0.2, 9.3))
bio.panel(ax, "B", (10.2, 9.3))
bio.panel(ax, "C", (20.2, 9.3))
