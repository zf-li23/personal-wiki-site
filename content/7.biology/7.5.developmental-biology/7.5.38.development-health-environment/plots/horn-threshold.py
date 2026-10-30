"""A threshold polyphenism: horns of male dung beetles (Onthophagus) as a sigmoid function of body size (Formula 38.8.1).

Body size X (pronotum width, mm) is normally distributed, mean 3.2, SD 0.35 (driven by larval food).
Horn length H = h0 + (h1 - h0) / (1 + exp(-(X - x0) / w)) with h0 = 0.05, h1 = 1.4 mm, x0 = 3.25 mm, w = 0.06 mm.
A: 2000 simulated males (seed 0) with small multiplicative noise in horn growth, and the sigmoid.
B: the distribution of horn length is bimodal although body size is unimodal (histogram of the sample; the
exact density without noise is f_H(h) = f_X(x(h)) |dx/dh|, which diverges at both plateaus). C: shifting the threshold x0 by 0.3 mm (a heritable
change, as between populations) changes the fraction of horned males from about 44 % to about 16 %.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
mu, sd = 3.2, 0.35
h0, h1, x0, w = 0.05, 1.4, 3.25, 0.06


def horn(x, x0=x0):
    return h0 + (h1 - h0) / (1 + np.exp(-(x - x0) / w))


X = rng.normal(mu, sd, 2000)
H = horn(X) * np.exp(rng.normal(0, 0.06, X.size))

fig, axs = plt.subplots(1, 3, figsize=(12.0, 3.6), gridspec_kw={"width_ratios": [1.2, 0.8, 1.0]})
fig.subplots_adjust(left=0.06, right=0.985, bottom=0.17, top=0.86, wspace=0.35)
a = axs[0]
a.plot(X, H, "o", ms=1.6, color=charts.line("animal"), alpha=0.45)
xs = np.linspace(2.0, 4.4, 300)
a.plot(xs, horn(xs), color=charts.line("drug"), lw=1.8)
a.axvline(x0, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
a.text(x0 + 0.04, 0.2, "threshold\nsize x0", fontsize=FT["tiny"], color=P.ink())
charts.style_axes(a, "body size X / mm", "horn length H / mm")
charts.title(a, "A  Horn allometry")

b = axs[1]
b.hist(H, bins=40, orientation="horizontal", density=True, color=P.light("animal"), edgecolor=P.edge("animal"), lw=0.4)
b.set_xlim(0, 9)
b.set_ylim(a.get_ylim())
charts.style_axes(b, "density", None)
charts.title(b, "B  Bimodal horns")

c = axs[2]
xx = np.linspace(1.8, 4.6, 300)
c.fill_between(xx, stats.norm.pdf(xx, mu, sd), color=P.fill("neutral"), alpha=0.35, lw=0)
c.plot(xx, stats.norm.pdf(xx, mu, sd), color=P.muted(), lw=1.0)
for th, tok in ((x0, "drug"), (x0 + 0.3, "dna")):
    frac = 1 - stats.norm.cdf(th, mu, sd)
    c.axvline(th, color=charts.line(tok), lw=1.4)
    left = tok == "drug"
    c.text(th - 0.05 if left else th + 0.05, 1.18 if left else 1.0, f"x0 = {th:.2f}:\n{100 * frac:.0f} % horned",
           fontsize=FT["tiny"], color=charts.line(tok), ha="right" if left else "left", va="top")
c.set_ylim(0, 1.25)
charts.style_axes(c, "body size X / mm", "density of body size")
charts.title(c, "C  Moving the threshold")
