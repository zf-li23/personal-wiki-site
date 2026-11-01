# Posterior genotype of a diploid site from read counts (Formula 12.2.1): every base has error
# probability 0.001, and the prior is 1 - 1.5 theta for the homozygous reference genotype, theta for the
# heterozygote and theta/2 for the homozygous alternative, with theta = 0.001. A: for each depth and number
# of alternative reads, the colour is the genotype of highest posterior probability and its shade the
# genotype quality GQ = -10 log10(1 - posterior of that genotype), capped at 99 as in VCF files. B: the
# posterior probability of the heterozygote against the alternative-allele fraction for depths 5, 10, 20
# and 40; at low depth the prior keeps a site with one or two alternative reads homozygous reference.
import numpy as np
import wikibio as bio
from wikibio import charts as C

EPS, THETA = 1e-3, 1e-3
PRIOR = np.log([1 - 1.5 * THETA, THETA, THETA / 2])
FRAC = np.array([0.0, 0.5, 1.0])


def posterior(n, a):
    pa = FRAC * (1 - EPS) + (1 - FRAC) * EPS / 3
    pr = FRAC * EPS / 3 + (1 - FRAC) * (1 - EPS)
    lp = (n - a) * np.log(pr) + a * np.log(pa) + PRIOR
    p = np.exp(lp - lp.max())
    return p / p.sum()


NMAX = 40
best = np.full((NMAX + 1, NMAX + 1), np.nan)
gq = np.full((NMAX + 1, NMAX + 1), np.nan)
for n in range(1, NMAX + 1):
    for a in range(n + 1):
        p = posterior(n, a)
        b = int(np.argmax(p))
        best[a, n] = b
        gq[a, n] = min(99.0, -10 * np.log10(max(1 - p[b], 1e-300)))

fig, ax = bio.canvas(24.0, 9.5)
a1 = C.axes_at(ax, (2.0, 1.5, 9.0, 7.0))
toks = ["dna", "highlight", "negative"]
names = ["0/0", "0/1", "1/1"]
img = np.ones((NMAX + 1, NMAX + 1, 3))
from matplotlib.colors import to_rgb
for b, tok in enumerate(toks):
    col = np.array(to_rgb(C.line(tok)))
    sel = best == b
    t = 0.35 + 0.65 * (gq[sel] / 99.0)[:, None]      # weight of the genotype colour against pale grey
    img[sel] = t * col + (1 - t) * 0.92
img[np.isnan(best)] = np.nan
a1.imshow(img, origin="lower", aspect="auto", extent=(0.5, NMAX + 0.5, -0.5, NMAX + 0.5), interpolation="nearest")
for b, (nm, tok) in enumerate(zip(names, toks)):
    a1.plot([], [], "s", ms=7, color=C.line(tok), label=f"best genotype {nm}")
a1.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=bio.P.ink(), loc="upper left")
C.style_axes(a1, "depth (reads)", "alternative reads", box=True)
C.title(a1, "A  Best genotype; paler = lower GQ")
a2 = C.axes_at(ax, (14.2, 1.5, 9.0, 7.0))
for n, tok in zip((5, 10, 20, 40), ("neutral", "rna", "dna", "positive")):
    k = np.arange(n + 1)
    a2.plot(k / n, [posterior(n, x)[1] for x in k], "o-", ms=3, lw=1.1, color=C.line(tok), label=f"depth {n}")
C.style_axes(a2, "alternative-allele fraction", "P(heterozygous | reads)")
a2.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=bio.P.ink())
C.title(a2, "B  Posterior of the heterozygote")
for n, x in ((10, 4), (20, 2), (4, 1)):
    print(n, x, np.round(posterior(n, x), 4))
