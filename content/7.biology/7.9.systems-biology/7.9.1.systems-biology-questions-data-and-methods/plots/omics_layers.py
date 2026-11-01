"""The layers of omics data. Each layer is a complete inventory of one class of molecules (or of
phenotypes); the downward arrows follow the flow of genetic information, the dashed arrows on the
right the regulation that closes the loop. For each layer: what is measured, the main technologies
and the finest resolution in routine use."""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(19, 11.6)

layers = [
    ("Genome", "dna", "DNA sequence and variants", "short- and long-read sequencing", "cell population, single cell"),
    ("Epigenome", "chromatin", "methylation, accessibility,\nhistone marks, 3D contacts",
     "bisulfite-seq, ATAC-seq,\nChIP-seq, Hi-C", "single cell"),
    ("Transcriptome", "rna", "RNA abundance, isoforms", "RNA-seq, microarrays", "single cell, spatial"),
    ("Translatome", "rrna", "ribosome-bound mRNA", "ribosome profiling", "cell population"),
    ("Proteome", "protein", "protein abundance, modifications", "mass spectrometry, antibody panels", "cell population, spatial"),
    ("Metabolome", "metabolite", "small-molecule concentrations, fluxes", "MS (GC, LC), NMR", "cell population, spatial"),
    ("Phenome", "positive", "traits: morphology, physiology, disease", "imaging, clinical records", "organism"),
]

top, step, h = 9.6, 1.42, 1.0
xb = 2.6
bio.label(ax, (xb, top + 1.1), "Layer", size="small", bold=True)
bio.label(ax, (7.7, top + 1.1), "What is measured", size="small", bold=True)
bio.label(ax, (12.3, top + 1.1), "Main technologies", size="small", bold=True)
bio.label(ax, (16.6, top + 1.1), "Resolution", size="small", bold=True)
ys = []
for i, (name, tok, what, tech, res) in enumerate(layers):
    y = top - i * step
    ys.append(y)
    bio.box(ax, (xb, y), 3.2, h, tok, text=name, size="normal")
    bio.label(ax, (5.7, y), what, size="tiny", ha="left")
    bio.label(ax, (10.4, y), tech, size="tiny", ha="left")
    bio.label(ax, (15.4, y), res, size="tiny", ha="left")
    if i:
        bio.arrow(ax, (xb, ys[i - 1] - h / 2 - 0.04), (xb, y + h / 2 + 0.04), kind="process")

# interactome bracket on the left: interactions among the molecules of the middle layers
x0 = 0.55
ax.plot([x0 + 0.25, x0, x0, x0 + 0.25], [ys[1] + 0.3, ys[1] + 0.3, ys[5] - 0.3, ys[5] - 0.3], color=P.muted(), lw=1.0)
bio.label(ax, (x0 - 0.25, (ys[1] + ys[5]) / 2), "Interactome", size="small", rotation=90)

# regulation feeding back on the genome-proximal layers
bio.arrow(ax, (xb + 1.65, ys[4]), (xb + 1.65, ys[1] - 0.15), kind="activation", dashed=True, bend=-0.35)
bio.arrow(ax, (xb + 1.65, ys[5] + 0.1), (xb + 1.65, ys[2] - 0.15), kind="activation", dashed=True, bend=-0.35)
bio.label(ax, (xb + 2.55, (ys[2] + ys[4]) / 2), "regulation", size="tiny", color=P.muted(), rotation=90)
