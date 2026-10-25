# Taylor-style Venn diagram of amino acid properties (W. R. Taylor, J. Theor. Biol. 119:205, 1986, with the
# sets of Livingstone and Barton, 1993): three overlapping sets, hydrophobic, polar and small, with each
# standard amino acid (one-letter code) placed in its region. Letters are coloured by the classes used for
# alignments (hydrophobic, polar, positive, negative); the subsets aliphatic, aromatic, tiny and charged are
# listed on the right.
import numpy as np
from matplotlib.patches import Circle
import wikibio as bio

fig, ax = bio.canvas(16, 11.2)
DY = 1.0  # vertical offset of the whole diagram
centres = {"hydrophobic": (5.0, 6.2 + DY), "polar": (9.0, 6.2 + DY), "small": (7.0, 3.0 + DY)}
R = 3.4
tok = {"hydrophobic": "lipid_tail", "polar": "dna", "small": "positive"}
for name, c in centres.items():
    ax.add_patch(Circle(c, R, facecolor="none", edgecolor=bio.P.edge(tok[name]), lw=2.0, zorder=3))
bio.label(ax, (1.9, 10.5), "Hydrophobic", size="normal", bold=True, color=bio.P.edge(tok["hydrophobic"]))
bio.label(ax, (12.1, 10.5), "Polar", size="normal", bold=True, color=bio.P.edge(tok["polar"]))
bio.label(ax, (10.3, 1.3), "Small", size="normal", bold=True, color=bio.P.edge(tok["small"]))

cls = {}
for k, (colour, letters) in bio.P.AMINO_ACID_CLASS.items():
    for ch in letters:
        cls[ch] = colour

regions = {  # letter positions inside the regions
    "I": (3.0, 7.6), "L": (4.0, 8.4), "M": (2.8, 6.0), "F": (3.9, 7.0),                 # hydrophobic only
    "E": (10.8, 7.4), "Q": (11.2, 6.0), "R": (10.0, 8.4),                               # polar only
    "P": (7.0, 1.0),                                                                     # small only
    "H": (6.6, 8.0), "K": (7.4, 8.0), "W": (6.55, 7.1), "Y": (7.45, 7.1),               # hydrophobic and polar
    "A": (4.4, 3.9), "G": (5.3, 3.4), "V": (5.0, 4.6),                                   # hydrophobic and small
    "D": (9.0, 4.6), "N": (9.6, 3.9), "S": (8.7, 3.4),                                   # polar and small
    "C": (6.55, 5.3), "T": (7.45, 5.3),                                                  # all three
}
regions = {k: (x, y + DY) for k, (x, y) in regions.items()}
for ch, xy in regions.items():
    ax.add_patch(Circle(xy, 0.36, facecolor=cls[ch], edgecolor=bio.P.mix(cls[ch], "#000000", 0.35), lw=0.8,
                        zorder=6))
    bio.label(ax, xy, ch, size="normal", bold=True, color=bio.P.on_fill(), zorder=7)

x0 = 12.9
items = [("aliphatic", "I L V"), ("aromatic", "F W Y H"), ("tiny", "A G S C"), ("charged", "D E H K R"),
         ("positive", "H K R"), ("negative", "D E")]
bio.label(ax, (x0, 5.3), "Subsets", size="small", bold=True, ha="left")
for i, (n, letters) in enumerate(items):
    bio.label(ax, (x0, 4.6 - 0.6 * i), f"{n}: {letters}", size="small", ha="left")
