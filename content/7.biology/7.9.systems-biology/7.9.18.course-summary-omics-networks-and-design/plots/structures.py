"""Recurring mathematical structures (columns) in the chapters 7.9.2-7.9.17 (rows). A dot means that
the chapter develops or uses the structure in a numbered statement or a worked analysis; the list
follows the index tables of section 18.3-18.5. Colours group the columns: statistics of the
measurements, graphs and networks, dynamics."""

import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
F = bio.core.FONT

cols = [
    ("count models", "stat"),
    ("mixtures, EM", "stat"),
    ("FDR, multiple testing", "stat"),
    ("randomized nulls", "stat"),
    ("set enrichment", "stat"),
    ("factorization, embedding", "stat"),
    ("information theory", "stat"),
    ("neighbor graphs, communities", "net"),
    ("random walks, Markov chains", "net"),
    ("optimal transport, scaling", "net"),
    ("HMM, Markov random field", "net"),
    ("ODEs, stability", "dyn"),
    ("stochastic dynamics, noise", "dyn"),
    ("fitting, identifiability", "dyn"),
]
C = {name: i for i, (name, _) in enumerate(cols)}
rows = [
    (2, "Bulk transcriptomics", ["count models", "mixtures, EM", "FDR, multiple testing", "factorization, embedding"]),
    (3, "Gene-set analysis", ["randomized nulls", "set enrichment", "FDR, multiple testing"]),
    (4, "RNA processing, translation", ["count models", "mixtures, EM", "FDR, multiple testing"]),
    (5, "Single cells", ["count models", "factorization, embedding", "neighbor graphs, communities", "mixtures, EM"]),
    (6, "Spatial omics", ["mixtures, EM", "randomized nulls", "neighbor graphs, communities", "optimal transport, scaling",
                          "HMM, Markov random field", "information theory"]),
    (7, "Trajectories, fates", ["random walks, Markov chains", "neighbor graphs, communities", "ODEs, stability",
                                "stochastic dynamics, noise", "set enrichment", "randomized nulls"]),
    (8, "Epigenome, 3D genome", ["count models", "mixtures, EM", "HMM, Markov random field", "optimal transport, scaling",
                                 "factorization, embedding", "FDR, multiple testing"]),
    (9, "Proteome, metabolome", ["randomized nulls", "FDR, multiple testing", "count models", "set enrichment"]),
    (10, "Interactomes, CRISPR screens", ["count models", "randomized nulls", "FDR, multiple testing",
                                         "neighbor graphs, communities"]),
    (11, "Regulatory networks", ["information theory", "neighbor graphs, communities", "set enrichment", "ODEs, stability", "fitting, identifiability",
                                "randomized nulls"]),
    (12, "Network analysis", ["randomized nulls", "neighbor graphs, communities", "random walks, Markov chains", "set enrichment"]),
    (13, "Cancer", ["count models", "factorization, embedding", "random walks, Markov chains", "FDR, multiple testing"]),
    (14, "Kinetic models", ["ODEs, stability", "fitting, identifiability"]),
    (15, "Motifs", ["randomized nulls", "ODEs, stability"]),
    (16, "Feedback, oscillations", ["ODEs, stability", "stochastic dynamics, noise", "information theory"]),
    (17, "Noise, robustness, evolution", ["stochastic dynamics, noise", "ODEs, stability", "information theory"]),
]
tok = {"stat": "rna", "net": "protein", "dyn": "enzyme"}

fig, ax = plt.subplots(figsize=(8.6, 6.4))
fig.subplots_adjust(left=0.27, right=0.99, top=0.70, bottom=0.04)
for j, (name, grp) in enumerate(cols):
    ax.axvline(j, color=P.muted(), lw=0.3, alpha=0.4, zorder=0)
for i, (n, name, used) in enumerate(rows):
    ax.axhline(i, color=P.muted(), lw=0.3, alpha=0.4, zorder=0)
    for u in used:
        j = C[u]
        g = cols[j][1]
        ax.plot(j, i, "o", ms=8.5, mfc=P.fill(tok[g]), mec=P.edge(tok[g]), mew=0.9, zorder=3)
ax.set_xlim(-0.6, len(cols) - 0.4)
ax.set_ylim(len(rows) - 0.5, -0.5)
ax.set_yticks(range(len(rows)))
ax.set_yticklabels([f"7.9.{n}  {name}" for n, _, name in [(r[0], None, r[1]) for r in rows]], fontsize=F["small"])
ax.set_xticks(range(len(cols)))
ax.set_xticklabels([c[0] for c in cols], rotation=55, ha="left", fontsize=F["small"])
ax.xaxis.tick_top()
charts.style_axes(ax)
for sp in ax.spines.values():
    sp.set_visible(False)
ax.tick_params(length=0)
for lab, (name, grp) in zip(ax.get_xticklabels(), cols):
    lab.set_color(charts.line(tok[grp]))
