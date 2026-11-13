# The skeleton of a pigeon in left lateral view, anterior to the left, wing folded (schematic, after
# Kardong 2019, Proctor and Lynch 1993 and Pough et al. 2023), with the fusions and other features related
# to flight labelled: the fused braincase and toothless beak; the flexible neck of heterocoelous cervical
# vertebrae; the notarium (fused thoracic vertebrae); the synsacrum (lumbar, sacral and some caudal
# vertebrae fused with the ilium); the pygostyle; ribs with uncinate processes; the keeled sternum; the
# strut-like coracoid, scapula and furcula (fused clavicles); the carpometacarpus; the tibiotarsus and
# tarsometatarsus. Bones in the course-wide homology colours; vertebrae drawn as a simplified chain.
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P
fig, ax = bio.canvas(24, 15.5)
O = (2.0, 2.0)


def chain(pts, r, key="centrum", state="bone"):
    pts = np.asarray(pts)
    t = np.linspace(0, 1, len(pts))
    out = []
    for i in range(len(pts)):
        out.append((key, vs.oval(tuple(pts[i]), r, r * 0.8), {"state": state}))
    return out


neck = [(4.2 + 2.4 * u, 9.0 + 0.4 * u - 1.5 * np.sin(np.pi * u)) for u in np.linspace(0.04, 0.96, 14)]
parts = []
# skull
parts += [("premaxilla", vs.poly([(-0.2, 9.5), (1.6, 10.1), (2.2, 9.6), (1.6, 9.45)])),
          ("maxilla", vs.poly([(1.6, 9.45), (2.2, 9.6), (2.4, 9.3), (1.4, 9.3)])),
          ("dentary", vs.poly([(0.0, 9.35), (2.6, 9.05), (2.8, 9.2), (1.4, 9.3)])),
          ("frontal", vs.smooth([(2.2, 9.6), (2.8, 10.6), (3.8, 11.0), (4.6, 10.6), (4.4, 9.8), (3.4, 9.4)])),
          ("quadrate", vs.rod((3.9, 9.6), (3.7, 9.1), 0.18)),
          ("jugal", vs.rod((2.3, 9.25), (3.7, 9.15), 0.12))]
parts += chain(neck, 0.24)
# trunk: notarium, synsacrum, free caudals, pygostyle
back = [(7.0 + 0.62 * i, 9.5 - 0.06 * i) for i in range(5)]
parts += chain(back, 0.3)
parts += [("ilium", vs.poly([(10.0, 9.7), (14.2, 9.5), (14.5, 8.5), (12.0, 8.2), (10.1, 8.9)])),
          ("ischium", vs.poly([(12.0, 8.2), (14.5, 8.5), (14.3, 7.5), (12.6, 7.6)])),
          ("pubis", vs.rod((12.0, 7.9), (15.2, 6.9), 0.12))]
parts += chain([(14.8 + 0.42 * i, 9.2 + 0.1 * i) for i in range(4)], 0.2)
parts += [("centrum", vs.poly([(16.4, 9.4), (17.6, 10.4), (17.4, 9.2)]), {"text": ""})]
# ribs, uncinate processes, sternum with keel
for i, x in enumerate(np.linspace(7.2, 9.8, 5)):
    parts.append(("rib", vs.rod((x, 9.2), (x + 0.4, 7.4), 0.13)))
    parts.append(("rib", vs.rod((x + 0.4, 7.4), (x - 0.1, 5.9), 0.13)))
    parts.append(("rib", vs.rod((x + 0.3, 8.1), (x + 0.95, 8.2), 0.08)))
parts += [("sternum", vs.poly([(6.4, 5.9), (11.6, 5.5), (11.0, 5.0), (6.6, 5.3)])),
          ("sternum", vs.poly([(6.6, 5.3), (11.0, 5.0), (9.6, 3.6), (7.0, 3.3)]), {"state": "highlight"})]
# pectoral girdle
parts += [("coracoid", vs.rod((6.6, 8.6), (6.6, 5.7), 0.32)),
          ("scapula", vs.rod((6.8, 8.8), (10.8, 9.0), 0.22, 0.12)),
          ("clavicle", vs.rod((6.3, 8.5), (5.9, 6.4), 0.12)),
          ("clavicle", vs.rod((5.9, 6.4), (6.4, 5.9), 0.12))]
# folded wing
parts += [("humerus", vs.rod((6.9, 8.6), (10.0, 7.6), 0.32)),
          ("ulna", vs.rod((10.0, 7.6), (6.8, 7.2), 0.24)),
          ("radius", vs.rod((9.9, 7.85), (6.9, 7.5), 0.14)),
          ("carpals", vs.oval((6.6, 7.35), 0.22, 0.22)),
          ("metacarpals", vs.poly([(6.4, 7.5), (11.2, 7.0), (11.3, 6.8), (6.4, 7.15)])),
          ("phalanges", vs.rod((11.2, 6.9), (13.0, 6.7), 0.14))]
# hindlimb
parts += [("femur", vs.rod((12.0, 8.3), (10.6, 6.4), 0.32)),
          ("tibia", vs.rod((10.6, 6.4), (12.6, 3.2), 0.28)),
          ("fibula", vs.rod((10.9, 6.2), (11.6, 5.0), 0.1)),
          ("metatarsals", vs.rod((12.6, 3.2), (11.9, 1.0), 0.24)),
          ("phalanges", vs.rod((11.9, 1.0), (9.8, 0.8), 0.12)),
          ("phalanges", vs.rod((11.9, 1.0), (13.5, 0.9), 0.12))]
a = vs.draw(ax, parts, at=O)
orb = np.array(vs.oval((O[0] + 3.4, O[1] + 10.1), 0.42, 0.38))
ax.fill(orb[:, 0], orb[:, 1], color=P.surface(), zorder=40)
X = lambda x, y: (O[0] + x, O[1] + y)  # noqa: E731
L = [((0.8, 9.75), (0.3, 12.6), "toothless beak (rhamphotheca on premaxilla)"),
     ((3.8, 10.6), (3.6, 13.2), "braincase: bones fused"),
     ((4.8, 8.0), (0.3, 10.8), "neck: 14 heterocoelous vertebrae"),
     ((7.6, 9.4), (6.5, 12.8), "notarium (fused thoracic vertebrae)"),
     ((12.4, 9.1), (11.8, 12.2), "synsacrum (fused with ilium)"),
     ((17.0, 9.8), (18.2, 11.6), "pygostyle"),
     ((8.95, 8.15), (19.5, 9.0), "uncinate process"),
     ((8.4, 4.2), (0.3, 3.2), "keel (carina) of sternum"),
     ((6.6, 7.6), (0.3, 6.0), "coracoid strut"),
     ((5.95, 6.6), (0.3, 7.4), "furcula (fused clavicles)"),
     ((9.0, 7.15), (19.5, 6.8), "carpometacarpus"),
     ((11.6, 4.8), (19.5, 4.8), "tibiotarsus"),
     ((12.25, 2.1), (19.5, 2.4), "tarsometatarsus"),
     ((13.6, 7.2), (19.5, 7.9), "pubis directed backward")]
for p0, p1, txt in L:
    bio.callout(ax, X(*p0), X(*p1), txt, size="tiny")
