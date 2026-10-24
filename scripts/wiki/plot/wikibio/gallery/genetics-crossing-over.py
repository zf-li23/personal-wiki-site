# Crossing over between non-sister chromatids in prophase I, and the four resulting chromatids
import wikibio as bio
from wikibio import genetics as G

fig, ax = bio.canvas(17.6, 5.6)
L, cen = 3.6, 0.32
loci = [(0.14, ("A", "a")), (0.84, ("B", "b"))]
y = 3.0

bio.panel(ax, "A", (0.2, 5.5))
G.homologous_pair(ax, (2.3, y), length=L, centromere=cen, width=0.56, gap=0.5, loci=loci)
bio.label(ax, (2.3, y - L / 2 - 0.45), "Replicated homologues", size="small", va="top")

bio.arrow(ax, (4.0, y), (5.1, y), kind="process")

bio.panel(ax, "B", (5.3, 5.5))
b = G.bivalent(ax, (7.2, y), length=L, centromere=cen, width=0.56, chiasma=0.55, separation=0.75, loci=loci)
bio.callout(ax, b["chiasma"], (8.9, b["chiasma"][1] + 0.9), "Chiasma")
bio.label(ax, (7.2, y - L / 2 - 0.45), "Bivalent with a chiasma", size="small", va="top")

bio.arrow(ax, (9.3, y), (10.4, y), kind="process")
bio.label(ax, (9.85, y + 0.3), "Meiosis I, II", size="tiny")

bio.panel(ax, "C", (10.6, 5.5))
blue, pink = "dna", "receptor"
s0 = 0.55
products = [
    ([(0, 1, blue)], ("A", "B"), "Parental"),
    ([(0, s0, blue), (s0, 1, pink)], ("A", "b"), "Recombinant"),
    ([(0, s0, pink), (s0, 1, blue)], ("a", "B"), "Recombinant"),
    ([(0, 1, pink)], ("a", "b"), "Parental"),
]
for i, (segs, alleles, kind) in enumerate(products):
    x = 11.5 + i * 1.65
    G.chromosome(ax, (x, y), length=L, centromere=cen, width=0.56, sister=False, colors=[segs],
                 loci=[(0.14, alleles[0]), (0.84, alleles[1])])
    bio.label(ax, (x, y - L / 2 - 0.45), kind, size="tiny", va="top", color=bio.P.muted() if kind == "Parental" else None)
