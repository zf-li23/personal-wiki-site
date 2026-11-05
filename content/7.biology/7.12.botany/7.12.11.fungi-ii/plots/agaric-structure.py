"""An agaric basidiocarp in median section (A) and from the side (B), and a transverse section of gills
(C) showing trama, subhymenium and hymenium with basidia and basidiospores."""
import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(30, 10.5)
bio.panel(ax, "A", (0.2, 10.3))
m = plant.mushroom(ax, (5.0, 0.8), 8.0, volva=True)
for key, xy, txt in [("cuticle", (9.6, 9.6), "Pileus (cap) and cuticle"), ("context", (0.4, 9.2), "Context (flesh)"),
                     ("lamella", (9.6, 6.4), "Lamella (gill)"), ("annulus", (9.6, 5.2), "Annulus (ring)"),
                     ("stipe", (9.6, 3.6), "Stipe"), ("volva", (9.6, 1.6), "Volva"), ("mycelium", (1.2, 0.5), "Mycelial strands")]:
    if key in m:
        bio.callout(ax, m[key], xy, txt)
bio.panel(ax, "B", (13.6, 10.3))
plant.mushroom(ax, (16.0, 0.8), 6.0, section=False, annulus=True, volva=True)
bio.label(ax, (16.0, 8.6), "Side view", size="small")
bio.panel(ax, "C", (19.4, 10.3))
g = plant.gill_section(ax, (19.8, 1.2, 29.6, 8.6), gills=3)
for key, xy, txt in [("context", (24.7, 9.6), "Context"), ("trama", (19.6, 0.5), "Trama"),
                     ("basidium", (29.0, 0.5), "Hymenium: basidia"), ("spore", (26.0, 0.5), "Basidiospores"), ("subhymenium", (29.4, 9.6), "Subhymenium")]:
    if key in g:
        bio.callout(ax, g[key], xy, txt)
