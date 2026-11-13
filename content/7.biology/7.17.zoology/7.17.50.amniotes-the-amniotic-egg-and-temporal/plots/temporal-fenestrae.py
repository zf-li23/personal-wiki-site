# The four classical patterns of temporal fenestration in amniote skulls, left lateral view, anterior to the
# left (schematic, after Romer 1966, Pough et al. 2023 and Kardong 2019). The same skull plan is used in all
# panels so that only the openings and the bones bordering them differ: anapsid (no opening; Captorhinus,
# Paleothyris), synapsid (one lower opening bordered above by the postorbital and squamosal and below by the
# jugal and quadratojugal; Dimetrodon, mammals), diapsid (an upper and a lower opening separated by the
# postorbital-squamosal bar; Petrolacosaurus, Sphenodon) and euryapsid (one upper opening, bordered below by
# the postorbital and squamosal; plesiosaurs and placodonts, derived from a diapsid skull by loss of the
# lower opening). Bones are coloured in the course-wide homology scheme of vertskel. Not to scale.
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P

SKULL = [
    ("chondrocranium", [(0.0, 1.2), (0.3, 2.2), (2.0, 3.2), (4.8, 3.75), (7.0, 3.88), (9.8, 3.6), (10.0, 2.0),
                        (9.8, 0.6), (0.6, 0.7)], {"state": "context"}),
    ("premaxilla", [(0.0, 1.2), (0.3, 2.2), (1.0, 2.6), (1.5, 1.9), (1.5, 0.7), (0.6, 0.7)]),
    ("nasal", [(1.0, 2.6), (2.0, 3.2), (3.6, 3.55), (3.6, 2.9), (1.5, 1.9)]),
    ("maxilla", [(1.5, 0.7), (1.5, 1.9), (2.8, 2.0), (3.6, 1.5), (5.5, 1.2), (6.2, 0.7)]),
    ("lacrimal", [(1.5, 1.9), (3.6, 2.9), (4.3, 2.8), (4.25, 1.75), (3.6, 1.5), (2.8, 2.0)]),
    ("prefrontal", [(3.6, 2.9), (3.6, 3.55), (4.8, 3.75), (4.6, 3.25), (4.0, 2.7)]),
    ("frontal", [(4.3, 2.8), (4.6, 3.25), (4.8, 3.75), (6.4, 3.86), (6.3, 3.35), (5.6, 3.0), (5.0, 3.05)]),
    ("postfrontal", [(6.3, 3.35), (6.4, 3.86), (7.0, 3.88), (6.9, 3.2), (6.2, 2.9), (5.6, 3.0)]),
    ("postorbital", [(6.2, 2.9), (6.9, 3.2), (7.6, 2.9), (7.4, 2.0), (6.3, 1.9), (5.8, 1.85), (5.9, 2.4)]),
    ("jugal", [(3.6, 1.5), (3.9, 1.9), (4.25, 1.75), (4.5, 1.5), (5.5, 1.45), (5.8, 1.85), (6.3, 1.9), (7.4, 2.0), (8.4, 1.5),
               (8.4, 0.65), (6.2, 0.7), (5.5, 1.2)]),
    ("parietal", [(6.9, 3.2), (7.0, 3.88), (8.8, 3.85), (8.8, 3.0), (7.6, 2.9)]),
    ("supratemporal", [(8.8, 3.0), (8.8, 3.85), (9.8, 3.6), (9.9, 2.8)]),
    ("squamosal", [(7.6, 2.9), (8.8, 3.0), (9.9, 2.8), (10.0, 2.0), (8.4, 1.5), (7.4, 2.0)]),
    ("quadratojugal", [(8.4, 0.65), (9.8, 0.6), (10.0, 2.0), (8.4, 1.5)]),
    ("dentary", [(0.7, 0.58), (6.6, 0.56), (7.6, 0.18), (6.0, -0.25), (1.2, 0.08)]),
    ("angular", [(6.0, -0.25), (7.6, 0.18), (9.7, 0.3), (9.0, -0.12)]),
    ("surangular", [(6.6, 0.56), (9.7, 0.52), (9.7, 0.3), (7.6, 0.18)]),
    ("articular", [(9.7, 0.52), (10.25, 0.48), (10.25, 0.22), (9.7, 0.3)]),
]


def hole(ax, at, c, rx, ry, angle=0.0):
    """An opening in the skull: background colour with a dark rim."""
    x, y = at
    pts = np.array(vs.oval((x + c[0], y + c[1]), rx, ry, angle))
    ax.fill(pts[:, 0], pts[:, 1], color=P.surface(), zorder=9, lw=0)
    ax.plot(np.r_[pts[:, 0], pts[0, 0]], np.r_[pts[:, 1], pts[0, 1]], color=P.ink(), lw=0.9, zorder=9.5)
    return (x + c[0], y + c[1])


titles = ["Anapsid", "Synapsid", "Diapsid", "Euryapsid"]
subs = ["no temporal opening", "one lower opening", "upper and lower openings", "one upper opening"]
examples = ["Captorhinus, Paleothyris; extant turtles secondarily",
            "Dimetrodon, therapsids, mammals",
            "Petrolacosaurus, Sphenodon, archosaurs",
            "plesiosaurs, placodonts (from a diapsid skull)"]
fig, ax, boxes = vs.panels(4, 12.6, 5.0, titles=titles, subtitles=subs, ncols=2, legend_rows=4, gap=1.0)
for i, (x, y, w, h) in enumerate(boxes):
    at = (x + 0.2, y + 0.9)
    a = vs.draw(ax, SKULL, at=at)
    hole(ax, at, (5.0, 2.35), 0.95, 0.8)                 # orbit
    hole(ax, at, (1.15, 1.75), 0.3, 0.22)                # external naris
    bio.label(ax, (at[0] + 5.0, at[1] + 2.35), "orbit", size="tiny", color=P.muted())
    if i in (1, 2):
        lt = hole(ax, at, (7.95, 1.55), 0.62, 0.4, angle=-10)
        vs.callout(ax, lt, (at[0] + 10.4, at[1] + 1.7), "lower temporal fenestra")
    if i in (2, 3):
        ut = hole(ax, at, (8.3, 3.38), 0.55, 0.3)
        vs.callout(ax, ut, (at[0] + 10.3, at[1] + 4.35), "upper temporal fenestra")
    if i == 1:
        vs.callout(ax, (at[0] + 8.0, at[1] + 1.02), (at[0] + 10.4, at[1] + 0.55), "lower temporal bar")
    if i == 2:
        vs.callout(ax, (at[0] + 7.65, at[1] + 2.6), (at[0] + 3.0, at[1] + 4.45), "postorbital-squamosal bar")
    bio.label(ax, (x + w / 2, y + 0.05), examples[i], size="tiny", italic=False, color=P.muted())

entries = ["premaxilla", "maxilla", "nasal", "frontal", "parietal", "lacrimal", "prefrontal", "postfrontal",
           "postorbital", "jugal", "squamosal", "quadratojugal", "supratemporal", "dentary", "angular",
           "surangular", "articular"]
vs.legend(ax, entries, at=(0.4, 4 * 0.55 + 0.25), width=22.0, ncols=6)
