"""Counts are overdispersed (airway RNA-seq, Himes et al. 2014, GEO GSE52778; Bioconductor airway;
a random sample of 8000 of the 22369 genes with at least 10 reads). A: mean and variance of the
normalized counts over the four untreated samples, log axes. Grey line: the Poisson variance (= mean);
coloured curve: the negative binomial variance mu + alpha(mu) mu^2 with the dispersion trend
alpha(mu) = 0.0101 + 2.583/mu fitted by pydeseq2 (design ~ cell + dex). The between-donor differences in
the untreated samples add to the scatter. B: dispersion estimates against the mean: gene-wise maximum
likelihood (Cox-Reid adjusted) estimates, the fitted trend, and the final values after shrinkage
(maximum a posteriori towards the trend; genes far above the trend keep their gene-wise value). With
three residual degrees of freedom more than half of the gene-wise estimates fall on the lower bound
(drawn at the bottom of the panel).
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
with open("airway_dispersion.csv") as fh:
    rows = list(csv.DictReader(line for line in fh if not line.startswith("#")))
c = {k: np.array([float(r[k]) for r in rows]) for k in rows[0]}
fig, axs = plt.subplots(1, 2, figsize=(10.0, 4.0))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.14, top=0.88, wspace=0.27)
ax = axs[0]
ok = (c["uvar"] > -8) & (c["umean"] > -0.5)
ax.scatter(10 ** c["umean"][ok], 10 ** c["uvar"][ok], s=2, color=P.fill("neutral"), edgecolor="none", alpha=0.6)
mu = np.logspace(-0.3, 5.3, 200)
alpha = 0.0101 + 2.583 / mu
ax.plot(mu, mu, color=P.ink(), lw=1.2, label="Poisson: variance = mean")
ax.plot(mu, mu + alpha * mu ** 2, color=charts.line("rna"), lw=1.6, label=r"NB: $\mu + \alpha(\mu)\mu^2$")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(0.5, 2e5)
ax.set_ylim(1e-2, 1e10)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "mean normalized count (untreated)", "variance")
charts.title(ax, "A  Mean-variance relation")
ax = axs[1]
lo = -3.6
gw = np.where(c["lgw"] < lo, lo, c["lgw"])
ax.scatter(10 ** c["lmean"], 10 ** gw, s=2, color=P.fill("neutral"), edgecolor="none", alpha=0.7, label="gene-wise")
ax.scatter(10 ** c["lmean"], 10 ** c["lfinal"], s=2, color=charts.line("dna"), edgecolor="none", alpha=0.5,
           label="final (shrunken)")
mm = np.logspace(0, 5.5, 200)
ax.plot(mm, 0.0101 + 2.583 / mm, color=charts.line("rna"), lw=1.6, label="fitted trend")
ax.axhline(10 ** lo, color=P.muted(), lw=0.5, ls=":")
ax.text(1.2, 10 ** lo * 1.4, f"gene-wise estimate at the bound: {np.mean(c['lgw'] < lo):.0%}", fontsize=FT["tiny"],
        color=P.ink())
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_ylim(10 ** (lo - 0.2), 30)
leg = ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right", markerscale=4)
charts.style_axes(ax, "mean normalized count", r"dispersion $\alpha$")
charts.title(ax, "B  Dispersion shrinkage")
