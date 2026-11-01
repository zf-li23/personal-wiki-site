# Insert size and adapter read-through for 2 x 150 paired-end reads. A: insert-size distributions of a whole-genome
# library (normal, mean 350, sd 90 nt) and of cell-free DNA (a mononucleosome peak at 167 nt with sd 15, and 10 %
# dinucleosomes at 334 nt). Fragments shorter than 2 x 150 = 300 nt give overlapping mates; fragments shorter than
# 150 nt are read through into the adapter at the 3' end of both reads. The fractions are computed from the
# distributions. B: the three cases for one fragment (insert in colour, adapters grey, reads as arrows).
import numpy as np
from matplotlib.patches import Rectangle
from scipy import stats
import wikibio as bio
from wikibio import charts as C

P = bio.P
L = 150
x = np.arange(20, 701)
wgs = stats.norm(350, 90)
cf = [(0.9, stats.norm(167, 15)), (0.1, stats.norm(334, 25))]


def cdf(t, mix):
    return sum(w * d.cdf(t) for w, d in mix)


fig, ax = bio.canvas(26.0, 9.4)
a = C.axes_at(ax, (1.8, 1.4, 11.0, 6.8))
a.plot(x, wgs.pdf(x), color=C.line("dna"), lw=1.8, label="whole-genome library")
a.plot(x, sum(w * d.pdf(x) for w, d in cf), color=C.line("rna"), lw=1.8, label="cell-free DNA")
a.axvline(L, color=P.edge("negative"), lw=0.9, ls=(0, (3, 2)))
a.axvline(2 * L, color=P.muted(), lw=0.9, ls=(0, (3, 2)))
a.text(L - 6, 0.0205, "read length 150:\nshorter inserts read\ninto the adapter", ha="right", va="top",
       fontsize=bio.core.FONT["tiny"], color=P.edge("negative"))
a.text(2 * L + 6, 0.0205, "2 x 150: shorter inserts\ngive overlapping mates", ha="left", va="top",
       fontsize=bio.core.FONT["tiny"], color=P.muted())
fr = [("WGS", wgs.cdf(L), wgs.cdf(2 * L)), ("cfDNA", cdf(L, cf), cdf(2 * L, cf))]
txt = "\n".join(f"{n}: {100 * r:.1f} % read-through, {100 * o:.0f} % overlap" for n, r, o in fr)
a.text(690, 0.012, txt, ha="right", va="top", fontsize=bio.core.FONT["tiny"], color=P.ink())
a.set_xlim(20, 700)
a.set_ylim(0, 0.026)
a.set_yticks([])
C.style_axes(a, "insert size (nt)", "density")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "A", (0.1, 9.3))

bio.panel(ax, "B", (14.4, 9.3))
s = 0.013  # canvas units per nt
x0 = 16.0
cases = [(450, "insert 450 > 300: no overlap"), (220, "insert 220: mates overlap"), (110, "insert 110 < 150: read-through")]
for k, (ins, lab) in enumerate(cases):
    y = 7.6 - k * 2.6
    ad = 60
    ax.add_patch(Rectangle((x0, y), ad * s, 0.3, facecolor=P.light("neutral"), edgecolor=P.edge("neutral"), lw=0.6))
    ax.add_patch(Rectangle((x0 + ad * s, y), ins * s, 0.3, facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.6))
    ax.add_patch(Rectangle((x0 + (ad + ins) * s, y), ad * s, 0.3, facecolor=P.light("neutral"),
                           edgecolor=P.edge("neutral"), lw=0.6))
    r1a, r1b = x0 + ad * s, x0 + (ad + L) * s
    r2b, r2a = x0 + (ad + ins) * s, x0 + (ad + ins - L) * s
    bio.arrow(ax, (r1a, y + 0.6), (r1b, y + 0.6), kind="process", color=P.edge("positive"), lw=1.6, head=0.15)
    bio.arrow(ax, (r2b, y - 0.3), (r2a, y - 0.3), kind="process", color=P.edge("protein"), lw=1.6, head=0.15)
    bio.label(ax, (x0, y + 1.15), lab, size="small", ha="left")
bio.label(ax, (x0, 0.5), "green: read 1 (forward); purple: read 2 (reverse); grey: adapters", size="tiny", ha="left",
          color=P.muted())
