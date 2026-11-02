"""Principal component analysis of the airway samples (Himes et al. 2014, GEO GSE52778; Bioconductor
package airway): variance-stabilized expression (pydeseq2 vst) of the 500 most variable genes, centred
per gene. A: scree plot, proportion of variance per component and cumulative. B: scores on PC1 and PC2;
colour is treatment, marker shape the cell line (donor). C: loadings of the ten genes with the largest
loadings on PC1 or PC2, drawn as arrows (a loading plot, the variable half of a biplot).
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
vcols = [j for j, h in enumerate(head) if h.startswith("v:")]
genes = np.array([r[0] for r in rows])
V = np.array([[float(r[j]) for j in vcols] for r in rows])
cells = [head[j].split(":")[2] for j in vcols]
trt = [head[j].split(":")[3] == "trt" for j in vcols]
top = np.argsort(-V.var(1, ddof=1), kind="stable")[:500]
X = V[top].T
X = X - X.mean(0)
U, S, Vt = np.linalg.svd(X, full_matrices=False)
ve = S ** 2 / np.sum(S ** 2)
pcs = U * S
# sign convention: treated samples positive on PC1
if pcs[np.array(trt), 0].mean() < 0:
    pcs[:, 0] *= -1
    Vt[0] *= -1

fig, axs = plt.subplots(1, 3, figsize=(11.2, 3.8), gridspec_kw={"width_ratios": [0.8, 1.1, 1.1]})
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.15, top=0.88, wspace=0.32)
ax = axs[0]
k = np.arange(1, 8)
ax.bar(k, 100 * ve[:7], color=P.fill("enzyme"), edgecolor=P.edge("enzyme"), width=0.65)
ax.plot(k, 100 * np.cumsum(ve[:7]), "o-", color=charts.line("protein"), ms=4, lw=1.3, label="cumulative")
for i in range(4):
    ax.text(k[i], 100 * ve[i] + 2, f"{100 * ve[i]:.0f}%", ha="center", fontsize=FT["tiny"], color=P.ink())
ax.set_xticks(k)
ax.set_ylim(0, 105)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(ax, "principal component", "% of total variance")
charts.title(ax, "A  Scree plot")

ax = axs[1]
marks = {"N61311": "o", "N052611": "s", "N080611": "^", "N061011": "D"}
for i in range(8):
    tok = "rna" if trt[i] else "dna"
    ax.plot(pcs[i, 0], pcs[i, 1], marks[cells[i]], ms=8, color=P.fill(tok), mec=P.edge(tok), mew=1.2)
for a in range(4):
    i, j = 2 * a, 2 * a + 1
    ax.annotate("", xy=pcs[j, :2], xytext=pcs[i, :2],
                arrowprops=dict(arrowstyle="-|>", color=P.muted(), lw=0.8, shrinkA=6, shrinkB=6))
for c, m in marks.items():
    ax.plot([], [], m, color=P.fill("neutral"), mec=P.edge("neutral"), label=c)
ax.plot([], [], "o", color=P.fill("dna"), mec=P.edge("dna"), label="untreated")
ax.plot([], [], "o", color=P.fill("rna"), mec=P.edge("rna"), label="dexamethasone")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left", ncol=2,
          handletextpad=0.2, columnspacing=0.8)
ax.set_ylim(pcs[:, 1].min() - 8, pcs[:, 1].max() + 24)
ax.axhline(0, color=P.muted(), lw=0.5, ls=":")
ax.axvline(0, color=P.muted(), lw=0.5, ls=":")
charts.style_axes(ax, f"PC1 ({100 * ve[0]:.0f}%)", f"PC2 ({100 * ve[1]:.0f}%)")
charts.title(ax, "B  Sample scores (arrow: same donor)")

ax = axs[2]
L = Vt[:2].T
g1 = np.argsort(-np.abs(L[:, 0]))[:4]
g2 = [c for c in np.argsort(-np.abs(L[:, 1])) if c not in g1][:4]
ax.scatter(L[:, 0], L[:, 1], s=4, color=P.fill("neutral"), edgecolor="none")
for c in list(g1) + list(g2):
    ax.annotate("", xy=L[c], xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=charts.line("enzyme"), lw=1.0))
# PC1 genes: labels stacked to the right; PC2 genes: labels beside the tips, alternating sides
for rank, c in enumerate(sorted(g1, key=lambda c: -L[c, 1])):
    ty = 0.075 - 0.035 * rank
    ax.annotate(genes[top[c]], xy=L[c], xytext=(0.165, ty), fontsize=FT["tiny"], color=P.ink(), fontstyle="italic",
                va="center", ha="left", arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.5))
for c in g2:
    side = 1 if L[c, 0] >= 0 else -1
    ax.text(L[c, 0] + 0.012 * side, L[c, 1] + 0.012 * np.sign(L[c, 1]), genes[top[c]], fontsize=FT["tiny"],
            color=P.ink(), fontstyle="italic", ha="left" if side > 0 else "right", va="center")
cand = np.r_[g1, g2]
lim = 1.25 * np.abs(L[cand]).max()
ax.set_xlim(-lim, lim + 0.06)
ax.set_ylim(-lim, lim)
ax.set_aspect("equal")
ax.axhline(0, color=P.muted(), lw=0.5, ls=":")
ax.axvline(0, color=P.muted(), lw=0.5, ls=":")
charts.style_axes(ax, "loading on PC1", "loading on PC2")
charts.title(ax, "C  Gene loadings (500 genes)")
