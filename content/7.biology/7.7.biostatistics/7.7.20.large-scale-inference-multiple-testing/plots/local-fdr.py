"""The two-groups model and the local false discovery rate for the airway Wald statistics (18899 genes
kept by independent filtering; Himes et al. 2014, Bioconductor airway; pydeseq2, model ~ cell + dex).
A: histogram of z (|z| < 6 shown and fitted; 870 genes lie beyond); dashed: pi0 times the theoretical null density N(0, 1) with pi0 = 0.65 from Storey's
estimator; solid: the mixture density f estimated by Lindsey's method (a Poisson regression of the
bin counts on a degree-7 polynomial in z). B: local fdr(z) = pi0 f0(z) / f(z) and the tail-area
(Benjamini-Hochberg type) Fdr(z) = pi0 P0(|Z| > |z|) / P(|Z| > |z|), both against z.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
with open("airway_wald.csv") as fh:
    z = np.array([float(r["z"]) for r in csv.DictReader(line for line in fh if not line.startswith("#"))])
m = z.size
p = 2 * stats.norm.sf(np.abs(z))
pi0 = min(1.0, np.mean(p > 0.5) / 0.5)
edges = np.linspace(-6, 6, 121)
h, _ = np.histogram(z, edges)
mid = 0.5 * (edges[1:] + edges[:-1])
w = edges[1] - edges[0]
Xp = np.column_stack([(mid / 3) ** j for j in range(8)])
beta = np.zeros(8)
beta[0] = np.log(h.mean() + 1)
for _ in range(100):
    eta = np.clip(Xp @ beta, -50, 50)
    mu = np.exp(eta)
    beta += np.linalg.solve(Xp.T @ (Xp * mu[:, None]) + 1e-9 * np.eye(8), Xp.T @ (h - mu))
f = np.exp(Xp @ beta) / (m * w)
f0 = stats.norm.pdf(mid)
lfdr = np.minimum(1, pi0 * f0 / f)
zs = np.abs(mid)
Fdr = np.minimum(1, pi0 * 2 * stats.norm.sf(zs) / np.array([np.mean(np.abs(z) >= a) for a in zs]))
fig, axs = plt.subplots(1, 2, figsize=(10.0, 3.8))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.87, wspace=0.27)
ax = axs[0]
ax.bar(mid, h / (m * w), width=w, color=P.fill("rna"), edgecolor=P.edge("rna"), lw=0.3)
ax.plot(mid, f, color=P.ink(), lw=1.3, label="mixture f (Lindsey fit)")
ax.plot(mid, pi0 * f0, color=charts.line("dna"), lw=1.3, ls="--", label=rf"$\pi_0 f_0$, $\pi_0$ = {pi0:.2f}")
ax.set_xlim(-6, 6)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "Wald statistic z", "density")
charts.title(ax, "A  Two-groups model")
ax = axs[1]
ax.plot(mid, lfdr, color=charts.line("rna"), lw=1.6, label="local fdr")
ax.plot(mid, Fdr, color=charts.line("dna"), lw=1.3, ls="--", label="tail-area Fdr")
ax.axhline(0.2, color=P.muted(), lw=0.7, ls=":")
k = np.sum(np.interp(z, mid, lfdr, left=0, right=0) < 0.2)
ax.text(-5.7, 0.24, f"local fdr < 0.2: {k} genes", fontsize=FT["tiny"], color=P.ink())
ax.set_xlim(-6, 6)
ax.set_ylim(0, 1.05)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "Wald statistic z", "estimated false discovery rate")
charts.title(ax, "B  Local and tail-area rates")
