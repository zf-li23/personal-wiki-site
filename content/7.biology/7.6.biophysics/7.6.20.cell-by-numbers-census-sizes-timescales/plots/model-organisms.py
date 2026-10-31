"""Model organisms by the numbers: haploid genome size against generation time (logarithmic axes).

Generation times are typical laboratory values: the lytic cycle of phage lambda (about 50 min from
infection to lysis), E. coli in rich and minimal medium (20 and 50 min), budding yeast (90 min),
C. elegans (3.5 days at 20 C), Drosophila (10 days at 25 C), Arabidopsis (6-8 weeks), zebrafish and
the mouse (about 3 and 2 months), Xenopus laevis (1-2 years) and humans (about 25 years). The vertical
bar for E. coli spans 20-50 min. Generation time is set by body plan and life history rather than by
the time to copy the genome, which takes 40 min in E. coli and minutes
to hours in eukaryotes, whose many replication origins work in parallel."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
day = 86400.0
org = [  # label, genome (bp), generation time (s), token, italic
    ("phage lambda", 4.85e4, 50 * 60, "virus", False),
    ("E. coli", 4.6e6, 35 * 60, "bacterium", True),
    ("S. cerevisiae", 1.2e7, 90 * 60, "neutral", True),
    ("C. elegans", 1.0e8, 3.5 * day, "animal", True),
    ("D. melanogaster", 1.4e8, 10 * day, "animal", True),
    ("A. thaliana", 1.35e8, 49 * day, "plant", True),
    ("D. rerio", 1.4e9, 90 * day, "animal", True),
    ("M. musculus", 2.7e9, 63 * day, "animal", True),
    ("X. laevis", 3.1e9, 1.5 * 365 * day, "animal", True),
    ("H. sapiens", 3.1e9, 25 * 365 * day, "animal", True),
]
fig, ax = plt.subplots(figsize=(7.2, 4.0))
fig.subplots_adjust(left=0.12, right=0.97, bottom=0.14, top=0.92)
for name, g, t, tok, it in org:
    ax.plot(g, t, "o", color=P.fill(tok), mec=P.edge(tok), ms=8, mew=1.0)
    lab = r"$\it{" + name.replace(" ", r"\ ") + "}$" if it else name
    ax.text(g * 1.35, t * (0.55 if name == "M. musculus" else 1.0), lab, va="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.errorbar([4.6e6], [35 * 60], yerr=[[15 * 60], [15 * 60]], color=P.edge("bacterium"), lw=0.8, capsize=2)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(2e4, 3e10)
ax.set_ylim(500, 3e9)
rt = ax.secondary_yaxis("right")
rt.set_yticks([3600, day, 30 * day, 365 * day, 10 * 365 * day])
rt.set_yticklabels(["1 h", "1 d", "1 mo", "1 yr", "10 yr"])
rt.tick_params(colors=P.muted(), labelcolor=P.ink(), labelsize=bio.core.FONT["tiny"])
charts.style_axes(ax, "haploid genome size / bp", "generation time / s")
