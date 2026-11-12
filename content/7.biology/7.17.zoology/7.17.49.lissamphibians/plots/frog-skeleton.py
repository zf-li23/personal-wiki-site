# Jumping adaptations of the frog skeleton, compared with a salamander; schematic dorsal views, anterior
# at the top, left limbs only, not to scale. Frog: short trunk of 8 presacral vertebrae without ribs, the
# postsacral vertebrae fused into the urostyle, long ilia reaching forward to the sacral diapophyses,
# radius and ulna fused (radioulna), tibia and fibula fused (tibiofibula), and the elongated proximal
# tarsals (astragalus and calcaneum) adding a lever segment to the hindlimb. Salamander: long trunk with
# ribs, a tail, short ilia and separate zeugopod bones. Colours follow the course-wide homology scheme.
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P
fig, ax, boxes = vs.panels(2, 10.0, 12.5, titles=["A  Salamander", "B  Frog"], ncols=2, legend_rows=2)

# ---------------- salamander
x, y, w, h = boxes[0]
parts = [("chondrocranium", vs.smooth([(4.2, 11.6), (5.0, 12.2), (5.8, 11.6), (5.9, 10.5), (5.0, 10.1),
                                       (4.1, 10.5)]), {"state": "context"})]
yy = 9.8
for k in range(16):
    parts.append(("centrum", vs.oval((5.0, yy), 0.32, 0.22)))
    if k < 14:
        parts.append(("rib", vs.rod((5.3, yy), (6.0, yy - 0.15), 0.1)))
        parts.append(("rib", vs.rod((4.7, yy), (4.0, yy - 0.15), 0.1)))
    yy -= 0.42
sac = yy + 0.42
parts.append(("ilium", vs.rod((4.65, sac), (4.0, sac - 0.6), 0.22)))
for k in range(8):
    parts.append(("centrum", vs.oval((5.0, sac - 0.45 - k * 0.38), 0.25 - k * 0.02, 0.17)))
parts += [("scapulocoracoid", vs.oval((4.3, 9.4), 0.35, 0.5)),
          ("humerus", vs.rod((4.1, 9.3), (2.9, 8.7), 0.22)),
          ("radius", vs.rod((2.85, 8.6), (2.4, 7.8), 0.13)), ("ulna", vs.rod((3.05, 8.6), (2.7, 7.75), 0.13)),
          ("carpals", vs.oval((2.5, 7.55), 0.25, 0.15))]
for k in range(4):
    parts.append(("phalanges", vs.rod((2.25 + k * 0.17, 7.45), (1.9 + k * 0.3, 6.9), 0.07)))
hy = sac - 0.6
parts += [("femur", vs.rod((4.0, hy), (2.8, hy - 0.6), 0.24)),
          ("tibia", vs.rod((2.75, hy - 0.7), (2.35, hy - 1.5), 0.14)),
          ("fibula", vs.rod((2.95, hy - 0.7), (2.65, hy - 1.5), 0.14)),
          ("tarsals", vs.oval((2.45, hy - 1.75), 0.27, 0.16))]
for k in range(5):
    parts.append(("phalanges", vs.rod((2.15 + k * 0.15, hy - 1.85), (1.7 + k * 0.28, hy - 2.5), 0.07)))
a = vs.draw(ax, parts, at=(x, y))
vs.callout(ax, a["ilium"], (x + 8.0, y + sac - 1.0), "short ilium")
vs.callout(ax, a["rib"], (x + 8.0, y + 8.4), "ribs")
bio.label(ax, (x + 6.2, y + 1.6), "tail", size="tiny", ha="left")

# ---------------- frog
x, y, w, h = boxes[1]
parts = [("chondrocranium", vs.smooth([(3.6, 11.4), (5.0, 12.4), (6.4, 11.4), (6.3, 10.4), (5.0, 10.0),
                                       (3.7, 10.4)]), {"state": "context"})]
yy = 9.8
for k in range(8):
    parts.append(("centrum", vs.oval((5.0, yy), 0.33, 0.24)))
    parts.append(("transverse_process", vs.rod((5.3, yy), (6.1 if k != 7 else 6.3, yy + (0.1 if k == 7 else 0)),
                                               0.11 if k != 7 else 0.2)))
    parts.append(("transverse_process", vs.rod((4.7, yy), (3.9 if k != 7 else 3.7, yy + (0.1 if k == 7 else 0)),
                                               0.11 if k != 7 else 0.2)))
    yy -= 0.5
sac = yy + 0.5
parts.append(("centrum", vs.rod((5.0, sac - 0.3), (5.0, sac - 3.6), 0.26, 0.12), {"state": "highlight"}))
parts.append(("ilium", vs.rod((3.75, sac + 0.05), (4.55, sac - 3.5), 0.22)))
parts.append(("ilium", vs.rod((6.25, sac + 0.05), (5.45, sac - 3.5), 0.22)))
parts.append(("puboischiadic", vs.oval((5.0, sac - 3.7), 0.6, 0.35)))
parts += [("scapulocoracoid", vs.oval((4.0, 9.3), 0.45, 0.5)),
          ("humerus", vs.rod((3.8, 9.2), (2.7, 8.4), 0.25)),
          ("radius", vs.rod((2.7, 8.3), (2.4, 7.4), 0.2), {"text": None}),
          ("carpals", vs.oval((2.35, 7.15), 0.25, 0.15))]
for k in range(4):
    parts.append(("phalanges", vs.rod((2.1 + k * 0.17, 7.0), (1.7 + k * 0.3, 6.4), 0.08)))
hy = sac - 3.7
parts += [("femur", vs.rod((4.5, hy), (2.4, hy + 1.2), 0.26)),
          ("tibia", vs.rod((2.35, hy + 1.1), (1.0, hy - 0.8), 0.24)),
          ("tarsals", vs.rod((1.0, hy - 0.9), (1.9, hy - 2.1), 0.16)),
          ("tarsals", vs.rod((1.25, hy - 0.8), (2.15, hy - 2.0), 0.14))]
for k in range(5):
    parts.append(("phalanges", vs.rod((1.9 + k * 0.12, hy - 2.2), (1.6 + k * 0.45, hy - 3.6), 0.08)))
a = vs.draw(ax, parts, at=(x, y))
vs.callout(ax, (x + 5.0, y + sac - 2.0), (x + 8.3, y + sac - 1.4), "urostyle")
vs.callout(ax, (x + 6.0, y + sac - 1.0), (x + 8.3, y + sac + 0.6), "long ilium")
vs.callout(ax, (x + 6.2, y + sac + 0.1), (x + 8.3, y + sac + 1.8), "sacral diapophysis")
vs.callout(ax, (x + 2.55, y + 7.85), (x + 0.4, y + 8.9), "radioulna")
vs.callout(ax, (x + 1.7, y + hy + 0.2), (x + 0.3, y + hy + 1.6), "tibiofibula")
vs.callout(ax, (x + 1.5, y + hy - 1.5), (x + 0.2, y + hy - 0.4), "astragalus, calcaneum")
vs.legend(ax, [("centrum", "vertebrae (urostyle outlined)"), ("rib", "ribs"), ("ilium", "ilium"),
               ("scapulocoracoid", "pectoral girdle"), ("humerus", "humerus, femur (stylopod)"),
               ("radius", "radius, tibia (zeugopod)"), ("ulna", "ulna, fibula"), ("carpals", "carpals, tarsals"),
               ("phalanges", "digits")], at=(0.5, 1.4), width=20.0, ncols=3)
