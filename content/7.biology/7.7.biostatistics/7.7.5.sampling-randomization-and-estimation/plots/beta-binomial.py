"""Bayesian estimation of a response rate. A phase II trial observes 6 responses in 20 patients. A: with a
flat Beta(1, 1) prior the posterior is Beta(7, 15) (mean 0.318), essentially the scaled likelihood.
B: with an informative Beta(2, 8) prior (mean 0.2, worth 10 earlier patients) the posterior Beta(8, 22) is
pulled towards 0.2. Shaded: 95 % equal-tailed credible intervals. Illustrative numbers.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT
x, n = 6, 20
p = np.linspace(0, 1, 500)
lik = stats.binom.pmf(x, n, p)
lik = lik / np.trapezoid(lik, p)

fig, axs = plt.subplots(1, 2, figsize=(10.0, 3.4), sharey=True)
fig.subplots_adjust(left=0.07, right=0.99, bottom=0.16, top=0.87, wspace=0.08)
for ax, (a0, b0), name in [(axs[0], (1, 1), "A  Flat prior Beta(1, 1)"), (axs[1], (2, 8), "B  Informative prior Beta(2, 8)")]:
    prior = stats.beta(a0, b0)
    post = stats.beta(a0 + x, b0 + n - x)
    ax.plot(p, prior.pdf(p), color=charts.line("neutral"), lw=1.4, ls="--", label="prior")
    ax.plot(p, lik, color=charts.line("dna"), lw=1.2, ls=":", label="likelihood (scaled)")
    ax.plot(p, post.pdf(p), color=charts.line("rna"), lw=1.8, label=f"posterior Beta({a0 + x}, {b0 + n - x})")
    lo, hi = post.ppf([0.025, 0.975])
    m = (p >= lo) & (p <= hi)
    ax.fill_between(p[m], post.pdf(p[m]), color=P.fill("rna"), alpha=0.35, lw=0)
    ax.text(0.55, 2.6, f"posterior mean {post.mean():.3f}\n95 % credible {lo:.3f} to {hi:.3f}\nP(p > 0.2) = {post.sf(0.2):.2f}",
            fontsize=FT["tiny"], color=P.ink())
    ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
    ax.set_xlim(0, 1)
    charts.style_axes(ax, "response rate p", "density" if ax is axs[0] else None)
    charts.title(ax, name)
