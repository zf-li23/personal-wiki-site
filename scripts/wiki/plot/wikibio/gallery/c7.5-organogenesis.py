# Organogenesis (wikibio.organogenesis): the heart from the cardiac crescent through the linear tube and looping to
# the four chambers, coloured by origin; a blood island, a primary plexus and a sprouting vessel with its tip
# cell; the dorsal aorta with hemogenic endothelium; the primitive gut tube with its buds; the pharyngeal arches
# and pouches; a seminiferous tubule, the lineages of spermatogenesis and oogenesis, and ovarian follicles.
import wikibio as bio
from wikibio import organogenesis as O

P = bio.P
fig, ax = bio.canvas(30, 34)

for k, st in enumerate(("crescent", "tube", "looping", "chambers")):
    a = O.heart(ax, (3.6 + 7.4 * k, 29.0), 2.3, st)
    bio.label(ax, (3.6 + 7.4 * k, 25.0), st, size="small", color=P.muted())
    if st == "tube":
        bio.callout(ax, a["oft"], (8.5, 33.0), "Outflow tract")
        bio.callout(ax, a["lv"], (13.8, 30.2), "LV")
    if st == "chambers":
        bio.callout(ax, a["oft_septum"], (27.5, 33.2), "Crest septum")

b = O.blood_island(ax, (2.2, 20.5), 1.0)
bio.callout(ax, b["angioblast"], (4.6, 22.6), "Angioblasts")
O.plexus(ax, (5.6, 18.6, 5.0, 3.8), cell=0.95)
s = O.sprout(ax, (16.0, 18.9), 80, 2.6)
bio.callout(ax, s["tip"], (19.2, 23.2), "Tip cell")
bio.callout(ax, s["stalk"], (19.8, 20.2), "Stalk cells")
ao = O.aorta_section(ax, (25.8, 20.6), 1.3)
bio.callout(ax, ao["hemogenic"], (28.8, 18.0), "Hemogenic floor")

g = O.gut_tube(ax, (0.8, 13.6), 15.0)
for key, txt, xy in (("lung", "Lung bud", (2.5, 10.4)), ("liver", "Liver", (6.4, 9.6)), ("stomach", "Stomach", (5.6, 15.6)),
                     ("dorsal_pancreas", "Dorsal pancreas", (9.3, 16.0)), ("allantois", "Allantois", (15.0, 10.2))):
    bio.callout(ax, g[key], xy, txt)
p = O.pharynx(ax, (23.5, 12.4), 5.0, 6.2)
bio.callout(ax, p["pouch3"], (28.8, 14.6), "Pouch 3")
bio.callout(ax, p["arch1"], (28.8, 15.6), "Arch 1")

t = O.seminiferous_tubule(ax, (3.8, 3.8), 2.8)
bio.callout(ax, t["leydig"], (8.4, 7.6), "Leydig cells")
O.germ_lineage(ax, (9.4, 5.2), "sperm", step=1.8, r=0.32)
O.germ_lineage(ax, (9.4, 1.6), "egg", step=1.9, r=0.28)
for k, st in enumerate(("primordial", "primary", "secondary", "antral")):
    O.follicle(ax, (19.6 + 2.6 * k + (1.0 if k == 3 else 0), 3.4), 1.6 if k == 3 else 1.3, st)
