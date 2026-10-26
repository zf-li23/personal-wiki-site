# A pooled CRISPR screen and its statistics.
# A: the workflow, from array synthesis to sequencing the guide cassette before and after selection.
# B: why the multiplicity of infection is kept low - Poisson occupancy at MOI 0.3 and 3.
# C: cells needed against library size for 100-, 500- and 1000-fold representation at MOI 0.3.
# D: simulated read counts for 100,000 guides, 2% of them targeting essential genes: log fold change against
#    mean count (negative binomial counts, so the separation appears only where counts are high).
# E: internal barcodes as built-in replicates - the spread between the barcodes of one guide estimates the noise.
import math

import numpy as np
import wikibio as bio
from wikibio import quant as Q

P = bio.P
fig, ax = bio.canvas(25.0, 13.4)
rng = np.random.default_rng(0)

# ----------------------------------------------------------------- A: the workflow
bio.panel(ax, "A", (0.1, 13.2))
bio.label(ax, (5.4, 13.2), "The workflow", size="small", bold=True)
steps = [("array synthesis of $10^{5}$ guides", "dna"),
         ("cloning into a lentiviral vector", "mrna"),
         ("infection at MOI $\\approx 0.3$, selection for the vector", "rna"),
         ("the selection: drug, pathogen, sorting or proliferation", "highlight"),
         ("PCR of the guide cassette from genomic DNA", "protein"),
         ("sequencing: counts before and after", "positive")]
for k, (text, token) in enumerate(steps):
    y = 12.1 - k * 1.05
    bio.box(ax, (1.6, y), 0.85, 0.6, token=token, text=f"{k + 1}", size="tiny", radius=0.1)
    bio.label(ax, (2.25, y), text, size="tiny", ha="left", color=P.ink())
    if k < len(steps) - 1:
        bio.arrow(ax, (1.6, y - 0.33), (1.6, y - 0.72), kind="process")
bio.label(ax, (5.4, 5.5), "depleted guides mark genes required under the selection,\n"
          "enriched guides mark genes that oppose survival", size="tiny", color=P.muted())

# ----------------------------------------------------------------- B: Poisson occupancy
bio.panel(ax, "B", (0.1, 4.8))
bio.label(ax, (5.4, 4.8), "Why the multiplicity of infection is low", size="small", bold=True)
k = np.arange(0, 8)


def pois(m):
    return np.exp(-m) * m ** k / np.array([math.factorial(i) for i in k])


pl = Q.Plot(ax, (2.0, 1.3, 7.4, 2.7), xlim=(-0.6, 7.6), ylim=(0, 0.8),
            xlabel="guides integrated per cell", ylabel="fraction of cells",
            xticks=[0, 2, 4, 6], yticks=[0, 0.4, 0.8], ylabel_offset=0.9)
for m, tok, off in ((0.3, "positive", -0.18), (3.0, "negative", 0.18)):
    p = pois(m)
    for i, pi in zip(k, p):
        pl.bars([i + off - 0.17, i + off + 0.17], [pi], token=tok)
pl.text(4.2, 0.62, "MOI 0.3: one guide per infected cell", size="tiny", color=P.edge("positive"))
pl.text(4.2, 0.5, "MOI 3: a mixture of phenotypes", size="tiny", color=P.edge("negative"))
bio.label(ax, (5.4, 0.3), "at MOI 0.3 only $26\\,\\%$ of cells are infected, of which $14\\,\\%$ carry more than one guide",
          size="tiny", color=P.muted())

# ----------------------------------------------------------------- C: cells needed
bio.panel(ax, "C", (10.6, 13.2))
bio.label(ax, (14.6, 13.2), "Coverage is the binding constraint", size="small", bold=True)
lib = np.logspace(3, 5.6, 100)
pl = Q.Plot(ax, (12.4, 9.0, 4.0, 3.2), xlim=(1e3, 4e5), ylim=(1e5, 1e10), xlog=True, ylog=True,
            xlabel="guides in the library", ylabel="cells to infect",
            xticks=[(1e3, "$10^{3}$"), (1e4, "$10^{4}$"), (1e5, "$10^{5}$")],
            yticks=[(1e6, "$10^{6}$"), (1e8, "$10^{8}$"), (1e10, "$10^{10}$")], ylabel_offset=1.2)
for rep, tok, at in ((100, "neutral", 0.3), (500, "rna", 0.5), (1000, "negative", 0.7)):
    pl.line(lib, lib * rep / 0.26, tok, text=f"{rep}×", at=at, dy=0.4)
pl.hline(1e9, text="in vivo screens stop here", side="left")
bio.label(ax, (14.6, 7.95), "internal barcodes allow MOI 3–10 and cut these numbers\nby one to two orders of magnitude",
          size="tiny", color=P.muted())

# ----------------------------------------------------------------- D: the readout
bio.panel(ax, "D", (10.6, 7.2))
bio.label(ax, (14.6, 7.2), "What the counts look like", size="small", bold=True)
n = 20000
mean_counts = 10 ** rng.normal(2.3, 0.45, n)
essential = rng.random(n) < 0.02
true_lfc = np.where(essential, rng.normal(-2.2, 0.5, n), rng.normal(0.0, 0.12, n))
disp = 0.25
obs = np.log2(np.maximum(rng.poisson(mean_counts * 2 ** true_lfc * np.exp(rng.normal(0, disp, n))), 0.5)
              / np.maximum(mean_counts, 0.5))
pl = Q.Plot(ax, (12.4, 1.35, 4.0, 4.3), xlim=(5, 3e3), ylim=(-6, 3), xlog=True,
            xlabel="mean count per guide", ylabel="log$_2$ fold change",
            xticks=[(10, "10"), (100, "100"), (1e3, "1000")], yticks=[-6, -3, 0, 3], ylabel_offset=1.1)
pl.hline(0)
sel = ~essential
pl.points(mean_counts[sel][:4000], obs[sel][:4000], "neutral", r=0.022)
pl.points(mean_counts[essential], obs[essential], "negative", r=0.035)
pl.text(300, -5.2, "essential genes", size="tiny", color=P.edge("negative"))
bio.label(ax, (14.6, 0.3), "the scatter of a guide's count is what coverage buys", size="tiny", color=P.muted())

# ----------------------------------------------------------------- E: internal barcodes
bio.panel(ax, "E", (17.6, 13.2))
bio.label(ax, (21.4, 13.2), "Internal barcodes as built-in replicates", size="small", bold=True)
y = 12.2
bio.label(ax, (19.0, y), "sgRNA", size="tiny", bold=True, ha="left")
for i in range(4):
    bio.box(ax, (20.6 + i * 1.05, y), 0.95, 0.52, token="highlight", text=f"iBAR {i + 1}", size="tiny", radius=0.08)
bio.label(ax, (21.9, y - 0.72), "four barcodes in the scaffold:\none guide, four countable molecules",
          size="tiny", color=P.muted())

g = 12
lfc = rng.normal(0, 0.25, (g, 4)) + np.concatenate([rng.normal(0, 0.15, g - 3), rng.normal(-2.0, 0.2, 3)])[:, None]
pl = Q.Plot(ax, (19.4, 6.95, 4.6, 3.7), xlim=(0, g + 1), ylim=(-3.2, 1.6),
            xlabel="guide", ylabel="log$_2$ fold change per barcode",
            xticks=[1, 6, 12], yticks=[-3, -1.5, 0, 1.5], ylabel_offset=1.0)
pl.hline(0)
for i in range(g):
    tok = "negative" if lfc[i].mean() < -1 else "neutral"
    pl.points(np.full(4, i + 1), lfc[i], tok, r=0.07)
    pl.line([i + 1 - 0.3, i + 1 + 0.3], [lfc[i].mean()] * 2, tok, lw=1.6)
bio.label(ax, (21.7, 5.95), "the spread within a guide estimates the noise, so one infection\n"
          "already supports a gene-level statistic", size="tiny", color=P.muted())
bio.box(ax, (21.7, 4.6), 6.4, 1.0, token="positive",
        text="base-editor screens replace the cut: no breaks,\nso no growth artefact in amplified regions",
        size="tiny", radius=0.12)
bio.label(ax, (21.7, 3.4), "resolution: gene → exon → codon. A library in which every guide converts one\n"
          "codon turns the question from “which genes” into “which residues”.", size="tiny", color=P.ink())
