"""The Ran cycle drives nuclear import and export (schematic; cytoplasm above, nucleus below).
Left pore: import of an NLS cargo by importin alpha/beta; Ran-GTP releases the cargo in the nucleus and the
importin beta-Ran-GTP complex returns. Right pore: export of an NES cargo by an exportin bound to Ran-GTP.
Middle pore: NTF2 imports Ran-GDP; RCC1 on chromatin exchanges GDP for GTP. In the cytoplasm RanGAP (with
RanBP1/RanBP2) triggers GTP hydrolysis, releasing receptors and export cargo. T = Ran-GTP, D = Ran-GDP."""

import wikibio as bio
from wikibio import nuclear as N

P = bio.P
fig, ax = bio.canvas(19.0, 11.0)
Y = 5.4
env = N.envelope(ax, 0.2, 18.8, Y, gap=0.5, pores=[5.0, 9.5, 14.0], pore_width=1.5, ribosomes=False, tint=(5.0, 5.0),
                 lamina_depth=0.0, heterochromatin=False, labels=False)
bio.label(ax, (0.5, 10.6), "Cytoplasm", size="normal", bold=True, ha="left", color=P.muted())
bio.label(ax, (0.5, 0.35), "Nucleus", size="normal", bold=True, ha="left", color=P.muted())
up, dn = Y + 1.25, Y - 1.25


def import_complex(x, y):
    N.karyopherin(ax, (x, y + 0.15), 0.5, kind="importin", angle=-90)
    N.karyopherin(ax, (x, y - 0.25), 0.28, kind="importin_a", angle=-90, zorder=14)
    N.cargo(ax, (x, y - 0.62), 0.24, signal=None)


# ---- import (left pore at x = 5.0)
import_complex(3.0, 8.6)
bio.label(ax, (3.0, 9.55), "Importin β · importin α · NLS cargo", size="small", va="bottom")
bio.arrow(ax, (3.5, 7.7), (5.25, up + 0.1), kind="process", bend=0.12)
bio.arrow(ax, (5.3, up), (5.3, dn), kind="process")
# release in the nucleus
N.karyopherin(ax, (3.2, 2.9), 0.5, kind="importin", angle=-90)
N.ran(ax, (3.2, 2.75), "GTP")
bio.label(ax, (3.2, 2.0), "Importin β · Ran-GTP", size="small", va="top")
N.karyopherin(ax, (6.5, 2.75), 0.28, kind="importin_a", angle=-90)
N.cargo(ax, (7.2, 2.4), 0.24, signal="NLS", angle=90)
bio.label(ax, (6.6, 1.75), "importin α + cargo", size="small", va="top")
bio.arrow(ax, (5.3, dn - 0.1), (6.3, 3.3), kind="process", bend=-0.15)
bio.arrow(ax, (5.3, dn - 0.1), (4.0, 3.3), kind="process", bend=0.15)
bio.label(ax, (6.9, 4.35), "Ran-GTP releases\nimportin α + cargo", size="tiny", ha="left")
# return of importin beta with Ran-GTP
bio.arrow(ax, (2.6, 3.45), (4.7, dn), kind="process", bend=-0.25)
bio.arrow(ax, (4.7, dn), (4.7, up), kind="process")
N.karyopherin(ax, (2.2, 6.9), 0.42, kind="importin", angle=-90)
N.ran(ax, (2.2, 6.75), "GTP")
bio.arrow(ax, (4.7, up + 0.05), (2.75, 6.95), kind="process", bend=-0.2)
bio.arrow(ax, (2.5, 7.35), (2.75, 7.95), kind="process")
N.ran(ax, (1.0, 8.2), "GDP")
bio.arrow(ax, (1.8, 7.2), (1.15, 7.95), kind="process")
bio.label(ax, (0.5, 6.4), "RanGAP:\nGTP hydrolysis", size="tiny", ha="left")

# ---- export (right pore at x = 14.0)
N.karyopherin(ax, (16.0, 2.9), 0.5, kind="exportin", angle=-90)
N.ran(ax, (15.82, 2.8), "GTP")
N.cargo(ax, (16.25, 2.72), 0.2, signal="NES", angle=-90)
bio.label(ax, (16.0, 2.0), "Exportin · Ran-GTP · NES cargo", size="small", va="top")
bio.arrow(ax, (15.4, 3.35), (14.3, dn), kind="process", bend=-0.1)
bio.arrow(ax, (14.3, dn), (14.3, up), kind="process")
bio.arrow(ax, (14.3, up + 0.05), (15.4, 7.4), kind="process", bend=-0.1)
N.karyopherin(ax, (16.0, 8.0), 0.5, kind="exportin", angle=-90)
N.ran(ax, (17.5, 8.4), "GDP")
N.cargo(ax, (17.4, 7.5), 0.22, signal="NES", angle=-90)
bio.label(ax, (16.6, 9.0), "Exportin + Ran-GDP + cargo", size="small", va="bottom")
bio.arrow(ax, (15.6, 8.3), (13.7, up), kind="process", bend=0.25)
bio.arrow(ax, (13.7, up), (13.7, dn), kind="process")
bio.label(ax, (12.6, 7.4), "exportin returns", size="tiny", ha="right")
bio.arrow(ax, (13.7, dn - 0.05), (15.3, 3.1), kind="process", bend=0.25)

# ---- Ran-GDP return and the GAP / GEF pair (middle pore at x = 9.5)
bio.box(ax, (9.5, 9.6), 3.6, 0.75, token="neutral", text="RanGAP + RanBP1/2", size="small")
bio.label(ax, (9.5, 10.25), "cytoplasm: Ran-GTP → Ran-GDP", size="tiny", va="bottom", color=P.muted())
N.ran(ax, (9.0, 7.9), "GDP")
bio.protein(ax, (9.55, 7.9), 0.45, 0.35, "metabolite")
bio.label(ax, (9.95, 7.9), "NTF2", size="tiny", ha="left")
bio.arrow(ax, (16.9, 8.6), (10.3, 8.3), kind="process", bend=0.08)
bio.arrow(ax, (1.25, 8.3), (8.7, 8.15), kind="process", bend=-0.1, dashed=True)
bio.arrow(ax, (9.3, 7.5), (9.3, up), kind="process")
bio.arrow(ax, (9.3, up), (9.3, dn), kind="process")
# chromatin with RCC1
ax.plot([8.4, 12.0], [1.3, 1.3], color=P.edge("chromatin"), lw=5, solid_capstyle="round")
for x in (8.8, 9.4, 10.0, 10.6, 11.2, 11.8):
    ax.add_patch(__import__("matplotlib.patches", fromlist=["Circle"]).Circle((x, 1.3), 0.2, facecolor=P.fill("chromatin"),
                                                                              edgecolor=P.edge("chromatin"), lw=0.6, zorder=8))
bio.protein(ax, (9.7, 1.95), 0.8, 0.5, "enzyme", text="RCC1")
bio.label(ax, (11.0, 0.75), "chromatin", size="tiny", color=P.muted())
N.ran(ax, (8.7, 3.4), "GDP")
N.ran(ax, (10.4, 3.4), "GTP")
bio.arrow(ax, (9.3, dn - 0.05), (8.8, 3.7), kind="process")
bio.arrow(ax, (8.95, 3.35), (10.15, 3.35), kind="process")
bio.label(ax, (9.55, 3.05), "GDP → GTP", size="tiny", va="top")
bio.arrow(ax, (10.65, 3.5), (12.2, 3.6), kind="process", bend=-0.1, dashed=True)
bio.label(ax, (12.3, 3.6), "to importins and exportins", size="tiny", ha="left")
