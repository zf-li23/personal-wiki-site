# Parts of a simple leaf, leaf margins and venation patterns, generated from rules (wikibio.botany).
# (A) A simple leaf at a node: lamina with apex, margin, midrib, secondary and tertiary veins, petiole and a
# pair of stipules; the axillary bud sits in the angle between petiole and stem. (B) Margins, from entire to
# deeply divided: lobed (sinuses less than halfway to the midrib), pinnatifid (more than halfway),
# pinnatisect (almost to the midrib). (C) Venation: pinnate with secondaries ending in the margin
# (craspedodromous), pinnate with secondaries looping inside the margin (brochidodromous, here with a
# reticulate network of finer veins), arcuate (secondaries curving towards the apex), palmate (several
# primary veins from the base), parallel (strap-shaped monocot leaf with transverse veinlets) and
# dichotomous (repeated equal forking, as in Ginkgo).
import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(27.0, 17.0)

# ---- A: parts of a leaf -------------------------------------------------------------------------------
bio.panel(ax, "A", (0.2, 16.8))
bio.label(ax, (0.85, 16.77), "Simple leaf", size="title", ha="left", va="top")
sx, sy = 3.4, 8.9
ax.plot([sx, sx], [sy, sy + 6.8], color=P.edge("plant"), lw=7.0, solid_capstyle="round", zorder=4)
ax.plot([sx, sx], [sy, sy + 6.8], color=P.fill("plant"), lw=4.6, solid_capstyle="round", zorder=4.1)
node = (sx, sy + 2.0)
a = B.leaf(ax, node, 5.4, 38, shape="ovate", margin="serrate", venation="pinnate", secondaries=6, petiole=1.7,
           stipules=True, tertiary="percurrent")
bud = B.bud(ax, (sx + 0.2, node[1] + 0.45), 0.5, angle=70)
ax.plot([sx - 0.15, sx + 0.15], [node[1], node[1]], color=P.edge("plant"), lw=1.2, zorder=5)
# right-hand labels, in the vertical order of their anchors so that leaders do not cross
right = [("Apex", a["apex"]), ("Blade (lamina)", B.leaf_point(a, 0.72, -0.35)),
         ("Margin (serrate)", a["tips"][min(range(len(a["tips"])), key=lambda i: ((a["tips"][i] - B.leaf_point(a, 0.45, -1)) ** 2).sum())]),
         ("Secondary vein", B.vein_point(a, 2, 0.5, -0.55)), ("Tertiary veins", B.vein_point(a, 3, 0.3, -0.6)),
         ("Midrib", B.leaf_point(a, 0.86, 0)), ("Leaf base", a["attachment"])]
right.sort(key=lambda t: -t[1][1])
for k, (name, p) in enumerate(right):
    bio.callout(ax, p, (12.6, 15.4 - k * 0.95), name)
bio.callout(ax, a["petiole"], (6.6, 9.3), "Petiole")
bio.callout(ax, a["stipules"][1], (6.1, 10.2), "Stipule")
bio.callout(ax, bud, (2.5, 13.0), "Axillary bud")
bio.callout(ax, node, (2.5, 11.6), "Node")
bio.callout(ax, (sx, sy + 0.6), (2.5, 9.5), "Stem")

# ---- B: margins ------------------------------------------------------------------------------------------
bio.panel(ax, "B", (14.2, 16.8))
bio.label(ax, (14.85, 16.77), "Margin", size="title", ha="left", va="top")
MARGINS = ["entire", "sinuate", "crenate", "dentate", "serrate", "serrulate", "doubly serrate", "spinose", "lobed",
           "pinnatifid", "pinnatisect"]
for i, m in enumerate(MARGINS):
    col, row = i % 6, i // 6
    x = 15.3 + col * 2.05
    y = 12.5 - row * 4.0
    shp = "obovate" if m in ("lobed",) else "elliptic"
    B.leaf(ax, (x, y), 2.7, 90, shape=shp, width=1.35 if m not in ("pinnatifid", "pinnatisect") else 1.55, margin=m,
           petiole=0.3, venation="pinnate", secondaries=5, apex="acute" if m != "lobed" else "obtuse")
    bio.label(ax, (x, y - 0.35), m.capitalize(), size="small")

# ---- C: venation ----------------------------------------------------------------------------------------------
bio.panel(ax, "C", (0.2, 6.4))
bio.label(ax, (0.85, 6.37), "Venation", size="title", ha="left", va="top")
VEN = [("Pinnate\n(craspedodromous)", dict(shape="elliptic", margin="serrate", venation="pinnate", secondaries=7)),
       ("Pinnate\n(brochidodromous)", dict(shape="elliptic", venation="brochidodromous", secondaries=6, tertiary="reticulate")),
       ("Arcuate", dict(shape="elliptic", venation="arcuate", secondaries=4, width=2.1)),
       ("Palmate", dict(shape="palmately lobed", margin="entire", venation="palmate", length=3.0, width=3.2)),
       ("Parallel", dict(shape="linear", width=0.8, venation="parallel", secondaries=4, tertiary=True, length=4.6)),
       ("Dichotomous", dict(shape="flabellate", venation="dichotomous", length=2.6, width=3.9))]
for i, (name, kw) in enumerate(VEN):
    x = 2.2 + i * 4.45
    ln = kw.pop("length", 4.0)
    B.leaf(ax, (x, 1.25 if "Palmate" not in name else 1.9), ln, 90, petiole=0.45 if "Palmate" not in name else 0.2, **kw)
    bio.label(ax, (x, 0.7), name, size="small", va="center")
