"""Measurements (left) and analysis methods and models (right) of systems biology, 1995-2025, with the
chapters (7.9.n) where they appear. Years as given in the chapters: cDNA microarrays 1995 (1); the
yeast two-hybrid map 2000 and synthetic lethal genetic arrays 2001 (10); SILAC 2002 (9); RNA-seq
2008 (1); Hi-C 2009 (8); ATAC-seq 2013 (8); MERFISH and droplet single-cell RNA-seq 2015 (6, 5);
spatially barcoded arrays and Perturb-seq 2016 (6, 7); the global yeast genetic-interaction map 2016
(10); CODEX 2018 (6); Slide-seq 2019 (6); Stereo-seq, Xenium and genome-wide Perturb-seq 2022
(6, 7); the telomere-to-telomere human genome 2022 (1). Methods: the centrality-lethality rule 2001
(12); network motifs, jActiveModules and modular response analysis 2002 (15, 12, 11); MCODE and
PathBLAST 2003 (12); GSEA and ARACNe 2005 (3, 11); the connectivity map 2006 (7); target-decoy FDR
2007 (9); MACS, WGCNA, the graphical lasso and IsoRank 2008 (8, 11, 12); ChromHMM and GENIE3 2010
(8, 11); IDR 2011 (8); ICE 2012 (8); mutational signatures and network-based stratification 2013
(13); DESeq2 2014 (2); SCENIC 2017 (11); RNA velocity, MNN and scVI 2018 (7, 5); Harmony, Scrublet
and the ABC model 2019 (5, 8); Pearson residuals, Tangram and Cellpose 2021 (5, 6); CellRank 2022
(7); SpatialData 2025 (6)."""

import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
F = bio.core.FONT
T, A = "rna", "dna"

events = [
    (1995, "cDNA microarrays (1)", T),
    (2000, "genome-wide yeast two-hybrid map (10)", T),
    (2001, "synthetic genetic arrays (10)", T),
    (2002, "SILAC labeling (9)", T),
    (2008, "RNA-seq (1)", T),
    (2009, "Hi-C (8)", T),
    (2013, "ATAC-seq (8)", T),
    (2015, "droplet single-cell RNA-seq (5)", T),
    (2015, "MERFISH (6)", T),
    (2016, "spatially barcoded arrays (6)", T),
    (2016, "Perturb-seq (7)", T),
    (2016, "global yeast genetic-interaction map (10)", T),
    (2018, "CODEX (6)", T),
    (2019, "Slide-seq (6)", T),
    (2022, "Stereo-seq, Xenium (6)", T),
    (2022, "genome-wide Perturb-seq (7)", T),
    (2022, "telomere-to-telomere human genome (1)", T),
    (2001, "centrality-lethality rule (12)", A),
    (2002, "network motifs (15)", A),
    (2002, "active subnetworks; modular response analysis (12, 11)", A),
    (2003, "MCODE, PathBLAST (12)", A),
    (2005, "GSEA (3); ARACNe (11)", A),
    (2006, "connectivity map (7)", A),
    (2007, "target-decoy FDR for peptides (9)", A),
    (2008, "MACS (8); WGCNA, graphical lasso (11); IsoRank (12)", A),
    (2010, "ChromHMM (8); GENIE3 (11)", A),
    (2011, "IDR (8)", A),
    (2012, "ICE balancing of Hi-C (8)", A),
    (2013, "mutational signatures; network-based stratification (13)", A),
    (2014, "DESeq2 (2)", A),
    (2017, "SCENIC (11)", A),
    (2018, "RNA velocity (7); MNN, scVI (5)", A),
    (2019, "Harmony, Scrublet (5); ABC model (8)", A),
    (2021, "Pearson residuals (5); Tangram, Cellpose (6)", A),
    (2022, "CellRank (7)", A),
    (2025, "SpatialData (6)", A),
]

Y0, Y1 = 1993, 2027
fig, ax = plt.subplots(figsize=(8.6, 8.4))
fig.subplots_adjust(left=0.02, right=0.98, top=0.95, bottom=0.02)
ax.set_xlim(-1, 1)
ax.set_ylim(Y1, Y0)
ax.axis("off")
ax.plot([0, 0], [Y0 + 1, Y1 - 1], color=P.ink(), lw=1.0)
for y in range(1995, 2030, 5):
    ax.plot([-0.012, 0.012], [y, y], color=P.ink(), lw=0.8)
    ax.text(-0.99, y, str(y), fontsize=F["tiny"], color=P.muted(), ha="left", va="center")
    ax.plot([-0.93, -0.9], [y, y], color=P.muted(), lw=0.6)

GAP = 0.95


def spread(ys):
    out = []
    for y in ys:
        out.append(max(y, out[-1] + GAP) if out else y)
    over = out[-1] - (Y1 - 0.5) if out else 0
    if over > 0:
        out = [y - over for y in out]
        for i in range(len(out) - 2, -1, -1):
            out[i] = min(out[i], out[i + 1] - GAP)
    return out


for side, tk in ((-1, T), (1, A)):
    evs = sorted([e for e in events if e[2] == tk], key=lambda e: e[0])
    ys = spread([e[0] for e in evs])
    for (year, text, tok), yl in zip(evs, ys):
        ax.plot([0], [year], "o", ms=5, mfc=P.fill(tok), mec=P.edge(tok), mew=0.9, zorder=5)
        xl = side * 0.12
        ax.plot([0, side * 0.05, xl], [year, year, yl], color=P.edge(tok), lw=0.6, zorder=4)
        ax.text(xl + side * 0.01, yl, f"{year}  {text}" if side > 0 else f"{text}  {year}", fontsize=F["tiny"],
                color=P.ink(), ha="left" if side > 0 else "right", va="center")
ax.text(-0.5, Y0 + 0.2, "measurements", fontsize=F["small"], color=charts.line(T), ha="center", weight="bold")
ax.text(0.5, Y0 + 0.2, "analysis methods and models", fontsize=F["small"], color=charts.line(A), ha="center",
        weight="bold")
