# Vegetative organs of a flowering plant and their modifications. A: the plant body: the shoot system
# (stem with nodes and internodes, leaves, buds, flowers) above ground and the root system below.
# B: a leaf: blade (lamina), petiole and a pair of stipules at its base on the stem. C: root systems:
# a fibrous system of many similar adventitious roots (grasses, most monocots) and a taproot (the
# enlarged primary root, here a storage taproot of carrot, typical of eudicots). D: modified stems,
# recognised as stems by their nodes, buds and scale leaves: tuber (potato; the eyes are axillary buds),
# rhizome (horizontal underground stem with scale leaves and adventitious roots), stolon (runner of
# strawberry, rooting at a node into a daughter plant), bulb (onion; a short disc-shaped stem, the basal
# plate, carrying fleshy scale leaves) and thorn (a sharp modified branch in the axil of a leaf).
import wikibio as bio
from wikibio import plantmorph as PM

P = bio.P
fig, ax = bio.canvas(37.6, 17.0)

# ---- A: plant body -----------------------------------------------------------------------------------
bio.panel(ax, "A", (0.2, 16.8))
bio.label(ax, (5.0, 16.2), "Plant body", size="normal", bold=True)
s = PM.specimen(ax, "wikimedia/plant-body", at=(4.6, 8.9), height=12.0, left=1.2, right=8.3, gap=0.55, labels=[
    dict(part="petal", text="Flower", side="right"),
    dict(at=(0.17, 0.62), text="Leaf", side="left"),
    dict(at=(0.573, 0.76), text="Axillary bud", side="right"),
    dict(at=(0.5, 0.63), text="Node", side="left"),
    dict(at=(0.51, 0.5), text="Internode", side="left"),
    dict(at=(0.51, 0.4), text="Stem", side="right"),
    dict(at=(0.5, 0.14), text="Primary root", side="right"),
    dict(at=(0.25, 0.1), text="Lateral root", side="left"),
])
x0, y0, w, h = s["box"]
bio.label(ax, (x0 + 0.2, y0 + h - 0.2), "Shoot system", size="small", bold=True, ha="left", va="top", color=P.muted())
bio.label(ax, (x0 + w - 0.2, y0 + 0.25), "Root system", size="small", bold=True, ha="right", va="bottom", color=P.muted())

# ---- B: leaf ----------------------------------------------------------------------------------------
bio.panel(ax, "B", (11.0, 16.8))
bio.label(ax, (14.6, 16.2), "Leaf", size="normal", bold=True)
PM.specimen(ax, "wikimedia/leaf-stipules", at=(14.6, 12.6), height=4.4, left=11.9, right=17.6, labels=[
    dict(at=(0.45, 0.8), text="Blade (lamina)", side="right"),
    dict(at=(0.57, 0.61), text="Midrib", side="right"),
    dict(at=(0.27, 0.28), text="Petiole", side="right"),
    dict(at=(0.15, 0.4), text="Stipule", side="left"),
    dict(at=(0.3, 0.205), text="Stipule ", side="right"),
    dict(at=(0.05, 0.12), text="Stem", side="left"),
])

# ---- C: root systems --------------------------------------------------------------------------------
bio.panel(ax, "C", (20.4, 16.8))
bio.label(ax, (26.0, 16.2), "Root systems", size="normal", bold=True)
r = bio.icon(ax, "wikimedia/root-systems", at=(25.6, 12.4), width=8.4, hide=["soil"], parts={"fibrous-root": "animal"})
ax.plot([r[0], r[0] + r[2]], [r[1] + r[3] * 0.595] * 2, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
bio.label(ax, (r[0] + r[2] * 0.33, r[1] - 0.35), "Fibrous root system", size="small", bold=True)
bio.label(ax, (r[0] + r[2] * 0.8, r[1] - 0.35), "Taproot", size="small", bold=True)
bio.callout(ax, PM.point_in(r, (0.81, 0.4)), (r[0] + r[2] + 0.5, r[1] + r[3] * 0.4), "Storage taproot")
bio.callout(ax, PM.point_in(r, (0.22, 0.35)), (r[0] - 0.4, r[1] + r[3] * 0.25), "Adventitious roots")

# ---- D: modified stems ------------------------------------------------------------------------------
bio.panel(ax, "D", (11.0, 8.2))
bio.label(ax, (24.0, 7.7), "Modified stems", size="normal", bold=True)
PM.specimen(ax, "wikimedia/potato-tuber", at=(13.3, 3.6), width=3.8, left=11.3, right=15.6, gap=0.5, labels=[
    dict(at=(0.66, 0.75), text="Eye (bud)", side="right"),
    dict(at=(0.3, 0.5), text="Storage tissue", side="left", y=2.2),
])
bio.label(ax, (13.3, 1.0), "Tuber (potato)", size="small", bold=True)
a = PM.rhizome(ax, (17.9, 3.0), 4.4)
PM.callouts(ax, [(a["scale_leaf"], "Scale leaf", "left"), (a["roots"], "Adventitious roots", "left"),
                 (a["shoot"], "Aerial shoot", "right"), (a["node"], "Node", "left")], left=17.7, right=22.7, gap=0.45)
bio.label(ax, (20.1, 1.0), "Rhizome", size="small", bold=True)
a = PM.stolon(ax, (24.3, 3.1), 3.2)
bio.callout(ax, a["stolon"], (25.9, 5.4), "Stolon")
bio.callout(ax, a["plantlet"], (27.4, 5.9), "Daughter plant")
bio.callout(ax, a["mother"], (24.0, 6.6), "Mother plant")
bio.label(ax, (25.9, 1.0), "Stolon (strawberry)", size="small", bold=True)
a = PM.bulb(ax, (30.0, 2.4), 3.8)
PM.callouts(ax, [(a["scale"], "Fleshy scale leaf", "right"), (a["bud"], "Bud", "right"), (a["basal_plate"], "Basal plate (stem)", "right"),
                 (a["tunic"], "Dry scale", "right")], right=31.6, gap=0.45)
bio.label(ax, (30.0, 1.0), "Bulb (onion)", size="small", bold=True)
PM.specimen(ax, "wikimedia/stem-thorn", at=(35.6, 4.3), height=4.6, right=37.0, labels=[
    dict(at=(0.08, 0.3), text="Thorn", side="left"),
    dict(at=(0.8, 0.4), text="Leaf", side="right"),
], left=34.0)
bio.label(ax, (35.6, 1.0), "Thorn", size="small", bold=True)
