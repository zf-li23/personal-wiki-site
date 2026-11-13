# The dermatocranium of an early tetrapod by series (vertskel level="series"), schematic, after Clack (2012),
# Romer & Parsons and Kardong (2019). A: left lateral view; B: dorsal view (left half drawn, right half
# mirrored). Openings: external naris, orbit, pineal foramen. Not to scale.
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P
fig, ax = bio.canvas(27, 10.5)

LAT = [
    ("premaxilla", [(0.0, 1.2), (0.3, 2.2), (1.0, 2.6), (1.5, 1.9), (1.5, 0.7), (0.6, 0.7)]),
    ("nasal", [(1.0, 2.6), (2.0, 3.2), (3.6, 3.55), (3.6, 2.9), (1.5, 1.9)]),
    ("maxilla", [(1.5, 0.7), (1.5, 1.9), (2.8, 2.0), (3.6, 1.5), (5.5, 1.2), (6.2, 0.7)]),
    ("lacrimal", [(1.5, 1.9), (3.6, 2.9), (4.3, 2.8), (4.25, 1.75), (3.6, 1.5), (2.8, 2.0)]),
    ("prefrontal", [(3.6, 2.9), (3.6, 3.55), (4.8, 3.75), (4.6, 3.25), (4.0, 2.7)]),
    ("frontal", [(4.3, 2.8), (4.6, 3.25), (4.8, 3.75), (6.4, 3.86), (6.3, 3.35), (5.6, 3.0), (5.0, 3.05)]),
    ("postfrontal", [(6.3, 3.35), (6.4, 3.86), (7.0, 3.88), (6.9, 3.2), (6.2, 2.9), (5.6, 3.0)]),
    ("postorbital", [(6.2, 2.9), (6.9, 3.2), (7.6, 2.9), (7.4, 2.0), (6.3, 1.9), (5.8, 1.85), (5.9, 2.4)]),
    ("jugal", [(3.6, 1.5), (4.25, 1.75), (4.5, 1.5), (5.5, 1.45), (5.8, 1.85), (6.3, 1.9), (7.4, 2.0), (8.4, 1.5),
               (8.4, 0.65), (6.2, 0.7), (5.5, 1.2)]),
    ("intertemporal", [(6.9, 3.2), (7.0, 3.88), (8.0, 3.86), (8.0, 3.0), (7.6, 2.9)]),
    ("supratemporal", [(8.0, 3.0), (8.0, 3.86), (9.2, 3.7), (9.3, 2.85)]),
    ("tabular", [(9.3, 2.85), (9.2, 3.7), (9.9, 3.5), (10.0, 2.7)]),
    ("squamosal", [(7.6, 2.9), (8.0, 3.0), (9.3, 2.85), (10.0, 2.7), (10.0, 2.0), (8.4, 1.5), (7.4, 2.0)]),
    ("quadratojugal", [(8.4, 0.65), (9.8, 0.6), (10.0, 2.0), (8.4, 1.5)]),
    ("dentary", [(0.7, 0.58), (6.6, 0.56), (7.6, 0.18), (6.0, -0.25), (1.2, 0.08)]),
    ("angular", [(6.0, -0.25), (7.6, 0.18), (9.7, 0.3), (9.0, -0.12)]),
    ("surangular", [(6.6, 0.56), (9.7, 0.52), (9.7, 0.3), (7.6, 0.18)]),
    ("articular", [(9.7, 0.52), (10.25, 0.48), (10.25, 0.22), (9.7, 0.3)]),
]


def hole(c, rx, ry):
    pts = np.array(vs.oval(c, rx, ry))
    ax.fill(pts[:, 0], pts[:, 1], color=P.surface(), zorder=20, lw=0)
    ax.plot(np.r_[pts[:, 0], pts[0, 0]], np.r_[pts[:, 1], pts[0, 1]], color=P.ink(), lw=0.9, zorder=21)


at = (1.0, 4.2)
a = vs.draw(ax, [(k, vs.poly(v)) for k, v in LAT], at=at, scale=1.15, level="series")
hole((at[0] + 5.0 * 1.15, at[1] + 2.35 * 1.15), 0.95 * 1.15, 0.8 * 1.15)
hole((at[0] + 1.15 * 1.15, at[1] + 1.75 * 1.15), 0.3, 0.22)
for key, (tx, ty) in (("premaxilla", (0.6, 9.4)), ("nasal", (3.0, 9.4)), ("lacrimal", (1.0, 3.2)), ("maxilla", (3.4, 3.0)),
                      ("prefrontal", (5.0, 9.4)), ("frontal", (7.2, 9.4)), ("postfrontal", (9.2, 9.4)),
                      ("postorbital", (10.0, 8.7)), ("intertemporal", (11.3, 9.4)), ("supratemporal", (13.2, 9.0)),
                      ("tabular", (13.6, 8.4)), ("squamosal", (13.6, 7.4)), ("quadratojugal", (13.6, 5.4)), ("jugal", (7.6, 3.0)),
                      ("dentary", (5.4, 3.1)), ("angular", (10.0, 3.2)), ("surangular", (12.2, 3.6)), ("articular", (13.6, 4.4))):
    vs.callout(ax, a[key], (tx, ty), key)
bio.panel(ax, "A", (0.3, 10.2))

# dorsal view: left half (y>0 lateral), mirrored
DOR = [
    ("premaxilla", [(0.0, 0.0), (0.2, 1.3), (1.0, 1.7), (1.4, 0.0)]),
    ("nasal", [(1.4, 0.0), (1.2, 1.0), (3.6, 1.0), (3.6, 0.0)]),
    ("maxilla", [(1.0, 1.7), (1.3, 2.3), (6.0, 2.75), (6.0, 2.5), (2.0, 1.8)]),
    ("lacrimal", [(1.2, 1.0), (1.0, 1.7), (2.0, 1.8), (4.0, 2.3), (4.0, 1.5), (3.6, 1.0)]),
    ("prefrontal", [(3.6, 1.0), (4.0, 1.5), (4.6, 1.3), (4.6, 0.85), (3.6, 0.85)]),
    ("frontal", [(3.6, 0.0), (3.6, 0.85), (4.6, 0.85), (5.8, 0.9), (5.8, 0.0)]),
    ("postfrontal", [(5.4, 0.9), (5.4, 1.35), (6.4, 1.45), (6.4, 0.95)]),
    ("parietal", [(5.8, 0.0), (5.8, 0.9), (6.4, 0.95), (7.8, 1.0), (7.8, 0.0)]),
    ("postorbital", [(5.4, 1.35), (5.6, 2.4), (6.6, 2.4), (6.4, 1.45)]),
    ("jugal", [(4.0, 2.3), (6.0, 2.5), (6.0, 2.75), (7.2, 2.95), (6.6, 2.4), (5.6, 2.4)]),
    ("intertemporal", [(6.4, 0.95), (6.4, 1.45), (6.6, 2.4), (7.8, 1.8), (7.8, 1.0)]),
    ("postparietal", [(7.8, 0.0), (7.8, 1.0), (9.6, 1.0), (9.6, 0.0)]),
    ("supratemporal", [(7.8, 1.0), (7.8, 1.8), (9.0, 2.0), (9.0, 1.0)]),
    ("tabular", [(9.0, 1.0), (9.0, 2.0), (9.8, 2.2), (9.6, 1.0)]),
    ("squamosal", [(6.6, 2.4), (7.2, 2.95), (9.6, 3.1), (9.8, 2.2), (9.0, 2.0), (7.8, 1.8)]),
]
ox, oy = 15.4, 4.9
parts = []
for k, v in DOR:
    parts.append((k, vs.poly([(x, y) for x, y in v])))
    parts.append((k, vs.poly([(x, -y) for x, y in v])))
b = vs.draw(ax, parts, at=(ox, oy), scale=1.1, level="series")
hole((ox + 4.85 * 1.1, oy + 1.85 * 1.1), 0.75, 0.55)
hole((ox + 4.85 * 1.1, oy - 1.85 * 1.1), 0.75, 0.55)
hole((ox + 1.2 * 1.1, oy + 1.35 * 1.1), 0.22, 0.15)
hole((ox + 1.2 * 1.1, oy - 1.35 * 1.1), 0.22, 0.15)
hole((ox + 6.8 * 1.1, oy), 0.12, 0.12)
vs.callout(ax, (ox + 6.8 * 1.1, oy), (ox + 11.6, oy - 1.2), "pineal foramen")
for key, (tx, ty) in (("nasal", (ox + 2.5, oy + 4.4)), ("frontal", (ox + 5.0, oy + 4.4)), ("parietal", (ox + 7.6, oy + 4.4)),
                      ("postparietal", (ox + 10.4, oy + 4.0)), ("tabular", (ox + 11.4, oy + 2.9)), ("squamosal", (ox + 11.4, oy + 1.6))):
    vs.callout(ax, b[key], (tx, ty), key)
bio.panel(ax, "B", (15.0, 10.2))
vs.legend(ax, [("maxilla", "marginal"), ("frontal", "roof"), ("postorbital", "circumorbital"), ("squamosal", "temporal and cheek"),
               ("dentary", "lower jaw (dermal)"), ("articular", "articular")], at=(0.5, 1.2), width=26.0, ncols=6, level="series")
