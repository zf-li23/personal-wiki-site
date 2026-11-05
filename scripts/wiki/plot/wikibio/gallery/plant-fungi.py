# Demo: fungal primitives of wikibio.plant (hyphae, asci, basidia, ascocarps, mushroom, gill section).
import numpy as np

import wikibio as bio
from wikibio import plant

fig, ax = bio.canvas(24, 16)
# hyphae
t = np.linspace(0, 1, 30)
plant.hypha(ax, np.c_[0.5 + 5 * t, 15 + 0.3 * np.sin(4 * t)], septa=0.9, nuclei=1)
plant.hypha(ax, np.c_[0.5 + 5 * t, 14 + 0.3 * np.sin(4 * t)], septa=None)
h = plant.hypha(ax, np.c_[0.5 + 5 * t, 13 + 0.3 * np.sin(4 * t)], septa=1.1, nuclei=2, clamps=True)
bio.label(ax, (6, 15), "Septate", ha="left", size="small")
bio.label(ax, (6, 14), "Coenocytic", ha="left", size="small")
bio.label(ax, (6, 13), "Dikaryotic, clamps", ha="left", size="small")
bio.callout(ax, h["clamps"][1], (2.5, 11.8), "Clamp connection")
# ascus stages
for i, st in enumerate(plant.ASCUS_STAGES[:5]):
    plant.ascus(ax, (9 + i * 0.9, 11.5), 3.0, stage=st)
plant.ascus(ax, (13.8, 11.5), 3.0, arrangement="biseriate", bitunicate=True)
plant.ascus(ax, (14.7, 11.5), 3.0, operculum=True)
plant.paraphysis(ax, (15.5, 11.5), 3.0)
# basidium stages
for i, st in enumerate(["dikaryotic", "karyogamy", "meiosis", "sterigmata", "mature"]):
    plant.basidium(ax, (17 + i * 1.4, 11.5), 2.2, stage=st)
# ascocarps
for i, k in enumerate(["apothecium", "perithecium", "cleistothecium", "pseudothecium"]):
    a = plant.ascocarp(ax, (2.5 + i * 5, 7.5), 4.0, kind=k, stalk=(i == 0))
    bio.label(ax, (2.5 + i * 5, 4.4), k.capitalize(), size="small")
# mushroom and gills
m = plant.mushroom(ax, (21.5, 0.8), 6.0, volva=True)
for key, xy in [("pileus", (24, 6.8)), ("lamella", (24, 4.6)), ("annulus", (24, 3.8)), ("stipe", (24, 2.6)),
                ("volva", (24, 1.2)), ("context", (18.2, 6.8))]:
    bio.callout(ax, m[key], xy, key.capitalize())
plant.mushroom(ax, (16.5, 0.8), 4.0, section=False, annulus=False)
g = plant.gill_section(ax, (0.5, 0.3, 12, 3.8), gills=3)
bio.callout(ax, g["basidium"], (13, 2.5), "Basidium")
bio.callout(ax, g["trama"], (13, 3.5), "Trama")
