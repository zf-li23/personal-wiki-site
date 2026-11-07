# Na+ transport and compartmentation under salt stress (schematic; after Munns and Tester 2008 and the SOS model
# of J.-K. Zhu). A, a root cortical cell: Na+ enters passively through non-selective cation channels (NSCC) and
# HKT-type transporters; the plasma-membrane P-type H+-ATPase energises the Na+/H+ antiporter SOS1, which pumps Na+
# back out; salt is sensed (e.g. by GIPC sphingolipids, MOCA1) and the Ca2+ signal activates the CBL-CIPK pair
# SOS3-SOS2, which phosphorylates SOS1. The tonoplast V-ATPase and H+-PPase energise NHX antiporters that load Na+
# into the vacuole; K+ is retained through K+ channels. B, the root stele: HKT1;1 (HKT1;5 in cereals) in xylem
# parenchyma retrieves Na+ from the xylem sap, limiting Na+ delivery to the leaves.
import wikibio as bio
from wikibio import cellbio as CB

P = bio.P
fig, ax = bio.canvas(27.0, 12.6)
yp, yt = 9.0, 3.4
CB.sides(ax, (0.2, 19.8), yp, height=(3.2, 2.45), top="Apoplast (soil solution: high Na⁺)", bottom="Cytosol",
         label_x=1.0)
CB.sides(ax, (0.2, 19.8), yt, height=(2.35, 2.6), top=None, bottom="Vacuole", top_token="cytoplasm",
         bottom_token="vacuole", label_x=17.9)
bio.bilayer(ax, [(0.2, yp), (19.8, yp)])
bio.bilayer(ax, [(0.2, yt), (19.8, yt)])
bio.panel(ax, "A", (0.3, 12.5))
bio.label(ax, (19.6, yp + 0.75), "plasma membrane", size="tiny", ha="right", color=P.muted())
bio.label(ax, (19.6, yt + 0.75), "tonoplast", size="tiny", ha="right", color=P.muted())


def title(x, y, a, b=None):
    bio.label(ax, (x, y), a, size="small", bold=True)
    if b:
        bio.label(ax, (x, y - 0.4), b, size="tiny", color=P.muted())


up, dn = yp - 1.55, yp + 1.55
# NSCC / HKT entry
x = 2.2
CB.channel(ax, x, yp)
CB.flux(ax, x, dn, up, species=[("na", 2)])
title(x, 11.6, "NSCC, HKT", "passive Na⁺ entry")
# K channel
x = 5.0
CB.channel(ax, x, yp, token="k")
CB.flux(ax, x, dn, up, species=[("k", 1)])
title(x, 11.6, "K⁺ channel", "keep K⁺/Na⁺ high")
# H+-ATPase
x = 8.2
atp = CB.pump(ax, x, yp, width=1.6)
CB.flux(ax, x - 0.4, up, dn, species=[("h", 1)])
bio.molecule(ax, atp + (0.2, 0.1), token="atp", text="ATP", r=0.27, size=5.0)
title(x, 11.6, "H⁺-ATPase", "P-type")
# SOS1
x = 12.0
CB.carrier(ax, x, yp, open="out", token="receptor", width=1.45)
CB.flux(ax, x - 0.32, dn, up, species=[("h", 1)], offset=0)
CB.flux(ax, x + 0.32, up, dn, species=[("na", 1)])
title(x, 11.6, "SOS1", "Na⁺/H⁺ antiporter")
# SOS3-SOS2 and Ca
bio.ion(ax, (14.6, 6.6), "ca", r=0.18)
bio.box(ax, (14.2, 5.6), 2.9, 0.62, token="enzyme", text="SOS3 (CBL4)", size="tiny")
bio.box(ax, (14.2, 4.8), 2.9, 0.62, token="protein", text="SOS2 (CIPK24)", size="tiny")
bio.arrow(ax, (14.6, 6.35), (14.4, 5.95), kind="activation")
bio.arrow(ax, (13.2, 5.15), (12.3, 7.25), kind="activation", bend=0.2)
bio.label(ax, (12.3, 6.0), "P", size="tiny", bold=True, color=P.edge("protein"))
bio.label(ax, (17.4, 6.9), "salt sensing:", size="tiny", bold=True)
bio.label(ax, (17.4, 6.5), "GIPC–MOCA1 →", size="tiny")
bio.label(ax, (17.4, 6.1), "Ca²⁺ influx", size="tiny")
# tonoplast
x = 3.2
CB.carrier(ax, x, yt, open="in", token="enzyme", width=1.5)
bio.molecule(ax, (x + 1.05, yt + 0.95), token="atp", text="ATP", r=0.27, size=5.0)
CB.flux(ax, x - 0.2, yt + 1.55, yt - 1.55, species=[("h", 2)])
title(x, yt + 2.05, "V-ATPase", None)
x = 7.0
CB.carrier(ax, x, yt, open="out", token="metabolite", width=1.3)
CB.flux(ax, x, yt + 1.55, yt - 1.55, species=[("h", 1)])
title(x, yt + 2.05, "H⁺-PPase", None)
x = 10.8
CB.carrier(ax, x, yt, open="in", token="receptor", width=1.45)
CB.flux(ax, x - 0.32, yt - 1.55, yt + 1.55, species=[("h", 1)])
CB.flux(ax, x + 0.32, yt + 1.55, yt - 1.55, species=[("na", 1)])
title(x, yt + 2.5, "NHX1", "Na⁺/H⁺ antiporter")
bio.label(ax, (14.0, 1.6), "vacuolar Na⁺, Cl⁻: osmotic adjustment", size="tiny")
bio.label(ax, (14.0, 1.2), "cytosol: compatible solutes", size="tiny")

# B: stele
bio.panel(ax, "B", (20.4, 12.5))
import matplotlib.patches as mp
ax.add_patch(mp.FancyBboxPatch((21.0, 1.0), 5.6, 10.4, boxstyle="round,pad=0,rounding_size=0.3",
                               facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cytoplasm"), lw=1, zorder=1))
ax.add_patch(mp.Rectangle((23.2, 1.0), 1.3, 10.4, facecolor=P.fill("channel"), edgecolor=P.edge("channel"), lw=1.2, zorder=2))
bio.label(ax, (23.85, 11.75), "xylem vessel", size="small", bold=True)
bio.label(ax, (21.9, 10.6), "xylem", size="tiny")
bio.label(ax, (21.9, 10.2), "parenchyma", size="tiny")
for k in range(4):
    bio.ion(ax, (23.85, 2.5 + 2.2 * k), "na", r=0.17, text=False, zorder=8)
bio.arrow(ax, (23.85, 2.0), (23.85, 10.6), kind="process", zorder=7)
bio.label(ax, (25.2, 10.3), "to the", size="tiny")
bio.label(ax, (25.2, 9.9), "shoot", size="tiny")
for y in (4.0, 7.0):
    CB.carrier(ax, 23.2, y, open="in", token="receptor", width=1.0)
    bio.arrow(ax, (23.6, y - 0.2), (22.1, y - 0.2), kind="process", zorder=9)
bio.label(ax, (22.2, 5.5), "HKT1", size="small", bold=True)
bio.label(ax, (22.2, 5.1), "retrieves Na⁺", size="tiny")

# ion key
for i, (k, t) in enumerate([("na", "Na⁺"), ("k", "K⁺"), ("h", "H⁺"), ("ca", "Ca²⁺")]):
    bio.ion(ax, (3.0 + 1.3 * i, 6.95), k, r=0.15, text=True)
