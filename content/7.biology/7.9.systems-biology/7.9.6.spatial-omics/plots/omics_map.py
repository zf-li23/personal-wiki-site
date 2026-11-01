"""The map of spatial omics: representative technologies placed by the spatial resolution of their
readout (horizontal, finer to the right) and by the number of molecular species measured in one
experiment (vertical). Colour: the omics layer; marker: the readout (capture and sequencing,
imaging, mass spectrometry). Values are approximate orders of magnitude for current versions;
genome- and epigenome-wide methods are drawn at the top."""

import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
# name, resolution in micrometres, features, layer token, readout
tech = [
    ("Slide-DNA-seq", 10, 3e4, "dna", "seq"),
    ("spatial ATAC-seq", 20, 6e4, "chromatin", "seq"),
    ("spatial CUT&Tag", 20, 3e4, "chromatin", "seq"),
    ("Visium", 55, 1.8e4, "rna", "seq"),
    ("Slide-seqV2", 10, 1.8e4, "rna", "seq"),
    ("Visium HD", 2, 1.8e4, "rna", "seq"),
    ("Stereo-seq", 0.5, 2e4, "rna", "seq"),
    ("smFISH", 0.2, 5, "rna", "img"),
    ("MERFISH", 0.15, 1000, "rna", "img"),
    ("seqFISH+", 0.15, 1e4, "rna", "img"),
    ("Xenium", 0.25, 5000, "rna", "img"),
    ("CosMx", 0.2, 6000, "rna", "img"),
    ("STARmap", 0.3, 1000, "rna", "img"),
    ("mIF", 0.5, 8, "enzyme", "img"),
    ("CODEX", 0.5, 60, "enzyme", "img"),
    ("CyCIF", 0.65, 40, "enzyme", "img"),
    ("IMC", 1, 40, "enzyme", "ms"),
    ("MIBI", 0.4, 40, "enzyme", "ms"),
    ("MALDI-MSI", 10, 1000, "atp", "ms"),
    ("scSpaMet", 1, 200, "atp", "ms"),
]
markers = {"seq": "s", "img": "o", "ms": "D"}
names = {"seq": "capture + sequencing", "img": "imaging", "ms": "mass spectrometry"}
layers = {"dna": "genome", "chromatin": "epigenome", "rna": "transcriptome", "enzyme": "proteome",
          "atp": "metabolome"}
# label offsets in points (dx, dy) and alignment
below = {"Visium", "Slide-seqV2", "MERFISH", "STARmap", "CyCIF", "scSpaMet", "Xenium"}
left = {"spatial CUT&Tag": -34}

fig, ax = plt.subplots(figsize=(9.4, 5.4))
fig.subplots_adjust(left=0.09, right=0.78, bottom=0.12, top=0.95)
for name, res, feat, tok, ro in tech:
    ax.scatter(res, feat, s=48, marker=markers[ro], color=P.fill(tok), edgecolor=P.edge(tok), lw=1.0, zorder=3)
    dy = -9 if name in below else (0 if name in left else 9)
    ax.annotate(name, (res, feat), xytext=(left.get(name, 0), dy), textcoords="offset points", fontsize=7,
                color=P.ink(), ha="center", va="center")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(150, 0.06)
ax.set_ylim(2, 2e5)
ax.axvspan(150, 10, color=P.fill("neutral"), alpha=0.18, lw=0)
ax.axvspan(10, 2, color=P.fill("neutral"), alpha=0.09, lw=0)
for x, t in [(40, "multicellular"), (4.5, "cellular"), (0.5, "subcellular")]:
    ax.text(x, 1.2e5, t, fontsize=7.5, color=P.muted(), ha="center")
charts.style_axes(ax, "spatial resolution of the readout / µm (finer to the right)",
                  "molecular species per experiment")
for tok, lab in layers.items():
    ax.scatter([], [], s=48, marker="o", color=P.fill(tok), edgecolor=P.edge(tok), label=lab)
for ro, lab in names.items():
    ax.scatter([], [], s=40, marker=markers[ro], color="none", edgecolor=P.ink(), label=lab)
ax.legend(frameon=False, fontsize=7.5, loc="upper left", bbox_to_anchor=(1.01, 1.0), labelcolor=P.ink())
