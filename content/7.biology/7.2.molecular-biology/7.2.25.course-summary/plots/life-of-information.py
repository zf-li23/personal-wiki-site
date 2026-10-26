# The life of one piece of information in a eukaryotic cell, as a process map in SBGN glyphs
# (nucleic-acid features, macromolecules, sinks). Top row, in the nucleus: a gene in closed chromatin
# is opened (remodelers, acetyltransferases), a preinitiation complex assembles on the core promoter,
# Pol II escapes into elongation and the nascent RNA is capped, spliced, cleaved and polyadenylated
# cotranscriptionally, giving a mature mRNP. Export takes it to the cytoplasm (bottom row), where it is
# translated on polysomes or degraded (deadenylation, decapping, exonucleases); the protein is folded,
# modified and targeted, and eventually degraded by the ubiquitin-proteasome system. Machines are written
# above each step and the main regulators below it; numbered badges mark the five regulatory layers.
# The dashed arc closes the loop: some products are transcription factors that act on other genes.
# The self-loop on the gene stands for its maintenance (replication, repair, recombination).
from matplotlib.patches import Circle

import wikibio as bio
from wikibio import network

P = bio.P
fig, ax = bio.canvas(25.5, 11.4)
d = network.Diagram(ax, size="small")
d.compartment("cyt", (0.3, 0.3, 25.2, 11.1), "Cytoplasm", token="cytoplasm", label_pos="tr")
d.compartment("nuc", (0.8, 6.0, 24.7, 10.25), "Nucleus", token="nucleus", label_pos="tl")

TOP, BOT = 8.3, 3.4
d.nucleic_acid("gc", (3.0, TOP), "gene in closed chromatin", token="chromatin", italic=False)
d.nucleic_acid("go", (7.9, TOP), "open promoter", token="dna", italic=False)
d.macromolecule("pic", (12.5, TOP), "preinitiation complex", token="enzyme")
d.macromolecule("elo", (17.3, TOP), "Pol II + nascent RNA", token="enzyme")
d.nucleic_acid("mrnp", (22.2, TOP), "mature mRNP", token="mrna", italic=False)
d.nucleic_acid("mc", (22.2, BOT), "cytoplasmic mRNA", token="mrna", italic=False)
d.macromolecule("poly", (17.3, BOT), "polysome", token="rrna")
d.macromolecule("prot", (12.0, BOT), "protein", token="protein")
d.empty("sp", (7.0, BOT))
d.empty("sm", (22.2, 1.25))

for a, b in (("gc", "go"), ("go", "pic"), ("pic", "elo"), ("elo", "mrnp"), ("mrnp", "mc"), ("mc", "poly"), ("poly", "prot"),
             ("prot", "sp"), ("mc", "sm")):
    d.connect(a, b, kind="process")

# maintenance of the gene and feedback of regulatory products
d.connect("gc", "gc", kind="process", loop=95, loop_size=0.75)
bio.label(ax, (3.0, 9.4), "replication, repair, recombination (7–9)", size="tiny", color=P.muted())
d.connect("prot", "go", kind="stimulation", dashed=True, via=[(12.0, 5.3), (7.9, 5.3)], color=P.muted(), lw=1.0)
bio.label(ax, (9.7, 5.12), "transcription factors act on other genes", size="tiny", color=P.muted(), va="top")

mut = P.muted()
steps = [  # (x, y, machine above, regulators below, layer)
    (5.45, TOP, "remodelers, HATs (15)", "HDACs, PRC2, HP1,\nDNA methylation", 1),
    (10.2, TOP, "TBP/TFIID, GTFs,\nMediator, activators (12–14)", "repressors, insulators,\nnucleosome positioning", 2),
    (14.9, TOP, "TFIIH, P-TEFb (13)", "promoter-proximal\npausing (DSIF, NELF)", 3),
    (19.75, TOP, "capping enzyme, spliceosome,\nCPSF, Xrn2 torpedo (16–17)", "alternative splicing,\nalternative poly(A), editing", 3),
    (14.65, BOT, "ribosome, eIF2, eIF4F,\naminoacyl-tRNAs (19)", "eIF2α-P, 4E-BPs, uORFs,\nIREs, miRNAs (20)", 4),
    (9.5, BOT, "folding, modification,\nSRP targeting (19)", "E3 ligases, degrons,\nproteasome (20)", 5),
]
for x, y, above, below, layer in steps:
    bio.label(ax, (x, y + 0.55), above, size="tiny", va="bottom")
    bio.label(ax, (x, y - 0.55), below, size="tiny", color=mut, va="top")
bio.label(ax, (22.45, 5.7), "export through\nnuclear pores", size="tiny", ha="left")
bio.label(ax, (21.75, 2.3), "deadenylation, decapping,\nXrn1, exosome, NMD (18)", size="tiny", color=mut, ha="right")
bio.label(ax, (7.0, BOT - 0.55), "degraded", size="tiny", color=mut, va="top")


def badge(xy, n):
    ax.add_patch(Circle(xy, 0.27, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.9, zorder=30))
    bio.label(ax, xy, str(n), size="tiny", bold=True, color=P.on_fill(), zorder=31)


for xy, n in (((5.45, TOP), 1), ((10.2, TOP), 2), ((14.9, TOP), 3), ((19.75, TOP), 3), ((14.65, BOT), 4), ((9.5, BOT), 5),
              ((22.2, 2.3), 5)):
    badge(xy, n)

legend = ["chromatin", "initiation", "elongation and processing", "translation", "mRNA and protein decay"]
x = 1.4
for k, t in enumerate(legend, 1):
    badge((x, 1.0), k)
    bio.label(ax, (x + 0.4, 1.0), t, size="tiny", ha="left")
    x += 0.95 + 0.115 * len(t)
