# The three components of the skull in a shark (Squalus-like), a bony fish (generalized teleost) and a mammal
# (dog-like), schematic left lateral views, anterior to the left, coloured by component (vertskel
# level="component"): chondrocranium sand, splanchnocranium warm, dermatocranium blue. After Kardong (2019)
# and Romer & Parsons. Not to scale.
import wikibio as bio
import vertskel as vs

P = bio.P
fig, ax, boxes = vs.panels(3, 10.5, 6.2, titles=["Shark", "Bony fish", "Mammal"],
                           subtitles=["cartilaginous skull", "dermal bones cover the braincase and jaws",
                                      "dermal bones form most of the skull"], ncols=3, legend_rows=1)
L = dict(level="component")

shark = [
    ("chondrocranium", vs.smooth([(0.3, 3.6), (1.5, 4.4), (5.0, 4.7), (7.6, 4.5), (8.3, 3.7), (7.8, 3.1), (2.2, 3.1), (0.9, 3.2)])),
    ("palatoquadrate", vs.smooth([(2.2, 2.9), (4.0, 3.2), (6.4, 3.0), (6.9, 2.5), (4.2, 2.35), (2.3, 2.5)])),
    ("meckel", vs.smooth([(2.2, 2.2), (6.9, 2.3), (7.0, 1.8), (4.5, 1.35), (2.2, 1.8)])),
    ("hyomandibula", vs.rod((7.7, 3.1), (7.1, 2.0), 0.35)),
    ("ceratohyal", vs.rod((7.0, 1.6), (4.8, 0.9), 0.3)),
]
for k in range(5):
    shark.append(("arch_%d" % (k + 3), vs.rod((8.3 + 0.42 * k, 3.1), (8.0 + 0.42 * k, 0.9), 0.22)))
x, y, w, h = boxes[0]
vs.draw(ax, shark, at=(x, y + 0.3), level="component")

fish = [
    ("chondrocranium", vs.smooth([(1.0, 3.3), (2.5, 4.1), (7.0, 4.3), (8.0, 3.5), (7.0, 3.0), (2.0, 3.0)]), {"z": 4}),
    ("hyomandibula", vs.rod((6.4, 3.2), (6.0, 2.0), 0.4), {"z": 5}),
    ("quadrate", vs.oval((4.7, 1.75), 0.45, 0.35), {"z": 6}),
    ("articular", vs.oval((4.4, 1.35), 0.4, 0.25), {"z": 7}),
    ("nasal", vs.poly([(1.0, 3.5), (2.3, 4.2), (2.8, 3.9), (1.6, 3.2)]), {"z": 8}),
    ("frontal", vs.poly([(2.3, 4.2), (5.2, 4.55), (5.3, 4.0), (2.8, 3.9)]), {"z": 8}),
    ("parietal", vs.poly([(5.2, 4.55), (6.8, 4.45), (6.9, 3.95), (5.3, 4.0)]), {"z": 8}),
    ("premaxilla", vs.poly([(0.4, 2.6), (1.4, 3.1), (1.6, 2.7), (0.6, 2.2)]), {"z": 8}),
    ("maxilla", vs.poly([(1.4, 3.0), (3.9, 2.4), (3.9, 2.05), (1.4, 2.6)]), {"z": 8}),
    ("dentary", vs.poly([(0.6, 2.1), (3.6, 1.2), (3.9, 1.65), (1.0, 2.4)]), {"z": 8}),
    ("angular", vs.poly([(3.6, 1.2), (4.6, 1.15), (4.4, 1.6), (3.9, 1.65)]), {"z": 8}),
    ("lacrimal", vs.poly([(1.7, 3.15), (2.8, 3.25), (2.7, 2.7), (1.8, 2.75)]), {"z": 8}),
    ("jugal", vs.poly([(2.8, 2.6), (4.5, 2.4), (4.6, 2.8), (3.0, 2.95)]), {"z": 8}),
    ("postorbital", vs.poly([(4.5, 2.8), (4.7, 3.7), (5.2, 3.6), (5.0, 2.6)]), {"z": 8}),
    ("preoperculum", vs.poly([(5.6, 3.6), (6.0, 3.6), (5.6, 1.2), (4.9, 1.0), (5.2, 1.4)]), {"z": 9}),
    ("operculum", vs.smooth([(6.1, 3.6), (8.0, 3.5), (8.2, 2.5), (6.4, 2.1), (6.0, 2.6)]), {"z": 9}),
    ("suboperculum", vs.smooth([(6.0, 2.0), (8.1, 2.3), (7.8, 1.6), (6.0, 1.3)]), {"z": 9}),
    ("interoperculum", vs.smooth([(5.0, 1.0), (5.9, 1.25), (5.9, 0.8), (5.0, 0.65)]), {"z": 9}),
]
x, y, w, h = boxes[1]
a = vs.draw(ax, fish, at=(x + 0.6, y + 0.6), level="component")
bio.label(ax, (x + 3.9, y + 3.45), "orbit", size="tiny", color=P.muted())
vs.callout(ax, a["operculum"], (x + 9.6, y + 4.8), "opercular series")
vs.callout(ax, a["hyomandibula"], (x + 9.6, y + 0.6), "hyomandibula (under opercle)")

mam = [
    ("occipital", vs.smooth([(8.6, 3.6), (9.4, 3.0), (9.3, 2.2), (8.6, 2.3)])),
    ("petrosal", vs.oval((8.0, 2.1), 0.45, 0.3)),
    ("tympanic", vs.oval((7.9, 1.75), 0.45, 0.3)),
    ("nasal", vs.poly([(0.6, 3.0), (3.2, 3.6), (3.4, 3.3), (0.8, 2.75)])),
    ("frontal", vs.poly([(3.2, 3.6), (5.6, 4.2), (5.8, 3.5), (3.4, 3.3)])),
    ("parietal", vs.poly([(5.6, 4.2), (8.2, 4.1), (8.6, 3.6), (7.6, 3.0), (5.8, 3.5)])),
    ("interparietal", vs.poly([(8.2, 4.1), (8.9, 3.8), (8.6, 3.6)])),
    ("premaxilla", vs.poly([(0.2, 2.3), (0.8, 2.75), (1.5, 2.6), (1.2, 1.9), (0.4, 1.9)])),
    ("maxilla", vs.poly([(1.3, 1.9), (1.5, 2.6), (3.3, 3.25), (4.0, 2.8), (4.0, 2.4), (4.4, 1.9)])),
    ("lacrimal", vs.poly([(3.4, 3.3), (4.0, 3.4), (4.2, 2.9), (4.0, 2.8)])),
    ("jugal", vs.poly([(4.0, 2.4), (6.4, 2.3), (6.5, 2.0), (4.4, 1.9)])),
    ("squamosal", vs.poly([(5.8, 3.5), (7.6, 3.0), (7.6, 2.2), (6.5, 2.0), (6.4, 2.3), (6.6, 2.9)])),
    ("dentary", vs.smooth([(0.4, 1.7), (4.4, 1.6), (6.4, 1.9), (7.0, 2.6), (7.3, 2.3), (7.2, 1.2), (6.6, 0.7), (3.5, 0.9), (0.6, 1.3)])),
    ("hyoid", vs.rod((6.0, 0.4), (7.8, 1.2), 0.18)),
    ("styloid", vs.rod((7.9, 1.4), (7.8, 1.2), 0.12)),
]
x, y, w, h = boxes[2]
a = vs.draw(ax, mam, at=(x + 0.4, y + 0.8), level="component")
bio.label(ax, (x + 5.5, y + 3.75), "orbit", size="tiny", color=P.muted())
vs.callout(ax, a["dentary"], (x + 2.8, y + 0.2), "dentary")
vs.callout(ax, a["hyoid"], (x + 9.6, y + 0.4), "hyoid")
vs.callout(ax, a["tympanic"], (x + 9.8, y + 1.7), "tympanic (from angular)")
vs.callout(ax, a["occipital"], (x + 10.0, y + 4.6), "occipital")
vs.legend(ax, [("frontal", "dermatocranium"), ("chondrocranium", "chondrocranium"),
               ("quadrate", "splanchnocranium")], at=(0.5, 0.8), width=30.0, ncols=3, level="component")
