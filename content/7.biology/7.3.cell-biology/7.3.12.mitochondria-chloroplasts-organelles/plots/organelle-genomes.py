"""Gene content of organelle genomes compared with free-living relatives (logarithmic scale; approximate values).
Mitochondrial lineage: the alphaproteobacterium Rickettsia prowazekii (an obligate intracellular parasite, already
reduced; 834 protein genes), the mtDNA of the jakobid Reclinomonas americana (97 genes, the most bacteria-like
mitochondrial genome), of Arabidopsis thaliana (57), of humans (37: 13 proteins, 2 rRNAs, 22 tRNAs) and of
Plasmodium falciparum (3 protein genes plus fragmented rRNAs); the human mitochondrial proteome (MitoCarta3.0,
1136 nuclear and mitochondrially encoded proteins) for comparison. Plastid lineage: the cyanobacterium
Synechocystis sp. PCC 6803 (about 3200 protein genes), the chromatophore of Paulinella chromatophora (a second,
recent primary plastid, about 870 protein genes), a typical land-plant chloroplast genome (about 120 genes, 80 of
them for proteins) and the estimated chloroplast proteome of Arabidopsis (about 3000 proteins)."""

import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, ax = bio.canvas(20.0, 8.6)

rows = [(r"$\it{Rickettsia\ prowazekii}$ (genome)", 834, "bacterium", True),
        (r"$\it{Reclinomonas\ americana}$ mtDNA", 97, "mitochondrion", False),
        (r"$\it{Arabidopsis\ thaliana}$ mtDNA", 57, "mitochondrion", False),
        ("Human mtDNA", 37, "mitochondrion", False),
        (r"$\it{Plasmodium\ falciparum}$ mtDNA", 5, "mitochondrion", False),
        ("Human mitochondrial proteome", 1136, "neutral", False),
        (None, None, None, None),
        (r"$\it{Synechocystis}$ sp. (genome)", 3200, "bacterium", True),
        (r"$\it{Paulinella}$ chromatophore", 870, "chloroplast", True),
        ("Land-plant chloroplast genome", 120, "chloroplast", False),
        (r"$\it{Arabidopsis}$ chloroplast proteome", 3000, "neutral", False)]
a = charts.axes_at(ax, (8.6, 0.9, 10.6, 7.2))
y = 0
ticks, labels = [], []
for name, n, tok, italic in rows:
    if name is None:
        y += 0.6
        continue
    a.barh(y, n, height=0.7, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.8)
    a.text(n * 1.12, y, f"{n}", va="center", fontsize=FT["tiny"], color=P.ink())
    ticks.append(y)
    labels.append(name)
    y += 1
a.set_yticks(ticks)
a.set_yticklabels(labels, fontsize=FT["tiny"])
a.invert_yaxis()
a.set_xscale("log")
a.set_xlim(1, 10000)
charts.style_axes(a, "number of genes (genomes) or proteins (proteomes)", None)
bio.label(ax, (0.3, 8.3), "Mitochondrial lineage", size="small", bold=True, ha="left")
bio.label(ax, (0.3, 3.4), "Plastid lineage", size="small", bold=True, ha="left")
