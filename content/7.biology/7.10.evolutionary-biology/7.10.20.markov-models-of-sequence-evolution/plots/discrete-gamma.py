"""Gamma rate variation among sites and its discretization. A: densities of the gamma distribution with
mean 1 (shape alpha, rate alpha) for several alpha; small alpha gives an L-shaped distribution with most
sites nearly invariant. B: the discrete gamma with K = 4 equiprobable categories for alpha = 0.5: the
category boundaries are the quartiles (vertical lines) and each category is represented by its mean rate
(dots; values in the panel). C: the probability that two sequences differ at a site against the distance d under
JC69 with one rate, with continuous gamma rates (alpha = 0.5) and with the 4-category discrete gamma; the
discrete approximation is close to the continuous model."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma
from scipy.special import gammainc
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

fig, (a, b, c) = plt.subplots(1, 3, figsize=(12.0, 3.8))
fig.subplots_adjust(left=0.06, right=0.985, bottom=0.16, top=0.9, wspace=0.3)
r = np.linspace(1e-3, 3, 500)
for al, tok in ((0.2, "negative"), (0.5, "rna"), (1.0, "dna"), (2.0, "enzyme"), (10.0, "plant")):
    a.plot(r, gamma.pdf(r, al, scale=1 / al), color=charts.line(tok), lw=1.5, label=f"$\\alpha = {al:g}$")
a.set_ylim(0, 2.2)
a.set_xlim(0, 3)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(a, "relative rate $r$", "density $g(r)$")
charts.title(a, "A  Gamma distributions with mean 1")

al, K = 0.5, 4
cuts = gamma.ppf(np.arange(1, K) / K, al, scale=1 / al)
edges = np.concatenate([[0], cuts, [np.inf]])
cdf1 = gammainc(al + 1, edges * al)
means = K * np.diff(cdf1)
rr = np.linspace(1e-3, 4, 600)
b.plot(rr, gamma.pdf(rr, al, scale=1 / al), color=charts.line("rna"), lw=1.5)
shades = ("dna", "enzyme", "plant", "rna")
for k in range(K):
    lo, hi = edges[k], min(edges[k + 1], 4)
    m = (rr >= lo) & (rr <= hi)
    b.fill_between(rr[m], 0, gamma.pdf(rr[m], al, scale=1 / al), color=P.fill(shades[k]), alpha=0.5, lw=0)
    b.plot([means[k]], [0.08], "o", ms=5, color=charts.line(shades[k]), zorder=5)
b.text(1.6, 1.2, "category means\n" + ", ".join(f"{m:.3f}" for m in means), fontsize=FT["tiny"],
       color=P.ink())
for x0 in cuts:
    b.axvline(x0, color=P.muted(), lw=0.7, ls=":")
b.set_ylim(0, 1.6)
b.set_xlim(0, 4)
charts.style_axes(b, "relative rate $r$", "density")
charts.title(b, "B  Discrete gamma, $\\alpha = 0.5$, $K = 4$")

d = np.linspace(0, 4, 400)
c.plot(d, 0.75 - 0.75 * np.exp(-4 * d / 3), color=P.muted(), lw=1.2, ls="--", label="one rate (JC69)")
c.plot(d, 0.75 - 0.75 * (1 + 4 * d / (3 * al)) ** (-al), color=charts.line("rna"), lw=1.6,
       label="continuous gamma")
disc = 0.75 - 0.75 * np.mean(np.exp(-4 * np.outer(d, means) / 3), axis=1)
c.plot(d[::12], disc[::12], "o", ms=3.2, color=charts.line("dna"), label="discrete gamma, $K = 4$")
c.axhline(0.75, color=P.muted(), lw=0.5, ls=":")
c.set_ylim(0, 0.8)
c.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(c, "distance $d$", "probability of a difference $p$")
charts.title(c, "C  Rate variation slows saturation")
