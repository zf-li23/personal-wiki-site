# A "property map" of the 20 standard amino acids: residue volume in proteins (Zamyatnin, 1972) against the
# Kyte-Doolittle hydropathy index (1982). Colours: the classes used for alignments (hydrophobic, polar,
# positive, negative); squares mark the aromatic residues. Residues close together on the map are the ones
# most often exchanged by conservative substitutions during evolution. D, N, E, Q and H are displaced slightly
# (by less than 0.4 index units) so that their symbols do not overlap.
import numpy as np
import wikibio as bio
from wikibio import charts as C

vol = {"G": 60.1, "A": 88.6, "S": 89.0, "C": 108.5, "D": 111.1, "P": 112.7, "N": 114.1, "T": 116.1, "E": 138.4,
       "V": 140.0, "Q": 143.8, "H": 153.2, "M": 162.9, "I": 166.7, "L": 166.7, "K": 168.6, "R": 173.4, "F": 189.9,
       "Y": 193.6, "W": 227.8}  # cubic angstrom
kd = {"I": 4.5, "V": 4.2, "L": 3.8, "F": 2.8, "C": 2.5, "M": 1.9, "A": 1.8, "G": -0.4, "T": -0.7, "S": -0.8,
      "W": -0.9, "Y": -1.3, "P": -1.6, "H": -3.2, "E": -3.5, "Q": -3.5, "D": -3.5, "N": -3.5, "K": -3.9, "R": -4.5}
cls = {}
for k, (colour, letters) in bio.P.AMINO_ACID_CLASS.items():
    for ch in letters:
        cls[ch] = colour
aromatic = set("FWYH")
# D, N, E and Q share the index -3.5: spread them slightly so that the symbols do not overlap
nudge = {"D": (-0.35, 0.0), "N": (0.35, 0.0), "E": (-0.35, 0.0), "Q": (0.35, -0.004), "H": (0.2, 0.005)}

fig, ax = bio.canvas(14, 9)
a = C.axes_at(ax, (1.9, 1.5, 11.4, 7.0))
a.axvline(0, color=bio.P.muted(), lw=0.7, ls=(0, (3, 3)))
for ch in vol:
    x, y = kd[ch], vol[ch] / 1000
    dx, dy = nudge.get(ch, (0, 0))
    x, y = x + dx, y + dy
    a.scatter([x], [y], s=330, marker="s" if ch in aromatic else "o", color=cls[ch],
              edgecolors=bio.P.mix(cls[ch], "#000000", 0.35), linewidths=0.8, zorder=4)
    a.text(x, y, ch, ha="center", va="center", fontsize=bio.core.FONT["small"], weight="bold",
           color=bio.P.on_fill(), zorder=5)
a.set_xlim(-5.2, 5.2)
a.set_ylim(0.04, 0.25)
a.text(-5.0, 0.243, "hydrophilic", fontsize=bio.core.FONT["tiny"], color=bio.P.muted())
a.text(5.0, 0.243, "hydrophobic", fontsize=bio.core.FONT["tiny"], color=bio.P.muted(), ha="right")
C.style_axes(a, "hydropathy index (Kyte–Doolittle)", "residue volume / nm$^3$")
