"""Publication bias in a funnel plot (simulation, seed 0). 120 two-arm trials of a treatment with a modest
benefit (true log odds ratio -0.15, odds ratio 0.86) have between 20 and 800 patients per arm (event risk
0.2); the standard error of each log odds ratio follows from its size. Trials with a significant benefit
(z < -1.96) are always published, the others with probability 0.2.

A: all 120 trials, with the pseudo 95 % limits around the true value. B: the published trials only: small
trials without a benefit are missing from the lower right, the funnel is asymmetric and the fixed-effect
estimate exaggerates the benefit; Egger's regression test has little power to show it.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
k = 120
mu = -0.15
n = np.exp(rng.uniform(np.log(20), np.log(800), k)).round()
p0 = 0.2
se = np.sqrt(2 / (n * p0 * (1 - p0)))
y = rng.normal(mu, se)
pub = (y / se < -1.96) | (rng.random(k) < 0.2)


def fe(y, s):
    w = 1 / s**2
    m = (w * y).sum() / w.sum()
    return m, 1 / np.sqrt(w.sum())


def egger(y, s):
    r = stats.linregress(1 / s, y / s)
    t = r.intercept / r.intercept_stderr
    return r.intercept, 2 * stats.t.sf(abs(t), len(y) - 2)


fig, axs = plt.subplots(1, 2, figsize=(10, 3.8), sharey=True)
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.87, wspace=0.12)
ss = np.linspace(0, se.max() * 1.05, 50)
for ax, mask, title in [(axs[0], np.ones(k, bool), "A  All 120 trials"), (axs[1], pub, f"B  The {pub.sum()} published trials")]:
    ax.plot(mu - 1.96 * ss, ss, color=P.muted(), lw=0.8, ls="--")
    ax.plot(mu + 1.96 * ss, ss, color=P.muted(), lw=0.8, ls="--")
    if ax is axs[1]:
        ax.plot(y[~pub], se[~pub], "o", ms=4, mfc="none", mec=P.fill("neutral"), mew=0.8, label="unpublished")
    ax.plot(y[mask], se[mask], "o", ms=4, color=P.fill("dna"), mec=charts.line("dna"), mew=0.6, label="published" if ax is axs[1] else None)
    m, s = fe(y[mask], se[mask])
    b0, pe = egger(y[mask], se[mask])
    ax.axvline(0, color=P.muted(), lw=0.6, ls=":")
    ax.axvline(mu, color=P.ink(), lw=0.8)
    ax.axvline(m, color=charts.line("rna"), lw=1.5, label=f"fixed effect {m:.3f} (OR {np.exp(m):.2f})")
    ax.text(0.98, 0.04, f"Egger intercept {b0:.2f}, p = {pe:.2g}", ha="right", transform=ax.transAxes, fontsize=FT["tiny"], color=P.ink())
    ax.set_xlim(-2.2, 1.9)
    ax.set_ylim(se.max() * 1.05, 0)
    ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
    charts.style_axes(ax, "log odds ratio", "standard error" if ax is axs[0] else None)
    charts.title(ax, title)
