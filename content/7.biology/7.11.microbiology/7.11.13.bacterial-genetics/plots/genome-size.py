# Genome size and gene content of Bacteria and Archaea.
# A: number of protein-coding genes (ORFs) against genome size for representative sequenced genomes
#    (data: Madigan et al. 2019, Brock Biology of Microorganisms 15e, Table 9.1), coloured by lifestyle.
#    The line is the pooled gene density of these genomes, 0.89 genes per kb.
# B: functional categories of the genes of three genomes of decreasing size (same source, Table 9.4):
#    the smaller the genome, the larger the share of genes for translation.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P

# name, genome size (bp), ORFs, lifestyle (E endosymbiont, P parasite, F free-living), domain
DATA = [
    ("Nasuia deltocephalicola", 112091, 137, "E", "B"),
    ("Tremblaya princeps", 138931, 121, "E", "B"),
    ("Hodgkinia cicadicola", 143795, 169, "E", "B"),
    ("Buchnera aphidicola", 422434, 362, "E", "B"),
    ("Mycoplasma genitalium", 580070, 470, "P", "B"),
    ("Borrelia burgdorferi", 910725, 853, "P", "B"),
    ("Rickettsia prowazekii", 1111523, 834, "P", "B"),
    ("Treponema pallidum", 1138006, 1041, "P", "B"),
    ("strain HTCC2181", 1304428, 1354, "F", "B"),
    ("Thermotoga maritima", 1860725, 1877, "F", "B"),
    ("Deinococcus radiodurans", 3284156, 2185, "F", "B"),
    ("Bdellovibrio bacteriovorus", 3782950, 3584, "F", "B"),
    ("Bacillus subtilis", 4214810, 4100, "F", "B"),
    ("Mycobacterium tuberculosis", 4411529, 3924, "P", "B"),
    ("Escherichia coli K-12", 4639221, 4288, "F", "B"),
    ("Escherichia coli O157:H7", 5594477, 5361, "F", "B"),
    ("Pseudomonas aeruginosa", 6264403, 5570, "F", "B"),
    ("Streptomyces coelicolor", 8667507, 7825, "F", "B"),
    ("Bradyrhizobium japonicum", 9105828, 8317, "F", "B"),
    ("Sorangium cellulosum", 14782125, 11559, "F", "B"),
    ("Nanoarchaeum equitans", 490885, 552, "P", "A"),
    ("Methanocaldococcus jannaschii", 1664976, 1738, "F", "A"),
    ("Pyrococcus horikoshii", 1738505, 2061, "F", "A"),
    ("Sulfolobus solfataricus", 2992245, 2977, "F", "A"),
    ("Haloarcula marismortui", 4274642, 4242, "F", "A"),
    ("Methanosarcina acetivorans", 5751000, 4252, "F", "A"),
]
LABEL = {"Nasuia deltocephalicola": (0.22, 100), "Buchnera aphidicola": (0.75, 250), "Mycoplasma genitalium": (0.2, 560),
         "Rickettsia prowazekii": (2.2, 560), "Escherichia coli K-12": (1.5, 7600), "Sorangium cellulosum": (6.0, 20000),
         "Nanoarchaeum equitans": (0.2, 1000), "Streptomyces coelicolor": (2.6, 13500)}
STYLE = {"E": ("highlight", "endosymbiont of insects"), "P": ("negative", "parasite or pathogen"), "F": ("dna", "free-living")}

fig = plt.figure(figsize=(12.0, 4.6))
gs = fig.add_gridspec(1, 2, width_ratios=[1.35, 1.0], wspace=0.32)

ax = fig.add_subplot(gs[0, 0])
size = np.array([d[1] for d in DATA]) / 1e6
orfs = np.array([d[2] for d in DATA])
density = orfs.sum() / (size.sum() * 1000)  # genes per kb, pooled
x = np.geomspace(0.08, 20, 50)
ax.plot(x, density * 1000 * x, color=P.muted(), lw=1.0, ls="--", zorder=1)
ax.text(9, density * 1000 * 9 * 0.42, f"{density:.2f} genes per kb", fontsize=6.8, color=P.muted(), ha="center",
        rotation=33)
for life, (tok, name) in STYLE.items():
    for dom, marker in (("B", "o"), ("A", "^")):
        sel = [k for k, d in enumerate(DATA) if d[3] == life and d[4] == dom]
        if not sel:
            continue
        ax.scatter(size[sel], orfs[sel], s=30, marker=marker, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=3,
                   label=f"{name}" + (" (Archaea)" if dom == "A" else ""))
for k, d in enumerate(DATA):
    if d[0] in LABEL:
        genus, species = d[0].split(" ")[:2]
        ax.annotate(f"{genus[0]}. {species}", (size[k], orfs[k]), LABEL[d[0]], fontsize=6.8, color=P.ink(), fontstyle="italic",
                    arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6, shrinkB=3), ha="center", va="center")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(0.08, 25)
ax.set_ylim(80, 30000)
ax.legend(fontsize=6.6, frameon=False, loc="upper left")
charts.style_axes(ax, "genome size / Mb", "protein-coding genes (ORFs)")
charts.title(ax, "A   Gene number is proportional to genome size")

# ---- B: functional categories -------------------------------------------------------------------------
ax = fig.add_subplot(gs[0, 1])
cats = ["Translation", "Transcription", "Replication", "Metabolism", "Transport", "Regulation", "Structure",
        "Other, known", "Unknown"]
toks = ["rrna", "mrna", "dna", "enzyme", "channel", "protein", "cell_wall", "neutral", "extracellular"]
genomes = [("E. coli\n4.64 Mb", [4.5, 1.3, 2.7, 21.0, 10.0, 8.5, 5.5, 8.5, 38.1]),
           ("H. influenzae\n1.83 Mb", [8.0, 1.5, 4.9, 19.0, 7.0, 6.6, 4.7, 5.2, 43.0]),
           ("M. genitalium\n0.58 Mb", [21.6, 2.6, 6.8, 14.6, 7.3, 6.0, 3.6, 5.8, 32.0])]
for i, (gname, vals) in enumerate(genomes):
    left = 0.0
    tot = sum(vals)
    for v, tok, c in zip(vals, toks, cats):
        v = 100 * v / tot
        ax.barh(i, v, left=left, height=0.62, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.6,
                label=c if i == 0 else None)
        if c == "Translation" and v > 6:
            ax.text(left + v / 2, i, f"{v:.0f}%", ha="center", va="center", fontsize=6.6, color=P.on_fill(), weight="bold")
        left += v
ax.set_yticks(range(3))
ax.set_yticklabels([g[0] for g in genomes], fontsize=6.8, fontstyle="italic")
ax.set_xlim(0, 100)
ax.invert_yaxis()
ax.legend(fontsize=6.2, frameon=False, ncol=3, loc="upper center", bbox_to_anchor=(0.45, -0.16))
charts.style_axes(ax, "share of genes / %")
charts.title(ax, "B   Small genomes keep the translation machinery")
