# The lower jaw and jaw joint along the synapsid lineage, left lateral view, anterior to the left
# (schematic, after Kemp 2005, Kardong 2019, Luo 2007 and Pough et al. 2023; not to scale, jaws drawn to the
# same length). The tooth-bearing dentary enlarges and forms a tall coronoid process for the temporalis
# muscle, while the postdentary bones (surangular, angular with its reflected lamina, articular) become
# smaller and are concentrated near the jaw joint. In Morganucodon a new joint between the dentary condyle
# and the squamosal works beside the old articular-quadrate joint. In crown mammals the lower jaw is the
# dentary alone; the articular (malleus), quadrate (incus) and angular (tympanic ring) form the middle ear
# with the stapes. Bones in the course-wide homology colours.
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P
titles = ["Dimetrodon", "Gorgonopsian", "Thrinaxodon", "Probainognathus", "Morganucodon", "Didelphis (opossum)"]
subs = ["sphenacodontid, 290 Ma", "therapsid, 260 Ma", "cynodont, 250 Ma", "probainognathian, 230 Ma",
        "mammaliaform, 205 Ma", "crown mammal"]
fig, ax, boxes = vs.panels(6, 8.0, 5.0, titles=titles, subtitles=subs, ncols=3, legend_rows=2, italic=False,
                           gap=0.8)
# dentary fraction of jaw length, coronoid height, postdentary height, reflected lamina
SPEC = [(0.62, 0.3, 0.75, 0.0), (0.72, 0.9, 0.6, 0.5), (0.82, 1.6, 0.45, 0.45), (0.9, 2.0, 0.3, 0.3),
        (0.95, 2.2, 0.18, 0.15), (1.0, 2.3, 0.0, 0.0)]
L, H, Y0 = 7.0, 0.9, 1.4


def jaw(x, y, f, cor, ph, refl, i):
    xd = 0.4 + L * f
    parts = [("squamosal", vs.poly([(5.6, 3.6), (7.8, 3.6), (7.8, 2.6), (6.2, 2.4)]), {"state": "context"})]
    dent = [(0.4, Y0), (0.6, Y0 + H), (xd - 2.2, Y0 + H), (xd - 1.3, Y0 + H + cor),
            (xd - 0.7, Y0 + H + cor * 0.85), (xd - 0.4, Y0 + H), (xd, Y0 + 0.6), (xd - 0.6, Y0 - 0.2),
            (2.0, Y0 - 0.25)]
    if f >= 0.95:
        dent[5:7] = [(xd - 0.1, Y0 + 1.0), (xd + 0.25, Y0 + 1.15), (xd + 0.1, Y0 + 0.8), (xd, Y0 + 0.5)]
    parts.append(("dentary", vs.poly(dent)))
    if ph > 0:
        xa = 0.4 + L * f - 0.5
        parts.append(("surangular", vs.poly([(xa, Y0 + 0.7), (7.3, Y0 + 0.6), (7.3, Y0 + 0.6 - ph * 0.5), (xa, Y0 + 0.3)])))
        parts.append(("angular", vs.poly([(xa, Y0 + 0.3), (7.3, Y0 + 0.6 - ph * 0.5), (7.0, Y0 + 0.6 - ph), (xa + 0.3, Y0 - 0.1)])))
        if refl > 0:
            parts.append(("angular", vs.oval((xa + 0.9, Y0 - 0.1 - refl * 0.4), 0.45 * refl + 0.2, 0.35 * refl + 0.1)))
        parts.append(("articular", vs.oval((7.45, Y0 + 0.6 - ph * 0.25), 0.28, 0.22 + ph * 0.15)))
        parts.append(("quadrate", vs.poly([(7.15, Y0 + 0.85), (7.75, Y0 + 0.85), (7.6, 2.6), (7.3, 2.6)])))
        parts.append(("stapes", vs.rod((7.5, 2.0), (8.4, 2.35), 0.12)))
    else:
        parts.append(("malleus", vs.oval((7.2, 1.6), 0.25, 0.32)))
        parts.append(("incus", vs.oval((7.55, 1.95), 0.2, 0.18)))
        parts.append(("stapes", vs.rod((7.7, 1.95), (8.2, 1.85), 0.1)))
        t = np.radians(np.linspace(0, 360, 60))
        parts.append(("tympanic", np.c_[7.05 + 0.55 * np.cos(t), 1.4 + 0.6 * np.sin(t)].tolist(), {"state": "lost"}))
    a = vs.draw(ax, parts, at=(x, y))
    return a


for i, (x, y, w, h) in enumerate(boxes):
    a = jaw(x, y, *SPEC[i], i)
    if i == 4:
        vs.callout(ax, (x + 7.0, y + Y0 + 1.15), (x + 4.0, y + 4.7), "dentary-squamosal joint")
        vs.callout(ax, (x + 7.45, y + Y0 + 0.6), (x + 4.6, y + 0.25), "articular-quadrate joint")
    if i == 1:
        vs.callout(ax, (x + 6.1, y + Y0 - 0.3), (x + 3.0, y + 0.1), "reflected lamina of angular")
    if i == 5:
        vs.callout(ax, (x + 7.2, y + 1.6), (x + 3.6, y + 0.2), "middle ear: malleus, incus, stapes, tympanic")
    if i == 2:
        vs.callout(ax, (x + 5.6, y + Y0 + H + 0.9), (x + 2.0, y + 4.4), "coronoid process")
vs.legend(ax, ["dentary", ("surangular", "surangular"), ("angular", "angular / tympanic"),
               ("articular", "articular / malleus"), ("quadrate", "quadrate / incus"), ("stapes", "stapes"),
               ("squamosal", "squamosal (skull)", "context")], at=(0.4, 2 * 0.55 + 0.25), width=24.0, ncols=4)
