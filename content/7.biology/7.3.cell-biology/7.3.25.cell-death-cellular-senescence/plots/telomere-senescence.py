"""Telomere shortening counts divisions: a stochastic model of replicative senescence (Hayflick limit).

A human fibroblast has 92 telomeres (46 chromosomes, two ends each). Initial lengths are normally distributed
(mean L0, standard deviation 1.5 kb); at every division each telomere of each daughter shortens by a random
amount (mean 80 bp, sd 40 bp, never negative), from incomplete end replication and end processing. A cell
stops dividing permanently (replicative senescence) when its shortest telomere falls below Lc = 1.5 kb,
which is then recognized as a DNA break. Cells with telomerase (hTERT) keep their telomere length.
(A) One lineage: mean and shortest telomere versus division number; the shortest telomere, not the mean,
sets the limit. (B) Replicative lifespan of 2000 lineages from a young donor (L0 = 10 kb) and an old
donor (L0 = 7.5 kb). (C) Cumulative population doublings of a culture (2000 cells sampled at each
passage), with one division per day: the curve flattens as more cells senesce (the Hayflick plateau);
the longest-lived lineages take over, so the plateau lies above the median lifespan of B, whereas cells expressing hTERT grow indefinitely.
"""

import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
NT, SD0, LOSS, LSD, LC = 92, 1.5, 0.08, 0.04, 1.5
rng = np.random.default_rng(0)


def lineage(L0):
    tel = rng.normal(L0, SD0, NT)
    mean, low = [tel.mean()], [tel.min()]
    while tel.min() > LC:
        tel = tel - np.clip(rng.normal(LOSS, LSD, NT), 0, None)
        mean.append(tel.mean()); low.append(tel.min())
    return np.array(mean), np.array(low)


def lifespans(L0, n):
    tel = rng.normal(L0, SD0, (n, NT))
    k = np.zeros(n, int)
    alive = tel.min(axis=1) > LC
    while alive.any():
        tel[alive] -= np.clip(rng.normal(LOSS, LSD, (alive.sum(), NT)), 0, None)
        k[alive] += 1
        alive = tel.min(axis=1) > LC
    return k - 1


def culture(L0, days, tert=False, n=2000):
    tel = rng.normal(L0, SD0, (n, NT))
    pd = [0.0]
    for _ in range(days):
        div = np.ones(len(tel), bool) if tert else tel.min(axis=1) > LC
        kids = np.repeat(tel[div], 2, axis=0)
        if not tert:
            kids -= np.clip(rng.normal(LOSS, LSD, kids.shape), 0, None)
        new = np.vstack([tel[~div], kids])
        pd.append(pd[-1] + np.log2(len(new) / len(tel)))
        tel = new[rng.choice(len(new), size=min(n, len(new)), replace=False)]
    return np.array(pd)


fig, ax = bio.canvas(27.0, 9.0)
bio.panel(ax, "A", (0.2, 8.8))
A = charts.axes_at(ax, (1.8, 1.5, 6.8, 6.6))
m, lo = lineage(10.0)
k = np.arange(len(m))
A.plot(k, m, color=charts.line("dna"), lw=1.8, label="mean of 92 telomeres")
A.plot(k, lo, color=charts.line("negative"), lw=1.8, label="shortest telomere")
A.axhline(LC, color=P.muted(), ls="--", lw=0.8)
A.text(1, LC + 0.25, "critical length Lc", fontsize=FT["tiny"], color=P.muted())
A.annotate("senescence", (k[-1], lo[-1]), (k[-1] - 22, 3.6), fontsize=FT["tiny"], color=P.ink(),
           arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
A.set_ylim(0, 11)
A.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(A, "number of divisions", "telomere length / kb")

bio.panel(ax, "B", (10.0, 8.8))
B = charts.axes_at(ax, (11.6, 1.5, 6.0, 6.6))
bins = np.arange(0, 90, 2)
for L0, tok, name in ((10.0, "positive", "young donor (L0 = 10 kb)"), (7.5, "drug", "old donor (L0 = 7.5 kb)")):
    ls = lifespans(L0, 2000)
    B.hist(ls, bins=bins, color=P.fill(tok), ec=P.edge(tok), lw=0.5, alpha=0.9, label=f"{name}, median {int(np.median(ls))}")
B.set_ylim(0, 300)
B.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(B, "replicative lifespan (divisions)", "number of lineages")

bio.panel(ax, "C", (19.0, 8.8))
C = charts.axes_at(ax, (20.6, 1.5, 6.0, 6.6))
days = 90
t = np.arange(days + 1)
C.plot(t, culture(10.0, days), color=charts.line("positive"), lw=1.8, label="young donor")
C.plot(t, culture(7.5, days), color=charts.line("drug"), lw=1.8, label="old donor")
C.plot(t, culture(10.0, days, tert=True, n=200), color=charts.line("negative"), lw=1.8, ls="--", label="+ hTERT")
C.set_ylim(0, 95)
C.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(C, "time in culture / days", "cumulative population doublings")
