# Reverse genetics for the three classes of RNA genome: how infectious virus is recovered from cloned DNA.
# A: a (+) strand genome (poliovirus) - cloned cDNA is infectious, as is RNA transcribed from it in vitro.
# B: a segmented (-) strand genome (influenza virus) - eight plasmids, each read by host RNA polymerase I
#    (making vRNA) and RNA polymerase II (making mRNA). C: a nonsegmented (-) strand genome - a plasmid for
# the full-length (+) strand antigenome plus plasmids for N, P and L, all driven by bacteriophage T7 polymerase.
import numpy as np
import wikibio as bio
from wikibio import genetics as G

P = bio.P
fig, ax = bio.canvas(18, 12.2)


def cellbox(center, w=2.3, h=1.9, text="Cultured cells"):
    bio.cell(ax, center, w / 2, h / 2, kind="animal")
    bio.label(ax, (center[0], center[1] - h / 2 - 0.42), text, size="small")
    return center


def virus_out(at, text="Infectious virus"):
    bio.virus(ax, at, 0.42, kind="enveloped", spikes=10)
    bio.label(ax, (at[0], at[1] - 0.95), text, size="small", bold=True)


def title(xy, text):
    bio.label(ax, xy, text, size="title", bold=True)


# --- A  (+) strand RNA: poliovirus ------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 12.0))
title((4.6, 11.8), "(+) strand RNA genome")
G.plasmid(ax, (1.9, 9.6), 1.15, 9000, name="cDNA\nclone", backbone_token="neutral",
          features=[{"name": "poliovirus cDNA", "start": 600, "end": 8000, "token": "dna", "strand": 1, "inside": False},
                    {"name": "T7", "start": 300, "end": 600, "token": "positive", "strand": 1}])
bio.arrow(ax, (3.2, 10.1), (5.1, 10.5), kind="process", bend=0.12)
bio.label(ax, (4.1, 10.85), "in vitro\ntranscription", size="tiny", color=P.muted())
bio.strand(ax, (5.5, 10.5), (8.2, 10.5), cap=False, polya=True)
bio.label(ax, (6.85, 10.9), "(+) strand RNA", size="small", color=P.edge("rna"))
bio.arrow(ax, (3.2, 9.2), (5.3, 8.3), kind="process", bend=-0.1)
bio.label(ax, (3.9, 8.5), "transfection", size="tiny", color=P.muted())
bio.arrow(ax, (8.3, 10.2), (6.9, 9.0), kind="process", bend=0.12)
cellbox((6.2, 8.1))
bio.arrow(ax, (7.5, 8.1), (8.6, 8.1), kind="process")
virus_out((9.3, 8.1))
bio.label(ax, (4.6, 6.2), "The genome is mRNA: once inside, it is translated and starts the cycle",
          size="small", color=P.muted())

# --- B  segmented (-) strand RNA: influenza virus ----------------------------------------------------------
bio.panel(ax, "B", (10.3, 12.0))
title((14.2, 11.8), "Segmented (−) strand genome")
parts = G.construct(ax, 11.0, 9.9, [("promoter", "Pol I"), {"kind": "cds", "text": "segment", "token": "dna", "width": 1.5},
                                    ("terminator", "Pol I"), ("promoter", "Pol II"), ("polya", "")], unit=0.52, gap=0.34)
bio.label(ax, (14.2, 10.75), "one plasmid per segment  (× 8)", size="small")
bio.label(ax, (11.6, 9.05), "(−) vRNA", size="tiny", color=P.edge("dna"))
bio.label(ax, (15.3, 9.05), "mRNA", size="tiny", color=P.edge("rna"))
bio.arrow(ax, (13.0, 8.8), (13.0, 8.0), kind="process")
cellbox((13.0, 7.1), text="Transfected cells")
bio.arrow(ax, (14.3, 7.1), (15.4, 7.1), kind="process")
virus_out((16.1, 7.1))
bio.label(ax, (14.2, 5.25), "vRNA and mRNA are made from the same cloned DNA, so\nnucleocapsids assemble and the cycle starts",
          size="small", color=P.muted())

# --- C  nonsegmented (-) strand RNA: rescue from an antigenome ---------------------------------------------
bio.panel(ax, "C", (0.1, 5.3))
title((6.0, 5.1), "Nonsegmented (−) strand genome")
y = 3.4
for i, (x, txt, tok) in enumerate([(1.3, "antigenome (+)", "rna"), (5.0, "N", "protein"), (7.2, "P", "protein"), (9.4, "L", "enzyme")]):
    w = 2.6 if i == 0 else 0.9
    G.construct(ax, x, y, [("promoter", "T7"), {"kind": "cds", "text": txt, "token": tok, "width": w}], unit=0.5)
bio.label(ax, (5.6, y + 1.05), "plasmids for the nucleocapsid proteins and the polymerase", size="small")
bio.label(ax, (2.6, y - 0.95), "a full-length (+) strand copy of the genome", size="tiny", color=P.muted())
bio.protein(ax, (12.5, y + 1.0), 2.2, 0.62, "positive", text="T7 RNA polymerase", size="tiny")
bio.label(ax, (12.5, y + 0.45), "from a helper virus\nor a stable cell line", size="tiny", color=P.muted())
bio.arrow(ax, (11.0, y), (12.9, y - 0.6), kind="process", bend=-0.1)
cellbox((14.6, y - 1.1), w=2.4, h=2.0, text="Transfected cells")
bio.arrow(ax, (15.9, y - 1.1), (16.9, y - 1.1), kind="process")
virus_out((17.3, y - 1.1), text="Virus")
bio.label(ax, (6.0, 0.55), "The antigenome is encapsidated by N and copied by L–P into (−) strand genomes",
          size="small", color=P.muted())
