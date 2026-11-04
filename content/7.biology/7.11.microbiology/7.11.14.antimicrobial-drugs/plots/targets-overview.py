# The five main targets of antibacterial drugs in a bacterial cell (schematic, not to scale):
# cell wall synthesis, the cytoplasmic (and outer) membrane, DNA replication and transcription,
# protein synthesis on the 70S ribosome (30S and 50S subunits), and folate synthesis.
# Drug classes (boxes) block their targets (SBGN inhibition bars).
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(22, 12.5)

# cell: wall (outer rim) and membrane (inner rim) around the cytoplasm
x0, y0, W, H = 5.2, 2.2, 11.6, 8.0
ax.add_patch(FancyBboxPatch((x0, y0), W, H, boxstyle="round,pad=0,rounding_size=3.2",
                            facecolor=P.fill("cell_wall"), edgecolor=P.edge("cell_wall"), lw=1.4, zorder=2))
ax.add_patch(FancyBboxPatch((x0 + 0.35, y0 + 0.35), W - 0.7, H - 0.7, boxstyle="round,pad=0,rounding_size=2.9",
                            facecolor=P.fill("lipid_head"), edgecolor=P.edge("lipid_head"), lw=1.2, zorder=3))
ax.add_patch(FancyBboxPatch((x0 + 0.55, y0 + 0.55), W - 1.1, H - 1.1, boxstyle="round,pad=0,rounding_size=2.75",
                            facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=4))
bio.label(ax, (x0 + W / 2, y0 + H + 0.35), "cell wall (peptidoglycan)", size="small", color=P.muted())
bio.label(ax, (x0 + W / 2, y0 + 6.95), "cytoplasmic membrane", size="tiny", color=P.muted())

# nucleoid: circular chromosome with gyrase and RNA polymerase
cx, cy, r = 8.6, 6.7, 1.55
th = np.linspace(0, 2 * np.pi, 300)
ax.plot(cx + r * np.cos(th) + 0.12 * np.sin(9 * th), cy + 0.8 * r * np.sin(th) + 0.1 * np.cos(7 * th),
        color=P.edge("dna"), lw=2.2, zorder=6)
bio.label(ax, (cx, cy), "DNA", size="small", color=P.edge("dna"))
gyr = (cx - 0.9, cy + 1.25)
bio.protein(ax, gyr, 1.3, 0.7, "enzyme", text="gyrase", size="tiny")
rnap = (cx + 1.3, cy - 1.0)
bio.protein(ax, rnap, 1.2, 0.7, "protein", text="RNAP", size="tiny")
bio.strand(ax, (rnap[0] + 0.6, rnap[1] - 0.1), (rnap[0] + 2.3, rnap[1] - 0.6), token="mrna")
bio.label(ax, (rnap[0] + 2.4, rnap[1] - 0.95), "mRNA", size="tiny", color=P.edge("mrna"))

# ribosome
rib = (13.2, 6.1)
bio.ribosome(ax, rib, size=1.6)
bio.label(ax, (rib[0], rib[1] + 0.3), "50S", size="tiny", color=P.on_fill())
bio.label(ax, (rib[0], rib[1] - 0.42), "30S", size="tiny", color=P.on_fill())

# folate pathway
fy = 3.6
steps = [(9.0, "PABA"), (11.3, "DHF"), (13.6, "THF")]
for x, name in steps:
    bio.box(ax, (x, fy), 1.25, 0.55, token="metabolite", text=name, size="tiny")
bio.arrow(ax, (9.65, fy), (10.65, fy), kind="process", lw=1.0, head=0.16)
bio.arrow(ax, (11.95, fy), (12.95, fy), kind="process", lw=1.0, head=0.16)
bio.label(ax, (10.15, fy + 0.45), "DHPS", size="tiny", color=P.muted())
bio.label(ax, (12.45, fy + 0.45), "DHFR", size="tiny", color=P.muted())
bio.label(ax, (14.75, fy), "nucleotides", size="tiny", ha="left", color=P.muted())

# drug boxes and inhibition arrows (from the box edge facing the target)
def drug(xy, text, w, h, side, target, bend=0.0):
    bio.box(ax, xy, w, h, token="drug", text=text, size="tiny", radius=0.12)
    x, y = xy
    start = {"r": (x + w / 2, y), "l": (x - w / 2, y), "b": (x, y - h / 2), "t": (x, y + h / 2)}[side]
    bio.arrow(ax, start, target, kind="inhibition", lw=1.2, bend=bend, zorder=16)


drug((2.4, 10.4), "Wall synthesis\nβ-lactams, glycopeptides,\nbacitracin, fosfomycin", 4.3, 1.25, "r", (x0 + 1.6, y0 + H - 0.9))
drug((2.4, 3.6), "Membranes\npolymyxins (LPS),\ndaptomycin", 3.6, 1.2, "r", (x0 + 0.45, y0 + 2.0))
drug((8.6, 11.6), "DNA gyrase / topo IV\nquinolones", 3.6, 0.95, "b", (gyr[0], gyr[1] + 0.35))
drug((2.4, 7.0), "RNA polymerase\nrifamycins", 3.0, 0.95, "r", (rnap[0] - 0.6, rnap[1]), bend=-0.2)
drug((19.4, 9.2), "50S subunit\nmacrolides, chloramphenicol,\nlincosamides, oxazolidinones", 4.6, 1.35, "l", (rib[0] + 0.75, rib[1] + 0.35))
drug((19.4, 6.0), "30S subunit\naminoglycosides,\ntetracyclines", 3.4, 1.2, "l", (rib[0] + 0.62, rib[1] - 0.4))
drug((19.4, 2.6), "Folate synthesis\nsulfonamides (DHPS)\ntrimethoprim (DHFR)", 3.8, 1.25, "l", (12.45, fy - 0.05), bend=0.25)
ax.set_ylim(1.3, 12.5)
