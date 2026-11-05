# Haploid (1C) genome sizes of selected angiosperms on a log scale. Values (Mbp) from the genome papers
# (Amborella Genome Project 2013; Zhang et al. 2020 Nymphaea colorata; Yang et al. 2020 Ceratophyllum
# demersum; Hu et al. 2019 Piper nigrum; Chaw et al. 2019 Cinnamomum kanehirae; Chen et al. 2019
# Liriodendron chinense; Ming et al. 2013 Nelumbo nucifera) and the Kew Plant DNA C-values database
# (Genlisea tuberosa, Fleischmann et al. 2014; Paris japonica, Pellicer et al. 2010, 152.23 pg); 1 pg is
# taken as 978 Mbp. Orders of magnitude only.
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
DATA = [  # species, Mbp, group
    ("Genlisea tuberosa", 61, "extreme"), ("Arabidopsis thaliana", 157, "model"),
    ("Nymphaea colorata", 409, "early"), ("Oryza sativa", 430, "model"),
    ("Cinnamomum kanehirae", 730, "early"), ("Ceratophyllum demersum", 733, "early"),
    ("Piper nigrum", 761, "early"), ("Amborella trichopoda", 870, "early"),
    ("Nelumbo nucifera", 929, "model"), ("Liriodendron chinense", 1750, "early"),
    ("Zea mays", 2300, "model"), ("Allium cepa", 16000, "model"), ("Triticum aestivum", 16000, "model"),
    ("Paris japonica", 148900, "extreme"),
]
TOK = {"extreme": "negative", "model": "neutral", "early": "plant"}
fig, ax = bio.canvas(24, 13)
pax = charts.axes_at(ax, (8.6, 1.6, 14.6, 10.6))
ys = np.arange(len(DATA))[::-1]
for (name, mb, grp), y in zip(DATA, ys):
    pax.plot([30, mb], [y, y], color=P.muted(), lw=0.6, alpha=0.6)
    pax.scatter([mb], [y], s=46, color=charts.line(TOK[grp]), zorder=5)
    pax.text(mb * 1.25, y, f"{mb:,}", fontsize=7, va="center", color=P.muted())
pax.set_xscale("log")
pax.set_xlim(30, 6e5)
pax.set_yticks(ys)
pax.set_yticklabels([d[0] for d in DATA], style="italic")
pax.set_ylim(-0.7, len(DATA) - 0.3)
charts.style_axes(pax, "Haploid genome size (Mbp, log scale)", None)
for x, (lab, tok) in zip([9.0, 14.0, 18.5], [("Extremes", "negative"), ("Models and crops", "neutral"),
                                            ("Early-diverging lineages (ch. 34-35)", "plant")]):
    ax.scatter([x], [12.7], s=40, color=charts.line(tok))
    bio.label(ax, (x + 0.3, 12.7), lab, size="small", ha="left")
