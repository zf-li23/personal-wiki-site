"""Batch effects seen by PCA (simulation, seed 0): 2000 genes on a log scale, 4 untreated and 4 treated
samples, gene-wise noise SD 0.4; treatment shifts 200 genes by 1.0 and a processing batch shifts 300
other genes by 0.8. A: balanced design, two samples of each group in each batch: PC1 is treatment, PC2
batch, and the two can be separated. B: confounded design, all untreated samples in batch 1 and all
treated in batch 2: a single dominant component that mixes both effects. C: the confounded design
again without any treatment effect: the PCA looks almost the same as in B, so the data alone cannot
tell a treatment effect from a batch effect.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
G = 2000
group = np.r_[np.zeros(4), np.ones(4)]


def sim(batch, effect=1.0):
    Z = rng.normal(0, 0.4, (G, 8))
    Z[:200] += effect * group
    Z[200:500] += 0.8 * batch
    return Z


def pca(Z):
    X = Z.T - Z.T.mean(0)
    U, S, _ = np.linalg.svd(X, full_matrices=False)
    return U[:, :2] * S[:2], S ** 2 / np.sum(S ** 2)


cases = [("A  balanced batches", np.array([0, 0, 1, 1, 0, 0, 1, 1.0]), 1.0),
         ("B  batch = treatment", group.copy(), 1.0),
         ("C  batch = treatment, no effect", group.copy(), 0.0)]
fig, axs = plt.subplots(1, 3, figsize=(10.4, 3.5))
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.16, top=0.86, wspace=0.3)
for ax, (name, batch, eff) in zip(axs, cases):
    sc, ve = pca(sim(batch, eff))
    for i in range(8):
        tok = "rna" if group[i] else "dna"
        ax.plot(sc[i, 0], sc[i, 1], "o" if batch[i] == 0 else "s", ms=8, color=P.fill(tok), mec=P.edge(tok), mew=1.2)
    lim = 1.3 * np.abs(sc).max()
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    charts.style_axes(ax, f"PC1 ({100 * ve[0]:.0f}%)", f"PC2 ({100 * ve[1]:.0f}%)")
    charts.title(ax, name)
ax = axs[0]
ax.plot([], [], "o", color=P.fill("dna"), mec=P.edge("dna"), label="untreated")
ax.plot([], [], "o", color=P.fill("rna"), mec=P.edge("rna"), label="treated")
ax.plot([], [], "o", color=P.fill("neutral"), mec=P.edge("neutral"), label="batch 1")
ax.plot([], [], "s", color=P.fill("neutral"), mec=P.edge("neutral"), label="batch 2")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left", ncol=2, handletextpad=0.2)
