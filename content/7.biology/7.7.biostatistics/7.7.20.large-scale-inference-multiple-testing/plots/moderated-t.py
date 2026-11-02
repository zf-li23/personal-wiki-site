"""Moderated t statistics (simulation, seed 0). 10000 genes, 3 + 3 samples on a log scale; true
gene-wise variances drawn from a scaled inverse chi-square prior with d0 = 4 degrees of freedom and
s0 = 0.25; 10% of the genes shift by 1.0. A: sample variances s^2 (4 residual degrees of freedom)
against their shrunken values, (d0 s0^2 + d s^2)/(d0 + d), with d0 and s0^2 estimated from all genes by
the method of moments on log s^2 (limma's approach); dashed: s0^2. B: number of truly changed genes
among the top-ranked genes, ranking by the ordinary t statistic, the moderated t statistic or the
fold change alone; the dotted line marks 1000, the number of changed genes.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import special, optimize
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
G, n, d0, s0 = 10000, 3, 4.0, 0.25
sig2 = d0 * s0 ** 2 / rng.chisquare(d0, G)
eff = np.zeros(G)
eff[:1000] = 1.0
A = rng.normal(0, 1, (G, n)) * np.sqrt(sig2)[:, None]
B = rng.normal(0, 1, (G, n)) * np.sqrt(sig2)[:, None] + eff[:, None]
diff = B.mean(1) - A.mean(1)
d = 2 * (n - 1)
s2 = (A.var(1, ddof=1) + B.var(1, ddof=1)) / 2
z = np.log(s2)
e = z - special.digamma(d / 2) + np.log(d / 2)
emean = e.mean()
evar = np.mean((e - emean) ** 2) * G / (G - 1) - special.polygamma(1, d / 2)
d0h = 2 * optimize.brentq(lambda x: special.polygamma(1, x) - evar, 1e-3, 1e4)
s02h = np.exp(emean + special.digamma(d0h / 2) - np.log(d0h / 2))
s2t = (d0h * s02h + d * s2) / (d0h + d)
se = np.sqrt(2 / n)
t = diff / (np.sqrt(s2) * se)
tm = diff / (np.sqrt(s2t) * se)
fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.9))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.87, wspace=0.28)
ax = axs[0]
ax.scatter(s2, s2t, s=2, color=P.fill("neutral"), edgecolor="none", alpha=0.6)
xx = np.logspace(-4, 1, 50)
ax.plot(xx, xx, color=P.muted(), lw=0.8)
ax.axhline(s02h, color=charts.line("rna"), ls="--", lw=1.0)
ax.text(2e-4, s02h * 1.25, f"$\\hat s_0^2$ = {s02h:.3f}, $\\hat d_0$ = {d0h:.1f}", fontsize=FT["tiny"], color=P.ink())
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(1e-4, 5)
ax.set_ylim(1e-4, 5)
ax.set_aspect("equal")
charts.style_axes(ax, "sample variance $s^2$", r"shrunken variance $\tilde s^2$")
charts.title(ax, "A  Variances pulled towards a common value")
ax = axs[1]
N = np.arange(1, 2001)
for score, tok, name in ((np.abs(tm), "rna", "moderated t"), (np.abs(t), "dna", "ordinary t"),
                         (np.abs(diff), "enzyme", "fold change")):
    o = np.argsort(-score)
    tp = np.cumsum(eff[o] > 0)[:2000]
    ax.plot(N, tp, color=charts.line(tok), lw=1.5, label=f"{name}: {tp[999]} in top 1000")
ax.plot(N, np.minimum(N, 1000), color=P.muted(), ls=":", lw=0.9)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "number of top-ranked genes", "truly changed genes among them")
charts.title(ax, "B  Ranking 3 vs 3 samples")
