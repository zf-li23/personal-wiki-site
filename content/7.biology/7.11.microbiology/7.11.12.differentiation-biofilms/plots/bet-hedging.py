"""Cohen's (1966) model of germination in a randomly varying environment, read as a model of spore
germination. A fraction G of the dormant propagules germinates each year. In a good year (probability p)
a germinated propagule yields Y new ones; in a bad year it yields nothing. Ungerminated propagules
survive the year with probability S. The population then multiplies each year by
w = S (1 - G) + Y G in a good year and by w = S (1 - G) in a bad year, and the long-run growth rate is
the arithmetic mean of ln w, that is Lambda(G) = p ln[S(1-G) + YG] + (1-p) ln[S(1-G)].
A: Lambda against G for several p (S = 0.9, Y = 10); dots mark the optima. Germinating everything
(G = 1) is lethal whenever a bad year is possible, because ln 0 = -infinity.
B: the optimal fraction G* against p for three yields Y (S = 0.9); the dotted line is the rule G* = p,
the limit of perfect dormancy and large yield, in which the optimal germination fraction is simply the
probability of a good year. A small yield makes germination less worthwhile and lowers G*.
C: 200 years of one simulated environment (p = 0.6): the population size of the optimal hedger, of a
genotype that germinates everything and of one that germinates a tenth as often as the optimum."""

import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
Y, S = 10.0, 0.9


def Lam(G, p, S=S, Y=Y):
    G = np.clip(G, 0, 1)
    good = S * (1 - G) + Y * G
    bad = S * (1 - G)
    with np.errstate(divide="ignore"):
        return p * np.log(good) + (1 - p) * np.log(np.maximum(bad, 1e-300))


fig, ax = bio.canvas(27.0, 9.0)
G = np.linspace(0, 0.999, 2000)

bio.panel(ax, "A", (0.2, 8.9))
pax = charts.axes_at(ax, (1.8, 1.8, 6.6, 6.0))
for p, ls in ((0.3, ":"), (0.6, "--"), (0.9, "-")):
    L = Lam(G, p)
    pax.plot(G, L, color=charts.line("plant" if p > 0.5 else "dna"), lw=1.8, ls=ls, label=f"p = {p}")
    k = np.argmax(L)
    pax.plot([G[k]], [L[k]], "o", ms=4, color=charts.line("negative"))
pax.set_xlim(0, 1)
pax.set_ylim(-2.5, 2.2)
pax.axhline(0, color=P.muted(), lw=0.8, ls=":")
pax.legend(fontsize=6.8, frameon=False, loc="lower left")
charts.style_axes(pax, "germination fraction G", "long-run growth rate Λ per year")
charts.title(pax, "Λ(G) for three probabilities of a good year")

bio.panel(ax, "B", (9.4, 8.9))
bax = charts.axes_at(ax, (11.0, 1.8, 6.0, 6.0))
ps = np.linspace(0.01, 1.0, 200)
for yy, ls, tok in ((100.0, "-", "dna"), (10.0, "--", "plant"), (3.0, "-.", "highlight")):
    opt = [G[np.argmax(Lam(G, p, Y=yy))] for p in ps]
    bax.plot(ps, opt, color=charts.line(tok), lw=1.8, ls=ls, label=f"Y = {yy:g}")
bax.plot(ps, ps, color=P.muted(), lw=1.0, ls=":")
bax.set_xlim(0, 1)
bax.set_ylim(0, 1.05)
bax.legend(fontsize=6.8, frameon=False, loc="upper left")
charts.style_axes(bax, "probability p of a good year", "optimal fraction G*")
charts.title(bax, "The optimum hedges")

bio.panel(ax, "C", (18.2, 8.9))
cax = charts.axes_at(ax, (19.8, 1.8, 6.2, 6.0))
p = 0.6
rng = np.random.default_rng(0)
good = rng.random(200) < p
Gopt = G[np.argmax(Lam(G, p))]
for g, tok, ls, name in ((Gopt, "plant", "-", f"optimal G = {Gopt:.2f}"), (1.0, "negative", "--", "G = 1 (extinct in year 1)"),
                         (Gopt / 10, "dna", ":", f"G = {Gopt/10:.3f}")):
    n = np.ones(201)
    for k, gd in enumerate(good):
        w = S * (1 - g) + (Y * g if gd else 0.0)
        n[k + 1] = n[k] * max(w, 1e-300)
    cax.plot(np.arange(201), np.maximum(n, 1e-20), color=charts.line(tok), lw=1.8, ls=ls, label=name)
cax.set_yscale("log")
cax.set_xlim(0, 200)
cax.set_ylim(1e-12, 1e30)
cax.legend(fontsize=6.6, frameon=False, loc="lower right")
charts.style_axes(cax, "year", "population size (relative)")
charts.title(cax, "One run of the environment (p = 0.6)")
