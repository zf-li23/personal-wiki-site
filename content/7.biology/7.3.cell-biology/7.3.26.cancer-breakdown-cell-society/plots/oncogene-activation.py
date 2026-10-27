"""Four ways to turn a proto-oncogene into an oncogene (schematic).

(A) Point mutation in the coding sequence changes the protein: Ras with Gly12 replaced (G12V, G12D, G12C)
cannot hydrolyze GTP and stays active (hyperactive protein, normal amount).
(B) Gene amplification: many copies of the gene, in tandem arrays within a chromosome (homogeneously staining
regions) or on extrachromosomal DNA, give overexpression of a normal protein (ERBB2/HER2 in breast cancer,
MYCN in neuroblastoma).
(C) Chromosomal translocation can join two genes into a fusion gene that encodes a new, deregulated protein
(BCR-ABL1 from the Philadelphia chromosome t(9;22) in chronic myeloid leukemia, a constitutively active
tyrosine kinase), or place an intact gene next to a strong enhancer (MYC next to the immunoglobulin
heavy-chain enhancer in Burkitt lymphoma, t(8;14)).
(D) Insertional mutagenesis: a retrovirus integrates near the gene and its long terminal repeat (LTR)
promoter or enhancer drives overexpression (avian leukosis virus next to MYC in bursal lymphoma).
"""

import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(28.0, 11.0)


def gene(x, y, w, text, tok="dna", italic=True, h=0.55):
    ax.add_patch(FancyBboxPatch((x, y - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.08",
                                facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.0, zorder=6))
    if text:
        bio.label(ax, (x + w / 2, y), text, size="tiny", italic=italic, color=P.on_fill(), zorder=7)


def chrom_line(x0, x1, y):
    ax.plot([x0, x1], [y, y], color=P.edge("dna"), lw=1.6, zorder=4, solid_capstyle="round")


def promoter(x, y, tok="ink"):
    c = P.ink() if tok == "ink" else P.edge(tok)
    ax.plot([x, x, x + 0.45], [y + 0.28, y + 0.75, y + 0.75], color=c, lw=1.2, zorder=8)
    ax.plot([x + 0.35, x + 0.48, x + 0.35], [y + 0.85, y + 0.75, y + 0.65], color=c, lw=1.2, zorder=8)


def proteins(x, y, n, tok, cols=6):
    for i in range(n):
        ax.add_patch(Circle((x + (i % cols) * 0.34, y - (i // cols) * 0.34), 0.13, facecolor=P.fill(tok),
                            edgecolor=P.edge(tok), lw=0.6, zorder=8))


def frame(x, y, letter, title):
    bio.panel(ax, letter, (x, y))
    bio.label(ax, (x + 0.8, y - 0.18), title, size="normal", bold=True, ha="left", va="top")


# A point mutation ---------------------------------------------------------
frame(0.2, 10.8, "A", "Point mutation")
for row, (txt, tok, lab) in enumerate((("KRAS", "dna", "normal"), ("KRAS", "negative", "mutant"))):
    y = 9.0 - row * 1.6
    chrom_line(1.0, 7.6, y)
    promoter(2.2, y)
    gene(2.6, y, 3.0, txt, tok)
    bio.label(ax, (0.9, y), lab, size="tiny", ha="right", color=P.muted())
    bio.arrow(ax, (7.9, y), (8.9, y), kind="process")
    bio.protein(ax, (10.2, y), 1.3, 0.7, "enzyme" if row == 0 else "negative", text="Ras")
    bio.label(ax, (12.4, y), "GTP ⇄ GDP\nregulated" if row == 0 else "GTP-locked,\nalways on", size="tiny",
              ha="center")
ax.plot([3.1, 3.1], [7.15, 7.65], color=P.edge("negative"), lw=2.2, zorder=9)
bio.label(ax, (3.1, 6.95), "codon 12: Gly → Val", size="tiny", color=P.edge("negative"))

# B amplification -----------------------------------------------------------
frame(14.2, 10.8, "B", "Gene amplification")
y = 9.0
chrom_line(15.0, 21.0, y)
gene(17.0, y, 1.6, "ERBB2")
bio.label(ax, (14.9, y), "normal", size="tiny", ha="right", color=P.muted())
proteins(22.2, y + 0.15, 3, "receptor")
y = 7.4
chrom_line(15.0, 21.6, y)
for k in range(5):
    gene(15.4 + k * 1.22, y, 1.05, "ERBB2" if k == 0 else "", "negative")
bio.label(ax, (14.9, y), "tandem\ncopies", size="tiny", ha="right", color=P.muted())
for k, c in enumerate([(16.3, 6.1), (17.6, 6.25), (18.9, 6.05)]):
    ax.add_patch(Circle(c, 0.42, fill=False, edgecolor=P.edge("dna"), lw=1.4, zorder=5))
    gene(c[0] - 0.3, c[1] + 0.42, 0.6, "", "negative", h=0.3)
bio.label(ax, (20.3, 6.1), "ecDNA", size="tiny", ha="left", color=P.muted())
proteins(22.2, y + 0.4, 18, "receptor")
bio.label(ax, (23.1, 5.6), "overexpressed\nnormal protein", size="tiny")

# C translocation -----------------------------------------------------------
frame(0.2, 5.2, "C", "Chromosomal translocation")
y = 3.6
chrom_line(1.0, 8.0, y + 0.8)
gene(1.6, y + 0.8, 2.4, "BCR", "dna")
bio.label(ax, (0.9, y + 0.8), "chr 22", size="tiny", ha="right", color=P.muted())
chrom_line(1.0, 8.0, y - 0.6)
gene(5.0, y - 0.6, 2.6, "ABL1", "channel")
bio.label(ax, (0.9, y - 0.6), "chr 9", size="tiny", ha="right", color=P.muted())
ax.plot([4.25, 4.25], [y + 0.45, y + 1.15], color=P.edge("negative"), lw=1.4, ls=(0, (2, 1.5)), zorder=9)
ax.plot([4.75, 4.75], [y - 0.95, y - 0.25], color=P.edge("negative"), lw=1.4, ls=(0, (2, 1.5)), zorder=9)
bio.label(ax, (4.5, y + 0.1), "breaks", size="tiny", color=P.edge("negative"))
bio.arrow(ax, (8.4, y), (9.4, y), kind="process")
chrom_line(9.8, 15.2, y + 0.1)
gene(10.2, y + 0.1, 2.4, "BCR", "dna")
gene(12.6, y + 0.1, 2.4, "ABL1", "channel")
bio.label(ax, (12.5, y - 0.6), "Philadelphia chromosome (22q−)", size="tiny", color=P.muted())
bio.arrow(ax, (15.5, y + 0.1), (16.5, y + 0.1), kind="process")
bio.protein(ax, (18.3, y + 0.1), 2.6, 0.75, "negative", text="BCR–ABL1")
bio.label(ax, (18.3, y - 0.9), "constitutive tyrosine kinase (CML)", size="tiny")
bio.label(ax, (8.0, 1.2), "also: MYC next to the IGH enhancer, t(8;14), Burkitt lymphoma", size="tiny",
          color=P.muted())

# D insertional mutagenesis -------------------------------------------------
frame(21.0, 5.2, "D", "Insertional mutagenesis")
y = 3.6
chrom_line(21.4, 27.6, y)
ax.add_patch(FancyBboxPatch((21.8, y - 0.3), 1.4, 0.6, boxstyle="round,pad=0,rounding_size=0.08",
                            facecolor=P.fill("virus"), edgecolor=P.edge("virus"), lw=1.0, zorder=6))
bio.label(ax, (22.5, y), "LTR", size="tiny", color=P.on_fill(), zorder=7)
promoter(23.1, y, tok="virus")
gene(24.0, y, 2.4, "MYC", "negative")
bio.label(ax, (22.5, y - 0.75), "provirus", size="tiny", color=P.muted())
proteins(24.2, y - 1.0, 12, "negative", cols=6)
bio.label(ax, (25.2, 1.2), "viral promoter or enhancer\ndrives overexpression", size="tiny")
