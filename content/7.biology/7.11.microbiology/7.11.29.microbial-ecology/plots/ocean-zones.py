"""The vertical zones of the open ocean and the abundance of Bacteria and Archaea with depth.

A: schematic depth zones (not to scale: each zone is given equal height): epipelagic (sunlit, 0-200 m),
mesopelagic (twilight, 200-1000 m), bathypelagic (1000-4000 m), abyssopelagic (4000-6000 m) and hadal
(trenches, to about 11 000 m); hydrostatic pressure rises by about 0.1 MPa (1 atm) per 10 m; typical light,
temperature and characteristic microbial groups of each zone.
B: cell numbers per millilitre of Bacteria and Archaea at six depths in the North Pacific, counted by FISH
(data from Madigan et al. (2019), after Karner et al. (2001)); the archaeal fraction rises from about 10% at
the surface to about half in the deep water.
"""
import numpy as np
from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(26.0, 13.0)

# A: zones ------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.3, 12.8))
zones = [  # name, depth range, conditions, microbes, token
    ("Epipelagic", "0–200 m", "light; 5–30 °C; nutrients low",
     [("Prochlorococcus, Synechococcus,", True), ("Pelagibacter, Roseobacter", True), ("(SAR11 and Roseobacter clades), diatoms", False)], "x"),
    ("Mesopelagic", "200–1000 m", "twilight; oxygen minimum zones",
     [("ammonia-oxidizing archaea, SAR11, SAR202;", False), ("anammox and denitrifiers in OMZs", False)], "x"),
    ("Bathypelagic", "1000–4000 m", "dark; 2–4 °C; 10–40 MPa",
     [("archaea up to half of the cells;", False), ("particle-attached heterotrophs", False)], "x"),
    ("Abyssopelagic", "4000–6000 m", "dark; ~2 °C; 40–60 MPa", [("piezotolerant and piezophilic bacteria", False)], "x"),
    ("Hadal", "6000–11 000 m", "trenches; up to 110 MPa",
     [("obligate piezophiles:", False), ("Colwellia, Moritella, Shewanella, Psychromonas", True)], "x"),
]
x0, w, ytop, hz = 1.2, 12.6, 11.8, 2.05
for i, (name, rng, cond, mic, tok) in enumerate(zones):
    yc = ytop - (i + 0.5) * hz
    strength = 0.25 + 0.12 * i
    ax.add_patch(FancyBboxPatch((x0, yc - hz / 2), w, hz, boxstyle="square,pad=0",
                                         facecolor=P.mix(P.surface(), P.fill("dna"), min(0.85, strength)),
                                         edgecolor=P.muted(), lw=0.6, zorder=2))
    bio.label(ax, (x0 + 0.2, yc + 0.45), name, size="small", bold=True, ha="left", zorder=5)
    bio.label(ax, (x0 + 0.2, yc - 0.05), rng, size="tiny", ha="left", zorder=5)
    bio.label(ax, (x0 + 0.2, yc - 0.5), cond, size="tiny", ha="left", color=P.muted(), zorder=5)
    for j, (txt, it) in enumerate(mic):
        bio.label(ax, (x0 + 5.0, yc + 0.2 * (len(mic) - 1) - 0.4 * j), txt, size="tiny", ha="left", italic=it, zorder=5)
bio.arrow(ax, (x0 + w + 0.4, ytop), (x0 + w + 0.4, ytop - 5 * hz), kind="process", color=P.muted())
bio.label(ax, (x0 + w + 0.7, ytop - 2.5 * hz), "depth, pressure", size="tiny", rotation=-90, color=P.muted())
bio.label(ax, (x0 + w / 2, ytop + 0.45), "sea surface", size="tiny", color=P.muted())

# B: cell numbers -----------------------------------------------------------------------------------
bio.panel(ax, "B", (16.2, 12.8))
depth = np.array([5, 100, 500, 1000, 2000, 5000])
arch = np.array([3e4, 3e4, 2e4, 7e3, 5e3, 4e3])
bact = np.array([3e5, 2e5, 3e4, 1e4, 3e3, 4e3])
pb = quant.Plot(ax, (18.2, 1.4, 7.0, 10.0), xlim=(1e3, 1e6), ylim=(5000, 5), xlog=True, ylog=True,
                xlabel="cells / mL", ylabel="depth / m",
                xticks=[(1e3, "10³"), (1e4, "10⁴"), (1e5, "10⁵"), (1e6, "10⁶")],
                yticks=[5, 10, 100, 1000, 5000], grid=True)
pb.line(bact, depth, "bacterium", lw=1.8)
pb.points(bact, depth, "bacterium")
pb.line(arch, depth, "atp", lw=1.8)
pb.points(arch, depth, "atp")
pb.text(3e5, 7.5, "Bacteria", token="bacterium", ha="left")
pb.text(3.2e4, 7.5, "Archaea", token="atp", ha="left")
for d, a, b in zip(depth, arch, bact):
    pb.text(1.1e3, d, f"{100 * a / (a + b):.0f}%", ha="left", va="bottom", color=P.muted())
pb.text(1.1e3, 2.6, "archaeal share", ha="left", va="bottom", color=P.muted())
