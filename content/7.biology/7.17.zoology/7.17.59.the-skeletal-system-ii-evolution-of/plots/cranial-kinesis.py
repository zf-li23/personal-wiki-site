# Cranial kinesis, schematic left lateral views (anterior to the left) after Frazzetta (1962), Bout & Zweers
# (2001) and Kardong (2019): lizard (streptostyly and mesokinesis), snake (mobile quadrate, maxilla and
# pterygoid; mandibles joined by elastic tissue), bird (prokinesis driven by the quadrate through the jugal and
# pterygoid-palatine bars). Open circles: movable joints; arrows: movements on opening the mouth. Not to scale.
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P
fig, ax, boxes = vs.panels(3, 9.0, 5.6, titles=["Lizard", "Snake", "Bird"],
                           subtitles=["streptostyly + mesokinesis", "highly kinetic skull", "prokinesis"], ncols=3)


def joint(p):
    c = np.array(vs.oval(p, 0.17, 0.17))
    ax.fill(c[:, 0], c[:, 1], color=P.surface(), zorder=30)
    ax.plot(np.r_[c[:, 0], c[0, 0]], np.r_[c[:, 1], c[0, 1]], color=P.ink(), lw=1.1, zorder=31)


def mv(a, b, bend=0.0):
    bio.arrow(ax, a, b, kind="process", bend=bend, color=P.fill("negative"), lw=1.6, zorder=32)


x, y, w, h = boxes[0]
o = (x + 0.3, y + 0.6)
parts = [("chondrocranium", vs.smooth([(5.2, 2.4), (8.2, 2.6), (8.4, 1.8), (5.4, 1.7)]), {"state": "context"}),
         ("parietal", vs.poly([(5.2, 3.6), (8.2, 3.5), (8.3, 3.0), (5.2, 3.1)])),
         ("frontal", vs.poly([(2.6, 3.5), (5.1, 3.65), (5.1, 3.1), (2.8, 3.0)])),
         ("nasal", vs.poly([(0.6, 2.7), (2.6, 3.5), (2.8, 3.0), (0.9, 2.4)])),
         ("maxilla", vs.poly([(0.4, 2.2), (0.9, 2.4), (4.6, 2.0), (4.8, 1.6), (0.6, 1.7)])),
         ("postorbital", vs.poly([(5.2, 3.1), (5.6, 3.1), (5.3, 2.0), (4.9, 2.0)])),
         ("quadrate", vs.rod((8.0, 3.2), (7.7, 1.2), 0.32)),
         ("dentary", vs.poly([(0.6, 1.5), (6.0, 1.4), (7.5, 1.0), (6.0, 0.6), (0.8, 1.0)])),
         ("articular", vs.oval((7.6, 1.05), 0.3, 0.2))]
a = vs.draw(ax, parts, at=o)
joint((o[0] + 5.15, o[1] + 3.35)); joint((o[0] + 8.0, o[1] + 3.2)); joint((o[0] + 7.7, o[1] + 1.2))
mv((o[0] + 7.6, o[1] + 0.4), (o[0] + 6.8, o[1] + 0.4))
mv((o[0] + 1.4, o[1] + 3.4), (o[0] + 1.2, o[1] + 4.3), bend=0.2)
vs.callout(ax, (o[0] + 5.15, o[1] + 3.35), (o[0] + 5.6, o[1] + 4.7), "mesokinetic joint")
vs.callout(ax, a["quadrate"], (o[0] + 8.5, o[1] - 0.2), "quadrate")

x, y, w, h = boxes[1]
o = (x + 0.3, y + 0.6)
parts = [("chondrocranium", vs.smooth([(3.6, 3.2), (8.0, 3.4), (8.2, 2.5), (3.8, 2.4)]), {"state": "context"}),
         ("parietal", vs.poly([(3.6, 3.6), (8.0, 3.7), (8.0, 3.3), (3.6, 3.2)])),
         ("supratemporal", vs.rod((7.4, 3.7), (8.8, 3.3), 0.22)),
         ("quadrate", vs.rod((8.8, 3.3), (8.4, 1.2), 0.26)),
         ("maxilla", vs.rod((0.8, 2.3), (3.6, 2.2), 0.3)),
         ("pterygoid", vs.rod((3.6, 2.0), (8.2, 1.5), 0.25)),
         ("dentary", vs.rod((0.8, 1.2), (5.5, 1.0), 0.35)),
         ("articular", vs.rod((5.5, 1.0), (8.4, 1.05), 0.3))]
a = vs.draw(ax, parts, at=o)
for p in ((7.4, 3.7), (8.8, 3.3), (8.4, 1.2), (3.6, 2.2), (3.6, 2.0), (5.5, 1.0)):
    joint((o[0] + p[0], o[1] + p[1]))
mv((o[0] + 2.0, o[1] + 0.6), (o[0] + 0.8, o[1] + 0.5))
vs.callout(ax, (o[0] + 0.8, o[1] + 1.2), (o[0] + 1.2, o[1] - 0.3), "mandibles joined by elastic tissue")
vs.callout(ax, a["quadrate"], (o[0] + 8.9, o[1] + 0.2), "quadrate")

x, y, w, h = boxes[2]
o = (x + 0.3, y + 0.6)
parts = [("chondrocranium", vs.smooth([(4.4, 3.0), (6.6, 4.2), (8.6, 3.8), (8.6, 2.2), (6.0, 2.0)]), {"state": "context"}),
         ("frontal", vs.smooth([(3.8, 3.3), (6.6, 4.3), (8.0, 4.2), (6.4, 3.6), (4.0, 3.0)])),
         ("premaxilla", vs.poly([(0.2, 2.1), (3.8, 3.4), (3.9, 2.9), (0.4, 2.0)])),
         ("maxilla", vs.poly([(1.6, 2.2), (3.8, 2.8), (3.8, 2.4), (2.0, 2.0)])),
         ("jugal", vs.rod((3.8, 2.4), (7.6, 1.6), 0.14)),
         ("palatine", vs.rod((3.6, 2.15), (6.0, 1.95), 0.14)),
         ("pterygoid", vs.rod((6.0, 1.95), (7.5, 1.85), 0.16)),
         ("quadrate", vs.rod((7.9, 2.7), (7.6, 1.6), 0.32)),
         ("dentary", vs.poly([(0.3, 1.8), (5.6, 1.3), (7.4, 1.3), (5.6, 1.0), (0.5, 1.6)])),
         ("articular", vs.oval((7.5, 1.35), 0.25, 0.18))]
a = vs.draw(ax, parts, at=o)
for p in ((3.85, 3.2), (7.9, 2.7), (7.6, 1.6), (3.8, 2.4)):
    joint((o[0] + p[0], o[1] + p[1]))
mv((o[0] + 8.3, o[1] + 1.4), (o[0] + 8.0, o[1] + 2.2), bend=-0.3)
mv((o[0] + 6.6, o[1] + 1.35), (o[0] + 5.2, o[1] + 1.55))
mv((o[0] + 0.9, o[1] + 2.4), (o[0] + 0.9, o[1] + 3.3), bend=0.2)
vs.callout(ax, (o[0] + 3.85, o[1] + 3.2), (o[0] + 2.6, o[1] + 4.7), "nasofrontal hinge")
vs.callout(ax, a["jugal"], (o[0] + 5.0, o[1] + 0.2), "jugal bar")
