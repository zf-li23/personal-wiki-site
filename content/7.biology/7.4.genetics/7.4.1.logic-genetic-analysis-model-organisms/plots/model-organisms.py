"""Model organisms of genetics: generation time against haploid genome size (both logarithmic).

Approximate values (generation time in days; haploid genome in Mb): E. coli 0.014, 4.6; phage lambda 0.03,
0.049; S. cerevisiae 0.06 (mitotic division), 12; N. crassa 18 (sexual cycle), 41; C. elegans 3.5, 100;
D. melanogaster 10, 140; A. thaliana 50, 135; mouse 75, 2700; zebrafish 90, 1400; maize 110, 2300;
human 9000 (about 25 years), 3100.
"""
import numpy as np

import wikibio as bio
from wikibio import ecology, quant

P = bio.P
fig, ax = bio.canvas(17.0, 11.0)
p = quant.Plot(ax, (2.2, 1.6, 14.0, 8.8), xlim=(0.005, 3.0e4), ylim=(0.02, 1.0e4), xlog=True, ylog=True,
               xlabel="generation time / d", ylabel="haploid genome size / Mb",
               xticks=[(0.01, "0.01"), (0.1, "0.1"), (1, "1"), (10, "10"), (100, "100"), (1000, "1000"), (1e4, "10⁴")],
               yticks=[(0.1, "0.1"), (1, "1"), (10, "10"), (100, "100"), (1000, "1000"), (1e4, "10⁴")], grid=True, ylabel_offset=1.05)

orgs = [
    # name, generation time (d), genome (Mb), icon id, token, label dx, dy
    ("E. coli", 0.014, 4.6, "phylopic/e-coli", "bacterium", 0.45, 0.0),
    ("phage λ", 0.03, 0.049, "servier/bacteriophage", "virus", 0.45, 0.0),
    ("S. cerevisiae", 0.06, 12.0, "phylopic/yeast", "neutral", 0.45, 0.0),
    ("N. crassa", 18.0, 41.0, None, "highlight", 0.3, -0.05),
    ("C. elegans", 3.5, 100.0, "phylopic/c-elegans", "animal", -0.45, 0.0),
    ("D. melanogaster", 10.0, 140.0, "phylopic/drosophila", "animal", 0.0, 0.55),
    ("A. thaliana", 50.0, 135.0, "phylopic/arabidopsis", "plant", 0.45, -0.25),
    ("M. musculus", 75.0, 2700.0, "phylopic/mouse", "animal", -0.45, 0.2),
    ("D. rerio", 90.0, 1400.0, "phylopic/zebrafish", "animal", 0.45, -0.1),
    ("Z. mays", 110.0, 2300.0, "phylopic/maize", "plant", 0.5, 0.05),
    ("H. sapiens", 9000.0, 3100.0, "phylopic/human", "neutral", -0.45, 0.0),
]
for name, g, mb, ic, tok, dx, dy in orgs:
    x, y = p.xy(g, mb)
    if ic:
        ecology.fit_icon(ax, ic, (x, y), 0.75, 0.6, color=tok)
    else:
        p.points([g], [mb], tok, r=0.12)
    ha = "left" if dx > 0 else "right" if dx < 0 else "center"
    bio.label(ax, (x + dx, y + dy), name, size="small", italic=not name.startswith("phage"), ha=ha)


