"""How the scale of the data changes a PCA (airway RNA-seq, Himes et al. 2014, GEO GSE52778;
Bioconductor package airway; eight samples, four cell lines with and without dexamethasone). On each
scale the 500 genes with the largest variance on that scale are kept and centred. A: normalized counts;
B: log2(normalized count + 1); C: variance-stabilized values (pydeseq2 vst). D: mean normalized count of
the 500 genes chosen on each scale (box plots, log axis): the raw scale selects only very highly
expressed genes, log2(x + 1) many weakly expressed and noisy ones.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
with open("airway_expr.csv") as fh:
    rows = [r for r in csv.reader(line for line in fh if not line.startswith("#"))]
head, rows = rows[0], rows[1:]
ncols = [j for j, h in enumerate(head) if h.startswith("n:")]
vcols = [j for j, h in enumerate(head) if h.startswith("v:")]
N = np.array([[float(r[j]) for j in ncols] for r in rows])
V = np.array([[float(r[j]) for j in vcols] for r in rows])
cells = [head[j].split(":")[2] for j in vcols]
trt = np.array([head[j].split(":")[3] == "trt" for j in vcols])
marks = {"N61311": "o", "N052611": "s", "N080611": "^", "N061011": "D"}
scales = [("A  normalized counts", N), ("B  log2(count + 1)", np.log2(N + 1)), ("C  vst", V)]

fig, axs = plt.subplots(1, 4, figsize=(12.4, 3.4), gridspec_kw={"width_ratios": [1, 1, 1, 0.8]})
fig.subplots_adjust(left=0.05, right=0.99, bottom=0.17, top=0.87, wspace=0.36)
chosen = []
for ax, (name, M) in zip(axs, scales):
    top = np.argsort(-M.var(1, ddof=1), kind="stable")[:500]
    chosen.append(top)
    X = M[top].T
    X = X - X.mean(0)
    U, S, _ = np.linalg.svd(X, full_matrices=False)
    ve = S ** 2 / np.sum(S ** 2)
    sc = U[:, :2] * S[:2]
    if sc[trt, 0].mean() < 0:
        sc[:, 0] *= -1
    sc = sc / np.abs(sc).max()
    for i in range(8):
        tok = "rna" if trt[i] else "dna"
        ax.plot(sc[i, 0], sc[i, 1], marks[cells[i]], ms=7, color=P.fill(tok), mec=P.edge(tok), mew=1.1)
    ax.set_xlim(-1.25, 1.25)
    ax.set_ylim(-1.25, 1.25)
    ax.set_xticks([])
    ax.set_yticks([])
    charts.style_axes(ax, f"PC1 ({100 * ve[0]:.0f}%)", f"PC2 ({100 * ve[1]:.0f}%)")
    charts.title(ax, name)
for c, m in marks.items():
    axs[0].plot([], [], m, color=P.fill("neutral"), mec=P.edge("neutral"), label=c)
axs[0].plot([], [], "o", color=P.fill("dna"), mec=P.edge("dna"), label="untreated")
axs[0].plot([], [], "o", color=P.fill("rna"), mec=P.edge("rna"), label="dexamethasone")
axs[0].legend(frameon=False, fontsize=5.8, labelcolor=P.ink(), loc="lower left", ncol=2, handletextpad=0.2,
              columnspacing=0.6)
ax = axs[3]
mean = N.mean(1)
bp = ax.boxplot([np.log10(mean[t]) for t in chosen], widths=0.55, patch_artist=True, showfliers=False)
for b in bp["boxes"]:
    b.set(facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"))
for k in ("whiskers", "caps", "medians"):
    for l in bp[k]:
        l.set_color(P.ink())
ax.set_xticks([1, 2, 3])
ax.set_xticklabels(["counts", "log2(x+1)", "vst"], fontsize=FT["tiny"])
ax.set_yticks([0, 1, 2, 3, 4, 5])
ax.set_yticklabels(["1", "10", "$10^2$", "$10^3$", "$10^4$", "$10^5$"])
charts.style_axes(ax, None, "mean normalized count")
charts.title(ax, "D  Genes selected")
