"""Territoriality, site-dependent regulation and the buffer effect (simulated parameters).

Two habitats offer 30 territories of good quality (mean 1.6 young per territory holder) and 70 of poor
quality (0.6 young); individuals settle preemptively, best territories first; birds that find no
territory become non-breeding floaters. Adult survival 0.5, juvenile survival 0.5. A: per capita
recruitment of the whole population against its size: although no individual suffers from crowding on
its territory, mean reproduction declines with N because additional birds occupy poorer sites and then
become floaters (site-dependent regulation; Rodenhouse et al. 1997); recruitment balances adult
mortality at N = 75, with all good and 45 poor territories occupied. B: 80 years with year-to-year
variation in breeding success (lognormal, sd 0.35, seed 3): the number of birds in good habitat stays
almost constant, the number in poor habitat fluctuates, and floaters absorb the excess (the buffer
effect; Kluyver and Tinbergen 1953; Brown 1969).
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 12.0)
G, Pn, fg, fp, sa, sj = 30, 70, 1.6, 0.6, 0.5, 0.5


def split(n):
    good = min(n, G)
    poor = min(max(n - G, 0), Pn)
    return good, poor, max(n - G - Pn, 0)


pa = C.axes_at(ax, (2.4, 1.8, 11.0, 8.6))
Ns = np.arange(1, 181)
rec = []
for n in Ns:
    g, p, fl = split(n)
    rec.append(sj * (g * fg + p * fp) / n)
pa.plot(Ns, rec, color=Q.line_color("dna"), lw=1.8)
pa.axhline(1 - sa, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pa.text(178, 1 - sa + 0.015, "replacement (= adult mortality)", fontsize=FS["tiny"], color=P.muted(), ha="right")
pa.axvline(G, color=P.muted(), lw=0.6)
pa.axvline(G + Pn, color=P.muted(), lw=0.6)
pa.text(G / 2, 0.85, "good\nsites", fontsize=FS["tiny"], color=P.ink(), ha="center")
pa.text(G + Pn / 2, 0.85, "poor sites", fontsize=FS["tiny"], color=P.ink(), ha="center")
pa.text(G + Pn + 40, 0.85, "floaters", fontsize=FS["tiny"], color=P.ink(), ha="center")
pa.set_xlim(0, 180)
pa.set_ylim(0, 0.95)
C.style_axes(pa, "population size N (adults)", "recruits per adult")
bio.panel(ax, "A", (0.4, 11.6))
bio.label(ax, (2.4, 11.2), "Site-dependent regulation", size="small", bold=True, ha="left")

rng = np.random.default_rng(3)
n = 40.0
years = 80
H = []
for t in range(years):
    g, p, fl = split(int(round(n)))
    H.append((g, p, fl))
    e = np.exp(0.35 * rng.standard_normal() - 0.06)
    n = sa * n + sj * e * (g * fg + p * fp)
H = np.array(H)
pb = C.axes_at(ax, (17.0, 1.8, 11.5, 8.6))
t = np.arange(years)
pb.plot(t, H[:, 0], color=Q.line_color("positive"), lw=1.6, label="in good habitat")
pb.plot(t, H[:, 1], color=Q.line_color("rna"), lw=1.6, label="in poor habitat")
pb.plot(t, H[:, 2], color=P.muted(), lw=1.0, ls=(0, (3, 2)), label="floaters")
pb.set_xlim(0, years - 1)
pb.set_ylim(0, None)
C.style_axes(pb, "year", "number of adults")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left", ncol=3)
bio.panel(ax, "B", (15.0, 11.6))
bio.label(ax, (17.0, 11.2), "The buffer effect", size="small", bold=True, ha="left")
