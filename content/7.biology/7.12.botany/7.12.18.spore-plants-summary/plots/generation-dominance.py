"""Relative size of the gametophyte and the sporophyte in representative land plants (typical length or
height, log scale; order-of-magnitude values). Solid bars: free-living generation; hatched bars: the
generation that depends on the other one (or develops inside the spore wall)."""
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(24, 12)
# (name, gametophyte size m, gametophyte independent?, sporophyte size m, sporophyte independent?)
DATA = [
    (r"$\it{Marchantia}$" "\n(liverwort)", 5e-2, True, 3e-3, False),
    (r"$\it{Polytrichum}$" "\n(moss)", 1.5e-1, True, 8e-2, False),
    (r"$\it{Lycopodium}$" "\n(club moss)", 1e-2, True, 3e-1, True),
    (r"$\it{Selaginella}$" "\n(spike moss)", 5e-4, False, 1e-1, True),
    (r"$\it{Pteridium}$" "\n(bracken fern)", 8e-3, True, 1.5, True),
    (r"$\it{Pinus}$" "\n(pine)", 5e-3, False, 30.0, True),
    ("Angiosperm\n(e.g. an oak)", 1.5e-4, False, 25.0, True),
]
bx = charts.axes_at(ax, (2.6, 2.8, 20.6, 8.2))
x = np.arange(len(DATA))
w = 0.36
cg, cs = charts.line("rna"), charts.line("dna")
for i, (n, g, gi, s, si) in enumerate(DATA):
    bx.bar(i - w / 2, g, w, color=cg if gi else "none", edgecolor=cg, hatch=None if gi else "////", lw=1.2,
           )
    bx.bar(i + w / 2, s, w, color=cs if si else "none", edgecolor=cs, hatch=None if si else "////", lw=1.2,
           )
bx.set_yscale("log")
bx.set_ylim(5e-5, 100)
bx.set_xticks(x)
bx.set_xticklabels([d[0] for d in DATA], fontsize=8)
bx.set_yticks([1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 100])
bx.set_yticklabels(["0.1 mm", "1 mm", "1 cm", "10 cm", "1 m", "10 m", "100 m"])
charts.style_axes(bx, ylabel="typical size")
from matplotlib.patches import Patch
bx.legend(handles=[Patch(color=cg, label="Gametophyte (n)"), Patch(color=cs, label="Sporophyte (2n)")], frameon=False,
          fontsize=8, loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=2)
bx.axvline(1.5, color=P.muted(), lw=0.8, ls=":")
bx.text(0.5, 40, "gametophyte dominant", ha="center", fontsize=8, color=P.ink())
bx.text(4.0, 40, "sporophyte dominant", ha="center", fontsize=8, color=P.ink())
bio.label(ax, (12.9, 0.9), "hatched: dependent on the other generation or inside the spore wall", size="small", color=P.muted())
