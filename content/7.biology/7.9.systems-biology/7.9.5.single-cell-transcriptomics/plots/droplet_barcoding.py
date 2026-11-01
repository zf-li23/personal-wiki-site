"""Barcoding in a droplet experiment (layout of the 10x Genomics 3' chemistry). A: a cell and a gel bead
are enclosed together in an oil droplet; the cell is lysed and its polyadenylated mRNAs bind to the
oligonucleotides of the bead. B: each oligonucleotide carries a primer site for sequencing read 1, a cell
barcode of 16 nt shared by all oligos of one bead, a unique molecular identifier of 12 nt that differs
between oligos, and a poly(dT) stretch; reverse transcription copies the mRNA, and template switching at
the 5' end of the mRNA adds a known sequence (TSO) for amplification. C: the final library molecule:
read 1 (28 nt) reads barcode and UMI, the index read gives the sample, read 2 (about 90 nt) reads the
cDNA near the 3' end of the transcript."""

import numpy as np
from matplotlib.patches import Circle, Rectangle
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30, 11)

# A: droplet
bio.panel(ax, "A", (0.2, 10.8))
ax.add_patch(Rectangle((0.4, 1.2), 8.4, 8.6, facecolor=P.fill("lipid"), edgecolor="none", zorder=1))
bio.label(ax, (4.6, 1.6), "oil", size="small", color=P.on_fill())
ax.add_patch(Circle((4.6, 5.6), 3.4, facecolor=P.fill("extracellular"), edgecolor=P.edge("extracellular"), lw=1.2, zorder=2))
ax.add_patch(Circle((3.4, 5.6), 1.35, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1.0, zorder=3))
for t in np.linspace(0, 2 * np.pi, 22, endpoint=False):
    a = np.array([3.4, 5.6]) + 1.35 * np.array([np.cos(t), np.sin(t)])
    b = np.array([3.4, 5.6]) + 1.75 * np.array([np.cos(t), np.sin(t)])
    ax.plot(*np.c_[a, b], color=P.edge("dna"), lw=1.0, zorder=3)
bio.label(ax, (3.4, 5.6), "gel bead", size="small", color=P.on_fill(), zorder=5)
bio.cell(ax, (6.5, 6.9), 1.0, 0.85, kind="animal")
bio.label(ax, (6.5, 5.0), "cell (lysed)", size="small")
for k in range(4):
    x0 = 5.4 + 0.45 * k
    ax.plot([x0, x0 + 0.35], [3.2 + 0.1 * k, 3.4 + 0.1 * k], color=P.edge("rna"), lw=1.4, zorder=4)
bio.label(ax, (6.0, 2.7), "mRNA", size="tiny")
bio.label(ax, (4.6, 9.4), "one droplet (GEM)", size="small", color=P.on_fill())

# B: bead oligo
bio.panel(ax, "B", (9.6, 10.8))
segs = [("bead", 1.0, "highlight"), ("read 1 primer", 2.6, "neutral"), ("cell barcode 16 nt", 3.2, "dna"),
        ("UMI 12 nt", 2.2, "protein"), ("poly(dT) 30 nt", 2.6, "enzyme")]
x = 10.2
y = 8.0
ends = []
for name, w, tok in segs:
    bio.box(ax, (x + w / 2, y), w - 0.08, 0.9, token=tok, text=name, size="tiny", radius=0.08)
    ends.append(x + w); x += w
# mRNA annealed to poly(dT)
x0 = ends[-2]
ax.plot([x0, x0 + 8.0], [y - 1.1, y - 1.1], color=P.edge("rna"), lw=2.2)
bio.label(ax, (x0 + 1.3, y - 1.55), "AAAA...3'", size="tiny")
bio.label(ax, (x0 + 7.6, y - 1.55), "5' cap", size="tiny")
bio.label(ax, (x0 + 4.3, y - 1.55), "mRNA", size="tiny", italic=False)
# cDNA and TSO
ax.plot([x0, x0 + 8.0], [y - 2.4, y - 2.4], color=P.edge("dna"), lw=2.2)
bio.box(ax, (x0 + 8.9, y - 2.4), 1.7, 0.7, token="neutral", text="TSO", size="tiny", radius=0.08)
bio.label(ax, (x0 + 4.0, y - 2.9), "first-strand cDNA, copied by reverse transcription", size="tiny")
bio.arrow(ax, (x0 + 0.5, y - 3.4), (x0 + 7.5, y - 3.4), kind="process", lw=1.0, head=0.18)

# C: library molecule
bio.panel(ax, "C", (9.6, 3.6))
lib = [("P5", 1.1, "neutral"), ("read 1", 1.6, "neutral"), ("barcode", 1.9, "dna"), ("UMI", 1.4, "protein"),
       ("dT", 1.0, "enzyme"), ("cDNA insert (3' end of transcript)", 6.4, "rna"), ("read 2 primer", 2.2, "neutral"),
       ("i7 index", 1.6, "highlight"), ("P7", 1.1, "neutral")]
x = 10.2; y = 2.0
pos = {}
for name, w, tok in lib:
    bio.box(ax, (x + w / 2, y), w - 0.08, 0.8, token=tok, text=name, size="tiny", radius=0.08)
    pos[name] = (x, x + w); x += w
bio.arrow(ax, (pos["read 1"][0] + 0.2, y + 0.9), (pos["UMI"][1], y + 0.9), kind="process", lw=1.0, head=0.18)
bio.label(ax, ((pos["read 1"][0] + pos["UMI"][1]) / 2, y + 1.35), "read 1: 28 nt (barcode + UMI)", size="tiny")
bio.arrow(ax, (pos["read 2 primer"][0] - 0.1, y - 0.9), (pos["read 2 primer"][0] - 4.0, y - 0.9), kind="process", lw=1.0, head=0.18)
bio.label(ax, (pos["read 2 primer"][0] - 2.0, y - 1.35), "read 2: about 90 nt of cDNA", size="tiny")
bio.label(ax, ((pos["i7 index"][0] + pos["i7 index"][1]) / 2, y - 0.9), "sample index", size="tiny")
