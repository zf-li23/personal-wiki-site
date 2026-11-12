# From fin to limb: the pectoral fin or forelimb skeleton of five taxa in dorsal view, proximal end at the
# bottom, preaxial (radial) side to the left. Bones are coloured in the course-wide homology scheme
# (stylopod blue: humerus; zeugopod: radius and ulna; autopod: carpals/ulnare, metacarpals, phalanges;
# fin radials and dermal fin rays). Simplified after Shubin et al. 2006, Clack 2012 and Pough et al.;
# not to scale.
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P
titles = ["Eusthenopteron", "Panderichthys", "Tiktaalik", "Acanthostega", "Generalized tetrapod"]
subs = ["385 Ma", "380 Ma", "375 Ma", "365 Ma", "pentadactyl limb"]
fig, ax, boxes = vs.panels(5, 5.2, 8.6, titles=titles, subtitles=subs, ncols=5, legend_rows=2, italic=True)


def rays(parts, base_pts, length, n_each=3, spread=0.5):
    """Dermal fin rays fanning out from a distal margin."""
    for (bx, by) in base_pts:
        for j in range(n_each):
            ang = np.radians(90 + (j - (n_each - 1) / 2) * spread * 12)
            parts.append(("fin_rays", vs.rod((bx, by), (bx + length * np.cos(ang) * 0.3, by + length), 0.06)))


def fish_fin(x, y, robust=1.0, wrist=False):
    parts = []
    parts.append(("humerus", vs.rod((2.6, 0.6), (2.6, 2.6), 0.55 * robust, 0.65 * robust)))
    parts.append(("radius", vs.rod((2.25, 2.9), (1.6, 4.3), 0.36 * robust)))
    parts.append(("ulna", vs.rod((2.95, 2.9), (3.2, 4.0), 0.4 * robust)))
    parts.append(("carpals", vs.oval((3.35, 4.45), 0.32, 0.36)))           # ulnare (axial element)
    if wrist:
        parts.append(("carpals", vs.oval((2.55, 4.6), 0.28, 0.28)))        # intermedium
        parts.append(("radials", vs.rod((3.5, 4.9), (3.7, 5.6), 0.22)))
        parts.append(("radials", vs.rod((3.0, 5.0), (2.9, 5.6), 0.2)))
        parts.append(("radials", vs.rod((2.4, 5.0), (2.1, 5.6), 0.2)))
        parts.append(("radials", vs.rod((1.6, 4.6), (1.2, 5.3), 0.2)))
        bases = [(3.75, 5.75), (2.9, 5.75), (2.05, 5.75), (1.15, 5.45)]
    else:
        parts.append(("radials", vs.rod((3.5, 4.85), (3.65, 5.4), 0.2)))
        parts.append(("radials", vs.rod((1.55, 4.55), (1.3, 5.1), 0.2)))
        parts.append(("radials", vs.rod((2.6, 4.2), (2.5, 5.0), 0.2)))
        bases = [(3.7, 5.5), (2.5, 5.15), (1.25, 5.25)]
    rays(parts, bases, 2.2)
    return vs.draw(ax, parts, at=(x, y))


x, y, w, h = boxes[0]
fish_fin(x, y, robust=0.9)
x, y, w, h = boxes[1]
fish_fin(x, y, robust=1.0)
x, y, w, h = boxes[2]
a = fish_fin(x, y, robust=1.15, wrist=True)
vs.callout(ax, a["carpals"], (x + 4.6, y + 3.4), "wrist-like joints")

# Acanthostega: eight digits, carpals unossified (drawn as cartilage)
x, y, w, h = boxes[3]
parts = [("humerus", vs.rod((2.6, 0.6), (2.6, 2.4), 0.75, 0.9)),
         ("radius", vs.rod((2.15, 2.75), (2.0, 4.0), 0.4)),
         ("ulna", vs.rod((3.05, 2.75), (3.25, 3.9), 0.42)),
         ("carpals", vs.oval((2.6, 4.45), 1.15, 0.35), {"state": "cartilage"})]
for k in range(8):
    dx = 1.2 + k * 0.38
    parts.append(("metacarpals", vs.rod((dx, 4.85), (dx + (k - 3.5) * 0.06, 5.6), 0.16)))
    parts.append(("phalanges", vs.rod((dx + (k - 3.5) * 0.06, 5.75), (dx + (k - 3.5) * 0.13, 6.7), 0.14)))
vs.draw(ax, parts, at=(x, y))
bio.label(ax, (x + 2.6, y + 7.4), "8 digits", size="tiny")

# generalized tetrapod: five digits, phalangeal formula 2-3-4-5-4 (simplified to 2-3-3-3-3)
x, y, w, h = boxes[4]
parts = [("humerus", vs.rod((2.6, 0.6), (2.6, 2.6), 0.6, 0.75)),
         ("radius", vs.rod((2.1, 2.95), (1.85, 4.2), 0.34)),
         ("ulna", vs.rod((3.1, 2.95), (3.35, 4.2), 0.36))]
for k, (cx, cy) in enumerate([(1.8, 4.6), (2.4, 4.6), (3.0, 4.6), (3.55, 4.6), (2.1, 5.05), (2.7, 5.05),
                              (3.25, 5.05)]):
    parts.append(("carpals", vs.oval((cx, cy), 0.24, 0.2)))
nph = [2, 3, 3, 3, 3]
for k in range(5):
    dx = 1.5 + k * 0.55
    ang = (k - 2) * 0.12
    parts.append(("metacarpals", vs.rod((dx, 5.4), (dx + ang, 6.1), 0.18)))
    yy = 6.25
    for j in range(nph[k]):
        parts.append(("phalanges", vs.rod((dx + ang * (1 + j * 0.6), yy), (dx + ang * (1.3 + j * 0.6), yy + 0.45),
                                          0.15)))
        yy += 0.6
vs.draw(ax, parts, at=(x, y))
vs.legend(ax, [("humerus", "humerus (stylopod)"), ("radius", "radius"), ("ulna", "ulna"),
               ("carpals", "ulnare, intermedium, carpals"), ("metacarpals", "metacarpals"),
               ("phalanges", "phalanges"), ("radials", "distal radials"), ("fin_rays", "dermal fin rays")],
          at=(0.5, 1.4), width=27.0, ncols=4)
