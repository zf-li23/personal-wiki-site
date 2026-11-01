"""Over-representation analysis and GSEA give different answers. The 50 MSigDB Hallmark sets (CC BY
4.0) tested on the airway data (dexamethasone against untreated, pydeseq2). Horizontal: normalized
enrichment score of preranked GSEA on the Wald statistic (2000 random gene sets per set). Vertical:
-log10 p of ORA for the 544 induced genes (padj < 0.05, log2 FC > 1) among 18865 tested genes.
Filled: GSEA q < 0.05; ringed: ORA q < 0.05 (Benjamini-Hochberg across the 50 sets). Sets such as
oxidative phosphorylation or E2F targets are found only by GSEA (coordinated small shifts of many
genes, or a shift downwards that a list of induced genes cannot see); TNF-alpha signaling stands out
in both."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rows = []
with open("hallmark_airway.csv") as f:
    f.readline()
    f.readline()
    for line in f:
        # the set names may contain commas only inside quotes; split from the right
        parts = line.rstrip("\n").rsplit(",", 9)
        rows.append(parts)
names = [r[0].strip('"') for r in rows]
nes = np.array([float(r[3]) for r in rows])
q_g = np.array([float(r[5]) for r in rows])
p_o = np.array([float(r[8]) for r in rows])
q_o = np.array([float(r[9]) for r in rows])
y = -np.log10(p_o)
fig, ax = plt.subplots(figsize=(7.2, 4.4))
fig.subplots_adjust(left=0.1, right=0.97, bottom=0.13, top=0.95)
for i in range(len(rows)):
    tok = "rna" if nes[i] > 0 else "dna"
    fc = P.fill(tok) if q_g[i] < 0.05 else "none"
    ax.scatter(nes[i], y[i], s=34, facecolor=fc, edgecolor=P.edge(tok), lw=1.0, zorder=3)
    if q_o[i] < 0.05:
        ax.scatter(nes[i], y[i], s=110, facecolor="none", edgecolor=P.ink(), lw=0.7, zorder=2)
label = {"TNF-alpha Signaling via NF-kB", "Oxidative Phosphorylation", "E2F Targets", "p53 Pathway",
         "Hypoxia", "Adipogenesis", "KRAS Signaling Up"}
for i, nm in enumerate(names):
    if nm in label:
        ax.annotate(nm, (nes[i], y[i]), xytext=(5, 4), textcoords="offset points", fontsize=7, color=P.ink())
ax.axvline(0, color=P.muted(), lw=0.7)
ax.axhline(-np.log10(0.05), color=P.muted(), lw=0.7, ls="--")
charts.style_axes(ax, "GSEA normalized enrichment score (NES)", "ORA of induced genes, -log10 p")
