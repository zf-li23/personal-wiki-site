# Chromosome anatomy (a G-banded metaphase X chromosome), the X ideogram with disease loci, and a karyotype
import wikibio as bio
from wikibio import genetics as G

# Figure 1: anatomy and ideogram
fig, ax = bio.canvas(14.6, 8.2)
bio.panel(ax, "A", (0.3, 8.15))
bands, cen = G.g_bands(G.HUMAN_X)
L = 6.4
top = 7.7
c = G.chromosome(ax, (3.6, top), length=L, centromere=cen, width=1.25, bands=bands, anchor="top")
yc = top - cen * L
bio.callout(ax, (3.6, yc), (6.0, yc), "Centromere")
bio.callout(ax, (3.95, top - 0.04), (6.0, top + 0.1), "Telomere")
bio.callout(ax, (3.95, top - 1.4), (6.0, top - 0.9), "Sister chromatids")
bio.callout(ax, (3.3, top - 1.8), (6.0, top - 0.9), "")
bio.label(ax, (2.3, top - cen * L / 2), "p arm", size="small", ha="right")
bio.label(ax, (2.3, top - (1 + cen) * L / 2), "q arm", size="small", ha="right")
for y0, y1 in ((top - 0.08, yc + 0.12), (yc - 0.12, top - L + 0.08)):
    ax.plot([2.45, 2.45], [y0, y1], color=bio.P.muted(), lw=0.8)
bio.label(ax, (3.6, top - L - 0.35), "Metaphase X chromosome (G-banded)", size="small", va="top")

bio.panel(ax, "B", (8.0, 8.15))
G.ideogram(ax, (11.0, 7.7), G.HUMAN_X, length=6.4, width=0.5, labels="major",
           loci=[("DMD", 31.1, 33.3), ("AR", 67.5, 67.7), ("XIST", 73.8, 73.9), ("F8", 154.8, 155.0)])
bio.label(ax, (11.0, 7.7 - 6.4 - 0.35), "Human X ideogram (about 400 bands)", size="small", va="top")

# Figure 2: karyotype of a boy with Down syndrome (trisomy 21)
fig2, ax2 = bio.canvas(9.9, 8.4)
formula = G.karyotype(ax2, (0.1, 8.3), sex="XY", extra={"21": 1}, highlight={"21"}, scale=0.0092, width=0.28,
                      slot=1.2, row_gap=0.6)
bio.label(ax2, (9.6, 0.9), formula, size="title", bold=True, ha="right")
