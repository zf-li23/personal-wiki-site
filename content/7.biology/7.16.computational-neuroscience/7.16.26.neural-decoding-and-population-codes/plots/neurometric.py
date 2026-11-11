"""Neurometric and psychometric functions for random-dot motion (after Britten et al. 1992).

Model MT neuron: spike count in a 2 s trial, mean 40 + 0.5 c (preferred direction) or
40 - 0.25 c (null direction), c = motion coherence in percent; count variance = 1.5 x mean
(Fano factor 1.5, Gaussian approximation). Monkey: Weibull psychometric function
p = 1 - 0.5 exp(-(c/alpha)^beta), alpha = 10 %, beta = 1.3.
A: count distributions at 12.8 % coherence. B: ROC curves at four coherences.
C: neurometric function (area under the ROC curve from 300 trials per direction) with its
Weibull fit, against the psychometric function.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import rankdata

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
F = 1.5
cohs = np.array([0.8, 1.6, 3.2, 6.4, 12.8, 25.6, 51.2])


def counts(mean, n):
    return np.maximum(0, np.round(rng.normal(mean, np.sqrt(F * mean), n)))


def auc(a, b):
    """P(a > b) + 0.5 P(a == b), by ranks."""
    r = rankdata(np.concatenate([a, b]))
    return (r[:len(a)].sum() - len(a) * (len(a) + 1) / 2) / (len(a) * len(b))


def weib(c, alpha, beta):
    return 1 - 0.5 * np.exp(-(c / alpha) ** beta)


def roc(a, b):
    z = np.arange(0, 200)
    return np.array([(b >= t).mean() for t in z]), np.array([(a >= t).mean() for t in z])


fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.1))
ax = axs[0]
c = 12.8
a, b = counts(40 + 0.5 * c, 5000), counts(40 - 0.25 * c, 5000)
bins = np.arange(10, 90, 2)
ax.hist(b, bins=bins, color=P.fill("dna"), edgecolor=P.edge("dna"), alpha=0.8, label="null direction")
ax.hist(a, bins=bins, color=P.fill("rna"), edgecolor=P.edge("rna"), alpha=0.8, label="preferred direction")
ax.axvline(48, color=P.ink(), lw=1.2, ls="--")
ax.text(48.8, ax.get_ylim()[1] * 0.92, "criterion z", fontsize=8, color=P.ink())
ax.set_xlabel("Spike count in 2 s")
ax.set_ylabel("Number of trials (of 5000)")
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("A  Responses at 12.8 % coherence", loc="left", fontsize=10)

ax = axs[1]
for c, col in zip((3.2, 6.4, 12.8, 25.6), [P.edge("dna"), P.edge("enzyme"), P.edge("rna"), P.edge("negative")]):
    a, b = counts(40 + 0.5 * c, 5000), counts(40 - 0.25 * c, 5000)
    fa, hit = roc(a, b)
    ax.plot(fa, hit, color=col, lw=2, label=f"{c:g} %  (area {auc(a, b):.2f})")
ax.plot([0, 1], [0, 1], color=P.muted(), lw=0.8)
ax.set_xlabel("False alarm rate  P(r >= z | null)")
ax.set_ylabel("Hit rate  P(r >= z | preferred)")
ax.legend(frameon=False, fontsize=8, loc="lower right")
ax.set_aspect("equal")
ax.set_title("B  ROC curves", loc="left", fontsize=10)

ax = axs[2]
areas = np.array([auc(counts(40 + 0.5 * c, 300), counts(40 - 0.25 * c, 300)) for c in cohs])
(al, be), _ = curve_fit(weib, cohs, areas, p0=[10, 1.3], bounds=([0.5, 0.3], [100, 4]))
cc = np.logspace(np.log10(0.7), np.log10(60), 200)
ax.semilogx(cc, weib(cc, 10, 1.3), color=P.edge("rna"), lw=2.2, label="psychometric (monkey)")
ax.semilogx(cc, weib(cc, al, be), color=P.edge("dna"), lw=2.2, ls="--", label="neurometric (Weibull fit)")
ax.semilogx(cohs, areas, "o", color=P.edge("dna"), ms=5)
ax.axhline(0.82, color=P.muted(), lw=0.6)
ax.text(0.75, 0.835, "82 % criterion", fontsize=7.5, color=P.muted())
ax.set_xlabel("Motion coherence / %")
ax.set_ylabel("Proportion correct")
ax.set_ylim(0.45, 1.02)
ax.legend(frameon=False, fontsize=8, loc="lower right")
ax.set_title(f"C  Thresholds: {10:.0f} % and {al:.0f} %", loc="left", fontsize=10)
fig.tight_layout()
