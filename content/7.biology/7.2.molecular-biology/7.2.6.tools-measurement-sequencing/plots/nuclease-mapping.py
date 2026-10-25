# Mapping the 5' end of a transcript by S1 nuclease protection. A: a DNA probe labelled at one 5' end (star)
# and spanning the transcription start site is hybridized to the RNA; S1 nuclease degrades all single-stranded
# nucleic acid, so the probe survives only where the RNA covers it, and the length of the surviving labelled
# fragment is the distance from the label to the 5' end of the RNA. B: the same logic read out on a denaturing
# gel next to a size ladder, for three hypothetical start sites; the band moves with the start site, and a
# transcript that starts upstream of the probe protects the probe over its whole length (full-length band).
import numpy as np
import wikibio as bio
from wikibio import quant as Q

P = bio.P
fig, ax = bio.canvas(20.0, 10.2)


def seg(x0, x1, y, tok, lw=3.4, z=8):
    ax.plot([x0, x1], [y, y], color=P.edge(tok), lw=lw, solid_capstyle="butt", zorder=z)


def star(x, y):
    th = np.linspace(0, 2 * np.pi, 11)
    r = np.where(np.arange(11) % 2 == 0, 0.17, 0.08)
    ax.add_patch(bio.core.Polygon(np.c_[x + r * np.cos(th + np.pi / 2), y + r * np.sin(th + np.pi / 2)],
                                  color=P.edge("highlight"), zorder=14))


bio.panel(ax, "A", (0.1, 10.1))
bio.label(ax, (0.6, 9.75), "S1 nuclease protection: principle", size="normal", bold=True, ha="left")
TSS = 7.0
y = 8.7
bio.label(ax, (0.4, y + 0.7), "1  probe: single-stranded DNA spanning the start site, labelled at the end inside the gene",
          size="small", ha="left")
seg(2.0, 11.0, y, "dna")
star(11.0, y)
bio.label(ax, (11.6, y), "label", size="tiny", ha="left")
ax.plot([TSS, TSS], [9.8, 3.2], color=P.muted(), lw=0.7, ls=(0, (2, 2)), zorder=3)
bio.label(ax, (TSS + 0.15, 9.95), "start site of the transcript", size="tiny", color=P.muted(), ha="left")

y = 6.9
bio.label(ax, (0.4, y + 0.7), "2  hybridize with the RNA, which runs from the start site into the gene",
          size="small", ha="left")
seg(2.0, 11.0, y + 0.14, "dna")
star(11.0, y + 0.14)
seg(TSS, 13.0, y - 0.24, "mrna")
bio.label(ax, (13.4, y - 0.24), "RNA", size="tiny", ha="left", color=P.edge("mrna"))

y = 5.1
bio.label(ax, (0.4, y + 0.7), "3  S1 nuclease removes everything single-stranded", size="small", ha="left")
seg(2.0, TSS, y + 0.14, "neutral", lw=1.0)
seg(13.0, TSS, y - 0.24, "neutral", lw=1.0)
seg(TSS, 11.0, y + 0.14, "dna")
seg(TSS, 11.0, y - 0.24, "mrna")
star(11.0, y + 0.14)

y = 3.2
bio.label(ax, (0.4, y + 0.8), "4  the labelled fragment that survives is measured on a gel", size="small", ha="left")
seg(TSS, 11.0, y, "dna")
star(11.0, y)
Q.bracket(ax, (TSS, y - 0.35), (11.0, y - 0.35), side=-1)
bio.label(ax, (9.0, y - 1.05), "protected length = distance from the label to the 5′ end of the RNA", size="small")

# ---- B: the gel ------------------------------------------------------------------------------------------
bio.panel(ax, "B", (14.2, 10.1))
bio.label(ax, (14.7, 9.75), "Read-out on a denaturing gel", size="normal", bold=True, ha="left")
gx, gy, gw, gh = 15.2, 1.2, 4.3, 7.6
ax.add_patch(bio.core.FancyBboxPatch((gx, gy), gw, gh, boxstyle="round,pad=0,rounding_size=0.1",
                                     facecolor=P.fill("extracellular"), edgecolor=P.edge("neutral"), lw=1.0, zorder=2))
lanes = [("M", None), ("start A", 300), ("start B", 180), ("start C", 90), ("read-\nthrough", 400)]
sizes = [400, 300, 200, 150, 100, 75]


def ypos(n):
    return gy + 0.6 + (gh - 1.2) * (np.log10(n) - np.log10(70)) / (np.log10(450) - np.log10(70))


for k, (name, band) in enumerate(lanes):
    x = gx + 0.45 + k * 0.85
    bio.label(ax, (x, gy + gh + 0.35), name, size="tiny")
    if band is None:
        for n in sizes:
            ax.plot([x - 0.26, x + 0.26], [ypos(n), ypos(n)], color=P.muted(), lw=2.6, solid_capstyle="butt", zorder=6)
            bio.label(ax, (gx - 0.2, ypos(n)), str(n), size="tiny", ha="right", color=P.muted())
    else:
        tok = "highlight" if band == 400 else "dna"
        ax.plot([x - 0.26, x + 0.26], [ypos(band), ypos(band)], color=P.edge(tok), lw=3.2, solid_capstyle="butt", zorder=6)
bio.label(ax, (gx + gw / 2, gy - 0.45), "nt", size="tiny", color=P.muted())
bio.label(ax, (14.7, 0.5), "full-length probe (yellow): transcript starts upstream of the probe", size="tiny", ha="left",
          color=P.muted())
