"""What "95 % confidence" means. One hundred simulated samples of n = 20 birth weights from a normal
population with mean 2945 g and SD 729 g (the values of the birthwt data); for each sample the 95 % t
interval mean +/- t(19, 0.025) s / sqrt(20) is drawn as a horizontal line. Intervals that miss the true
mean (vertical line) are drawn in orange. Over many repetitions 95 % of the intervals cover the mean; any
single interval either covers it or does not. Simulated data, random seed 0.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
mu, sigma, n, reps = 2945.0, 729.0, 20, 100
x = rng.normal(mu, sigma, size=(reps, n))
m = x.mean(axis=1)
se = x.std(axis=1, ddof=1) / np.sqrt(n)
tq = stats.t.isf(0.025, n - 1)
lo, hi = m - tq * se, m + tq * se
miss = (lo > mu) | (hi < mu)

fig, ax = plt.subplots(figsize=(10.0, 3.6))
fig.subplots_adjust(left=0.07, right=0.99, bottom=0.15, top=0.90)
for i in range(reps):
    tok = "rna" if miss[i] else "dna"
    ax.plot([i, i], [lo[i], hi[i]], color=charts.line(tok), lw=1.6 if miss[i] else 1.0)
    ax.plot(i, m[i], "o", color=charts.line(tok), ms=2.2)
ax.axhline(mu, color=P.ink(), lw=0.9)
ax.text(reps + 0.5, mu, "true mean\n2945 g", va="center", fontsize=FT["tiny"], color=P.ink())
ax.text(1, hi.max() + 20, f"{miss.sum()} of {reps} intervals miss the true mean", fontsize=FT["tiny"], color=P.ink())
ax.set_xlim(-1, reps + 12)
charts.style_axes(ax, "simulated sample (n = 20 births each)", "95 % CI for mean birth weight (g)")
charts.title(ax, "One hundred 95 % confidence intervals")
