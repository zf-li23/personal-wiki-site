"""Rarefaction and nonparametric richness estimators on simulated communities.

Community 1: 150 species with log-normal relative abundances (log-sd 1.5); community 2: 80 species with
log-normal abundances (log-sd 0.6), more even. Samples of individuals are multinomial draws.
A: expected rarefaction curves E[S_n] = sum_i [1 - C(N - N_i, n) / C(N, n)] (Hurlbert 1971) computed from
one sample of N = 1500 individuals of each community; dots mark the full samples (124 and 80 species). At n = 1500
community 1 shows more species, although the more even community 2 shows more below n of about 180: the curves cross.
B: community 1, mean over 40 replicate samples of size n: observed richness, the bias-corrected Chao1
estimator S_obs + (n - 1)/n F1 (F1 - 1) / (2 (F2 + 1)) and ACE (rare species: at most 10 individuals);
dashed: the true richness 150. Estimators approach the truth faster than S_obs but remain lower bounds
for small samples.
"""

import numpy as np
from scipy.special import gammaln

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(5)


def community(S, sd):
    a = np.exp(rng.normal(0, sd, S))
    return a / a.sum()


def rarefy(counts, ns):
    counts = counts[counts > 0]
    N = counts.sum()

    def lc(a, b):
        return gammaln(a + 1) - gammaln(b + 1) - gammaln(a - b + 1)
    out = []
    for n in ns:
        terms = np.where(N - counts >= n, np.exp(lc(N - counts, n) - lc(N, n)), 0.0)
        out.append((1 - terms).sum())
    return np.array(out)


def chao1(c):
    c = c[c > 0]
    n = c.sum()
    F1, F2 = (c == 1).sum(), (c == 2).sum()
    return len(c) + (n - 1) / n * F1 * (F1 - 1) / (2 * (F2 + 1))


def ace(c, k=10):
    c = c[c > 0]
    rare = c[c <= k]
    Sab = (c > k).sum()
    Sr, Nr = len(rare), rare.sum()
    F1 = (rare == 1).sum()
    if Nr == 0 or F1 == Nr:
        return len(c)
    Cc = 1 - F1 / Nr
    s = sum(i * (i - 1) * (rare == i).sum() for i in range(1, k + 1))
    g2 = max(Sr / Cc * s / (Nr * (Nr - 1)) - 1, 0)
    return Sab + Sr / Cc + F1 / Cc * g2


p1, p2 = community(150, 1.5), community(80, 0.6)
fig, ax = bio.canvas(30.0, 11.0)
pa = C.axes_at(ax, (2.0, 2.0, 11.0, 7.0))
for p, tok, lab in ((p1, "dna", "community 1 (150 species)"), (p2, "negative", "community 2 (80 species)")):
    c = rng.multinomial(1500, p)
    ns = np.unique(np.round(np.logspace(0, np.log10(1500), 60)).astype(int))
    pa.plot(ns, rarefy(c, ns), color=Q.line_color(tok), lw=1.8, label=lab)
    pa.plot([1500], [(c > 0).sum()], "o", color=Q.line_color(tok), ms=5)
pa.set_xlim(0, 1550)
pa.set_ylim(0, 160)
C.style_axes(pa, "individuals sampled, n", "expected species observed")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right")
bio.panel(ax, "A", (0.3, 10.7))
bio.label(ax, (2.0, 10.0), "Rarefaction curves", size="small", bold=True, ha="left")

sizes = np.array([50, 100, 200, 400, 800, 1600, 3200, 6400])
obs, ch, ac = [], [], []
for n in sizes:
    r = [rng.multinomial(n, p1) for _ in range(40)]
    obs.append(np.mean([(c > 0).sum() for c in r]))
    ch.append(np.mean([chao1(c) for c in r]))
    ac.append(np.mean([ace(c) for c in r]))
pb = C.axes_at(ax, (17.5, 2.0, 11.0, 7.0))
pb.semilogx(sizes, obs, "o-", color=Q.line_color("neutral"), lw=1.6, ms=4, label="observed S")
pb.semilogx(sizes, ch, "s-", color=Q.line_color("dna"), lw=1.6, ms=4, label="Chao1")
pb.semilogx(sizes, ac, "^-", color=Q.line_color("plant"), lw=1.6, ms=4, label="ACE")
pb.axhline(150, color=P.ink(), lw=1.0, ls=(0, (4, 2)))
pb.text(55, 153, "true richness", fontsize=FS["tiny"], color=P.ink())
pb.set_ylim(0, 175)
C.style_axes(pb, "sample size n (individuals)", "species richness")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right")
bio.panel(ax, "B", (15.8, 10.7))
bio.label(ax, (17.5, 10.0), "Estimators against sample size (community 1)", size="small", bold=True, ha="left")
