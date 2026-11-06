# The triangle of U (U 1935): three diploid Brassica species (genomes A, B, C) and the three
# allotetraploids formed from each pair, with chromosome numbers and the main crop types; for each crop
# the organ enlarged by selection is given in brackets.
import numpy as np

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30, 17)

V = {"A": np.array([15.0, 14.2]), "B": np.array([5.2, 3.2]), "C": np.array([24.8, 3.2])}
M = {"AB": (V["A"] + V["B"]) / 2, "AC": (V["A"] + V["C"]) / 2, "BC": (V["B"] + V["C"]) / 2}
for a, b in (("A", "B"), ("A", "C"), ("B", "C")):
    ax.plot(*np.array([V[a], V[b]]).T, color=P.muted(), lw=1.2, zorder=2)
DIP = {"A": ("B. rapa", "AA, 2n = 20", "rna"), "B": ("B. nigra", "BB, 2n = 16", "neutral"),
       "C": ("B. oleracea", "CC, 2n = 18", "dna")}
TET = {"AB": ("B. juncea", "AABB, 2n = 36"), "AC": ("B. napus", "AACC, 2n = 38"), "BC": ("B. carinata", "BBCC, 2n = 34")}
for k, (sp, g, tok) in DIP.items():
    bio.box(ax, V[k], 4.4, 1.7, token=tok)
    bio.label(ax, V[k] + (0, 0.35), sp, italic=True, color=P.on_fill())
    bio.label(ax, V[k] - (0, 0.4), g, size="small", color=P.on_fill())
for k, (sp, g) in TET.items():
    bio.box(ax, M[k], 4.6, 1.7, token="plant")
    bio.label(ax, M[k] + (0, 0.35), sp, italic=True, color=P.on_fill())
    bio.label(ax, M[k] - (0, 0.4), g, size="small", color=P.on_fill())

CROPS = {
    "A": (V["A"] + (3.0, 0.4), "left", ["Chinese cabbage (leaf head)", "pak choi (leaf)", "turnip (root)", "oilseed rape (seed)"]),
    "B": (V["B"] + (0, -1.4), "center", ["black mustard (seed)"]),
    "C": (V["C"] + (0, -1.4), "center", ["cabbage (terminal bud)", "Brussels sprouts (axillary buds)",
                                          "cauliflower, broccoli (inflorescence)", "kohlrabi (stem)", "kale, kai-lan (leaf)"]),
    "AB": (M["AB"] + (-2.6, 0.4), "right", ["leaf mustard (leaf)", "zha cai (stem swelling)", "root mustard (root)",
                                            "brown mustard (seed)"]),
    "AC": (M["AC"] + (2.6, 0.4), "left", ["rapeseed, canola (seed)", "rutabaga (root)"]),
    "BC": (M["BC"] + (0, 1.5), "center", ["Ethiopian mustard (seed, leaf)"]),
}
for k, (xy, ha, lines) in CROPS.items():
    down = k in ("B", "C")
    for i, s in enumerate(lines):
        y = xy[1] - 0.55 * i if down or k != "BC" else xy[1] + 0.55 * i
        bio.label(ax, (xy[0], y), s, size="small", ha=ha)
