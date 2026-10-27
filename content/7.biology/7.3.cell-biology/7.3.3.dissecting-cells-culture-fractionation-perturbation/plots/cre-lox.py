# A conditional knockout with the Cre-loxP system, in SBOL Visual glyphs (triangles: loxP sites, both in
# the same orientation). Top: a mouse line carrying a "floxed" allele, in which an essential exon (exon 2) of
# the gene of interest is flanked by loxP sites placed in introns, so the gene is expressed normally.
# Middle: a second line carries a transgene expressing Cre recombinase from a tissue-specific promoter (here
# Alb, hepatocytes). Bottom: in offspring with both, Cre excises the DNA between the two loxP sites in the
# cells that express it, leaving a single loxP site and a deleted allele; other tissues keep the intact gene.
# Adding a ligand-dependent Cre (CreERT2, activated by tamoxifen) also controls the time of deletion.
import wikibio as bio
from wikibio import genetics as G

P = bio.P
fig, ax = bio.canvas(19, 8.4)

gl = G.construct(ax, 2.2, 6.6, [("promoter", "P_gene"), {"kind": "cds", "text": "exon 1", "token": "dna", "italic": False}, ("recombination", None, "highlight"),
                               {"kind": "cds", "text": "exon 2", "token": "negative", "italic": False}, ("recombination", None, "highlight"), {"kind": "cds", "text": "exon 3", "token": "dna", "italic": False},
                               ("terminator",)], unit=0.6, gap=0.35)
bio.label(ax, (0.3, 6.6), "floxed\nallele", size="small", ha="left")
bio.label(ax, (gl[2]["x0"] + 0.15, 7.55), "loxP", size="tiny")
bio.label(ax, (gl[4]["x0"] + 0.15, 7.55), "loxP", size="tiny")

G.construct(ax, 2.2, 4.4, [("promoter", "P_Alb", "positive"), ("cds", "Cre", "enzyme"), ("polya",)], unit=0.6, gap=0.35)
bio.label(ax, (0.3, 4.4), "Cre\ntransgene", size="small", ha="left")
bio.label(ax, (9.3, 4.4), "expressed only in hepatocytes", size="small", ha="left")

g3 = G.construct(ax, 2.2, 2.0, [("promoter", "P_gene"), {"kind": "cds", "text": "exon 1", "token": "dna", "italic": False}, ("recombination", None, "highlight"),
                               {"kind": "cds", "text": "exon 3", "token": "dna", "italic": False}, ("terminator",)], unit=0.6, gap=0.35)
bio.label(ax, (0.3, 2.0), "deleted\nallele", size="small", ha="left")
bio.label(ax, (9.3, 2.0), "in Cre-expressing cells: no functional product", size="small", ha="left")

ax.add_patch(__import__("matplotlib").patches.Circle(((gl[3]["x0"] + gl[3]["x1"]) / 2 + 5.6, 6.0), 0.45, fill=False,
                                                       edgecolor=P.edge("negative"), lw=1.2))
bio.label(ax, ((gl[3]["x0"] + gl[3]["x1"]) / 2 + 5.6, 6.0), "exon 2", size="tiny")
bio.label(ax, ((gl[3]["x0"] + gl[3]["x1"]) / 2 + 5.6, 5.3), "excised circle (degraded)", size="tiny")
bio.arrow(ax, (14.2, 6.2), (14.2, 2.7), kind="process", bend=0.0)
bio.label(ax, (14.4, 4.5), "Cre + loxP × 2\n→ recombination", size="small", ha="left")
