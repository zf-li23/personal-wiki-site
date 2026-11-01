"""Design and batch structure seen in sample PCA. A: the airway experiment (Himes et al. 2014, GEO
GSE52778; Bioconductor package airway): principal component analysis of the variance-stabilized
expression of the 500 most variable genes in eight samples of four primary airway smooth-muscle cell
lines (marker shape), untreated or treated with dexamethasone (colour); PC1 separates treatment, PC2
the cell lines. B, C: simulations with no treatment effect at all (2000 genes, 4 + 4 samples, a batch
shift of 0.8 log2 units in 300 genes): p-values of per-gene t-tests of treatment when every treated
sample was processed in batch 2 (B, design confounded) and when each batch holds two samples of each
group and batch is a covariate in the linear model (C, balanced)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
with open("airway_vst_top500.csv") as f:
    f.readline()
    cols = f.readline().strip().split(",")
    X = np.array([[int(v) for v in line.split(",")] for line in f], float) / 100
cells = [c.split(":")[1] for c in cols]
dex = [c.split(":")[2] for c in cols]
Y = X.T - X.T.mean(0)
U, S, Vt = np.linalg.svd(Y, full_matrices=False)
pcs = U * S
ve = S ** 2 / np.sum(S ** 2) * 100

fig, axs = plt.subplots(1, 3, figsize=(11, 3.6))
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.16, top=0.88, wspace=0.3)
ax = axs[0]
marks = dict(zip(sorted(set(cells)), ["o", "s", "^", "D"]))
for i in range(len(cols)):
    tok = "rna" if dex[i] == "trt" else "dna"
    ax.plot(pcs[i, 0], pcs[i, 1], marks[cells[i]], ms=8, color=P.fill(tok), mec=P.edge(tok), mew=1.2)
for c, m in marks.items():
    ax.plot([], [], m, color=P.fill("neutral"), mec=P.edge("neutral"), label=c)
ax.plot([], [], "o", color=P.fill("dna"), mec=P.edge("dna"), label="untreated")
ax.plot([], [], "o", color=P.fill("rna"), mec=P.edge("rna"), label="dexamethasone")
ax.legend(frameon=False, fontsize=6.5, loc="upper left", ncol=2, handletextpad=0.2, columnspacing=0.8)
ax.set_ylim(pcs[:, 1].min() - 8, pcs[:, 1].max() + 22)
charts.style_axes(ax, f"PC1 ({ve[0]:.0f}% of variance)", f"PC2 ({ve[1]:.0f}%)")
charts.title(ax, "A  airway: sample PCA")

rng = np.random.default_rng(0)
G, n = 2000, 4
group = np.r_[np.zeros(n), np.ones(n)]


def simulate(batch):
    Z = rng.normal(0, 0.4, (G, 2 * n))
    Z[:300] += 0.8 * batch
    return Z


# B: batch identical to treatment; only a t-test of treatment is possible
Zb = simulate(group)
pb = stats.ttest_ind(Zb[:, group == 1], Zb[:, group == 0], axis=1).pvalue
# C: balanced; regress on [1, group, batch]
batch = np.array([0, 0, 1, 1, 0, 0, 1, 1], float)
Zc = simulate(batch)
D = np.c_[np.ones(2 * n), group, batch]
beta, *_ = np.linalg.lstsq(D, Zc.T, rcond=None)
res = Zc.T - D @ beta
df = 2 * n - 3
s2 = (res ** 2).sum(0) / df
se = np.sqrt(s2 * np.linalg.inv(D.T @ D)[1, 1])
pc = 2 * stats.t.sf(np.abs(beta[1] / se), df)
for ax, p, ttl in [(axs[1], pb, "B  Batch = treatment"), (axs[2], pc, "C  Balanced, batch modelled")]:
    h, _, _ = ax.hist(p, bins=20, range=(0, 1), color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.5)
    ax.set_ylim(0, 1.3 * h.max())
    ax.axhline(G / 20, color=charts.line("dna"), lw=1, ls="--")
    k = int(np.sum(p < 0.01))
    ax.text(0.35, 0.9, f"p < 0.01: {k} of {G} genes\n(no gene truly changes)", transform=ax.transAxes,
            fontsize=7.5, color=P.ink())
    charts.style_axes(ax, "p-value for treatment", "number of genes")
    charts.title(ax, ttl)
