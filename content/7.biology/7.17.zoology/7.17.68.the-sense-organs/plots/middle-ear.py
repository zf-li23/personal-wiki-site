# Evolution of the middle ear: jaw joint and ear region in five stages, bones in the homology colours of
# vertskel (lateral views, anterior to the left). Schematic, not to scale.
import vertskel as vs

titles = ["A  Fish", "B  Early tetrapod", "C  Lizard", "D  Cynodont", "E  Mammal"]
fig, ax, boxes = vs.panels(5, 4.8, 4.6, titles=titles, ncols=5, legend_rows=2)
R, O, S, P_ = vs.rod, vs.oval, vs.smooth, vs.poly


def otic(x):
    return ("otic_capsule", O((3.9, 3.1), 0.7, 0.55))


stages = [
    [otic(0), ("hyomandibula", R((3.6, 3.3), (2.7, 1.5), 0.35)), ("palatoquadrate", S([(0.3, 2.3), (2.0, 2.7), (2.8, 2.0), (2.6, 1.6), (0.4, 1.9)])),
     ("meckel", S([(0.3, 1.5), (2.5, 1.6), (2.9, 1.1), (0.4, 1.0)]))],
    [otic(0), ("stapes", R((3.4, 3.0), (2.4, 2.4), 0.45)), ("quadrate", O((2.2, 2.0), 0.35, 0.5)),
     ("dentary", P_([(0.2, 1.4), (2.0, 1.55), (2.0, 1.1), (0.2, 1.0)])), ("articular", O((2.25, 1.3), 0.3, 0.25)),
     ("angular", P_([(1.0, 0.95), (2.1, 1.05), (2.0, 0.75), (1.1, 0.7)]))],
    [otic(0), ("columella", R((3.4, 3.0), (2.2, 2.7), 0.14)), ("quadrate", O((2.0, 2.2), 0.28, 0.55)),
     ("dentary", P_([(0.2, 1.5), (1.7, 1.6), (1.7, 1.2), (0.2, 1.1)])), ("articular", O((2.0, 1.45), 0.28, 0.22)),
     ("angular", P_([(1.0, 1.1), (1.95, 1.2), (1.9, 0.95), (1.1, 0.9)]))],
    [otic(0), ("stapes", R((3.4, 3.0), (2.4, 2.4), 0.16)), ("quadrate", O((2.3, 2.1), 0.2, 0.3)),
     ("squamosal", P_([(1.6, 2.8), (2.9, 2.9), (2.9, 2.4), (1.7, 2.3)])),
     ("dentary", P_([(0.2, 1.5), (2.0, 1.7), (2.1, 2.3), (2.3, 1.9), (2.0, 1.2), (0.2, 1.1)])),
     ("articular", O((2.35, 1.75), 0.18, 0.14)), ("angular", P_([(1.4, 1.2), (2.3, 1.55), (2.25, 1.35), (1.5, 1.05)]))],
    [otic(0), ("stapes", R((3.3, 3.0), (2.85, 2.75), 0.1)), ("incus", O((2.7, 2.85), 0.14, 0.18)),
     ("malleus", O((2.5, 2.7), 0.2, 0.12)), ("tympanic", O((2.35, 2.45), 0.32, 0.2)),
     ("squamosal", P_([(1.2, 3.0), (2.2, 3.1), (2.2, 2.6), (1.3, 2.5)])),
     ("dentary", P_([(0.2, 1.4), (1.6, 1.6), (1.7, 2.45), (1.9, 2.4), (1.9, 1.3), (0.2, 1.0)]))],
]
for (x, y, w, h), parts in zip(boxes, stages):
    vs.draw(ax, parts, at=(x + 0.2, y + 0.2), scale=1.0)
vs.legend(ax, [("hyomandibula", "hyomandibula / columella / stapes"), ("palatoquadrate", "palatoquadrate / quadrate / incus"),
               ("meckel", "Meckel's cartilage / articular / malleus"), ("angular", "angular / tympanic"),
               ("dentary", "dentary"), ("squamosal", "squamosal"), ("otic_capsule", "otic capsule")],
          at=(0.6, 1.3), width=24, ncols=4)
