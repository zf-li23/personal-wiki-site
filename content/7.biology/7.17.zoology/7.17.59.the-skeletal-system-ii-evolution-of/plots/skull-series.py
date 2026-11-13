# The skull from a lobe-finned fish to a mammal, schematic left lateral views (anterior to the left), each bone
# in its course-wide homology colour: an osteolepiform fish (Eusthenopteron-like; short snout, opercular bones),
# an early tetrapod (Acanthostega-like; long snout, opercular series lost), an early synapsid (lower temporal
# fenestra; intertemporal lost), a lizard (upper fenestra; lower temporal bar and quadratojugal lost, quadrate
# exposed and movable) and a dog (zygomatic arch, orbit confluent with the temporal fossa, dentary only).
# After Clack (2012), Romer & Parsons, Kardong (2019). Not to scale.
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P
LAT = {
    "premaxilla": [(0.0, 1.2), (0.3, 2.2), (1.0, 2.6), (1.5, 1.9), (1.5, 0.7), (0.6, 0.7)],
    "nasal": [(1.0, 2.6), (2.0, 3.2), (3.6, 3.55), (3.6, 2.9), (1.5, 1.9)],
    "maxilla": [(1.5, 0.7), (1.5, 1.9), (2.8, 2.0), (3.6, 1.5), (5.5, 1.2), (6.2, 0.7)],
    "lacrimal": [(1.5, 1.9), (3.6, 2.9), (4.3, 2.8), (4.25, 1.75), (3.6, 1.5), (2.8, 2.0)],
    "prefrontal": [(3.6, 2.9), (3.6, 3.55), (4.8, 3.75), (4.6, 3.25), (4.0, 2.7)],
    "frontal": [(4.3, 2.8), (4.6, 3.25), (4.8, 3.75), (6.4, 3.86), (6.3, 3.35), (5.6, 3.0), (5.0, 3.05)],
    "postfrontal": [(6.3, 3.35), (6.4, 3.86), (7.0, 3.88), (6.9, 3.2), (6.2, 2.9), (5.6, 3.0)],
    "postorbital": [(6.2, 2.9), (6.9, 3.2), (7.6, 2.9), (7.4, 2.0), (6.3, 1.9), (5.8, 1.85), (5.9, 2.4)],
    "jugal": [(3.6, 1.5), (4.25, 1.75), (4.5, 1.5), (5.5, 1.45), (5.8, 1.85), (6.3, 1.9), (7.4, 2.0), (8.4, 1.5),
              (8.4, 0.65), (6.2, 0.7), (5.5, 1.2)],
    "intertemporal": [(6.9, 3.2), (7.0, 3.88), (8.0, 3.86), (8.0, 3.0), (7.6, 2.9)],
    "supratemporal": [(8.0, 3.0), (8.0, 3.86), (9.2, 3.7), (9.3, 2.85)],
    "tabular": [(9.3, 2.85), (9.2, 3.7), (9.9, 3.5), (10.0, 2.7)],
    "squamosal": [(7.6, 2.9), (8.0, 3.0), (9.3, 2.85), (10.0, 2.7), (10.0, 2.0), (8.4, 1.5), (7.4, 2.0)],
    "quadratojugal": [(8.4, 0.65), (9.8, 0.6), (10.0, 2.0), (8.4, 1.5)],
    "dentary": [(0.7, 0.58), (6.6, 0.56), (7.6, 0.18), (6.0, -0.25), (1.2, 0.08)],
    "angular": [(6.0, -0.25), (7.6, 0.18), (9.7, 0.3), (9.0, -0.12)],
    "surangular": [(6.6, 0.56), (9.7, 0.52), (9.7, 0.3), (7.6, 0.18)],
    "articular": [(9.7, 0.52), (10.25, 0.48), (10.25, 0.22), (9.7, 0.3)],
}
ORBIT = (5.0, 2.35)


def tx(pts, f):
    return [f(x, y) for x, y in pts]


def hole(c, rx, ry, at, s):
    pts = np.array(vs.oval((at[0] + c[0] * s, at[1] + c[1] * s), rx * s, ry * s))
    ax.fill(pts[:, 0], pts[:, 1], color=P.surface(), zorder=20, lw=0)
    ax.plot(np.r_[pts[:, 0], pts[0, 0]], np.r_[pts[:, 1], pts[0, 1]], color=P.ink(), lw=0.8, zorder=21)


titles = ["Osteolepiform", "Early tetrapod", "Early synapsid", "Lizard", "Dog"]
subs = ["opercular bones; short snout", "long snout; no opercular", "lower temporal fenestra",
        "upper fenestra; lower bar lost", "zygomatic arch; dentary only"]
fig, ax, boxes = vs.panels(5, 7.4, 4.4, titles=titles, subtitles=subs, ncols=5, legend_rows=3, gap=0.5)
s = 0.62

# fish: compress the snout
fishf = lambda x, y: (x * 0.75 if x < 5 else 3.75 + (x - 5) * 1.0, y)
fish = [(k, vs.poly(tx(v, fishf))) for k, v in LAT.items()]
fish += [("preoperculum", vs.poly([(9.0, 2.6), (9.4, 2.6), (9.3, 0.6), (8.9, 0.6)])),
         ("operculum", vs.smooth([(9.9, 3.4), (11.6, 3.2), (11.7, 2.0), (10.0, 1.7)])),
         ("suboperculum", vs.smooth([(10.0, 1.6), (11.6, 1.9), (11.3, 0.9), (10.0, 0.8)]))]
at = (boxes[0][0] + 0.1, boxes[0][1] + 0.9)
vs.draw(ax, fish, at=at, scale=s * 0.86)
hole((ORBIT[0] * 0.75 + 0.05, ORBIT[1]), 0.6, 0.55, at, s * 0.86)

at = (boxes[1][0] + 0.2, boxes[1][1] + 0.9)
vs.draw(ax, [(k, vs.poly(v)) for k, v in LAT.items()], at=at, scale=s)
hole(ORBIT, 0.8, 0.7, at, s)

syn = {k: v for k, v in LAT.items() if k != "intertemporal"}
syn["postfrontal"] = [(6.3, 3.35), (6.4, 3.86), (8.0, 3.86), (8.0, 3.0), (6.9, 3.2), (6.2, 2.9), (5.6, 3.0)]
at = (boxes[2][0] + 0.2, boxes[2][1] + 0.9)
vs.draw(ax, [(k, vs.poly(v)) for k, v in syn.items()], at=at, scale=s)
hole(ORBIT, 0.8, 0.7, at, s)
hole((8.1, 1.7), 0.6, 0.45, at, s)

liz = {k: v for k, v in LAT.items() if k not in ("intertemporal", "tabular", "quadratojugal")}
liz["jugal"] = [(3.6, 1.5), (4.25, 1.75), (4.5, 1.5), (5.5, 1.45), (5.8, 1.85), (6.3, 1.9), (7.4, 2.0), (7.6, 1.6),
                (6.6, 0.75), (6.2, 0.7), (5.5, 1.2)]
liz["squamosal"] = [(7.6, 2.9), (8.0, 3.0), (9.3, 2.85), (9.9, 2.8), (9.9, 2.4), (8.6, 2.3), (7.5, 2.4)]
at = (boxes[3][0] + 0.2, boxes[3][1] + 0.9)
lz = [(k, vs.poly(v)) for k, v in liz.items()] + [("quadrate", vs.rod((9.75, 2.5), (9.95, 0.55), 0.35))]
vs.draw(ax, lz, at=at, scale=s)
hole(ORBIT, 0.85, 0.75, at, s)
hole((8.4, 3.35), 0.5, 0.25, at, s)

dog = [("occipital", vs.smooth([(8.6, 3.6), (9.4, 3.0), (9.3, 2.2), (8.6, 2.3)])),
       ("tympanic", vs.oval((7.9, 1.75), 0.45, 0.3)),
       ("nasal", vs.poly([(0.6, 3.0), (3.2, 3.6), (3.4, 3.3), (0.8, 2.75)])),
       ("frontal", vs.poly([(3.2, 3.6), (5.6, 4.2), (5.8, 3.5), (3.4, 3.3)])),
       ("parietal", vs.poly([(5.6, 4.2), (8.2, 4.1), (8.6, 3.6), (7.6, 3.0), (5.8, 3.5)])),
       ("premaxilla", vs.poly([(0.2, 2.3), (0.8, 2.75), (1.5, 2.6), (1.2, 1.9), (0.4, 1.9)])),
       ("maxilla", vs.poly([(1.3, 1.9), (1.5, 2.6), (3.3, 3.25), (4.0, 2.8), (4.0, 2.4), (4.4, 1.9)])),
       ("lacrimal", vs.poly([(3.3, 3.25), (4.0, 3.4), (4.2, 2.9), (4.0, 2.8)])),
       ("jugal", vs.poly([(4.0, 2.4), (6.4, 2.3), (6.5, 2.0), (4.4, 1.9)])),
       ("squamosal", vs.poly([(5.8, 3.5), (7.6, 3.0), (7.6, 2.2), (6.5, 2.0), (6.4, 2.3), (6.6, 2.9)])),
       ("dentary", vs.smooth([(0.4, 1.7), (4.4, 1.6), (6.4, 1.9), (7.0, 2.6), (7.3, 2.3), (7.2, 1.2), (6.6, 0.7),
                              (3.5, 0.9), (0.6, 1.3)]))]
at = (boxes[4][0] + 0.3, boxes[4][1] + 0.5)
vs.draw(ax, dog, at=at, scale=s * 1.05)
bio.label(ax, (at[0] + 5.3 * s * 1.05, at[1] + 3.0 * s * 1.05), "orbit +\ntemporal fossa", size="tiny", color=P.muted())

vs.legend(ax, ["premaxilla", "maxilla", "nasal", "frontal", "parietal", "lacrimal", "prefrontal", "postfrontal",
               "postorbital", "jugal", "intertemporal", "supratemporal", "tabular", "squamosal", "quadratojugal",
               ("quadrate", "quadrate"), "operculum", "dentary", "angular", ("tympanic", "angular = tympanic (mammal)"),
               "surangular", "articular", "occipital"], at=(0.4, 3 * 0.55 + 0.3), width=38.0, ncols=8)
