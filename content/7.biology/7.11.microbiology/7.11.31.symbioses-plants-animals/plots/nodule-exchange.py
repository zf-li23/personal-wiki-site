"""A: the signal exchange that starts a legume root nodule. B: exchange of metabolites between an infected
nodule cell and a symbiosome (schematic)."""
import numpy as np
from matplotlib.patches import Ellipse, FancyBboxPatch
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26, 11)

# ---------------- A: signalling steps
bio.panel(ax, "A", (0.2, 10.8))
bio.label(ax, (2.6, 10.3), "Rhizobium", italic=True, size="small")
bio.label(ax, (8.6, 10.3), "legume root hair", size="small")
ax.plot([5.6, 5.6], [1.0, 9.9], color=P.muted(), lw=0.8, ls=(0, (3, 2)), zorder=2)
steps_b = [(8.9, "flavonoids\n(root exudate)", None), (7.3, "NodD active", "protein"),
           (5.7, "nod genes\ntranscribed", "dna"), (4.1, "Nod factor\n(lipochitooligosaccharide)", "carbohydrate")]
bio.box(ax, (2.6, 8.9), 3.6, 1.1, "metabolite", "flavonoid binds NodD", size="small")
bio.box(ax, (2.6, 7.0), 3.6, 1.1, "dna", "nodD activates nod genes", size="small", italic=False)
bio.box(ax, (2.6, 5.1), 3.6, 1.1, "enzyme", "NodABC + host-specific\nNod proteins", size="small")
bio.box(ax, (2.6, 3.2), 3.6, 1.1, "carbohydrate", "Nod factor secreted", size="small")
for y0, y1 in ((8.35, 7.55), (6.45, 5.65), (4.55, 3.75)):
    bio.arrow(ax, (2.6, y0), (2.6, y1), kind="process", head=0.18)
bio.box(ax, (8.6, 8.9), 3.6, 1.1, "plant", "flavonoids released", size="small")
bio.arrow(ax, (6.8, 8.9), (4.4, 8.9), kind="process", head=0.18)
bio.box(ax, (8.6, 6.4), 3.6, 1.1, "receptor", "LysM receptors\nNFR1/NFR5", size="small")
bio.arrow(ax, (4.4, 3.2), (6.8, 6.2), kind="process", head=0.18)
bio.box(ax, (8.6, 4.5), 3.6, 1.1, "ca", "nuclear Ca²⁺ spiking", size="small")
bio.box(ax, (8.6, 2.6), 3.6, 1.1, "plant", "root-hair curling,\ninfection thread,\ncortical division", size="small")
for y0, y1 in ((5.85, 5.05), (3.95, 3.15)):
    bio.arrow(ax, (8.6, y0), (8.6, y1), kind="process", head=0.18)
bio.label(ax, (5.6, 0.6), "specificity: flavonoid–NodD and Nod factor–receptor", size="tiny", color=P.muted())

# ---------------- B: infected cell and symbiosome
bio.panel(ax, "B", (11.6, 10.8))
ax.add_patch(FancyBboxPatch((12.2, 0.9), 13.3, 9.2, boxstyle="round,pad=0,rounding_size=0.6",
                            facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cell_wall"), lw=2.4, zorder=1))
bio.label(ax, (12.6, 9.6), "infected nodule cell (plant cytoplasm)", size="small", ha="left")
# symbiosome
ax.add_patch(Ellipse((18.6, 5.2), 7.4, 5.0, facecolor=P.fill("vacuole"), edgecolor=P.edge("membrane"), lw=2.0, zorder=3))
bio.label(ax, (18.6, 8.0), "symbiosome membrane (plant origin)", size="tiny", color=P.muted())
bio.label(ax, (17.2, 5.75), "bacteroid", size="small", color=P.on_fill(), zorder=21)
ax.add_patch(Ellipse((18.6, 5.0), 5.2, 2.5, facecolor=P.fill("bacterium"), edgecolor=P.edge("bacterium"), lw=1.4, zorder=4))
bio.box(ax, (17.4, 4.8), 1.9, 0.8, "enzyme", "TCA cycle", size="tiny")
bio.box(ax, (19.9, 4.8), 2.0, 0.8, "protein", "nitrogenase", size="tiny")
bio.arrow(ax, (18.4, 4.8), (18.85, 4.8), kind="process", head=0.14, color=P.on_fill())
bio.label(ax, (18.9, 4.15), "e⁻, ATP", size="tiny", color=P.on_fill())
# fluxes
bio.arrow(ax, (13.4, 5.6), (16.3, 5.0), kind="process", head=0.18)
bio.label(ax, (13.4, 6.1), "malate,\nsuccinate", size="tiny", ha="left")
bio.label(ax, (15.0, 4.85), "DctA", size="tiny")
bio.arrow(ax, (21.0, 5.6), (24.2, 7.3), kind="process", head=0.18)
bio.label(ax, (24.1, 7.85), "NH₄⁺ → Gln, Asn\nor ureides (export)", size="tiny", ha="right")
bio.arrow(ax, (24.0, 3.2), (20.6, 4.4), kind="process", head=0.18)
bio.label(ax, (24.3, 2.75), "N₂", size="small", ha="right")
# leghemoglobin buffer
for k, (x, y) in enumerate([(13.4, 2.2), (14.4, 1.9), (15.5, 2.4), (21.4, 2.5), (22.6, 2.9)]):
    bio.molecule(ax, (x, y), token="blood", r=0.23)
bio.label(ax, (14.4, 3.05), "leghemoglobin–O₂", size="tiny")
bio.arrow(ax, (16.0, 2.4), (17.5, 3.4), kind="process", head=0.14, dashed=True)
bio.label(ax, (19.4, 1.3), "free O₂ kept at nM; bound O₂ supplies respiration", size="tiny", color=P.muted())
