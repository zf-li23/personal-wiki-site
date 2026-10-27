# Two functions of the ER membrane. A: phospholipid synthesis. Enzymes with their active sites in the cytosol
# join two acyl-CoAs to glycerol 3-phosphate and add the head group, so new phospholipids (highlighted heads)
# appear only in the cytosolic leaflet; an ER scramblase (an energy-independent lipid scramblase) equilibrates
# them between the leaflets, so that the bilayer grows symmetrically. B: the ER as a Ca2+ store. SERCA
# (a P-type ATPase, 2 Ca2+ per ATP) pumps Ca2+ into the lumen (free ~0.1-0.8 mM; cytosol ~0.1 uM), where
# low-affinity binding proteins (calreticulin; calsequestrin in the sarcoplasmic reticulum) buffer it; IP3
# receptors and ryanodine receptors are the release channels.
import numpy as np
import wikibio as bio
from wikibio import cellbio as cb

fig, ax = bio.canvas(22, 8.0)
P = bio.P

# ---- A ------------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.2, 7.9))
y = 4.2
cb.sides(ax, (0.5, 10.3), y, half=0.42, top="ER lumen", bottom="Cytosol", height=(2.9, 3.1), top_token="er")
q, nrm = bio.bilayer(ax, [(0.5, y), (10.3, y)])
new = [3, 4, 5, 6, 7, 9]
for k in new:  # freshly made lipids in the cytosolic leaflet
    p = q[k] - nrm[k] * 0.365
    ax.add_patch(bio.core.Circle(p, 0.09, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.6, zorder=8))
for k in (38, 41):  # some already moved to the lumenal leaflet
    p = q[k] + nrm[k] * 0.365
    ax.add_patch(bio.core.Circle(p, 0.09, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.6, zorder=8))
bio.protein(ax, (2.0, y - 1.25), 2.7, 0.8, "enzyme", text="acyltransferases")
bio.label(ax, (1.9, y - 2.25), "glycerol 3-P + 2 acyl-CoA\n→ phosphatidate → PC, PE, PS", size="tiny")
bio.arrow(ax, (2.6, y - 0.85), (3.8, y - 0.5), kind="process", bend=0.15)
sx = 7.3
bio.protein(ax, (sx, y), 0.85, 1.25, "protein", text="")
bio.label(ax, (sx, y - 1.05), "scramblase", size="small")
bio.arrow(ax, (sx - 1.0, y - 0.45), (sx - 0.25, y + 0.55), kind="process", bend=0.25)
bio.arrow(ax, (sx + 0.25, y + 0.55), (sx + 1.0, y - 0.45), kind="process", bend=0.25)
bio.label(ax, (5.4, 1.5), "new lipids enter the cytosolic leaflet only", size="tiny", color=P.muted())

# ---- B ------------------------------------------------------------------------------------------------
bio.panel(ax, "B", (11.0, 7.9))
cb.sides(ax, (11.4, 21.6), y, half=0.37, top="ER lumen: free Ca²⁺ 0.1–0.8 mM", bottom="Cytosol: ~0.1 µM",
         height=(2.9, 3.1), top_token="er")
from wikibio import traffic as T
T.band(ax, [(11.4, y), (21.6, y)], thickness=0.74, token="membrane", zorder=5)
atp = cb.pump(ax, 13.4, y, text=None)
bio.label(ax, (13.4, y - 2.15), "SERCA", size="small", bold=True)
cb.flux(ax, 13.4 - 0.375, y - 1.3, y + 1.2, species=[("ca", 2)])
bio.label(ax, atp + (0.1, -0.6), "ATP → ADP", size="tiny", ha="left")
cb.channel(ax, 17.0, y, token="receptor")
bio.label(ax, (17.0, y - 1.95), "IP₃ receptor", size="small", bold=True)
cb.flux(ax, 17.0, y + 1.3, y - 1.4, species=[("ca", 3)])
bio.molecule(ax, (16.25, y - 0.95), token="metabolite", text="IP₃", r=0.28)
cb.channel(ax, 20.0, y, token="channel")
bio.label(ax, (20.0, y - 1.95), "Ryanodine receptor", size="small", bold=True)
cb.flux(ax, 20.0, y + 1.3, y - 1.4, species=[("ca", 1)])
for xx, name in ((14.8, "calreticulin"), (18.6, "calsequestrin")):
    bio.protein(ax, (xx, y + 1.9), 1.9, 0.5, "antibody", text=name)
    for j in range(3):
        bio.ion(ax, (xx - 0.35 + 0.35 * j, y + 2.35), "ca", r=0.11, text=False)
