"""The connectivity score of the Connectivity Map (simulated profiles). A query signature has 100 up genes
and 100 down genes; each reference profile ranks 10000 genes from most induced to most repressed by a
perturbation. Kolmogorov-Smirnov-type running sums are computed for the up and down sets (Lamb et al.,
2006). A: a reference that mimics the query (the query's up genes shifted toward the top of its ranking,
the down genes toward the bottom): the up set peaks early, the down set late, and the score is positive.
B: a reference that reverses the query, with a negative score, the profile sought for a drug against a
disease signature. C: scores of 2000 random references (null) and of 20 mimicking and 20 reversing
references whose shift is weaker (half the strength of A and B); note the logarithmic axis."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
n, t = 10000, 100
up = np.arange(t)
dn = np.arange(t, 2 * t)


def reference(strength):
    """Ranks (1 = most induced) of all genes under a perturbation that mimics (+) or reverses (-) the query."""
    z = rng.standard_normal(n)
    z[up] += strength
    z[dn] -= strength
    order = np.argsort(-z)
    rank = np.empty(n, int)
    rank[order] = np.arange(1, n + 1)
    return rank


def ks(rank, tags):
    V = np.sort(rank[tags])
    j = np.arange(1, len(V) + 1)
    a = np.max(j / len(V) - V / n)
    b = np.max(V / n - (j - 1) / len(V))
    return a if a > b else -b


def score(rank):
    ku, kd = ks(rank, up), ks(rank, dn)
    return 0.0 if np.sign(ku) == np.sign(kd) else ku - kd


def running(rank, tags):
    hit = np.zeros(n)
    hit[rank[tags] - 1] = 1
    return np.cumsum(hit / len(tags) - (1 - hit) / (n - len(tags)))


fig, axs = plt.subplots(1, 3, figsize=(12.6, 3.7))
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.17, top=0.88, wspace=0.3)
for ax, s, ttl in [(axs[0], 1.0, "A  A mimicking perturbation"), (axs[1], -1.0, "B  A reversing perturbation")]:
    r = reference(s)
    ax.plot(np.arange(1, n + 1), running(r, up), color=charts.line("negative"), lw=1.3,
            label=f"up set, KS = {ks(r, up):+.3f}")
    ax.plot(np.arange(1, n + 1), running(r, dn), color=charts.line("dna"), lw=1.3,
            label=f"down set, KS = {ks(r, dn):+.3f}")
    ax.axhline(0, color=P.muted(), lw=0.6)
    ax.text(0.04, 0.06, f"score = {score(r):+.3f}", transform=ax.transAxes, fontsize=8, color=P.ink())
    ax.legend(frameon=False, fontsize=7.5, loc="upper right")
    charts.style_axes(ax, "rank in reference profile", "running sum")
    charts.title(ax, ttl)
    print(ttl, ks(r, up), ks(r, dn), score(r))

ax = axs[2]
null = np.array([score(reference(0.0)) for _ in range(2000)])
mim = np.array([score(reference(0.5)) for _ in range(20)])
rev = np.array([score(reference(-0.5)) for _ in range(20)])
bins = np.linspace(-1.0, 1.0, 51)
ax.hist(null, bins=bins, color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.4, label="random references")
ax.hist(mim, bins=bins, color=P.fill("negative"), edgecolor=P.edge("negative"), lw=0.4, label="mimicking")
ax.hist(rev, bins=bins, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.4, label="reversing")
ax.legend(frameon=False, fontsize=7.5, loc="upper left")
ax.set_yscale("log")
charts.style_axes(ax, "connectivity score", "references (log scale)")
charts.title(ax, "C  Scores against a null")
print("null zero frac", np.mean(null == 0), "null 99% abs", np.quantile(np.abs(null), 0.99),
      "mim mean", mim.mean(), "rev mean", rev.mean(), "min mim", mim.min(), "max rev", rev.max())
