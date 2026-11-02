"""Orders of magnitude of the data of the course, with the chapters (7.9.n) that give them.

Points are single values, bars ranges, all as stated in the chapters: a 30x human genome is
9.3e10 bases and about 2.2e11 bytes of reads (1); a human cell holds of the order of 1e5 mRNA
molecules (6), of which a droplet protocol counts a few thousand (5); a Visium spot holds parts of
5-40 cells (6); experiments have tens of thousands of cells and atlases millions (5), foundation
models are pretrained on tens of millions (7); the airway study has 8 libraries and 18 865 ranked
genes (2, 3); about 0.9 million cCREs and 28 million CpGs (8); 10 kb Hi-C has 4.8e10 bin pairs, the
GM12878 map 4.9e9 contacts (8); a human proteome has about 1e6 tryptic peptides, protein copy
numbers span 1e3-1e8 per cell (9); the yeast genetic-interaction map tested 2.3e7 double mutants
and found about 9e5 interactions (10); 1600 factors and 20 000 genes give 3.2e7 candidate arcs (11)
and 2e8 gene pairs (12); the E. coli network of Shen-Orr and colleagues has 424 operons and 519
arcs (15); a 1 cm2 CODEX whole-slide image is 4e10 bytes (6)."""

import numpy as np
import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
F = bio.core.FONT

# (label, low, high, chapter, group); high = None for a single value
items = [
    ("cells sharing one Visium spot", 5, 40, "6", "space"),
    ("libraries in the airway study", 8, None, "2", "bulk"),
    (r"$\it{E.\ coli}$ transcription network: operons, arcs", 424, 519, "15", "net"),
    ("UMIs counted per cell (droplets)", 1e3, 1e4, "5", "cell"),
    ("protein copies per human cell", 1e3, 1e8, "9", "prot"),
    ("genes ranked in the airway analysis", 18865, None, "3", "bulk"),
    ("mRNA molecules per mammalian cell", 1e5, None, "6", "cell"),
    ("cells per single-cell experiment", 1e4, 1e5, "5", "cell"),
    ("candidate cis-regulatory elements (ENCODE)", 9e5, None, "8", "epi"),
    ("tryptic peptides of the human proteome", 1e6, None, "9", "prot"),
    ("genetic interactions found in yeast", 9e5, None, "10", "net"),
    ("cells in atlas projects", 1e6, 1e7, "5", "cell"),
    ("cells used to pretrain foundation models", 1e7, 1e8, "7", "cell"),
    ("double mutants tested in yeast", 2.3e7, None, "10", "net"),
    ("CpGs of the human genome", 2.8e7, None, "8", "epi"),
    ("candidate factor-gene arcs (1600 x 20 000)", 3.2e7, None, "11", "net"),
    ("gene pairs of 20 000 genes", 2e8, None, "12", "net"),
    ("Hi-C contacts, GM12878 map", 4.9e9, None, "8", "epi"),
    ("bases sequenced for a 30x human genome", 9.3e10, None, "1", "bulk"),
    ("Hi-C bin pairs at 10 kb resolution", 4.8e10, None, "8", "epi"),
    ("bytes: CODEX whole slide, 1 cm2, 50 channels", 4e10, None, "6", "space"),
    ("bytes: reads of one 30x human genome", 2.2e11, None, "1", "bulk"),
]
tok = {"bulk": "rna", "cell": "positive", "space": "highlight", "epi": "chromatin", "prot": "protein", "net": "dna"}
names = {"bulk": "sequencing, bulk", "cell": "single cells", "space": "spatial", "epi": "epigenome",
         "prot": "proteome", "net": "networks"}

items.sort(key=lambda it: it[1])
fig, ax = plt.subplots(figsize=(8.6, 6.6))
fig.subplots_adjust(left=0.43, right=0.97, top=0.95, bottom=0.09)
for i, (lab, lo, hi, ch, g) in enumerate(items):
    c, f = charts.line(tok[g]), P.fill(tok[g])
    if hi is None:
        ax.plot(lo, i, "o", ms=6.5, mfc=f, mec=c, mew=1.0, zorder=3)
    else:
        ax.plot([lo, hi], [i, i], color=c, lw=5.5, solid_capstyle="round", alpha=0.9, zorder=2)
    ax.text((hi or lo) * 2.2, i, f"7.9.{ch}", fontsize=F["tiny"], color=P.muted(), va="center")
ax.set_xscale("log")
ax.set_xlim(1, 1e13)
ax.set_ylim(len(items) - 0.4, -0.6)
ax.set_yticks(range(len(items)))
ax.set_yticklabels([it[0] for it in items], fontsize=F["tiny"])
ax.set_xticks([10.0 ** k for k in range(0, 14, 2)])
for k in range(0, 14):
    ax.axvline(10.0 ** k, color=P.muted(), lw=0.3, alpha=0.35, zorder=0)
charts.style_axes(ax, "number (log scale)")
handles = [plt.Line2D([], [], marker="o", ls="", mfc=P.fill(tok[g]), mec=charts.line(tok[g]), label=names[g])
           for g in names]
ax.legend(handles=handles, fontsize=F["tiny"], frameon=False, loc="upper right")
