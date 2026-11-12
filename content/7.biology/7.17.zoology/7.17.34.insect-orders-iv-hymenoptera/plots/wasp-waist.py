# The "wasp waist" of Apocrita compared with the broad waist of sawflies (schematic lateral view, legs and
# wings omitted). In sawflies abdominal segment 1 (A1) is a normal abdominal segment broadly joined to
# A2; in Apocrita A1 is fused to the metathorax as the propodeum and the constriction lies between A1 and
# A2, so that the functional "thorax" (mesosoma) includes A1 and the
# functional "abdomen" (metasoma, the gaster) begins with A2, which forms a narrow petiole.
import numpy as np
from matplotlib.patches import Ellipse, Polygon
import wikibio as bio
from wikibio.core import smooth_closed

P = bio.P
fig, ax = bio.canvas(26, 9.4)


def seg(pts, tok, z=5):
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.9, zorder=z,
                         joinstyle="round"))


def body(x0, y0, apocrita):
    # head
    ax.add_patch(Ellipse((x0 + 0.8, y0), 1.6, 1.9, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.9, zorder=6))
    x = x0 + 1.6
    th = [("T1", 0.7, "protein"), ("T2", 1.7, "enzyme"), ("T3", 0.8, "channel")]
    cuts = []
    for name, w, tok in th:
        seg([(x, y0 - 0.85), (x + w, y0 - 0.95), (x + w, y0 + 0.95), (x, y0 + 0.85)], tok)
        bio.label(ax, (x + w / 2, y0), name, size="tiny", color=P.on_fill())
        x += w
    # A1 propodeum
    w1 = 1.0
    if apocrita:
        seg([(x, y0 - 0.95), (x + w1, y0 - 0.5), (x + w1, y0 + 0.55), (x, y0 + 0.95)], "highlight")
    else:
        seg([(x, y0 - 0.95), (x + w1, y0 - 0.95), (x + w1, y0 + 0.95), (x, y0 + 0.95)], "highlight")
    bio.label(ax, (x + w1 / 2, y0), "A1", size="tiny", color=P.on_fill())
    a1 = (x + w1 / 2, y0 + 0.75)
    x += w1
    # A2
    if apocrita:
        seg([(x, y0 - 0.2), (x + 1.3, y0 - 0.25), (x + 1.3, y0 + 0.25), (x, y0 + 0.2)], "bone")
        pet = (x + 0.65, y0 - 0.2)
        x += 1.3
        hs = [0.9, 1.25, 1.3, 1.2, 1.0, 0.7, 0.35]
    else:
        seg([(x, y0 - 0.95), (x + 0.8, y0 - 0.95), (x + 0.8, y0 + 0.95), (x, y0 + 0.95)], "bone")
        pet = (x + 0.4, y0 - 0.9)
        x += 0.8
        hs = [0.95, 0.95, 0.9, 0.85, 0.75, 0.6, 0.4]
    for i in range(len(hs) - 1):
        seg([(x, y0 - hs[i]), (x + 0.75, y0 - hs[i + 1]), (x + 0.75, y0 + hs[i + 1]), (x, y0 + hs[i])], "bone")
        x += 0.75
    return a1, pet, x


bio.label(ax, (6.5, 9.4), "Symphyta (sawflies)", size="title", bold=True)
a1, pet, xe = body(0.6, 6.2, False)
bio.callout(ax, a1, (5.9, 8.4), "A1: first abdominal segment", size="small")
bio.callout(ax, pet, (8.8, 4.3), "A1 and A2 broadly joined: no waist", size="small")
bio.label(ax, (19.5, 9.4), "Apocrita (wasps, bees, ants)", size="title", bold=True)
a1b, petb, xe2 = body(13.4, 6.2, True)
bio.callout(ax, a1b, (18.9, 8.4), "A1 = propodeum, part of the mesosoma", size="small")
bio.callout(ax, petb, (20.0, 4.3), "A2 = petiole (waist)", size="small")
# brackets for tagmata
for x0, x1, y, t in ((15.0, 18.9, 3.3, "mesosoma (T1-T3 + A1)"), (18.9, 25.2, 3.3, "metasoma (A2 onward)"),
                     (2.2, 5.3, 3.3, "thorax (T1-T3)"), (5.3, 11.6, 3.3, "abdomen (A1 onward)")):
    ax.plot([x0 + 0.05, x1 - 0.05], [y, y], color=P.ink(), lw=1.0)
    for xx in (x0 + 0.05, x1 - 0.05):
        ax.plot([xx, xx], [y, y + 0.25], color=P.ink(), lw=1.0)
    bio.label(ax, ((x0 + x1) / 2, y - 0.45), t, size="tiny")
bio.label(ax, (13.0, 1.6), "T1-T3: pro-, meso- and metathorax; A1-A2: abdominal segments 1-2. In Apocrita the gaster is "
          "the metasoma behind the petiole.", size="tiny", color=P.muted())
bio.label(ax, (25.8, 0.9), "Schematic lateral view; legs and wings omitted", size="tiny", color=P.muted(), ha="right")
