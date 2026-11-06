# Radial path of ions from the soil solution to the xylem (schematic, one radial file of cells).
# An ion can enter the symplast at the epidermis (H+-coupled carriers and channels in the plasma membrane,
# energized by the H+-ATPase) and move from cell to cell through plasmodesmata (orange), or diffuse in the
# cell walls of the epidermis and cortex (apoplast, blue dashed) as far as the endodermis, where the
# Casparian strip (red) blocks the apoplast so that it must cross a plasma membrane there. Inside the stele it
# diffuses symplastically to the pericycle and xylem parenchyma and is released into the dead xylem vessels
# (xylem loading): K+ through the outward-rectifying channel SKOR, anions through anion channels, B and other
# nutrients by specific efflux transporters; HKT1 in the xylem parenchyma retrieves Na+ from the xylem sap.
# Ions in the vessel then move to the shoot with the transpiration stream (and generate root pressure).
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30.0, 11.0)


def cell(x, w, token="cytoplasm", wall="cell_wall", y=3.0, h=4.6, lw=1.6):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.3", facecolor=P.fill(token),
                                edgecolor=P.edge(wall), lw=lw, zorder=5))


names = ["Epidermis", "Cortex", "Cortex", "Endodermis", "Pericycle", "Xylem\nparenchyma", "Xylem vessel"]
xs = [3.2, 6.6, 9.9, 13.2, 16.0, 18.7, 21.6]
ws = [3.0, 3.0, 3.0, 2.4, 2.4, 2.6, 3.6]
toks = ["cytoplasm", "cytoplasm", "cytoplasm", "golgi", "metabolite", "metabolite", "extracellular"]
ax.add_patch(Rectangle((0.2, 2.2), 2.8, 6.2, facecolor=P.fill("extracellular"), edgecolor="none", zorder=1))
bio.label(ax, (1.6, 8.8), "Soil solution", size="small", bold=True)
for x, w, t, n in zip(xs, ws, toks, names):
    if n == "Xylem vessel":
        cell(x, w, token="extracellular", wall="cell_wall", lw=3.0)
    else:
        cell(x, w, token=t)
    bio.label(ax, (x + w / 2, 8.3), n, size="small")
bio.label(ax, (19.3, 10.3), "Stele", size="small", bold=True, color=P.muted())
ax.plot([16.0, 25.2], [9.85, 9.85], color=P.muted(), lw=0.8)
# root hair
ax.add_patch(FancyBboxPatch((0.6, 6.2), 2.9, 0.8, boxstyle="round,pad=0,rounding_size=0.4", facecolor=P.fill("cytoplasm"),
                            edgecolor=P.edge("cell_wall"), lw=1.6, zorder=4.8))
bio.label(ax, (1.6, 7.4), "root hair", size="tiny", color=P.muted())
# Casparian strip in the radial walls of the endodermis (drawn top and bottom)
for yy in (2.95, 7.55):
    ax.add_patch(Rectangle((13.9, yy - 0.18), 1.0, 0.36, facecolor=P.fill("negative"), edgecolor=P.edge("negative"),
                           lw=0.8, zorder=8))
bio.callout(ax, (14.4, 2.8), (16.2, 1.6), "Casparian strip")

# apoplastic path in the wall at the bottom of the file
ya = 2.75
ax.plot([0.8, 13.7], [ya, ya], color=P.edge("dna"), lw=2.2, ls=(0, (3, 2)), zorder=9)
bio.label(ax, (8.0, 2.35), "apoplast (cell walls): diffusion and mass flow", size="tiny", color=P.edge("dna"))
bio.arrow(ax, (13.2, ya), (13.75, 3.6), kind="process", color=P.edge("dna"), dashed=True)
bio.label(ax, (10.6, 1.65), "blocked → must enter a cell", size="tiny", color=P.edge("negative"))

# symplastic path
ys = 5.3
pts = [1.2, 4.7, 8.1, 11.4, 14.4, 17.2, 20.0]
ax.plot(pts, [ys] * len(pts), color=P.edge("rna"), lw=2.4, zorder=9)
for x in (6.6, 9.9, 13.2, 16.0, 18.7):
    ax.plot([x - 0.06, x + 0.06], [ys, ys], color=P.ink(), lw=5, zorder=9.5, solid_capstyle="butt")
bio.label(ax, (8.1, 5.75), "symplast via plasmodesmata", size="tiny", color=P.edge("rna"))

# uptake at the epidermis plasma membrane
bio.label(ax, (4.7, 4.3), "uptake: H⁺-ATPase,\nsymporters, channels", size="tiny")
for (yy, sp) in ((6.6, "k"), (4.9, "cl")):
    bio.ion(ax, (2.6, yy), sp, r=0.16, text=False, zorder=12)
bio.arrow(ax, (2.8, 6.6), (3.8, 6.0), kind="process", zorder=12)
# xylem loading
bio.arrow(ax, (20.0, ys), (22.4, ys), kind="process", color=P.edge("rna"), zorder=12)
bio.label(ax, (21.0, 6.75), "SKOR (K⁺)\nanion channels", size="tiny")
bio.arrow(ax, (22.4, 4.0), (20.2, 4.0), kind="process", color=P.edge("na"), zorder=12)
bio.label(ax, (21.0, 3.45), "HKT1 retrieves Na⁺", size="tiny", color=P.edge("na"))
bio.arrow(ax, (23.4, 4.0), (23.4, 7.2), kind="process", zorder=12)
bio.label(ax, (27.3, 5.6), "to the shoot in\nthe transpiration\nstream", size="small")
bio.label(ax, (21.2, 0.9), "xylem loading", size="small", bold=True)
ax.plot([18.7, 25.2], [1.35, 1.35], color=P.muted(), lw=0.8)
