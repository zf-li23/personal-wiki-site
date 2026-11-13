# Serial and historical homology of tetrapod limbs (schematic). A: forelimb and hindlimb of a generalized
# early tetrapod in dorsal view, proximal end at the top, preaxial side (radius, tibia, digit I) on the left;
# each element is coloured by its serial homologue in the course-wide vertskel scheme (humerus = femur,
# radius = tibia, ulna = fibula, carpals = tarsals, metacarpals = metatarsals, phalanges). B: forelimbs of a
# human, a bat, a bird and a toothed whale drawn with the same colours (wikibio zoomorph.forelimb).
# Not to scale.
import wikibio as bio
import vertskel as vs
from wikibio import zoomorph as zm

P = bio.P
fig, ax = bio.canvas(26, 11.5)


def limb(x0, y0, keys, labels):
    """A pentadactyl limb: stylopod, two zeugopod bones, two carpal rows, five rays."""
    sty, pre, post, mid, meta, phal = keys
    parts = [(sty, vs.rod((2.5, 9.6), (2.5, 6.9), 0.7, 0.55)),
             (pre, vs.rod((2.05, 6.55), (1.75, 4.95), 0.42)),
             (post, vs.rod((2.95, 6.55), (3.25, 4.95), 0.46))]
    for j in range(3):
        parts.append((mid, vs.oval((1.6 + 0.9 * j, 4.5), 0.38, 0.27)))
    for j in range(5):
        parts.append((mid, vs.oval((0.95 + 0.78 * j, 3.85), 0.32, 0.24)))
    nph = [2, 3, 4, 5, 4]
    for j in range(5):
        x = 0.95 + 0.78 * j - (2 - j) * 0.08
        parts.append((meta, vs.rod((x, 3.45), (x - (2 - j) * 0.1, 2.45), 0.24)))
        y = 2.3
        for k in range(nph[j] - 1):
            ln = 0.48 - 0.05 * k
            parts.append((phal, vs.rod((x - (2 - j) * 0.12, y), (x - (2 - j) * 0.14, y - ln), 0.2)))
            y -= ln + 0.12
    a = vs.draw(ax, parts, at=(x0, y0))
    lx = x0 + 4.6
    for key, lab, yy in zip(keys, labels, (8.3, 5.9, 5.4, 4.2, 2.9, 1.5)):
        vs.callout(ax, a[key], (lx, y0 + yy), lab)
    return a


limb(0.4, 0.6, ("humerus", "radius", "ulna", "carpals", "metacarpals", "phalanges"),
     ("humerus", "radius", "ulna", "carpals", "metacarpals", "phalanges"))
bio.label(ax, (3.0, 10.9), "Forelimb", size="small", bold=True)
limb(7.6, 0.6, ("femur", "tibia", "fibula", "tarsals", "metatarsals", "phalanges"),
     ("femur", "tibia", "fibula", "tarsals", "metatarsals", "phalanges"))
bio.label(ax, (10.2, 10.9), "Hindlimb", size="small", bold=True)
bio.panel(ax, "A", (0.2, 11.2))

bio.panel(ax, "B", (14.0, 11.2))
for i, (taxon, name) in enumerate((("human", "Human"), ("bat", "Bat"), ("bird", "Bird"), ("whale", "Toothed whale"))):
    x = 15.4 + i * 2.95
    zm.forelimb(ax, (x, 5.4), 8.4, taxon=taxon, width=2.5)
    bio.label(ax, (x, 10.9), name, size="small", bold=True)
