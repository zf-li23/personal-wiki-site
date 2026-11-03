"""Origin of the chimeric gene jingwei in Drosophila by retrotransposition (after Futuyma and Kirkpatrick
2017, Fig. 14.8). A: an Adh mRNA is reverse-transcribed and inserted into intron 3 of a duplicate of Ymp.
B: in jingwei, Ymp exons 1-3 are spliced to the intronless Adh sequence, whose stop codon ends the reading
frame; downstream Ymp exons degenerate."""
from matplotlib.patches import Rectangle
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(22, 8.6)


def exon(x, y, w, token, text=None, faded=False):
    bio.box(ax, (x + w / 2, y), w, 0.55, token, radius=0.06, lw=0.8)
    if faded:
        ax.plot([x + 0.1, x + w - 0.1], [y - 0.2, y + 0.2], color=P.edge("negative"), lw=1.0, zorder=12)
    if text:
        bio.label(ax, (x + w / 2, y), text, size="tiny", color=P.on_fill())


def intron(x0, x1, y):
    ax.plot([x0, x1], [y, y], color=P.muted(), lw=1.2, zorder=5)


bio.panel(ax, "A", (0.2, 8.4))
y = 6.6
bio.label(ax, (0.5, y), "Ymp\nduplicate", size="small", italic=True, ha="left")
xs = [3.0, 5.4, 7.8, 13.6, 16.0]
intron(3.0, 17.2, y)
for k, x in enumerate(xs):
    exon(x, y, 1.2, "positive", str(k + 1))
bio.label(ax, (11.1, y + 0.55), "intron 3", size="tiny", color=P.muted())
# Adh mRNA above
ym = 8.0
bio.label(ax, (19.9, ym), r"$\it{Adh}$ mRNA", size="small", ha="left")
bio.box(ax, (16.2, ym), 5.2, 0.45, "protein", radius=0.06, lw=0.8)
bio.label(ax, (16.2, ym), r"$\it{Adh}$ coding sequence", size="tiny", color=P.on_fill())
bio.label(ax, (19.0, ym - 0.03), "AAAA", size="tiny", ha="left", color=P.muted())
bio.arrow(ax, (14.0, ym - 0.3), (11.2, y + 0.35), kind="process", bend=0.2)
bio.label(ax, (14.4, 7.15), "reverse transcription\nand insertion", size="tiny", ha="left", color=P.muted())

bio.panel(ax, "B", (0.2, 4.3))
y = 2.6
bio.label(ax, (0.5, y), "jingwei", size="small", italic=True, ha="left")
intron(3.0, 19.6, y)
for k, x in enumerate(xs[:3]):
    exon(x, y, 1.2, "positive", str(k + 1))
exon(9.4, y, 3.4, "protein", r"$\it{Adh}$")
ax.add_patch(Rectangle((12.82, y - 0.4), 0.18, 0.8, facecolor=P.edge("negative"), edgecolor="none", zorder=13))
bio.label(ax, (12.9, y - 0.75), "stop codon\nfrom " + r"$\it{Adh}$", size="tiny", va="top", color=P.muted())
for x in (15.6, 18.0):
    exon(x, y, 1.2, "neutral", faded=True)
bio.label(ax, (17.4, y + 0.65), r"former $\it{Ymp}$ exons decay", size="tiny", color=P.muted())
bio.label(ax, (7.3, 3.9), r"chimeric open reading frame: $\it{Ymp}$ exons 1-3 + $\it{Adh}$", size="tiny", color=P.muted())
ax.plot([3.0, 13.0], [3.5, 3.5], color=P.muted(), lw=0.8)
bio.arrow(ax, (11.0, 5.6), (11.0, 4.0), kind="process")
bio.label(ax, (11.3, 4.8), "about 2 Myr ago", size="tiny", ha="left", color=P.muted())
