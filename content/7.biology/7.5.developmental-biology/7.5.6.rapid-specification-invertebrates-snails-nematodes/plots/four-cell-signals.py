"""Cell interactions at the four-cell stage of C. elegans (anterior left, dorsal up). A: P2 signals to its two
neighbours. Its Delta-like ligand APX-1 activates the Notch-like receptor GLP-1 on ABp, which touches P2,
and not on ABa, which does not: the two AB daughters, identical when born, take different fates. Its
Wnt-like signal MOM-2 acts through the Frizzled-like receptor MOM-5 on EMS and polarizes it, so that the
daughter next to P2 (E) forms endoderm and the other (MS) mesoderm. B: the experiment that showed the
second signal (Goldstein, 1992): an EMS cell isolated before the contact has acted makes no gut; recombined
with P2 on either side, it makes gut on the side touching P2."""
import wikibio as bio
from matplotlib.patches import Ellipse
from wikibio import embryology as E

P = bio.P
fig, ax = bio.canvas(22, 9.0)
ec, me, en, gl = E.tok("ectoderm"), E.tok("mesoderm"), E.tok("endoderm"), E.tok("germline")


def cell(xy, rx, ry, t, name, seed=0, face=None):
    o = bio.blob(xy, rx, ry, wobble=0.03, seed=seed, k=8)
    bio.shape(ax, o, t, lw=1.1, zorder=5)
    bio.label(ax, xy, name, size="small", color=P.on_fill())


bio.label(ax, (0.4, 8.6), "A  Four-cell stage", size="small", bold=True, ha="left")
c = (6.0, 4.6)
ax.add_patch(Ellipse(c, 9.4, 5.6, facecolor="none", edgecolor=P.muted(), lw=1.0, ls=(0, (3, 2))))
cell((3.3, 4.7), 1.55, 1.6, ec, "ABa", 1)
cell((6.2, 5.9), 1.6, 1.25, "dna2", "ABp", 2)
cell((6.4, 3.3), 1.5, 1.15, "neutral", "EMS", 3)
cell((8.9, 4.5), 1.15, 1.25, gl, "P2", 4)
bio.arrow(ax, (8.4, 5.4), (7.25, 6.2), kind="activation", lw=1.6)
bio.label(ax, (9.0, 6.7), "APX-1 (Delta) → GLP-1 (Notch)", size="tiny", ha="left")
bio.arrow(ax, (8.3, 3.7), (7.45, 3.1), kind="activation", lw=1.6)
bio.label(ax, (8.6, 2.6), "MOM-2 (Wnt) → MOM-5 (Frizzled)", size="tiny", ha="left")
bio.label(ax, (1.3, 2.3), "no contact with P2:\nABa fate", size="tiny", color=P.muted())
bio.label(ax, (1.5, 7.6), "anterior", size="tiny", color=P.muted())
bio.label(ax, (10.8, 7.6), "posterior", size="tiny", color=P.muted())

bio.label(ax, (13.2, 8.6), "B  EMS with and without P2", size="small", bold=True, ha="left")
rows = [(6.6, "EMS alone", None), (3.6, "EMS + P2", "right"), (0.9, "EMS + P2 on the other side", "left")]
for y, name, side in rows:
    bio.label(ax, (13.2, y + 0.9), name, size="tiny", ha="left", color=P.muted())
    cell((14.6, y), 0.75, 0.6, "neutral", "EMS", 5)
    if side == "right":
        cell((15.9, y), 0.5, 0.5, gl, "P2", 6)
    if side == "left":
        cell((13.3, y), 0.5, 0.5, gl, "P2", 6)
    bio.arrow(ax, (16.6, y), (17.6, y), kind="process", head=0.18)
    if side is None:
        cell((18.6, y), 0.55, 0.5, me, "MS", 7)
        cell((19.8, y), 0.55, 0.5, me, "MS", 8)
        bio.label(ax, (21.0, y), "no gut", size="tiny", ha="left")
    else:
        a, b = ((me, "MS"), (en, "E")) if side == "right" else ((en, "E"), (me, "MS"))
        cell((18.6, y), 0.55, 0.5, a[0], a[1], 7)
        cell((19.8, y), 0.55, 0.5, b[0], b[1], 8)
        bio.label(ax, (21.0, y), "gut next\nto P2", size="tiny", ha="left")
