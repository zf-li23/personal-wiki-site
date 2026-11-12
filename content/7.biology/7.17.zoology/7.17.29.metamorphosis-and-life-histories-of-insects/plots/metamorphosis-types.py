# Types of postembryonic development (schematic): ametaboly (silverfish, adult keeps molting),
# hemimetaboly (grasshopper: five nymphal instars with growing wing pads, then the adult) and
# holometaboly (butterfly: egg, caterpillar, pupa, adult). Arrows are molts; the stage in which
# wings first become externally visible is shaded.
import numpy as np
import wikibio as bio
from matplotlib.patches import Ellipse, Circle, Polygon, FancyBboxPatch

P = bio.P
fig, ax = bio.canvas(28, 15.5)
rows = {"amet": 12.6, "hemi": 7.8, "holo": 2.9}
ink = P.ink()


def row_title(y, title, sub):
    bio.label(ax, (0.3, y + 0.35), title, size="normal", bold=True, ha="left")
    bio.label(ax, (0.3, y - 0.35), sub, size="tiny", ha="left", color=P.muted())


def highlight(x, y, w, h):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.3",
                                facecolor=P.light("highlight"), edgecolor=P.edge("highlight"), lw=0.8, zorder=2))


def molt(a, b, y):
    bio.arrow(ax, (a, y), (b, y), kind="process", color=P.muted())


def egg(x, y, r=0.32):
    ax.add_patch(Ellipse((x, y), 2 * r, 1.4 * r, facecolor=P.fill("ovule"), edgecolor=P.edge("ovule"), lw=1.0, zorder=8))


# --- ametaboly
y = rows["amet"]
row_title(y, "Ametaboly", "Zygentoma, Archaeognatha")
egg(5.2, y)
xs = [7.6, 10.6, 14.2, 18.4]
hs = [0.7, 1.0, 1.35, 1.7]
boxes = [bio.icon(ax, "phylopic/silverfish", at=(x, y), height=h, color=P.edge("animal")) for x, h in zip(xs, hs)]
molt(5.7, boxes[0][0] - 0.25, y)
for a, b in zip(boxes[:-1], boxes[1:]):
    molt(a[0] + a[2] + 0.25, b[0] - 0.25, y)
bio.label(ax, (7.6, y - 1.2), "juvenile", size="tiny", color=P.muted())
bio.label(ax, (18.4, y - 1.4), "adult (mature)", size="tiny", color=P.muted())
bio.arrow(ax, (20.0, y + 0.5), (20.0, y - 0.5), kind="process", bend=-1.2, color=P.muted())
bio.label(ax, (22.9, y), "adult goes on molting", size="small", ha="left")

# --- hemimetaboly
y = rows["hemi"]
row_title(y, "Hemimetaboly", "Polyneoptera, Paraneoptera")
egg(5.2, y)
hs = [0.5, 0.65, 0.8, 1.0, 1.2, 1.75]
ids = ["wikimedia/grasshopper-instar-1", "wikimedia/grasshopper-instar-2", "wikimedia/grasshopper-instar-3",
       "wikimedia/grasshopper-instar-4", "wikimedia/grasshopper-instar-5", "wikimedia/grasshopper-adult"]
x = 6.3
boxes = []
for i, h in enumerate(hs):
    bb = bio.icon(ax, ids[i], at=(x, y), height=h, anchor="left", color=P.edge("animal"))
    boxes.append(bb)
    x = bb[0] + bb[2] + 0.75
x0h = boxes[1][0] - 0.2
x1h = boxes[4][0] + boxes[4][2] + 0.2
highlight((x0h + x1h) / 2, y, x1h - x0h, 2.2)
molt(5.7, boxes[0][0] - 0.1, y)
for a, b in zip(boxes[:-1], boxes[1:]):
    molt(a[0] + a[2] + 0.1, b[0] - 0.1, y)
for i, bb in enumerate(boxes[:5]):
    bio.label(ax, (bb[0] + bb[2] / 2, y - 1.25), "N%d" % (i + 1), size="tiny", color=P.muted())
bb = boxes[5]
bio.label(ax, (bb[0] + bb[2] / 2, y - 1.4), "adult", size="tiny", color=P.muted())
bio.label(ax, ((x0h + x1h) / 2, y + 1.45), "external wing pads, larger at each molt", size="tiny", color=P.edge("highlight"))
bio.label(ax, (22.9, y), "nymphs resemble the adult;", size="small", ha="left")
bio.label(ax, (22.9, y - 0.55), "no pupa", size="small", ha="left")

# --- holometaboly
y = rows["holo"]
row_title(y, "Holometaboly", "Holometabola")
egg(5.2, y)
# caterpillar: chain of segments with head
x0 = 7.0
for k in range(10):
    ax.add_patch(Circle((x0 + 0.42 * k, y + 0.05 * np.sin(k)), 0.32, facecolor=P.fill("plant"), edgecolor=P.edge("plant"),
                        lw=0.9, zorder=8))
ax.add_patch(Circle((x0 + 4.3, y + 0.1), 0.36, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=0.9, zorder=9))
for k in (0, 1, 2, 5, 6, 7, 8):  # prolegs (rear) and true legs (front)
    xx = x0 + 0.42 * (9 - k) if k < 3 else x0 + 0.42 * (k - 5)
    ax.plot([xx, xx], [y - 0.3, y - 0.48], color=P.edge("plant"), lw=1.6, zorder=7)
bio.label(ax, (x0 + 2.1, y - 1.0), "larva (several instars)", size="tiny", color=P.muted())
molt(5.7, x0 - 0.5, y)
# pupa (chrysalis)
cx = 14.3
highlight(cx, y, 2.4, 2.6)
pts = [(cx - 0.35, y + 0.95), (cx + 0.35, y + 0.95), (cx + 0.55, y + 0.3), (cx + 0.42, y - 0.5), (cx + 0.12, y - 1.0),
       (cx - 0.12, y - 1.0), (cx - 0.42, y - 0.5), (cx - 0.55, y + 0.3)]
ax.add_patch(Polygon(bio.smooth_closed(pts), closed=True, facecolor=P.fill("bract"), edgecolor=P.edge("bract"), lw=1.0, zorder=8))
ax.plot([cx - 0.5, cx + 0.05, cx + 0.35], [y + 0.25, y - 0.45, y - 0.75], color=P.edge("bract"), lw=0.9, zorder=9)
bio.label(ax, (cx, y - 1.55), "pupa", size="tiny", color=P.muted())
bio.label(ax, (cx, y + 1.55), "wings first visible", size="tiny", color=P.edge("highlight"))
molt(x0 + 4.8, cx - 0.9, y)
bio.icon(ax, "phylopic/swallowtail", at=(19.8, y), height=2.2, color=P.edge("animal"))
molt(cx + 0.9, 17.9, y)
bio.label(ax, (19.6, y - 1.55), "adult", size="tiny", color=P.muted())
bio.label(ax, (22.9, y), "larva unlike the adult;", size="small", ha="left")
bio.label(ax, (22.9, y - 0.55), "wings from imaginal discs", size="small", ha="left")

bio.label(ax, (14, 0.35), "Arrows: molts. Shaded: immature stages with external wing pads. Not to scale.",
          size="tiny", color=P.muted())
