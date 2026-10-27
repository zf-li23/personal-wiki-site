# Clathrin-coated vesicle formation. A: a clathrin triskelion (three heavy chains joined at the hub, each with
# a light chain on its proximal segment, a knee and an N-terminal domain that binds adaptors). B: triskelia
# assemble into a polyhedral lattice of hexagons and exactly 12 pentagons; shown is the 60-triskelion
# 'soccer ball' cage (one triskelion per vertex) around its vesicle. C: budding at the plasma membrane:
# adaptors (AP2) bind cargo and PI(4,5)P2 and recruit clathrin to a flat patch; the lattice curves into a pit;
# dynamin assembles as a helical collar around the neck and constricts it on GTP hydrolysis until the vesicle
# is released; Hsc70 and auxilin then remove the coat.
import wikibio as bio
from wikibio import traffic as T

fig, ax = bio.canvas(22, 9.5)
P = bio.P
bio.panel(ax, "A", (0.2, 9.3))
T.triskelion(ax, (2.6, 6.6), 1.5, angle=10, labels=True)
bio.panel(ax, "B", (6.6, 9.3))
T.cage(ax, (9.0, 6.6), 2.0, kind="clathrin", rotation=(18, 28, 0))
bio.label(ax, (9.0, 4.2), "12 pentagons + 20 hexagons", size="small")
bio.panel(ax, "C", (11.8, 9.3))
names = ("flat coated patch", "coated pit", "deep pit", "dynamin collar")
for k, st in enumerate((0.0, 0.4, 0.68, 0.88)):
    x0 = 12.2 + k * 2.15
    a = T.bud(ax, (x0, 7.6), (x0 + 2.0, 7.6), at=1.0, stage=st, r=0.6, kind="clathrin", side=-1, cargo=3)
    if st > 0.8:
        T.dynamin(ax, a["neck_center"] + (0, -0.1), 2 * a["neck_halfwidth"] + 0.16, rings=2, axis=90)
    bio.label(ax, (x0 + 1.0, 5.4), names[k], size="tiny")
bio.label(ax, (12.2, 8.1), "Extracellular space", size="tiny", ha="left", color=P.muted())
bio.label(ax, (12.2, 4.8), "Cytosol", size="tiny", ha="left", color=P.muted())
# release and uncoating
T.coated_vesicle(ax, (14.0, 2.4), 0.6, kind="clathrin", cargo=3)
bio.arrow(ax, (15.1, 2.4), (16.6, 2.4), kind="process")
bio.label(ax, (15.85, 2.85), "Hsc70 + auxilin\n(ATP)", size="tiny")
T.coated_vesicle(ax, (17.6, 2.4), 0.6, kind=None, cargo=3)
for k in range(3):
    T.triskelion(ax, (19.4 + 0.9 * k, 2.8 - 0.5 * (k % 2)), 0.45, angle=30 * k)
bio.label(ax, (20.3, 1.3), "free triskelia (recycled)", size="tiny")
bio.label(ax, (14.0, 1.2), "released coated vesicle", size="tiny")
