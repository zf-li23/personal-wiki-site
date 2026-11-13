# Foot postures of mammals: left hindlimb in lateral view, anterior to the left (schematic, after Kardong
# 2019 and Hildebrand and Goslow 2001; not to scale). Plantigrade (human, bear, rodents): the whole sole,
# from heel to toes, rests on the ground. Digitigrade (dog, cat): the animal stands on its toes, the heel and
# metatarsals raised. Unguligrade (horse, deer): the animal stands on the tips of the toes, which bear hooves;
# the metatarsals are long, and in the horse a single digit (III) remains, in the deer two (III, IV). The
# distal segments lengthen from left to right, lengthening the stride. Bones in the course-wide homology
# colours (femur, tibia and fibula, tarsals, metatarsals, phalanges).
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P
fig, ax, boxes = vs.panels(3, 6.5, 8.0, titles=["Plantigrade", "Digitigrade", "Unguligrade"],
                           subtitles=["human, bear, rodents", "dog, cat", "horse, deer"], legend_rows=1, gap=1.0)


def limb(x, y, pts, widths, hoof=False):
    keys = ["femur", "tibia", "tarsals", "metatarsals", "phalanges"]
    parts = []
    for k, (a, b), w in zip(keys, zip(pts[:-1], pts[1:]), widths):
        parts.append((k, vs.rod(a, b, w)))
    parts.append(("fibula", vs.rod((pts[1][0] + 0.25, pts[1][1] - 0.3), (pts[2][0] + 0.2, pts[2][1] + 0.4), 0.12)))
    if hoof:
        tip = pts[-1]
        parts.append(("phalanges", vs.poly([(tip[0] - 0.45, tip[1] - 0.05), (tip[0] + 0.25, tip[1] - 0.05),
                                             (tip[0] + 0.15, tip[1] + 0.45), (tip[0] - 0.3, tip[1] + 0.4)]),
                      {"state": "highlight"}))
    a = vs.draw(ax, parts, at=(x, y))
    ax.plot([x - 0.2, x + 6.4], [y, y], color=P.muted(), lw=1.4)
    return a


x, y, w, h = boxes[0]
limb(x, y + 0.3, [(3.5, 7.6), (3.2, 4.6), (3.7, 1.7), (4.0, 0.25), (2.7, 0.15), (1.6, 0.12)], [0.5, 0.4, 0.45, 0.3, 0.2])
vs.callout(ax, (x + 4.0, y + 0.55), (x + 5.8, y + 2.0), "heel on ground")
x, y, w, h = boxes[1]
limb(x, y + 0.3, [(3.2, 7.6), (3.8, 5.0), (3.0, 2.6), (3.4, 2.0), (2.4, 0.2), (1.6, 0.1)], [0.5, 0.4, 0.4, 0.3, 0.2])
vs.callout(ax, (x + 3.4, y + 2.4), (x + 5.8, y + 3.2), "heel raised (hock)")
x, y, w, h = boxes[2]
limb(x, y + 0.3, [(3.0, 7.6), (3.7, 5.8), (2.9, 3.9), (3.15, 3.4), (2.6, 0.9), (2.3, 0.3)], [0.55, 0.45, 0.4, 0.32, 0.25], hoof=True)
vs.callout(ax, (x + 2.3, y + 0.6), (x + 5.0, y + 1.0), "hoof on digit III")
vs.callout(ax, (x + 2.9, y + 2.4), (x + 5.4, y + 2.9), "long metatarsal (cannon bone)")
vs.legend(ax, ["femur", ("tibia", "tibia"), ("fibula", "fibula"), ("tarsals", "tarsals"),
               ("metatarsals", "metatarsals"), ("phalanges", "phalanges")], at=(0.4, 0.55 + 0.25), width=21.0, ncols=6)
